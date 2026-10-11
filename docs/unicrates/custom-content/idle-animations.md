---
title: Idle animations and particles
description: All 17 UniCrates idle particle emitters, their parameters, coordinate origins and browser workflow.
---

# Idle animations and particles

Placed crates can emit procedural particles while they wait for an opening. There are **17 particle patterns plus `none`**: 18 choices in the browser editor. These effects live in the crate's `particles` section, not in `config/unicrates/animations/`.

[Opening animations](./animations) · [Model configuration](./models) · [Preview gallery](./gallery)

## Apply an idle effect

Merge this into an existing crate definition:

```json
{
  "particles": {
    "enabled": true,
    "type": "double_helix",
    "particle": "minecraft:portal",
    "speed": 0.7,
    "radius": 0.9,
    "count": 2,
    "heightOffset": 0.15
  }
}
```

Run `/crates reload` and inspect a loaded placed crate. In `/crates editor`, open **Idle animation**, enable particles, choose a mathematical pattern and particle preset, then tune its sliders. Save and apply the generated `/crates apply <hash>` command.

The browser preview follows the server emission trajectories around the model. Particle sprite appearance, lifetime and motion are approximate; use Minecraft for the final visual check. The opening GIF gallery demonstrates opening sequences, not every idle emitter.

## Parameters and defaults

| Field | Default | Meaning |
| --- | --- | --- |
| `enabled` | `true` | Master switch. `false` stops emission. |
| `type` | `spiral` | Pattern ID from the table below. Matching ignores case; unknown/null types use the single-spiral fallback. |
| `particle` | `minecraft:portal` | Particle ID. Unsupported/invalid IDs fall back to portal. Use simple particle types. |
| `speed` | `1.0` | Pattern phase/time multiplier, not particle launch velocity. Nonpositive values use `1.0`. |
| `radius` | `1.2` | Base horizontal radius before appearance-scale adjustment. Nonpositive values use `1.0`. |
| `count` | `2` | Pattern density seed, **not literal particles per tick**. Effective count is `1–25`; nonpositive values use `2`. |
| `heightOffset` | `0.0` | Moves only the emitter's vertical origin, in blocks. |

Speed, radius and height must be finite. The browser offers convenient ranges: speed `0.1–3`, radius `0.2–3`, density `1–25`, height `−0.5–2.5`. These slider ranges are not the complete server-side finite-value validation rules; use moderate values for useful placement and performance.

Each emitted point is a single particle with zero random spread and zero launch speed. Its subsequent sprite behavior comes from Minecraft's particle implementation.

## Every pattern

Here `c` means the effective density seed after clamping. Point counts are emitted points **per active server tick** for one loaded idle anchor.

| ID | Shape | Points/tick |
| --- | --- | --- |
| `spiral` | Rotating horizontal sample points with sinusoidal vertical movement. | `c` |
| `double_spiral` | Opposing points with inverted vertical waves. | `2c` |
| `growing_spiral` | Radius breathes from 40% to 100%; samples rise cyclically. | `c` |
| `helix` | One moving strand making two turns through a vertical span. | `6c` |
| `double_helix` | Opposed twin strands at each height. | `12c` |
| `tilted_rings` | Ring tilted 35 degrees, rotating over time. | `c` |
| `orbital_rings` | Two inclined rings and one flatter orbit. | `15c` |
| `circle` | Complete horizontal ring, fixed sampling positions. | `4c` |
| `animated_circle` | Rotating ring with breathing radius and a vertical ripple. | `4c` |
| `rings` | Three stacked rings with independent waves/radius changes. | `12c` |
| `sphere` | Rotating Fibonacci sphere envelope. | `10c` |
| `vortex` | Three tapered swirling strands climbing through the emitter. | `6c` |
| `beacon_pillar` | Narrow rising pillar plus a pulsing base ring. | `7c` |
| `fountain` | Expanding radial samples following parabolic vertical arcs. | `6c` |
| `cube_cage` | Moving samples on twelve edges of a breathing cube. | `48`, independent of count |
| `galaxy_swirl` | Three spiral arms with a gentle vertical wave. | `12c` |
| `star_burst` | Spherical radial burst that expands and repeats. | `6c` |
| `none` | Emitter disabled, even if enabled is true. | `0` |

For example, `orbital_rings` with count `2` emits 30 points per tick; `double_helix` emits 24. Dense patterns on many loaded anchors can cost much more than their count slider suggests. Start with count `1–2` for these shapes. The world-opening particle budget does not cap idle emitters.

## Coordinate origin and scale

The emitter is independent of the physical model. Define `effectiveScale = max(0.5, appearance.scale)` for a positive configured model scale:

```text
emitter X/Z center = anchor X/Z + 0.5
emitter Y center   = anchor Y + 0.5 + particles.heightOffset
                     + 0.5 × (effectiveScale − 1)
effective radius  = positive radius × effectiveScale
```

Pattern-local points are rotated by the crate's visual yaw, including the bundled model's orientation correction. Pattern vertical spans are defined by each formula; they are not all multiplied uniformly by scale. Sphere/orbit shapes that derive height from radius do grow vertically with radius.

The persistent model uses a different origin:

```text
model display Y = anchor Y + 0.5 × appearance.scale
                  + appearance.idleYOffset
```

Increasing `particles.heightOffset` raises the aura without lifting the crate. Increasing `appearance.idleYOffset` raises the model without moving the aura. Neither field sets an opening timeline's reward actor position.

## Idle models, nameplates and lifecycle

The idle model is selected from `appearance.customItemModel`, then `appearance.builtinModel`, then the vanilla fallback. Its `appearance.scale` and `idleYOffset` control placement. It is a persistent display, not a continuously evaluated custom timeline.

The current anchor tick does not use `appearance.floatingRotation` to spin the idle model. The field is serialized for compatibility, but it is not an idle animation type. Use procedural particle rotation for a moving aura; use an opening timeline for active actor motion.

Idle emission pauses while the anchor is locked for an opening. Models/nameplates are hidden/restored by the opening lifecycle as appropriate. Nameplate text is refreshed approximately every 20 ticks and the idle display is checked approximately every 40 ticks while idle. Chunk unloading ends ticking; reloading the anchor restores its persistent presentation.

To disable only the particles:

```json
{
  "particles": { "enabled": false, "type": "none" }
}
```

This leaves the model and hologram configuration available. For a complete opening's effects, edit its [timeline](./timeline-reference) or [scene parameters](./animation-catalog#controller-presets) instead.
