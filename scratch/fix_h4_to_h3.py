import os
import re

tasks = [
    ("portfolio/commercial/altitudex-sentosa-commercial.html", 282),
    ("portfolio/commercial/catholic-centre-security-partnership.html", 300),
    ("portfolio/commercial/em-services-call-centre-redhill.html", 273),
    ("portfolio/commercial/hilton-singapore-orchard-fire-door.html", 308),
    ("portfolio/commercial/scape-commercial.html", 301),
    ("portfolio/commercial/scape-smart-booking-access.html", 280),
    ("portfolio/commercial/st-engineering-mobility-cctv.html", 264),
    ("portfolio/condominiums/clearwater-access-salto-partnership.html", 280),
    ("portfolio/condominiums/clearwater-cctv-upgrade.html", 276),
    ("portfolio/condominiums/high-oak-condominium-cctv.html", 256),
    ("portfolio/condominiums/idyllic-suites-geylang-condo.html", 179),
    ("portfolio/condominiums/light-cairnhill-condo.html", 179),
    ("portfolio/condominiums/newton21-newton-condo.html", 162),
    ("portfolio/condominiums/rezi-3two-condo.html", 274),
    ("portfolio/condominiums/suites-cairnhill-intercom-lpr.html", 271),
    ("portfolio/condominiums/the-verte-telok-kurau-condo.html", 152),
    ("portfolio/condominiums/village-pasir-panjang-condo.html", 188),
    ("portfolio/data-centres/fort-data-centre-access-upgrade.html", 267),
    ("portfolio/data-centres/fort-st-engineering.html", 234),
    ("portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html", 284),
    ("portfolio/healthcare/surya-home.html", 293),
    ("portfolio/industrial/cogent-logistics-hub-cctv.html", 294),
    ("portfolio/industrial/cyrus-tech-industrial.html", 269),
    ("portfolio/industrial/mitsubishi-elevator-face-access-bms.html", 273),
    ("portfolio/industrial/multibase-construction-security-upgrade.html", 282),
    ("portfolio/industrial/smartflex-tampines.html", 300),
    ("portfolio/industrial/sta-compliance-imaging.html", 170),
    ("portfolio/industrial/sta-inspection-industrial.html", 230),
    ("portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html", 282),
    ("portfolio/institutions/catholic-centre-waterloo.html", 229),
    ("portfolio/institutions/changi-airport-lpr-barriers.html", 265),
    ("portfolio/institutions/cpf-maxwell-institution.html", 262),
    ("portfolio/institutions/das-learning-centre-woodlands.html", 282),
    ("portfolio/institutions/my-world-preschool-cctv.html", 282),
    ("portfolio/institutions/sengkang-interim-bus-interchange.html", 301),
    ("portfolio/institutions/sfx-retreat-centre-punggol.html", 263),
    ("portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html", 232),
    ("portfolio/managed-living/scb-worker-dormitory-jalan-papan.html", 231),
    ("portfolio/condominiums/country-grandeur-upper-thomson-condo.html", 179),
    ("portfolio/condominiums/d-elias-pasir-ris-condo.html", 183)
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

with open("h4_to_h3_results.txt", "w", encoding="utf-8") as out:
    out.write("File | Line number changed | Tag before | Tag after | Other h4s unchanged\n")
    out.write("---|---|---|---|---\n")

    for fpath, line in tasks:
        full = os.path.join(base_dir, fpath)
        if not os.path.exists(full):
            continue
            
        with open(full, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        # Count original h4s
        orig_content = "".join(lines)
        h4_count_before = len(re.findall(r'<h4', orig_content, re.IGNORECASE))
        
        target_line = lines[line-1]
        
        # Check if there's an h4 to change
        if re.search(r'<h4', target_line, re.IGNORECASE):
            tag_before = "h4"
            
            # replace h4 with h3
            new_line = re.sub(r'<h4([^>]*)>', r'<h3\1>', target_line, flags=re.IGNORECASE)
            new_line = re.sub(r'</h4>', r'</h3>', new_line, flags=re.IGNORECASE)
            
            lines[line-1] = new_line
            
            tag_after = "h3" if re.search(r'<h3', new_line, re.IGNORECASE) else "unknown"
            
            new_content = "".join(lines)
            h4_count_after = len(re.findall(r'<h4', new_content, re.IGNORECASE))
            
            unchanged = "Yes" if h4_count_before - h4_count_after == 1 else "No"
            
            out.write(f"{fpath} | {line} | {tag_before} | {tag_after} | {unchanged}\n")
            
            with open(full, "w", encoding="utf-8") as f:
                f.writelines(lines)
        else:
            out.write(f"{fpath} | {line} | none | none | N/A\n")
