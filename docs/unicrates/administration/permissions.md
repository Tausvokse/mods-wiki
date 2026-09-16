# Permissions Reference

UniCrates integrates with **LuckPerms** (or any standard permission provider) while falling back to vanilla OP levels (Level 2) if no permission manager is installed.

---

## Administrative Permissions

| Permission Node | Description | Default Level |
| :--- | :--- | :--- |
| `unicrates.admin` | Full wildcard administrative access to all commands, editors, and bypasses. | OP Level 2 |
| `unicrates.command.create` | Permission to place and configure in-world crate anchors. | OP Level 2 |
| `unicrates.command.remove` | Permission to delete crate anchors. | OP Level 2 |
| `unicrates.command.edit` | Permission to open the in-game GUI editor. | OP Level 2 |
| `unicrates.command.reload` | Permission to hot-reload configs, crates, and animations. | OP Level 2 |
| `unicrates.command.key` | Permission to give, take, or set player keys. | OP Level 2 |
| `unicrates.command.give` | Permission to give portable crate items. | OP Level 2 |

---

## Bypass Permissions

These permissions allow admins or privileged players to bypass opening limitations:

| Permission Node | Description | Default Level |
| :--- | :--- | :--- |
| `unicrates.bypass.cost` | Open crates without consuming physical or virtual keys. | OP Level 2 |
| `unicrates.bypass.cooldown` | Bypass cooldown timers between crate rolls. | OP Level 2 |
| `unicrates.bypass.limits` | Bypass daily and lifetime reward limits. | OP Level 2 |

---

## Player Permissions

| Permission Node | Description | Default Level |
| :--- | :--- | :--- |
| `unicrates.crate.<id>.open` | Required if the crate has `restrictions.requiredPermission` set to this node. | Configurable |
| `unicrates.crate.<id>.preview` | Required if the crate has `preview.requirePermissionToPreview: true`. | Granted if not restricted |
| `unicrates.command.preview` | Allows using `/crate preview <id>` command. | All Players |
| `unicrates.command.balance` | Allows checking virtual key balances via `/crate key balance`. | All Players |
| `unicrates.command.stats` | Allows checking personal opening history and pity progress. | All Players |
