import os
import re

files = [
    "portfolio/commercial/altitudex-sentosa-commercial.html",
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html",
    "portfolio/commercial/scape-commercial.html",
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/mergui-mansions-novena-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/industrial/cyrus-tech-industrial.html",
    "portfolio/industrial/hoy-san-industrial.html",
    "portfolio/industrial/sta-compliance-imaging.html",
    "portfolio/industrial/sta-inspection-industrial.html",
    "portfolio/institutions/cpf-maxwell-institution.html",
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

print("File | sv-wa-float found | Removed | sv-wa-float still present")

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        found = "No"
        removed = "No"
        
        if re.search(r'class=["\']sv-wa-float["\']', content):
            found = "Yes"
            pattern = r'\n*[ \t]*<a[^>]*class=["\']sv-wa-float["\'][^>]*>.*?</a>[ \t]*\n*'
            new_content = re.sub(pattern, '\n', content, flags=re.DOTALL)
            
            if new_content != content:
                removed = "Yes"
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                content = new_content
                
        still_present = "No"
        if re.search(r'class=["\']sv-wa-float["\']', content):
            still_present = "Yes"
            
        print(f"{os.path.basename(filepath)} | {found} | {removed} | {still_present}")
    except Exception as e:
        print(f"{os.path.basename(filepath)} | Error: {e} | N/A | N/A")
