# Updating an existing UniCrates server

Replacing the server JAR does **not** replace existing JSON animation definitions. UniCrates installs bundled defaults only while `config/unicrates/.defaults-installed` is absent, and preserves existing files even then. Do not delete your configuration or marker to perform an upgrade.

## Before the upgrade

1. Stop the Minecraft server cleanly. Close old Web Editor sessions.
2. Back up the entire world and `config/unicrates`. If using MySQL, also take a database backup. Preserve the exact previous server JAR outside `mods`.
3. Select the new **server JAR for the same loader**. Keep exactly one UniCrates server JAR in `mods`. Replace client companions on clients when instructed by the release.

## Refresh bundled JSON animations safely

The release utility `upgrade-bundled-animations.py` needs Python 3.10 or newer and uses only the standard library. Run it outside Minecraft. Start with a read-only preview:

```powershell
python upgrade-bundled-animations.py --config "D:\MinecraftServer\config\unicrates" --old-jar "D:\Backups\unicrates-previous-server.jar" --new-jar "D:\Release\unicrates-fabric-2.3-server.jar"
```

Then apply the reviewed plan while the server is stopped:

```powershell
python upgrade-bundled-animations.py --config "D:\MinecraftServer\config\unicrates" --old-jar "D:\Backups\unicrates-previous-server.jar" --new-jar "D:\Release\unicrates-fabric-2.3-server.jar" --apply --server-stopped
```

On Linux use `python3` and your server paths. For NeoForge use its server JAR.

The comparison uses parsed JSON, so whitespace and object-key ordering alone do not count as customization:

| Result | Behavior |
| --- | --- |
| `update` | Existing JSON matches the old JAR default; replace with new default. |
| `install` | Default filename is absent; install the new definition. This also restores intentionally removed bundled files: review the preview first. |
| `unchanged` | Existing JSON already matches the new default; leave it alone. |
| `preserve-custom` | Existing JSON differs from the old default, is invalid, or has no old baseline; preserve it. |

If you no longer have the exact old JAR, omit `--old-jar`. Existing differing definitions will all be preserved; missing bundled definitions will still be installed. Using an unrelated old JAR can misclassify your files: use the exact previously deployed artifact.

Unknown custom filenames are untouched. The utility never edits crate rewards, keys, player data, database settings, `.defaults-installed`, resource packs or language files. It does not migrate settings or rename animation IDs.

Before writing active files, it creates `config/unicrates/.animation-upgrades/<timestamp>/` with `originals/`, `incoming/` and `report.json`. Every existing bundled candidate is backed up. For each `preserve-custom` result, compare your active definition against its new version in `incoming/`; merge changes manually or save the new definition under a unique filename **and unique animation `id`**. Duplicate IDs are not a valid side-by-side setup.

The utility replaces each active file atomically and records completed writes. A power interruption may leave a partially applied batch; the prepared report and complete originals remain available. Keep the server stopped until you review or restore it.

## Manual alternative and rollback

Without Python, open the new JAR as a ZIP and inspect `unicrates_defaults/animations/`. Back up the current animation folder, compare definitions, and copy only known unmodified defaults or explicitly reviewed custom merges. Do not bulk-overwrite customized files. Code-based animation controllers are updated through the JAR; they are not JSON files in this directory.

For rollback, stop the server. Restore both the old server/client JARs and your full configuration backup together. A full world/database backup is required if gameplay already changed persistent state. For an animation-only rollback before any gameplay, copy backed-up `originals/<filename>` over each completed update. For a completed `install` with `before_sha256: null`, remove that newly installed file. Use `report.json` to identify affected files; if interruption occurred between a write and progress recording, compare active SHA256 against `new_sha256` as well. Do not copy `incoming/` into the active folder wholesale.

## Start and validate

Start the server and review the UniCrates startup log for invalid animation definitions. Open representative crates and verify rewards, labels and models. Open a fresh Web Editor session. Run `/crates reload` after subsequent manual JSON edits, and resolve any reported errors before exposing the server to players.

## Egg reward limitation

`cobblemon_egg` creates a Pokémon with the `egg` aspect and invokes optional Cobblemon methods `setEgg(true)` / `asEgg()` if exposed by the installed version. It is placed into party or PC through the Pokémon reward path; UniCrates does not create a universal physical egg item or implement a hatching timer. An egg aspect alone does not prove hatching support. Use `cobblemon_pokemon` unless your exact Cobblemon/egg extension combination has been tested, and do not advertise guaranteed hatching based only on successful delivery.
