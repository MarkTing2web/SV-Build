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

replacement = """<div class="trust-bar">
  <div class="container">
    <div class="trust-bar-inner">
      <span>Police Licensed</span>
      <span class="trust-divider">|</span>
      <span class="sv-bizsafe"></span>
      <span class="trust-divider">|</span>
      <span><strong class="sv-sites"></strong> Sites Protected</span>
    </div>
  </div>
</div>"""

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'<div\s+class="(?:sv-)?trust-bar"[^>]*>', content)
        if not match:
            # try finding police licensed and tracking back
            idx_police = content.find("Police Licensed")
            if idx_police != -1:
                # Find the highest level div before this, but this is tricky without dom parsing.
                # Since we know it's a direct child of some section or header, maybe we just use BeautifulSoup
                pass
            print(f"No sv-trust-bar or trust-bar found in {filepath}")
            return False
        
        start_idx = match.start()
        
        div_count = 0
        current_idx = start_idx
        end_idx = -1
        while current_idx < len(content):
            next_open = content.find("<div", current_idx)
            next_close = content.find("</div", current_idx)
            
            if next_close == -1:
                break
                
            if next_open != -1 and next_open < next_close:
                div_count += 1
                current_idx = next_open + 4
            else:
                div_count -= 1
                current_idx = next_close + 5
                if div_count == 0:
                    end_idx = content.find(">", current_idx) + 1
                    break
        
        if end_idx != -1:
            line_start = content.rfind("\\n", 0, start_idx)
            if line_start != -1:
                indent = content[line_start+1:start_idx]
                if not indent.isspace():
                    indent = ""
            else:
                indent = ""
            
            repl_lines = replacement.split("\\n")
            indented_repl = repl_lines[0] + "\\n" + "\\n".join(indent + line for line in repl_lines[1:])
            
            new_content = content[:start_idx] + indented_repl + content[end_idx:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        else:
            print(f"Could not find matching closing div in {filepath}")
            return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

for file in files:
    process_file(file)
