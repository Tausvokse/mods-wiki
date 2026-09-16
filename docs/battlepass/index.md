# Cobblemon Ranked Battle Pass

Welcome to the official technical and administration guide for **Cobblemon Ranked Battle Pass** — the premier seasonal progression engine engineered for Minecraft 1.21.1 across Fabric and NeoForge.

---

## Overview

Cobblemon Ranked Battle Pass introduces an engaging, seasonal tier-based progression loop to Minecraft Cobblemon servers. Designed to drive daily active engagement and tournament participation without violating the Minecraft Commercial Usage Guidelines (EULA), all progression tracks offer 100% cosmetic and non-pay-to-win utility rewards.

### Key Highlights
- **Dual-Track Progression**: Fully separated **Free** and **Premium** reward tiers.
- **Cobblemon 1.7 / 1.8+ Native Integration**: Automatically hooks `CobblemonEvents.BATTLE_VICTORY` to grant pass XP based on PvP battle difficulty, ranked tournament matches, and wild boss encounters.
- **Minecraft 1.21.1 Data Components**: Persisted cleanly via `BattlePassData` custom data components and wire-safe `CustomPacketPayload` network synchronizations.
- **GeckoLib Animated Visuals**: Exclusive cosmetic Pokéball skins, custom Pokédoll statues, particle trails, and victory title displays.
- **Full Hot-Reload Support**: Tweak rewards, XP curves, and seasonal durations on the fly without server restarts.

---

## Core Mechanics & Game Loop

```
  +-----------------------------------------------------------+
  |              Cobblemon Battle Event Trigger               |
  | (Ranked PvP Match / Casual Battle / Wild Mega Encounter)  |
  +-----------------------------+-----------------------------+
                                |
                                v
  +-----------------------------------------------------------+
  |               XP Calculation & Scaling Engine             |
  |  - Base PvP Victory: +250 XP                              |
  |  - Tournament Match Multiplier: 1.5x                      |
  |  - Daily First Win Bonus: +500 XP                         |
  +-----------------------------+-----------------------------+
                                |
                                v
  +-----------------------------------------------------------+
  |               Pass Progression State Machine              |
  |  - Re-evaluates Tier = floor(f(TotalXP))                  |
  |  - Unlocks claimable nodes on Free & Premium tracks       |
  |  - Dispatches SyncBattlePassPayload (S2C) to Client       |
  +-----------------------------+-----------------------------+
                                |
                                v
  +-----------------------------------------------------------+
  |            Cosmetic Reward Claim & Delivery               |
  |  - Pokédoll Statues & 3D Animated Pokéball Skins          |
  |  - Particle Auras & Custom Chat Titles                    |
  +-----------------------------------------------------------+
```

### XP Curve Formula
Progression follows a soft-capped polynomial curve that rewards consistent play while preventing instant season completion:

$$\text{RequiredXP}(T) = 1000 + 150 \cdot (T - 1)^{1.25}$$

- **Tiers 1–10**: Rapid onboarding (1,000 – 2,500 XP per tier).
- **Tiers 11–35**: Mid-season engagement (2,500 – 6,000 XP per tier).
- **Tiers 36–50**: Prestige endgame rewards (6,000 – 10,000 XP per tier).

---

## Configuration (`config/battlepass.json`)

The battle pass is configured via standard JSON format. Below is an excerpt of a production configuration:

```json
{
  "season": {
    "id": "season_1_champions",
    "name": "Season 1: League of Champions",
    "duration_days": 60,
    "max_tier": 50,
    "base_xp_per_tier": 1000,
    "growth_exponent": 1.25
  },
  "xp_sources": {
    "ranked_pvp_win": 250,
    "casual_pvp_win": 100,
    "wild_boss_win": 75,
    "daily_first_win_bonus": 500
  },
  "tiers": [
    {
      "tier": 1,
      "required_xp": 1000,
      "free_reward": {
        "type": "item",
        "item": "cobblemon:poke_ball",
        "count": 16,
        "title": "Trainer's Starter Kit"
      },
      "premium_reward": {
        "type": "cosmetic_title",
        "title_id": "title_challenger",
        "display": "&6[Challenger]"
      }
    },
    {
      "tier": 10,
      "required_xp": 3800,
      "free_reward": {
        "type": "pokedoll",
        "doll_id": "custompokedolls:eevee",
        "scale": 1.0
      },
      "premium_reward": {
        "type": "pokeball_skin",
        "skin_id": "geckolib:animated_luxury_ball"
      }
    },
    {
      "tier": 50,
      "required_xp": 25000,
      "free_reward": {
        "type": "cosmetic_aura",
        "aura_id": "unicrates:celestial_sparks"
      },
      "premium_reward": {
        "type": "pokedoll",
        "doll_id": "custompokedolls:mewtwo_armored",
        "scale": 1.8,
        "shiny": true
      }
    }
  ]
}
```

---

## Administration & Commands

| Command | Permission | Description |
| :--- | :--- | :--- |
| `/battlepass` | `battlepass.user.view` | Opens the interactive Battle Pass GUI. |
| `/battlepass claim <tier> [track]` | `battlepass.user.claim` | Claims an unlocked reward on free or premium track. |
| `/battlepass addxp <player> <amount>` | `battlepass.admin.addxp` | Grants battle pass XP to a specific player. |
| `/battlepass setlevel <player> <tier>` | `battlepass.admin.setlevel`| Manually overrides a player's pass tier. |
| `/battlepass grantpremium <player>` | `battlepass.admin.grant` | Unlocks the premium reward track for the player. |
| `/battlepass reload` | `battlepass.admin.reload` | Hot-reloads seasonal configuration and rewards. |

---

## Developer & Integration API

### Listening to Pass Events
Cobblemon Ranked Battle Pass exposes an extensible event bus for server administrators and addon developers:

```java
// Example: Listening to Battle Pass Level Up Event
BattlePassEvents.PLAYER_LEVEL_UP.register((player, newTier, wasPremium) -> {
    player.sendSystemMessage(Component.literal("§a§l[BattlePass] §fCongratulations! You reached Tier " + newTier + "!"));
    player.playNotifySound(SoundEvents.UI_TOAST_CHALLENGE_COMPLETE, SoundSource.PLAYERS, 1.0f, 1.0f);
    return InteractionResult.SUCCESS;
});
```

### Pure Domain Layer Architecture
The core calculation engine (`PassProgression`) is completely separated from Minecraft/Loom dependencies, allowing full unit test coverage and easy porting:

```java
PassProgression progression = new PassProgression(currentXp, claimedFreeMask, claimedPremiumMask, isPremium);
PassRewardClaimResult result = progression.claimReward(targetTier, isPremiumTrack);
```
