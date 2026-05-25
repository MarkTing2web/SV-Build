import os

html_path = r"c:\Projects\SV-Build\portfolio\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

task_c_rules = [
    ('/images/portfolio/rezi-3two-thumb.png', '/images/portfolio/condominiums/rezi32-rel.webp'),
    ('/images/portfolio/mergui-mansions-facade.webp', '/images/portfolio/condominiums/mergui-mansions-rel.webp'),
    ('/images/portfolio/idyllic-suites-front-facade.webp', '/images/portfolio/condominiums/idyllic-suites-rel.webp'),
    ('/images/portfolio/newton21-front-facade.webp', '/images/portfolio/condominiums/newton21-rel.webp'),
    ('/images/portfolio/lviv-front-entrance-gate-hero.webp', '/images/portfolio/condominiums/the-lviv-rel.webp'),
    ('/images/portfolio/light-at-cairnhill-front-facade-hero.webp', '/images/portfolio/condominiums/light-cairnhill-rel.webp'),
    ('/images/portfolio/condominiums/village-pasir-panjang-hero.webp', '/images/portfolio/condominiums/the-village-at-pasir-panjang-rel.webp')
]

task_c_count = 0
for old_src, new_src in task_c_rules:
    # We look for exact src="old_src" or src='old_src'
    # Actually, let's just do a string replacement on the old_src
    # Since these are specific paths, string replace is safe.
    
    # Count occurrences
    count = content.count(f'"{old_src}"') + content.count(f"'{old_src}'")
    task_c_count += count
    
    content = content.replace(f'"{old_src}"', f'"{new_src}"')
    content = content.replace(f"'{old_src}'", f"'{new_src}'")

print(f"Task C replaced {task_c_count} instances.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
