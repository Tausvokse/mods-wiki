# Installation and first crate

UniCrates 3.x targets **Minecraft 1.21.1 / Java 21** on Fabric and NeoForge. JARs for different loaders are not interchangeable. Fabric also requires Fabric API; NeoForge does not use Fabric API.

## Pick one installation mode

| Edition and mode | Server | Client |
| --- | --- | --- |
| Lite server + client | `unicrates-lite-<loader>-3.0.0.jar` | The same matching JAR |
| Lite server-only | `unicrates-lite-<loader>-3.0.0-server-only.jar` | No UniCrates mod; required resource pack |
| Pro server + client | `unicrates-<loader>-3.0.0-server.jar` | `unicrates-<loader>-3.0.0-client.jar` |
| Pro server-only | `unicrates-<loader>-3.0.0-server-only.jar` | No UniCrates mod; required resource pack |

Replace `<loader>` with `fabric` or `neoforge`. Install only one UniCrates JAR per side. Do not install server-only together with the companion-mode server JAR. QA, slim and dev-shadow artifacts are not releases. A Pro client companion alone does not implement singleplayer server gameplay.

The verified build uses Fabric Loader 0.19.3 with Fabric API 0.116.15+1.21.1, or NeoForge 21.1.248. Other modpack dependencies retain their own requirements. Cobblemon is optional and is not needed for Lite; Pro Pokémon features require a compatible Cobblemon installation. Back up worlds and configuration before switching modes because registered blocks/items are not automatically migrated.

## First Lite crate

1. Put the matching Lite JAR and required loader dependencies in `mods/`.
2. Start the server once to create `config/unicrates/`.
3. Edit names and rewards in the four JSON files in `config/unicrates/crates/`.
4. As an administrator, run `/crate reload` and read the load report.
5. Target a suitable block and run `/crate create common_crate`.
6. Run `/crate key give Alex common_crate 1`.
7. Alex right-clicks the crate with its physical key. `/crate preview common_crate` shows its rewards.

Fresh Lite defaults allow normal players to preview and open crates with their key; OP and LuckPerms are not required for gameplay. Administrative commands still require OP or the configured admin permission. Existing JSON files keep their permission settings: if upgrading an older setup, review `opening.permission` rather than testing only as OP.

Lite allows four bundled tier families and item, command, experience and broadcast rewards. Editors, custom models/timelines, SQL and additional integrations are Pro features. Lite does not require a key or activation service. A paid-edition information link is shown once per player on each Lite server.

## Required server-only resource pack

Start once, then host `config/unicrates/generated-server-only-resourcepack.zip` at a direct HTTP(S) download URL. Put that URL in `config/unicrates/server-only-resourcepack.json` and restart. Clients must accept and finish loading the required pack; refusing or failing to download it disconnects the client.

After changing pack assets, run `/crate exportpack`, replace the hosted ZIP and restart. The host must return the ZIP itself, without a login page. Server-only removes the need for the UniCrates client mod, not other client mods required by your modpack.

## Pro activation

Use the correct Pro server build and place the delivered key at `config/unicrates/license.key`. The seller must register it before use. Allow outgoing HTTPS, start the server, then check `/crate license`. Clients do not need a license. Read [activation and purchase scope](../editions) before buying. SQL storage is selected at startup; activate before startup or restart after activation.

Defaults install once and existing definitions are preserved. [Upgrade instructions](./upgrading), [commands](../administration/commands) and [troubleshooting](./troubleshooting) explain recovery and advanced administration.
