# Features
## GUI Mechanics
The mod provides a visual minigame using a client-side GUI. When a session starts, the server sends an `S2C_OpenWtpGuiPacket` to the client, which opens a graphical interface displaying the silhouette of a random Pokémon. As the player guesses, hints can be requested (if enabled), which display the first letter of the Pokémon's name and its length. 
When the player either guesses correctly, exhausts all their attempts, or surrenders, the server sends an `S2C_RevealPokemonPacket`. This packet reveals the true Pokémon sprite, plays sound effects (if `enable_sounds` is true), and shows the final score and remaining attempts. A rate limit (`rate_limit_ms`) ensures the server isn't spammed with guesses.

## Leaderboard
The leaderboard ranks players by their cumulative points. When a player types `/wtp top`, the `LeaderboardAPI` retrieves the top 10 highest-scoring players. 
- If `leaderboard_gui_enabled` is set to `true`, players receive an `S2C_OpenLeaderboardPacket`, opening a visually formatted GUI showing the top players and the player's personal rank.
- If disabled or if the command is run from the console, the top 10 list is printed directly in the chat.
The leaderboard data is periodically saved to disk based on the `leaderboard_save_interval_seconds` setting.

## Difficulty Tiers & Timer
The game features a strict timer (`session_timeout_seconds`), managed by the `ServerManager`, which penalizes players if they fail to guess the Pokémon before time runs out. The difficulty tier (`difficulty`) directly affects this timer:
- **Easy:** Grants an additional 15 seconds to the base `session_timeout_seconds`.
- **Medium:** Uses the base `session_timeout_seconds` without modification.
- **Hard:** Subtracts 10 seconds from the base timer (capped at a minimum of 10 seconds).

## Rewards & Loot Tables
Winning a round correctly yields rewards, which can be configured to integrate directly with Minecraft's data-driven Loot Tables or fallback item rewards.
- **Loot Tables:** If a `loot_table_id` is defined (e.g., `minecraft:chests/simple_dungeon`), the mod generates context-aware loot at the player's position, taking their Luck attribute into account.
- **Direct Items:** If no Loot Table is specified, it picks a random entry from the `rewards` list (e.g., `minecraft:emerald;5`). The amount of items granted increases dynamically with the player's score bonus (`baseAmount + (currentScore / 100)`).
- **Reward Commands:** Additionally, custom console commands can be executed via `reward_commands` with chance logic (e.g., `0.5;/give %player%...`) and placeholders like `%player%`, `%uuid%`, `%score%`, and coordinates.

---