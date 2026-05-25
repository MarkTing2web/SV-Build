import os
import re
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Projects\SV-Build"
img_dir = os.path.join(base_dir, "images", "portfolio", "institutions")

files = [
    "portfolio/institutions/catholic-centre-waterloo.html",
    "portfolio/institutions/changi-airport-lpr-barriers.html",
    "portfolio/institutions/cpf-maxwell-institution.html",
    "portfolio/institutions/das-learning-centre-woodlands.html",
    "portfolio/institutions/my-world-preschool-cctv.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/institutions/sfx-retreat-centre-punggol.html"
]

print("## CHECK 1 — Hero, mobile override and og:image\n")
print("| File | Hero background-image | Mobile @media image | og:image |")
print("|---|---|---|---|")

c2_data = []
c3_data = []
c4_data = []

bad_refs = [
    "prop-institutional.webp",
    "prop-healthcare.webp",
    "sengkang-interim-thumb",
    "sfx-retreat-centre-thumb",
    "fort-st-engineering-thumb",
    "cpf-maxwell-thumb",
    "surya-home-thumb",
    "smartflex-thumb",
    "rezi-3two-thumb",
    "das-hero.webp",
    "das-context.webp",
    "my-world-context.webp",
    "sengkang-hero.webp",
    "sunlove-haig-hero.webp",
    "changi-airport-lpr-hero.webp",
    "scape-hero.webp",
    "pillar_surveillance.webp",
    "pillar_people_access.webp",
    "pillar_vehicle_access.webp"
]

def get_local_path(url_path):
    if url_path.startswith("https://www.securevision.com.sg/"):
        url_path = url_path.replace("https://www.securevision.com.sg/", "/")
    if url_path.startswith("/"):
        return os.path.join(base_dir, url_path.lstrip("/").replace('/', '\\'))
    return None

for rel_path in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    filename = os.path.basename(rel_path)

    # CHECK 1
    hero_match = re.search(r'<header[^>]*portfolio-hero[^>]*style=["\'][^"\'>]*url\([\'"]?([^)\'"]+)[\'"]?\)', content)
    hero_val = hero_match.group(1) if hero_match else "MISSING"
    
    mobile_match = re.search(r'@media\s*\(\s*max-width:\s*768px\s*\).*?background-image[^;]*url\([\'"]?([^)\'"]+)[\'"]?\)', content, flags=re.DOTALL)
    mobile_val = mobile_match.group(1) if mobile_match else "MISSING"
    
    og_match = re.search(r'<meta\s+property="og:image"\s+content="([^"]*)">', content)
    og_val = og_match.group(1) if og_match else "MISSING"
    
    print(f"| {filename} | {hero_val} | {mobile_val} | {og_val} |")

    # CHECK 2
    broken = []
    
    def check_ref(ref_val, ref_type):
        local = get_local_path(ref_val)
        if local and not os.path.exists(local):
            broken.append((ref_val, ref_type))

    for m in re.finditer(r'src=["\']([^"\']+)["\']', content):
        val = m.group(1)
        if val.startswith('/'): check_ref(val, 'src')

    for m in re.finditer(r'url\([\'"]?([^)\'"]+)[\'"]?\)', content):
        val = m.group(1)
        if val.startswith('/') or val.startswith('http'): check_ref(val, 'url()')

    if og_match:
        check_ref(og_match.group(1), 'og:image')

    broken = list(set(broken))
    if not broken:
        c2_data.append(f"✅ {filename} — clean")
    else:
        for ref_val, ref_type in broken:
            c2_data.append(f"| {filename} | {ref_val} | {ref_type} | NO |")

    # CHECK 3
    sys_block = "YES" if '<script src="/systems-block.js"></script>' in content else "NO"
    port_block = "YES" if '<script src="/portfolio-block.js"></script>' in content else "NO"
    nav_foot = "YES" if '<script src="/nav-footer.js"></script>' in content else "NO"

    idx_sys = content.find('<script src="/systems-block.js"></script>')
    idx_port = content.find('<script src="/portfolio-block.js"></script>')
    idx_nav = content.find('<script src="/nav-footer.js"></script>')
    order_correct = "YES" if (-1 < idx_sys < idx_port < idx_nav) else "NO"

    sys_div = "YES" if 'class="sv-systems-block"' in content else "NO"
    port_div = "YES" if 'class="sv-portfolio-block"' in content else "NO"
    
    cat_match = re.search(r'data-category=["\'](.*?)["\']', content)
    cat_correct = "YES" if (cat_match and cat_match.group(1) == "institutions") else "NO"

    c3_data.append(f"| {filename} | {sys_block} | {port_block} | {nav_foot} | {order_correct} | {sys_div} | {port_div} | {cat_correct} |")

    # CHECK 4
    found_refs = []
    for bad in bad_refs:
        if bad == "das-hero.webp":
            matches = list(re.finditer(bad, content))
            for m in matches:
                start = max(0, m.start() - 30)
                context = content[start:m.start()]
                if '/institutions/' not in context:
                    found_refs.append(bad)
                    break
        elif bad == "scape-hero.webp":
            matches = list(re.finditer(bad, content))
            for m in matches:
                start = max(0, m.start() - 30)
                context = content[start:m.start()]
                if '/commercial/' not in context:
                    found_refs.append(bad)
                    break
        else:
            if bad in content:
                found_refs.append(bad)

    if not found_refs:
        c4_data.append(f"| {filename} | CLEAN | |")
    else:
        c4_data.append(f"| {filename} | YES | {', '.join(found_refs)} |")

print("\n## CHECK 2 — Broken image references\n")
has_broken = any("| NO |" in x for x in c2_data)
if has_broken:
    print("| File | Reference value | Type | Exists? |")
    print("|---|---|---|---|")
for row in c2_data:
    print(row)

print("\n## CHECK 3 — Script load order and blocks\n")
print("| File | systems-block.js? | portfolio-block.js? | nav-footer.js? | Correct order? | sv-systems-block present? | sv-portfolio-block present? | data-category correct? |")
print("|---|---|---|---|---|---|---|---|")
for row in c3_data:
    print(row)

print("\n## CHECK 4 — No old broken references remain\n")
print("| File | Any old references found? | Which ones |")
print("|---|---|---|")
for row in c4_data:
    print(row)

print("\n## CHECK 5 — Mobile dimensions\n")
print("| Image filename | Dimensions (W×H) | Correct (1080×1920)? |")
print("|---|---|---|")

for f in os.listdir(img_dir):
    if f.endswith("-mobile.webp"):
        img_path = os.path.join(img_dir, f)
        with Image.open(img_path) as img:
            w, h = img.size
            correct = "YES" if w == 1080 and h == 1920 else "NO"
            print(f"| {f} | {w}×{h} | {correct} |")
