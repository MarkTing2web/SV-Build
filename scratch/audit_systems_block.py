import os
import re

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

old_images = [
    "prop-condo.webp",
    "prop-landed.webp",
    "pillar_surveillance.webp",
    "pillar_people_access.webp",
    "pillar_vehicle.webp",
    "pillar_vehicle_access.webp"
]

print("| File | script tag? | sv-systems-block? | data-systems value | Vehicle override? | Old broken refs? |")
print("|---|---|---|---|---|---|")

for rel_path in files:
    full_path = os.path.join(r"c:\Projects\SV-Build", rel_path)
    if not os.path.exists(full_path):
        # file not found
        print(f"| {rel_path} | NOT FOUND | - | - | - | - |")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check 1: Script tag present
    has_script = "YES" if '<script src="/systems-block.js"></script>' in content else "NO"
    
    # Check 2: sv-systems-block div present
    # regex to check for sv-systems-block class (e.g. class="sv-systems-block" or similar)
    has_div = "NO"
    data_systems = "N/A"
    has_override = "N/A"
    
    # Let's search for sv-systems-block class in elements
    div_match = re.search(r'<[^>]*class="[^"]*sv-systems-block[^"]*"[^>]*>', content)
    if div_match:
        has_div = "YES"
        div_tag = div_match.group(0)
        # extract data-systems
        ds_match = re.search(r'data-systems="([^"]*)"', div_tag)
        if ds_match:
            data_systems = ds_match.group(1)
        else:
            data_systems = "None"
            
        # Check 4: Residential vehicle override present
        if "portfolio/residential/" in rel_path:
            # Let's check for the exact override string or attribute
            override_attr = 'data-desc-vehicle-lpr="Auto gates, sliding gates, and remote entry — secure your driveway and control vehicle access to your home."'
            has_override = "YES" if override_attr in div_tag else "NO"
    
    # Check 5: No old broken image references in Discovery Path
    # Since we want to find if any exist, let's extract the Discovery Path section to check.
    # The discovery path is generally between section opening/closing or commented boundaries.
    # Let's find any occurrences of the old images in the entire content, as they shouldn't be anywhere else in the related sections.
    # Actually, we can search the whole file for these image names to see if they are referenced anywhere in the Discovery Path block, or just print if any are present at all.
    # Wait, the instruction says "Confirm no references to these filenames remain inside the Discovery Path section".
    # Let's locate the Discovery Path section. It starts with a <section containing eyebrow Discovery Path or similar, up to </section>.
    # Let's extract sections and find the one that has "Discovery Path" or "Explore Related Solutions".
    sections = re.findall(r'<section.*?</section>', content, re.DOTALL)
    discovery_section = ""
    for sec in sections:
        if "Discovery Path" in sec or "Explore Related Solutions" in sec or "<!-- DISCOVERY PATH -->" in sec or "<!-- SECTION 9 -->" in sec:
            discovery_section = sec
            break
            
    has_old_refs = "YES (None found)"
    if discovery_section:
        found_refs = []
        for img in old_images:
            if img in discovery_section:
                found_refs.append(img)
        if found_refs:
            has_old_refs = f"NO ({', '.join(found_refs)} present)"
    else:
        # If no discovery section found (maybe it was already replaced or we can't find it)
        # Check the whole file as fallback
        found_refs = []
        for img in old_images:
            if img in content:
                found_refs.append(img)
        if found_refs:
            has_old_refs = f"NO (no section found, but {', '.join(found_refs)} in file)"
        else:
            has_old_refs = "YES (None found)"

    print(f"| `{os.path.basename(rel_path)}` | {has_script} | {has_div} | {data_systems} | {has_override} | {has_old_refs} |")
