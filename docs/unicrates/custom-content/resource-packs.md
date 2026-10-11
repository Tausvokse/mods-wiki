---
title: Resource Packs
description: Generate, export, merge, and deliver custom crate and key assets for Minecraft 1.21.1.
---

# Resource Packs

Bundled models ship in the UniCrates client mod. Custom Java models and PNG textures need a resource pack on every client that should render them. Server configuration selects the appearance; the client pack supplies the geometry and pixels.

## Generate and export

1. Save your model, textures, and crate configuration through the [web editor](./web-editor) or [file import](./model-import).
2. Run `/crate reload` and resolve any model, texture, or duplicate CMD warnings.
3. Run `/crate exportpack` as an administrator.
4. Retrieve `config/unicrates/exported-resourcepack.zip` and install or host it for players.

| Path | Purpose |
| --- | --- |
| `config/unicrates/resources/` | Source model/texture files you own |
| `config/unicrates/generated-resourcepack/` | Automatically assembled directory when `general.autoGenerateResourcePack` is enabled |
| `config/unicrates/exported-resourcepack/` | Directory assembled by `/crate exportpack` |
| `config/unicrates/exported-resourcepack.zip` | ZIP created by that export command |
| `resourcepacks/UniCrates-ResourcePack.zip` | Extra convenience copy if the game directory already has a `resourcepacks` directory |

On a dedicated server, retrieve the exported ZIP explicitly; the client convenience directory may not exist. Automatic assembly creates server-side assets. It does not push a pack URL or reload client resources.

The assembler uses `pack_format: 34` for Minecraft 1.21.1 and computes a SHA-1 of the exported ZIP for Minecraft resource-pack delivery. A new export can change that hash.

## What the pack contains

For crate ID `festival_crate`, the custom-model workflow produces:

```text
pack.mcmeta
assets/
  minecraft/models/item/paper.json
  unicrates/
    models/item/custom/festival_crate.json
    models/item/custom/keys/festival_crate.json
    models/item/crate_key.json
    models/item/custom_paper_fallback.json
    models/item/custom_key_fallback.json
    textures/custom/festival_crate/wood.png
```

The crate mapping uses the existing `minecraft:paper` item. The physical key mapping uses the existing `unicrates:crate_key` item and retains bundled key overrides. The assembler adds reset entries after custom values because vanilla CMD predicates are thresholds; unrelated values should return to their fallback model rather than inherit the last crate override.

Custom file models use the **crate ID** as their generated output name, regardless of the input filename. The original model texture references remain unchanged.

## Optional generated texture layers

The assembler also copies paths configured through `appearance.blockTexture`, `appearance.guiIcon`, and `key.texture`. For example:

```json
{
  "appearance": {
    "blockTexture": "resources/festival_crate/block.png",
    "guiIcon": "resources/festival_crate/icon.png"
  },
  "key": {
    "texture": "resources/festival_crate/key.png"
  }
}
```

These are fields to merge into your existing sections. The generator emits texture files under `assets/unicrates/textures/crate/festival_crate/` and flat `minecraft:item/generated` model definitions such as `crate_festival_crate_icon.json`.

This is an asset-generation route. It does not automatically recolor a bundled 3D rig or register a new item for the generated flat model. For a complete custom physical crate/key appearance, use [Java model import](./model-import) and its CMD mapping. The browser upload patch accepts only Java models and `textures/custom/` PNGs; these optional legacy texture paths use the server file workflow.

## Activate on clients

For local testing, put the ZIP in the client's `resourcepacks` directory and enable it in **Options → Resource Packs**. If it was already enabled and you replaced its contents, reload resources with `F3 + T`.

For server delivery, host the ZIP at a URL clients can download and configure your Minecraft server's resource-pack settings with that URL and the current SHA-1. Update the hosted file and hash together after exporting a new pack. A server `/crate reload` does not refresh a connected client's resource assets.

The imported model route uses vanilla Java item-model rendering. UniCrates menus, networking, and cinematic companion behavior have their own client requirements; installing a pack alone is not a substitute for the required mod setup.

## Merge with an existing server pack

Place the generated pack above packs that replace `assets/minecraft/models/item/paper.json` or `assets/unicrates/models/item/crate_key.json`, or merge those files into your main pack. Minecraft pack priority replaces whole model JSON files; it does not combine `overrides` arrays from different packs.

When merging, preserve both systems' parent/texture requirements, sort thresholds correctly, resolve CMD collisions, and retain fallback/reset mappings. The UniCrates browser allocates IDs among loaded crate/key configurations; it cannot see CMD values used by an unrelated external pack. Reserve your own range to keep the two systems coordinated.

Bundled crate/key rig parents referenced by the generated key override still depend on the UniCrates client assets.

## Resource changes and backups

Web editor uploads overlay matching resource paths and preserve other existing resources. An omitted resource is not deleted. Crate and animation snapshots have different replacement semantics, described in [web editor](./web-editor).

The editor apply process validates all model and texture references before creating its backup and staged swap. Its preserved resource tree is bounded to 4096 files and 256 MiB, with a 16 MiB preserved-file limit; symbolic links are rejected during that staged copy. Use compact, regular files within `config/unicrates/resources/`.

The generated/exported directories are reused. Exporting again is not a guarantee that every old, now-unreferenced asset file has been removed. Inspect the resulting ZIP when publishing a changed pack, especially after deleting or renaming a crate.

## Acceptance checklist

- Confirm the current exported ZIP contains every referenced custom PNG and generated model.
- Verify a normal paper item still renders normally and your custom crate uses its assigned CMD.
- Verify built-in keys still render and a custom key uses its own mapping.
- Open and close the crate, then check restored facing, scale, and height.
- Check held-key first-person, third-person, GUI, and dropped-item views.
- Check a second client with the same pack priority and current ZIP.

Missing textures, incorrect pack priority, and duplicate CMDs are explained in the [model-import troubleshooting table](./model-import#troubleshooting).

