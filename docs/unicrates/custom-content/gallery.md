---
title: Opening GIF Gallery
description: Watch all 59 ready-to-use UniCrates opening animations in recorded Minecraft gameplay.
outline: [2, 3]
---

# Opening GIF gallery

Watch **59 ready-to-use openings** before assigning one to a crate. Search by display name or copy the exact ID shown below a preview. Click **Play GIF** to load an animation; click **Stop GIF** to return to its still image. GIFs do not download or animate until you choose to play them.

These are real Minecraft recordings. The Master Singularity preview uses the **October 11, 2026 roulette hotfix**; other previews were recorded on **October 10, 2026**. They demonstrate the selected opening with an example crate, reward pool and shader settings. Your configured reward, model, scale, timings, particles and shaders change the result. A Pokémon shown here is an example reward, not a forced winner.

The gallery includes **52 bundled JSON timeline definitions**, four Pokémon companion scenes, Master Singularity, interactive Poké Ball selection and the GUI roulette. Aliases are not counted as extra animations. Removed experimental openings are not included.

<UniCratesGallery />

## Use a previewed opening

1. Copy its ID and open your server's editor with `/crates editor`.
2. Select the crate, choose the corresponding opening or timeline and save the configuration.
3. Run the apply command shown by the editor, then test the crate with a matching key.

For file-based configuration, follow the [ready-to-use animation guide](./animations) and [complete opening catalog](./animation-catalog). The catalog explains which IDs belong in `opening.openingType` and which belong in the timeline fields. The [timeline tutorial](./animation-tutorial) walks through making your own sequence.

## Why the recorded duration differs from a configured tick duration

A recording includes a short idle view before interaction and a short restored view after cleanup. GIF playback is sampled from the recorded frames; it is a visual preview rather than a timing benchmark. Server lag, scene initialization and shader performance also affect wall-clock playback. The catalog lists configured scene durations separately.

## Custom animation requests

UniCrates costs **$40**. Buyers can request one custom animation **free**; additional animations cost **$5 each**. You can request your first animation before purchasing the mod to see the result before deciding. Send a DM through the [UniCrates Discord community](https://discord.gg/VjU5AybJYr) to discuss the idea and scope.
