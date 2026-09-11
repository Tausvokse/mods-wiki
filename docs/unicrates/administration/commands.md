# Commands Reference

All UniCrates commands use the root command `/crate` (or alias `/unicrates`).

---

## Command Table

| Command | Description | Default Permission |
| :--- | :--- | :--- |
| `/crate create <name>` | Create a crate anchor on the targeted block, aligning orientation to player look angle. | OP Level 2 (`unicrates.admin`) |
| `/crate remove` | Remove the targeted crate anchor cleanly and despawn holograms/displays. | OP Level 2 (`unicrates.admin`) |
| `/crate edit [crate]` | Open in-game visual GUI editor with sliders for scale, height, and particles. | OP Level 2 (`unicrates.admin`) |
| `/crate studio [anim_id]` | Open the **Visual Animation Studio** to design and live-preview opening sequences. | OP Level 2 (`unicrates.admin`) |
| `/crate bundle <crate> <reward>` | Open the 27-slot visual drag-and-drop item bundle editor for compound drops. | OP Level 2 (`unicrates.admin`) |
| `/crate list` | List all currently loaded crates, active anchors, and storage status. | OP Level 2 (`unicrates.admin`) |
| `/crate reload` | Hot-reload all configs, crates, animations, language files, and rebuild resource pack. | OP Level 2 (`unicrates.admin`) |
| `/crate give <player> <crate> [amount]` | Give portable crate item(s) to a player. | OP Level 2 (`unicrates.admin`) |
| `/crate key give <player> <crate> [amount]` | Grant physical or virtual keys to a player. | OP Level 2 (`unicrates.admin`) |
| `/crate key take <player> <crate> [amount]` | Deduct keys from a player's balance or inventory. | OP Level 2 (`unicrates.admin`) |
| `/crate key set <player> <crate> <amount>` | Set a player's virtual key balance to a specific value. | OP Level 2 (`unicrates.admin`) |
| `/crate key balance [player] [crate]` | View virtual key balances for yourself or another player. | All Players |
| `/crate preview <crate>` | Open the graphical reward probability preview GUI. | All Players (`unicrates.crate.<id>.preview`) |
| `/crate massopen <crate>` | Open the mass-open batch selector (x1, x5, x10, x25, All) and results summary. | All Players |
| `/crate info <crate>` | Print crate technical details, mathematical odds, and limits to chat. | All Players |
| `/crate stats [player] [crate]` | View opening statistics, pity counter progress, and daily limits. | All Players / OP Level 2 |
| `/crate anim <animation_id>` | Test-play an animation timeline at your current looking position. | OP Level 2 (`unicrates.admin`) |
