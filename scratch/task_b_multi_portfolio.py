import os
import re

base_dir = r"c:\Projects\SV-Build"

sunlove_hero = "/images/portfolio/healthcare/sunlove-card.webp"
if os.path.exists(os.path.join(base_dir, r"images\portfolio\healthcare\sunlove-hero.webp")):
    sunlove_hero = "/images/portfolio/healthcare/sunlove-hero.webp"

fort_st_hero = "/images/portfolio/data-centres/fort-st-engineering-rel.webp"
if os.path.exists(os.path.join(base_dir, r"images\portfolio\data-centres\fort-st-engineering-hero.webp")):
    fort_st_hero = "/images/portfolio/data-centres/fort-st-engineering-hero.webp"

updates = {
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html": {
        "hero": sunlove_hero,
        "og": "https://www.securevision.com.sg/images/portfolio/healthcare/sunlove-rel.webp",
        "has_mobile": False
    },
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html": {
        "hero": "/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-hero.webp",
        "og": "https://www.securevision.com.sg/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-hero.webp",
        "has_mobile": False 
    },
    "portfolio/data-centres/fort-data-centre-access-upgrade.html": {
        "hero": "/images/portfolio/data-centres/fort-data-centre-hero.webp",
        "og": "https://www.securevision.com.sg/images/portfolio/data-centres/fort-data-centre-hero.webp",
        "has_mobile": True,
        "mobile": "/images/portfolio/data-centres/fort-data-centre-mobile.webp"
    },
    "portfolio/data-centres/fort-st-engineering.html": {
        "hero": fort_st_hero,
        "og": "https://www.securevision.com.sg/images/portfolio/data-centres/fort-st-engineering-rel.webp",
        "has_mobile": False
    }
}

count = 0
for rel_path, data in updates.items():
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    hero_tag = '<header class="portfolio-hero">'
    new_hero_tag = f'<header class="portfolio-hero" style="background-image: linear-gradient(rgba(14,26,43,0.82), rgba(14,26,43,0.82)), url(\'{data["hero"]}\');">'
    if hero_tag in content:
        content = content.replace(hero_tag, new_hero_tag)
    
    if data["has_mobile"]:
        mobile_css = f"""  <style>
  @media (max-width: 768px) {{
    .portfolio-hero {{
      background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('{data["mobile"]}') !important;
    }}
  }}
  </style>
"""
        if data["mobile"] not in content:
            if '</style>' in content:
                mobile_css_inner = f"""  @media (max-width: 768px) {{
    .portfolio-hero {{
      background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('{data["mobile"]}') !important;
    }}
  }}
"""
                content = content.replace('</style>', mobile_css_inner + '</style>')
            else:
                content = content.replace('</head>', mobile_css + '</head>')
                
    og_meta = f'<meta property="og:image" content="{data["og"]}">'
    if 'property="og:image"' in content:
        content = re.sub(r'<meta\s+property="og:image"\s+content="[^"]*">', og_meta, content)
    else:
        if '<meta property="og:url"' in content:
            content = re.sub(r'(<meta property="og:url" content="[^"]*">)', r'\1\n  ' + og_meta, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated {rel_path}")

surya_path = os.path.join(base_dir, r"portfolio\healthcare\surya-home.html")
with open(surya_path, 'r', encoding='utf-8') as f:
    surya_content = f.read()

if 'property="og:image"' in surya_content:
    surya_content = re.sub(r'<meta\s+property="og:image"\s+content="[^"]*">\s*', '', surya_content)
    with open(surya_path, 'w', encoding='utf-8') as f:
        f.write(surya_content)
    count += 1
    print("Updated surya-home.html")

print(f"Task B updated {count} files.")
