---
layout: home
title: UniCrates 2.3
description: Complete UniCrates documentation, configuration reference, animation previews and custom content tutorials.
hero:
  name: UniCrates 2.3
  text: Your rewards. Your opening.
  tagline: Animated crates for Minecraft 1.21.1 on Fabric and NeoForge. Configure rewards, choose a model, watch an opening, and build your own experience.
  actions:
    - theme: brand
      text: Install & create your first crate
      link: /unicrates/getting-started/
    - theme: alt
      text: Watch 59 opening GIFs
      link: /unicrates/custom-content/gallery
    - theme: alt
      text: Open the web editor
      link: https://unicrates-cloud-relay.tausvokse.workers.dev/#/
features:
  - icon: 🎁
    title: Models and matching keys
    details: 31 built-in crate rigs and key models, plus custom model and resource-pack workflows. Choose the model independently from its opening.
    link: /unicrates/custom-content/models
  - icon: ✨
    title: 59 ready-to-use openings
    details: 52 JSON timelines, four Pokémon scenes, Master Singularity, interactive Poké Ball selection and a GUI roulette. Browse real recorded GIF previews.
    link: /unicrates/custom-content/gallery
  - icon: 🛠️
    title: Make it your own
    details: Edit rewards, keys, models, idle particles and appearance in the browser. Author custom timeline actions in JSON with a complete step-by-step guide.
    link: /unicrates/custom-content/web-editor
  - icon: 🧩
    title: Rewards and integrations
    details: Item, command, economy, key and Cobblemon rewards. Physical and virtual keys, weighted pools, pity, milestones and recoverable delivery.
    link: /unicrates/custom-content/rewards
---

## Start with the task you want to complete

| I want to… | Read this |
|---|---|
| Install the mod and open my first crate | [Getting started](./getting-started/) |
| Choose an opening after seeing how it looks | [GIF gallery](./custom-content/gallery) and [opening catalog](./custom-content/animation-catalog) |
| Create a crate with the browser editor | [Web editor walkthrough](./custom-content/web-editor) |
| Create or adjust JSON files | [Crate tutorial](./custom-content/create), [crate field reference](./configuration/crate-reference) and [JSON formats](./custom-content/json) |
| Add Pokémon, items, money or commands to a pool | [Rewards guide](./custom-content/rewards) |
| Configure floating models and idle effects | [Models](./custom-content/models) and [idle animations](./custom-content/idle-animations) |
| Write my own animation | [Timeline tutorial](./custom-content/animation-tutorial) and [action reference](./custom-content/timeline-reference) |
| Import a Blockbench model or replace a texture | [Model import](./custom-content/model-import) and [resource packs](./custom-content/resource-packs) |
| Configure a database, backups or recovery | [Storage guide](./configuration/storage) |
| Find commands and exact permission nodes | [Commands](./administration/commands) and [permissions](./administration/permissions) |
| Troubleshoot a crate, reward or resource pack | [Troubleshooting](./getting-started/troubleshooting) |

## See the latest opening

**Master Singularity** charges the Master Ball, rapidly cycles the real eligible reward pool, locks onto the server-confirmed winner and gradually reveals it. The October 11 hotfix uses **0.20–0.30-second candidate slots**, a stable larger winner label and synchronized final timing after Pokémon initialization.

<AnimationPreview id="astral_reveal" />

The stored opening ID is `astral_reveal`, and the model ID is `astral_pokeball`. These IDs remain valid for existing configurations. [See the full catalog and setup](./custom-content/animation-catalog).

## How the pieces fit together

A **crate definition** controls its key requirements, reward pool and opening settings. A **placed anchor** makes that crate available at a world location. Its **model** determines the physical appearance; its **idle effects** run while it waits; its **opening** determines the reveal sequence. The **reward definition** decides what the player receives. The same model can use different openings, and the same opening can reveal different configured rewards.

Most server customization lives under `config/unicrates/`. Install the matching UniCrates client companion to display its custom models and scenes. Use the [installation guide](./getting-started/) for exact artifacts and optional dependencies.

## Version and documentation scope

This guide describes the **current 2.3 source and shipped data**, including the Master roulette hotfix. It separates implemented behavior from stored settings that currently have no runtime effect. Definitions, commands and examples are checked against the code; it does not claim that every external integration version or shader pack has been tested.

The [2.3 release notes](./release-notes) describe the current feature set and changes. The [developer section](./developer/) covers internal architecture and extension points.

## Purchase and custom animation requests

UniCrates is **$40**, with the price permanently fixed at that amount. Buyers receive **one free custom animation**; additional custom animations cost **$5 each**. You may request the first animation before buying to see its result before deciding. [Join Discord](https://discord.gg/VjU5AybJYr) and DM the author to discuss your request.

[Mod trailer](https://youtu.be/EIxJPLKGiW0) · [Web editor video](https://youtu.be/YmDfbAc74U4) · [Support and request details](./support)
