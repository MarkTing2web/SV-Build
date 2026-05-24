import os
import re

files_to_update = [
    # Condos
    "portfolio/condominiums/clearwater-access-salto-partnership.html",
    "portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/mergui-mansions-novena-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    # Residential
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

updated_count = 0
for filepath in files_to_update:
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Check if already has systems-block.js
    if 'systems-block.js' in content:
        print(f"Skipping (already updated): {filepath}")
        continue
        
    # Find and replace
    target = '<script src="/nav-footer.js"></script>'
    replacement = '<script src="/systems-block.js"></script>\n  <script src="/nav-footer.js"></script>'
    
    if target in content:
        new_content = content.replace(target, replacement)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
        updated_count += 1
    else:
        # Try regular expression replace
        new_content, count = re.subn(
            r'<script\s+src=[\'"]/nav-footer\.js[\'"]>\s*</script>',
            r'<script src="/systems-block.js"></script>\n  <script src="/nav-footer.js"></script>',
            content,
            flags=re.IGNORECASE
        )
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated (regex): {filepath}")
            updated_count += 1
        else:
            print(f"ERROR: Target script tag not found in {filepath}")

print(f"Total updated: {updated_count}")
