---
title: Opening animations
description: Choose an opening engine and customize UniCrates 2.3 JSON timelines.
---

# Opening animations

UniCrates 2.3 includes **59 named opening presets: 52 editable JSON timelines, four Pokémon cinematic scenes, Master Singularity, interactive Poké Ball selection, and one GUI roulette preset**. The opening controls presentation; the crate's reward configuration controls prizes and eligibility.

<AnimationPreview id="astral_reveal" />

[Browse all 59 previews](./gallery) · [Preset catalog](./animation-catalog) · [Create a timeline](./animation-tutorial) · [Timeline reference](./timeline-reference) · [Idle effects](./idle-animations)

## Choose the right engine

| Presentation | Configuration | Customization |
| --- | --- | --- |
| Instant grant | `opening.openingType: "instant"` | Rewards and delivery; no timeline. |
| World timeline | `opening.openingType: "world_animation"` and `opening.animationId` | JSON displays, motion, particles, sounds, titles and cleanup. Uses vanilla display entities. |
| Pokémon cinematic | `animation.sceneVariant` or `opening.openingType: "scene_<variant>"` | Scene choice, duration, volume, density and appearance. Attack choreography belongs to its controller. |
| Master Singularity | World mode with `opening.animationId: "astral_reveal"` | Master Ball appearance, reward pool, scene volume and density. Adaptive roulette/emergence belong to its controller. |
| Interactive Poké Balls | World mode with `opening.animationId: "interactive_pokeball"` | Crate and rewards. Aim at a ball and right-click with the main hand. |
| GUI roulette | `opening.openingType: "roulette"` or `csgo_roulette_gui` | GUI appearance and duration. World steps do not edit the GUI reel. |

The simple grant path is `instant`; there is no `simple` timeline action or separate `simple` animation file. [Idle effects](./idle-animations) use a separate configuration while a placed crate is waiting.

## Assign a bundled timeline

Merge these sections into an existing valid crate file under `config/unicrates/crates/`, keeping its appearance, key and rewards:

```json
{
  "opening": {
    "openingType": "world_animation",
    "animationId": "classic_chest_pop"
  },
  "animation": {
    "type": "classic_chest_pop",
    "durationTicks": 145,
    "hideCrate": false
  }
}
```

Run `/crates reload`, then open the placed crate normally. `hideCrate: false` lets bundled split base/lid models accompany the timeline with their automatic hinge animation. Use `true` when your timeline supplies its own stage.

For the world runner, `main-config.json` → `animations.allowPerCrateOverride` defaults to `true`. Selection priority is: explicit roulette/strip/CSGO mode, `opening.animationId`, `animation.timeline`, `animation.type`, then global `animations.defaultAnimation`. Use explicit `opening.animationId` for new world configurations. A positive crate duration has a minimum of 20 ticks, and the opening also lasts for its timeline's declared duration and action endpoints.

An unknown ID can fall back to the matching crate timeline (`example_crate` → `example_timeline`). If none exists, the runner completes through its instant fallback. Reaching the world concurrency limit also uses that fallback. Check reload warnings instead of relying on it.

## Crate animation parameters

These fields belong to the crate's `animation` section, rather than an individual timeline step:

| Field | Default | Purpose |
| --- | --- | --- |
| `type` | `particle_vortex` | Legacy animation selector, used after the explicit opening ID and timeline selector. |
| `timeline` | Unset | Alternate JSON timeline selector; prefer `opening.animationId` in new configurations. |
| `durationTicks` | `100` | Minimum presentation duration for ordinary world/GUI openings; scene controllers normalize or adapt separately. |
| `hideCrate` | `false` | Suppresses the normal active base/lid model around a world timeline. |
| `sounds` | Empty map | Timeline sound aliases, for example `{"win":"minecraft:block.amethyst_block.chime"}`. |
| `cameraLock` | `false` | World runner applies strong movement slowdown for the initial configured duration, then removes it at completion. This is not a camera-keyframe definition. |
| `cinematicCamera` | `false` | Requests companion orbit-camera presentation. The current world runner also requests it for a non-null reward, even when this flag is false. |
| `cinematicRadius` | `2.8` | Companion orbit radius, normalized to `1.5–8` blocks. |
| `cinematicHeight` | `1.8` | Companion orbit height, normalized to `0.5–6` blocks. |
| `sceneVariant` | Unset | One of the four Pokémon attack variants. |
| `sceneVolume` | `1.0` | Scene audio multiplier, normalized to `0–2`. |
| `sceneParticleDensity` | `1.0` | Scene particle multiplier, normalized to `0–2`. |
| `visibleToNearbyPlayers` | `true` | Serialized setting; the current world-display runner does not use it to hide entities from nearby players. |
| `particles` | Empty list | Serialized compatibility field; executable world effects come from `play_particle`/`play_vortex` steps. |

Companion orbit-camera sessions require the opener's cinematic handshake; unsupported clients continue with the world presentation. The ordinary world runner requests at most 120 ticks of orbit-camera time, based on the initial configured crate duration. The camera has its own normalization and exit lifecycle, so extending a timeline does not extend that request automatically.

## Edit in the browser

1. Run `/crates editor` as an administrator and select the crate.
2. Open **Opening timeline** and choose a JSON preset.
3. Choose **Copy timeline** to create an independent ID for this crate; change ticks, displays, motion and effects on the copy.
4. For a phase definition, use **Convert phases to timed steps** if you prefer the flat editor.
5. Save the session and run its generated `/crates apply <hash>` command. Resolve validation errors before applying.

The timeline track is an action editor, not full 3D playback of an opening. Use the [recorded gallery](./gallery) for bundled sequences and Minecraft to inspect your custom result. The [web editor guide](./web-editor) explains the complete session/export/apply workflow.

Master Singularity and interactive selection show controller descriptions instead of editable steps. Pokémon scenes also use controllers: copying an ordinary timeline does not copy their actor attacks. The [catalog](./animation-catalog) separates controllers from JSON definitions.

## Edit on disk

Save `config/unicrates/animations/my_reveal.json`, set `id` to `my_reveal`, and assign that ID to the crate. Only top-level `.json` files in this directory are loaded. Bundled definitions are copied during initial default installation while `.defaults-installed` is absent; existing files are preserved. Later reloads do not restore a deleted preset once that marker exists. Back up presets or give your custom version a new ID.

The [tutorial](./animation-tutorial) contains a complete copyable reel and final winner lock. The [reference](./timeline-reference) covers every executable action, defaults, limits, easing, phases and inheritance.

## Reward presentation and delivery

World openings select a reward before the timeline starts. `reward_icon` displays it; `cycle_display_items` shows decorative decoys. `stop_cycle` on the reward item display restores the selected item stack. Display actions do not grant rewards, run reward commands, spend another key or reroll the winner. Normal completion invokes the server's reward delivery callback.

Interactive selection and Master Singularity use their own delivery lifecycle. Master Singularity settles delivery at its final winner lock and reveals the confirmed result. Transactions and pending delivery govern actual rewards when a presentation is interrupted.

## Pokémon cinematics and fallback

Scene variants are `gengar_shadow`, `charizard_rift`, `pikachu_electric` and `articuno_frost`. Full Pokémon actor scenes require server Cobblemon and a compatible UniCrates cinematic companion on the viewing client. Global `animations.companionMode` controls the opener's fallback:

| Mode | Behavior |
| --- | --- |
| `AUTO_FALLBACK` | Uses a vanilla timeline if the opener lacks cinematic support, or Cobblemon is absent. |
| `REQUIRE_COMPANION` | Rejects a cinematic opening if the opener lacks the companion handshake. |
| `FORCE_VANILLA` | Uses the timeline fallback even with a companion. |

`animation.sceneVolume` and `animation.sceneParticleDensity` are independently normalized to `0.0–2.0`; `0` mutes audio or disables scene particles. They do not replace world timeline particle counts or sound aliases. World display entities use normal entity tracking; per-crate visibility fields should not be treated as a private-view filter for those entities.

## Cleanup and troubleshooting

Put `despawn_all` before the declared end tick. Normal completion also removes remaining tracked displays and restores the anchor model/nameplate. Startup orphan cleanup removes temporary animation entities; persistent idle displays have separate tags.

| Symptom | Check |
| --- | --- |
| Immediate completion | Exact ID, reload warnings and world concurrency cap. |
| GUI instead of world sequence | Set `opening.openingType` to `world_animation`; old strip/roulette values have GUI precedence. |
| Move/scale does nothing | Spawn the target first; match its ID and required fields. |
| Prize remains a decoy | Add `stop_cycle` targeting `reward_icon`. |
| Particle absent | World bursts support simple particles, not parameterized dust/block/item payloads. |
| Rotation does not tween | `rotate_display` sets yaw/pitch immediately; use `spinSpeed` for continuous rotation. |
| Idle model moves when tuning effects | Particle height uses `particles.heightOffset`; model height uses `appearance.idleYOffset`. |
| Pokémon attack becomes a chest reveal | Check Cobblemon, companion handshake, companion mode and fallback timeline. |

Gallery previews are recorded demonstrations. Your server's tick rate, Minecraft settings, models and reward pool affect the result.
