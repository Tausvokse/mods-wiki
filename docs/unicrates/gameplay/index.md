# Gameplay

UniCrates connects a placed crate anchor to a server-defined reward pool. The server checks access, keys, payment, cooldown and reward eligibility before confirming an opening. The visual sequence does not let the client set its own reward or probability.

## Preview and opening

| Action | Current behavior |
| --- | --- |
| Shift + right-click crate | Request preview |
| Left-click/attack crate | Preview when enabled and authorized |
| Empty-handed right-click | Preview if no usable virtual key and no positive purchase alternative; otherwise attempt opening |
| Main-hand physical key + right-click | Attempt opening with that key (or virtual first in BOTH mode) |
| `/crate preview <id>` | Open allowed crate preview without targeting anchor |
| `/crate key balance [crate]` | Inspect own physical/virtual balance |

Only main-hand interaction initiates the ordinary item interaction path. Physical keys must be real UniCrates key items with accepted identity components, not renamed vanilla items. Keys lying elsewhere in inventory are counted for multi-key requirements, but the normal physical single-key path checks the held stack.

Empty-handed preview is therefore not universal: a player with virtual keys may spend one, and a crate with a purchase alternative may try an economy opening. Shift-right-click is the reliable explicit preview request. Schema trigger options do not change this handler behavior in 2.3.

Preview must be enabled and may require `unicrates.crate.<id>.preview`. Opening may have independent permissions and dimension restrictions. A preview is information, not a reservation of a displayed reward. The companion preview calculates configured-weight percentages; actual eligible odds can differ because of permissions, installed integrations, exhausted limits, fallbacks and pity.

## Opening styles

| Style | Player experience |
| --- | --- |
| strip / roulette / reels / wheel | GUI presentation of the server-selected result |
| instant | Confirm reward without prolonged presentation |
| world_animation | In-world sequence around the crate |
| selectable | Choose configured number of cards from revealed pool |
| interactive_pokeball / interactive_3d | Select a displayed in-world ball through supported interaction |
| cinematic / scene route | Pokémon scene according to server settings and companion capabilities |

The [animation guide](../custom-content/animations) explains exact mode routing, scene variants and fallback behavior. Companion installation improves screens and scenes; server-only paths have different fallback interfaces.

Large companion preview/card lists paginate with arrow buttons, mouse wheel and Left/Right or Page Up/Page Down. Long reward tooltips scroll when necessary; Home/End moves through overflowing name text. When multiple cards must be claimed, the menu stays open after the first; Claimed is shown after server confirmation, and closing requires the configured number of claims or recovery handling.

## Costs, denials and concurrency

An opening can require a physical/virtual key, multiple key types, XP levels, XP points and registered economy currency. A positive purchase alternative replaces a missing normal key, while additional configured costs still apply. Requirements are server-side. Permission failure, missing keys, insufficient payment, dimension denial, lifetime cap, cooldown, unavailable reward pool or active opening can prevent an opening; denial pushback/sound may be configured.

One player cannot start a second opening while an opening or scene is active. An anchor already in use is protected from overlapping openings. Wait for completion instead of repeatedly clicking. A pending reward can also block new openings until it is settled or recovered.

Creative mode skips deductions and cooldown, and OP fallback can grant cooldown bypass; testing as staff does not reproduce ordinary survival costs. See [permissions](../administration/permissions).

## Receiving rewards and interrupted openings

Items are split into normal stacks and inserted into inventory; uninserted remainder drops by the player. Pokémon use party storage and may overflow into PC. Key rewards deliver physical keys. Economy/permissions use their registered external providers. Bonus commands can accompany any reward type.

Interrupted/offline reward handling preserves pending identities where supported. Log in again to allow normal recovery. If you see a pending transaction, unavailable configuration or external payment review message, contact staff rather than assuming the payment was refunded. Administrator recovery is documented in [storage and recovery](../configuration/storage).

Read [keys, probability, pity and milestones](./keys-and-rewards) for reward mechanics, or [reward fields](../custom-content/rewards) to define content.

Source: `CrateAnchorBlock`, `LinkedCrateInteractHandler`, platform GUI routes, `RewardDelivery`, client preview/selectable screens.
