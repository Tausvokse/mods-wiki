# Configuration

UniCrates 2.3 reads server-owned JSON files from `config/unicrates/`. Players do not define rewards or change server probabilities through client settings.

| Location | Purpose |
| --- | --- |
| `main-config.json` | Global settings and storage destination |
| `crates/<id>.json` | One crate definition, keys, access rules, costs and rewards |
| `animations/<id>.json` | Custom animation timelines |
| `resources/` | Uploaded/custom model and texture assets |
| `lang/en_us.json` | Server message templates |
| `discord.yml` | Discord webhook routing and announcement filters |
| `data/` | Player records, global win reservations and migration information |
| `generated-resourcepack/` | Resource pack generated during reload when enabled |
| `exported-resourcepack/` | Resource pack exported by `/crate exportpack` |
| `.backups/` | Configuration snapshots created before editor apply |
| `.staging/` | Configuration transaction staging |
| `.defaults-installed` | Marker preventing repeated installation of bundled crate/timeline examples |

Read the [main configuration reference](./main-config), [crate field reference](./crate-reference), [reward reference](../custom-content/rewards), [storage and recovery guide](./storage), and [Discord guide](./discord). Appearance and animation details are explained in [models](../custom-content/models) and [animations](../custom-content/animations).

## Editing and reload behavior

Save complete JSON objects with double-quoted names and strings. Keep the filename and crate `id` identical. Run `/crate reload` and read every error. Reload constructs a registry from successfully loaded files: an invalid crate file is omitted from the new live registry. An invalid manual edit does not preserve the previous live definition.

Web editor apply validates its payload and uses a staged configuration transaction with backup/rollback support. It differs from manually saving broken JSON and reloading. Configuration backups cover `crates/`, `animations/` and `resources/`; they do not replace backups of player data, the world or external economy data.

Storage selection and economy provider registration happen at startup. Restart after changing those settings. Reload reads the settings file but does not construct a new data store or register a new provider.

Defaults in this reference are Java model defaults for omitted fields, not a guarantee that bundled examples use them. Explicit `null` differs from omission: avoid null sections. Some modeled settings have no active runtime consumer in this version; their references identify this limitation.

Source: `ConfigManager`, `MainConfig`, `CrateConfig`, `CrateConfigValidator`, `UniCrates`.
