# Commands
All commands can be localized (e.g., EN, RU) and display custom GUIs rather than basic chat text. 

### `/rank` (Matchmaking & Leaderboard)
- `/rank hub` – Opens the main Rank Hub GUI to view ratings and enter queues.
- `/rank queue &lt;format&gt;` – Joins the matchmaking queue for a specific format.
- `/rank leave` – Leaves the matchmaking queue.
- `/rank challenge &lt;player&gt; &lt;format&gt;` – Sends a direct, ranked challenge to another player, bypassing the public queue.
- `/rank top &lt;format&gt;` – Displays the top players for a given format (opens a GUI for players, prints to chat for console).
- `/rank stats` – Displays the executor's rating statistics across all formats.
- `/rank history` – Shows the executor's recent match history and `Δμ` changes.
- `/rank theme <name>` – Changes the client-side GUI theme.
- **Admin Commands (Permission Level 2):**
  - `/rank showfor &lt;player&gt; &lt;hub|stats|history|top&gt; [format]` – Force-opens a rank screen on a target player's client.
  - `/rank admin setrating &lt;player&gt; &lt;format&gt; &lt;mu&gt;` – Manually sets a player's rating.
  - `/rank admin season &lt;format&gt;` – Soft-resets the season for a given format (pulling ratings toward the baseline).

### `/tourney` (Tournaments)
- `/tourney list` – Lists all current and past tournaments.
- `/tourney join &lt;id&gt;` – Registers the executor for a tournament.
- `/tourney bracket &lt;id&gt;` – Opens the visual tournament bracket GUI.
- **Admin Commands (Permission Level 2):**
  - `/tourney create &lt;format&gt; &lt;type&gt;` – Creates a new tournament. Supported types: `single_elimination`, `double_elimination`, `round_robin`, `swiss`.
  - `/tourney start &lt;id&gt;` – Transitions a tournament from registration to the running state, generating the bracket.
  - `/tourney admin` – Opens the tournament administration control panel.
  - `/tourney forcejoin &lt;id&gt; &lt;player&gt;` – Manually adds a player to a tournament (useful for manual seeding).
  - `/tourney dq &lt;id&gt; &lt;player&gt;` – Disqualifies a player, automatically advancing their opponent.
  - `/tourney forceadvance &lt;id&gt; &lt;round&gt; &lt;slot&gt; &lt;player&gt;` – Manually records a winner for a specific bracket cell.
  - `/tourney showfor &lt;player&gt; &lt;list|admin|bracket&gt; [id]` – Force-opens a tournament screen on a target player's client.