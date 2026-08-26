# Configuration Overview

UniCrates configuration consists of a primary main-config.json and a directory of JSON configurations for crates and custom animations. They are managed through plain JSON files.

## Main Config (config/unicrates/main-config.json)

Controls global plugin/mod settings.

### General
* configVersion (int, default: 1): The version of the config format.
* general.debugMode (boolean, default: true): Toggles debug logging and features.
* general.autoGenerateResourcePack (boolean, default: true): Determines if the mod generates a resource pack on reload.
* general.requireClientMod (boolean, default: true): Whether players require the client-side mod.

### Integrations
* integrations.luckperms.enabled (boolean, default: true): Enables LuckPerms support.
* integrations.cobblemon.enabled (boolean, default: true): Enables Cobblemon integrations.
* integrations.economy.enabled (boolean, default: false): Enables economy rewards.

### Animations
* nimations.defaultAnimation (String, default: "particle_vortex")
* nimations.allowPerCrateOverride (boolean, default: true)
* nimations.maxConcurrentAnimationsPerServer (int, default: 40)

### Storage
* storage.backend (String, default: "flatfile"): Options: "flatfile", "sqlite", "mysql".

### Pity System
* pitySystem.enabled (boolean, default: false)
* pitySystem.guaranteedMinimumRarity (String, default: "rare")
* pitySystem.guaranteedAfterOpens (int, default: 50)

## Crate Config (config/unicrates/crates/&lt;name&gt;.json)

Controls individual crate configuration.

See the Custom Content section for more details on Crates and Rewards JSON schemas.
