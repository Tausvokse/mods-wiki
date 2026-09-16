# UniCrates Documentation

Welcome to the official documentation for **UniCrates** (Version 2.0.0)!

UniCrates is a production-grade, multi-loader (Fabric & NeoForge) data-driven crate and lootbox engine designed natively for **Minecraft 1.21.1** with first-class **Cobblemon 1.7 / 1.8+** integration.

---

## What makes UniCrates 2.0 Special?

- **Dual-Loader Parity**: Single shared architecture across Fabric and NeoForge with zero split-package overhead or runtime desyncs.
- **Pure Vanilla Display Entities**: Zero GeckoLib dedicated server traps! All idle animations, 3D crate models, rotating reward drops, and floating holograms run entirely on vanilla `ItemDisplay`, `BlockDisplay`, and `TextDisplay` entities with 0.0 ms tick overhead.
- **Dynamic Orientation & Yaw Conformance (New in 2.0)**: Placed crates automatically align to the exact angle you were looking during `/crate create`. Idle rigs, particle trails, and orbiting props conform to the crate's facing direction.
- **First-Person Key Viewmodel Alignment (New in 2.0)**: Bespoke 3D key display transforms orient keys straight forward from the player's view in first-person without awkward vertical tilt.
- **Universal Floating Item Animation (New in 2.0)**: Won prize items across all crate models rotate smoothly around their vertical Y-axis with natural physics bobbing.
- **Anti-Interference Player Shield (New in 2.0)**: Outside players trying to steal or interrupt active crate openings are gently pushed back by a localized velocity shield with status warnings.
- **Interactive 3D Poké Ball Selection**: Physical in-world 3D roulette where players interact directly with floating Poké Balls featuring GPU scale interpolation, main-hand security, and disconnect failsafes.
- **Cinematic Orbit Camera Splines**: Cinematic Catmull-Rom orbit camera curves for Legendary and Mythic reward drops with instant combat-damage safety abort.
- **LuckPerms-Style Web Editor (`/crates editor`) & GUI Editor**: Create and edit crates, configure rewards, customize 47 animation timelines, and sync in real-time with one command.
- **Asynchronous Discord Webhooks**: Rich Discord victory embeds with 3D player skin avatars and Cobblemon IV/EV/Shiny stats.
- **Triple Storage Backend**: Support for `flatfile`, `sqlite`, and `mysql`/`mariadb` with automated one-shot live data migration.

---

## Visual Showcase

<div style="display: flex; overflow-x: auto; gap: 15px; padding: 15px 0; scroll-snap-type: x mandatory; align-items: center; background: rgba(0,0,0,0.2); border-radius: 10px; margin: 1.5rem 0;">
  <img src="/UniCrates/image.png" alt="UniCrates in World" style="scroll-snap-align: center; max-height: 350px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);" />
  <img src="/UniCrates/image1.png" alt="UniCrates Holograms" style="scroll-snap-align: center; max-height: 350px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);" />
  <img src="/UniCrates/image2.png" alt="UniCrates GUI Preview" style="scroll-snap-align: center; max-height: 350px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);" />
  <img src="/UniCrates/image3.png" alt="UniCrates Opening Animation" style="scroll-snap-align: center; max-height: 350px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.5);" />
</div>

---

## Documentation Navigation

| Section | Description |
| :--- | :--- |
| **[Getting Started](/unicrates/getting-started/)** | Installation instructions for Fabric & NeoForge, first crate setup. |
| **[Gameplay Guide](/unicrates/gameplay/)** | How players interact with crates, keys, previewing odds, and mass opening. |
| **[Configuration Overview](/unicrates/configuration/)** | Global settings, Discord webhooks, interactive 3D Poké Balls, and camera splines. |
| **[How to Create a Crate](/unicrates/custom-content/create)** | Step-by-step tutorial on crafting custom crate definitions. |
| **[Custom Models & Rendering](/unicrates/custom-content/models)** | Display Entity rendering, 3D rig models, and custom model data. |
| **[Rewards Guide](/unicrates/custom-content/rewards)** | Weighted odds, Cobblemon Pokémon specs, commands, economy, and limits. |
| **[Custom Animations](/unicrates/custom-content/animations)** | Timeline-based keyframed animations, orbits, particles, and easing curves. |
| **[JSON Format Reference](/unicrates/custom-content/json)** | Exhaustive field-by-field schema reference for all configurations. |
| **[Commands](/unicrates/administration/commands)** | Full command list with syntax, parameters, and permission levels. |
| **[Permissions](/unicrates/administration/permissions)** | Granular permissions matrix for LuckPerms and vanilla OP levels. |
| **[Developer Architecture](/unicrates/developer/)** | Modular architecture, event bus hooks, and storage engine design. |
