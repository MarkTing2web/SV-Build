import os
import re

base_dir = r"c:\Projects\SV-Build"

b1_7 = {
    'portfolio/industrial/cogent-logistics-hub-cctv.html': {
        'hero': '/images/portfolio/industrial/cogent-1-logistics-hub-hero.webp',
        'mobile': '/images/portfolio/industrial/cogent-1-logistics-hub-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/industrial/cogent-1-logistics-hub-hero.webp'
    },
    'portfolio/industrial/cyrus-tech-industrial.html': {
        'hero': '/images/portfolio/industrial/cyrus-tech-at-loyang-hero.webp',
        'mobile': '/images/portfolio/industrial/cyrus-tech-at-loyang-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/industrial/cyrus-tech-at-loyang-hero.webp'
    },
    'portfolio/industrial/mitsubishi-elevator-face-access-bms.html': {
        'hero': '/images/portfolio/industrial/mitsubishi-elevator-singapore-hero.webp',
        'mobile': '/images/portfolio/industrial/mitsubishi-elevator-singapore-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/industrial/mitsubishi-elevator-singapore-hero.webp'
    },
    'portfolio/industrial/multibase-construction-security-upgrade.html': {
        'hero': '/images/portfolio/industrial/multibase-construction-hero.webp',
        'mobile': '/images/portfolio/industrial/multibase-construction-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/industrial/multibase-construction-hero.webp'
    },
    'portfolio/industrial/smartflex-tampines.html': {
        'hero': '/images/portfolio/industrial/smartflex-at-tampines-hero.webp',
        'mobile': '/images/portfolio/industrial/smartflex-at-tampines-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/industrial/smartflex-at-tampines-hero.webp'
    },
    'portfolio/industrial/sta-inspection-industrial.html': {
        'hero': '/images/portfolio/industrial/sta-inspection-centre-sin-ming-hero.webp',
        'mobile': '/images/portfolio/industrial/sta-inspection-centre-sin-ming-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/industrial/sta-inspection-centre-sin-ming-hero.webp'
    },
    'portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html': {
        'hero': '/images/portfolio/industrial/st-microelectronics-loyang-hero.webp',
        'mobile': '/images/portfolio/industrial/st-microelectronics-loyang-mobile.webp',
        'og': 'https://www.securevision.com.sg/images/portfolio/industrial/st-microelectronics-loyang-hero.webp'
    }
}

count = 0
for rel_path, data in b1_7.items():
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    hero_tag = '<header class="portfolio-hero">'
    new_hero_tag = f'<header class="portfolio-hero" style="background-image: linear-gradient(rgba(14,26,43,0.82), rgba(14,26,43,0.82)), url(\'{data["hero"]}\');">'
    if hero_tag in content:
        content = content.replace(hero_tag, new_hero_tag)

    mobile_css = f"""  @media (max-width: 768px) {{
    .portfolio-hero {{
      background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('{data["mobile"]}') !important;
    }}
  }}
</style>"""
    if data["mobile"] not in content:
        content = content.replace('</style>', mobile_css)

    og_meta = f'<meta property="og:image" content="{data["og"]}">'
    if 'property="og:image"' in content:
        content = re.sub(r'<meta\s+property="og:image"\s+content="[^"]*">', og_meta, content)
    else:
        if '<meta property="og:url"' in content:
            content = re.sub(r'(<meta property="og:url" content="[^"]*">)', r'\1\n  ' + og_meta, content)
        else:
            content = re.sub(r'(<meta property="og:description" content="[^"]*">)', r'\1\n  ' + og_meta, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {rel_path}")

filepath = os.path.join(base_dir, r"portfolio\industrial\sta-compliance-imaging.html")
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

og_match = re.search(r'<meta\s+property="og:image"\s+content="([^"]*)">', content)
if og_match:
    og_url = og_match.group(1)
    if 'sta-compliance-hero.jpg' in og_url:
        content = re.sub(r'<meta\s+property="og:image"\s+content="[^"]*">\s*', '', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print("Updated portfolio/industrial/sta-compliance-imaging.html (removed og:image)")

print(f"\nTask B updated {count} files.")
