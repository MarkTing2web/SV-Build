import os
import re

html_path = r"c:\Projects\SV-Build\portfolio\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

task_b_rules = [
    ('/portfolio/condominiums/high-oak-condominium-cctv.html', '/images/prop-condo.webp', '/images/portfolio/condominiums/high-oak-condominium-rel.webp'),
    ('/portfolio/condominiums/the-bale-intercom-cctv.html', '/images/prop-condo.webp', '/images/portfolio/condominiums/the-bale-rel.webp'),
    ('/portfolio/condominiums/clearwater-access-salto-partnership.html', '/images/prop-condo.webp', '/images/portfolio/condominiums/the-clearwater-rel.webp'),
    ('/portfolio/condominiums/suites-cairnhill-intercom-lpr.html', '/images/prop-condo.webp', '/images/portfolio/condominiums/suites-cairnhill-rel.webp'),
    ('/portfolio/condominiums/clearwater-cctv-upgrade.html', '/images/prop-condo.webp', '/images/portfolio/condominiums/the-clearwater-rel.webp'),
    ('/portfolio/condominiums/hillview-park-cctv-upgrade.html', '/images/prop-condo.webp', '/images/portfolio/condominiums/hillview-park-condo-rel.webp')
]

task_b_count = 0
parts = content.split('<a ')
for i in range(1, len(parts)):
    for href_val, old_img, new_img in task_b_rules:
        # Check if the href is exactly this
        if f'href="{href_val}"' in parts[i] or f"href='{href_val}'" in parts[i]:
            if f'src="{old_img}"' in parts[i] or f"src='{old_img}'" in parts[i]:
                parts[i] = parts[i].replace(f'src="{old_img}"', f'src="{new_img}"')
                parts[i] = parts[i].replace(f"src='{old_img}'", f"src='{new_img}'")
                task_b_count += 1
                
content = '<a '.join(parts)

print(f"Task B replaced {task_b_count} instances.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
