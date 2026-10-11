---
title: Integrations & Extension Points
description: Actual Cobblemon, LuckPerms, Impactor, Discord, economy bridge, and web relay behavior.
---

# Integrations & Extension Points

Integrations combine optional runtime adapters with data-defined rewards. Enable the required provider, verify availability, and test delivery using your actual installed versions. The interface names below describe the current source; they are not a promise of binary compatibility across releases.

## Integration matrix

| Integration | Implemented behavior | Configuration / prerequisite |
| --- | --- | --- |
| Cobblemon | Pokémon/item/egg rewards; Pokémon properties; party/PC placement; species-derived preview items and cinematic support | Cobblemon mod present; the main config declares a version expectation of `1.7.3` |
| LuckPerms | Permission checks, permission rewards, permission/meta-based eligibility and modifiers | Mod present, service available, integration settings enabled where checked |
| Impactor | Asynchronous account balance, deposit/withdraw and awaited account save | Economy enabled with provider `impactor`, compatible Impactor API present |
| Custom economy bridge | One registered `EconomyProvider` used by currency costs/rewards | Call `EconomyProviders.register(provider)` and enable economy |
| Discord webhook | Rarity/crate-routed win announcements with delivered Pokémon details | Discord config enabled and valid webhook routing |
| Web editor relay | Crate/timeline snapshots and model/PNG patches through HTTP | Compatible relay and configured browser URL |
| External item resource packs | Existing registered item + matching CMD override | Client pack installed and CMD ranges coordinated |

## Cobblemon rewards

`CobblemonIntegration` isolates direct Cobblemon classes behind runtime availability checks. The Pokémon issuer's `isAvailable()` checks `Services.PLATFORM.isModLoaded("cobblemon")`; availability is evaluated per issuer. Do not assume a declaration in `main-config.json` alone supplies the dependency or changes every issuer's gate.

Example reward entry:

```json
{
  "id": "festival_eevee",
  "type": "cobblemon_pokemon",
  "displayName": "&eFestival Eevee",
  "weight": 5,
  "rarity": "rare",
  "pokemon": {
    "species": "eevee",
    "level": 15,
    "shiny": false,
    "ballType": "cobblemon:poke_ball"
  }
}
```

`buildProperties` parses an optional `propertiesString`, then applies explicit fields such as species, form, aspects, level, shiny/shinyChance, ability, nature, held item, ball type, nickname, IV preset, gender, and moves. Explicit shiny state takes precedence over shiny chance. An explicit six-value IV preset replaces conflicting minimum-perfect-IV requirements.

Delivery uses party storage with PC fallback. The transactional delivery path prepares reward identity/state instead of treating an animation preview as a granted Pokémon. Display species/appearance come from the selected reward configuration; the Master Ball opening is not bound to a fixed species.

Source: `common/.../integration/cobblemon/CobblemonIntegration.java` and the three `Cobblemon*RewardIssuer` classes.

## LuckPerms and fallback behavior

`PermissionChecker.hasPermission(player, node)` allows blank nodes, consults LuckPerms when enabled/present/available, and otherwise uses configured fallback behavior with vanilla permission level 2. `PermissionChecker.isAdmin` also permits an OP-level-2 player directly, even if normal permission checks were configured to avoid an OP fallback.

Permission rewards use an awaited LuckPerms save. Temporary grants freeze their expiry in prepared external reward state, so replaying the same transaction does not extend a temporary permission. Reward entries can also require all listed permissions or exclude players with any denied permission; the selection pipeline evaluates eligibility before weighted choice.

Refer to [permissions](../administration/permissions) and [rewards](../custom-content/rewards) for nodes, limits, and modifier settings.

## Economy providers

Enable the shipped Impactor route in the main config:

```json
{
  "integrations": {
    "economy": {
      "enabled": true,
      "provider": "impactor"
    }
  }
}
```

This is a section to merge, not a complete main config. On reload, `UniCrates.reload()` attempts `ImpactorEconomyAdapter.tryRegister()` when that selection is enabled. The adapter resolves Impactor API methods reflectively, checks transaction success, and awaits an explicit public account save.

The default provider string `vault` does not mean a built-in Vault adapter exists. This checkout includes the Impactor adapter and a generic provider interface. If your currency system is different, supply a bridge or use an installed server command through a command reward.

### Actual provider contract

```java
package com.unicrates.integration.economy;

import java.util.UUID;
import java.util.concurrent.CompletionStage;

public interface EconomyProvider {
    boolean deposit(UUID playerId, double amount);
    boolean withdraw(UUID playerId, double amount);
    double balance(UUID playerId);
    String providerName();
    // Source includes default depositAsync, withdrawAsync, balanceAsync methods.
    // Override those methods when the backing API already provides futures.
}
```

Register an implementation after its backing service is ready:

```java
import com.unicrates.integration.economy.EconomyProvider;
import com.unicrates.integration.economy.EconomyProviders;

public final class MyEconomyBridge {
    private MyEconomyBridge() {}

    public static void install(EconomyProvider provider) {
        EconomyProviders.register(provider);
    }
}
```

`EconomyProviders` stores one volatile active provider; a later registration replaces it. There is no multi-provider routing registry. Make lifecycle order explicit, particularly if reload is configured to register Impactor again.

Default async methods run legacy synchronous methods on a worker. Override them for a provider with native futures, and respect the backend's own thread rules. Do not block the Minecraft thread waiting on network/database calls.

An economy reward is available only when the economy config is enabled and a provider is registered. Currency amount must be finite and positive for a reward deposit. Delivery saves a prepared external transaction before deposit and records the outcome afterward. An interrupted deposit whose outcome is uncertain is retained for administrator review; automatic replay is not equivalent to a safe retry against every currency API.

## Discord announcements

`DiscordWebhookService` snapshots game/config facts on the server thread, constructs immutable JSON, and sends through a bounded worker pool and admission limiter. Overload can drop announcements, and remote HTTP errors can still occur; webhook success is separate from prize delivery.

Delivered Pokémon details support announcement fields that reflect the awarded Pokémon. Webhook configuration and URLs are not part of the ordinary web-editor snapshot. See the [configuration guide](../configuration/) for Discord routing/options. The webhook service is an internal notification service, not a public event bus with subscribe/register hooks.

## Relay HTTP contract

The bundled Worker accepts these routes:

| Route | Behavior |
| --- | --- |
| `GET /health` | Service status, declared version, TTL, maximum body size |
| `POST /post` or `POST /api/session` | Store JSON, return `key`, `token`, `url`, and `expiresIn` |
| `POST /post?key=<key>` | Update an existing protected key with its token |
| `GET /<key>` or `GET /api/session/<key>` | Return stored JSON; request `Accept: application/json` |
| `POST /close/<key>` | Close/delete; token required for a protected existing session |
| `DELETE /<key>` or `DELETE /api/session/<key>` | Equivalent close/delete route |
| `OPTIONS` | CORS preflight |

Tokens are accepted via `Authorization: Bearer <token>`, `X-Session-Token`, or the relay request's `token` query parameter. The browser stores capabilities in sessionStorage and strips the initial fragment token. Sessions use a 24-hour KV TTL and a 5-MiB request-body limit. The reader enforces that limit while streaming rather than trusting Content-Length alone.

Session reads are currently unauthenticated, and returned payloads are not field-redacted. New snapshot keys are not bound to a particular Minecraft administrator/server. The server's admin-guarded apply command validates content and stages it but does not perform origin ownership or stale-version checks. See [web editor](../custom-content/web-editor#session-authorization-and-expiry) for operator-visible consequences.

The normal browser save creates a new key each time. Its apply snapshot remains available for the server command. The server's post-apply close call does not send a token or verify HTTP status, so a protected saved key can remain reusable until authorized deletion or TTL expiry.

### Resource patch envelope

```json
{
  "crates": {},
  "animations": null,
  "resources": {
    "models/example.json": {
      "encoding": "utf8",
      "data": "{\"parent\":\"minecraft:item/generated\",\"textures\":{\"layer0\":\"minecraft:item/paper\"}}"
    }
  }
}
```

This illustrates serialization only. Applying an empty `crates` object replaces the server crate set with an empty set. Texture assets use `encoding: "base64"` and canonical base64 PNG data. Paths are relative to `config/unicrates/resources/`; the upload validator restricts models and custom PNGs and resolves dependencies before any live swap.

The current payload/Worker health version string remains `2.1.0-beta` in source even though this wiki documents the 2.3 release line. Treat it as legacy transport metadata, not a reliable feature negotiation protocol.

## Integrating custom content versus extending runtime

| Need | Appropriate route |
| --- | --- |
| Your own crate, key, rewards, particle settings | JSON/web editor |
| Your own cube model and textures | Validated Java model import + resource pack |
| Your own timed opening choreography | Custom timeline JSON |
| Your own economy service | Implement/register `EconomyProvider` |
| A brand-new reward type | Source changes to enum, issuer dispatch, validation, UI and delivery |
| A new scene controller or mesh renderer | Source changes to runtime/client code; not a JSON-model upload |

The source does not expose a general third-party reward-registration API, arbitrary scene/plugin registry, or runtime item registration. Extend those systems deliberately and verify both loaders and dedicated-server initialization.
