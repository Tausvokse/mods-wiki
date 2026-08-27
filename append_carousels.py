import os
import glob

# Mod mapping to public folders
mods = {
    'custompokedolls': 'custompokedolls',
    'cobbletracker': 'poketracker',
    'tourney': 'tourney',
    'unicrates': 'UniCrates',
    'guessthepokemon': 'whothatpokemon'
}

for mod, folder in mods.items():
    index_path = f'docs/{mod}/index.md'
    if not os.path.exists(index_path):
        continue
        
    photos = glob.glob(f'docs/public/{folder}/*.png')
    if not photos:
        continue
        
    carousel_html = '\n\n## Screenshots\n\n<div style="display: flex; overflow-x: auto; gap: 15px; padding: 15px 0; scroll-snap-type: x mandatory; align-items: center; background: rgba(0,0,0,0.1); border-radius: 10px;">\n'
    
    for photo in photos:
        web_path = '/' + os.path.relpath(photo, 'docs/public').replace('\\\\', '/')
        carousel_html += f'  <img src="{web_path}" style="scroll-snap-align: center; max-height: 350px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);" />\n'
        
    carousel_html += '</div>\n'
    
    with open(index_path, 'a', encoding='utf-8') as f:
        f.write(carousel_html)
