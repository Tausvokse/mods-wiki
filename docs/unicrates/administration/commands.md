# Commands

Both `/crate` and `/crates` register the same command tree. Commands below use `/crate`; omit the slash in a dedicated server console. `<value>` is required; `[value]` is optional. Player arguments using Minecraft's player selector must resolve to **one online player**.

An administrator is a player with `unicrates.admin` or vanilla OP level 2. The server console uses permission level 2. There are no separate per-subcommand administrative nodes in the current command tree.

## Command reference

| Syntax | Access / executor | Result |
| --- | --- | --- |
| `/crate create <crate>` | Admin player | Replace targeted block within 6 blocks with a crate anchor linked to existing crate ID |
| `/crate remove` | Admin player | Remove targeted linked anchor |
| `/crate edit [crate]` | Admin player | Open in-game editor; without ID, target a placed crate |
| `/crate editor` | Admin | Create web editor session; integration must be enabled |
| `/crate apply <hash>` | Admin | Download, validate and apply web editor payload |
| `/crate info <crate>` | Admin | Print configured crate information and weights |
| `/crate list` | Admin | List loaded crates |
| `/crate give <player> <crate> <amount>` | Admin | Give portable crate anchor items; **amount is required**, integer ≥1 |
| `/crate key give <player> <crate> [amount] [type]` | Admin | Grant physical keys or virtual balance; amount defaults 1, must be ≥1 |
| `/crate key take <player> <crate> [amount] [type]` | Admin | Remove matching physical/virtual keys; amount defaults 1, must be ≥1 |
| `/crate key set <player> <crate> <amount> [type]` | Admin | Set matching key count/balance; integer ≥0 |
| `/crate key balance` | Player | Show own nonzero key balances |
| `/crate key balance <crate>` | Player | Show own physical and virtual balance for a loaded crate |
| `/crate key balance <player> [crate]` | Admin to inspect others | Show one online player's balances |
| `/crate preview <crate>` | Player | Open preview if enabled; optional preview permission applies |
| `/crate stats <player> [crate]` | Admin | Show player's opening/win statistics and up to ten history entries |
| `/crate reward add <crate> hand [weight] [rarity]` | Admin player | Add held item/Pokémon representation as reward |
| `/crate addhand <crate> [weight] [rarity]` | Admin player | Alias for held reward capture |
| `/crate exportpack` | Admin | Assemble pack into `config/unicrates/exported-resourcepack/` |
| `/crate reload` | Admin | Reload main/Discord/crates/timelines and optionally generate pack |
| `/crate pending status <player>` | Admin | Review pending identities, intent and fingerprint |
| `/crate pending adopt-current <player> <transaction> <fingerprint> accept-replay-risk` | Admin | Adopt current command snapshots for legacy pending transaction; no immediate payout |
| `/crate pending mark-settled <player> <operation> <fingerprint> no-issue-no-refund` | Admin | Close reviewed pending opening without reward or refund |

There is no `/crate open`, `/crate reset`, `/crate delete`, `/crate key giveall`, `/crate backup`, `/crate rollback`, or offline-player mutation command in this tree. `create` places an already-loaded definition; it does not create the definition JSON. Use the editor or [JSON recipes](../custom-content/json) to define a new crate first.

## Key command rules

Use explicit `physical` or `virtual` for predictable administration:

```text
/crate key give Alex starter 5 physical
/crate key give Alex starter 5 virtual
/crate key take Alex starter 2 virtual
/crate key set Alex starter 0 virtual
/crate key balance Alex starter
```

For give/take, the literal type may be supplied without amount: `/crate key give Alex starter virtual`. With an amount, the final type accepts physical/virtual and the helper's short forms p/v. Prefer the documented full forms; arbitrary strings are not an alternative key storage backend.

Without type, `VIRTUAL` crates default to virtual. Give/set on `BOTH` default to physical. Take on `BOTH` removes virtual first, then physical if more are needed. A virtual mutation addresses `key.virtualKeyId` or crate ID when blank. Physical removal counts accepted identities in inventory. Physical give uses inventory insertion and drops overflow.

A single argument after balance is interpreted as a loaded crate ID **before** it is interpreted as a player name. If a player and crate share a name, use the explicit two-argument form for the player. Balance output is by loaded crate; a shared key identity may appear under more than one accepting crate.

## Placing and editing

```text
/crate list
/crate create starter
/crate give Alex starter 1
/crate edit starter
/crate info starter
```

`create` replaces the block you point at, captures facing from your yaw plus 180 degrees, and assigns the loaded ID. It does not preserve the replaced block. Use a dedicated pedestal/anchor location. `edit` without an ID searches the targeted crate and nearby ray path within 6 blocks.

Held reward capture defaults to weight **10.0**, rarity **rare**. Explicit weight must be at least 0.01. The rarity suggestion list includes common through legendary; the schema also recognizes mythic. Captured custom item data is limited to supported fields, not every ItemStack component; see [reward component support](../custom-content/rewards#data-component-support).

## Reload, pack export and web apply

`reload` reports loaded/failed crate files and animation warnings. Invalid files are omitted from the rebuilt registry. It does not switch the active storage destination or register a newly selected economy provider; restart for those changes.

`exportpack` creates a directory, not a hosted download or server-resource-pack URL. Distribution and client loading of that pack are separate tasks; see [models](../custom-content/models).

`apply` validates a staged editor payload and preserves a configuration snapshot before replacement. Review the editor content before applying. It does not restore player balances, reset statistics or back up databases.

Player query commands (preview, balance, stats and pending review/actions) share a 500 ms per-player rate gate. Client configuration-save packets have a separate 2-second gate. A rate-limit message means wait before repeating the operation; it does not imply the preceding transaction failed.

## Recovery commands

Start with `/crate pending status Alex`. Copy the **current** fingerprint and retain the review output. Keep the player still and review again after any player/configuration state change. Settlement uses a new operation UUID you choose; preserve the UUID and fingerprint for an exact retry.

`adopt-current` is intended for legacy pending commands without their original frozen snapshot. It accepts current replacement commands and possible replay, persists snapshots and relies on normal recovery at next login. It is not a refund or immediate reward command.

`mark-settled` closes the whole reviewed opening with **no issue and no refund**. It records settlement/known reservation cleanup and retains diagnostic evidence for unknown or conflicting identities. Read [storage and recovery](../configuration/storage#pending-transactions-and-administrator-recovery) before using either mutation.

Source: `common/.../command/UniCratesCommand.java`, `PermissionChecker`, `ServerActionRateLimits`.
