import os

mods = {
    'tourney': {'title': 'Cobblemon Tournament', 'price': '25$'},
    'custompokedolls': {'title': 'Custom Pokedolls', 'price': '25$'}
}

for slug, data in mods.items():
    with open(f'docs/{slug}/index.md', 'w', encoding='utf-8') as f:
        f.write(f'''# {data["title"]}

Welcome to the official documentation for **{data["title"]}**.

This is a premium mod available for purchase.
**Price:** {data["price"]}

<a href="https://discord.gg/HDV4T4NGym" target="_blank" style="display: inline-block; padding: 10px 20px; background-color: #5865F2; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 10px;">Buy in our Discord Server</a>

Use the sidebar to explore the features, configuration, and commands.
''')
