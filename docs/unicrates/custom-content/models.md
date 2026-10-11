---
title: Models, Keys & Rigs
description: The complete built-in model inventory, physical key models, rig variants, and appearance options.
---

# Models, Keys & Rigs

UniCrates 2.3 exposes **31 canonical built-in model IDs**, each with a bundled physical key rig. Browse the [visual gallery](./gallery), then use this page to choose exact IDs and understand what each asset controls.

## Built-in model gallery

These stills show actual closed crates in Minecraft. Search by theme, inspect the canonical model ID and key CMD, and follow a card to its recorded opening.

<ModelGallery />

## Select a bundled crate and key

Add these sections to your crate definition:

```json
{
  "appearance": {
    "displayMode": "item_display",
    "builtinModel": "sculk_warden",
    "scale": 1.0,
    "idleYOffset": 0.0,
    "floatingRotation": false,
    "glowEffect": false
  },
  "key": {
    "id": "my_warden_key",
    "displayName": "&3Warden Key",
    "keyModel": "sculk_warden",
    "keyMode": "PHYSICAL",
    "consumeOnOpen": true
  }
}
```

These are sections to merge into a complete [crate definition](./create). Run `/crate reload` after editing a file. Bundled assets ship with the mod; imported assets need a [resource pack](./resource-packs).

`appearance.builtinModel` selects the world model. `key.keyModel` selects the visual on the static `unicrates:crate_key` item. `key.id` identifies the key accepted by gameplay. A key's shape does not change its identity, consumption rule, or virtual balance.

## Complete built-in inventory

IDs are normalized to lowercase and accept a trailing `_crate`: `sculk_warden_crate` resolves to `sculk_warden`. The canonical names below avoid that extra suffix. The key CMD column documents the bundled `custom_model_data` mapping; select `keyModel` instead of manually assigning these reserved values.

| Canonical model ID | Crate canvas item | Physical key rig | Key CMD |
| --- | --- | --- | ---: |
| `sculk_warden` | `unicrates:crate_display_sculk_warden` | `sculk_warden_key` | 1 |
| `frostmourne_glacial` | `unicrates:crate_display_frostmourne_glacial` | `frostmourne_glacial_key` | 2 |
| `solar_flare` | `unicrates:crate_display_solar_flare` | `solar_flare_key` | 3 |
| `amethyst_geode` | `unicrates:crate_display_amethyst_geode` | `amethyst_geode_key` | 4 |
| `abyssal_prismarine` | `unicrates:crate_display_abyssal_prismarine` | `abyssal_prismarine_key` | 5 |
| `vampiric_blood` | `unicrates:crate_display_vampiric_blood` | `vampiric_blood_key` | 6 |
| `ender_voidborn` | `unicrates:crate_display_ender_voidborn` | `ender_voidborn_key` | 7 |
| `witchcraft_cauldron` | `unicrates:crate_display_witchcraft_cauldron` | `witchcraft_cauldron_key` | 8 |
| `aztec_jaguar` | `unicrates:crate_display_aztec_jaguar` | `aztec_jaguar_key` | 9 |
| `pharaoh_tomb` | `unicrates:crate_display_pharaoh_tomb` | `pharaoh_tomb_key` | 10 |
| `celestial_astral` | `unicrates:crate_display_celestial_astral` | `celestial_astral_key` | 11 |
| `steampunk_chronos` | `unicrates:crate_display_steampunk_chronos` | `steampunk_chronos_key` | 12 |
| `radioactive_biohazard` | `unicrates:crate_display_radioactive_biohazard` | `radioactive_biohazard_key` | 13 |
| `tactical_airdrop` | `unicrates:crate_display_tactical_airdrop` | `tactical_airdrop_key` | 14 |
| `mecha_dragon` | `unicrates:crate_display_mecha_dragon` | `mecha_dragon_key` | 15 |
| `samurai_shinto` | `unicrates:crate_display_samurai_shinto` | `samurai_shinto_key` | 16 |
| `kraken_galleon` | `unicrates:crate_display_kraken_galleon` | `kraken_galleon_key` | 17 |
| `retro_arcade` | `unicrates:crate_display_retro_arcade` | `retro_arcade_key` | 18 |
| `prismatic_fairy` | `unicrates:crate_display_prismatic_fairy` | `prismatic_fairy_key` | 19 |
| `wyrm_hoard` | `unicrates:crate_display_wyrm_hoard` | `wyrm_hoard_key` | 20 |
| `angelic` | `unicrates:crate_display_angelic` | `angelic_key` | 21 |
| `atlantis` | `unicrates:crate_display_atlantis` | `atlantis_key` | 22 |
| `demonic` | `unicrates:crate_display_demonic` | `demonic_key` | 23 |
| `money` | `unicrates:crate_display_money` | `money_key` | 24 |
| `nature` | `unicrates:crate_display_nature` | `nature_key` | 25 |
| `pokemon` | `unicrates:crate_display_pokemon` | `pokemon_key` | 26 |
| `common` | `unicrates:crate_display_common` | `common_key` | 27 |
| `rare` | `unicrates:crate_display_rare` | `rare_key` | 28 |
| `epic` | `unicrates:crate_display_epic` | `epic_key` | 29 |
| `legendary` | `unicrates:crate_display_legendary` | `legendary_key` | 30 |
| `astral_pokeball` | `unicrates:crate_display_astral_pokeball` | `astral_pokeball_key` | 31 |

`interactive`, `interactive_key`, and `pokeball_interactive` are key-model aliases for the `pokemon` key (CMD `26`). They are not additional crate model IDs.

### Physical key image samples

These ten existing key images illustrate the bundled shapes. All 31 key rigs are listed above; the remaining themes can be inspected through the web editor's key preview using the corresponding `keyModel` or in Minecraft.

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:1rem;margin:1.5rem 0">
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/angelic_key.png" alt="Angelic physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Angelic</figcaption></figure>
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/demonic_key.png" alt="Demonic physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Demonic</figcaption></figure>
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/atlantis_key.png" alt="Atlantis physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Atlantis</figcaption></figure>
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/pokemon_key.png" alt="Pokémon physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Pokémon</figcaption></figure>
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/money_key.png" alt="Money physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Money</figcaption></figure>
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/nature_key.png" alt="Nature physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Nature</figcaption></figure>
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/legendary_key.png" alt="Legendary physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Legendary</figcaption></figure>
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/epic_key.png" alt="Epic physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Epic</figcaption></figure>
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/rare_key.png" alt="Rare physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Rare</figcaption></figure>
  <figure style="margin:0;text-align:center"><img src="/UniCrates/models/common_key.png" alt="Common physical key" loading="lazy" style="height:90px;object-fit:contain;margin:auto" /><figcaption>Common</figcaption></figure>
</div>

### Master Ball

The modern Master Ball uses model **`astral_pokeball`** and opening **`astral_reveal`**. The shipped `astral_reveal_crate` uses key identity `astral_reveal_key` and the `pokemon` key rig. You can choose `astral_pokeball` for its physical key visual instead; its bundled rig exists with CMD `31`.

The world opening uses the server-confirmed winner from the eligible reward pool. Configure your own prizes; the model does not imply a fixed Pokémon species. Its pedestal has a dedicated startup-registered canvas item, `unicrates:crate_display_astral_pokeball_pedestal`.

## Rig files and opening variants

For each canonical ID, the mod contains a crate wrapper model at `assets/unicrates/models/item/crate_display_<id>.json` and geometry under `assets/unicrates/models/item/rig/`. Keys use `rig/<id>_key.json`. The display canvas items are registered at startup.

| Variant suffix | Purpose |
| --- | --- |
| No suffix | Closed/idle model |
| `_opening` | Opening-state wrapper |
| `_opening_1` … `_opening_5` | Opening pose/frame wrappers |
| `_open` | Open-state wrapper |
| `_closing_1` … `_closing_3` | Closing pose/frame wrappers |
| `_base` | Stationary body for a decomposed hinge |
| `_lid` | Separate lid with a local hinge pivot |

Some wrappers intentionally point to the same geometry. Having a frame filename does not guarantee a distinct pose. A rig is a set of item-model assets; it is not a GeckoLib skeleton or an imported Blockbench animation.

Built-in hinge control uses separate base/lid `ItemDisplay` entities and native transform interpolation. `angelic`, `atlantis`, `demonic`, `money`, `nature`, and `pokemon` have an additional 180-degree facing correction. The runtime applies their hinge offset and opening pitch accordingly. Do not compensate these bundled rigs by rotating their JSON again.

### Shipped crate presets

This matrix lists the **36 shipped crate definitions**, including the presets that reuse existing rigs. Key identity and key rig are intentionally separate columns. A timeline ID is different from an engine-controlled scene variant.

| Crate ID | Model | Key identity | Key rig | Opening reference |
| --- | --- | --- | --- | --- |
| `abyssal_prismarine_crate` | `abyssal_prismarine_crate` | `abyssal_prismarine_key` | `abyssal_prismarine` | `abyssal_prismarine_timeline` |
| `amethyst_geode_crate` | `amethyst_geode_crate` | `amethyst_geode_key` | `amethyst_geode` | `amethyst_geode_timeline` |
| `angelic_crate` | `angelic_crate` | `angelic_key` | `angelic` | `angelic_ascension` |
| `articuno_crate` | `frostmourne_glacial` | `articuno_crate_key` | `frostmourne_glacial` | `scene / articuno_frost` |
| `astral_reveal_crate` | `astral_pokeball` | `astral_reveal_key` | `pokemon` | `astral_reveal` |
| `atlantis_crate` | `atlantis_crate` | `atlantis_key` | `atlantis` | `atlantis_abyss` |
| `aztec_jaguar_crate` | `aztec_jaguar_crate` | `aztec_jaguar_key` | `aztec_jaguar` | `aztec_jaguar_timeline` |
| `celestial_astral_crate` | `celestial_astral_crate` | `celestial_astral_key` | `celestial_astral` | `celestial_astral_timeline` |
| `charizard_crate` | `solar_flare` | `charizard_crate_key` | `solar_flare` | `scene / charizard_rift` |
| `common_crate` | `common_crate` | `common_key` | `common` | `common_wooden_timeline` |
| `demonic_crate` | `demonic_crate` | `demonic_key` | `demonic` | `demonic_hellfire` |
| `ender_voidborn_crate` | `ender_voidborn_crate` | `ender_voidborn_key` | `ender_voidborn` | `ender_voidborn_timeline` |
| `epic_crate` | `epic_crate` | `epic_key` | `epic` | `epic_obsidian_timeline` |
| `frostmourne_glacial_crate` | `frostmourne_glacial_crate` | `frostmourne_glacial_key` | `frostmourne_glacial` | `frostmourne_glacial_timeline` |
| `gengar_crate` | `ender_voidborn` | `gengar_crate_key` | `ender_voidborn` | `scene / gengar_shadow` |
| `kraken_galleon_crate` | `kraken_galleon_crate` | `kraken_galleon_key` | `kraken_galleon` | `kraken_galleon_timeline` |
| `legendary_crate` | `legendary_crate` | `legendary_key` | `legendary` | `legendary_gold_timeline` |
| `mecha_dragon_crate` | `mecha_dragon_crate` | `mecha_dragon_key` | `mecha_dragon` | `mecha_dragon_timeline` |
| `money_crate` | `money_crate` | `money_key` | `money` | `money_jackpot` |
| `nature_crate` | `nature_crate` | `nature_key` | `nature` | `nature_bloom` |
| `pharaoh_tomb_crate` | `pharaoh_tomb_crate` | `pharaoh_tomb_key` | `pharaoh_tomb` | `pharaoh_tomb_timeline` |
| `pikachu_crate` | `celestial_astral` | `pikachu_crate_key` | `celestial_astral` | `scene / pikachu_electric` |
| `pokeball_interactive_crate` | `pokemon` | `interactive_key` | `pokemon` | `interactive_pokeball` |
| `pokemon_crate` | `pokemon_crate` | `pokemon_key` | `pokemon` | `scene / charizard_rift` |
| `prismatic_fairy_crate` | `prismatic_fairy_crate` | `prismatic_fairy_key` | `prismatic_fairy` | `prismatic_fairy_timeline` |
| `radioactive_biohazard_crate` | `radioactive_biohazard_crate` | `radioactive_biohazard_key` | `radioactive_biohazard` | `radioactive_biohazard_timeline` |
| `rare_crate` | `rare_crate` | `rare_key` | `rare` | `rare_iron_timeline` |
| `retro_arcade_crate` | `retro_arcade_crate` | `retro_arcade_key` | `retro_arcade` | `retro_arcade_timeline` |
| `samurai_shinto_crate` | `samurai_shinto_crate` | `samurai_shinto_key` | `samurai_shinto` | `samurai_shinto_timeline` |
| `sculk_warden_crate` | `sculk_warden_crate` | `sculk_warden_key` | `sculk_warden` | `sculk_warden_timeline` |
| `solar_flare_crate` | `solar_flare_crate` | `solar_flare_key` | `solar_flare` | `solar_flare_timeline` |
| `steampunk_chronos_crate` | `steampunk_chronos_crate` | `steampunk_chronos_key` | `steampunk_chronos` | `steampunk_chronos_timeline` |
| `tactical_airdrop_crate` | `tactical_airdrop_crate` | `tactical_airdrop_key` | `tactical_airdrop` | `tactical_airdrop_timeline` |
| `vampiric_blood_crate` | `vampiric_blood_crate` | `vampiric_blood_key` | `vampiric_blood` | `vampiric_blood_timeline` |
| `witchcraft_cauldron_crate` | `witchcraft_cauldron_crate` | `witchcraft_cauldron_key` | `witchcraft_cauldron` | `witchcraft_cauldron_timeline` |
| `wyrm_hoard_crate` | `wyrm_hoard_crate` | `wyrm_hoard_key` | `wyrm_hoard` | `wyrm_hoard_timeline` |

Use [animations](./animations) to distinguish custom timeline steps, interactive selection, and cinematic engine openings.

## Appearance resolution

For the idle item display, a nonblank `customItemModel` takes precedence over `builtinModel`. A `.json` file reference uses a paper canvas plus Custom Model Data; an item ID uses that existing registered item. Otherwise a known built-in model is used, followed by `vanillaBlockFallback`.

| Source | Example | What you must supply |
| --- | --- | --- |
| Bundled rig | `builtinModel: "epic"` | Mod assets installed on the client |
| Imported Java model | `customItemModel: "resources/models/my_crate.json"` | Model, PNG dependencies, unique CMD, generated pack |
| Existing item with a pack override | `customItemModel: "minecraft:paper"`, CMD `10005` | Your external pack's matching paper override |
| Existing registered item | `customItemModel: "minecraft:beacon"` | The item must exist in the installed game/mod registry |

An arbitrary model resource such as `myserver:beautiful_chest` does not create a registered item. Use the imported Java-model route, or select an existing item whose resource-pack model you override. ItemsAdder/Oraxen-style resource packs can be used through matching item/CMD assets; this is resource-pack compatibility, not a bundled plugin bridge.

### Placement controls

| Field | Meaning |
| --- | --- |
| `appearance.scale` | Positive finite display scale, up to `50` |
| `appearance.idleYOffset` | Vertical adjustment of the physical model |
| `appearance.floatingRotation` | Enables the idle rotation behavior |
| `appearance.glowEffect` | Glowing entity outline; does not emit block light |
| `particles.heightOffset` | Idle particle emitter height, independent of the model |
| `hologram.heightOffset` | Text placement, independent of both |

The physical anchor uses `0.5 * scale + idleYOffset`. Idle particle emitters start from the block center plus `particles.heightOffset`. Keep those values separate when correcting placement. `displayMode` is validated against `item_display`, `block_display`, and `vanilla_block`; the imported cube-model workflow uses `item_display`.

## Preview and acceptance

The web editor renders Java cube geometry and supported PNG textures, with orbit, zoom, and reset controls. Built-in previews resolve the copied canonical mod assets. The wiki's visual gallery documents those assets.

Lighting is approximate. Generated item layers, missing parent/texture assets, held-key display transforms, and final in-game openings require inspection in Minecraft. A single imported mesh does not gain the built-in hinge automatically, and the browser model viewer is not a full Minecraft opening player.

Continue with [model import](./model-import) for Blockbench exports, or [resource packs](./resource-packs) to distribute custom textures.
