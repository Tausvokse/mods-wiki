import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Mod Documentation Hub',
  description: 'Official technical and user documentation for our mods.',
  appearance: 'dark',
  cleanUrls: true,
  base: '/mods-wiki/',
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'UniCrates', link: '/unicrates/' },
      { text: 'CobbleTracker', link: '/cobbletracker/' },
      { text: 'Guess The Pokemon', link: '/guessthepokemon/' },
      { text: 'Tourney', link: '/tourney/' },
      { text: 'Custom Pokedolls', link: '/custompokedolls/' }
    ],
    sidebar: {
      '/unicrates/': [
        {
          text: 'Introduction',
          items: [
            { text: 'Getting Started', link: '/unicrates/getting-started/' },
            { text: 'Gameplay', link: '/unicrates/gameplay/' },
          ]
        },
        {
          text: 'Configuration',
          items: [
            { text: 'Configuration Overview', link: '/unicrates/configuration/' },
          ]
        },
        {
          text: 'Custom Content',
          items: [
            { text: 'Overview', link: '/unicrates/custom-content/' },
            { text: 'How to Create a Crate', link: '/unicrates/custom-content/create' },
            { text: 'Custom Models', link: '/unicrates/custom-content/models' },
            { text: 'Rewards Guide', link: '/unicrates/custom-content/rewards' },
            { text: 'Animations', link: '/unicrates/custom-content/animations' },
            { text: 'JSON Formats', link: '/unicrates/custom-content/json' }
          ]
        },
        {
          text: 'Administration',
          items: [
            { text: 'Commands', link: '/unicrates/administration/commands' },
            { text: 'Permissions', link: '/unicrates/administration/permissions' }
          ]
        },
        {
          text: 'Developer Guide',
          items: [
            { text: 'Architecture', link: '/unicrates/developer/' }
          ]
        }
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
      ]
    },
    search: {
      provider: 'local'
    }
  }
})
