"""Extract closed crate views from accepted gameplay recordings, never mockups."""
from pathlib import Path
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("wiki_previews", Path(__file__).with_name("build-unicrates-previews.py"))
previews = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previews)

def main():
    coverage = previews.read(previews.COVERAGE)
    source = (ROOT / "common/src/main/java/com/unicrates/util/BuiltinModels.java").read_text()
    models = re.findall(r'"([a-z_]+)"', source.split("AVAILABLE_MODELS = List.of(", 1)[1].split(");", 1)[0])
    assert len(models) == 31
    choices = {}
    for opening, row in coverage["openings"].items():
        proof = previews.read(Path(row["proof"]))
        family = proof["family"].removesuffix("_crate")
        if family in models and (family not in choices or opening == family + "_timeline"):
            choices[family] = (opening, row)
    output = ROOT / "wiki/docs/public/UniCrates/models"
    output.mkdir(parents=True, exist_ok=True)
    entries = []
    for index, model in enumerate(models):
        opening, row = choices[model]
        cohort, case = row["cohort"], row["index"]
        if model == "astral_pokeball":
            cohort, case, opening = "master-roulette-hotfix-item-r2-20261011", 1000, "astral_reveal"
        movie = ROOT / "video-output/animation-polish" / cohort / "recordings" / f"case-{case:04d}-{opening}-edit.mp4"
        assert movie.exists()
        target = output / f"{model}-in-game.webp"
        previews.run("-ss", "0.55", "-i", movie, "-frames:v", "1", "-vf", "scale=480:-1:flags=lanczos", "-quality", "85", target)
        entries.append({"id": model, "name": "Master Ball" if model == "astral_pokeball" else model.replace("_", " ").title(), "image": f"/UniCrates/models/{model}-in-game.webp", "keyCustomModelData": index + 1, "previewOpening": opening, "imageSha256": previews.sha(target)})
        print(f"WIKI_MODEL_STILL {model}", flush=True)
    data = ROOT / "wiki/docs/.vitepress/theme/data/unicrates-models.json"
    data.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
    (output / "in-game-manifest.json").write_text(json.dumps({"count": len(entries), "note": "Real closed-crate views with example configured scale, hologram and environment. Key ID refers to matching asset, not a key shown in the screenshot.", "entries": entries}, indent=2) + "\n", encoding="utf-8")
    print("WIKI_MODELS_DONE count=31", flush=True)

if __name__ == "__main__":
    main()
