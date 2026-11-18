# Lite and Pro editions

Minecraft 1.21.1 / Java 21. Choose Fabric or NeoForge and one installation mode.

| Capability | Lite | Pro |
| --- | --- | --- |
| License | Free, no activation | US$40 once, one active server, 3.x updates |
| Crates | Four tier families | Additional families and custom crates |
| Models and openings | Four bundled tier models/timelines | Additional models, custom content and opening systems |
| Rewards | Item, command, XP, broadcast | Additional types and optional integrations |
| Configuration | JSON | JSON, browser and in-game editors |
| Storage | JSON | JSON, SQLite, MySQL/MariaDB |
| Server-only | Hosted required resource pack | Hosted required resource pack |
| Server + client | Same matching Lite JAR on both sides | Separate Pro server and companion client JARs |

## Pro activation

Put the delivered, registered key at `config/unicrates/license.key` on the server. Allow outgoing HTTPS to the activation service. Start the server or run `/crate reload`, then `/crate license`. Players do not need the key.

Each JVM startup needs fresh approval. Signed permits renew in the background and last at most two minutes. A running process retains only its current permit's remaining time if the service cannot be reached. Starting a new process replaces the previous process’s renewal access; an already issued permit can remain valid until expiry. Expired or denied activation applies Lite limits. There is no promise of perpetual offline access or an indefinitely available service.

The allowance is one simultaneously active installation, associated with its observed outgoing IP. Stop the old server and contact support before moving hosts or changing that address. Activate before initial startup when using SQL storage; changing storage after activation requires a restart.

## Purchase scope

US$40 is a one-time Pro 3.x license for one server, with 3.x updates. New purchases do not include custom animation services or future major versions. Tax is included where applicable; the final charge is shown at checkout. Previously agreed individual terms remain valid.

[Product page and payment availability](https://taushop.me/unicrates/) · [Terms](https://taushop.me/unicrates/terms/) · [Refunds](https://taushop.me/unicrates/refunds/) · [Support](https://taushop.me/unicrates/support/)
