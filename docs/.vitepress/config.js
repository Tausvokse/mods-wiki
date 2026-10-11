import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Mod Documentation Hub',
  description: 'Official technical and user documentation for our mods.',
  appearance: 'dark',
  cleanUrls: true,
  lastUpdated: true,
  markdown: { lineNumbers: true },
  base: '/mods-wiki/',
  themeConfig: {
    outline: [2, 3],
    socialLinks: [{ icon: 'discord', link: 'https://discord.gg/VjU5AybJYr' }],
    nav: [
      { text: 'Home', link: '/' },
      { text: 'UniCrates', link: '/unicrates/' },
      { text: 'CobbleTracker', link: '/cobbletracker/' },
      { text: 'Guess The Pokemon', link: '/guessthepokemon/' },
      { text: 'Tourney', link: '/tourney/' },
      { text: 'Custom Pokedolls', link: '/custompokedolls/' },
      { text: 'Battle Pass', link: '/battlepass/' }
    ],
    sidebar: {
      '/unicrates/': [
        { text: 'UniCrates 2.3', items: [
          { text: 'Overview', link: '/unicrates/' },
          { text: 'Release Notes', link: '/unicrates/release-notes' },
          { text: 'Installation & First Crate', link: '/unicrates/getting-started/' },
          { text: 'Upgrade an Existing Server', link: '/unicrates/getting-started/upgrading' },
          { text: 'Troubleshooting', link: '/unicrates/getting-started/troubleshooting' },
          { text: 'Player Gameplay', link: '/unicrates/gameplay/' },
          { text: 'Keys & Reward Delivery', link: '/unicrates/gameplay/keys-and-rewards' }
        ] },
        { text: 'Configure Your Server', collapsed: false, items: [
          { text: 'Configuration Overview', link: '/unicrates/configuration/' },
          { text: 'Main Config Reference', link: '/unicrates/configuration/main-config' },
          { text: 'Crate Field Reference', link: '/unicrates/configuration/crate-reference' },
          { text: 'Databases, Backups & Recovery', link: '/unicrates/configuration/storage' },
          { text: 'Discord Webhooks', link: '/unicrates/configuration/discord' },
          { text: 'Reward Types & Pokémon', link: '/unicrates/custom-content/rewards' }
        ] },
        { text: 'Models & Crate Creation', collapsed: false, items: [
          { text: 'Customization Overview', link: '/unicrates/custom-content/' },
          { text: 'Create a Crate', link: '/unicrates/custom-content/create' },
          { text: 'Web Editor Walkthrough', link: '/unicrates/custom-content/web-editor' },
          { text: 'All Models & Keys', link: '/unicrates/custom-content/models' },
          { text: 'Import a Custom Model', link: '/unicrates/custom-content/model-import' },
          { text: 'Resource Packs & Textures', link: '/unicrates/custom-content/resource-packs' },
          { text: 'JSON Formats', link: '/unicrates/custom-content/json' }
        ] },
        { text: 'Animation Workshop', collapsed: false, items: [
          { text: 'Watch All Opening GIFs', link: '/unicrates/custom-content/gallery' },
          { text: 'Use a Ready-Made Opening', link: '/unicrates/custom-content/animations' },
          { text: 'Complete Opening Catalog', link: '/unicrates/custom-content/animation-catalog' },
          { text: 'Idle Models & Particle Patterns', link: '/unicrates/custom-content/idle-animations' },
          { text: 'Create Your First Animation', link: '/unicrates/custom-content/animation-tutorial' },
          { text: 'Timeline Action Reference', link: '/unicrates/custom-content/timeline-reference' }
        ] },
        { text: 'Administration & Development', collapsed: true, items: [
          { text: 'Commands', link: '/unicrates/administration/commands' },
          { text: 'Permissions', link: '/unicrates/administration/permissions' },
          { text: 'Developer Architecture', link: '/unicrates/developer/' },
          { text: 'Integration Reference', link: '/unicrates/developer/integrations' },
          { text: 'Support & Custom Animations', link: '/unicrates/support' }
        ] }
      ],
      '/cobbletracker/': [
        {
          text: 'CobbleTracker',
          items: [
            { text: 'Overview', link: '/cobbletracker/' },
            { text: 'Features', link: '/cobbletracker/features' },
            { text: 'Commands', link: '/cobbletracker/commands' },
            { text: 'Configuration', link: '/cobbletracker/configuration' }
          ]
        }
      ],
      '/guessthepokemon/': [
        {
          text: 'Guess The Pokemon',
          items: [
            { text: 'Overview', link: '/guessthepokemon/' },
            { text: 'Features', link: '/guessthepokemon/features' },
            { text: 'Commands', link: '/guessthepokemon/commands' },
            { text: 'Configuration', link: '/guessthepokemon/configuration' }
          ]
        }
      ],
      '/tourney/': [
        {
          text: 'Cobblemon Tournament',
          items: [
            { text: 'Overview', link: '/tourney/' },
            { text: 'Features', link: '/tourney/features' },
            { text: 'Commands', link: '/tourney/commands' },
            { text: 'Configuration', link: '/tourney/configuration' }
          ]
        }
      ],
      '/custompokedolls/': [
        {
          text: 'Custom Pokedolls',
          items: [
            { text: 'Overview', link: '/custompokedolls/' },
            { text: 'Features', link: '/custompokedolls/features' },
            { text: 'Commands', link: '/custompokedolls/commands' },
            { text: 'Configuration', link: '/custompokedolls/configuration' }
          ]
        }
      ],
      '/battlepass/': [
        {
          text: 'Ranked Battle Pass',
          items: [
            { text: 'Overview & Mechanics', link: '/battlepass/' }
          ]
        }
      ]
    },
    search: {
      provider: 'local'
    }
  }
})
