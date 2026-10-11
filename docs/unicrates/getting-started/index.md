# Installation and first crate

UniCrates 2.3 targets **Minecraft 1.21.1** and **Java 21**, with Fabric and NeoForge artifacts. Choose the matching loader build; Fabric and NeoForge JARs are not interchangeable.

## Build targets and dependencies

| Platform | Project target |
| --- | --- |
| Minecraft | 1.21.1; metadata accepts 1.21.1 through before 1.21.2 |
| Java | 21 or newer compatible runtime |
| Fabric | Loader 0.19.3 minimum encoded in this build; Fabric API required; build dependency 0.116.15+1.21.1 |
| NeoForge | 21.1.x metadata range; project build target 21.1.248 |
| Cobblemon | Optional; project target 1.7.3+1.21.1; NeoForge optional metadata range 1.7.3 through before 1.8 |
| LuckPerms | Optional; permission nodes and permission rewards |
| Impactor | Optional; bundled economy adapter needs compatible installed provider |

These are repository build/metadata values, not claims about the latest upstream releases. Follow dependencies of optional mods themselves, including Fabric Language Kotlin when required by your Cobblemon build. Pokémon reward/scenes require compatible Cobblemon on the appropriate sides. A version-warning setting is not a guarantee of compatibility with another Cobblemon release.

## Artifact selection

| Artifact | Install location |
| --- | --- |
| `unicrates-fabric-2.3-server.jar` | Dedicated Fabric server |
| `unicrates-fabric-2.3-client.jar` | Fabric multiplayer client companion |
| `unicrates-fabric-2.3.jar` | Universal Fabric artifact; singleplayer/integrated server or universal installation |
| `unicrates-neoforge-2.3-server.jar` | Dedicated NeoForge server |
| `unicrates-neoforge-2.3-client.jar` | NeoForge multiplayer client companion |
| `unicrates-neoforge-2.3.jar` | Universal NeoForge artifact; singleplayer/integrated server or universal installation |

Put the chosen JAR in the instance's `mods/` directory. Do not install universal alongside a split artifact on the same side. A client-only companion does not initialize server gameplay; singleplayer requires the universal artifact. `slim`, dev-shadow, QA and gametest artifacts are build intermediates/test helpers, not release installation choices.

Keep server and companion versions matched. Scene features also negotiate capability bits; an old companion may use standard effects even when updated scene settings exist. `general.requireClientMod` is stored metadata without an active connection-enforcement consumer in current source. It is not a switch guaranteeing all client-side features on a client without the companion.

## First startup

1. Back up an existing world before adding/upgrading the mod.
2. Install the correct loader artifact and required loader dependencies.
3. Start the server once with Java 21; read startup errors before inviting players.
4. Confirm `config/unicrates/` contains main-config.json, discord.yml, crates/, animations/, resources/, lang/ and data/.
5. Keep bundled examples or define a crate using the [complete JSON recipe](../custom-content/json#smallest-practical-crate).

Defaults are installed once behind `.defaults-installed`. Deleting a sample later does not cause it to regenerate every reload. The configVersion value 1 is independent from mod version 2.3.

## Create, preview and test

After saving the starter JSON recipe and running reload:

```text
/crate reload
/crate list
/crate create starter
/crate key give Alex starter 3 physical
/crate preview starter
```

Run create as an administrator player while targeting a block within 6 blocks. It replaces that block with the anchor and captures facing from player yaw plus 180 degrees. Choose a deliberate placement location. To hand out a portable anchor instead:

```text
/crate give Alex starter 1
```

Alex holds a real key in the main hand and right-clicks to open. Shift-right-click requests preview. Empty-handed right-click may open instead of preview if virtual keys or purchase alternatives apply. See [gameplay](../gameplay/).

For actual access/cost/cooldown tests, use a non-OP survival player; operator/creative bypasses can mask errors. Check inventory or dropped overflow, party/PC for Pokémon, provider balance, key balance and statistics after one opening.

## Owner workflow

Use `/crate editor` for browser configuration and `/crate apply <hash>` to apply its reviewed result, or edit server JSON and reload. `/crate edit [id]` opens the in-game editor for the administrator player. Administrative access is unicrates.admin or OP level 2. Full syntax is in [commands](../administration/commands).

Custom models/textures may need a generated/exported resource pack loaded by clients. Automatic assembly does not host or force-download the pack. See [models](../custom-content/models).

Before using SQL storage, economy payment, custom command rewards or production reward caps, read [storage and recovery](../configuration/storage), [main settings](../configuration/main-config) and [reward reference](../custom-content/rewards). Installation problems are covered in [troubleshooting](./troubleshooting).

Source: `gradle.properties`, loader metadata and build.gradle split tasks, `ConfigManager`, `UniCratesCommand`, loader entrypoints.
