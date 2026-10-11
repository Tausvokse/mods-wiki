---
title: Create a custom opening
description: Build, assign and tune a complete UniCrates reward reel with valid timeline JSON.
---

# Create a custom opening

This tutorial creates **Aurora Reveal**: an item rises from the crate, cycles through decorative prize icons, locks on the selected reward, displays its name, and disappears cleanly. It uses vanilla display entities and simple particles. You do not need a Pokémon scene controller to run it.

## 1. Prepare a crate

Use an existing working crate with at least two rewards. Confirm its key and reward delivery work before changing presentation. Keep a copy of its JSON. The timeline's decorative reel does not change reward weights or eligibility.

The [catalog](./animation-catalog) and [recorded gallery](./gallery) help you choose a starting style. If you prefer a bundled effect, copy its timeline in `/crates editor`; the following definition is self-contained.

## Browser authoring alternative

You can build the same sequence visually instead of writing a file:

1. Run `/crates editor`, select your crate, and open **Opening timeline**.
2. Select an ordinary JSON preset and choose **Copy timeline**, or choose **Create timeline** when the selected preset has no editable definition. The editor gives the crate its own unique timeline ID.
3. Set **Overall duration** to `120`. Use **Add step** to enter the sequence below; select each step to change its tick, action and fields. **Duplicate step** is useful for similar bursts; **Remove step** deletes a selected action.
4. Use vector inputs for position/destination, the display target fields, and the easing dropdown. If you copied a phase definition, choose **Convert phases to timed steps** before editing individual actions.
5. Resolve displayed validation errors, save the session, and run its generated `/crates apply <hash>` command.

Use the JSON below as the complete field-by-field recipe in either workflow. The browser can edit loaded JSON timelines directly; copying one first protects other crates that share its ID. Controller presets such as Master Singularity and interactive selection do not expose editable action steps.

The timeline track edits actions rather than playing a full opening in 3D. Use [recorded previews](./gallery) to compare presets, then open your custom crate in Minecraft. See the [web editor guide](./web-editor) for the session export/apply workflow.

## 2. Save the complete timeline

Create `config/unicrates/animations/aurora_reveal.json` on the server. Paste this JSON without comments:

```json
{
  "id": "aurora_reveal",
  "durationTicks": 120,
  "timeline": [
    {
      "tick": 0,
      "action": "play_sound",
      "sound": "open"
    },
    {
      "tick": 2,
      "action": "play_particle",
      "particle": "minecraft:poof",
      "particleCount": 12,
      "particleSpeed": 0.02,
      "offset": [0, 0.8, 0]
    },
    {
      "tick": 5,
      "action": "spawn_display",
      "displayId": "reward_icon",
      "displayType": "item_display",
      "offset": [0, 0.8, 0],
      "scale": 0.2,
      "billboard": "fixed",
      "spinSpeed": 4
    },
    {
      "tick": 5,
      "action": "cycle_display_items",
      "target": "reward_icon",
      "cycleIntervalTicks": 2
    },
    {
      "tick": 6,
      "action": "move_display",
      "target": "reward_icon",
      "targetOffset": [0, 1.8, 0],
      "durationTicks": 24,
      "easing": "ease_out_cubic",
      "arcHeight": 0.2,
      "spinSpeed": 4,
      "bobAmplitude": 0.035,
      "bobFrequency": 0.1
    },
    {
      "tick": 6,
      "action": "scale_display",
      "target": "reward_icon",
      "scale": 0.85,
      "durationTicks": 24,
      "easing": "ease_out_cubic",
      "spinSpeed": 4
    },
    {
      "tick": 28,
      "action": "cycle_display_items",
      "target": "reward_icon",
      "cycleIntervalTicks": 5
    },
    {
      "tick": 40,
      "action": "play_sound",
      "sound": "tick"
    },
    {
      "tick": 48,
      "action": "stop_cycle",
      "target": "reward_icon"
    },
    {
      "tick": 48,
      "action": "rotate_display",
      "target": "reward_icon",
      "spinSpeed": 1.5,
      "pitch": 0,
      "bobAmplitude": 0.025,
      "bobFrequency": 0.08
    },
    {
      "tick": 48,
      "action": "spawn_display",
      "displayId": "reward_title",
      "displayType": "text_display",
      "text": "<aqua><b>{reward}</b></aqua>",
      "offset": [0, 2.55, 0],
      "scale": 0.4,
      "billboard": "center"
    },
    {
      "tick": 48,
      "action": "play_sound",
      "sound": "win"
    },
    {
      "tick": 48,
      "action": "play_particle",
      "particle": "minecraft:happy_villager",
      "particleCount": 16,
      "particleSpeed": 0.03,
      "offset": [0, 1.8, 0]
    },
    {
      "tick": 108,
      "action": "despawn_display",
      "target": "reward_title"
    },
    {
      "tick": 108,
      "action": "scale_display",
      "target": "reward_icon",
      "scale": 0.05,
      "durationTicks": 8,
      "easing": "ease_in_cubic",
      "spinSpeed": 0,
      "bobAmplitude": 0
    },
    {
      "tick": 118,
      "action": "despawn_all"
    }
  ]
}
```

## 3. Understand the stages

| Ticks | What happens | Why these fields matter |
| --- | --- | --- |
| `0–4` | Sound and smoke-like poof above the anchor. | `offset` uses bottom Y; `0.8` places the burst near the crate top. |
| `5` | Spawns the reserved reward actor and starts cycling. | `reward_icon` is the selected reward sentinel, not an arbitrary item ID. Array order spawns it before cycling it. |
| `6–29` | Rises to `1.8` and grows from `0.2` to `0.85`. | Move and scale run together. `arcHeight` adds a small lift while monotonic easing still arrives at the destination. |
| `28–47` | Slows content replacement from 2 to 5 ticks. | A new cycle action replaces the previous cycle on the target. |
| `48` | Restores the real winner, slows rotation, creates its title. | `stop_cycle` restores the chosen stack; `rotate_display` updates spin immediately. `{reward}` names the winner. |
| `48–107` | Holds the prize for 3 seconds. | No repeating hold action is required; continuous motion remains active. |
| `108–116` | Removes the title and shrinks the actor. | Explicit `spinSpeed: 0` prevents default reward spin from restarting. |
| `118–120` | Clears displays, then finishes. | Cleanup precedes the end; actual reward delivery happens through normal completion. |

The reel uses random icons from other configured rewards, with the selected reward as fallback when there are no alternatives. This is presentation, not a second eligible-pool lottery. Use Master Singularity when you specifically want its controller's complete eligible-pool pass.

## 4. Assign it to the crate

Merge these sections into your crate JSON. Keep its other sections and use the actual crate ID:

```json
{
  "opening": {
    "openingType": "world_animation",
    "animationId": "aurora_reveal"
  },
  "animation": {
    "type": "aurora_reveal",
    "durationTicks": 120,
    "hideCrate": false,
    "sounds": {
      "open": "minecraft:block.chest.open",
      "tick": "minecraft:block.note_block.hat",
      "win": "minecraft:entity.player.levelup"
    }
  }
}
```

These are merge fragments, not a replacement for a complete crate definition. `opening.animationId` chooses the timeline; `animation.durationTicks` sets the crate's minimum presentation length. Matching both durations avoids a blank pause caused by an older, longer crate duration. `hideCrate: false` preserves the bundled base/lid opening around your prize actor.

## 5. Reload and preview in Minecraft

Run `/crates reload` with administrator permission. Read the command summary and server warnings for invalid animation IDs/JSON. Then use a normal crate key on the placed crate. Check the actor rises above the model, the reel settles on the delivered reward, the label is readable, and temporary displays disappear afterward.

If you change only timeline JSON, no resource-pack rebuild is needed. New models/textures do require their resource-pack workflow. The browser's model/idle preview approximates Minecraft particle sprites and motion; an in-game opening is the final visual check.

## 6. Tune one parameter at a time

| Change | Edit |
| --- | --- |
| Higher prize | `move_display.targetOffset[1]`; move the title and burst upward separately. |
| Slower roll | Increase `cycleIntervalTicks` or delay the stop/title ticks together. |
| Longer prize hold | Move cleanup later and extend both timeline/crate duration, staying within 600 ticks. |
| Still prize | Set final `spinSpeed: 0` and `bobAmplitude: 0`; keep explicit zero spin on later move/scale steps. |
| Larger icon | Increase final scale; leave clearance for the crate and title. |
| Softer effects | Reduce `particleCount`; overlapping bursts share a 48-particle tick budget. |
| Different name color | Edit MiniMessage in `text`, keeping `{reward}`. |

Avoid changing `particles.heightOffset` to move the prize: that field affects only idle emitters. Timeline coordinates, idle model placement and idle particle origins are separate controls.

For composition or preset modifications, continue with [phases and inheritance](./timeline-reference#phases). For an effect you can start from without copying JSON, see the [full catalog](./animation-catalog).
