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

### Web Editor
* webEditor.enabled (boolean, default: true): Enables `/crates editor` and `/crates apply <hash>`.
* webEditor.editorUrl (String, default: "https://unicrates.net/editor/"): Web UI client location.
* webEditor.relayUrl (String, default: "https://unicrates-relay.workers.dev/"): Cloudflare Worker + KV payload relay service URL.

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
avatar_url_template: "https://mc-heads.net/avatar/{player}/100"
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

---

## Cinematic Orbit Camera Splines (`animation.cinematicCamera`)

UniCrates includes a cinematic orbit camera spline system (Idea 12) that delivers esports-grade showcase presentation:

* **Automatic Rarity Trigger**: Automatically engages for **Legendary** or **Mythic** reward drops, or on crates configured with `"cinematicCamera": true`.
* **Smooth Orbit Curve**: The camera smoothly orbits around the reward focus using an ease-in-out Catmull-Rom spline:
  $$\theta(t) = \theta_0 + 2\pi \cdot (3t^2 - 2t^3)$$
* **Combat & Survival Failsafe**: Taking damage from mobs, fire, or hazards immediately aborts the cinematic view and restores normal player perspective. Movement keys (`WASD`, `Jump`, `Sneak`) also allow the player to instantly cancel the camera.
* **Crate Config Fields**:
  * `animation.cinematicCamera` (`boolean`, default: `false`): Enables orbit camera for this crate.
  * `animation.cinematicRadius` (`float`, default: `2.8`): Orbit distance in blocks.
  * `animation.cinematicHeight` (`float`, default: `1.8`): Camera elevation above the anchor.

---

## Animation Timeline Management (`/crates editor`)

Administrators can configure and customize crate animations in the browser via the Web Editor:

* **Command**: `/crates editor` (requires OP-2 permissions).
* **Features**:
  * **Timeline Selection**: Choose from 47 cinematic pre-built timelines.
  * **Cooldowns & Duration**: Configure per-crate opening duration and cooldowns.
  * **Cinematic Orbit Camera**: Enable 360-degree dynamic orbit camera on crate reveal.
  * **Camera Lock**: Prevent unwanted player movement during opening.
  * **Instant Cloud Sync**: Save in browser and apply immediately on server with `/crates apply <hash>`.


