# UniCrates Custom Animations Guide

Welcome to the UniCrates Custom Animations Guide! The data-driven animation timeline system allows you to create custom, spectacular crate opening sequences completely through JSON.

Animations are defined in `config/unicrates/animations/&lt;id&gt;.json`. You can create self-contained timelines or extend built-in animations.

## Timeline Structure

An animation timeline is a JSON object with a unique identifier and an array of timeline steps.

### Basic Structure
```json
{
  "id": "my_custom_animation",
  "extendsId": null,
  "timeline": [
    {
      "tick": 0,
      "action": "play_sound",
      "sound": "minecraft:entity.player.levelup"
    }
  ]
}
```
- `id`: The unique identifier for this animation.
- `extendsId`: (Optional) The base built-in animation ID this extends. Use `null` for a self-contained timeline.
- `timeline`: An array of step objects, representing actions that occur on specific ticks.

## Actions and Parameters

Each entry in the `timeline` is an action that executes at a specific `tick`. Every step has:
- `tick` (Integer): The tick at which the action occurs. 20 ticks = 1 second.
- `action` (String): The action to perform.
- `durationTicks` (Integer, Optional): The interpolation duration for move/rotate/scale actions, in ticks.

Below are the available actions and their specific fields.

### `spawn_display`
Spawns a display entity (item, block, or text).
- `displayId` (String): Unique identifier for this display within the timeline. Use `"reward_icon"` as a reserved sentinel to automatically use the rolled reward item/block.
- `displayType` (String): `"item_display"`, `"block_display"`, or `"text_display"`.
- `item` (String, Optional): The item ID.
- `block` (String, Optional): The block ID.
- `text` (String, Optional): The text to display.
- `offset` (Array of Double, Optional): `[x, y, z]` starting offset relative to the crate's anchor block.
- `rotation` (Array of Double, Optional): `[yaw, pitch]` starting rotation in degrees.
- `scale` (Float, Optional): Starting scale.

### `move_display`
Moves an existing display smoothly over time.
- `target` (String): The `displayId` to target.
- `targetOffset` (Array of Double): `[x, y, z]` final offset relative to the anchor block.
- `durationTicks` (Integer): How long the movement interpolation should take.

### `rotate_display`
Rotates a display smoothly.
- `target` (String): The `displayId` to target.
- `rotation` (Array of Double): `[yaw, pitch]` final rotation in degrees.
- `durationTicks` (Integer): How long the rotation interpolation should take.

### `scale_display`
Scales a display smoothly.
- `target` (String): The `displayId` to target.
- `scale` (Float): Final scale multiplier.
- `durationTicks` (Integer): How long the scale interpolation should take.

### `despawn_display`
Removes a spawned display entity.
- `target` (String): The `displayId` to target.

### `play_sound`
Plays a sound effect at the crate's location.
- `sound` (String): The sound event ID (e.g., `"minecraft:entity.firework_rocket.launch"`).

### `play_particle`
Spawns particles at the crate's location.
- `particle` (String): The particle ID (e.g., `"minecraft:poof"`).
- `particleCount` (Integer, Optional): Number of particles to spawn.
- `particleSpeed` (Double, Optional): The speed of the particles.
- `offset` (Array of Double, Optional): `[x, y, z]` offset from the anchor block where particles should spawn.

### `cycle_display_items`
Cycles the displayed item rapidly (useful for the "spinning/rolling" effect before the final reward stops).
- `target` (String): The `displayId` to target.
- `cycleIntervalTicks` (Integer): Ticks between each item cycle.

### `orbit_display`
Makes a display entity orbit around the crate.
- `target` (String): The `displayId` to target.
- `orbitRadius` (Array of Double): `[radiusX, radiusZ]` for elliptical orbits.
- `orbitDegreesPerTick` (Double): Orbit speed in degrees per tick.
- `orbitStartAngle` (Double): Initial angle on the orbit path.

---

## Example: Epic Firework Opening

Here is a full JSON example utilizing multiple display actions, sounds, and particles:

```json
{
  "id": "epic_firework_opening",
  "extendsId": null,
  "timeline": [
    {
      "tick": 0,
      "action": "play_sound",
      "sound": "minecraft:block.chest.open"
    },
    {
      "tick": 5,
      "action": "spawn_display",
      "displayId": "reward_icon",
      "displayType": "item_display",
      "offset": [0.0, 0.5, 0.0],
      "rotation": [0.0, 0.0],
      "scale": 0.5
    },
    {
      "tick": 5,
      "action": "cycle_display_items",
      "target": "reward_icon",
      "cycleIntervalTicks": 2
    },
    {
      "tick": 5,
      "action": "move_display",
      "target": "reward_icon",
      "targetOffset": [0.0, 2.5, 0.0],
      "durationTicks": 40
    },
    {
      "tick": 5,
      "action": "rotate_display",
      "target": "reward_icon",
      "rotation": [720.0, 0.0],
      "durationTicks": 40
    },
    {
      "tick": 5,
      "action": "scale_display",
      "target": "reward_icon",
      "scale": 1.5,
      "durationTicks": 40
    },
    {
      "tick": 45,
      "action": "play_sound",
      "sound": "minecraft:entity.firework_rocket.blast"
    },
    {
      "tick": 45,
      "action": "play_particle",
      "particle": "minecraft:explosion",
      "particleCount": 50,
      "particleSpeed": 0.5,
      "offset": [0.0, 2.5, 0.0]
    },
    {
      "tick": 100,
      "action": "despawn_display",
      "target": "reward_icon"
    }
  ]
}
```
