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

print("File | CTA button label found | Action taken")

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the CTA section
        cta_match = re.search(r'<section\s+class="[^"]*cta-(?:section|high-impact)[^"]*"[^>]*>.*?</section>', content, re.DOTALL)
        
        if not cta_match:
            print(f"{filepath} | N/A | Not found [FLAG]")
            continue

        cta_block = cta_match.group(0)
        
        if "Request a Proposal" in cta_block:
            print(f"{filepath} | Request a Proposal | Already correct")
            continue
            
        # Match the a tag
        a_tag_pattern = r'(<a[^>]*>)\s*Book\s+(?:a\s+)?Site\s+Assessment\s*(</a>)'
        
        match = re.search(a_tag_pattern, cta_block, re.IGNORECASE)
        if match:
            # We want to know exactly what the label was
            label_found = match.group(0).replace(match.group(1), '').replace(match.group(2), '').strip()
            
            # Replace
            new_cta_block = re.sub(a_tag_pattern, r'\g<1>Request a Proposal\2', cta_block, flags=re.IGNORECASE)
            
            new_content = content[:cta_match.start()] + new_cta_block + content[cta_match.end():]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"{filepath} | {label_found} | Updated")
        else:
            print(f"{filepath} | Unknown | Not found [FLAG]")

    except Exception as e:
        print(f"{filepath} | Error: {e} | Not found [FLAG]")
