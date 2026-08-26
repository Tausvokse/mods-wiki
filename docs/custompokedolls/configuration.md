# Configuration
To add your own Custom Pokedolls, simply place your assets into the generated folder structure inside your Minecraft instance directory.

## Folder Structure
```text
.minecraft/
└── custom_pokedolls/
    ├── geo/                 (Place your .geo.json models here)
    └── textures/            (Place your .png textures here)
```
*(Note: The mod also gracefully falls back to scanning the base `custom_pokedolls/` directory and `textures/block/` or `textures/item/` subfolders if preferred).*

## Naming Conventions
Files must be identically named using lowercase letters and underscores (`snake_case`) to be successfully paired.
For example, to add a "Charizard" doll:
1. **Model**: `charizard.geo.json` (Save inside the `geo/` folder).
2. **Texture**: `charizard.png` (Save inside the `textures/` folder).
3. **Shiny Texture** *(Optional)*: `charizard_shiny.png` OR `shiny_charizard.png` (Save inside the `textures/` folder).

Once the files are placed, run `/pokedolls reload` in-game, and your new statue will instantly appear in the Creative menu!