# UniCrates Rewards System Guide

Welcome to the UniCrates Rewards System Guide! This document explains how the reward pool works, how to configure different types of rewards (including items and Cobblemon), and how to set up limits and broadcasts.

## How the Reward Pool Works

UniCrates uses a **weighted probability system** to determine which rewards players receive when they open a crate. Instead of setting fixed percentage chances, each reward is assigned a `weight`.

**How it calculates:**
1. The system adds up the `weight` of all rewards configured for a given crate to get the total weight.
2. The probability of obtaining any specific reward is its weight divided by the total weight.

For example, if you have three rewards with weights 10, 30, and 60 (totaling 100), the first reward has a 10% chance, the second 30%, and the third 60%. If you add a new reward with a weight of 100, the total weight becomes 200, and the new reward has a 50% chance (100/200) to be selected.

---

## Reward Limits

You can control how frequently players can win a specific reward using the `limits` object. This is perfect for ultra-rare jackpots or daily limits.

- `maxPerPlayerPerDay`: The maximum number of times a single player can win this reward in a single day.
- `maxPerPlayerLifetime`: The maximum number of times a single player can win this reward ever.
- `globalWinLimit`: The maximum number of times this reward can be won across the entire server.

**Example:**
```json
"limits": {
  "maxPerPlayerPerDay": 1,
  "maxPerPlayerLifetime": 5,
  "globalWinLimit": 100
}
```

---

## Win Broadcasts

You can announce to the server when a player wins a specific reward using the `broadcastOnWin` object.

- `enabled`: Set to `true` to enable broadcasts.
- `message`: The message to broadcast.
- `scope`: The audience of the broadcast. Options are:
  - `"global"` (default): Broadcasts to the entire server.
  - `"nearby"`: Broadcasts only to players near the crate.
  - `"player"`: Sends a private message to the player who won.

**Example:**
```json
"broadcastOnWin": {
  "enabled": true,
  "message": "{player} just won a Legendary Item from a crate!",
  "scope": "global"
}
```

---

## Configuring Rewards: JSON Examples

Every reward entry goes into the `rewards` array of a crate configuration file. Below are examples of how to configure different `RewardType`s.

### 1. Item Reward (`item`)

You can specify a single item or bundle multiple items. You can also configure NBT data using `components`.

**Basic Item Example:**
```json
{
  "id": "diamonds",
  "type": "item",
  "item": "minecraft:diamond",
  "amountMin": 1,
  "amountMax": 5,
  "weight": 50,
  "rarity": "uncommon"
}
```

**Advanced Item with Components (NBT) & Bundled Items:**
```json
{
  "id": "starter_kit",
  "type": "item",
  "weight": 10,
  "rarity": "rare",
  "bundledItems": [
    {
      "item": "minecraft:iron_sword",
      "amount": 1,
      "displayName": "Starter Sword",
      "lore": ["A trusty blade."],
      "components": {
        "minecraft:enchantments": {
          "minecraft:sharpness": 1
        }
      }
    },
    {
      "item": "minecraft:bread",
      "amount": 16
    }
  ]
}
```

### 2. Cobblemon Pokémon Reward (`cobblemon_pokemon`)

Reward players with specific Pokémon. The `pokemon` object provides extensive configuration options.

- `species`: The Pokémon species (e.g., `"pikachu"`).
- `form`: Specific form (e.g., `"alolan"`).
- `shiny`: Set to `true` to guarantee a shiny, `false` to prevent it. Omit to rely on standard rates.
- `shinyChance`: Custom probability for the Pokémon to be shiny (e.g., `0.1` for 10%).
- `ivPreset`: Set to `"random"`, `"perfect"`, or provide a CSV array for 6 specific IVs (e.g., `"31,31,31,31,31,31"`).
- Additional options include: `aspects`, `level`, `ability`, `nature`, `heldItem`, `ballType`, `customNickname`, `genderOverride`, `moves`, and `propertiesString`.

**Example:**
```json
{
  "id": "shiny_charizard",
  "type": "cobblemon_pokemon",
  "weight": 5,
  "rarity": "legendary",
  "pokemon": {
    "species": "charizard",
    "level": 50,
    "shiny": true,
    "nature": "timid",
    "ivPreset": "perfect",
    "ballType": "cobblemon:ultra_ball",
    "moves": ["flamethrower", "dragon_pulse"]
  },
  "broadcastOnWin": {
    "enabled": true,
    "message": "{player} won a Shiny Charizard!"
  }
}
```

### 3. Cobblemon Egg Reward (`cobblemon_egg`)
Similar to the Pokémon reward, but gives the player an egg that must be hatched.

**Example:**
```json
{
  "id": "eevee_egg",
  "type": "cobblemon_egg",
  "weight": 20,
  "rarity": "rare",
  "pokemon": {
    "species": "eevee",
    "ivPreset": "perfect"
  }
}
```

### 4. Cobblemon Item Reward (`cobblemon_item`)
Awards specific Cobblemon items. This uses the same configuration format as the standard `item` type.

**Example:**
```json
{
  "id": "master_ball",
  "type": "cobblemon_item",
  "item": "cobblemon:master_ball",
  "amountMin": 1,
  "amountMax": 1,
  "weight": 2,
  "rarity": "mythic"
}
```

### 5. Command Reward (`command`)
Executes server commands when won. Use `{player}` as a placeholder for the winner's username.

**Example:**
```json
{
  "id": "heal_player",
  "type": "command",
  "weight": 40,
  "commands": [
    "heal {player}",
    "feed {player}"
  ]
}
```

### 6. Permission Reward (`permission`)
Grants a permission node to the player, optionally for a specific duration.

**Example:**
```json
{
  "id": "fly_perk",
  "type": "permission",
  "weight": 10,
  "permission": "essentials.fly",
  "durationSeconds": 86400
}
```

### 7. Economy Reward (`economy`)
Grants money to the player (requires Vault or a compatible economy plugin).

**Example:**
```json
{
  "id": "cash_prize",
  "type": "economy",
  "weight": 50,
  "amount": 1000.0
}
```

### 8. Experience Reward (`experience`)
Grants standard Minecraft experience points or levels. Set `experienceIsLevels` to true for levels.

**Example:**
```json
{
  "id": "exp_levels",
  "type": "experience",
  "weight": 60,
  "experienceAmount": 30,
  "experienceIsLevels": true
}
```

### 9. Key Reward (`key`)
Awards a crate key to the player, allowing them to open another crate.

**Example:**
```json
{
  "id": "bonus_key",
  "type": "key",
  "item": "unicrates:rare_key",
  "weight": 15
}
```

### 10. Broadcast Only Reward (`broadcast_only`)
A special type of reward that doesn't give any physical item or perk, but just broadcasts a message. Useful for "troll" rewards.

**Example:**
```json
{
  "id": "fake_out",
  "type": "broadcast_only",
  "weight": 5,
  "broadcastOnWin": {
    "enabled": true,
    "message": "{player} won... absolutely nothing!",
    "scope": "global"
  }
}
```
