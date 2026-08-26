# Configuration
The mod utilizes a TOML configuration file typically named `whosthatpokemon-server.toml` (located in the server config directory). 

### Configuring Pokémon
The `allowed_pokemon` list specifies which Pokémon can appear in the game. It supports localized names by using an equals sign `=`. The English/internal name must be on the left, and comma-separated localized names on the right.
```toml
allowed_pokemon = [
    "pikachu=Пикачу",
    "bulbasaur=Бульбазавр,Булбасаур",
    "charizard"
]
```

### Rewards Configuration
You can configure both direct item drops, loot tables, and commands.
```toml
# Use a data-driven loot table instead of direct items
loot_table_id = "minecraft:chests/village/village_desert_house"

# Fallback direct item rewards (format: "item_id;base_amount")
rewards = ["minecraft:diamond;1", "minecraft:emerald;5"]

# Commands to run upon a correct guess. 
# Prefix with "chance;" for a probability roll. Placeholders: %player%, %score%, %x%
reward_commands = ["0.5;give %player% minecraft:golden_apple 1", "say %player% guessed correctly!"]
```

### Points and Penalties
The leaderboard point system strictly dictates how points are gained and lost:
```toml
reward_points = 50          # Points gained for a correct guess
penalty_wrong_guess = 10    # Points lost per incorrect guess
penalty_timeout = 10        # Points lost if time runs out
penalty_surrender = 10      # Points lost if the player closes the GUI (surrenders)
```

### Difficulty & Hints
You can adjust the difficulty tier and configure hint costs. 
```toml
max_attempts = 3
session_timeout_seconds = 30
difficulty = "medium"       # Can be "easy", "medium", or "hard"

enable_hints = true
hint_cost = 15              # Score deducted to reveal a hint
max_hints_per_round = 2
```