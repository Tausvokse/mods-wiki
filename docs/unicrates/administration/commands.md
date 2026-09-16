# Commands Reference

All UniCrates commands use the root command `/crate` (or alias `/unicrates`).

---

## Command Table

| Command | Description | Default Permission |
| :--- | :--- | :--- |
| `/crates editor` | Generate a temporary web editor session link (LuckPerms style) to visually create/configure crates and animations in browser. | OP Level 2 (`unicrates.admin`) |
| `/crates apply <hash>` | Download and safely apply modified crate and animation configurations from the web editor. | OP Level 2 (`unicrates.admin`) |
| `/crate create <name>` | Create a crate anchor on the targeted block, aligning orientation to player look angle. | OP Level 2 (`unicrates.admin`) |
| `/crate remove` | Remove the targeted crate anchor cleanly and despawn holograms/displays. | OP Level 2 (`unicrates.admin`) |
| `/crate edit [crate]` | Open in-game visual GUI editor with sliders for scale, height, and particles. | OP Level 2 (`unicrates.admin`) |
| `/crate list` | List all currently loaded crates, active anchors, and storage status. | OP Level 2 (`unicrates.admin`) |
| `/crate reload` | Hot-reload all configs, crates, animations, language files, and rebuild resource pack. | OP Level 2 (`unicrates.admin`) |
| `/crate give <player> <crate> [amount]` | Give portable crate item(s) to a player. | OP Level 2 (`unicrates.admin`) |
| `/crate key give <player> <crate> [amount]` | Grant physical or virtual keys to a player. | OP Level 2 (`unicrates.admin`) |
| `/crate key take <player> <crate> [amount]` | Deduct keys from a player's balance or inventory. | OP Level 2 (`unicrates.admin`) |
| `/crate key set <player> <crate> <amount>` | Set a player's virtual key balance to a specific value. | OP Level 2 (`unicrates.admin`) |
| `/crate key balance [player] [crate]` | View virtual key balances for yourself or another player. | All Players |
| `/crate preview <crate>` | Open the graphical reward probability preview GUI. | All Players (`unicrates.crate.<id>.preview`) |
| `/crate info <crate>` | Print crate technical details, mathematical odds, and limits to chat. | All Players |
| `/crate stats [player] [crate]` | View opening statistics, pity counter progress, and daily limits. | All Players / OP Level 2 |
