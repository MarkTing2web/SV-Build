import os
import re

files = [
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html",
    "portfolio/commercial/em-services-call-centre-redhill.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

print("File | Class before fix | Class after fix | Changed")
print("---|---|---|---")

for fpath in files:
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        print(f"{fpath} | FILE NOT FOUND | N/A | Error")
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r'<nav[^>]*aria-label="Breadcrumb"[^>]*>')
    match = pattern.search(content)
    
    # Just in case some use different casing or it's missing aria-label
    # I'll fall back to checking if there's any `<nav class="...breadcrumb...">`
    if not match:
        pattern2 = re.compile(r'<nav[^>]*class="[^"]*breadcrumb[^"]*"[^>]*>')
        match = pattern2.search(content)
        
    if match:
        full_tag = match.group(0)
        class_attr = re.search(r'class="([^"]*)"', full_tag)
        old_class = class_attr.group(1) if class_attr else ""
        
        if old_class != "sv-breadcrumb":
            if 'class="' in full_tag:
                new_tag = re.sub(r'class="[^"]*"', 'class="sv-breadcrumb"', full_tag)
            else:
                new_tag = full_tag.replace('<nav ', '<nav class="sv-breadcrumb" ')
                
            content = content.replace(full_tag, new_tag)
            
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)
                
            print(f"{fpath} | {old_class if old_class else 'None'} | sv-breadcrumb | Yes")
        else:
            print(f"{fpath} | {old_class} | sv-breadcrumb | No")
    else:
        print(f"{fpath} | NOT FOUND | NOT FOUND | Error")
