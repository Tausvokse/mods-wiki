# Custom Models & Rendering Architecture

UniCrates renders all 3D crate models, animated rigs, holographic text, and prize items using native Minecraft **Display Entities** (`ItemDisplay`, `BlockDisplay`, and `TextDisplay`).

> [!IMPORTANT]
> **Zero GeckoLib Traps**: Unlike mods relying on complex third-party client renderers that frequently crash dedicated servers, UniCrates uses 100% vanilla Display Entities. Server CPU overhead is effectively 0.0 ms, and models render natively with GPU-accelerated client interpolation.

---

## 1. Dynamic Yaw Orientation (New in 2.0)

When you look at a block and run `/crate create <id>`, UniCrates captures the player's yaw angle:
- The persistent idle `ItemDisplay` is spawned with the exact rotation matrix matching your placement angle.
- Holograms (`TextDisplay`) use `billboard: "center"` to face viewers while remaining locked to the anchor's vertical axis.
- Dynamic idle animations (e.g., sinusoidal hovering, orbital halos, particles) calculate their spherical coordinates relative to the crate's placed yaw angle.

---

## 2. First-Person Key Viewmodel Transforms (New in 2.0)

In version 2.0, 3D keys feature tailored transformation matrices in their model JSONs:
- **`firstperson_righthand`**: Configured with rotation `[0, -45, 0]` and translations `[1.13, 3.2, 1.13]` so the key is held by its bow while the blade and teeth point straight forward into your crosshair.
- **`thirdperson_righthand`**: Positioned naturally in the player's hand during third-person view.
- **`gui` & `ground`**: Balanced isometric rendering for inventories and ground drops.

---

## 3. Universal Rotating Reward Animation (New in 2.0)

During opening conclusions across all crate types:
- The winning item or Cobblemon display is spawned above the crate with a continuous vertical angular velocity ($\approx 4^\circ/\text{tick}$).
- Simulates the natural spinning and bobbing of dropped items in Minecraft while suspended dramatically in mid-air.

---

## 4. Built-in Rigs & Custom Models

### Built-in 3D Rigs
UniCrates bundles high-fidelity block models accessible via `"builtinModel"`:
- `"common"`: Wooden reinforced chest with iron braces.
- `"rare"`: Lapis and sea lantern infused chest.
- `"epic"`: Amethyst crystal and dark prismarine vault.
- `"legendary"`: Netherite and glowing magma forge.
- `"pokeball"`: Custom 3D interactive Poké Ball rig.

### Adding Your Own Custom Models
To use your own models:
1. Place your Blockbench JSON model inside your server's resource pack under `assets/<namespace>/models/item/<model_name>.json`.
2. Reference your item in the crate's appearance config:
   ```json
   "appearance": {
     "displayMode": "item_display",
     "customItemModel": "mymod:crate_special",
     "scale": 1.0,
     "glowEffect": true
   }
   ```
3. Run `/crate reload` to instantly rebuild the dynamic server resource pack and update in-world displays.
