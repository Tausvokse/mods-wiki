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

## Discord Webhook Integration (`config/unicrates/discord.yml`)

UniCrates supports high-performance, asynchronous Discord announcements with rich embeds. The configuration is stored in a dedicated `config/unicrates/discord.yml` file.

> [!IMPORTANT]
> The very first line of `discord.yml` must strictly be `enabled: true` or `enabled: false`.

### Configuration Fields
* `enabled: <true|false>`: Toggles Discord webhook integration.
* `default_webhook_url`: The primary fallback Discord webhook URL.
* `min_rarity`: Minimum rarity to broadcast (`"common"`, `"uncommon"`, `"rare"`, `"epic"`, `"legendary"`, `"mythic"`).
* `include_player_avatar`: Fetches the player's 3D skin avatar for the embed thumbnail.
* `avatar_url_template`: Avatar API endpoint template (supports `{uuid}` and `{player}`).
* `include_cobblemon_stats`: Formats detailed Pokémon stats (Level, Shiny ✨, Nature, Ability, IVs) in the embed.
* `channels.by_crate`: Map of crate IDs to specific Discord webhook URLs.
* `channels.by_rarity`: Map of rarities (e.g. `mythic`, `legendary`) to specific Discord webhook URLs.

### Example `discord.yml`
```yaml
enabled: true

default_webhook_url: "https://discord.com/api/webhooks/123456789/abcdef..."
min_rarity: "rare"
include_player_avatar: true
avatar_url_template: "https://crafatar.com/avatars/{uuid}?overlay"
include_cobblemon_stats: true

channels:
  by_crate:
    pokeball_interactive_crate: "https://discord.com/api/webhooks/.../crate-announcements"
  by_rarity:
    mythic: "https://discord.com/api/webhooks/.../jackpot"
    legendary: "https://discord.com/api/webhooks/.../jackpot"
```

---

## Interactive 3D Poké Ball Selection (Opening Type)

UniCrates introduces an immersive, hand-only physical roulette mode:

* `opening.openingType: "interactive_pokeball"` or `"interactive_3d"`
* **Hover Scale Interpolation**: Looking at a floating Poké Ball smoothly magnifies its scale (1.0x $\to$ 1.35x) via client GPU transformation interpolation.
* **Hand-Only Click**: Players can only select using `InteractionHand.MAIN_HAND` (no projectile or off-hand bypass).
* **Dissolve Effect**: Non-chosen Poké Balls dissolve into smoke poof particles, while the winning ball erupts in totem particles and level-up sounds.
* **15-Second Fail-Safe**: Automatic auto-claim if the player disconnects, moves away (> 8 blocks), or timer expires.

### Example Crate Configuration
```json
{
  "id": "pokeball_interactive_crate",
  "displayName": "<gradient:#EE1515:#FFFFFF:#222224><b>Interactive Poke Crate</b></gradient>",
  "opening": {
    "openingType": "interactive_pokeball",
    "cooldownSeconds": 0
  },
  "animation": {
    "type": "interactive_pokeball",
    "durationTicks": 300
  },
  "key": {
    "id": "interactive_key",
    "consumeOnOpen": true,
    "displayName": "&e&lInteractive Key"
  }
}
```
