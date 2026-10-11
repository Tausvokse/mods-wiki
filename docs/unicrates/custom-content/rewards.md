# Reward reference

Rewards live in a crate's `rewards` array. Each entry needs a unique nonblank `id`, a recognized `type`, and a finite nonnegative `weight`. The entire crate needs positive finite total weight. Weight 0 allows an entry to be referenced by a milestone while excluding it from normal random selection.

## Types and dependencies

| Type | Delivered result | Requirements |
| --- | --- | --- |
| `item` | Registered item(s), with supported customization | Item exists on server |
| `cobblemon_item` | Registered Cobblemon item(s) | Cobblemon installed |
| `cobblemon_pokemon` | Pokémon placed in party or PC | Cobblemon installed; valid species/form |
| `cobblemon_egg` | Pokémon created with egg aspect/state and placed in party or PC | Cobblemon installed; version-specific egg hooks |
| `command` | Frozen commands executed as server command source | Valid commands from installed server mods |
| `permission` | LuckPerms node, permanent or temporary | LuckPerms installed |
| `economy` | Deposit through registered provider | Economy integration enabled and provider registered |
| `experience` | XP levels or points | Positive experienceAmount |
| `key` | Physical UniCrates key(s) for a loaded crate | Target crate exists |
| `broadcast_only` | Successful win with no material payout | Configure announcement if desired |

Unavailable reward types are excluded from ordinary candidate pools, changing effective chances. Vanilla item rewards containing `cobblemon:` items are also filtered when Cobblemon item support is unavailable.

`cobblemon_egg` is not a physical egg item. Current creation adds the `egg` aspect and invokes optional `setEgg(true)` / `asEgg()` hooks if present. Actual hatching behavior depends on the installed Cobblemon/egg implementation; this mod does not define a universal hatching timer.

## Shared fields

| Field | Default | Meaning |
| --- | --- | --- |
| `id` | required | Persistent identity; unique within crate |
| `type` | required | Type above |
| `displayName` | unset | Name in preview/GUI/announcements; does **not** rename granted items |
| `icon` | unset | Display icon identifier |
| `displayItem` | unset | Display item override; aliases `displayitem`, `display_item` |
| `displayBlock` | unset | Display block override; aliases `displayblock`, `display_block` |
| `weight` | `0` | Relative probability weight, not percent |
| `rarity` | unset, effectively common | Valid values: `common`, `uncommon`, `rare`, `epic`, `legendary`, `mythic` |
| `requiredPermissions` | `[]` | All nonblank nodes must pass for ordinary candidate selection |
| `deniedPermissions` | `[]` | Any passing node excludes candidate |
| `rerollOnFailure` | `true` | Try alternative rewards after an issuer explicitly reports failure |
| `commands` | `[]` | Primary action for command rewards, bonus commands for other types |
| `limits` | initialized empty limits | See limits below |
| `broadcastOnWin` | disabled object | See announcements below |

Rarity controls display and pity classification. It does not independently multiply normal chances. The base probability is `eligible weight / sum of eligible weights`; use [gameplay probability details](../gameplay/keys-and-rewards).

Keep reward IDs stable. Player lifetime/daily win maps use reward ID alone, while global win maps use crate ID plus reward ID. Reusing one reward ID across crates intentionally or accidentally shares player limits. Prefer distinct IDs such as `starter_diamonds` and `vip_diamonds`.

## Items and bundles

| Field | Default / behavior |
| --- | --- |
| `item` | Item ID; aliases `itemId`, `item_id`, `material`. If blank, usable displayItem is fallback |
| `count` | unset; fixed amount; aliases `itemCount`, `item_count`, `item_amount` |
| `amountMin`, `amountMax` | unset; provide both for inclusive random quantity |
| `amount` | unset; legacy non-economy quantity fallback, rounded to integer |
| `customName` | unset; applied to actual item; aliases `custom_name`, `itemCustomName`, `item_custom_name` |
| `lore` | `[]`; actual item lore lines |
| `customModelData` | unset; alias `custom_model_data` |
| `components` | `{}`; supported subset below |
| `bundledItems` | `[]`; nonempty bundle replaces standalone item payout |

Quantity precedence is positive `amountMin`, then positive `count`, then positive non-economy `amount`, then **1**. `amountMax` is used only when at least the effective minimum; the validator requires min and max together. Counts/min/max must be 1–4096. The issuer also enforces its 4096 ceiling after legacy amount resolution.

Each bundle entry contains `item`, `amount` (default 1), optional `displayName`, `customName`, `lore`, `customModelData`, `components`. Maximum **27 entries**, maximum **4096 total items**. Bundle entry displayName is metadata, not the actual item rename. The complete bundle is checked before inventory mutation. Items are split by actual maximum stack size; overflow drops beside the player when inventory insertion fails.

```json
{
  "id": "starter_supplies",
  "type": "item",
  "displayName": "&aStarter Supplies",
  "weight": 80,
  "rarity": "common",
  "bundledItems": [
    { "item": "minecraft:bread", "amount": 16 },
    { "item": "minecraft:iron_pickaxe", "amount": 1, "customName": "&f%player%'s Pickaxe" }
  ]
}
```

This is a reward object to insert into a crate's rewards array, not a standalone crate file.

### Data component support

Minecraft 1.21.1 uses data components for ItemStack customization. UniCrates' JSON `components` map implements a subset; it is not a generic codec for every Minecraft component.

| Key | Accepted value | Effect |
| --- | --- | --- |
| `minecraft:custom_name` | String | Fallback when customName is null |
| `minecraft:lore` | Array of strings | Fallback when lore is absent/empty |
| `minecraft:custom_model_data` | Number or integer string | Fallback when customModelData is null |
| `minecraft:unbreakable` | Boolean `true` | Set unbreakable component |

Other map entries are not applied by `ItemRewardIssuer`. There is no automatic arbitrary NBT/enchantment/component import. Use valid server commands for customization beyond this subset. `/crate addhand` captures item ID, count, custom name, lore, custom model data and unbreakable, plus a recognized Pokémon spec where available; it is not a complete component clone.

Item customName/lore support `%player%`, `%crate%`, `%crate_id%`. Use strings in the mod's formatting syntax rather than assuming full vanilla JSON text component objects will be decoded.

## Pokémon

Use `pokemon` object or `pokemonSpec` shorthand (aliases `pokemon_spec`, `spec`). An object with species or propertiesString takes priority over the shorthand.

```json
{
  "id": "starter_pikachu",
  "type": "cobblemon_pokemon",
  "displayName": "&ePikachu",
  "weight": 20,
  "rarity": "rare",
  "pokemon": {
    "species": "pikachu",
    "level": 25,
    "shinyChance": 0.01,
    "ivPreset": "random",
    "ballType": "cobblemon:poke_ball"
  }
}
```

| `pokemon` field | Default | Behavior |
| --- | --- | --- |
| `species` | unset | Required at delivery; namespaced or Cobblemon species ID; `random` chooses among implemented species |
| `form` | unset | Valid form-only Showdown ID for species |
| `aspects` | `[]` | Added to parsed properties |
| `level` | unset | Positive explicit value overrides properties string; otherwise parsed value, then level 1 |
| `shiny` | unset | Explicit true/false overrides parsed shiny and shinyChance |
| `shinyChance` | `0.0` | Fractional probability, e.g. 0.01 = 1%; used only without explicit shiny and when >0 |
| `ability`, `nature` | unset | Passed to Cobblemon properties |
| `heldItem` | unset | Held item identifier |
| `ballType` | unset | Explicit capture ball; default when unspecified in properties is `cobblemon:poke_ball` |
| `customNickname` | unset | Literal nickname |
| `ivPreset` | `"random"` | `random`, `perfect`, or six comma-separated integers 0–31 |
| `genderOverride` | unset | Recognized gender override |
| `moves` | `[]` | Added to properties moves |
| `propertiesString` | unset | Parsed first by Cobblemon; explicit object fields then override/extend it |

IV CSV order is **HP, Attack, Defense, Special Attack, Special Defense, Speed**. `perfect` means six 31s. `random` leaves Cobblemon's properties/default generation in control. No dedicated EV field exists in this object; advanced properties require a valid Cobblemon propertiesString.

Shorthand example: `"pokemonSpec": "pikachu level=25 shiny=false"`. Shorthand parsing recognizes level, shiny and form before the integration parses the complete string. Do not combine conflicting shorthand and object values.

The validator does not fully resolve Cobblemon species, moves, abilities, levels or forms at JSON-load time. Unknown species/form can fail at delivery. Validate on a test server running your actual Cobblemon version. The adapter inserts using party storage and reconciles the exact Pokémon UUID in party and PC. A full party can overflow to PC; unavailable storage or ambiguous reconciliation retains a pending reward. Prepared Pokémon data freezes the result for transaction retry rather than rolling fresh IVs/species on each reconnect.

## Commands and bonus commands

```json
{
  "id": "welcome_command",
  "type": "command",
  "displayName": "&bWelcome Gift",
  "displayItem": "minecraft:diamond",
  "weight": 10,
  "rarity": "rare",
  "commands": [
    "give %player% minecraft:diamond 2",
    "[delay=40] tellraw %player% {\"text\":\"Enjoy your gift!\"}"
  ]
}
```

A leading `/` is stripped. `[delay=<ticks>]` at the start schedules delayed dispatch; 20 ticks is approximately one second at normal tick rate. Commands run as a server command source at the frozen dimension and position, not with the winner as the executor. Use `%player%` / `%player_uuid%` instead of assuming `@s` means the winner.

Both `%name%` and `{name}` forms are supported for: `player`, `player_uuid`, `crate`, `crate_id`, `reward`, `reward_id`, `rarity`, `world`, `x`, `y`, `z`, `amount`, `permission`. Pokémon object rewards also expose `pokemon`, `form`, `level`, `shiny`. Coordinates are the player's block coordinates when prepared. Pokémon placeholders are configuration values, not a certified snapshot of the final delivered random Pokémon. Amount for ranged items is the configured effective minimum, not the randomly delivered count.

Commands are resolved and frozen before dispatch. Later config edits do not replace an existing frozen batch. Runtime limits: 1024 entries, 32768 UTF-8 bytes per command, 1 MiB per frozen batch. A successful command callback acknowledges the outbox; failed/no-callback commands remain pending. A crash between external command effect and acknowledgement can replay an effect. Write repeat-safe commands where possible and use [pending review](../configuration/storage#pending-transactions-and-administrator-recovery) for ambiguous outcomes.

## Other payouts

| Type | Fields | Details |
| --- | --- | --- |
| `permission` | `permission`, `durationSeconds` | Nonblank node required. Unset/nonpositive duration grants permanent node; positive duration freezes absolute expiry in seconds. LuckPerms user save is awaited |
| `economy` | `amount` | Finite positive deposit through provider; amount is not an item count. An uncertain deposit is retained for review rather than automatically repeated |
| `experience` | `experienceAmount`, `experienceIsLevels` | Positive integer; boolean default false means XP points, true means levels |
| `key` | `item`, quantity fields | Here item is **target crate ID**, not key ID or Minecraft item ID. Blank uses current crate. Payout is physical keys, maximum stack 16, even for a virtual-key crate |
| `broadcast_only` | `broadcastOnWin` | No material reward; counts as successful win |

For virtual key rewards, use a command reward such as `crate key give %player% starter 2 virtual`. The target crate must already be loaded. Review command replay considerations before using commands for balances.

## Win limits and fallbacks

| `limits` field | Default | Meaning |
| --- | --- | --- |
| `maxGlobalWins` | unset | Positive server-wide limit for crate/reward identity; includes reserved openings |
| `maxPlayerWins` | unset | Positive player lifetime limit by reward ID |
| `maxPerPlayerPerDay` | unset | Positive daily limit by reward ID; resets at UTC midnight |
| `fallbackRewardId` | unset | Substitute another reward in the same crate when exhausted |
| `hideWhenExhausted` | `false` | Visibility hint used by server fallback preview; companion preview is based on configured rows |

Unset/nonpositive numeric limits are not enforced by the exhaustion checks. Fallback cannot reference itself. A missing/denied/unavailable/exhausted fallback excludes that slot. A usable fallback inherits the **original slot's weight**; if it also has its own eligible slot, probabilities add together. There is no recursive fallback chain traversal.

Aliases supported: `max_global_wins`, `globalWinLimit`, `global_win_limit`; `max_player_wins`, `maxPerPlayerLifetime`, `max_per_player_lifetime`; `max_per_player_per_day`; `fallback_reward_id`, `fallbackReward`, `fallback_reward`; `hide_when_exhausted`.

```json
"limits": {
  "maxGlobalWins": 100,
  "maxPlayerWins": 1,
  "maxPerPlayerPerDay": 1,
  "fallbackRewardId": "starter_supplies",
  "hideWhenExhausted": true
}
```

This fragment belongs inside a reward object. Removing a limit does not remove its saved counters. There is no reset-limits command. Global persistence remains file-backed even with SQL player storage.

## Announcements and failure handling

`broadcastOnWin.enabled` defaults false, `message` is unset, `scope` defaults `global`. Scopes: `global`, `nearby`, `player`. Templates replace `%player%`, `%crate%`, `%reward%`, `%rarity%` and brace equivalents. An unset message uses the standard win message. Discord is configured independently in [discord.yml](../configuration/discord).

Ordinary failure reroll is not another weighted draw: delivery shuffles alternative positive-weight rewards, checks their availability/permissions/limits, and tries them in that order. An exception or uncertain transaction is not a confirmed failure and can keep the original pending state. If no alternative succeeds, the reward stays pending. Primary confirmation can precede a later milestone failure; preserve pending records rather than manually erasing them.

Source: `RewardConfig`, `RewardType`, `RewardRngEngine`, `RewardIssuers`, `ItemRewardIssuer`, `KeyRewardIssuer`, `CommandRewardIssuer`, `PermissionRewardIssuer`, `EconomyRewardIssuer`, `ExperienceRewardIssuer`, `CobblemonIntegration`, `RewardDelivery`, `PreparedCommandBatch`.
