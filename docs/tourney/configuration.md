# Configuration
The engine reads from `config/cobbletourney.json`. It covers rating parameters, matchmaking constraints, arena coordinates, and format-specific clauses.

- **Rating Settings:** Controls the Glicko-2 `rating_tau`, the number of `provisional_games`, and how often inactivity degrades the rating (`rating_decay_period_millis`).
- **Matchmaking Settings:** Controls the `matchmaking_base_delta` and `matchmaking_max_delta` for the search window, `matchmaking_ramp_millis` for expansion speed, and `rematch_cooldown_millis` to prevent sniping.
- **Arena (Optional):** Teleports players to a specific location for their matches by setting `enabled` to `true` and defining `dimension`, `pos1`/`pos2` arrays, and yaw values.
- **Clauses:** Configured per-format inside the `clauses` block. You can enforce standard boolean clauses (e.g., `species_clause`, `sleep_clause`), define a `level_cap`, set `min_team_size` / `max_team_size`, and outline arrays of banned species, moves, items, or abilities.

**Example `config/cobbletourney.json`:**
```json
{
  "rating_tau": 0.5,
  "provisional_games": 15,
  "rating_decay_period_millis": 86400000,
  "matchmaking_base_delta": 50.0,
  "matchmaking_max_delta": 500.0,
  "matchmaking_ramp_millis": 120000,
  "min_candidate_pool": 1,
  "rematch_cooldown_millis": 86400000,
  "chat_prefix": "[Tourney]",
  "arena": {
    "enabled": true,
    "dimension": "minecraft:overworld",
    "pos1": [8.5, 65.0, 0.5],
    "pos2": [8.5, 65.0, 16.5],
    "yaw1": 180.0,
    "yaw2": 0.0
  },
  "rewards": {
    "enabled": true,
    "champion_loot_table": "cobbletourney:rewards/champion",
    "runner_up_loot_table": "cobbletourney:rewards/runner_up"
  },
  "clauses": {
    "singles-6v6-ou": {
      "species_clause": true,
      "item_clause": true,
      "sleep_clause": true,
      "evasion_clause": true,
      "ohko_clause": true,
      "endless_battle_clause": true,
      "level_cap": 50,
      "min_team_size": 6,
      "max_team_size": 6,
      "banned_species": ["mewtwo", "rayquaza"],
      "banned_moves": [],
      "banned_items": [],
      "banned_abilities": []
    }
  }
}
```