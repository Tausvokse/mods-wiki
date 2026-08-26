# Features
The Cobblemon Tournament engine brings structured, automated competitive mechanics natively into the game. Its core features are driven by robust backend systems:

- **Glicko-2 Rating System:** Player ratings are calculated using the industry-standard Glicko-2 algorithm (with a starting `μ` of 1500, a starting `RD` of 350, and volatility `τ`). The system accounts for inactivity by decaying the RD (Rating Deviation) over time, ensuring matchmaking remains accurate for returning players. Players also undergo a **Provisional Phase** for their first set of games to calibrate their ratings quickly. The engine uses a strict closed-loop state machine (`IN_BATTLE → SETTLING → IDLE`) to prevent players from exploiting "dirty" ratings by queuing before their previous match transaction fully settles.
- **Anti-Sniping Matchmaking:** To prevent win-trading and sniping in the queue, the engine implements several safeguards:
  - The rating window (`rating ± Δ`) expands non-linearly, accelerating smoothly to obfuscate when a match will pop.
  - The exact queue state (number of players and their ratings) is hidden to prevent coordination.
  - A strict **rematch cooldown** is enforced per-UUID across all formats, preventing players from farming the same opponent.
  - Match timing includes random jitter and requires a minimum candidate pool.
- **Team Snapshot DTOs:** When a match is made, the engine captures a `TeamSnapshot`—a stabilized, immutable DTO rather than raw, volatile NBT data. This ensures reliable pre-battle validation without hooking dangerously deep into the active Cobblemon engine during matchmaking.
- **Automated Tournament Bracket Structures:** Tournaments manage their own life cycles (`CREATED → REGISTRATION → SEEDING → RUNNING → COMPLETED`). The bracket engine natively supports Single-Elimination, Double-Elimination, Swiss, and Round-Robin formats. Auto-progression automatically advances winners to the next slot upon match completion and distributes byes seamlessly to top seeds based on player count.
- **Clause Enforcement:** 
  - **Pre-Battle (Team-level):** Checked via the `TeamSnapshot` before a battle can even start. Enforces the *Species Clause* (no duplicate Pokémon), *Item Clause* (no duplicate held items), *Level Caps* (or auto-scaling), team size constraints, and specific format bans.
  - **In-Battle (Battle-level):** Enforced while the battle runs. Features include the *Sleep Clause* (only one opponent can be put to sleep at a time), *Evasion Clause*, *OHKO Clause*, and *Endless Battle Clause* to prevent infinite stalls.