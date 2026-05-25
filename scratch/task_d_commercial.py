import os
import re

base_dir = r"c:\Projects\SV-Build"
files = [
    'portfolio/commercial/altitudex-sentosa-commercial.html',
    'portfolio/commercial/catholic-centre-security-partnership.html',
    'portfolio/commercial/em-services-call-centre-redhill.html',
    'portfolio/commercial/hilton-singapore-orchard-fire-door.html',
    'portfolio/commercial/scape-commercial.html',
    'portfolio/commercial/scape-smart-booking-access.html',
    'portfolio/commercial/st-engineering-mobility-cctv.html'
]

count = 0
for rel_path in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    slug = '/' + rel_path
    
    new_block = f"""<div class="sv-portfolio-block"
     data-category="commercial"
     data-exclude="{slug}"
     data-bg="sv-section-white"
     data-heading="Related Case Studies"
     data-eyebrow="Next Steps in Discovery"
     data-intro="Explore how we have delivered security solutions for other commercial properties across Singapore.">
</div>"""

    content = re.sub(
        r'<section[^>]*>(?:(?!</section>).)*?(?:Related Case Studies|related-project-card).*?</section>',
        new_block,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {rel_path}")

print(f"Task D updated {count} files.")
