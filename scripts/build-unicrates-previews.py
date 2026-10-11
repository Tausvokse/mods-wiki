"""Build wiki GIFs from accepted recordings in the parent UniCrates checkout.

No Minecraft scenes are re-recorded. Frame timestamps are normalized using the
recorder metadata before making small GIF previews and still-image posters.
Run from the combined checkout: python wiki/scripts/build-unicrates-previews.py
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import shutil
import subprocess
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"
PUBLIC = WIKI / "docs/public/UniCrates/animations"
DATA = WIKI / "docs/.vitepress/theme/data/unicrates-previews.json"
FFMPEG = ROOT / "video-output/hyperframes/runtime/node_modules/ffmpeg-static/ffmpeg.exe"
COVERAGE = ROOT / ".buildcache/animation-polish-final-coverage-20261010.json"
NORMALIZER = ROOT / "video-output/scripts/normalize-minecraft-recordings.py"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()

def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def run(*args):
    result = subprocess.run([str(FFMPEG), "-hide_banner", "-loglevel", "error", "-y", *map(str, args)], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"FFmpeg exit {result.returncode}: {result.stderr}")

def category(identity):
    if identity == "astral_reveal": return "Master Singularity"
    if identity in ("charizard_rift", "pikachu_electric", "gengar_shadow", "articuno_frost"): return "Pokémon scenes"
    if identity == "interactive_pokeball": return "Interactive selection"
    if identity == "csgo_roulette_gui": return "GUI roulette"
    return "Themed timelines" if identity.endswith("_timeline") else "Effect timelines"

def main():
    coverage = read(COVERAGE)
    assert coverage["passed"] and len(coverage["openings"]) == 59
    spec = importlib.util.spec_from_file_location("native_normalize", NORMALIZER)
    normalizer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(normalizer)
    PUBLIC.mkdir(parents=True, exist_ok=True)
    DATA.parent.mkdir(parents=True, exist_ok=True)
    entries = []
    manifest = []
    for identity, supplied in sorted(coverage["openings"].items()):
        if identity == "astral_reveal":
            cohort, index = "master-roulette-hotfix-item-r2-20261011", 1000
            acceptance = read(ROOT / ".buildcache" / cohort / "evidence.json")
            assert acceptance["passed"] and acceptance["acceptancePassed"]
            proof = ROOT / ".buildcache" / cohort / "client-runtime/qa-evidence/case-1000-cleanup.json"
            name = "Master Singularity"
            recorded = "2026-10-11"
        else:
            cohort, index = supplied["cohort"], supplied["index"]
            proof = Path(supplied["proof"])
            assert sha(proof) == supplied["sha256"]
            name = supplied["displayName"]
            recorded = "2026-10-10"
        actual = read(proof)
        assert actual["opening"] == identity and actual["entitiesAbsent"]
        assert "qa_" not in actual.get("displayName", "").lower()
        metadata = ROOT / "video-output/animation-polish" / cohort / "recordings" / f"case-{index:04d}-{identity}-capture.json"
        normal = normalizer.normalize(metadata)
        movie = Path(normal["output"])
        gif, poster = PUBLIC / f"{identity}.gif", PUBLIC / f"{identity}.webp"
        metadata_sha = sha(metadata)
        checkpoint = PUBLIC / f".{identity}.checkpoint.json"
        previous = read(checkpoint) if checkpoint.exists() else {}
        fresh = previous.get("metadataSha256") == metadata_sha and gif.exists() and poster.exists() and previous.get("gifSha256") == sha(gif) and previous.get("posterSha256") == sha(poster)
        if not fresh:
            if identity == "astral_reveal":
                shutil.copy2(ROOT / "video-output/master-roulette-hotfix-20261011/Master-Singularity-Final.gif", gif)
            else:
                run("-i", movie, "-filter_complex", "[0:v]fps=15,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=3", "-loop", "0", gif)
            run("-ss", "2.5", "-i", movie, "-frames:v", "1", "-vf", "scale=480:-1:flags=lanczos", "-quality", "82", poster)
            checkpoint.write_text(json.dumps({"metadataSha256": metadata_sha, "gifSha256": sha(gif), "posterSha256": sha(poster)}), encoding="utf-8")
        with Image.open(gif) as image:
            frames, width, height = image.n_frames, image.width, image.height
            assert frames >= 60 and width in (480, 960) and height == width * 9 // 16
            duration = 0
            for frame in range(frames):
                image.seek(frame)
                duration += image.info.get("duration", 0)
        entry = {"id": identity, "name": name, "category": category(identity), "recordedOn": recorded, "gif": f"/UniCrates/animations/{identity}.gif", "poster": f"/UniCrates/animations/{identity}.webp"}
        entries.append(entry)
        manifest.append({**entry, "gifSha256": sha(gif), "posterSha256": sha(poster), "sourceRecordingSha256": sha(movie), "captureMetadataSha256": metadata_sha, "acceptedProofSha256": sha(proof), "frames": frames, "width": width, "height": height, "gifDurationSeconds": duration / 1000, "gifBytes": gif.stat().st_size, "sourceFrames": normal["inputCapturedFrames"], "sourceFramesAdded": normal["framesAdded"], "sourceFramesRemoved": normal["framesRemoved"]})
        print(f"WIKI_PREVIEW {len(entries)}/59 {identity} frames={frames} bytes={gif.stat().st_size}", flush=True)
    entries.sort(key=lambda row: (0 if row["id"] == "astral_reveal" else 1, row["category"], row["name"]))
    DATA.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (PUBLIC / "manifest.json").write_text(json.dumps({"count": len(entries), "source": "Accepted recorded gameplay; current Master hotfix plus previous bundled-opening recordings.", "entries": manifest}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # Checkpoints are private build intermediates, not files served by the wiki.
    for checkpoint in PUBLIC.glob(".*.checkpoint.json"):
        checkpoint.unlink()
    print(f"WIKI_GALLERY_DONE openings={len(entries)} totalGifBytes={sum(row['gifBytes'] for row in manifest)}", flush=True)

if __name__ == "__main__":
    main()
