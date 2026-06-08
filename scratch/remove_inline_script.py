import os
import re

files = [
    "portfolio/commercial/altitudex-sentosa-commercial.html",
    "portfolio/commercial/catholic-centre-security-partnership.html",
    "portfolio/commercial/em-services-call-centre-redhill.html",
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html",
    "portfolio/commercial/scape-commercial.html",
    "portfolio/commercial/scape-smart-booking-access.html",
    "portfolio/commercial/st-engineering-mobility-cctv.html",
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
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html",
    "portfolio/data-centres/fort-st-engineering.html",
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/industrial/cogent-logistics-hub-cctv.html",
    "portfolio/industrial/cyrus-tech-industrial.html",
    "portfolio/industrial/hoy-san-industrial.html",
    "portfolio/industrial/mitsubishi-elevator-face-access-bms.html",
    "portfolio/industrial/multibase-construction-security-upgrade.html",
    "portfolio/industrial/smartflex-tampines.html",
    "portfolio/industrial/sta-compliance-imaging.html",
    "portfolio/industrial/sta-inspection-industrial.html",
    "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html",
    "portfolio/institutions/catholic-centre-waterloo.html",
    "portfolio/institutions/changi-airport-lpr-barriers.html",
    "portfolio/institutions/cpf-maxwell-institution.html",
    "portfolio/institutions/das-learning-centre-woodlands.html",
    "portfolio/institutions/my-world-preschool-cctv.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/institutions/sfx-retreat-centre-punggol.html",
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html",
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

patterns = [
    r"\.sv-bizsafe",
    r"\.sv-sites",
    r"\.sv-licence",
    r"SV\.bizsafeLevel",
    r"SV\.siteDisplay",
    r"SV\.licenceNumber"
]

def check_script(script_text):
    for pattern in patterns:
        if re.search(pattern, script_text):
            return True
    return False

print("File | Inline script found | Removed | bizSAFE string still in body")
print("---|---|---|---")

script_found = False

def repl(m):
    global script_found
    script_tag = m.group(0)
    inner_html = m.group(1)
    
    if 'src=' in script_tag:
        return script_tag # keep it
        
    if check_script(inner_html):
        script_found = True
        return "\n" # Replace with a single newline
    return script_tag

for fpath in files:
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        continue
        
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    script_pattern = re.compile(r'(?:\n\s*)?<script\b[^>]*>([\s\S]*?)</script>(?:\n\s*)?', re.IGNORECASE)
    
    script_found = False
    new_content = script_pattern.sub(repl, content)
    
    if script_found:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        has_bizsafe = "Yes" if "bizSAFE" in new_content else "No"
        flag = " 🚩" if has_bizsafe == "Yes" else ""
        print(f"{fpath} | Yes | Yes | {has_bizsafe}{flag}")
    else:
        print(f"{fpath} | Not present — skipped | N/A | N/A")
