import os
import re

files = [
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html",
    "portfolio/commercial/scape-commercial.html",
    "portfolio/commercial/scape-smart-booking-access.html",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/industrial/hoy-san-industrial.html",
    "portfolio/industrial/multibase-construction-security-upgrade.html",
    "portfolio/industrial/smartflex-tampines.html",
    "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html",
    "portfolio/institutions/das-learning-centre-woodlands.html",
    "portfolio/institutions/my-world-preschool-cctv.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

with open("descriptions.txt", "w", encoding="utf-8") as out:
    for fpath in files:
        full = os.path.join(base_dir, fpath)
        if not os.path.exists(full):
            out.write(f"FILE: {fpath}\nNot found\n\n")
            continue
            
        with open(full, "r", encoding="utf-8") as f:
            content = f.read()
            
        dmatch = re.search(r'<meta[^>]*name="description"[^>]*content="(.*?)"', content, re.IGNORECASE)
        if dmatch:
            desc = dmatch.group(1)
            out.write(f"FILE: {fpath}\n")
            out.write(f"CONTENT: {desc}\n")
            out.write(f"LENGTH: {len(desc)}\n\n")
        else:
            out.write(f"FILE: {fpath}\n")
            out.write(f"CONTENT: Not found\n")
            out.write(f"LENGTH: 0\n\n")
