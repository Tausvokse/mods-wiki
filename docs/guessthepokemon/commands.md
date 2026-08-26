# Commands
All commands are prefixed with `/wtp`.

*   `/wtp` or `/wtp play`
    *   **Description:** Starts a new minigame session and opens the GUI for the player.
    *   **Permission:** None (available to all players).
*   `/wtp top`
    *   **Description:** Displays the top 10 players on the leaderboard (in a GUI or via chat messages).
    *   **Permission:** None.
*   `/wtp reload`
    *   **Description:** Notifies the user that the configuration can be edited in the server config folder. (Actual dynamic reloading depends on Forge/Fabric config mechanisms).
    *   **Permission:** `wtp.command.reload` or Operator Level 2.
*   `/wtp reset`
    *   **Description:** Resets the player's own active cooldown, allowing them to play again immediately.
    *   **Permission:** `wtp.command.reset` or Operator Level 2.
*   `/wtp reset &lt;player&gt;`
    *   **Description:** Resets the active cooldown of a specified target player.
    *   **Permission:** `wtp.command.reset` or Operator Level 2.

---