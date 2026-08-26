# Custom Models & Rendering

UniCrates relies entirely on vanilla Minecraft's Display entities (specifically ItemDisplay and BlockDisplay) to render 3D models. **GeckoLib is not used.**

## Idle Crate Visuals
- Crates are placed in the world as a block entity.
- To render the crate model, it summons a persistent ItemDisplay entity centered on the block.
- The mod uses standard Minecraft custom_model_data to apply custom 3D models to vanilla items (e.g., unicrates:crate_display_&lt;rarity&gt;).

## Holograms
- Handled by spawning TextDisplay entities above the crate. These entities are marked with the tag unicrates_hologram to persist and manage them independently.

## How Users Can Add Custom Content
Since UniCrates uses vanilla resource packs and display entities, adding custom models and resources is straightforward:

- **Built-in Rigs**: Users can specify ppearance.builtinModel in their crates/&lt;name&gt;.json (e.g., "common", "rare", "epic", "legendary"). For keys, key.keyModel applies custom_model_data values (1-4) to the default CrateKeyItem.
- **Custom Item Models**: For completely custom crates, admins can supply an item model file under the crate's 
esources/&lt;id&gt;/ folder and reference it using ppearance.customItemModel.
