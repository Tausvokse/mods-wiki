# How to Create a Crate

Welcome to the comprehensive guide on creating a new crate in **UniCrates**! This tutorial will walk you through the process of writing a `crates/&lt;name&gt;.json` configuration file, explaining every aspect of its structure.

By the end of this guide, you will understand how to:
- Set up the base crate structure.
- Customize its appearance and holograms.
- Configure its key (physical or virtual).
- Define how it opens.
- Add varied and weighted rewards (including Pokémon!).

> [!NOTE]
> All crate configuration files must be placed in `config/unicrates/crates/` and have a `.json` extension.

---

## 1. Base Structure

Every crate needs a unique identifier and basic metadata.

```json
{
  "configVersion": 1,
  "id": "my_epic_crate",
  "displayName": "&5&lEpic Crate",
  "lore": [
    "&7Contains epic loot!",
    "&7Open with an Epic Key."
  ]
}
```

- **`configVersion`**: Keep this as `1` for now.
- **`id`**: Must be unique, lower-case, and use underscores instead of spaces.
- **`displayName`**: The name of the crate, supporting formatting codes (`&`).
- **`lore`**: A list of strings displayed when previewing the crate in GUIs.

---

## 2. Appearance

The `appearance` block controls what the crate looks like in the world.

```json
  "appearance": {
    "displayMode": "item_display",
    "vanillaBlockFallback": "minecraft:chest",
    "glowEffect": true,
    "floatingRotation": false,
    "scale": 1.2,
    "builtinModel": "epic",
    "guiTheme": "dark",
    "hologram": {
      "enabled": true,
      "heightOffset": 1.8,
      "lines": [
        "&5&l[%crate%&5&l]",
        "&7(&dRight-click &fto open&7)"
      ]
    }
  }
```

### Key Appearance Fields:
- **`displayMode`**: Usually `"item_display"`.
- **`builtinModel`**: One of the mod's bundled 3D rigs: `"common"`, `"rare"`, `"epic"`, `"legendary"`. Leave blank if you use `customItemModel` for your own resource pack model.
- **`scale`**: Multiplier for the 3D model size.
- **`glowEffect`**: Set to `true` to make the model emit light/glow.
- **`hologram`**: Floating text above the crate block. You can use placeholders like `%crate%` and `%key%`.

---

## 3. Configuring the Key

The `key` section determines what is required to open the crate.

```json
  "key": {
    "id": "epic_key",
    "displayName": "&5Epic Key",
    "consumeOnOpen": true,
    "virtualKey": false,
    "acceptedKeyIds": ["epic_key", "master_key"],
    "keyModel": "epic"
  }
```

- **`virtualKey`**: If `true`, the key is tracked virtually per player. If `false`, it's a physical item.
- **`consumeOnOpen`**: Set to `true` to take the key from the player upon opening.
- **`acceptedKeyIds`**: A list of valid key IDs that can open this crate.
- **`keyModel`**: Uses one of the bundled key rig models (e.g., `"epic"`).

---

## 4. Opening Mechanism

The `opening` block determines how players interact with the crate and what animation plays.

```json
  "opening": {
    "trigger": "right_click",
    "openingType": "roulette",
    "cooldownSeconds": 5,
    "requireEmptyHandOrKeyOnly": false,
    "bulkOpenAllowed": true,
    "bulkOpenOptions": [1, 5, 10, "all"]
  }
```

### Opening Types (`openingType`)
UniCrates supports several UI and animation types:
- **`roulette`**: A CS:GO style scrolling GUI.
- **`strip`**: A linear scrolling animation.
- **`reels`**: A slot-machine style animation.
- **`wheel`**: A spinning wheel.
- **`selectable`**: Allows the player to pick from hidden options.
- **`instant`**: No UI, grants rewards immediately.
- **`world_animation`**: Plays a physical world animation instead of a GUI.

> [!TIP]
> If you enable `bulkOpenAllowed`, you can define options in `bulkOpenOptions` like `[1, 5, 10, "all"]` to allow players to open multiple crates at once!

---

## 5. Adding Rewards

Rewards are configured in the `rewards` array. Each reward has a **`weight`** which determines its chance to be picked relative to other rewards. 

### Common Fields:
- **`id`**: A unique ID for the reward.
- **`type`**: The kind of reward (`item`, `command`, `cobblemon_pokemon`, etc.).
- **`weight`**: Higher numbers mean a higher chance to win. (e.g., `100` is much more common than `1`).
- **`rarity`**: Usually matches your theme (`common`, `rare`, `epic`, `legendary`).

### Example: Item Reward
```json
{
  "id": "diamond_reward",
  "type": "item",
  "displayName": "&bDiamonds",
  "item": "minecraft:diamond",
  "amountMin": 1,
  "amountMax": 5,
  "weight": 50,
  "rarity": "rare"
}
```

### Example: Command Reward
```json
{
  "id": "money_reward",
  "type": "command",
  "displayName": "&a$1000",
  "commands": [
    "eco give %player% 1000"
  ],
  "weight": 30,
  "rarity": "rare"
}
```

### Example: Pokémon Reward (Cobblemon)
```json
{
  "id": "shiny_charizard",
  "type": "cobblemon_pokemon",
  "displayName": "&6Shiny Charizard",
  "weight": 1,
  "rarity": "legendary",
  "pokemon": {
    "species": "charizard",
    "level": 50,
    "shiny": true,
    "ivPreset": "perfect",
    "ballType": "cobblemon:ultra_ball"
  }
}
```

---

## 6. Complete Example

Here is a full, copy-pasteable JSON configuration for our `epic_crate`. Save this as `config/unicrates/crates/epic_crate.json`.

```json
{
  "configVersion": 1,
  "id": "epic_crate",
  "displayName": "&5&lEpic Crate",
  "lore": [
    "&7Contains epic loot!",
    "&7Open with an Epic Key."
  ],
  "appearance": {
    "displayMode": "item_display",
    "vanillaBlockFallback": "minecraft:chest",
    "glowEffect": true,
    "scale": 1.2,
    "builtinModel": "epic",
    "guiTheme": "dark",
    "hologram": {
      "enabled": true,
      "heightOffset": 1.8,
      "lines": [
        "&5&l[%crate%&5&l]",
        "&7(&dRight-click &fto open&7)"
      ]
    }
  },
  "key": {
    "id": "epic_key",
    "displayName": "&5Epic Key",
    "consumeOnOpen": true,
    "virtualKey": false,
    "acceptedKeyIds": ["epic_key"],
    "keyModel": "epic"
  },
  "opening": {
    "trigger": "right_click",
    "openingType": "roulette",
    "cooldownSeconds": 2,
    "bulkOpenAllowed": true,
    "bulkOpenOptions": [1, 5, "all"]
  },
  "animation": {
    "type": "particle_vortex",
    "durationTicks": 100
  },
  "rewards": [
    {
      "id": "diamond_reward",
      "type": "item",
      "displayName": "&bDiamonds",
      "item": "minecraft:diamond",
      "amountMin": 3,
      "amountMax": 10,
      "weight": 100,
      "rarity": "common"
    },
    {
      "id": "money_reward",
      "type": "command",
      "displayName": "&a$5000",
      "commands": [
        "eco give %player% 5000"
      ],
      "weight": 50,
      "rarity": "rare"
    },
    {
      "id": "shiny_charizard",
      "type": "cobblemon_pokemon",
      "displayName": "&6Shiny Charizard",
      "pokemon": {
        "species": "charizard",
        "level": 50,
        "shiny": true,
        "ivPreset": "perfect"
      },
      "weight": 5,
      "rarity": "legendary",
      "broadcastOnWin": {
        "enabled": true,
        "message": "&6%player% just unboxed a Shiny Charizard from the Epic Crate!"
      }
    }
  ]
}
```
