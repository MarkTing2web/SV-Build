import os

replacements = {
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html": [
        "<li>Restoring Reliability through Strategic Intercom Modernisation</li>",
        "<li>Country Grandeur</li>"
    ],
    "portfolio/condominiums/d-elias-pasir-ris-condo.html": [
        "<li>From Fragmentation to Unified Security at D'Elias</li>",
        "<li>D'Elias</li>"
    ],
    "portfolio/condominiums/idyllic-suites-geylang-condo.html": [
        "<li>Restoring Estate-Wide Security and Access Reliability</li>",
        "<li>Idyllic Suites</li>"
    ],
    "portfolio/condominiums/light-cairnhill-condo.html": [
        "<li>Strategic System Consolidation and Estate Modernisation</li>",
        "<li>Light@Cairnhill</li>"
    ],
    "portfolio/residential/upper-east-coast-road-landed-home.html": [
        "<li>Ten Years of Upgrades for a Home That Kept Evolving</li>",
        "<li>Upper East Coast Road</li>"
    ]
}

print("File | Fourth breadcrumb item text")

for filepath, (old_text, new_text) in replacements.items():
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if old_text in content:
            content = content.replace(old_text, new_text)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Verify the 4th item text
            print(f"{os.path.basename(filepath)} | {new_text.replace('<li>', '').replace('</li>', '')}")
        else:
            print(f"{os.path.basename(filepath)} | Not found")
    except Exception as e:
        print(f"{os.path.basename(filepath)} | Error: {e}")
