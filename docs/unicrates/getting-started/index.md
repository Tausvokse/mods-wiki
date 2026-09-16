# Getting Started with UniCrates 2.0

Welcome to **UniCrates**! This guide walks you through installing the mod and creating your very first animated in-world crate.

---

## Video Showcase & Quick Tutorial

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; margin: 1.5rem 0; box-shadow: 0 6px 16px rgba(0,0,0,0.4);">
  <iframe 
    src="https://www.youtube-nocookie.com/embed/JM8lRIMVzbY" 
    title="UniCrates 2.0 Showcase" 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen>
  </iframe>
</div>

---

## Requirements

- **Minecraft**: `1.21.1`
- **Mod Loader**: Fabric (`>=0.16.0`) or NeoForge (`>=21.1.65`)
- **Java**: `Java 21` or higher
- **Optional Dependencies**:
  - `Cobblemon` (1.7+ / 1.8+) for Pokémon rewards and 3D Pokédoll displays.
  - `LuckPerms` for granular permissions management.
  - An Economy provider (such as Impactor) for virtual balance rewards and purchases.

---

## Installation

1. Download `unicrates-fabric-2.0.0.jar` or `unicrates-neoforge-2.0.0.jar` depending on your server loader.
2. Place the JAR file into your server's `mods/` directory (and client `mods/` folder if playing singleplayer or testing visuals).
3. Start the server. UniCrates will automatically generate default configuration templates under `config/unicrates/`.

---

## Quick Start: Creating Your First Crate

### 1. Position & Orientation
Stand in front of the block you want to designate as your crate (e.g., a decorative pedestal or chest) and face the direction you want the crate model and animations to face:

```bash
/crate create pokeball_interactive_crate
```
*(Or use `basic_crate` for a traditional roulette or `milestone_crate`)*

> [!TIP]
> **Dynamic Yaw Orientation**: In UniCrates 2.0, the crate automatically captures your exact look angle when executing `/crate create`. The 3D model, opening effects, idle particles, and floating holograms will face precisely towards where you were standing!

### 2. Granting a Key
To test the opening sequence, give yourself an appropriate key:

```bash
/crate key give <player> pokeball_interactive_crate 5
```

### 3. Opening & Previewing
- **Right-Click with Key**: Initiates the interactive opening sequence.
- **Right-Click Empty-Handed (or Shift + Right-Click)**: Opens the graphical reward preview GUI showcasing weighted drop rates, rarity tiers, and daily limits.
