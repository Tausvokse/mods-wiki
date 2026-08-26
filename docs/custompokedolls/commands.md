# Commands
## `/pokedolls reload`
**Alias**: `/custom_pokedolls reload`
**Permission**: Level 2 (Server Operator)

This command is the backbone of the mod's dynamic capabilities, allowing server administrators to add new Pokedolls or update textures on the fly without restarting the server.
When executed:
1. The server re-scans the `custom_pokedolls` directory.
2. Any newly detected files are automatically registered as new `PokedollSpecies` and blocks.
3. A new `SyncCatalogPayload` is broadcasted to all connected clients.
4. Clients instantly download any missing files, trigger a client-side resource reload, and update their Creative tabs—syncing the new statues to their game in seconds.

*Note: If a model file is deleted, the mod will intentionally "orphan" placed statues in the world rather than deleting them, though their block items will no longer be generated.*

---