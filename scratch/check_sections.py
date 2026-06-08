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
    "portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html",
    "portfolio/data-centres/fort-st-engineering.html",
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/industrial/cogent-logistics-hub-cctv.html",
    "portfolio/industrial/cyrus-tech-industrial.html",
    "portfolio/industrial/mitsubishi-elevator-face-access-bms.html",
    "portfolio/industrial/multibase-construction-security-upgrade.html",
    "portfolio/industrial/smartflex-tampines.html",
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
    "portfolio/residential/upper-east-coast-road-landed-home.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

with open("section_clashes.txt", "w", encoding="utf-8") as out:
    for fpath in files:
        full_path = os.path.join(base_dir, fpath)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        sections = []
        for match in re.finditer(r'<section([^>]*)>', content, re.IGNORECASE):
            attrs = match.group(1)
            class_match = re.search(r'class=["\']([^"\']*)["\']', attrs, re.IGNORECASE)
            if class_match:
                classes = class_match.group(1).split()
                bg_class = None
                if 'sv-section-grey' in classes:
                    bg_class = 'grey'
                elif 'sv-section-white' in classes:
                    bg_class = 'white'
                    
                if bg_class:
                    line_no = content[:match.start()].count('\n') + 1
                    sections.append((len(sections) + 1, bg_class, line_no))
                    
        if not sections:
            continue
            
        clashes = []
        order_str = []
        for i, (sec_idx, bg, line) in enumerate(sections):
            order_str.append(bg)
            if i > 0:
                prev_idx, prev_bg, prev_line = sections[i-1]
                if bg == prev_bg:
                    clashes.append(f"Section {prev_idx} {prev_bg} consecutive with Section {sec_idx} {bg} at lines {prev_line} and {line}")
                    
        if clashes:
            out.write(f"FILE: {fpath}\n")
            out.write(f"Sections in order: {' / '.join(order_str)}\n")
            out.write(f"Clashes: {'; '.join(clashes)}\n\n")
