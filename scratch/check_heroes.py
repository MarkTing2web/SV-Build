import os
import re

portfolio_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio"

portfolio_hero_files = []
hero_compact_files = []

for root, _, files in os.walk(portfolio_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            rel_path = os.path.relpath(filepath, portfolio_dir).replace('\\', '/')
            if rel_path.lower() == 'index.html':
                continue
            
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                
                if re.search(r'class="[^"]*portfolio-hero[^"]*"', content):
                    portfolio_hero_files.append(rel_path)
                
                if re.search(r'class="[^"]*hero-compact[^"]*"', content):
                    hero_compact_files.append(rel_path)

print("Files using portfolio-hero class:")
if portfolio_hero_files:
    for f in sorted(portfolio_hero_files):
        print(f"- {f}")
else:
    print("- None")

print("\nFiles using hero-compact class:")
if hero_compact_files:
    for f in sorted(hero_compact_files):
        print(f"- {f}")
else:
    print("- None")
