# Gameplay Guide

UniCrates delivers an intuitive yet deeply customizable crate experience for players on your server.

---

## 1. Crates & Keys

### Physical vs Virtual Keys
- **Physical Keys**: Custom 3D modeled items that players hold in their hands. In UniCrates 2.0, first-person viewmodel angles point keys naturally forward in the player's grasp.
- **Virtual Keys**: Digital balances stored securely in SQLite/MySQL or FlatFiles, allowing players to open crates without carrying items. Checked via `/crate key balance [crate]`.

### Portable Crate Items
Admins can grant portable crate items (`/crate give <player> <crate> <amount>`), which players can place in the world or right-click to open on the fly depending on configuration.

---

## 2. Opening Sequences

### Standard & GUI Openings
- **Roulette / CS:GO Style**: Horizontal scrolling item carousel that gradually slows down to highlight the winning reward.
- **Reels & Strip**: Slot-machine style spinning strips.
- **Selective Choice**: Non-gambling mode offering players 3 face-down cards to pick their favorite reward.

### Interactive 3D Poké Ball Roulette
- 3 to 5 floating Poké Balls hover in a semi-circle around the crate.
- As the player looks at each Poké Ball, it smoothly enlarges via GPU transformation interpolation.
- The player must click their choice using their **main hand**. Non-selected Poké Balls dissipate with smoke poof particles, while the winner reveals the prize accompanied by fanfare sounds.
- **Safety Guard**: 15-second timeout or walking away (>8 blocks) automatically picks a reward so players never lose their keys.

---

## 3. Anti-Interference Shield (Anti-Griefing)

To prevent players from clustering around someone actively rolling a crate or trying to grief animations:
- An active opening activates an **Anti-Interference Shield**.
- Any other player who attempts to click or interact with the crate while an opening sequence is running is immediately repelled with a gentle radial knockback velocity.
- The interfering player receives a clear feedback notice:  
  `"This crate is currently being opened by another player! Please wait."`

---

## 4. Graphical Reward Odds Preview

Players can inspect the contents and transparent odds of any crate:
- **How to Open**: Right-click the crate anchor with an empty hand, or type `/crate preview <crate_id>`.
- **Rarity Highlights**: Common (Gray), Uncommon (Green), Rare (Blue), Epic (Purple), Legendary (Gold), Mythic (Pink).
- **Percentages**: Automatically calculated from the underlying weighted RNG system ($P_i = W_i / \sum W$).
- **Limits**: Daily win limits and lifetime limits are displayed dynamically per player.
