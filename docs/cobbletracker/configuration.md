# Configuration
CobbleTracker uses three main configuration files situated in `config/cobbletracker/`. They use a safe SnakeYAML parser restricted to basic structures.

## 1. `config.yml`
This is the primary settings file handling beams, minimaps, hunt settings, and the definitions of tracked categories.

**Example YAML Structure:**
```yaml
general-settings:
  chat-prefix: "&8[&bTracker&8]"
  hide-exact-position: true
  show-title: true

beam:
  enabled: true
  radius: 1
  duration-seconds: 60
  height: 256

minimap:
  enabled: true
  xaero: true
  voxelmap: true
  journeymap: true
  use-beam-color: true

hunt:
  enabled: true

trackers:
  shiny:
    name: "Shiny"
    spec: "isShiny"
    color: "#FFD700"
    max-stored: 25
    blacklist: ["magikarp", "rattata"]
    dimensions: ["minecraft:overworld"]
    on-spawn-commands:
      - "say A shiny spawned!"
    on-catch-commands:
      - "give %player% diamond 1"
    spawn:
      enabled: false
      chance: 0.1
      mode: "auto"
```

*   **`general-settings`**: Adjusts the chat prefix, title display, and whether coordinates are slightly obfuscated (`hide-exact-position`).
*   **`beam` & `minimap`**: Globally toggles and tunes the visual helpers (beam height/radius and minimap mod integrations).
*   **`trackers`**: Defines the `TrackerCategory` targets. A tracker needs a `spec` (like `"isShiny"` or `"!islegendary"`), a `color`, a `max-stored` limit for history trimming, dimension restrictions, blacklists, and lists of server commands to execute on spawn or catch. The nested `spawn` section configures native spawning if active.

## 2. `tracker.json`
Maintains persistent spawn history records across server restarts. The JSON is written off the main thread as a temporary file then moved over using atomic swaps (`StandardCopyOption.ATOMIC_MOVE`) to prevent data corruption.

**Example JSON Structure:**
```json
{
  "legendary": {
    "9a45610b-11d2-430b-9cf9-fb1bc6e6f1f3": {
      "species": "Mew",
      "species-id": "mew",
      "spawn-time": 1700000000,
      "world": "minecraft:overworld",
      "x": 100,
      "y": 64,
      "z": -150,
      "biome": "minecraft:jungle",
      "shiny": false,
      "caught": true,
      "outcome": "caught",
      "outcome-by": "Steve",
      "details": {
        "level": 50,
        "gender": "NONE",
        "nature": "Timid",
        "ability": "Synchronize",
        "ivs": "31/31/31/31/31/31"
      },
      "catcher-uuid": "00000000-0000-0000-0000-000000000000",
      "catcher-name": "Steve"
    }
  }
}
```
*   Stores `SpawnRecord` instances inside arrays keyed by UUID per tracker category. It keeps track of IVs, EVs, location, shiny status, outcome (caught/defeated), and catcher identity.

## 3. `legendaries.yml`
Dictates the context-aware rules (`LegendaryRule`) the `LegendaryDirector` uses when the built-in spawner attempts to place a legendary.

**Example YAML Structure:**
```yaml
legendaries:
  - species: "kyogre"
    weight: 1.0
    biomes:
      - "#minecraft:is_ocean"
      - "#minecraft:is_deep_ocean"
    dimensions:
      - "minecraft:overworld"
    time: "night"
    isRaining: true
    isThundering: false
    minY: 0
    maxY: 60
```
*   **`species`**: The internal species ID to spawn.
*   **`weight`**: The probability share compared to other valid choices.
*   **`biomes`**: Accepts both exact biome IDs or datapack tags (prefixed with `#`).
*   **`time` / `isRaining` / `isThundering` / `minY` / `maxY`**: Context rules restricting the spawn. For example, booleans are tri-state; if left out or undefined, the director doesn't check them.