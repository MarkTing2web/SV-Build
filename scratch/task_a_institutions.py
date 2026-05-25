import os
import re

base_dir = r"c:\Projects\SV-Build\portfolio\institutions"

a1_a4 = {
    "changi-airport-lpr-barriers.html": {
        "hero": "/images/portfolio/institutions/changi-airside-hero.webp",
        "mobile": "/images/portfolio/institutions/changi-airside-mobile.webp",
        "og": "https://www.securevision.com.sg/images/portfolio/institutions/changi-airside-hero.webp"
    },
    "das-learning-centre-woodlands.html": {
        "hero": "/images/portfolio/institutions/das-learning-centre-hero.webp",
        "mobile": "/images/portfolio/institutions/das-learning-centre-mobile.webp",
        "og": "https://www.securevision.com.sg/images/portfolio/institutions/das-learning-centre-hero.webp"
    },
    "cpf-maxwell-institution.html": {
        "hero": "/images/portfolio/institutions/cpf-maxwell-hero.webp",
        "mobile": "/images/portfolio/institutions/cpf-maxwell-mobile.webp",
        "og": "https://www.securevision.com.sg/images/portfolio/institutions/cpf-maxwell-hero.webp"
    }
}

a6_a7 = {
    "my-world-preschool-cctv.html": "/images/portfolio/institutions/my-world-preschool-mobile.webp",
    "sfx-retreat-centre-punggol.html": "/images/portfolio/institutions/st-francis-xavier-retreat-centre-mobile.webp"
}

count = 0

for filename, data in a1_a4.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if filename == "cpf-maxwell-institution.html" and '<header class="portfolio-hero">' not in content:
        new_header = f"""<header class="portfolio-hero" style="background-image: linear-gradient(rgba(14,26,43,0.82), rgba(14,26,43,0.82)), url('{data["hero"]}');">
  <div class="container pos-relative z-2">
    <div class="portfolio-kicker">
      <span class="badge badge-primary">Institution Case Study</span>
    </div>
    <h1 class="portfolio-hero-title">CPF Maxwell — Security Infrastructure for a Government Service Centre</h1>
  </div>
</header>"""
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + new_header, content)
    else:
        hero_tag = '<header class="portfolio-hero">'
        new_hero_tag = f'<header class="portfolio-hero" style="background-image: linear-gradient(rgba(14,26,43,0.82), rgba(14,26,43,0.82)), url(\'{data["hero"]}\');">'
        if hero_tag in content:
            content = content.replace(hero_tag, new_hero_tag)

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
    print(f"Updated {filename}")

for filename, mobile_path in a6_a7.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    mobile_css = f"""  <style>
  @media (max-width: 768px) {{
    .portfolio-hero {{
      background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('{mobile_path}') !important;
    }}
  }}
  </style>
"""
    if mobile_path not in content:
        if '</style>' in content:
            mobile_css_inner = f"""  @media (max-width: 768px) {{
    .portfolio-hero {{
      background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('{mobile_path}') !important;
    }}
  }}
"""
            content = content.replace('</style>', mobile_css_inner + '</style>')
        else:
            content = content.replace('</head>', mobile_css + '</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {filename}")

filepath = os.path.join(base_dir, "sengkang-interim-bus-interchange.html")
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

if 'property="og:image"' in content:
    content = re.sub(r'<meta\s+property="og:image"\s+content="[^"]*">\s*', '', content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f"Updated sengkang-interim-bus-interchange.html")

print(f"Task A updated {count} files.")
