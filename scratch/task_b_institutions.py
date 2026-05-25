import os

base_dir = r"c:\Projects\SV-Build\portfolio\institutions"

replacements = {
    "das-learning-centre-woodlands.html": [
        ("/images/portfolio/das-hero.webp", "/images/portfolio/institutions/das-learning-centre-hero.webp"),
        ("/images/portfolio/das-context.webp", "/images/portfolio/institutions/das-learning-centre-hero.webp"),
        ("/images/portfolio/scape-hero.webp", "/images/portfolio/commercial/scape-rel.webp"),
        ("/images/portfolio/sunlove-haig-hero.webp", "/images/portfolio/healthcare/sunlove-rel.webp")
    ],
    "my-world-preschool-cctv.html": [
        ("/images/portfolio/das-hero.webp", "/images/portfolio/institutions/das-learning-centre-rel.webp"),
        ("/images/portfolio/sunlove-haig-hero.webp", "/images/portfolio/healthcare/sunlove-rel.webp"),
        ("/images/portfolio/sengkang-hero.webp", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
        ("/images/portfolio/my-world-context.webp", "/images/portfolio/institutions/my-world-preschool-hero.webp")
    ],
    "sengkang-interim-bus-interchange.html": [
        ("/images/portfolio/cpf-maxwell-thumb.webp", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
        ("/images/portfolio/surya-home-thumb.png", "/images/portfolio/healthcare/sunlove-rel.webp"),
        ("/images/portfolio/smartflex-thumb.png", "/images/portfolio/industrial/smartflex-at-tampines-rel.webp")
    ],
    "sfx-retreat-centre-punggol.html": [
        ("/images/portfolio/sengkang-interim-thumb.webp", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
        ("/images/portfolio/surya-home-thumb.webp", "/images/portfolio/healthcare/sunlove-rel.webp"),
        ("/images/portfolio/rezi-3two-thumb.webp", "/images/portfolio/condominiums/rezi32-rel.webp")
    ],
    "changi-airport-lpr-barriers.html": [
        ("/images/portfolio/sengkang-interim-thumb.webp", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
        ("/images/portfolio/sfx-retreat-centre-thumb.webp", "/images/portfolio/institutions/st-francis-xavier-retreat-centre-rel.webp"),
        ("/images/portfolio/smartflex-thumb.webp", "/images/portfolio/industrial/smartflex-at-tampines-rel.webp")
    ],
    "catholic-centre-waterloo.html": [
        ("/images/portfolio/sfx-retreat-centre-thumb.webp", "/images/portfolio/institutions/st-francis-xavier-retreat-centre-rel.webp"),
        ("/images/portfolio/sengkang-interim-thumb.webp", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
        ("/images/portfolio/fort-st-engineering-thumb.webp", "/images/portfolio/data-centres/fort-data-centre-rel.webp")
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

print(f"Task B updated {count} files.")
