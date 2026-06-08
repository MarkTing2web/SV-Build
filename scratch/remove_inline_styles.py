import os
import re

files = [
    "portfolio/commercial/catholic-centre-security-partnership.html",
    "portfolio/commercial/st-engineering-mobility-cctv.html",
    "portfolio/condominiums/clearwater-access-salto-partnership.html",
    "portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
    "portfolio/condominiums/d-elias-pasir-ris-condo.html",
    "portfolio/condominiums/high-oak-condominium-cctv.html",
    "portfolio/condominiums/idyllic-suites-geylang-condo.html",
    "portfolio/condominiums/light-cairnhill-condo.html",
    "portfolio/condominiums/mergui-mansions-novena-condo.html",
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/the-bale-intercom-cctv.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/industrial/cogent-logistics-hub-cctv.html",
    "portfolio/industrial/cyrus-tech-industrial.html",
    "portfolio/industrial/hoy-san-industrial.html",
    "portfolio/industrial/smartflex-tampines.html",
    "portfolio/industrial/sta-compliance-imaging.html",
    "portfolio/industrial/sta-inspection-industrial.html",
    "portfolio/institutions/cpf-maxwell-institution.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html",
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

print("File | SVG styles removed | grid-column styles removed | Other styles removed | Remaining style= count")
print("---|---|---|---|---")

svg_removed = 0
grid_removed = 0
other_removed = 0
remaining_count = 0

def repl(m):
    global svg_removed, grid_removed, other_removed
    full_tag = m.group(0)
    tag_name = m.group(2).lower()
    style_quote = m.group(3)
    style_content = m.group(4)
    style_attr = f'style={style_quote}{style_content}{style_quote}'
    
    if tag_name == "header" and "class=" in full_tag and "hero" in full_tag:
        return full_tag
    if "background-image" in style_content:
        return full_tag
    if "stat-bar-fill" in full_tag and re.search(r'width:\s*\d+%', style_content):
        return full_tag

    new_tag = re.sub(r'\s*style=[\'"]' + re.escape(style_content) + r'[\'"]', "", full_tag)

    compact_style = style_content.replace(" ", "")
    is_svg_style = compact_style == "width:14px;height:14px;display:inline-block;vertical-align:middle;margin-right:4px;"

    if tag_name == "svg" and is_svg_style:
        svg_removed += 1
        return new_tag
    elif "grid-column: span" in style_content or "grid-column:span" in style_content:
        grid_removed += 1
        return new_tag
    else:
        other_removed += 1
        return new_tag

def repl_remain(m):
    global remaining_count
    full_tag = m.group(0)
    tag_name = m.group(2).lower()
    style_content = m.group(4)
    
    is_allowed = False
    if tag_name == "header" and "class=" in full_tag and "hero" in full_tag:
        is_allowed = True
    if "background-image" in style_content:
        is_allowed = True
    if "stat-bar-fill" in full_tag and re.search(r'width:\s*\d+%', style_content):
        is_allowed = True
        
    if not is_allowed:
        remaining_count += 1
        
    return full_tag

for fpath in files:
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    body_split = content.split("<body", 1)
    if len(body_split) < 2:
        continue
    head_content = body_split[0]
    body_content = "<body" + body_split[1]

    svg_removed = 0
    grid_removed = 0
    other_removed = 0
    remaining_count = 0

    pattern = re.compile(r'(<(\w+)[^>]*?\bstyle=([\'"])(.*?)\3[^>]*?>)', re.IGNORECASE | re.DOTALL)
    
    new_body_content = pattern.sub(repl, body_content)
    pattern.sub(repl_remain, new_body_content)

    new_content = head_content + new_body_content

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    flag = " 🚩" if remaining_count > 0 else ""
    print(f"{fpath} | {svg_removed} | {grid_removed} | {other_removed} | {remaining_count}{flag}")
