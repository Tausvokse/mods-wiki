# Features
## Dynamic Asset Loading
Custom Pokedolls is built on a highly dynamic registry system that entirely bypasses the need for hardcoded Java models or textures. 
During initialization (or a hot-reload), the mod scans the `custom_pokedolls` directory for `.geo.json` models and `.png` textures. When a valid model-texture pair is found, the mod automatically calculates the bounding boxes and hitboxes from the Geometry JSON by parsing its bones and cubes, dynamically sets its scale based on the model's highest dimensions, and registers a new `PokedollSpecies` into the game.

## Auto-Generated Shiny Variants
Shiny variants are generated effortlessly without writing any extra JSON files. When the scanner finds a base texture (e.g., `pikachu.png`), it explicitly searches for a shiny equivalent named `pikachu_shiny.png` or `shiny_pikachu.png`.
If found, the mod flags the species with `hasShinyTexture = true`. 
Behind the scenes, the virtual resource pack generates physical JSON resource item models dynamically for both variants (`&lt;id&gt;_doll.json` and `&lt;id&gt;_shiny_doll.json`) and binds them into Fabric's `BuiltinItemRendererRegistry`. Geckolib picks up this flag during rendering and automatically swaps to the shiny texture whenever the shiny item or block entity is displayed.

## Virtual Resource Pack Sync
The mod features a robust Server-to-Client synchronization system to ensure all players see custom models without needing to manually download a resource pack.
1. **Catalog Syncing**: Upon joining the server (or after a reload), the server builds a `SyncCatalogPayload` containing the SHA-1 hashes of all registered `.geo.json` and `.png` files and sends it to the client.
2. **Cache Comparison**: The client cross-references these hashes against a local `cache_map.json` and a `.cache/` folder. Missing files trigger a `RequestFilesPayload` back to the server.
3. **Chunked Transfers**: To prevent massive memory spikes, the server streams requested files in 32KB chunks via `FileTransferChunkPayload`.
4. **Virtual Pack Registration**: Once downloaded, files are physically cached and dynamically injected into the client's `DirectoryVirtualResourcePack`. 
5. **Seamless Application**: The client automatically calls `reloadResources()` to refresh textures and models in real-time.

## Pokedoll Chisel GUI
The Chisel GUI (accessed by interacting with a placed Pokedoll) empowers players to heavily customize how their statues are displayed in the world. Using the `PokedollSizeScreen`, players can tweak:
- **Scale**: A slider to shrink or grow the statue (from `0.5x` up to `15.0x`).
- **Rotation & Offsets**: Sliders for precise 360-degree rotation and X/Y/Z coordinate offsets to nudge the statue perfectly into place.
- **Effects**: Toggles for "Glowing Effect" and "Auto-Rotate" (showcase spin).
- **Poses**: A cycle button to choose between baked Geckolib animations like `Static`, `Idle / Breathing`, `Battle Stance`, `Walk / Fly`, and `Sleeping`.

All changes are sent over the network via `SizeSelectPayload` and instantly applied to the `PokedollBlockEntity`, updating live for all observing players.

---