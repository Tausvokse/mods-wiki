# Crate JSON field reference

File: `config/unicrates/crates/<id>.json`. This reference describes the current Java schema. Omitted sections use initialized defaults; explicit nulls can remove those defaults and should be avoided. Copy the complete example in [JSON recipes](../custom-content/json) for a working starting point.

## Identity and content

| Field | Default | Rules |
| --- | --- | --- |
| `configVersion` | `1` | Schema metadata |
| `id` | none; required | Must match filename without `.json`; 1–64 letters, digits, underscores or hyphens |
| `displayName` | none; required | Nonblank; supports the mod's formatted text parser |
| `lore` | `[]` | Description lines |
| `rewards` | `[]` | At least one entry; unique nonblank reward IDs within this crate; positive finite total weight |
| `milestones` | `[]` | Additional rewards tied to opening counts |
| `hologram` | unset | When present, replaces the entire nested `appearance.hologram` object |

Reward types, item components and Pokémon attributes have their own [complete reference](../custom-content/rewards).

## Keys

| `key` field | Default | Meaning |
| --- | --- | --- |
| `id` | none; required | Physical key identity stored by UniCrates; use a stable ID such as `starter_key` |
| `displayName` | unset | Key item name |
| `texture` | unset | Resource-pack texture path |
| `customItemModel` | unset | Item identifier or validated custom model file |
| `customModelData` | unset | Custom model data integer |
| `lore` | `[]` | Physical key description |
| `consumeOnOpen` | `true` | Consume the normal key used for opening |
| `acceptedKeyIds` | `[]` | Extra accepted physical key IDs |
| `keyMode` | `"PHYSICAL"` | `PHYSICAL`, `VIRTUAL`, `BOTH`; case-insensitive helper |
| `virtualKeyId` | unset | Virtual ledger ID; blank/unset uses crate `id` |
| `virtualKey` | `false` | Legacy fallback only when `keyMode` is blank/invalid; it does not override the default valid `PHYSICAL` mode |
| `keyModel` | unset | Bundled visual key model |

`keyMode` aliases: `key_mode`, `mode`. `virtualKeyId` alias: `virtual_key_id`. Prefer the canonical spellings. In `BOTH`, normal opening spends a virtual key first, then a valid physical key held in the main hand. Physical keys are mod items with a data-component identity; ordinary renamed items are not accepted as keys.

The handler accepts configured `key.id` (apart from the generic `unicrates:crate_key` sentinel), crate ID, `<crate_id>_key`, and additional accepted IDs. Existing physical stacks retain their identity after a configuration rename. Keep key IDs stable or retain old IDs as accepted IDs.

### Multiple key requirements

`keyRequirements` replaces the normal single-key check when enabled with a nonempty list. Aliases: `key_requirements`, `keyRequirementsConfig`.

| Field | Default | Behavior |
| --- | --- | --- |
| `enabled` | `false` | Activate multi-key check |
| `mode` | `"ALL"` | `ALL`: meet every entry; `ANY`: take the first satisfied entry in list order |
| `requirements` | `[]` | Must be nonempty when enabled |
| `requirements[].keyId` | required | Exact ledger/physical identity; aliases `key_id`, `id` |
| `requirements[].amount` | `1` | Positive integer |
| `requirements[].type` | `"ANY"` | `VIRTUAL`, `PHYSICAL`, `ANY`; aliases `key_type`, `keyType` |

An entry with type `ANY` can combine virtual and inventory physical keys, spending virtual first. The engine reserves balances across repeated IDs in `ALL` mode, so the same balance cannot satisfy two entries twice. The mode helper treats unknown modes as `ALL` and unknown entry types as `ANY`; spell valid values explicitly. Multi-key deductions are separate from `key.consumeOnOpen` and consume the planned quantities.

## Opening

| `opening` field | Default | Effective behavior |
| --- | --- | --- |
| `openingType` | `"strip"` | `strip`, `roulette`, `reels`, `wheel`, `selectable`, `instant`, `world_animation`, `interactive_pokeball`, `interactive_3d`, `cinematic`, or a supported `scene_...` route |
| `animationId` | unset | Opening-specific animation reference; see animation guide |
| `cooldownSeconds` | `0` | Per-player, per-crate cooldown; negative values effectively clamp to 0 |
| `permission` | unset | Additional opening permission node; blank means unrestricted |
| `noPermissionMessage` | `"&cYou do not have permission to open this crate!"` | Denial text; alias `no_permission_message` |
| `knockbackOnDenied` | `true` | Push on permission denial; alias `knockback_on_denied` |
| `knockbackStrength` | `1.2` | Must be finite; nonpositive runtime value uses 1.2 for this permission-denial path; alias `knockback_strength` |
| `purchaseCostAlternative` | unset | Positive economy price used when no normal key is available; finite, nonnegative; 0 disables alternative |
| `trigger` | `"right_click"` | Schema accepts `right_click`, `sneak_right_click`, `gui_confirm`; handler does not use this field to change triggering |
| `requireEmptyHandOrKeyOnly` | `false` | Stored; no runtime consumer found |
| `bulkOpenAllowed` | `false` | Stored; no implemented bulk-open entry point found |
| `bulkOpenOptions` | `[]` | Stored list of numbers / `"all"`; not an active bulk picker |

Shift-right-click currently requests preview regardless of `trigger`. An empty main hand requests preview unless a usable virtual key or positive purchase alternative makes it an opening attempt. A physical key held in the main hand initiates the physical path. See [gameplay](../gameplay/).

## Access restrictions

| `restrictions` field | Default | Behavior |
| --- | --- | --- |
| `dimensionWhitelist` | `[]` | Empty permits any dimension; otherwise current namespaced dimension ID must appear |
| `dimensionBlacklist` | `[]` | Deny listed dimension IDs, including IDs also in whitelist |
| `requiredPermission` | unset | Checked alongside `opening.permission`; both must pass |
| `pokemonOnly` | `false` | Validator requires every reward type to be `cobblemon_*`; includes Cobblemon item/egg types |
| `maxOpensPerPlayer` | unset | Positive lifetime opening cap for that crate |

There is no implicit `unicrates.crate.<id>.open` gate: set a node in one of the permission fields to create a gate.

## Additional costs

| `costs` field | Default | Effective behavior |
| --- | --- | --- |
| `enabled` | `false` | Enable additional cost checks/deductions |
| `currencyCost` | unset | Finite nonnegative amount; positive values use registered economy provider |
| `experienceLevels` | unset | Nonnegative integer levels; positive values deducted |
| `experiencePoints` | unset | Nonnegative integer XP points; positive values deducted |
| `requiredKeyIds` | `[]` | Stored legacy field; handler does not enforce it; use `keyRequirements` |
| `requireAllKeys` | `false` | Stored legacy field; use `keyRequirements.mode` |

Currency cost is additive: if an opening uses the purchase alternative, the withdrawal is `purchaseCostAlternative + costs.currencyCost`. Level and point costs are also both charged when both are positive. Test with a survival player: creative mode skips payment deduction and bypasses cooldown, which can conceal configuration mistakes.

## Selection and milestones

| Field | Default | Rules / behavior |
| --- | --- | --- |
| `selective.enabled` | `false` | Enable card-selection path |
| `selective.amountToPick` | `1` | Positive; player must claim that many rewards |
| `selective.poolSize` | `3` | Must be at least amountToPick; number of revealed choices |
| `milestones[].openings` | `10` | Positive opening threshold |
| `milestones[].rewardId` | required | Must match a reward in this crate |
| `milestones[].displayName` | unset | Stored label; delivery message resolves reward display name |
| `milestones[].repeatEvery` | `false` | False: once on/after threshold; true: every multiple of threshold |
| `milestones[].broadcast` | `true` | Stored field; not read by milestone delivery |

A selectable opening counts once even when several cards are claimed. One-time milestones are tracked by **list index**: avoid reordering/deleting entries after players have claimed them. Milestones are direct bonus issuance, not normal weighted candidate rolls; do not assume ordinary weight, probability, permission filters or win-limit behavior applies to the bonus path. Use explicit reward definitions suitable for every eligible milestone player.

## Preview and denial effects

| Field | Default | Meaning |
| --- | --- | --- |
| `preview.enabled` | `true` | Permit preview UI; disabling does not remove public access via other commands |
| `preview.showChancePercentage` | `true` | Show configured percentages |
| `preview.sortByRarity` | `true` | Sort higher tiers first |
| `preview.requirePermissionToPreview` | `false` | Require `unicrates.crate.<id>.preview` |
| `pushback.enabled` | `true` | General denial pushback |
| `pushback.strength` | `1.2` | Finite, nonnegative |
| `pushback.sound` | `"minecraft:entity.iron_golem.damage"` | General denial sound |
| `pushback.playParticles` | `true` | General denial particles |

The permission-denial branch has its own `opening.knockbackOnDenied` and strength; disabling general pushback is not equivalent to disabling permission-denial knockback.

## Appearance, hologram, animation and particles

These fields are listed here for schema completeness. Use [models](../custom-content/models) and [animations](../custom-content/animations) for visual workflows and selection precedence.

| `appearance` field | Default |
| --- | --- |
| `displayMode` | `"item_display"`; validator also accepts `block_display`, `vanilla_block` |
| `vanillaBlockFallback` | `"minecraft:chest"` |
| `blockTexture`, `customItemModel`, `guiIcon`, `builtinModel` | unset |
| `customModelData` | unset |
| `glowEffect`, `floatingRotation` | `false` |
| `scale` | `1.0`; positive finite float, maximum 50 |
| `idleYOffset` | `0.0`; finite |
| `guiTheme` | `"dark"`; `dark`, `light`, `gold`, `void`; unknown falls back to dark |
| `hologram` | initialized object below |

`floatingRotation` is stored without an active rotation consumer. `displayMode` is schema-valid metadata; do not assume changing it creates a different block/entity implementation. The manual file loader normalizes negative `idleYOffset` and exactly `0.5` to 0 as legacy correction. The model anchor uses `0.5 * scale + idleYOffset`; particle offset is independent.

| Hologram field | Default / rules |
| --- | --- |
| `enabled` | `true` |
| `lines` | Three lines: formatted crate title, right-click to open, empty-handed right-click to preview |
| `heightOffset` | `1.8`; height of lowest line above anchor floor |
| `offsetY` | `0.0`; positive values override heightOffset |
| `lineSpacing` | `0.28`; runtime uses 0.38 for values ≤0 or >1 |
| `backgroundArgb` | `1073741824` (`0x40000000`) |
| `seeThrough` | `false` |
| `scale` | `1.0`; >0 and ≤50 |

Root `hologram` wins over nested `appearance.hologram` as a whole object. Empty lines `[]` hide the text while preserving other settings. Limits: 32 lines, 4096 UTF-16 code units per template, finite offsets within -100..100, finite spacing. Substituted text is capped at 8192 UTF-16 code units. Hologram clearance also respects nominal model height; changing `particles.heightOffset` never moves holograms or the model.

| `animation` field | Default |
| --- | --- |
| `type` | `"particle_vortex"`; nonblank required |
| `timeline` | unset |
| `durationTicks` | `100` |
| `visibleToNearbyPlayers` | `true` |
| `sounds` | `{}` |
| `particles` | `[]` |
| `cameraLock`, `cinematicCamera`, `hideCrate` | `false` |
| `cinematicRadius` | `2.8`; finite |
| `cinematicHeight` | `1.8`; finite |
| `sceneVariant` | unset; aliases `scene_variant`, `cinematicVariant`, `cinematic_variant` |
| `sceneVolume` | `1.0`; finite, effective clamp 0–2; alias `scene_volume` |
| `sceneParticleDensity` | `1.0`; finite, effective clamp 0–2; alias `scene_particle_density` |

Scene settings require appropriate companion capabilities. Generic animation duration is not a universal cap: Pokémon scenes clamp to 40–300 ticks. See animation reference for actual mode behavior.

| `particles` field | Default |
| --- | --- |
| `enabled` | `true` |
| `type` | `"spiral"` |
| `particle` | `"minecraft:portal"` |
| `speed` | `1.0`; finite |
| `radius` | `1.2`; finite |
| `count` | `2` |
| `heightOffset` | `0.0`; finite, independent emitter offset |

Particle shape names: `none`, `spiral`, `double_spiral`, `growing_spiral`, `helix`, `double_helix`, `tilted_rings`, `orbital_rings`, `circle`, `animated_circle`, `rings`, `sphere`, `vortex`, `beacon_pillar`, `fountain`, `cube_cage`, `galaxy_swirl`, `star_burst`. Runtime rendering clamps work; see the animation guide for effective limits.

Custom model files ending in `.json` must use a safe `resources/.../*.json` path, at most 207 characters, with lowercase letters/digits/underscore/hyphen path segments. File-backed models require customModelData 1000–16777214. Namespaced item identifiers are a separate accepted form.

Source: `CrateConfig`, `CrateConfigValidator`, `CostConfig`, `KeyRequirementConfig`, `KeyRequirementEngine`, `MilestoneConfig`, `SelectiveRewardConfig`, `LinkedCrateInteractHandler`, `CrateOpenService`, `RewardDelivery`.
