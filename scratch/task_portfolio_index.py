import os
import re

filepath = r"c:\Projects\SV-Build\portfolio\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ("/portfolio/industrial/mitsubishi-elevator-face-access-bms.html", "/images/prop-industrial.webp", "/images/portfolio/industrial/mitsubishi-elevator-singapore-rel.webp"),
    ("/portfolio/industrial/cogent-logistics-hub-cctv.html", "/images/prop-industrial.webp", "/images/portfolio/industrial/cogent-1-logistics-hub-rel.webp"),
    ("/portfolio/industrial/smartflex-tampines.html", "/images/portfolio/smartflex-thumb.png", "/images/portfolio/industrial/smartflex-at-tampines-rel.webp"),
    ("/portfolio/industrial/sta-inspection-industrial.html", "/images/portfolio/sta-inspection-hero.jpg", "/images/portfolio/industrial/sta-inspection-centre-sin-ming-rel.webp"),
    ("/portfolio/industrial/cyrus-tech-industrial.html", "/images/portfolio/cyrus-tech-hero.webp", "/images/portfolio/industrial/cyrus-tech-at-loyang-rel.webp"),
    ("/portfolio/industrial/sta-compliance-imaging.html", "/images/portfolio/sta-compliance-hero.jpg", "/images/portfolio/industrial/sta-inspection-centre-sin-ming-rel.webp"),
    ("/portfolio/industrial/multibase-construction-security-upgrade.html", "/images/prop-industrial.webp", "/images/portfolio/industrial/multibase-construction-rel.webp"),
    ("/portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html", "/images/prop-industrial.webp", "/images/portfolio/industrial/st-microelectronics-loyang-rel.webp"),
    
    ("/portfolio/institutions/changi-airport-lpr-barriers.html", "/images/portfolio/changi-airport-lpr-thumb.png", "/images/portfolio/institutions/changi-airside-rel.webp"),
    ("/portfolio/institutions/sfx-retreat-centre-punggol.html", "/images/portfolio/sfx-retreat-centre-thumb.png", "/images/portfolio/institutions/st-francis-xavier-retreat-centre-rel.webp"),
    ("/portfolio/institutions/sengkang-interim-bus-interchange.html", "/images/portfolio/sengkang-interim-thumb.png", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
    ("/portfolio/institutions/cpf-maxwell-institution.html", "/images/portfolio/cpf-maxwell-hero.jpg", "/images/portfolio/institutions/cpf-maxwell-rel.webp"),
    ("/portfolio/institutions/my-world-preschool-cctv.html", "/images/prop-institution.webp", "/images/portfolio/institutions/my-world-preschool-rel.webp"),
    ("/portfolio/institutions/das-learning-centre-woodlands.html", "/images/prop-institution.webp", "/images/portfolio/institutions/das-learning-centre-rel.webp"),
    
    ("/portfolio/healthcare/surya-home.html", "/images/portfolio/surya-home-hero.png", "/images/portfolio/healthcare/sunlove-rel.webp"),
    ("/portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html", "/images/prop-healthcare.webp", "/images/portfolio/healthcare/sunlove-rel.webp"),
    
    ("/portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html", "/images/portfolio/nursing-hostel-thumb.png", "/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-rel.webp"),
    ("/portfolio/managed-living/scb-worker-dormitory-jalan-papan.html", "/images/portfolio/scb-dormitory-thumb.webp", "/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-rel.webp"),
    
    ("/portfolio/data-centres/fort-data-centre-access-upgrade.html", "/images/prop-datacentre.webp", "/images/portfolio/data-centres/fort-data-centre-rel.webp"),
    ("/portfolio/data-centres/fort-data-centre-access-upgrade.html", "/images/prop-industrial.webp", "/images/portfolio/data-centres/fort-data-centre-rel.webp")
]

for href, old_src, new_src in replacements:
    pattern = r'(href=["\']' + re.escape(href) + r'["\'][^>]*>(?:(?!</a>).)*?<img[^>]*src=["\'])' + re.escape(old_src) + r'(["\'])'
    def replace_src(match):
        return match.group(1) + new_src + match.group(2)
        
    content, num_subs = re.subn(pattern, replace_src, content, flags=re.DOTALL)
    print(f"Replaced {num_subs} instance(s) of {old_src} for {href}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done replacing.")
