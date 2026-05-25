import os

filepath = r"c:\Projects\SV-Build\portfolio\index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

bad_refs = [
    "prop-industrial.webp",
    "prop-datacentre.webp",
    "prop-healthcare.webp",
    "prop-institution.webp",
    "smartflex-thumb.png",
    "changi-airport-lpr-thumb.png",
    "sfx-retreat-centre-thumb.png",
    "sengkang-interim-thumb.png",
    "surya-home-hero.png",
    "nursing-hostel-thumb.png",
    "scb-dormitory-thumb.webp",
    "sta-inspection-hero.jpg",
    "sta-compliance-hero.jpg",
    "cpf-maxwell-hero.jpg",
    "/images/portfolio/cyrus-tech-hero.webp"
]

found_any = False
for ref in bad_refs:
    if ref in content:
        print(f"[ ] Found bad ref: {ref}")
        found_any = True

if not found_any:
    print("All bad refs removed. Checklist PASS.")
