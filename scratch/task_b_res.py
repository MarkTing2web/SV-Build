import os
import re

base_dir = r"c:\Projects\SV-Build"

files = [
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

count = 0
for rel_path in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    slug = '/' + rel_path
    
    new_block = f"""<div class="sv-portfolio-block"
     data-category="residential"
     data-exclude="{slug}"
     data-bg="sv-section-grey"
     data-heading="Related Case Studies"
     data-eyebrow="Next Steps in Discovery"
     data-intro="Explore how we have secured other landed homes across Singapore.">
</div>"""

    content = re.sub(
        r'<section[^>]*>(?:(?!</section>).)*?(?:Related Case Studies|Related Projects|related-project-card).*?</section>',
        new_block,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {rel_path}")

print(f"Task B updated {count} files.")
