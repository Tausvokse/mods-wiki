# Permissions

UniCrates has one administrative node plus configurable crate/reward access rules. It consults LuckPerms when enabled, installed under the expected `luckperms` mod ID and available. Blank permission fields mean unrestricted access.

## Actual nodes

| Node / field | Use |
| --- | --- |
| `unicrates.admin` | Administrative command tree and editor authorization |
| `unicrates.bypass.cooldown` | Skip opening cooldown checks |
| `unicrates.crate.<crate_id>.preview` | Checked only when that crate's preview.requirePermissionToPreview is true |
| `opening.permission` | Arbitrary node chosen by server owner; checked for opening |
| `restrictions.requiredPermission` | Additional arbitrary opening node; both gates must pass |
| `rewards[].requiredPermissions` | Require every nonblank node for normal candidate pool |
| `rewards[].deniedPermissions` | Exclude reward when any nonblank node is granted |

`unicrates.crate.<id>.open` is a useful naming convention **only if you put it in a configuration field**. The handler does not automatically check it. There are no built-in nodes such as `unicrates.command.reload`, `unicrates.key.give`, `unicrates.stats`, `unicrates.use`, or a generic cost-bypass node.

## LuckPerms examples

```text
/lp group admin permission set unicrates.admin true
/lp group default permission set unicrates.crate.starter.preview true
/lp group vip permission set unicrates.crate.vip.open true
/lp group staff permission set unicrates.bypass.cooldown true
```

For the VIP opening node to have an effect, place it in the crate:

```json
"opening": {
  "openingType": "strip",
  "permission": "unicrates.crate.vip.open",
  "cooldownSeconds": 5
}
```

This is a crate-section fragment. Preview permissions are independent from opening permissions: a player may inspect a gated crate without permission to open it, unless you explicitly enable the preview gate.

## OP fallback details

When LuckPerms is available and enabled, ordinary permission checks return its result. When unavailable, checks fall back to vanilla OP level 2 unless LuckPerms is enabled and fallbackToOpIfMissing is false. If integration is disabled, nonblank ordinary nodes still use OP fallback.

**Administrative authorization has an additional OP level 2 fallback** in `isAdmin`, even when `fallbackToOpIfMissing` is false or LuckPerms denies unicrates.admin. Disabling that setting does not remove OP administrator access. The console checks permission level 2.

Without LuckPerms, adding nonblank permission nodes typically restricts normal players to OP access because vanilla does not provide arbitrary node assignment. Use empty nodes for public crates or install the supported permission integration.

Creative mode bypasses cost deductions and cooldowns in the interaction handler, but access/key-availability checks still run. Use a non-OP survival player when testing permissions, keys and costs. OP fallback also means an operator can pass `unicrates.bypass.cooldown` without an explicit LuckPerms grant when the provider is absent.

Permission rewards require LuckPerms presence. Their availability check is separate from the general permission-check enable flag; do not use that flag as a promise that existing permission rewards are removed from candidate pools.

Source: `PermissionChecker`, `UniCratesCommand`, `LinkedCrateInteractHandler`, `RewardRngEngine`, `PermissionRewardIssuer`.
