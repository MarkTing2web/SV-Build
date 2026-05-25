import os

base_dir = r"c:\Projects\SV-Build\portfolio\industrial"

replacements = {
    "hoy-san-industrial.html": [
        ("/images/portfolio/hoy-san-gantrygo-lpr-barrier.webp", "/images/portfolio/industrial/hoy-san-gantrygo-lpr-barrier.webp"),
        ("/images/portfolio/hoy-san-preparation-work.webp", "/images/portfolio/industrial/hoy-san-preparation-work.webp"),
        ("/images/portfolio/cyrus-tech-park-facade.webp", "/images/portfolio/industrial/cyrus-tech-at-loyang-rel.webp"),
        ("/images/portfolio/newton21-front-facade.webp", "/images/portfolio/industrial/hoy-san-rel.webp")
    ],
    "cyrus-tech-industrial.html": [
        ("/images/portfolio/cyrus-tech-hero.webp", "/images/portfolio/industrial/cyrus-tech-at-loyang-hero.webp"),
        ("/images/portfolio/sta-inspection-centre-front.webp", "/images/portfolio/industrial/sta-inspection-centre-sin-ming-rel.webp")
    ],
    "multibase-construction-security-upgrade.html": [
        ("/images/portfolio/cyrus-hero.webp", "/images/portfolio/industrial/cyrus-tech-at-loyang-rel.webp"),
        ("/images/portfolio/smartflex-hero.webp", "/images/portfolio/industrial/smartflex-at-tampines-rel.webp"),
        ("/images/portfolio/st-mobility-hero.webp", "/images/portfolio/commercial/st-engineering-mobility-rel.webp")
    ],
    "stmicroelectronics-loyang-perimeter-alarm.html": [
        ("/images/portfolio/multibase-hero.webp", "/images/portfolio/industrial/multibase-construction-rel.webp"),
        ("/images/portfolio/cyrus-hero.webp", "/images/portfolio/industrial/cyrus-tech-at-loyang-rel.webp"),
        ("/images/portfolio/smartflex-hero.webp", "/images/portfolio/industrial/smartflex-at-tampines-rel.webp")
    ],
    "smartflex-tampines.html": [
        ("/images/portfolio/cpf-maxwell-thumb.webp", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
        ("/images/portfolio/sengkang-interim-thumb.png", "/images/portfolio/industrial/cogent-1-logistics-hub-rel.webp"),
        ("/images/portfolio/surya-home-thumb.png", "/images/portfolio/industrial/multibase-construction-rel.webp")
    ],
    "cogent-logistics-hub-cctv.html": [
        ("/images/temp-doc/portfolio-cyrus.webp", "/images/portfolio/industrial/cyrus-tech-at-loyang-rel.webp")
    ],
    "mitsubishi-elevator-face-access-bms.html": [
        ("/images/temp-doc/portfolio-cyrus.webp", "/images/portfolio/industrial/cyrus-tech-at-loyang-rel.webp")
    ]
}

count = 0
for filename, repls in replacements.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    for old_val, new_val in repls:
        if old_val in content:
            content = content.replace(old_val, new_val)
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {filename}")

print(f"Task C updated {count} files.")
