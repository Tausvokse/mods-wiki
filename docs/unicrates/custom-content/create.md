---
title: Create a Crate
description: A guided workflow from a bundled crate to custom models, keys, and a tested opening.
---

# Create a Crate

Create `festival_crate` with a matching physical key, two item prizes, a bundled opening, and a hologram. Then replace the visuals with your own model if you want a unique design. Use lowercase IDs with letters, digits, underscores, or hyphens; these also meet the model upload and pack assembler rules.

## Route A: use the web editor

1. Run `/crates editor` as an administrator and open the link generated in chat.
2. Select **Create New Crate** and start with the Starter template.
3. In **General & Key**, set ID `festival_crate`, name `&6&lFestival Crate`, `PHYSICAL` key mode, and key name `&eFestival Key`. Review `key.id` in **Raw JSON**: key identity is separate from the rendered item or model.
4. In **3D Appearance**, select **Common** and scale `1.0`. Keep `appearance.idleYOffset` at `0.0` in Raw JSON. This selects the bundled crate and key theme.
5. In **Opening Timeline**, select `common_wooden_timeline`.
6. In **Rewards & Odds**, add four iron ingots with weight `80` and one diamond with weight `20`. Give each entry a unique reward ID.
7. In **Hologram**, use `%crate%` and `&7Key: %key%`. Adjust text height independently of the model and particles.
8. Click **Apply Changes**, then **Save to Server**. Run the new `/crates apply <hash>` command shown by the editor.
9. Place and test the crate using the commands below.

**Apply Changes** commits the form to the browser workspace. It does not write server files. [Web editor](./web-editor) explains the save/apply stages, cancellation, expiry, and concurrent edits.

## Route B: write the JSON file

Save this complete example as `config/unicrates/crates/festival_crate.json`. The filename and `id` must match.

```json
{
  "configVersion": 1,
  "id": "festival_crate",
  "displayName": "&6&lFestival Crate",
  "lore": ["&7A celebration with useful prizes."],
  "appearance": {
    "displayMode": "item_display",
    "builtinModel": "common",
    "scale": 1.0,
    "idleYOffset": 0.0,
    "floatingRotation": false,
    "glowEffect": false,
    "guiTheme": "dark"
  },
  "key": {
    "id": "festival_key",
    "displayName": "&eFestival Key",
    "lore": ["&7Opens the Festival Crate."],
    "keyModel": "common",
    "keyMode": "PHYSICAL",
    "consumeOnOpen": true,
    "acceptedKeyIds": ["festival_key"]
  },
  "opening": {
    "trigger": "right_click",
    "openingType": "world_animation",
    "animationId": "common_wooden_timeline",
    "cooldownSeconds": 2,
    "bulkOpenAllowed": false
  },
  "animation": {
    "type": "timeline",
    "timeline": "common_wooden_timeline",
    "durationTicks": 100,
    "visibleToNearbyPlayers": true,
    "cameraLock": false
  },
  "particles": {
    "enabled": true,
    "type": "spiral",
    "particle": "minecraft:happy_villager",
    "speed": 1.0,
    "radius": 1.2,
    "count": 2,
    "heightOffset": 0.0
  },
  "hologram": {
    "enabled": true,
    "heightOffset": 1.8,
    "lineSpacing": 0.28,
    "lines": ["%crate%", "&7Key: %key%"]
  },
  "rewards": [
    {
      "id": "iron",
      "type": "item",
      "displayName": "&fFour Iron Ingots",
      "item": "minecraft:iron_ingot",
      "count": 4,
      "weight": 80,
      "rarity": "common"
    },
    {
      "id": "diamond",
      "type": "item",
      "displayName": "&bA Diamond",
      "item": "minecraft:diamond",
      "count": 1,
      "weight": 20,
      "rarity": "rare"
    }
  ]
}
```

With both rewards eligible and no modifiers or pity adjustment, their base chances are `80%` and `20%`. Weights are relative numbers; they do not need to total 100. [Rewards](./rewards) explains how availability, permissions, limits, and modifiers change the live pool.

Run `/crate reload` and resolve reported validation errors before placing it.

## Place it and give a test key

Look at the block that should host the crate and run:

```text
/crate create festival_crate
```

Alternatively, give yourself a portable anchor and place it:

```text
/crate give @s festival_crate
```

Give yourself a physical key for this crate:

```text
/crate key give @s festival_crate 1 physical
```

Use a player name instead of `@s` in the server console. See [commands and permissions](../administration/commands) for the full command reference.

Right-click with the key to test opening and delivery. Check preview with an empty hand or sneak-right-click according to your configuration. Confirm the prize count, key consumption, cooldown, hologram restoration, and model placement after opening.

## Replace the model and physical key

Keep the rewards and key identity. Replace the `appearance` section with:

```json
{
  "displayMode": "item_display",
  "customItemModel": "resources/models/festival_crate.json",
  "customModelData": 1200,
  "scale": 1.0,
  "idleYOffset": 0.0,
  "floatingRotation": false,
  "guiTheme": "dark"
}
```

Follow [model import](./model-import) to create this Java model and resolve its textures. Add these two fields to the existing `key` section for a custom physical key:

```json
{
  "customItemModel": "resources/models/keys/festival_crate.json",
  "customModelData": 1200
}
```

Crate and key Custom Model Data are separate ranges on separate base items. Both can use `1200`, but two custom crate models cannot share a crate value, and two custom key models cannot share a key value.

Export and install the [resource pack](./resource-packs). A single imported model does not automatically acquire the built-in hinged lid animation. Add reward displays, sounds, movement, and particles through a [custom timeline](./animations).

## Choose the next layer

| Change | Field or workflow |
| --- | --- |
| Model floats too high | `appearance.idleYOffset` |
| Idle particles start too high | `particles.heightOffset` |
| Text overlaps the model | `hologram.heightOffset` |
| Different bundled physical key | `key.keyModel` |
| Virtual keys | `key.keyMode: "VIRTUAL"`, optionally `key.virtualKeyId` |
| Require several keys | `keyRequirements`, with `ALL` or `ANY` logic |
| Immediate delivery | `opening.openingType: "instant"` |
| Master Ball opening | Model `astral_pokeball`, engine opening `astral_reveal` |
| New prize types or eligibility | [Rewards](./rewards) |
| New server choreography | [Animations](./animations) |

`glowEffect` controls the glowing display outline; it does not set block light output. The Master Ball's prize comes from your configured eligible reward pool.
