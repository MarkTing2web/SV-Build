import os

files = [
    # Condominiums
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

target = '<script src="/nav-footer.js"></script>'

updated_count = 0
for rel_path in files:
    full_path = os.path.join(r"c:\Projects\SV-Build", rel_path)
    if not os.path.exists(full_path):
        print(f"ERROR: {rel_path} does not exist!")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if '/systems-block.js' in content:
        print(f"SKIPPED (already present): {rel_path}")
        continue
        
    if target in content:
        lines = content.splitlines(keepends=True)
        new_lines = []
        injected = False
        for line in lines:
            if target in line:
                indent = line[:line.find(target)]
                new_lines.append(f"{indent}<script src=\"/systems-block.js\"></script>\n")
                new_lines.append(line)
                injected = True
            else:
                new_lines.append(line)
        
        if injected:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write("".join(new_lines))
            print(f"UPDATED: {rel_path}")
            updated_count += 1
        else:
            print(f"ERROR (could not inject): {rel_path}")
    else:
        print(f"ERROR (target script tag not found): {rel_path}")

print(f"\nTotal files updated: {updated_count}")
