---
title: Import a Custom Model
description: Import Blockbench Java cube models and physical keys with validated PNG textures.
---

# Import a Custom Model

The supported import format is a **Minecraft Java item-model JSON** using cube `elements` or a supported vanilla parent. Importing it changes appearance without adding an item registry entry or recompiling UniCrates.

## Prepare the Blockbench export

Use a Java Block/Item project with cubes, UV faces, and vanilla-compatible element rotations. Export the Java model JSON and any PNG textures. Saving the editing project as `.bbmodel` does not produce the model format needed here.

| File or feature | Import support |
| --- | --- |
| Java item/block-model JSON with cube elements | Supported within the limits below |
| Vanilla `minecraft:` parent | Supported by validation; preview depends on available assets |
| PNG referenced as `unicrates:custom/...` | Supported with a matching uploaded or server-side PNG |
| Vanilla `minecraft:` texture | Uses the client's Minecraft assets |
| `.bbmodel` project | Export Java model JSON first |
| Bedrock `.geo.json`, GeckoLib geometry/animations | Not this importer |
| OBJ, glTF/GLB, FBX, arbitrary mesh faces | Not this importer |
| Custom model parent from another namespace | Rejected by the importer |
| Item `overrides` inside the imported model | Rejected; UniCrates generates the outer override mapping |
| Blockbench bone animations | Not transferred to the runtime |

For a hinge, the built-in rigs use separate base and lid item models. A custom single-mesh import stays one mesh during opening. Use timeline display movement for additional choreography; adding `_lid` filenames to resources does not automatically register a custom hinged rig.

## Browser workflow: crate model

1. Open your administrator session with `/crates editor`.
2. Give the crate a lowercase ID before uploading, for example `festival_crate`.
3. In **3D Appearance**, choose **Java item model JSON**. The editor stages it at `resources/models/festival_crate.json` and assigns an unused crate Custom Model Data value starting at `1000`.
4. For each `unicrates:custom/...` dependency, choose its **Texture reference** and upload the corresponding **PNG texture**. The dropdown lists references already present in the model; uploading a PNG does not rewrite the model's texture declarations.
5. Inspect the 3D preview. Orbit, zoom, and reset help locate UV or orientation mistakes. A missing-resource status needs resolving before the Minecraft check.
6. Click **Apply Changes**, then **Save to Server**, and run the new `/crates apply <hash>` command.
7. Run `/crate exportpack`, deliver the ZIP to your clients, and test the placed crate.

Selecting a built-in model clears the form's custom crate model and CMD override. Selecting **Use built-in key model** clears the custom key override. Existing resource files remain preserved on the server; changing the selection is not a resource deletion operation.

## Browser workflow: physical key

In **General & Key**, use **Key Java item model JSON** and **Key PNG texture**. The key JSON is staged at `resources/models/keys/festival_crate.json` with an unused key CMD value. Keep `key.id`, key mode, and consumption settings appropriate for your crate.

The key upload changes the static `unicrates:crate_key` item's visual. It does not change the accepted key identity. Virtual keys are balances and do not need a rendered physical item. Crate and key uploads share one resource patch but use separate model folders.

Cancelling the form discards its staged uploads and edits. **Apply Changes** retains them in the browser workspace; saving/applying the session transfers them to the server. See [web editor](./web-editor) for the complete lifecycle.

## File workflow: a working cube model

Create `config/unicrates/resources/models/festival_crate.json`:

```json
{
  "ambientocclusion": true,
  "textures": {
    "wood": "minecraft:block/oak_planks"
  },
  "elements": [
    {
      "from": [2, 0, 2],
      "to": [14, 12, 14],
      "faces": {
        "north": {"uv": [0, 0, 16, 16], "texture": "#wood"},
        "south": {"uv": [0, 0, 16, 16], "texture": "#wood"},
        "east": {"uv": [0, 0, 16, 16], "texture": "#wood"},
        "west": {"uv": [0, 0, 16, 16], "texture": "#wood"},
        "up": {"uv": [0, 0, 16, 16], "texture": "#wood"},
        "down": {"uv": [0, 0, 16, 16], "texture": "#wood"}
      }
    }
  ]
}
```

The vanilla wood texture needs no imported PNG. In your complete crate definition, set:

```json
{
  "appearance": {
    "displayMode": "item_display",
    "customItemModel": "resources/models/festival_crate.json",
    "customModelData": 1200,
    "scale": 1.0,
    "idleYOffset": 0.0
  }
}
```

The file model uses `minecraft:paper` as the existing canvas. The generated pack maps exactly CMD `1200` to `assets/unicrates/models/item/custom/festival_crate.json`.

For your own PNG, change the texture declaration to:

```json
{
  "textures": {
    "wood": "unicrates:custom/festival_crate/wood"
  }
}
```

Save its PNG at `config/unicrates/resources/textures/custom/festival_crate/wood.png`. Resource IDs omit the `.png` extension. Faces reference `#wood`; texture variables must exist and cannot form cycles.

For a custom key, save another Java model at `config/unicrates/resources/models/keys/festival_crate.json` and add to the existing key section:

```json
{
  "customItemModel": "resources/models/keys/festival_crate.json",
  "customModelData": 1200
}
```

The generated key model becomes `assets/unicrates/models/item/custom/keys/festival_crate.json` and overrides CMD `1200` on `unicrates:crate_key`. Values are independent from the crate's paper values. Choose unique values **among all crate appearance CMDs** and **among all key CMDs**, respectively; another configured CMD of the same category can cause a collision even when its model uses an existing item ID.

Run `/crate reload`, inspect warnings, export the [resource pack](./resource-packs), and activate it on every client.

## Validation limits

The browser does initial checks. The server applies the stricter model, PNG, reference, and snapshot validation before changing live configuration.

| Asset or field | Limit or rule |
| --- | --- |
| Model JSON | At most `1 MiB` UTF-8, 32 nesting levels, 100,000 parsed tokens |
| Cube elements | At most `2048`; `from`, `to`, and rotation origin components between `-16` and `32` |
| Texture variables | At most `64`; names use letters, digits, `_`, or `-`, up to 64 characters |
| Resource IDs inside imported model | Explicit `minecraft:` or `unicrates:` namespace; lowercase letters, digits, `_`, `-`, `/` |
| Parent | Explicit `minecraft:` resource only |
| Element rotation | One `x`, `y`, or `z` axis; angle `-45`, `-22.5`, `0`, `22.5`, or `45` |
| Face rotation | `0`, `90`, `180`, or `270` |
| Face UV | Four numeric values, each within `-4096` to `4096` |
| PNG file | At most `4 MiB`; width and height each `1–2048` pixels |
| PNG integrity | Correct PNG chunks/checksums, terminal IEND, decodable image data |
| Imported dependencies per model | At most `32 MiB` of unique custom PNG data |
| File-model CMD | Integer from `1000` through `16777214` |
| Browser upload patch | At most `128` files and `3 MiB` decoded file data combined |
| Complete session JSON | At most `5 MiB`, including base64 expansion and configuration |

The upload patch can contain only `models/...json` and `textures/custom/...png` paths, relative to `resources/`. Use lowercase path segments and forward slashes. Absolute paths, `..`, repeated separators, backslashes, and links escaping the resource tree are not accepted. A safe short layout such as the examples above avoids browser/server path-length differences.

Imported display contexts support `thirdperson_righthand`, `thirdperson_lefthand`, `firstperson_righthand`, `firstperson_lefthand`, `head`, `gui`, `ground`, and `fixed`. Their transforms require rotation components within `-360..360`, translation within `-80..80`, and scale within `0..4`. Numbers and booleans must be actual JSON values, not quoted strings.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Upload accepted, server apply rejected | Server validation is stricter; inspect the first reported model/PNG error |
| Missing or magenta texture | Match `unicrates:custom/...` to the exact PNG path; export and activate the new pack |
| Paper appears | Confirm file reference, valid/unique CMD, generated paper override, and pack priority |
| Another custom crate appears | Resolve duplicate CMD values and conflicting paper overrides from other packs |
| Model is too high | Change `appearance.idleYOffset`, not particle emitter height |
| Model is oversized | Check both Java model `display` transforms and crate `appearance.scale` |
| Key looks right in preview but awkward in hand | Inspect first/third-person transforms in Minecraft |
| Imported model does not open its lid | A single Java mesh does not supply a decomposed hinge/controller |
| PNG is over the session limit | Reduce resolution/compression or use the file workflow; per-file and total limits both apply |

The generated pack does not synchronize itself to players merely because server configuration was reloaded.
