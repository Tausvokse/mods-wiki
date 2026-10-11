# JSON recipes and validation

These examples target the current UniCrates 2.3 schema. Complete examples can be saved directly as crate files. Section fragments are labeled and must be inserted into an existing crate object.

## Smallest practical crate

Save as `config/unicrates/crates/starter.json`, then `/crate reload`.

```json
{
  "id": "starter",
  "displayName": "&aStarter Crate",
  "key": {
    "id": "starter_key",
    "displayName": "&aStarter Key",
    "keyMode": "PHYSICAL"
  },
  "opening": {
    "openingType": "instant",
    "cooldownSeconds": 2
  },
  "animation": { "type": "particle_vortex" },
  "rewards": [
    {
      "id": "starter_bread",
      "type": "item",
      "displayName": "&fBread x16",
      "item": "minecraft:bread",
      "count": 16,
      "weight": 80,
      "rarity": "common"
    },
    {
      "id": "starter_diamonds",
      "type": "item",
      "displayName": "&bDiamonds x2",
      "item": "minecraft:diamond",
      "count": 2,
      "weight": 20,
      "rarity": "rare"
    }
  ]
}
```

The appearance section is omitted intentionally: initialized defaults supply it. This crate has 80% bread and 20% diamonds before eligibility/pity changes. Instant opening pays out without relying on a particular world-animation timeline. `animation.type` still exists because crate validation requires it.

Test as an administrator:

```text
/crate create starter
/crate key give Alex starter 3 physical
/crate preview starter
```

Then open with Alex holding a key in the main hand. Test economy/cooldown behavior using a non-OP survival account.

## Virtual crate with XP cost, limits and milestone

Save as `config/unicrates/crates/veteran.json`.

```json
{
  "id": "veteran",
  "displayName": "&6Veteran Crate",
  "key": {
    "id": "veteran_key",
    "displayName": "&6Veteran Key",
    "keyMode": "VIRTUAL",
    "virtualKeyId": "veteran"
  },
  "opening": { "openingType": "strip", "cooldownSeconds": 5 },
  "animation": { "type": "particle_vortex", "durationTicks": 100 },
  "costs": { "enabled": true, "experienceLevels": 2 },
  "milestones": [
    { "openings": 10, "rewardId": "veteran_bonus", "repeatEvery": false }
  ],
  "rewards": [
    {
      "id": "veteran_iron",
      "type": "item",
      "item": "minecraft:iron_ingot",
      "count": 8,
      "weight": 90,
      "rarity": "common"
    },
    {
      "id": "veteran_diamond",
      "type": "item",
      "item": "minecraft:diamond",
      "count": 1,
      "weight": 10,
      "rarity": "rare",
      "limits": { "maxPlayerWins": 1, "fallbackRewardId": "veteran_iron" }
    },
    {
      "id": "veteran_bonus",
      "type": "item",
      "displayName": "&6Ten-opening Bonus",
      "item": "minecraft:gold_ingot",
      "count": 16,
      "weight": 0,
      "rarity": "epic"
    }
  ]
}
```

Grant virtual keys with `/crate key give Alex veteran 10 virtual`. Two XP levels are required in addition to a key. The zero-weight bonus is only referenced by the milestone. The first diamond win exhausts its lifetime slot for that player; afterward its weight substitutes iron. Keep reward IDs and milestone ordering stable on a live server.

## Several keys: section fragment

Replace/add this section in a complete crate:

```json
"keyRequirements": {
  "enabled": true,
  "mode": "ALL",
  "requirements": [
    { "keyId": "starter", "amount": 2, "type": "VIRTUAL" },
    { "keyId": "veteran_key", "amount": 1, "type": "PHYSICAL" }
  ]
}
```

The first keyId is a virtual ledger ID; the second is a physical component ID. They are not necessarily the same as crate IDs. `ANY` at the outer mode means the first affordable alternative in list order, while type ANY permits mixing virtual and physical quantities for one entry.

## Selection: section fragment

```json
"opening": { "openingType": "selectable", "cooldownSeconds": 5 },
"selective": { "enabled": true, "amountToPick": 2, "poolSize": 4 }
```

Use a complete crate with at least two eligible distinct choices and enough content to fill the desired pool. A paid opening counts once, even if two rewards are claimed. Claims are server-authoritative; the card is marked Claimed only after confirmation. See [gameplay](../gameplay/).

## Common validation failures

| Error | Correction |
| --- | --- |
| ID differs from filename | `starter.json` must contain `"id": "starter"` |
| Missing displayName/key.id | Supply nonblank strings |
| Missing animation.type | Keep a nonblank animation type even for instant mode |
| Empty rewards / nonpositive total weight | Include at least one positive-weight reward |
| Duplicate reward ID | Give each entry a distinct stable ID within crate |
| Invalid rarity | Use lowercase common, uncommon, rare, epic, legendary or mythic |
| Invalid display mode | Use item_display, block_display or vanilla_block; this validation does not guarantee different rendering implementations |
| Unsupported opening type | Use an actual supported mode; arbitrary scene_ prefix passes schema but still needs implemented runtime support |
| Invalid quantity range | Supply both amountMin and amountMax, each 1–4096, min ≤ max |
| Oversized bundle | At most 27 entries and 4096 total items |
| Missing milestone target | rewardId must exist in rewards |
| Empty enabled key requirements | Supply at least one positive-amount entry with keyId |
| Invalid selection count | amountToPick >0; poolSize ≥ amountToPick |
| Invalid scale/hologram | Finite positive scale ≤50; ≤32 lines, ≤4096 UTF-16 units per template, offsets -100..100 |
| Invalid IV preset | random, perfect, or exactly six CSV values 0–31 |
| Invalid custom model path | Safe resources/... JSON path and file-backed customModelData in 1000–16777214 |

Validation covers schema/semantic bounds, not every installed registry/dependency capability. Unknown items or invalid Cobblemon species/forms can reach runtime delivery and fail there. A load-success message is not proof that every reward can be issued.

JSON has no comments or trailing commas. Unknown fields can be ignored by Gson: a misspelled setting may appear to load but do nothing. Prefer [crate fields](../configuration/crate-reference) and [reward fields](./rewards) over copied historical examples.

Source: `CrateConfig`, `RewardConfig`, `CrateConfigValidator`, `ConfigManager`, `LinkedCrateInteractHandler`.
