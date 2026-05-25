import os
import re

filepath = r"c:\Projects\SV-Build\portfolio\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        r'(href=["\']/portfolio/commercial/st-engineering-mobility-cctv\.html["\'][^>]*>.*?<img[^>]*src=["\'])/images/prop-commercial\.webp(["\'])',
        r'\g<1>/images/portfolio/commercial/st-engineering-mobility-rel.webp\g<2>'
    ),
    (
        r'(href=["\']/portfolio/commercial/catholic-centre-security-partnership\.html["\'][^>]*>.*?<img[^>]*src=["\'])/images/prop-commercial\.webp(["\'])',
        r'\g<1>/images/portfolio/commercial/catholic-centre-rel.webp\g<2>'
    ),
    (
        r'(href=["\']/portfolio/commercial/em-services-call-centre-redhill\.html["\'][^>]*>.*?<img[^>]*src=["\'])/images/prop-commercial\.webp(["\'])',
        r'\g<1>/images/portfolio/commercial/em-engineering-at-jalan-kilang-rel.webp\g<2>'
    ),
    (
        r'(href=["\']/portfolio/industrial/cogent-logistics-hub-cctv\.html["\'][^>]*>.*?<img[^>]*src=["\'])/images/prop-commercial\.webp(["\'])',
        r'\g<1>/images/portfolio/industrial/cogent-1-logistics-hub-rel.webp\g<2>'
    ),
    (
        r'(href=["\']/portfolio/commercial/scape-commercial\.html["\'][^>]*>.*?<img[^>]*src=["\'])/images/portfolio/portfolio-scape\.webp(["\'])',
        r'\g<1>/images/portfolio/commercial/scape-rel.webp\g<2>'
    ),
    (
        r'(href=["\']/portfolio/commercial/altitudex-sentosa-commercial\.html["\'][^>]*>.*?<img[^>]*src=["\'])/images/portfolio/altitudex-hero\.webp(["\'])',
        r'\g<1>/images/portfolio/commercial/altitudex-sentosa-rel.webp\g<2>'
    ),
    (
        r'(href=["\']/portfolio/commercial/hilton-singapore-orchard-fire-door\.html["\'][^>]*>.*?<img[^>]*src=["\'])/images/portfolio/hilton-singapore-orchard-hero\.webp(["\'])',
        r'\g<1>/images/portfolio/commercial/hilton-singapore-orchard-rel.webp\g<2>'
    )
]

for pat, repl in replacements:
    content, count = re.subn(pat, repl, content, flags=re.DOTALL)
    print(f"Replaced {count} occurrences for pattern")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

prop_comm = len(re.findall(r'prop-commercial\.webp', content))
scape = len(re.findall(r'portfolio-scape\.webp', content))
altitudex = len(re.findall(r'altitudex-hero\.webp', content))
hilton = len(re.findall(r'hilton-singapore-orchard-hero\.webp', content))

print(f"Remaining prop-commercial.webp: {prop_comm}")
print(f"Remaining portfolio-scape.webp: {scape}")
print(f"Remaining altitudex-hero.webp: {altitudex}")
print(f"Remaining hilton-singapore-orchard-hero.webp: {hilton}")
