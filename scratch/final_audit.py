import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Projects\SV-Build"

residential_files = [
    "portfolio/residential/shelford-landed-home.html",
    "portfolio/residential/siglap-bank-landed-home.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html",
    "portfolio/residential/dunbar-walk-landed-home.html",
    "portfolio/residential/dyson-8-residences-landed-home.html",
    "portfolio/residential/lengkok-mariam-landed-home.html",
    "portfolio/residential/merryn-road-landed-home.html"
]

condo_files = [
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
    "portfolio/condominiums/village-pasir-panjang-condo.html"
]

all_23 = residential_files + condo_files

def check_exists(path):
    if not path.startswith('/'):
        return True # Skip external or relative not starting with /
    # strip query params or fragments
    path = path.split('?')[0].split('#')[0]
    filepath = os.path.join(base_dir, path.lstrip('/\\').replace('/', '\\'))
    return os.path.exists(filepath)

def extract_path_from_og(url):
    if 'securevision.com.sg' in url:
        return url.split('securevision.com.sg')[-1]
    return url

# PART 1 & 5
print("## PART 1 — BROKEN LINK CHECK\n")
print("| File | Reference value | Type | Exists? |")
print("|---|---|---|---|")

part5_data = {f: [] for f in all_23}
part1_clean = {f: True for f in all_23}

for f in all_23:
    filepath = os.path.join(base_dir, f.replace('/', '\\'))
    if not os.path.exists(filepath):
        print(f"File missing: {f}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        content = file_obj.read()
        
    # find hrefs
    hrefs = re.findall(r'href=["\'](.*?)["\']', content)
    for h in hrefs:
        if h.startswith('/'):
            if h.endswith('.html') or '.html#' in h or '.html?' in h:
                part5_data[f].append(h)
            if not check_exists(h):
                print(f"| {os.path.basename(f)} | {h} | href | NO |")
                part1_clean[f] = False

    # find srcs
    srcs = re.findall(r'src=["\'](.*?)["\']', content)
    for s in srcs:
        if s.startswith('/') and not check_exists(s):
            print(f"| {os.path.basename(f)} | {s} | src | NO |")
            part1_clean[f] = False
            
    # find background-image url
    bg_urls = re.findall(r'background-image:[^;]*url\([\'"]?(.*?)[\'"]?\)', content)
    for u in bg_urls:
        if u.startswith('/') and not check_exists(u):
            print(f"| {os.path.basename(f)} | {u} | background-image | NO |")
            part1_clean[f] = False

    # find og:image
    og_imgs = re.findall(r'<meta property="og:image" content=["\'](.*?)["\']', content)
    for og in og_imgs:
        path = extract_path_from_og(og)
        if path.startswith('/') and not check_exists(path):
            print(f"| {os.path.basename(f)} | {og} | og:image | NO |")
            part1_clean[f] = False

for f in all_23:
    if part1_clean[f]:
        print(f"✅ {os.path.basename(f)} — clean")


print("\n## PART 2 — HERO / MOBILE / OG:IMAGE CHECK\n")
print("| File | Hero image exists? | Mobile image exists? | og:image exists? |")
print("|---|---|---|---|")

for f in all_23:
    filepath = os.path.join(base_dir, f.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        content = file_obj.read()
        
    # hero: look for <header class="portfolio-hero" ... style="...url('...')"
    hero_m = re.search(r'<header[^>]*portfolio-hero[^>]*url\([\'"]?(.*?)[\'"]?\)', content)
    hero_status = "MISSING"
    if hero_m:
        h_url = hero_m.group(1)
        hero_status = "YES" if check_exists(h_url) else f"NO ({h_url})"

    # mobile: @media (max-width: 768px) ... .portfolio-hero ... url('...')
    mobile_m = re.search(r'@media\s*\(\s*max-width:\s*768px\s*\).*?\.portfolio-hero[^}]*url\([\'"]?(.*?)[\'"]?\)', content, re.DOTALL)
    mobile_status = "MISSING"
    if mobile_m:
        m_url = mobile_m.group(1)
        mobile_status = "YES" if check_exists(m_url) else f"NO ({m_url})"

    # og:image
    og_m = re.search(r'<meta property="og:image" content=["\'](.*?)["\']', content)
    og_status = "MISSING"
    if og_m:
        og_url = og_m.group(1)
        og_path = extract_path_from_og(og_url)
        og_status = "YES" if check_exists(og_path) else f"NO ({og_url})"
        
    print(f"| {os.path.basename(f)} | {hero_status} | {mobile_status} | {og_status} |")


print("\n## PART 3 — RELATED CASE STUDIES IMAGE CHECK\n")
print("| File | Related card image src | Exists? |")
print("|---|---|---|")

for f in all_23:
    filepath = os.path.join(base_dir, f.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        content = file_obj.read()
        
    clean = True
    parts = content.split('<a href')
    for part in parts:
        if 'related-project' in part:
            img_m = re.search(r'<img[^>]*src=["\'](.*?)["\']', part)
            if img_m:
                src = img_m.group(1)
                if not check_exists(src):
                    print(f"| {os.path.basename(f)} | {src} | NO |")
                    clean = False
    
    if clean:
        print(f"✅ {os.path.basename(f)} — all related images clean")


print("\n## PART 4 — PORTFOLIO INDEX CONDO AND RESIDENTIAL CARDS\n")
print("| Card href | img src | Image exists on disk? |")
print("|---|---|---|")

index_path = os.path.join(base_dir, r"portfolio\index.html")
with open(index_path, 'r', encoding='utf-8') as file_obj:
    idx_content = file_obj.read()

parts = idx_content.split('<a href')
for part in parts:
    if 'class="project-card"' in part:
        href_m = re.match(r'\s*=["\'](.*?)["\']', part)
        if href_m:
            href = href_m.group(1)
            if '/condominiums/' in href or '/residential/' in href:
                img_m = re.search(r'<img[^>]*src=["\'](.*?)["\']', part)
                if img_m:
                    src = img_m.group(1)
                    if not check_exists(src):
                        print(f"| {href} | {src} | NO |")

print("\n## PART 5 — INTERNAL HREF LINK CHECK\n")
print("| File | href value | Page exists? |")
print("|---|---|---|")

for f in all_23:
    broken = False
    for h in part5_data[f]:
        if not check_exists(h):
            print(f"| {os.path.basename(f)} | {h} | NO |")
            broken = True
    if not broken:
        print(f"✅ {os.path.basename(f)} — all links clean")
