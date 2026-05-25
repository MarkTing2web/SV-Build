import os
import re

filepath = r"c:\Projects\SV-Build\portfolio\commercial\hilton-singapore-orchard-fire-door.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_img(match):
    tag = match.group(0)
    tag = re.sub(r'src=["\'].*?["\']', r'src="/images/portfolio/commercial/hilton-singapore-orchard-hero.webp"', tag)
    if 'alt=' in tag:
        tag = re.sub(r'alt=["\'].*?["\']', r'alt="Hilton Singapore Orchard"', tag)
    else:
        # If no alt attribute exists, add it
        tag = tag.replace('src=', 'alt="Hilton Singapore Orchard" src=')
    return tag

content = re.sub(r'<img[^>]*src=["\']/images/portfolio/hilton-singapore-orchard-stairwell\.webp["\'][^>]*>', replace_img, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Task F replaced the hilton stairwell image.")
