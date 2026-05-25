import os

base_dir = r"c:\Projects\SV-Build"

updates = {
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html": [
        ("/images/portfolio/surya-home-hero.webp", "/images/portfolio/healthcare/sunlove-rel.webp"),
        ("/images/portfolio/hillview-park-hero.webp", "/images/portfolio/condominiums/hillview-park-condo-rel.webp")
    ],
    "portfolio/healthcare/surya-home.html": [
        ("/images/portfolio/sengkang-interim-thumb.png", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
        ("/images/portfolio/cpf-maxwell-thumb.png", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
        ("/images/portfolio/smartflex-thumb.png", "/images/portfolio/industrial/smartflex-at-tampines-rel.webp")
    ],
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html": [
        ("/images/portfolio/scb-dormitory-thumb.webp", "/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-rel.webp"),
        ("/images/portfolio/surya-home-thumb.webp", "/images/portfolio/healthcare/sunlove-rel.webp"),
        ("/images/portfolio/sfx-retreat-centre-thumb.webp", "/images/portfolio/institutions/st-francis-xavier-retreat-centre-rel.webp")
    ],
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html": [
        ("/images/portfolio/nursing-hostel-thumb.webp", "/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-rel.webp"),
        ("/images/portfolio/surya-home-thumb.webp", "/images/portfolio/healthcare/sunlove-rel.webp"),
        ("/images/portfolio/sfx-retreat-centre-thumb.webp", "/images/portfolio/institutions/st-francis-xavier-retreat-centre-rel.webp")
    ],
    "portfolio/data-centres/fort-data-centre-access-upgrade.html": [
        ("/images/portfolio/portfolio-scape.webp", "/images/portfolio/commercial/scape-rel.webp"),
        ("/images/portfolio/portfolio-sta.webp", "/images/portfolio/industrial/sta-inspection-centre-sin-ming-rel.webp"),
        ("/images/temp-doc/portfolio-cyrus.webp", "/images/portfolio/industrial/cyrus-tech-at-loyang-rel.webp"),
        ("/images/solutions/solution-hub-solution-data-center.png", "/images/portfolio/data-centres/fort-data-centre-rel.webp")
    ],
    "portfolio/data-centres/fort-st-engineering.html": [
        ("/images/portfolio/changi-airport-lpr-thumb.webp", "/images/portfolio/institutions/changi-airside-rel.webp"),
        ("/images/portfolio/sengkang-interim-thumb.webp", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
        ("/images/portfolio/smartflex-thumb.webp", "/images/portfolio/industrial/smartflex-at-tampines-rel.webp")
    ]
}

count = 0
for rel_path, replacements in updates.items():
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    for old_val, new_val in replacements:
        if old_val in content:
            content = content.replace(old_val, new_val)
            changed = True
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {rel_path}")

print(f"Task C updated {count} files.")
