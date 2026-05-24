import os

replacements = {
    "/images/portfolio/country-grandeur-condo.webp": "/images/portfolio/condominiums/country-grandeur-condo.webp",
    "/images/portfolio/country-grandeur-wide.webp": "/images/portfolio/condominiums/country-grandeur-wide.webp",
    "/images/portfolio/d-elias-front-facade.webp": "/images/portfolio/condominiums/d-elias-front-facade.webp",
    "/images/portfolio/d-elias-front-gate.webp": "/images/portfolio/condominiums/d-elias-front-gate.webp",
    "/images/portfolio/idyllic-condo-facade.webp": "/images/portfolio/condominiums/idyllic-condo-facade.webp",
    "/images/portfolio/idyllic-condo-main.webp": "/images/portfolio/condominiums/idyllic-condo-main.webp",
    "/images/portfolio/idyllic-suites-front-facade.webp": "/images/portfolio/condominiums/idyllic-suites-front-facade.webp",
    "/images/portfolio/light-at-cairnhill-entrance.webp": "/images/portfolio/condominiums/light-at-cairnhill-entrance.webp",
    "/images/portfolio/light-condo-facade.webp": "/images/portfolio/condominiums/light-condo-facade.webp",
    "/images/portfolio/light-condo-main-hero.webp": "/images/portfolio/condominiums/light-condo-main-hero.webp",
    "/images/portfolio/lviv-condo-akuvox-upgrade.webp": "/images/portfolio/condominiums/lviv-condo-akuvox-upgrade.webp",
    "/images/portfolio/lviv-condo-biometric.webp": "/images/portfolio/condominiums/lviv-condo-biometric.webp",
    "/images/portfolio/lviv-condo-palm-reader.webp": "/images/portfolio/condominiums/lviv-condo-palm-reader.webp",
    "/images/portfolio/lviv-front-entrance-gate-hero.webp": "/images/portfolio/condominiums/lviv-front-entrance-gate-hero.webp",
    "/images/portfolio/mergui-condo-building.webp": "/images/portfolio/condominiums/mergui-condo-building.webp",
    "/images/portfolio/mergui-condo-intercom.webp": "/images/portfolio/condominiums/mergui-condo-intercom.webp",
    "/images/portfolio/mergui-mansions-facade.webp": "/images/portfolio/condominiums/mergui-mansions-facade.webp",
    "/images/portfolio/newton-21-condo-intercom.webp": "/images/portfolio/condominiums/newton-21-condo-intercom.webp",
    "/images/portfolio/newton-21-condo-main.webp": "/images/portfolio/condominiums/newton-21-condo-main.webp",
    "/images/portfolio/newton21-180-wide-angle-camera.webp": "/images/portfolio/condominiums/newton21-180-wide-angle-camera.webp",
    "/images/portfolio/newton21-akuvox-x915-lobby.webp": "/images/portfolio/condominiums/newton21-akuvox-x915-lobby.webp",
    "/images/portfolio/newton21-front-facade.webp": "/images/portfolio/condominiums/newton21-front-facade.webp",
    "/images/portfolio/newton21-smartplus-app.webp": "/images/portfolio/condominiums/newton21-smartplus-app.webp",
    "/images/portfolio/the-verte-condo-facade.webp": "/images/portfolio/condominiums/the-verte-condo-facade.webp",
    "/images/portfolio/village-at-pasir-panjang-front-entrance.webp": "/images/portfolio/condominiums/village-at-pasir-panjang-front-entrance.webp",
    "/images/portfolio/village-condo-gantrygo.webp": "/images/portfolio/condominiums/village-condo-gantrygo.webp",
    "/images/portfolio/village-condo-intercom.webp": "/images/portfolio/condominiums/village-condo-intercom.webp"
}

files = [
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
    "portfolio/condominiums/village-pasir-panjang-condo.html"
]

total_files_updated = 0

for rel_path in files:
    full_path = os.path.join(r"c:\Projects\SV-Build", rel_path)
    if not os.path.exists(full_path):
        print(f"ERROR: {rel_path} does not exist!")
        continue
        
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    replacements_made = 0
    new_content = content
    for old, new in replacements.items():
        if old in new_content:
            count = new_content.count(old)
            new_content = new_content.replace(old, new)
            replacements_made += count
            
    if replacements_made > 0:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[{rel_path}] {replacements_made} replacements made.")
        total_files_updated += 1
    else:
        print(f"[{rel_path}] No replacements needed.")

print(f"\nTask D complete: {total_files_updated} files modified.")
