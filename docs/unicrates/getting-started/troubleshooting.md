# Troubleshooting

Start with the exact server error and affected crate/player IDs. A successful JSON parse does not prove every referenced item, command, Pokémon or external provider exists. Keep transaction data and logs before changing a live configuration.

## Installation and startup

| Symptom | Checks |
| --- | --- |
| Loader rejects JAR | Minecraft 1.21.1, correct Fabric/NeoForge artifact, Java 21, required loader/API versions |
| Duplicate mod / duplicate classes | Remove universal + split artifact overlap; one UniCrates distribution per side |
| Singleplayer has no crate commands | Use universal artifact; client companion alone does not initialize an integrated server |
| SQL initialization fails | Endpoint, credentials, database existence, SQLite parent directory/permissions and migration destination identity |
| Missing JDBC class | Use release server/universal artifact rather than slim/dev/test output |
| Cobblemon version warning | Compare installed version with configured 1.7.3 target; warning does not repair incompatibility |

The current Fabric metadata uses the project's loader value as its minimum. Older documentation quoting only Cobblemon's 0.17.2 minimum is insufficient for this build's UniCrates requirement.

## Missing crate or command

Run `/crate list` as administrator and `/crate reload`; inspect loaded/failed counts. Invalid manual files are omitted from the newly rebuilt registry. Filename and `id` must match. `displayName`, `key.id`, animation type and a positive-weight reward pool are required. Full diagnostics appear in server log/reload messages.

`/crate create <id>` places an existing loaded definition; it does not create JSON. `/crate give <player> <id> <amount>` requires the amount. `/crate info`, list and stats are administrative, and stats requires an online player. Use [exact command syntax](../administration/commands).

If deleting a sample does not regenerate it, `.defaults-installed` is doing its intended one-time job. Restore the desired example from your backup or define it again; do not clear that marker as a routine reload fix on a customized server.

## Keys, previews and costs

| Symptom | Likely cause / action |
| --- | --- |
| Renamed item rejected as key | Physical keys need UniCrates identity component; grant with key command |
| Physical inventory key does not open | Normal path checks main-hand stack; multi-key path checks inventory |
| Empty hand opens instead of previews | Usable virtual key or purchase alternative; shift-right-click explicitly previews |
| BOTH uses virtual instead of physical | Intended virtual-first order |
| Virtual balance appears missing | Check crate virtualKeyId; default is crate ID, not physical key ID |
| virtualKey:true still uses physical | Default valid keyMode PHYSICAL takes precedence; set keyMode VIRTUAL explicitly |
| Extra requiredKeyIds ignored | Legacy costs fields have no active handler; use keyRequirements |
| Trigger/bulk options do nothing | Stored schema fields without implemented alternate-trigger/bulk-open flow in 2.3 |
| Global default cooldown does nothing | Set crate opening.cooldownSeconds; global cooldown fields have no runtime read |
| Staff never pays or sees cooldown | Creative skips deductions/cooldown; OP fallback can pass bypass node |
| Economy reward absent | Integration enabled plus actual registered provider required; vault default does not install a bundled bridge |
| Unexpected currency withdrawal | Missing-key alternative and costs.currencyCost add together |

Check both opening.permission and restrictions.requiredPermission. See [permissions](../administration/permissions) for OP fallback behavior. Permission-denial pushback has separate opening controls from generic pushback.

## Probabilities, limits and milestones

Configured preview percentages can differ from actual eligibility because dependencies, permissions, limits, fallback slots and pity filter the pool. Rarity does not independently set chance. Inspect weights and each limit; see [probability mechanics](../gameplay/keys-and-rewards).

Daily reward caps reset at UTC midnight. Player reward maps key by reward ID across crates, so reused IDs can share caps. Global caps include pending reservations. Do not delete global_limits.json to free a slot without reviewing pending openings.

One-time milestone claim flags are array-index based. Reordered entries can produce surprising claim behavior. Milestones are direct bonuses and do not use the ordinary weighted candidate filter. Restore intended ordering or plan a complete data migration rather than resetting isolated flags.

## Reward delivery

| Symptom | Checks |
| --- | --- |
| Item name differs from preview | displayName is preview metadata; customName renames actual item |
| Enchantments/components missing | Only custom_name, lore, custom_model_data and unbreakable map subset is applied |
| Captured hand item lost properties | addhand is limited field capture, not an arbitrary component clone |
| Item not in inventory | Check dropped overflow beside player; confirm registered item ID |
| Pokémon not in party | Check PC; adapter reconciles destination by exact UUID |
| Pokémon reward fails | Explicit species required, valid species/form and compatible Cobblemon; inspect delivery log |
| Egg is not a physical egg item | Egg reward creates egg-marked Pokémon in storage; hatching behavior is external-version dependent |
| Command uses wrong player | Server source executor is not winner; use player placeholder rather than @s |
| Delay/bonus command missing | Check frozen outbox/command callback and original dimension availability |
| Pending reward blocks openings | Restore original definition/provider and let recovery run, or perform reviewed admin settlement |

Ordinary failure reroll tries shuffled alternatives; it is not a second weighted draw. Exceptions and uncertain external effects can retain pending state. Before compensation, review `/crate pending status <player>` and actual inventory, party/PC, balances, permission nodes and command effect. See [recovery](../configuration/storage#pending-transactions-and-administrator-recovery).

## Visuals and editor

Use [models](../custom-content/models) for missing resource packs, customModelData mapping and ownership of crate displays; use [animations](../custom-content/animations) for companion capability and scene fallback issues.

Keep model idleYOffset, particle heightOffset and hologram offsets separate. Root hologram replaces nested appearance.hologram as a whole object. The file loader corrects negative model offsets and exactly 0.5 to 0. An invalid scale/hologram limit rejects the crate file rather than silently fixing every value.

When the cloud editor cannot create/download a session, inspect effective webEditor URLs, enabled setting, hash and transport log. Service availability is separate from server JSON: manual configuration remains usable. Use a fresh reviewed payload after configuration changes, and preserve configuration backups. Do not infer that an apply error left player state changed; apply edits content configuration, not player balances.

## Useful support evidence

Record Minecraft/Java/loader versions, exact UniCrates artifact/version on both sides, optional mod versions, crate filename/ID, relevant JSON sections, exact command and server diagnostic. For delivery issues include pending status and actual destination/economy evidence. Remove database passwords and webhook tokens before sharing configuration/log excerpts.

Source: current loader metadata, `ConfigManager`, `UniCratesCommand`, `LinkedCrateInteractHandler`, reward issuers and transaction recovery code.
