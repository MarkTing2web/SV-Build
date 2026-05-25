import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Projects\SV-Build"

residential = [
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

condos = [
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
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html"
]

commercial = [
    "portfolio/commercial/altitudex-sentosa-commercial.html",
    "portfolio/commercial/catholic-centre-security-partnership.html",
    "portfolio/commercial/em-services-call-centre-redhill.html",
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html",
    "portfolio/commercial/scape-commercial.html",
    "portfolio/commercial/scape-smart-booking-access.html",
    "portfolio/commercial/st-engineering-mobility-cctv.html"
]

all_files = residential + condos + commercial

def get_category(fpath):
    if 'residential' in fpath: return 'residential'
    if 'condominiums' in fpath: return 'condominiums'
    if 'commercial' in fpath: return 'commercial'
    return 'unknown'

old_refs = [
    "prop-condo.webp",
    "prop-commercial.webp",
    "prop-landed.webp",
    "prop-industrial.webp",
    "portfolio-scape.webp",
    "portfolio-sta.webp",
    "portfolio-delias.webp",
    "altitudex-hero.webp",
    "scape-hero.webp",
    "hilton-singapore-orchard-hero.webp",
    "catholic-centre-hero.webp",
    "em-services-hero.webp",
    "cyrus-tech-park-hero.webp",
    "sta-building-hero.webp",
    "solution-hub-solution-data-center.png"
]

print("## CHECK 1 — Script load order\n")
print("| File | systems-block.js? | portfolio-block.js? | nav-footer.js? | Correct order? |")
print("|---|---|---|---|---|")

c1_data = []
c2_data = []
c3_data = []

for rel_path in all_files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # CHECK 1
    sys_block = "YES" if '<script src="/systems-block.js"></script>' in content else "NO"
    port_block = "YES" if '<script src="/portfolio-block.js"></script>' in content else "NO"
    nav_foot = "YES" if '<script src="/nav-footer.js"></script>' in content else "NO"

    idx_sys = content.find('<script src="/systems-block.js"></script>')
    idx_port = content.find('<script src="/portfolio-block.js"></script>')
    idx_nav = content.find('<script src="/nav-footer.js"></script>')
    
    order_correct = "YES" if (-1 < idx_sys < idx_port < idx_nav) else "NO"
    print(f"| {os.path.basename(rel_path)} | {sys_block} | {port_block} | {nav_foot} | {order_correct} |")

    # CHECK 2
    has_port = "YES" if 'class="sv-portfolio-block"' in content else "NO"
    expected_cat = get_category(rel_path)
    
    cat_match = re.search(r'data-category=["\'](.*?)["\']', content)
    cat_correct = "YES" if (cat_match and cat_match.group(1) == expected_cat) else "NO"
    
    exc_match = re.search(r'data-exclude=["\'](.*?)["\']', content)
    exc_present = "YES" if exc_match else "NO"
    exc_val = exc_match.group(1) if exc_match else ""
    
    hardcoded = "YES" if "related-project-card" not in content else "NO"

    c2_data.append(f"| {os.path.basename(rel_path)} | {has_port} | {cat_correct} | {exc_present} | {exc_val} | {hardcoded} |")

    # CHECK 3
    found_refs = []
    for ref in old_refs:
        matches = list(re.finditer(ref, content))
        if matches:
            for m in matches:
                start = max(0, m.start() - 30)
                context = content[start:m.start()]
                
                needs_commercial = ["altitudex-hero.webp", "scape-hero.webp", "hilton-singapore-orchard-hero.webp", "catholic-centre-hero.webp"]
                
                if ref in needs_commercial:
                    if '/commercial/' not in context:
                        found_refs.append(ref)
                        break
                else:
                    found_refs.append(ref)
                    break
    
    found_str = ", ".join(found_refs) if found_refs else ""
    any_found = "YES" if found_refs else "CLEAN"
    c3_data.append(f"| {os.path.basename(rel_path)} | {any_found} | {found_str} |")

print("\n## CHECK 2 — sv-portfolio-block div present and correct\n")
print("| File | sv-portfolio-block present? | data-category correct? | data-exclude present? | data-exclude value | No hardcoded cards? |")
print("|---|---|---|---|---|---|")
for row in c2_data:
    print(row)

print("\n## CHECK 3 — No old broken image references remain\n")
print("| File | Any old references found? | Which ones |")
print("|---|---|---|")
for row in c3_data:
    print(row)
