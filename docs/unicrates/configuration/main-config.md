# Main configuration reference

File: `config/unicrates/main-config.json`. First start writes the defaults from `MainConfig`. Omitted fields retain Java defaults. Use non-null sections when editing a generated file.

## General and integrations

| Field | Default | Effective behavior in 2.3 |
| --- | --- | --- |
| `configVersion` | `1` | Format metadata; not the mod version |
| `general.debugMode` | `true` | Debug configuration flag |
| `general.autoGenerateResourcePack` | `true` | Assemble `generated-resourcepack/` on reload |
| `general.requireClientMod` | `true` | Stored setting; no runtime read enforcing client installation was found |
| `general.checkForUpdates` | `true` | Stored setting; no update-check consumer was found |
| `integrations.luckperms.enabled` | `true` | Consult LuckPerms when installed and available |
| `integrations.luckperms.fallbackToOpIfMissing` | `true` | OP level 2 fallback when LuckPerms is unavailable; see [permissions](../administration/permissions) for the separate admin fallback |
| `integrations.cobblemon.enabled` | `true` | Controls version-warning check; reward availability checks the installed mod |
| `integrations.cobblemon.requiredVersion` | `"1.7.3"` | Version compared for warning; does not download Cobblemon |
| `integrations.cobblemon.warnOnVersionMismatch` | `true` | Log mismatched installed version when the check is enabled |
| `integrations.economy.enabled` | `false` | Required for economy reward availability |
| `integrations.economy.provider` | `"vault"` | Bundled startup registration exists for `"impactor"`; `"vault"` does not create a built-in Vault bridge |

Economy operations require a registered `EconomyProvider`. The bundled adapter targets Impactor and uses its default currency. `vault` or `none` does not install a provider. An external integration can register the interface. For the bundled path, install compatible Impactor, enable the integration, select `impactor`, restart and confirm registration in the server log.

```json
{
  "integrations": {
    "economy": { "enabled": true, "provider": "impactor" }
  },
  "storage": { "backend": "flatfile" }
}
```

## Animation settings

| Field | Default | Meaning |
| --- | --- | --- |
| `animations.defaultAnimation` | `"particle_vortex"` | Global animation selection |
| `animations.allowPerCrateOverride` | `true` | Let crate animation configuration override global selection |
| `animations.broadcastAnimationToNearbyPlayers` | `true` | Nearby animation broadcast setting |
| `animations.animationRadiusBlocks` | `12` | Broadcast radius in blocks |
| `animations.maxConcurrentAnimationsPerServer` | `40` | Animation manager admission limit |
| `animations.companionMode` | `"AUTO_FALLBACK"` | Pokémon scene policy: `AUTO_FALLBACK`, `REQUIRE_COMPANION`, `FORCE_VANILLA` |
| `animations.enablePokemonCinematics` | `true` | Enable Pokémon cinematic path |

Read [animations](../custom-content/animations) before choosing a companion policy. Availability depends on handshake capabilities and the selected opening.

## Block and cooldown fields

These fields exist in `MainConfig` but have no runtime reads in the current source. Changing them does not configure mining, drops or opening cooldowns.

| Field | Stored default |
| --- | --- |
| `blocks.crateHardness` | `3.0` |
| `blocks.crateBlastResistance` | `6.0` |
| `blocks.crateLightLevel` | `0` |
| `blocks.requireSilkTouchToBreak` | `true` |
| `blocks.dropsCrateItemOnBreak` | `true` |
| `cooldowns.defaultOpenCooldownSeconds` | `2` |
| `cooldowns.perCrateCooldownOverrideAllowed` | `true` |

The active cooldown comes from each crate's `opening.cooldownSeconds`, whose omitted-field default is **0 seconds**. Set it explicitly for crates that need a cooldown.

## Pity and logging

| Field | Default | Meaning |
| --- | --- | --- |
| `pitySystem.enabled` | `false` | Enable per-player, per-crate pity counter |
| `pitySystem.guaranteedMinimumRarity` | `"rare"` | Minimum guarantee tier; unrecognized values fall back to rare |
| `pitySystem.guaranteedAfterOpens` | `50` | Consecutive misses before guarantee; nonpositive disables it |
| `logging.logRewardWinsToConsole` | `true` | Console reward wins |
| `logging.logRewardWinsToFile` | `true` | Asynchronous log at `logs/unicrates/rewards.log` |

A natural win at or above the minimum tier resets pity. At the threshold, only currently eligible rewards of that tier or higher are considered. If none exist, the engine rolls normally and retains the advancing counter. Pity cannot manufacture an unavailable reward or override an exhausted limit. See [keys and rewards](../gameplay/keys-and-rewards).

## Storage

| Field | Default |
| --- | --- |
| `storage.backend` | `"flatfile"` |
| `storage.sqlite.file` | `"data/unicrates.db"` |
| `storage.mysql.host` | `""` |
| `storage.mysql.port` | `3306` |
| `storage.mysql.database` | `""` |
| `storage.mysql.user` | `""` |
| `storage.mysql.password` | `""` |
| `storage.mysql.useSsl` | `false` |

Accepted names are `flatfile`, `sqlite`, `mysql`; `mariadb` uses the MySQL JDBC path. Relative SQLite paths resolve under `config/unicrates/`. Read [storage and recovery](./storage) before switching: destination markers prevent reusing obsolete player JSON.

## Web editor

| Field | Default |
| --- | --- |
| `webEditor.enabled` | `true` |
| `webEditor.editorUrl` | `"https://unicrates-cloud-relay.tausvokse.workers.dev/#/"` |
| `webEditor.relayUrl` | `"https://unicrates-cloud-relay.tausvokse.workers.dev/"` |
| `webEditor.bytebinUrl` | `null`, deprecated fallback |

These are defaults encoded in source, not a promise of service uptime. URL helpers replace blank and recognized obsolete placeholders (`unicrates.net`, `taushop.me`, `parhom137`, `unicrates-relay.workers.dev`) with the unified Worker default. Relay selection tries valid `relayUrl`, then `bytebinUrl`, then the default; URLs containing `bytebin` are rejected by that helper. The editor URL is normalized to a trailing hash route. See [web editor workflow](../custom-content/create).

Source: `MainConfig`; consumers in `ConfigManager`, `UniCrates`, `AnimationManager`, loader entrypoints and `PermissionChecker`.
