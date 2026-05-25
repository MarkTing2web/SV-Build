import os
import re

base_dir = r"c:\Projects\SV-Build"

files_data = {
    'portfolio/commercial/altitudex-sentosa-commercial.html': {
        'hero': '/images/portfolio/commercial/altitudex-sentosa-hero.webp',
        'mobile': '/images/portfolio/commercial/altitudex-sentosa-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/commercial/altitudex-sentosa-hero.webp'
    },
    'portfolio/commercial/catholic-centre-security-partnership.html': {
        'hero': '/images/portfolio/commercial/catholic-centre-hero.webp',
        'mobile': '/images/portfolio/commercial/catholic-centre-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/commercial/catholic-centre-hero.webp'
    },
    'portfolio/commercial/em-services-call-centre-redhill.html': {
        'hero': '/images/portfolio/commercial/em-engineering-at-jalan-kilang-hero.webp',
        'mobile': '/images/portfolio/commercial/em-engineering-at-jalan-kilang-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/commercial/em-engineering-at-jalan-kilang-hero.webp'
    },
    'portfolio/commercial/hilton-singapore-orchard-fire-door.html': {
        'hero': '/images/portfolio/commercial/hilton-singapore-orchard-hero.webp',
        'mobile': '/images/portfolio/commercial/hilton-singapore-orchard-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/commercial/hilton-singapore-orchard-hero.webp'
    },
    'portfolio/commercial/scape-commercial.html': {
        'hero': '/images/portfolio/commercial/scape-hero.webp',
        'mobile': '/images/portfolio/commercial/scape-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/commercial/scape-hero.webp'
    },
    'portfolio/commercial/scape-smart-booking-access.html': {
        'hero': '/images/portfolio/commercial/scape-hero.webp',
        'mobile': '/images/portfolio/commercial/scape-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/commercial/scape-hero.webp'
    },
    'portfolio/commercial/st-engineering-mobility-cctv.html': {
        'hero': '/images/portfolio/commercial/st-engineering-mobility-hero.webp',
        'mobile': '/images/portfolio/commercial/st-engineering-mobility-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/commercial/st-engineering-mobility-hero.webp'
    }
}

count = 0
for rel_path, data in files_data.items():
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change 1: Hero
    hero_tag = '<header class="portfolio-hero">'
    new_hero_tag = f'<header class="portfolio-hero" style="background-image: linear-gradient(rgba(14,26,43,0.82), rgba(14,26,43,0.82)), url(\'{data["hero"]}\');">'
    if hero_tag in content:
        content = content.replace(hero_tag, new_hero_tag)

    # Change 2: Mobile override
    mobile_css = f"""  @media (max-width: 768px) {{
    .portfolio-hero {{
      background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('{data["mobile"]}') !important;
    }}
  }}
</style>"""
    if data["mobile"] not in content:
        content = content.replace('</style>', mobile_css)

    # Change 3: og:image
    og_meta = f'<meta property="og:image" content="{data["og"]}">'
    if 'property="og:image"' in content:
        content = re.sub(r'<meta\s+property="og:image"\s+content="[^"]*">', og_meta, content)
    else:
        # insert after og:url or og:description
        if '<meta property="og:url"' in content:
            content = re.sub(r'(<meta property="og:url" content="[^"]*">)', r'\1\n  ' + og_meta, content)
        else:
            content = re.sub(r'(<meta property="og:description" content="[^"]*">)', r'\1\n  ' + og_meta, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {rel_path}")

print(f"\nTask B updated {count} files.")
