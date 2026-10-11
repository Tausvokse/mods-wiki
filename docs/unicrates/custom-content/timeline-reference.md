---
title: Timeline JSON reference
description: Every UniCrates 2.3 action, field, default, limit, easing curve and composition rule.
---

# Timeline JSON reference

This schema applies to server world timelines in `config/unicrates/animations/`. Start with the [tutorial](./animation-tutorial) for a complete example. Scenes, interactive selection and GUI roulette use [separate controllers](./animations#choose-the-right-engine).

## Root object and time

```json
{
  "id": "my_reveal",
  "durationTicks": 120,
  "timeline": [
    { "tick": 0, "action": "play_sound", "sound": "open" },
    { "tick": 118, "action": "despawn_all" }
  ]
}
```

| Field | Meaning |
| --- | --- |
| `id` | Definition ID. A missing/blank file ID defaults to the filename. Keep filename and ID identical. |
| `extendsId` | Optional parent ID from the loaded animation snapshot. |
| `durationTicks` | Optional overall end tick, `0–600`; retains a pause after the last step. |
| `timeline` | Steps with `tick` and `action`. An omitted array defaults to empty; do not set it to `null`. |
| `phases` | Optional phase DSL. Nonempty phases replace the flat timeline during compilation. |

**20 ticks = 1 second** at normal server tick rate. Flat step ticks are absolute; phase steps are local. Same-tick steps execute in array order, so spawn before moving/cycling. Action IDs are exact lowercase strings.

Step `durationTicks` contributes to total timeline duration even on actions that do not use it operationally. Runtime is the maximum of crate duration, declared duration and timed endpoints. Completion happens after advancing elapsed time: schedule cleanup **before** the overall end rather than depending on a last-tick step. Completion still discards remaining displays.

Some bundled files retain the historical property `totalDurationTicks`. It is not a current schema field; use `durationTicks` in new JSON.

## Coordinates and targets

Positions use the anchor's horizontal center and **bottom Y**:

```text
world X = anchor X + 0.5 + offset[0]
world Y = anchor Y       + offset[1]
world Z = anchor Z + 0.5 + offset[2]
```

`[0,1,0]` is the anchor's top surface. `targetOffset` is a destination relative to the anchor, not a displacement from the actor. These are world axes, not axes rotated by crate yaw. Mesh placement can make the visible center differ from the entity origin.

`displayId` names one display in the opening; `target` matches it exactly, including case. Reusing an ID updates compatible content. For reliable type changes, despawn then spawn: text/block spawning can replace another kind, but an item spawn encountering a different existing kind returns without replacement.

The model controller reserves `crate_base` and `crate_lid` when a bundled hinge rig is visible. Use other IDs for your decorative actors; the rig's hinge schedule runs separately from timeline motion.

## All 14 actions

| Action | Fields/defaults | Executable behavior |
| --- | --- | --- |
| `play_sound` | `sound` | Anchor sound, volume/pitch `1`. Resolves crate sound aliases. Missing/unresolvable IDs are ignored; offset is unused. |
| `play_particle` | `particle`; count `1`, speed `0.02`, offset `[0,0,0]` | Simple-particle burst, spread `0.15` per axis, subject to budgets. |
| `spawn_display` | Required `displayId`; item behavior by default; offset `[0,0,0]`, scale `0.6` | Spawns/updates item, block or text content. |
| `move_display` | Required `target`, `targetOffset`; duration `1`, easing `linear`, arc height `0` | Interpolates base position each tick; positive arc height adds vertical lift. |
| `rotate_display` | Required `target`; optional `rotation`, spin, pitch and bob fields | Immediate yaw/pitch plus continuous settings. Duration/easing do not tween this action. |
| `scale_display` | Required `target`; supply `scale`; duration `1`, easing `linear` | Scale interpolation. Missing scale is a no-op. Reward labels apply their multiplier. |
| `despawn_display` | Required `target` | Removes that display/context. Motion entries retire when they next find it absent. |
| `despawn_all` | None | Clears tracked displays, contexts, moves, orbits, cycles and vortices. |
| `cycle_display_items` | Required `target`; interval `2` | Random decoy reward icons. Replaces any previous cycle on that target. |
| `stop_cycle` | Required `target` | Stops cycling. Item `reward_icon` restores its selected reward stack with fixed billboard/ground pose. |
| `orbit_display` | Required `target`, `orbitRadius`; speed `5`, start angle `0`; optional `offset` | Ellipse around anchor. Only `offset[1]` sets height; omitted height preserves Y. Forces fixed billboard. |
| `stop_spin` | Supply `target` | Sets context yaw speed to `0`; does not stop orbiting/cycling. |
| `play_vortex` | Duration `40` | End-rod spiral shrinking from radius `1.2` and rising `2.2` blocks. Particle/offset/radius do not customize it. |
| `summon_lightning` | Offset `[0,0.5,0]` | Visual-only lightning; does not apply normal strike damage. |

There is no command, reward-grant, wait, camera-keyframe, stop-orbit or arbitrary entity-spawn action. Express waits through timing. An orbit ends when its target is removed or cleanup runs; avoid overlapping orbits on the same target. Orbit positioning takes precedence over that target's movement/bobbing.

## Display content and reward tokens

| Field | Values/behavior |
| --- | --- |
| `displayType` | `item_display`, `block_display`, `text_display`. `text` also works; prefer canonical names. |
| `item` | Ordinary item ID. Missing content uses a decoy reward icon. |
| `block` | Block ID; default `minecraft:stone`. No separate block-state properties field. |
| `text` | MiniMessage; empty/missing resolves to reward name. |
| `billboard` | `fixed`, `vertical`, `horizontal`, `center`. Item default `fixed`, text default `center`. |
| `rotation` | Exactly `[yawDegrees,pitchDegrees]`. Spawn initializes yaw; use `pitch` or a later rotate action for persistent context tilt. |
| `scale` | Uniform scale, default `0.6`. Reward text labels multiply configured scale by `8/7`. |

For item/text displays, spawn scale is applied immediately. The block-display spawn helper initially uses its default transform; add an explicit `scale_display` immediately after spawning a block actor when you need a chosen visible scale. Item spawning uses its yaw setting, while text/block spawn yaw is not applied by those helpers; use a rotate action for their orientation.

**`reward_icon`** is a reserved display ID. Its content comes from the already-selected reward; an explicit `item` does not override it. Item mode uses the resolved reward stack/components. Block mode uses the reward's resolved display ID; prefer item mode for non-block prizes.

Text supports `{reward}`, `{rarity}`, `{player}` and `%reward%`, `%rarity%`, `%player%`. `reward_title`, empty text, and text containing a reward token are reward labels and receive the `8/7` scale multiplier. Token text describes the selected reward even while decorative decoys cycle.

End a reel with `stop_cycle` on `reward_icon` before showing the title. Re-spawning the same reward item ID also restores the winner/cancels its cycle. Content updates are not position commands; use motion actions to move an existing actor.

## Motion parameters

| Field | Meaning/runtime |
| --- | --- |
| `spinSpeed` | Degrees/tick. Ordinary context starts at `0`; reward icon starts at `6` unless explicitly set. Supported on spawn/move/scale/rotate. |
| `bobAmplitude` | Vertical sine amplitude, in blocks. Providing it enables bobbing; `0` removes visible displacement. Context default `0.08`, initially disabled. Supported on spawn/move/scale/rotate. |
| `bobFrequency` | Radians/tick, context default `0.12`. Cycle length approximately `2π/frequency` ticks. Does not itself enable bobbing. |
| `pitch` | Fixed tilt in degrees; context default `0`. Supported on spawn/move/scale/rotate. |
| `arcHeight` | Additional parabolic lift on a move, maximum halfway. Only positive values add lift. |
| `pulse` | Parsed/stored on spawn/move/scale, but not applied by the current world runner. Use explicit scale steps. |
| `orbitRadius` | `[radiusX,radiusZ]` in blocks. |
| `orbitDegreesPerTick` | Elliptical path speed in degrees/tick. |
| `orbitStartAngle` | Initial angle in degrees; the first orbit tick advances by the speed. |
| `cycleIntervalTicks` | Ticks between content replacements; minimum `1`. |

Move/scale steps on a stopped `reward_icon` can restart its default spin when `spinSpeed` is omitted. Supply `spinSpeed: 0` on later steps to keep it still. A rotate action with `spinSpeed: 0` also controls its final pose.

## Easing curves

Easing applies to **move and scale**. Missing/blank means linear.

| IDs | Shape |
| --- | --- |
| `linear` | Constant progress. |
| `ease_in`, `ease_in_quad` | Quadratic acceleration. |
| `ease_out`, `ease_out_quad` | Quadratic deceleration. |
| `ease_in_out`, `ease_in_out_quad` | Quadratic acceleration then deceleration. |
| `ease_in_cubic`, `ease_out_cubic`, `ease_in_out_cubic` | Cubic acceleration/deceleration. |
| `ease_in_back`, `ease_out_back`, `ease_in_out_back` | Anticipation/overshoot; leave clearance. |
| `ease_in_bounce`, `ease_out_bounce` | Reversed/forward bounce. |
| `ease_in_out_sine` | Gentle sine easing. |
| `arc`, `parabola` | Progress reaches `1` halfway then returns to `0`; does not finish at the destination. |

For a jump that arrives at its destination, use a monotonic easing such as `ease_out_quad` **plus `arcHeight`**. Easing names trim whitespace and ignore case; action names do not.

## Sound aliases and particle budgets

The crate's `animation.sounds` map resolves `sound` keys first. Otherwise the aliases are:

| Alias | Default |
| --- | --- |
| `open` | `minecraft:block.chest.open` |
| `win` | `minecraft:entity.player.levelup` |
| `rareWin` | `minecraft:ui.toast.challenge_complete` |
| `tick` | `minecraft:block.note_block.hat` |

Other strings are full sound event IDs. Scene volume does not change these world sound calls.

World bursts accept **simple particles** such as `minecraft:poof`, `minecraft:smoke`, `minecraft:portal` and `minecraft:happy_villager`. The schema cannot provide the color/block/item payload required by parameterized types. Unsupported IDs are ignored.

The **48 physical particles per opening per tick** budget is shared proportionally by overlapping bursts/vortices. Per-burst caps: flash/explosion emitter `1`, explosion `4`, end rod/firework/glow `12`. Configured counts may be reduced, without affecting another opening's budget. File validation rejects `particleCount: 0`; use at least `1`.

## Phases

Phase names such as `intro`, `buildup`, `reveal` and `cleanup` are descriptive, not special triggers.

```json
{
  "id": "phase_reveal",
  "durationTicks": 100,
  "phases": [
    {
      "name": "intro",
      "durationTicks": 20,
      "steps": [
        { "tick": 0, "action": "play_sound", "sound": "open" }
      ]
    },
    {
      "name": "reveal",
      "durationTicks": 60,
      "steps": [
        { "tick": 0, "action": "spawn_display", "displayId": "reward_icon", "displayType": "item_display", "offset": [0, 1.6, 0], "scale": 0.8, "spinSpeed": 2 },
        { "tick": 10, "action": "play_sound", "sound": "win" }
      ]
    },
    {
      "name": "cleanup",
      "startTick": 90,
      "durationTicks": 10,
      "steps": [
        { "tick": 5, "action": "despawn_all" }
      ]
    }
  ]
}
```

Omitted `startTick` uses the preceding phase's start plus duration; omitted phase duration is `0`. Steps compile to `phase start + local tick`; explicit starts permit gaps/overlap. Here the prize spawns at `20` and clears at `95`. Missing step `phase` inherits the phase name. Compiled steps sort by tick. Nonempty phases replace a simultaneously supplied flat sequence.

## Inheritance

```json
{
  "id": "my_classic",
  "extendsId": "classic_chest_pop",
  "durationTicks": 170,
  "timeline": [
    { "tick": 45, "action": "play_sound", "sound": "minecraft:block.amethyst_block.chime" },
    { "tick": 130, "action": "play_particle", "particle": "minecraft:happy_villager", "particleCount": 12, "offset": [0, 2, 0] }
  ]
}
```

The parent must be a loaded JSON definition. Inheritance cannot copy Master Singularity, Pokémon attacks, interactive input or GUI controller logic.

Merge identity is **tick + action + displayId**, or `target` if displayId is absent, or an empty name if both are absent. A matching child replaces the whole parent step; others append. The example replaces the unnamed sound at `45` and adds a particle at `130`. Multiple unnamed same-tick parent sounds/particles share a key and can collapse during inheritance. Clone the whole definition when you need to preserve every overlapping effect.

Inheritance does not shift parent steps, remove cleanup or shorten duration. Extending the duration can leave an empty pause after parent cleanup; copy/edit cleanup to extend the actual prize hold. Resolved duration uses the maximum of parent/child durations and merged endpoints.

Depth limit is `64`. Unknown parents warn and leave the child standalone; invalid loaded parents cause the child to be skipped. Circular inheritance warns and treats the detected definition as standalone during resolution. Fix the parent/cycle instead of relying on fallback.

## Validation limits

| Input | Limit |
| --- | --- |
| Definition/parent/display/target IDs | `1–64` characters matching `[a-zA-Z0-9_.-]`; no spaces, slashes or namespace colons. Prefer lowercase underscores for new content. |
| Flat/compiled steps | At most `500`; at most `500` phases. |
| Ticks and declared/compiled endpoints | `0–600`; duration cannot be negative. |
| `offset`, `targetOffset` | Exactly 3 finite numbers, each within `±100`. |
| `orbitRadius` | Exactly 2 finite numbers, each within `±100`. |
| `rotation` | Exactly 2 finite numbers, each within `±1,000,000`. |
| `scale` | Finite `0–50`. |
| `particleCount` | Integer `1–200`. |
| `particleSpeed`, `arcHeight`, `bobAmplitude` | Finite, within `±100`. |
| `cycleIntervalTicks` | Integer `1–600`. |
| Other numeric motion fields | Finite, within `±1,000,000`. |
| `easing` | A listed easing ID. |

Validation runs before and after phase compilation/inheritance. Duplicate IDs, malformed JSON and invalid definitions produce warnings. Validation does not guarantee registry IDs exist or that a target has already spawned. Unknown properties are not executable features.

The `600`-tick limit belongs to JSON timelines. Master Singularity is adaptive procedural code and can run longer for large eligible pools.
