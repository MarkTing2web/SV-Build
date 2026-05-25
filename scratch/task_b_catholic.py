import os
import re

filepath = r"c:\Projects\SV-Build\portfolio\institutions\catholic-centre-waterloo.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

if '<header class="portfolio-hero">' in content:
    new_hero = '<header class="portfolio-hero" style="background-image: linear-gradient(rgba(14,26,43,0.82), rgba(14,26,43,0.82)), url(\'/images/portfolio/institutions/catholic-centre-waterloo-hero.webp\');">'
    content = content.replace('<header class="portfolio-hero">', new_hero)

mobile_css = """  @media (max-width: 768px) {
    .portfolio-hero {
      background-image: linear-gradient(rgba(7,13,22,0.82), rgba(7,13,22,0.82)), url('/images/portfolio/institutions/catholic-centre-waterloo-mobile.webp') !important;
    }
  }
"""
if "catholic-centre-waterloo-mobile.webp" not in content:
    if '</style>' in content:
        content = content.replace('</style>', mobile_css + '</style>')
    else:
        full_css = "<style>\n" + mobile_css + "</style>\n"
        content = content.replace('</head>', full_css + '</head>')

og_image = '<meta property="og:image" content="https://www.securevision.com.sg/images/portfolio/institutions/catholic-centre-waterloo-hero.webp">'
if 'property="og:image"' not in content:
    content = re.sub(r'(<meta property="og:url" content="[^"]*">)', r'\1\n  ' + og_image, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated HTML")
