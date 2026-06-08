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

print('File | Trust bar outer class | Inner class | Divider class | BCA Registered present | sv-sites in strong')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the trust bar element
    match = re.search(r'<div\s+class="(?:sv-)?trust-bar(?:-outer)?"[^>]*>', content)
    if not match:
        idx_police = content.find('Police Licensed')
        if idx_police != -1:
            print(f'{filepath} | N/A | N/A | N/A | N/A | N/A | [FLAG] No recognizable trust bar outer class')
        else:
            print(f'{filepath} | N/A | N/A | N/A | N/A | N/A | [FLAG] No Police Licensed found')
        continue

    start_idx = match.start()
    
    # We want to extract the class name. Need to search again to extract group without outer group issue.
    class_match = re.search(r'class="((?:sv-)?trust-bar(?:-outer)?)"', match.group(0))
    outer_class = class_match.group(1) if class_match else "trust-bar"
    
    # Extract the whole block to analyze it
    div_count = 0
    current_idx = start_idx
    end_idx = -1
    while current_idx < len(content):
        next_open = content.find('<div', current_idx)
        next_close = content.find('</div', current_idx)
        
        if next_close == -1:
            break
            
        if next_open != -1 and next_open < next_close:
            div_count += 1
            current_idx = next_open + 4
        else:
            div_count -= 1
            current_idx = next_close + 5
            if div_count == 0:
                end_idx = content.find('>', current_idx) + 1
                break
                
    if end_idx == -1:
        print(f'{filepath} | {outer_class} | N/A | N/A | N/A | N/A | [FLAG] Malformed HTML')
        continue
        
    block = content[start_idx:end_idx]
    
    # Inner class
    inner_match = re.search(r'<div\s+class="([^"]*trust[^"]*)"', block[len(match.group(0)):])
    inner_class = inner_match.group(1) if inner_match else 'None'
    
    # Divider class
    divider_match = re.search(r'<span\s+class="([^"]*divider[^"]*)"', block)
    divider_class = divider_match.group(1) if divider_match else 'None'
    
    # BCA Registered present
    bca_present = 'Yes' if 'BCA Registered' in block else 'No'
    
    # sv-sites in strong
    sv_sites_match = re.search(r'<strong\s+class="sv-sites"\s*>', block)
    sv_sites_strong = 'Yes' if sv_sites_match else 'No'
    
    flag = ''
    if outer_class != 'trust-bar' or inner_class != 'trust-bar-inner' or divider_class != 'trust-divider' or bca_present != 'No' or sv_sites_strong != 'Yes':
        flag = ' [FLAG]'
        
    print(f'{filepath} | {outer_class} | {inner_class} | {divider_class} | {bca_present} | {sv_sites_strong}{flag}')
