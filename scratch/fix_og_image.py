import os
import re

filepath = r"c:\Projects\SV-Build\portfolio\data-centres\fort-data-centre-access-upgrade.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

og_image = '<meta property="og:image" content="https://www.securevision.com.sg/images/portfolio/data-centres/fort-data-centre-hero.webp">'
if 'property="og:image"' not in content:
    content = re.sub(r'(<meta property="og:description" content="[^"]*">)', r'\1\n  ' + og_image, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed og:image")
