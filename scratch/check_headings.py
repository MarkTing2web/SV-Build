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
    "portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
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
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

with open("heading_violations.txt", "w", encoding="utf-8") as out:
    for fpath in files:
        full_path = os.path.join(base_dir, fpath)
        if not os.path.exists(full_path):
            continue
            
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        seen_h2 = False
        seen_h3 = False
        last_heading = None
        violation = None
        
        for match in re.finditer(r'<(h[1-6])[^>]*>(.*?)</\1>', content, re.IGNORECASE | re.DOTALL):
            tag = match.group(1).lower()
            text = re.sub(r'<[^>]*>', '', match.group(2)).strip()
            # Clean up newlines and spaces in text
            text = " ".join(text.split())
            line_no = content[:match.start()].count('\n') + 1
            
            if tag == 'h3':
                if not seen_h2:
                    violation = f"{tag} \"{text}\" at line {line_no} — h3 before h2"
                    break
                seen_h3 = True
                
            elif tag == 'h4':
                if not seen_h3:
                    violation = f"{tag} \"{text}\" at line {line_no} — h4 before h3"
                    break
                if last_heading == 'h2':
                    violation = f"{tag} \"{text}\" at line {line_no} — h2 to h4 skip"
                    break
                    
            elif tag == 'h2':
                seen_h2 = True
                
            last_heading = tag
            
        if violation:
            out.write(f"FILE: {fpath}\n")
            out.write(f"VIOLATION: {violation}\n\n")
