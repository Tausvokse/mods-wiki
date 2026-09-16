# UniCrates Custom Animations Guide

Welcome to the UniCrates Custom Animations Guide! The data-driven animation timeline system allows you to create custom, spectacular crate opening sequences completely through JSON.

Animations are defined in `config/unicrates/animations/<id>.json`. You can create self-contained timelines or extend built-in animations.

### Quick Start Commands (In-Game Zero-Code Workflow)
- **Create new animation**: `/crate anim new <name> [template]` — Clones a working animation template into `config/unicrates/animations/<name>.json` and hot-reloads it immediately.
- **Test-play in-game**: `/crate anim test <name>` — Look at any placed crate anchor and test your animation in real time without spending keys or granting items!

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

## Catalog of Built-in Animations (All Ready-to-Use)

UniCrates ships with **12 production-grade animation sequences** out of the box under `config/unicrates/animations/`:

| Animation ID | Duration | Primary Effects & Particles | Key Sound Effects | Ideal Crate Themes |
| :--- | :--- | :--- | :--- | :--- |
| `angelic_ascension` | **160 ticks (8.0s)** | Glowing ascending beam, `minecraft:flash`, holy halo rings (`minecraft:wax_off`), firework finale. | `block.enchantment_table.use`, `ui.toast.challenge_complete` | Angelic, Holy, Celestial, Mythic |
| `atlantis_abyss` | **155 ticks (7.8s)** | Deep-sea bubble vortex (`minecraft:bubble_pop`), nautilus swirling shells, splashing eruption. | `ambient.underwater.enter`, `block.conduit.activate`, `elder_guardian.ambient` | Atlantis, Oceanic, Water, Sunken |
| `classic_chest_pop` | **145 ticks (7.2s)** | Crisp chest pop, gentle smoke ring, celebratory totem sparkles and firework poof. | `block.chest.open`, `entity.item.pickup`, `win` | Starter, Classic, Spruce, Wooden |
| `demonic_hellfire` | **155 ticks (7.8s)** | Nether brimstone smoke, swirling `soul_fire_flame` geysers, dripping lava drops. | `entity.blaze.shoot`, `entity.wither.ambient`, `rareWin` | Demonic, Nether, Magma, Boss |
| `firework_burst` | **140 ticks (7.0s)** | Ascending rocket trail with flame particles, mid-air detonation with multi-color fireworks. | `open`, `win` | Celebratory, Holiday, Event |
| `hologram_spin` | **170 ticks (8.5s)** | Cybernetic orbital rings, rotating `end_rod` matrix, flash burst and high-tech hologram scan. | `entity.generic.explode`, `win`, `rareWin` | Cyberpunk, Sci-Fi, Holo, Futuristic |
| `item_display_carousel` | **150 ticks (7.5s)** | 5-item spinning 3D orbital carousel, totem particles, dynamic decelerating reward selection. | `block.note_block.hat`, `open`, `win` | Carousel, Mystery, Multi-Reward |
| `light_beam_pillar` | **145 ticks (7.2s)** | Skyward beacon light pillar, ascending particle ladder, radiant celestial flash. | `block.beacon.activate`, `open`, `win` | Lapis, Beam, Sacred, Crystal |
| `money_jackpot` | **155 ticks (7.8s)** | Gold coin geysers, ringing bell fanfare, experience orb rain, gold sparkle eruption. | `block.bell.use`, `entity.experience_orb.pickup`, `ui.toast` | Economy, Casino, Jackpot, Money |
| `nature_bloom` | **160 ticks (8.0s)** | Swirling cherry blossom leaves, blooming bone meal sparkles, joyful villager green glints. | `item.bone_meal.use`, `block.enchantment_table.use`, `win` | Botanical, Forest, Nature, Spring |
| `particle_vortex` | **150 ticks (7.5s)** | Dark matter cosmic vortex (`reverse_portal`), gravitational pull, sonic boom detonation. | `block.respawn_anchor.charge`, `entity.warden.sonic_boom` | Void, Netherite, Legendary, Vortex |
| `pokemon_master_capture` | **160 ticks (8.0s)** | Ultra-tech capture ray (`minecraft:witch`), 3-shake tension sequence, Master Ball star explosion. | `block.anvil.land`, `ui.toast.challenge_complete`, `rareWin` | Cobblemon, Pokémon, Legendaries |

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
