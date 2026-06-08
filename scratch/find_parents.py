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

try:
    from bs4 import BeautifulSoup
    has_bs4 = True
except ImportError:
    has_bs4 = False

with open("parent_classes.txt", "w", encoding="utf-8") as out:
    for fpath, line in tasks:
        full = os.path.join(base_dir, fpath)
        if not os.path.exists(full):
            continue
            
        with open(full, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        if has_bs4:
            content = "".join(lines)
            soup = BeautifulSoup(content, 'html.parser')
            # find the h4 at the specific line. BS4 doesn't easily map lines to tags.
            # So we will extract a unique string from that line.
            target_line = lines[line-1]
            match = re.search(r'<h4[^>]*>(.*?)</h4>', target_line, re.IGNORECASE)
            if match:
                text = match.group(1).strip()
                h4s = soup.find_all('h4')
                found = False
                for h4 in h4s:
                    if text in str(h4):
                        parent = h4.parent
                        pclass = " ".join(parent.get('class', [])) if parent.get('class') else "NONE"
                        out.write(f"FILE: {fpath} — line {line} — parent class: {pclass}\n")
                        found = True
                        break
                if not found:
                    out.write(f"FILE: {fpath} — line {line} — parent class: UNKNOWN (Not found in soup)\n")
            else:
                 out.write(f"FILE: {fpath} — line {line} — parent class: UNKNOWN (No h4 on line)\n")
        else:
            # simple regex backward search
            closed_tags = 0
            parent_class = "UNKNOWN"
            for i in range(line-1, -1, -1):
                text = lines[i]
                closed_tags += len(re.findall(r'</div|</li>|</article', text, re.IGNORECASE))
                
                # find opening tags with class
                open_tags = list(re.finditer(r'<(div|li|article)[^>]*class=["\']([^"\']+)["\'][^>]*>', text, re.IGNORECASE))
                for match in reversed(open_tags):
                    if closed_tags > 0:
                        closed_tags -= 1
                    else:
                        parent_class = match.group(2)
                        break
                if parent_class != "UNKNOWN":
                    break
            out.write(f"FILE: {fpath} — line {line} — parent class: {parent_class}\n")
