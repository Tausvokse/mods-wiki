---
layout: home

hero:
  name: "Mod Documentation Hub"
  text: "High-Performance Minecraft & Cobblemon Mods"
  tagline: "Official guides, configuration references, and developer documentation for Minecraft 1.21.1."
  actions:
    - theme: brand
      text: Explore UniCrates
      link: /unicrates/getting-started/
    - theme: alt
      text: Ranked Battle Pass
      link: /battlepass/
    - theme: alt
      text: Cobblemon Tournaments
      link: /tourney/
    - theme: alt
      text: Custom Pokedolls
      link: /custompokedolls/

features:
  - icon: 🎁
    title: UniCrates
    details: Universal animated crates powered by Display Entities, custom GeckoLib opening sequences, and Showdown reward pools. Cross-loader Fabric & NeoForge.
    link: /unicrates/
  - icon: ⚔️
    title: Ranked Battle Pass
    details: Seasonal dual-track progression engine with Cobblemon 1.7+ battle hooks, cosmetic Pokédoll & Pokéball skins, and 100% EULA-compliant rewards.
    link: /battlepass/
  - icon: 📡
    title: CobbleTracker
    details: Real-time legendary and shiny Pokémon radar with in-world beacon beams, custom HUD cards, and 3D animated GUI sprites.
    link: /cobbletracker/
  - icon: 🏆
    title: Cobblemon Tournament
    details: Automated competitive engine featuring Glicko-2 ranked queues, Swiss/Elimination brackets, and official Showdown clause enforcement.
    link: /tourney/
  - icon: 🧸
    title: Custom Pokedolls
    details: GeckoLib 4.7-animated Pokémon statues and collectibles with dynamic scale modifiers, auto-rotation, and dedicated-server crash protection.
    link: /custompokedolls/
  - icon: ❓
    title: Who's That Pokémon?
    details: Engaging chat and GUI guessing minigame with real-time dynamic silhouette dilation shaders, leaderboards, and sound effects.
    link: /guessthepokemon/
---

<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-number">1.21.1</div>
    <div class="stat-label">Target Minecraft Version</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">Dual-Loader</div>
    <div class="stat-label">Fabric & NeoForge Native</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">0.0 ms</div>
    <div class="stat-label">Display Entity Overhead</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">100%</div>
    <div class="stat-label">EULA Compliant Architecture</div>
  </div>
</div>

<style>
:root {
  --vp-home-hero-name-color: transparent;
  --vp-home-hero-name-background: -webkit-linear-gradient(120deg, #bd34fe 30%, #41d1ff);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  max-width: 1152px;
  margin: 3rem auto 1rem auto;
  padding: 0 1.5rem;
}

.stat-card {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  transition: transform 0.25s ease, border-color 0.25s ease;
}

.stat-card:hover {
  transform: translateY(-4px);
  border-color: var(--vp-c-brand-1);
}

.stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: var(--vp-c-brand-1);
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  font-weight: 500;
}
</style>
