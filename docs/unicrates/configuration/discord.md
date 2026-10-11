# Discord reward announcements

File: `config/unicrates/discord.yml`. Discord announcements run asynchronously after confirmed reward delivery. Discord delivery is independent from the in-game broadcastOnWin flag.

## Minimal configuration

```yaml
enabled: false
default_webhook_url: ""
min_rarity: "rare"
include_player_avatar: true
avatar_url_template: "https://minotar.net/helm/{player}/100.png"
include_cobblemon_stats: true
channels:
  by_crate:
  by_rarity:
```

Set enabled true and supply your actual Discord webhook URL to turn it on. Keep webhook tokens private. UniCrates validates webhook targets; an arbitrary HTTP endpoint is not an interchangeable webhook receiver.

The current parser is a small purpose-built YAML subset, not a full YAML library. Use the generated layout, double-quoted strings and simple maps. Do not rely on anchors, block scalars or complex YAML types. The serializer writes enabled on the first line; keeping this convention is useful, but the actual parser skips blank/comment lines and does not enforce a literal first-line requirement. Its inline-comment handling strips text after `#`, including within quoted strings, so avoid hash characters in values.

## All fields

| YAML key | Default | Behavior |
| --- | --- | --- |
| `enabled` | `false` | Enable webhook announcements |
| `default_webhook_url` | `""` | Fallback webhook; legacy webhook_url also recognized |
| `min_rarity` | `"rare"` | Minimum tier; common, uncommon, rare, epic, legendary, mythic; all/blank removes threshold |
| `include_player_avatar` | `true` | Include configured avatar URL |
| `avatar_url_template` | `"https://minotar.net/helm/{player}/100.png"` | Template supporting player/UUID substitution |
| `include_cobblemon_stats` | `true` | Include verified delivered Pokémon details when available |
| `channels.by_crate` | empty map | Exact crate-ID routing |
| `channels.by_rarity` | empty map | Lowercase rarity routing |

Routing priority: crate-specific webhook, then rarity-specific webhook, then default. The rarity filter applies before routing. The webhook threshold helper recognizes ancient as mythic-level for compatibility, but crate reward validation supports mythic rather than ancient.

Example routing fragment to add to a real configuration:

```yaml
channels:
  by_crate:
    starter: "https://discord.com/api/webhooks/REPLACE_ID/REPLACE_TOKEN"
  by_rarity:
    legendary: "https://discord.com/api/webhooks/REPLACE_ID/REPLACE_TOKEN"
    mythic: "https://discord.com/api/webhooks/REPLACE_ID/REPLACE_TOKEN"
```

Those placeholders are not functional URLs. Use real webhook URLs from your Discord server, then `/crate reload`.

## Delivered facts and transport limits

Pokémon details come from an immutable snapshot of the exact delivered transaction UUID found in party or PC: species/form, level, shiny, nature, ability, gender, six IVs and six EVs. If delivery facts cannot be verified, Pokémon detail fields are omitted. Configuration presets and random chance settings are not presented as delivered statistics.

The transport admits at most four queued/in-flight announcements, with a token burst of five and one token refill per 500 ms. Excess announcements are dropped with throttled logging. Requests time out after six seconds. There is no guaranteed webhook delivery or automatic retry. Payload fields are bounded to embed limits, automatic mentions are disabled, and transport errors avoid logging webhook tokens.

A missing Discord card does not mean reward delivery failed. Check player storage, actual inventory/party/PC and server win logs before issuing compensation. For missing cards, inspect enabled, minimum rarity, selected routing URL and server transport logs first.

Source: `DiscordConfig`, `DiscordConfigYamlParser`, `DiscordWebhookService`, `DiscordWebhookSafety`, `RewardDelivery`.
