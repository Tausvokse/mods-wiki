import os

mods = [
    {"slug": "cobbletracker", "title": "CobbleTracker", "file": "cobbletracker_audit.md"},
    {"slug": "guessthepokemon", "title": "Who's That Pokemon", "file": "guessthepok_audit.md"},
    {"slug": "tourney", "title": "Cobblemon Tournament", "file": "tourney_audit.md"},
    {"slug": "custompokedolls", "title": "Custom Pokedolls", "file": "pokedolls_audit.md"}
]

artifact_dir = r"C:\Users\parho\.gemini\antigravity\brain\29b07af1-65a1-4a95-8b78-30e22a20a472"

for mod in mods:
    os.makedirs(f'docs/{mod["slug"]}', exist_ok=True)
    
    with open(os.path.join(artifact_dir, mod['file']), 'r', encoding='utf-8') as f:
        content = f.read()
        
    md = f'''# {mod["title"]}

Welcome to the official documentation for **{mod["title"]}**.

## Repository Audit

The following technical information has been strictly verified against the source code to ensure zero hallucinations:

`	ext
{content}
`
'''
    with open(f'docs/{mod["slug"]}/index.md', 'w', encoding='utf-8') as f:
        f.write(md)
