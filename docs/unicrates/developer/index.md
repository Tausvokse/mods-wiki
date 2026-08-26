# Architecture

UniCrates is built with a core-agnostic architecture. The \core\ module contains all pure Java logic (data structures, math, POJO configurations, pity system). The \common\ module provides multi-loader abstractions (Minecraft classes). The \abric\ and \
eoforge\ modules contain platform-specific hooks.

## Reward Engine
Supports 9 reward types (\item\, \command\, \permission\, \economy\, \experience\, \roadcast_only\, \cobblemon_pokemon\, \cobblemon_item\, \cobblemon_egg\). You can register your own \RewardIssuer\ via the API.

## Storage Backends
FlatFile (default), SQLite, MySQL/MariaDB with automatic migrations.

## Modifying Data
You can read or modify \PlayerData\ directly from \PlayerDataStore\ instance provided by \UniCrates.instance()\. The player data object tracks cooldowns, lifetime opens, daily limits, and virtual keys.
