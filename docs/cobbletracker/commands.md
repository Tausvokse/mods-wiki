# Commands
CobbleTracker uses a robust command tree built on Brigadier. Permissions are soft-dependent on LuckPerms (checking `cobbletracker.command.<name>` nodes via reflection) and seamlessly fall back to vanilla operator levels if LuckPerms is absent.

*   `/cobbletracker` (Aliases: `/ct`, `/last`, `/ll`)
    *   **Permission:** `cobbletracker.command.gui` (Anyone)
    *   **Function:** Opens the client-side tracker GUI containing recent spawn history.
*   `/cobbletracker reload`
    *   **Permission:** `cobbletracker.command.reload` (Operator)
    *   **Function:** Hot-reloads the configuration files (`config.yml`, `announcements.yml`). Rejects the reload and keeps the previous state if the YAML files are malformed.
*   `/cobbletracker admin`
    *   **Permission:** `cobbletracker.command.admin` (Operator)
    *   **Function:** Opens the in-game admin screen to edit settings live.
*   `/cobbletracker fakehit`
    *   **Permission:** `cobbletracker.command.fakehit` (Operator)
    *   **Function:** Spawns a shiny test Pikachu at the admin's location to verify announcements, beams, and webhooks.
*   `/cobbletracker waypoint &lt;id&gt;`
    *   **Permission:** `cobbletracker.command.waypoint` (Anyone)
    *   **Function:** Receives a unique spawn ID and places a waypoint at its coordinates on the player's minimap.
*   `/cobbletracker notify`
    *   **Permission:** `cobbletracker.command.notify` (Anyone)
    *   **Function:** Prints the player's notification preferences.
*   `/cobbletracker notify &lt;category&gt; [on|off|sound|radius]`
    *   **Permission:** `cobbletracker.command.notify` (Anyone)
    *   **Function:** Modifies individual notification settings (toggling on/off, modifying sound alerts, or adjusting block radius) for a specific tracker category.
*   `/cobbletracker theme <name>`
    *   **Permission:** `cobbletracker.command.theme` (Anyone)
    *   **Function:** Pushes a specified GUI theme palette to the client.
*   `/lastlegend`
    *   **Permission:** `cobbletracker.command.lastlegend` (Anyone)
    *   **Function:** Opens the legendaries tab of the GUI if the mod is installed, or outputs a fallback chat rundown for vanilla clients.
*   `/checklegendary`
    *   **Permission:** `cobbletracker.command.checklegendary` (Anyone)
    *   **Function:** Calculates and prints what legendaries can spawn in the player's current location based on biome and time rules, and reports when the next spawn attempt is.
*   `/spawnlegendary`
    *   **Permission:** `cobbletracker.command.spawnlegendary` (Operator)
    *   **Function:** Spends one scheduled spawn attempt right now using the same context rules to force a legendary to appear nearby.