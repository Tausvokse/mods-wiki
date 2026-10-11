---
title: Animation catalog
description: All 59 UniCrates 2.3 named opening presets with recorded previews and exact configuration IDs.
---

# Animation catalog

The current library contains **59 named presets: 52 JSON definitions and seven controller presets**. The [gallery](./gallery) contains recorded previews for these IDs. JSON durations below come from the bundled definitions and their timed endpoints; a longer crate duration extends the actual opening.

Several themed files provide alternate IDs for the same starting choreography. They are separate editable files and count among the 52 definitions. Runtime aliases are listed separately at the end and do not add presets. The older Reality Slice, Chrono Rewind, Magnetic Assembly and Resonance Core controllers are no longer part of the current library.

## Controller presets

### Master Singularity — `astral_reveal`

<AnimationPreview id="astral_reveal" />

The Master Ball lifts above its stationary pedestal, opens, and charges with opposing energy ribbons. Its roulette passes through every unique eligible reward, slows from **4 to 6 ticks per candidate**, holds the confirmed winner for **12 ticks**, then releases one continuous prize emergence and a coronation halo. The title settles at scale **0.40** without following prize bob/spin. The prize retreats, the shell closes, and the ball lands.

The eligible pool is captured before the opening updates win counters and is deduplicated by reward ID. It respects reward eligibility, limits, permissions and supported reward issuers. **1–256 unique eligible entries** are supported; larger pools are rejected before starting. Multi-entry pools make enough complete passes to display at least 12 candidate slots; a single eligible prize holds for 60 ticks. The controller's base minimum is **280 ticks / 14 seconds**, growing automatically with the pool. Its duration is adaptive; the crate's configured duration does not force a large pool into a shorter roll.

Delivery is requested at the final lock, and the display uses the confirmed issued result. If confirmation is delayed, the controller can wait up to 60 additional ticks and shift the reveal timing. Decorative previews do not run reward commands or issue Pokémon repeatedly.

Merge these fields into your existing crate:

```json
{
  "appearance": {
    "displayMode": "item_display",
    "builtinModel": "astral_pokeball",
    "scale": 1.35
  },
  "opening": {
    "openingType": "world_animation",
    "animationId": "astral_reveal"
  },
  "animation": {
    "type": "astral_reveal",
    "durationTicks": 280,
    "hideCrate": true,
    "sceneVolume": 1.0,
    "sceneParticleDensity": 1.0
  }
}
```

This is a procedural controller, not an editable `astral_reveal.json` timeline. Tune its model/pool/effect parameters; do not create an `extendsId` parent expecting to inherit this choreography. The Master preview uses the October 11 roulette hotfix recording.

[Watch Master Singularity in the gallery](./gallery?opening=astral_reveal)

### Four Pokémon attack scenes

These scenes use Pokémon actors and companion choreography, with [vanilla fallback](./animations#pokemon-cinematics-and-fallback) for unsupported openers. `durationTicks` is normalized into `40–300` for these four scenes; the defaults below apply when no positive duration is configured. Climax scales proportionally while leaving room for the prize ascent.

| Scene variant | Default duration | Default climax | Presentation | Preview |
| --- | --- | --- | --- | --- |
| `gengar_shadow` | 80 ticks / 4 s | 45 | Gengar and shadow energy. | [Watch](./gallery?opening=gengar_shadow) |
| `charizard_rift` | 90 ticks / 4.5 s | 50 | Charizard and a fiery rift attack. | [Watch](./gallery?opening=charizard_rift) |
| `pikachu_electric` | 70 ticks / 3.5 s | 38 | Pikachu and an electrical strike. | [Watch](./gallery?opening=pikachu_electric) |
| `articuno_frost` | 80 ticks / 4 s | 42 | Articuno and a frost attack. | [Watch](./gallery?opening=articuno_frost) |

<AnimationPreview id="gengar_shadow" />
<AnimationPreview id="charizard_rift" />
<AnimationPreview id="pikachu_electric" />
<AnimationPreview id="articuno_frost" />

Example scene assignment, merged into a valid crate:

```json
{
  "opening": {
    "openingType": "scene_charizard_rift",
    "animationId": "classic_chest_pop"
  },
  "animation": {
    "sceneVariant": "charizard_rift",
    "durationTicks": 90,
    "sceneVolume": 1.0,
    "sceneParticleDensity": 0.8
  }
}
```

Here `classic_chest_pop` is an explicit fallback timeline; it is not the scene's internal attack program. You can also use world opening mode with `animation.sceneVariant`. Canonical variant names belong in `sceneVariant` or the `scene_` opening mode, rather than pretending they are JSON files.

### Interactive Poké Ball selection — `interactive_pokeball`

<AnimationPreview id="interactive_pokeball" />

Three Poké Balls appear above the crate. The opener aims at a ball and **right-clicks with the main hand**. Selection uses the current accepted player look direction rather than an old hover state; entity hitboxes also support selection. Other players cannot choose the opener's ball. This is manual selection, not an automatic gaze-only action. The finishing prize presentation lasts 80 ticks after selection.

The controller has a 300-tick selection timeout; expiry automatically claims a ball. The backup look selection checks a target ahead of the player's eyes within 6 blocks. Offhand interaction does not select a ball.

Use world opening mode and `opening.animationId: "interactive_pokeball"`. It is distinct from **`pokeball_interactive_timeline`**, which is an ordinary timed JSON sequence with no manual input controller.

[Watch interactive Poké Ball selection](./gallery?opening=interactive_pokeball)

### GUI roulette — `csgo_roulette_gui`

The GUI controller presents an inventory reel. Use `opening.openingType: "roulette"` or select this preset for the appropriate world-runner route. Its positive configured duration has a minimum of 20 ticks, with 100 ticks as fallback. It uses GUI layout/theme controls; world displays and timeline actions do not define its reel.

[Watch GUI roulette](./gallery?opening=csgo_roulette_gui)

## All 52 editable JSON definitions

Each row corresponds to `config/unicrates/animations/<id>.json`. Select its ID with `opening.animationId` and world opening mode. Clone a definition for independent editing, or use [inheritance](./timeline-reference#inheritance) for a small, carefully targeted override. Step counts describe the bundled JSON, not extra base/lid controller motion.

| Definition ID | Ticks / seconds | Steps | Starting theme | Preview |
| --- | --- | --- | --- | --- |
| `abyssal_prismarine_timeline` | 137 / 6.85 | 50 | Abyssal Prismarine | [Watch](./gallery?opening=abyssal_prismarine_timeline) |
| `amethyst_geode_timeline` | 134 / 6.7 | 54 | Amethyst Geode | [Watch](./gallery?opening=amethyst_geode_timeline) |
| `angelic_ascension` | 125 / 6.25 | 38 | Holy ascent and radiant reward | [Watch](./gallery?opening=angelic_ascension) |
| `angelic_timeline` | 125 / 6.25 | 38 | Angelic | [Watch](./gallery?opening=angelic_timeline) |
| `atlantis_abyss` | 138 / 6.9 | 49 | Deep-sea reveal | [Watch](./gallery?opening=atlantis_abyss) |
| `atlantis_timeline` | 138 / 6.9 | 49 | Atlantis | [Watch](./gallery?opening=atlantis_timeline) |
| `aztec_jaguar_timeline` | 128 / 6.4 | 72 | Aztec Jaguar | [Watch](./gallery?opening=aztec_jaguar_timeline) |
| `celestial_astral_timeline` | 134 / 6.7 | 59 | Celestial Astral | [Watch](./gallery?opening=celestial_astral_timeline) |
| `celestial_convergence` | 132 / 6.6 | 48 | Celestial convergence | [Watch](./gallery?opening=celestial_convergence) |
| `classic_chest_pop` | 145 / 7.25 | 28 | Chest pop with decorative coins | [Watch](./gallery?opening=classic_chest_pop) |
| `common_timeline` | 127 / 6.35 | 46 | Common | [Watch](./gallery?opening=common_timeline) |
| `common_wooden_timeline` | 127 / 6.35 | 46 | Common Wooden | [Watch](./gallery?opening=common_wooden_timeline) |
| `demonic_hellfire` | 125 / 6.25 | 39 | Nether flame reveal | [Watch](./gallery?opening=demonic_hellfire) |
| `demonic_timeline` | 125 / 6.25 | 39 | Demonic | [Watch](./gallery?opening=demonic_timeline) |
| `ender_voidborn_timeline` | 134 / 6.7 | 51 | Ender Voidborn | [Watch](./gallery?opening=ender_voidborn_timeline) |
| `epic_obsidian_timeline` | 127 / 6.35 | 52 | Epic Obsidian | [Watch](./gallery?opening=epic_obsidian_timeline) |
| `epic_timeline` | 127 / 6.35 | 52 | Epic | [Watch](./gallery?opening=epic_timeline) |
| `firework_burst` | 140 / 7 | 22 | Rocket and celebratory fireworks | [Watch](./gallery?opening=firework_burst) |
| `frostmourne_glacial_timeline` | 125 / 6.25 | 39 | Frostmourne Glacial | [Watch](./gallery?opening=frostmourne_glacial_timeline) |
| `hologram_spin` | 170 / 8.5 | 30 | Holographic spinning prize | [Watch](./gallery?opening=hologram_spin) |
| `item_display_carousel` | 150 / 7.5 | 53 | Orbiting item carousel | [Watch](./gallery?opening=item_display_carousel) |
| `kraken_galleon_timeline` | 139 / 6.95 | 50 | Kraken Galleon | [Watch](./gallery?opening=kraken_galleon_timeline) |
| `legendary_gold_timeline` | 130 / 6.5 | 63 | Legendary Gold | [Watch](./gallery?opening=legendary_gold_timeline) |
| `legendary_timeline` | 130 / 6.5 | 63 | Legendary | [Watch](./gallery?opening=legendary_timeline) |
| `light_beam_pillar` | 145 / 7.25 | 23 | Ascending light pillar | [Watch](./gallery?opening=light_beam_pillar) |
| `mecha_dragon_timeline` | 159 / 7.95 | 56 | Mecha Dragon | [Watch](./gallery?opening=mecha_dragon_timeline) |
| `meteor_shower_reveal` | 132 / 6.6 | 37 | Meteor shower reveal | [Watch](./gallery?opening=meteor_shower_reveal) |
| `money_jackpot` | 127 / 6.35 | 69 | Economy jackpot | [Watch](./gallery?opening=money_jackpot) |
| `money_timeline` | 127 / 6.35 | 69 | Money | [Watch](./gallery?opening=money_timeline) |
| `nature_bloom` | 125 / 6.25 | 39 | Botanical bloom | [Watch](./gallery?opening=nature_bloom) |
| `nature_timeline` | 125 / 6.25 | 39 | Nature | [Watch](./gallery?opening=nature_timeline) |
| `orbital_sweep` | 101 / 5.05 | 19 | Orbital sweep | [Watch](./gallery?opening=orbital_sweep) |
| `particle_vortex` | 150 / 7.5 | 28 | Shrinking particle vortex | [Watch](./gallery?opening=particle_vortex) |
| `pharaoh_tomb_timeline` | 128 / 6.4 | 72 | Pharaoh Tomb | [Watch](./gallery?opening=pharaoh_tomb_timeline) |
| `pokeball_interactive_timeline` | 127 / 6.35 | 49 | Pokeball Interactive | [Watch](./gallery?opening=pokeball_interactive_timeline) |
| `pokemon_master_capture` | 127 / 6.35 | 52 | Pokémon capture themed reveal | [Watch](./gallery?opening=pokemon_master_capture) |
| `pokemon_timeline` | 127 / 6.35 | 52 | Pokemon | [Watch](./gallery?opening=pokemon_timeline) |
| `portal_pull` | 99 / 4.95 | 20 | Portal pull | [Watch](./gallery?opening=portal_pull) |
| `prismatic_fairy_timeline` | 134 / 6.7 | 55 | Prismatic Fairy | [Watch](./gallery?opening=prismatic_fairy_timeline) |
| `radioactive_biohazard_timeline` | 160 / 8 | 64 | Radioactive Biohazard | [Watch](./gallery?opening=radioactive_biohazard_timeline) |
| `rare_iron_timeline` | 127 / 6.35 | 54 | Rare Iron | [Watch](./gallery?opening=rare_iron_timeline) |
| `rare_timeline` | 127 / 6.35 | 54 | Rare | [Watch](./gallery?opening=rare_timeline) |
| `retro_arcade_timeline` | 159 / 7.95 | 67 | Retro Arcade | [Watch](./gallery?opening=retro_arcade_timeline) |
| `samurai_shinto_timeline` | 128 / 6.4 | 61 | Samurai Shinto | [Watch](./gallery?opening=samurai_shinto_timeline) |
| `sculk_warden_timeline` | 134 / 6.7 | 57 | Sculk Warden | [Watch](./gallery?opening=sculk_warden_timeline) |
| `solar_flare_timeline` | 125 / 6.25 | 38 | Solar Flare | [Watch](./gallery?opening=solar_flare_timeline) |
| `steampunk_chronos_timeline` | 159 / 7.95 | 54 | Steampunk Chronos | [Watch](./gallery?opening=steampunk_chronos_timeline) |
| `tactical_airdrop_timeline` | 129 / 6.45 | 43 | Tactical Airdrop | [Watch](./gallery?opening=tactical_airdrop_timeline) |
| `vampiric_blood_timeline` | 137 / 6.85 | 44 | Vampiric Blood | [Watch](./gallery?opening=vampiric_blood_timeline) |
| `void_rift_reveal` | 132 / 6.6 | 42 | Void rift reveal | [Watch](./gallery?opening=void_rift_reveal) |
| `witchcraft_cauldron_timeline` | 128 / 6.4 | 73 | Witchcraft Cauldron | [Watch](./gallery?opening=witchcraft_cauldron_timeline) |
| `wyrm_hoard_timeline` | 137 / 6.85 | 45 | Wyrm Hoard | [Watch](./gallery?opening=wyrm_hoard_timeline) |

## Runtime aliases and routing

Aliases below do not add JSON definitions or recorded canonical presets.

| Input | Resolves/routes to |
| --- | --- |
| `csgo_roulette`, `gui_roulette`, `strip`, `csgo` as animation IDs | `csgo_roulette_gui` in animation-type resolution. |
| `roulette`, `gui_spin`, `csgo` as opening modes | Direct GUI spin route. `strip` is also recognized by world-runner selection as GUI. |
| `interactive_3d` | Interactive Poké Ball controller. |
| `timeline` as opening mode | World timeline route; use `world_animation` for new configurations. |
| `scene_gengar_shadow`, `scene_charizard_rift`, `scene_pikachu_electric`, `scene_articuno_frost` | Corresponding scene variant. |
| `cinematic` as opening mode | Gengar scene default when no explicit sceneVariant is supplied. |

`instant` and `selectable` are gameplay opening modes, not additional animated catalog presets. For reliable configuration, use the canonical IDs shown above. See [opening selection](./animations#assign-a-bundled-timeline) for precedence and fallbacks.

The shared gallery uses the accepted October 10 recordings for the other presets and the October 11 hotfix for Master Singularity. It shows the recorded result, not a promise that every scene was recaptured on the latest build.
