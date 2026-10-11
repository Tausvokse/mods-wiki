# Keys, probability, pity and milestones

## Physical and virtual keys

Physical keys are `unicrates:crate_key` items whose identity is stored as a registered data component. Name/lore/model customize presentation; the identity determines eligibility. A portable crate anchor similarly stores which crate definition it represents. Ordinary renamed vanilla items cannot impersonate these identities.

Virtual keys are integer balances in the player's UniCrates record. `key.virtualKeyId` chooses the ledger ID, otherwise crate ID is used. Virtual keys have no inventory item, cannot be dropped by ordinary item actions, and are administered through key commands.

| Mode | Ordinary opening source |
| --- | --- |
| `PHYSICAL` | Accepted key held in main hand |
| `VIRTUAL` | Positive balance in configured ledger |
| `BOTH` | Spend virtual first; use held physical key if virtual balance is empty |

`key.consumeOnOpen=false` makes the ordinary key reusable; enabled multi-key requirements consume planned deductions independently. `keyRequirements.mode=ALL` requires all entries, while ANY chooses the first satisfied entry. Entry type ANY combines virtual and physical quantity, virtual first. Use [crate reference](../configuration/crate-reference#multiple-key-requirements) for exact fields.

Shared key IDs can let one key open multiple crates. Shared virtual IDs intentionally share a balance. Commands still identify the crate definition to resolve which identity and visuals to grant:

```text
/crate key give Alex starter 5 virtual
/crate key balance starter
```

There is no ordinary player exchange/buy-key command. `purchaseCostAlternative` pays for an opening when its normal key is absent; it does not first grant a reusable inventory key.

## Weighted probabilities

Weight is relative, not percent. For eligible candidates A weight 80, B weight 15, C weight 5, their probabilities are 80%, 15%, 5%. Weights 8, 1.5, 0.5 give the same probabilities. Weights 80 and 20 have 80/20 chances; adding a weight-100 third reward changes them to 40/10/50.

For an ordinary draw:

```text
chance(candidate) = candidate weight / sum of current eligible candidate weights
```

Before the draw the engine excludes nonpositive/nonfinite weights, unrecognized/unimplemented types, reward permission failures and exhausted limits. Missing optional integrations can therefore change probabilities. Reward rarity labels do not change weight by themselves. The core supports a rarity multiplier hook; the standard block-opening handler uses `RewardWeightModifier.NONE`.

Companion preview and `/crate info` show configured-weight information, not a fully personalized guarantee of eligible chances. The companion preview data is built from configured reward rows. Fallback server preview may hide exhausted rows, but its displayed probability is still not an authoritative transaction-time pool calculation.

## Exhaustion and fallback substitution

Example: gold has weight 80, diamond weight 20. Diamond has a one-win player cap and fallbackRewardId gold. Before the cap: gold 80%, diamond 20%. After diamond is exhausted: its 20-weight slot pays gold, so gold effectively gets 100%.

Fallback retains the exhausted reward's original weight. It must reference another existing reward in the same crate, pass permissions/dependency availability and be unexhausted. Missing/invalid/exhausted fallback drops that slot entirely. Fallback chains are not recursively evaluated. A fallback can have zero normal weight yet still receive a substituted slot.

Global limits include active reservations as well as delivered wins so simultaneous openings cannot freely consume the same final global slot. Global state is keyed by crate/reward. Player lifetime and daily counters are keyed by reward ID alone; reuse across crates shares these player caps. Daily counters reset at **UTC midnight**, not server-local midnight.

Only positive limit values enforce exhaustion. Deleting/recreating the same JSON does not reset saved counters. Changing IDs creates different identity relationships; do not use renames as an unreviewed reset while pending transactions exist.

## Pity

Global pity is disabled by default. Example main-config section:

```json
"pitySystem": {
  "enabled": true,
  "guaranteedMinimumRarity": "rare",
  "guaranteedAfterOpens": 10
}
```

The counter is separate for each player and crate. A natural rare-or-higher win resets it. After nine consecutive below-rare wins, the tenth draw uses eligible rare-or-higher candidates only, preserving their relative weights. An epic, legendary or mythic win also satisfies a rare minimum.

If no eligible rare-or-higher reward remains, the engine rolls from the ordinary eligible pool and keeps the increasing pity counter. Pity does not bypass reward permissions, unavailable integration types or exhausted caps. It is a tier guarantee when candidates exist, not a guarantee of one specific species/item.

The standard random-opening decision applies this mechanism. Selectable/card pools and direct milestone issuance have their own paths; do not advertise a pity guarantee for every opening mode without checking its runtime route.

## Milestones

Milestones issue bonus rewards after configured opening counts. Entries reference existing reward IDs. A zero-weight reward is useful for milestone-only content.

```json
"milestones": [
  { "openings": 10, "rewardId": "ten_open_bonus", "repeatEvery": false },
  { "openings": 50, "rewardId": "fifty_open_bonus", "repeatEvery": true }
]
```

The first is claimed once when the player's new opening total reaches/passes 10. The second triggers at 50, 100, 150, etc. Several milestones can trigger on one opening. One paid selectable opening counts once even if several cards are granted.

One-time claims use milestone **array index**. Reordering entries on a live server can change which claim flag corresponds to which reward; preserve the order or plan a data migration. Milestone displayName and broadcast fields exist in the model but are not read by current delivery. The player receives a bonus message based on reward display name.

Milestones issue referenced rewards directly rather than running the normal weighted/permission/exhaustion candidate filter. Design milestone bonuses for their actual audience; do not assume ordinary win limits or permission lists automatically restrict them. Pending milestone transaction identities allow delivery to be tracked separately from an already confirmed primary result.

## Failure is different from a new weighted roll

`rerollOnFailure=true` is default. If an issuer explicitly returns false, the primary delivery path shuffles positive-weight alternatives and tries eligible ones. It does not repeat the original weighted probability calculation. A failed or ambiguous external call may retain pending state instead; `true` does not guarantee a successful replacement.

Changing config during an unfinished opening can prevent pending recovery if its crate/reward IDs disappear. Prepared command and Pokémon snapshots preserve selected details, but original context still matters. See [storage and recovery](../configuration/storage).

Source: `RewardRngEngine`, `WeightedRewardSelector`, `CrateOpenService`, `KeyRequirementEngine`, `LinkedCrateInteractHandler`, `GlobalLimitStore`, `RewardDelivery`, `CratePreviewMenu`.
