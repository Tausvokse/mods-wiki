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

<div class="crates-grid">
  <div class="crate-card angelic">
    <div class="crate-badge">Mythic Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/angelic.png" alt="Angelic Crate" /></div>
    <div class="crate-info">
      <h3>Angelic Crate</h3>
      <p class="crate-desc">Golden crown trim with feathered wings and holy ascendance halos.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>angelic</code></span>
        <span><strong>Animation:</strong> <code>angelic_ascension</code></span>
        <span><strong>Key:</strong> <code>angelic_crate_key</code></span>
      </div>
    </div>
  </div>

  <div class="crate-card demonic">
    <div class="crate-badge red">Nether Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/demonic.png" alt="Demonic Crate" /></div>
    <div class="crate-info">
      <h3>Demonic Crate</h3>
      <p class="crate-desc">Soul fire pillars, curving magma horns, and pulsating nether embers.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>demonic</code></span>
        <span><strong>Animation:</strong> <code>demonic_hellfire</code></span>
        <span><strong>Key:</strong> <code>demonic_crate_key</code></span>
      </div>
    </div>
  </div>

  <div class="crate-card atlantis">
    <div class="crate-badge cyan">Oceanic Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/atlantis.png" alt="Atlantis Crate" /></div>
    <div class="crate-info">
      <h3>Atlantis Crate</h3>
      <p class="crate-desc">Dark prismarine vault with coral outcroppings and conduit bubble vents.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>atlantis</code></span>
        <span><strong>Animation:</strong> <code>atlantis_abyss</code></span>
        <span><strong>Key:</strong> <code>atlantis_crate_key</code></span>
      </div>
    </div>
  </div>

  <div class="crate-card pokemon">
    <div class="crate-badge red-white">Cobblemon Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/pokemon.png" alt="Pokemon Crate" /></div>
    <div class="crate-info">
      <h3>Pokémon Master Crate</h3>
      <p class="crate-desc">High-tech Poké Ball terminal with neon cyan energy conduits and capture latch.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>pokemon</code></span>
        <span><strong>Animation:</strong> <code>pokemon_master_capture</code></span>
        <span><strong>Key:</strong> <code>pokemon_crate_key</code></span>
      </div>
    </div>
  </div>

  <div class="crate-card money">
    <div class="crate-badge gold">Economy Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/money.png" alt="Money Crate" /></div>
    <div class="crate-info">
      <h3>Money / Jackpot Crate</h3>
      <p class="crate-desc">Gilded emerald lockbox overflowing with banknotes and golden ingots.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>money</code></span>
        <span><strong>Animation:</strong> <code>money_jackpot</code></span>
        <span><strong>Key:</strong> <code>money_crate_key</code></span>
      </div>
    </div>
  </div>

  <div class="crate-card nature">
    <div class="crate-badge green">Botanical Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/nature.png" alt="Nature Crate" /></div>
    <div class="crate-info">
      <h3>Nature Bloom Crate</h3>
      <p class="crate-desc">Ancient overgrown mossy shrine adorned with glowing cyan petals and spores.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>nature</code></span>
        <span><strong>Animation:</strong> <code>nature_bloom</code></span>
        <span><strong>Key:</strong> <code>nature_crate_key</code></span>
      </div>
    </div>
  </div>

  <div class="crate-card legendary">
    <div class="crate-badge gold">Legendary Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/legendary.png" alt="Legendary Crate" /></div>
    <div class="crate-info">
      <h3>Legendary Vault</h3>
      <p class="crate-desc">Heavy netherite safe reinforced with pure gold bands and corner pedestals.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>legendary</code></span>
        <span><strong>Animation:</strong> <code>particle_vortex</code></span>
        <span><strong>Key:</strong> <code>legendary_crate_key</code></span>
      </div>
    </div>
  </div>

  <div class="crate-card epic">
    <div class="crate-badge purple">Epic Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/epic.png" alt="Epic Crate" /></div>
    <div class="crate-info">
      <h3>Epic Crystal Crate</h3>
      <p class="crate-desc">Amethyst-faceted lockbox with deepslate trim and shimmering crystal locks.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>epic</code></span>
        <span><strong>Animation:</strong> <code>item_display_carousel</code></span>
        <span><strong>Key:</strong> <code>epic_crate_key</code></span>
      </div>
    </div>
  </div>

  <div class="crate-card rare">
    <div class="crate-badge blue">Rare Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/rare.png" alt="Rare Crate" /></div>
    <div class="crate-info">
      <h3>Rare Lapis Crate</h3>
      <p class="crate-desc">Polished lapis lazuli chest bordered by reinforced iron and sapphire runes.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>rare</code></span>
        <span><strong>Animation:</strong> <code>light_beam_pillar</code></span>
        <span><strong>Key:</strong> <code>rare_crate_key</code></span>
      </div>
    </div>
  </div>

  <div class="crate-card common">
    <div class="crate-badge gray">Starter Tier</div>
    <div class="crate-img-wrap"><img src="/UniCrates/models/common.png" alt="Common Crate" /></div>
    <div class="crate-info">
      <h3>Common Wooden Crate</h3>
      <p class="crate-desc">Classic reinforced spruce timber crate with riveted iron strapping.</p>
      <div class="crate-meta">
        <span><strong>Model:</strong> <code>common</code></span>
        <span><strong>Animation:</strong> <code>classic_chest_pop</code></span>
        <span><strong>Key:</strong> <code>common_crate_key</code></span>
      </div>
    </div>
  </div>
</div>

### 3D Crate Keys Gallery

Each crate has a corresponding 3D key model rendered with `custom_model_data` and precise `firstperson_righthand` transformations:

<div class="keys-grid">
  <div class="key-card"><img src="/UniCrates/models/angelic_key.png" alt="Angelic Key" /><span>Angelic Key</span></div>
  <div class="key-card"><img src="/UniCrates/models/demonic_key.png" alt="Demonic Key" /><span>Demonic Key</span></div>
  <div class="key-card"><img src="/UniCrates/models/atlantis_key.png" alt="Atlantis Key" /><span>Atlantis Key</span></div>
  <div class="key-card"><img src="/UniCrates/models/pokemon_key.png" alt="Pokemon Key" /><span>Pokemon Key</span></div>
  <div class="key-card"><img src="/UniCrates/models/money_key.png" alt="Money Key" /><span>Money Key</span></div>
  <div class="key-card"><img src="/UniCrates/models/nature_key.png" alt="Nature Key" /><span>Nature Key</span></div>
  <div class="key-card"><img src="/UniCrates/models/legendary_key.png" alt="Legendary Key" /><span>Legendary Key</span></div>
  <div class="key-card"><img src="/UniCrates/models/epic_key.png" alt="Epic Key" /><span>Epic Key</span></div>
  <div class="key-card"><img src="/UniCrates/models/rare_key.png" alt="Rare Key" /><span>Rare Key</span></div>
  <div class="key-card"><img src="/UniCrates/models/common_key.png" alt="Common Key" /><span>Common Key</span></div>
</div>

### Complete Preset Matrix

| Preset ID | Display Name | 3D Rig Model | Animation | Opening Style | Key ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `pokeball_interactive_crate` | **Interactive Poke Crate** | Poké Ball Ring | `interactive_pokeball` | 3D Hand-Pick | `interactive_key` |
| `pokemon_crate` | **Pokemon Crate** | `pokemon` | `pokemon_master_capture` | World 3D Anim | `pokemon_crate_key` |
| `angelic_crate` | **Angelic Crate** | `angelic` | `angelic_ascension` | World 3D Anim | `angelic_crate_key` |
| `demonic_crate` | **Demonic Crate** | `demonic` | `demonic_hellfire` | World 3D Anim | `demonic_crate_key` |
| `atlantis_crate` | **Atlantis Crate** | `atlantis` | `atlantis_abyss` | World 3D Anim | `atlantis_crate_key` |
| `money_crate` | **Money Crate** | `money` | `money_jackpot` | World 3D Anim | `money_crate_key` |
| `nature_crate` | **Nature Crate** | `nature` | `nature_bloom` | World 3D Anim | `nature_crate_key` |
| `selectable_crate` | **Destiny Oracle Crate** | `legendary` | Oracle Cards | Selectable Cards | `selectable_crate_key` |
| `instant_crate` | **Tactical Airdrop Crate** | `legendary` | None (Instant) | Instant Grant | `instant_crate_key` |
| `basic_gui_crate` | **Roulette Crate** | Chest Anchor | CS:GO Carousel | GUI Roulette | `basic_gui_crate_key` |
| `carousel_crate` | **Carousel Crate** | Chest Anchor | `item_display_carousel` | World 3D Anim | `carousel_crate_key` |
| `vortex_crate` | **Vortex Crate** | Chest Anchor | `particle_vortex` | World 3D Anim | `vortex_crate_key` |
| `firework_crate` | **Firework Crate** | Chest Anchor | `firework_burst` | World 3D Anim | `firework_crate_key` |
| `beam_crate` | **Beam Crate** | Chest Anchor | `light_beam_pillar` | World 3D Anim | `beam_crate_key` |
| `classic_chest_crate` | **Classic Crate** | Chest Anchor | `classic_chest_pop` | World 3D Anim | `classic_chest_crate_key` |
| `hologram_spin_crate` | **Cyber Holo Crate** | Chest Anchor | `hologram_spin` | World 3D Anim | `hologram_spin_crate_key` |

---

### Adding Your Own Custom Models
You can add your own models using **three non-programming pathways**:

#### 1. CustomModelData (ItemsAdder, Oraxen & Custom Resource Packs)
If your server uses custom item models via `CustomModelData`:
```json
"appearance": {
  "displayMode": "item_display",
  "customItemModel": "minecraft:paper",
  "customModelData": 10005,
  "scale": 1.2,
  "idleYOffset": 0.1,
  "glowEffect": true
}
```
UniCrates automatically attaches the `custom_model_data` component to the spawned `ItemDisplay` entity.

#### 2. Direct Resource Pack Item Models
Place your Blockbench JSON model inside your server's resource pack under `assets/<namespace>/models/item/<model_name>.json`:
```json
"appearance": {
  "displayMode": "item_display",
  "customItemModel": "mymod:crate_special",
  "scale": 1.0,
  "glowEffect": true
}
```

#### 3. Vanilla Block/Item Canvas
Use any vanilla item or block as a floating canvas:
```json
"appearance": {
  "displayMode": "item_display",
  "customItemModel": "minecraft:beacon",
  "scale": 1.0
}
```

### 4. Zero-Code Custom Textures & One-Click Pack Export

UniCrates allows server owners and builders to add custom crate textures without any code or manual resource-pack zipping:

1. **Drop Textures**: Place your PNG files in `config/unicrates/resources/<crate_id>/`:
   - `block.png` — In-world crate texture
   - `key.png` — Physical key texture
   - `icon.png` — GUI roulette and preview icon
2. **Export Pack**: Run the built-in compiler command in-game:
   ```bash
   /crate exportpack
   ```
   UniCrates automatically generates `pack.mcmeta`, registers item models, and bundles everything into `.minecraft/resourcepacks/UniCrates-ResourcePack.zip`.
3. Press `F3 + T` to reload your client textures.

### 5. In-Game Hand Reward Addition

Skip writing complex JSON strings and item IDs manually. Add any held item directly:
```bash
/crate reward add <crate> hand [weight] [rarity]
# Quick alias:
/crate addhand <crate> [weight] [rarity]
```
UniCrates captures the exact item in your hand, including:
- Custom Names, Lore, and MiniMessage styling
- Enchantments and Data Components
- Custom Model Data
- Cobblemon Pokémon species, forms, and shiny variants

Run `/crate reload` to instantly rebuild the dynamic server resource pack and update in-world displays.

<style>
.crates-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
.crate-card { background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-border); border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; position: relative; transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease; }
.crate-card:hover { transform: translateY(-6px); border-color: var(--vp-c-brand-1); box-shadow: 0 10px 24px rgba(0,0,0,0.35); }
.crate-badge { position: absolute; top: 12px; right: 12px; background: rgba(255, 215, 0, 0.2); color: #ffd700; border: 1px solid rgba(255, 215, 0, 0.4); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; padding: 3px 8px; border-radius: 6px; letter-spacing: 0.5px; }
.crate-badge.red { background: rgba(255, 68, 68, 0.2); color: #ff5555; border-color: rgba(255, 68, 68, 0.4); }
.crate-badge.cyan { background: rgba(0, 210, 255, 0.2); color: #00d2ff; border-color: rgba(0, 210, 255, 0.4); }
.crate-badge.red-white { background: rgba(238, 21, 21, 0.2); color: #ff6b6b; border-color: rgba(238, 21, 21, 0.4); }
.crate-badge.green { background: rgba(76, 209, 55, 0.2); color: #4cd137; border-color: rgba(76, 209, 55, 0.4); }
.crate-badge.purple { background: rgba(156, 39, 176, 0.2); color: #ba68c8; border-color: rgba(156, 39, 176, 0.4); }
.crate-badge.blue { background: rgba(33, 150, 243, 0.2); color: #64b5f6; border-color: rgba(33, 150, 243, 0.4); }
.crate-badge.gray { background: rgba(158, 158, 158, 0.2); color: #bdbdbd; border-color: rgba(158, 158, 158, 0.4); }
.crate-img-wrap { background: radial-gradient(circle, rgba(255,255,255,0.06) 0%, rgba(0,0,0,0.2) 80%); padding: 1.5rem; display: flex; align-items: center; justify-content: center; height: 210px; }
.crate-img-wrap img { max-height: 180px; max-width: 100%; filter: drop-shadow(0 8px 16px rgba(0,0,0,0.5)); transition: transform 0.3s ease; }
.crate-card:hover .crate-img-wrap img { transform: scale(1.08) rotate(-2deg); }
.crate-info { padding: 1.25rem; flex: 1; display: flex; flex-direction: column; }
.crate-info h3 { margin: 0 0 0.5rem 0; font-size: 1.15rem; color: var(--vp-c-text-1); }
.crate-desc { font-size: 0.85rem; color: var(--vp-c-text-2); line-height: 1.4; margin-bottom: 1rem; flex: 1; }
.crate-meta { display: flex; flex-direction: column; gap: 0.35rem; font-size: 0.78rem; background: var(--vp-c-bg); padding: 0.6rem 0.8rem; border-radius: 8px; border: 1px solid var(--vp-c-border); }
.crate-meta code { font-size: 0.75rem; }
.keys-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 1rem; margin: 1.5rem 0 2.5rem 0; }
.key-card { background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-border); border-radius: 10px; padding: 0.8rem; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 0.5rem; transition: transform 0.2s ease, border-color 0.2s ease; }
.key-card:hover { transform: translateY(-4px); border-color: var(--vp-c-brand-1); }
.key-card img { max-height: 80px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.4)); }
.key-card span { font-size: 0.78rem; font-weight: 600; color: var(--vp-c-text-1); }
</style>
