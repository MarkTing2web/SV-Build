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

incorrect_files = []
correct_files = []

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        nav_line = -1
        hero_line = -1
        trust_bar_line = -1
        breadcrumb_line = -1
        section_line = -1
        
        for i, line in enumerate(lines):
            l = line.lower()
            if nav_line == -1 and '<nav id="sv-nav"' in l:
                nav_line = i + 1
            if hero_line == -1 and ('<header class="hero' in l or '<header class="portfolio-hero' in l or ('<header' in l and 'hero' in l)):
                hero_line = i + 1
            if trust_bar_line == -1 and ('<div class="trust-bar"' in l or '<div class="sv-trust-bar"' in l or '<div class="trust-bar ' in l):
                trust_bar_line = i + 1
            if breadcrumb_line == -1 and '<nav class="sv-breadcrumb"' in l:
                breadcrumb_line = i + 1
            if section_line == -1 and breadcrumb_line != -1 and i + 1 > breadcrumb_line:
                if '<section' in l or '<main' in l:
                    section_line = i + 1
                    
        order_correct = "Yes"
        if nav_line == -1 or hero_line == -1 or trust_bar_line == -1 or breadcrumb_line == -1 or section_line == -1:
            order_correct = "No"
        elif not (nav_line < hero_line < trust_bar_line < breadcrumb_line < section_line):
            order_correct = "No"
            
        elements = [
            ("nav", nav_line),
            ("hero", hero_line),
            ("trust-bar", trust_bar_line),
            ("breadcrumb", breadcrumb_line),
            ("first-section", section_line)
        ]
        elements_sorted = sorted([e for e in elements if e[1] != -1], key=lambda x: x[1])
        actual_order = " -> ".join([f"{name}({line})" for name, line in elements_sorted])
        missing = [f"{name}(-1)" for name, line in elements if line == -1]
        if missing:
            actual_order += " -> " + " -> ".join(missing)
            
        res_str = f"{filepath} | {nav_line} | {hero_line} | {trust_bar_line} | {breadcrumb_line} | {section_line} | {order_correct}"
        
        if order_correct == "No":
            res_str += f"\nACTUAL ORDER: {actual_order}"
            incorrect_files.append(res_str)
        else:
            correct_files.append(res_str)
            
    except Exception as e:
        incorrect_files.append(f"{filepath} | Error | Error | Error | Error | Error | No\nACTUAL ORDER: Error: {str(e)}")

print("File | nav line | hero line | trust-bar line | breadcrumb line | first-section line | Order correct")
for res in incorrect_files:
    print(res)
for res in correct_files:
    print(res)
