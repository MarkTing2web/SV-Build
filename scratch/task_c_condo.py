import os
import re

base_dir = r"c:\Projects\SV-Build"

files = [
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
    "portfolio/condominiums/village-pasir-panjang-condo.html"
]

count = 0
for rel_path in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    slug = '/' + rel_path
    
    new_block = f"""<div class="sv-portfolio-block"
     data-category="condominiums"
     data-exclude="{slug}"
     data-bg="sv-section-white"
     data-heading="Related Case Studies"
     data-eyebrow="Next Steps in Discovery"
     data-intro="Explore how we have solved similar security challenges for other condominium estates in Singapore.">
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

print(f"Task C updated {count} files.")
