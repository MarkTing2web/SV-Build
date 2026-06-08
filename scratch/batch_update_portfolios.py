import os
import re

files_list = [
    "portfolio/commercial/altitudex-sentosa-commercial.html",
    "portfolio/commercial/catholic-centre-security-partnership.html",
    "portfolio/commercial/em-services-call-centre-redhill.html",
    "portfolio/commercial/hilton-singapore-orchard-fire-door.html",
    "portfolio/commercial/st-engineering-mobility-cctv.html",
    "portfolio/condominiums/clearwater-access-salto-partnership.html",
    "portfolio/condominiums/clearwater-cctv-upgrade.html",
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/hillview-park-cctv-upgrade.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/mergui-mansions-novena-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html",
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
    "portfolio/industrial/cogent-logistics-hub-cctv.html",
    "portfolio/industrial/cyrus-tech-industrial.html",
    "portfolio/industrial/hoy-san-industrial.html",
    "portfolio/industrial/mitsubishi-elevator-face-access-bms.html",
    "portfolio/industrial/multibase-construction-security-upgrade.html",
    "portfolio/industrial/smartflex-tampines.html",
    "portfolio/industrial/sta-inspection-industrial.html",
    "portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html",
    "portfolio/institutions/catholic-centre-waterloo.html",
    "portfolio/institutions/changi-airport-lpr-barriers.html",
    "portfolio/institutions/cpf-maxwell-institution.html",
    "portfolio/institutions/das-learning-centre-woodlands.html",
    "portfolio/institutions/my-world-preschool-cctv.html",
    "portfolio/institutions/sfx-retreat-centre-punggol.html",
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html",
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"
results = []

for rel_path in sorted(list(set(files_list))):
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"NOT FOUND: {rel_path}")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    filename = os.path.basename(rel_path)
    slug = filename.replace('.html', '')
    
    # 1. Replace header tag & Extract desktop image path
    header_match = re.search(r'<header[^>]*class="[^"]*portfolio-hero[^"]*"[^>]*>', content)
    desktop_img = ""
    if header_match:
        header_tag = header_match.group(0)
        style_match = re.search(r'style="[^"]*url\([\'"]?([^\'"]+)[\'"]?\)[^"]*"', header_tag)
        if style_match:
            desktop_img = style_match.group(1)
            
        new_header_tag = f'<header class="hero hero-compact hero-high-impact hero-{slug}">'
        content = content.replace(header_tag, new_header_tag)

    # 2. Remove hero-image and hero-overlay
    content = re.sub(r'\s*<img[^>]*class="[^"]*hero-image[^"]*"[^>]*>', '', content)
    content = re.sub(r'\s*<div[^>]*class="[^"]*hero-overlay[^"]*"[^>]*>\s*</div>', '', content)

    # 3. Replace <style> block(s) and Extract mobile image path
    mobile_img = ""
    style_blocks = re.findall(r'<style[^>]*>.*?</style>', content, re.DOTALL)
    for block in style_blocks:
        m_match = re.search(r'@media[^{]+{[^}]+url\([\'"]?([^\'"]+)[\'"]?\)', block)
        if m_match:
            mobile_img = m_match.group(1)
            
    if not mobile_img and desktop_img:
        mobile_img = desktop_img.replace('-hero.webp', '-mobile.webp')

    for block in style_blocks:
        content = content.replace(block + '\n', "").replace(block, "")

    new_style_block = f"""<style>
  :root {{ --page-accent: #0056b3; }}
  .hero-{slug} {{ background-image: url('{desktop_img}'); }}
  @media (max-width: 768px) {{
    .hero-{slug} {{ background-image: url('{mobile_img}'); }}
  }}
</style>
"""
    
    content = content.replace('</head>', new_style_block + '</head>')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    results.append((rel_path, f"hero-{slug}", desktop_img, mobile_img))

with open(os.path.join(base_dir, r"scratch\batch_update_report.txt"), "w", encoding="utf-8") as f:
    f.write("File | New header class | Desktop image path in style block | Mobile image path in style block\n")
    f.write("-" * 150 + "\n")
    for r in results:
        f.write(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}\n")
