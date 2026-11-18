# Release notes

## 3.0.0 — Lite and separately activated Pro

Four Lite distributions cover Fabric/NeoForge in server+client and server-only modes. Lite has four tier families and JSON configuration. Pro has separate server/client companions or server-only builds and requires registered online activation. See [editions](./editions) and the [current installation guide](./getting-started/).

Lite defaults permit ordinary-player preview/opening. A one-time per-player chat notice links to the separate paid edition. Server-only requires the hosted pack. Older server configuration is preserved.

The following notes describe the historical engine and are not the Lite feature list.

# UniCrates 2.3 release notes

## Current documentation edition

This wiki covers the October 11, 2026 **Master roulette hotfix** alongside the rest of the 2.3 feature set. The current data inventory contains **31 built-in crate rigs with matching key models**, **52 bundled JSON animation definitions**, and **seven additional opening modes**. Aliases are documented separately and do not increase the opening count.

## Master Singularity

- Rapid complete passes through the real eligible reward pool at **4–6 ticks per candidate**.
- A final **12-tick lock** onto the confirmed server-issued winner.
- One winner label entrance, a static readable hold and one exit, avoiding per-tick interpolation resets.
- Moderately larger winner labels across opening animations.
- Smooth prize growth and retreat, continuous charge ribbons, release geometry and a coronation halo.
- Authoritative time synchronization after winner preparation, keeping the final lock aligned when first-use Pokémon initialization stalls a server tick.
- A minimum **280-tick** sequence that extends for larger eligible pools; up to **256 distinct eligible entries** are supported.

The opening remains `astral_reveal`, the model remains `astral_pokeball`, and the public editor names are **Master Singularity** and **Master Ball**. The reward comes from your configuration; an example Riolu shown in a recording is not hardcoded into the opening.

<AnimationPreview id="astral_reveal" />

## Opening and editor options

The [opening catalog](./custom-content/animation-catalog) lists every bundled timeline and special mode, including the four Pokémon scenes, interactive Poké Ball selection and GUI roulette. The [GIF gallery](./custom-content/gallery) provides a recorded preview for each canonical ID.

The browser editor manages crates, rewards, key settings, appearance, idle particle effects and selected opening presets. It also provides per-crate raw JSON editing and JSON export. Custom timeline action authoring uses the separate animation JSON format; see the [web editor guide](./custom-content/web-editor) for the actual save/apply workflow and the [timeline tutorial](./custom-content/animation-tutorial) for creating sequences.

## Reward delivery and operations

Reward selection, costs and delivery remain server-owned. Storage supports flat files, SQLite and MySQL/MariaDB. Durable transactions support recovery, and ambiguous command outcomes require an administrator decision rather than an automatic replay. See [storage and recovery](./configuration/storage) before changing backends or clearing pending records.

## Preview and compatibility scope

The Master preview was recorded on October 11 after the hotfix. Other gallery previews are accepted gameplay recordings from October 10; they illustrate their configured openings rather than a fresh replay of all 59 modes. The latest hotfix passed 67 required GameTests and native Fabric item/Pokémon opening acceptance. NeoForge artifacts were compiled and distribution-checked; those Fabric shader recordings are not native NeoForge footage.

## Requirements

Minecraft **1.21.1** and **Java 21** are required. Use matching client/server artifacts for your loader. [Read the installation instructions](./getting-started/).
