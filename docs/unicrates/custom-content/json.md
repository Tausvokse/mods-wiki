# JSON Formats Audit Report

This document details all user-editable JSON configuration models found in the UniCrates project.

## 1. MainConfig (config/unicrates/main-config.json)

Controls global plugin/mod settings.

### Schema
* configVersion (int): Version of the config schema. Default: 1.
* general (object)
  * debugMode (boolean). Default: true
  * autoGenerateResourcePack (boolean). Default: true
  * requireClientMod (boolean). Default: true
  * checkForUpdates (boolean). Default: true
* integrations (object)
  * luckperms.enabled (boolean). Default: true
  * luckperms.fallbackToOpIfMissing (boolean). Default: true
  * cobblemon.enabled (boolean). Default: true
  * economy.enabled (boolean). Default: false
* animations (object)
  * defaultAnimation (string). Default: particle_vortex
  * allowPerCrateOverride (boolean). Default: true
* storage (object)
  * backend (string). Options: flatfile, sqlite, mysql. Default: flatfile
* pitySystem (object)
  * enabled (boolean). Default: false
  * guaranteedMinimumRarity (string). Default: rare
  * guaranteedAfterOpens (int). Default: 50

---

## 2. CrateConfig (config/unicrates/crates/&lt;name&gt;.json)

Controls individual crate configuration.

### Schema
* configVersion (int): Default 1
* id (string): Unique identifier for the crate.
* displayName (string): Display name.
* lore (List&lt;string&gt;): Lore lines.
* appearance (object)
  * displayMode (string). Default: item_display
  * vanillaBlockFallback (string). Default: minecraft:chest
  * builtinModel (string, optional): common, rare, epic, legendary
* key (object)
  * id (string)
  * consumeOnOpen (boolean). Default: true
  * virtualKey (boolean). Default: false
* opening (object)
  * trigger (string). Default: right_click
  * cooldownSeconds (int). Default: 0
  * openingType (string): roulette, strip, reels, wheel, selectable, instant, world_animation. Default: strip
* animation (object)
  * type (string). Default: particle_vortex
  * durationTicks (int). Default: 100
* preview (object)
  * enabled (boolean). Default: true
* restrictions (object)
  * maxOpensPerPlayer (int, optional)
* rewards (List&lt;object&gt;)

---

## 3. RewardConfig (inside CrateConfig -> rewards[])

Defines possible rewards from a crate.

### Schema
* id (string)
* type (string): item, cobblemon_item, command, permission, economy, experience, cobblemon_pokemon, cobblemon_egg
* displayName (string)
* icon (string)
* weight (double)
* rarity (string)
* limits (object)
  * maxPerPlayerPerDay (int, optional)
  * maxPerPlayerLifetime (int, optional)
  * globalWinLimit (int, optional)
* broadcastOnWin (object)
  * enabled (boolean). Default: false

**Type-Specific Fields:**
* **Item**: item (string), amountMin (int), amountMax (int)
* **Command**: commands (List&lt;string&gt;)
* **Permission**: permission (string), durationSeconds (long)
* **Economy**: amount (double)
* **Experience**: experienceAmount (int), experienceIsLevels (boolean)
* **Pokemon**: pokemon (object)
