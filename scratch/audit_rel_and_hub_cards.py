import os
import re
from bs4 import BeautifulSoup

repo_root = r"c:\Projects\SV-Build"

rel_files = [
    "commercial-security-systems-hero-rel.webp",
    "condominium-security-systems-hero-rel.webp",
    "solution-condominiums-managing-agents-hero-rel.webp",
    "solution-condominiums-mcst-hero-rel.webp",
    "solution-condominiums-security-contractors-hero-rel.webp",
    "data-centre-security-systems-hero-rel.webp",
    "solution-healthcare-daycare-hero-rel.webp",
    "healthcare-security-systems-hero-rel.webp",
    "industrial-security-systems-hero-rel.webp",
    "solution-industrial-logistics-hero-rel.webp",
    "solution-industrial-manufacturing-hero-rel.webp",
    "solution-industrial-tech-park-hero-rel.webp",
    "solution-institutions-community-hero-rel.webp",
    "solution-institutions-govt-office-hero-rel.webp",
    "institutions-security-systems-hero-rel.webp",
    "solution-institutions-schools-hero-rel.webp",
    "solution-managed-living-co-living-hero-rel.webp",
    "managed-living-security-systems-hero-rel.webp"
]

subsector_pages = [
    "solutions/commercial/commercial-security-systems.html",
    "solutions/condominiums/condominium-security-systems.html",
    "solutions/condominiums/managing-agents.html",
    "solutions/condominiums/mcst.html",
    "solutions/condominiums/security-contractors.html",
    "solutions/data-centres/data-centre-security-systems.html",
    "solutions/healthcare/day-care.html",
    "solutions/healthcare/healthcare-security-systems.html",
    "solutions/industrial/industrial-security-systems.html",
    "solutions/industrial/logistics.html",
    "solutions/industrial/manufacturing.html",
    "solutions/industrial/tech-park.html",
    "solutions/institutions/community.html",
    "solutions/institutions/govt-office.html",
    "solutions/institutions/institutions-security-systems.html",
    "solutions/institutions/schools.html",
    "solutions/managed-living/co-living.html",
    "solutions/managed-living/managed-living-security-systems.html"
]

hub_pages = [
    "solutions/index.html",
    "solutions/commercial.html",
    "solutions/condominiums.html",
    "solutions/data-centres.html",
    "solutions/healthcare.html",
    "solutions/industrial.html",
    "solutions/institutions.html",
    "solutions/managed-living.html"
]

# Step 1: Scan all HTML files for -rel image filenames
exclude_dirs = {'.git', '.vercel', 'scratch', 'node_modules', 'artifacts', '.github'}
html_files = []
for root, dirs, files in os.walk(repo_root):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

html_files.sort()

# Read all file contents
file_contents = {}
for hf in html_files:
    try:
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            file_contents[hf] = f.read()
    except Exception:
        pass

rel_references = {fn: [] for fn in rel_files}
for fn in rel_files:
    for hf, content in file_contents.items():
        if fn in content:
            rel_hf = os.path.relpath(hf, repo_root).replace('\\', '/')
            rel_references[fn].append(rel_hf)

# Step 2: Audit hub page card images
css_url_pattern = re.compile(r'url\(\s*[\'"]?([^\'")\s]+)[\'"]?\s*\)', re.IGNORECASE)

print("PART 1 — -rel reference check:")
referenced_rel_count = 0
not_referenced_rel_count = 0

for fn in rel_files:
    refs = rel_references[fn]
    if refs:
        print(f"  {fn} — REFERENCED IN: {', '.join(refs)}")
        referenced_rel_count += 1
    else:
        print(f"  {fn} — NOT REFERENCED in any file")
        not_referenced_rel_count += 1

print("\nPART 2 — Hub page card images:")
cards_with_missing_images = 0

# Normalise subsector links for matching
subsector_normalized = {}
for page in subsector_pages:
    subsector_normalized[f"/{page}"] = page
    subsector_normalized[page] = page
    # also strip leading solutions/
    if page.startswith("solutions/"):
        short = page[10:]
        subsector_normalized[short] = page
        subsector_normalized[f"/{short}"] = page
        subsector_normalized[f"/solutions/{short}"] = page

for hub in hub_pages:
    hub_path = os.path.join(repo_root, hub)
    if not os.path.exists(hub_path):
        print(f"  Hub file not found: {hub}")
        continue
        
    with open(hub_path, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Find all anchor tags
    for a in soup.find_all('a'):
        href = a.get('href', '').split('?')[0].split('#')[0].strip()
        if href in subsector_normalized:
            target_subsector = subsector_normalized[href]
            
            # Find the card image associated with this link
            card_img = None
            
            # Traverse parents to find a card image or background image
            curr = a
            card_container = None
            for _ in range(5):
                if curr.name in ('div', 'a') and any(cls in (curr.get('class') or []) for cls in ('card', 'rel-card', 'item', 'card-clickable')):
                    card_container = curr
                    break
                curr = curr.parent
                if not curr:
                    break
                    
            if card_container:
                # Check for img tag inside card_container
                imgs = card_container.find_all('img')
                if imgs:
                    card_img = imgs[0].get('src')
                else:
                    # Check for background image in style
                    style = card_container.get('style', '')
                    style_matches = css_url_pattern.findall(style)
                    if style_matches:
                        card_img = style_matches[0]
            else:
                # Fallback: check if the 'a' tag itself contains an image
                imgs = a.find_all('img')
                if imgs:
                    card_img = imgs[0].get('src')
                else:
                    # check style of 'a' tag itself
                    style = a.get('style', '')
                    style_matches = css_url_pattern.findall(style)
                    if style_matches:
                        card_img = style_matches[0]
            
            # If still none, check next siblings or parents' siblings
            if not card_img:
                card_img = "NOT FOUND"
                
            # Verify if file exists on disk
            missing_flag = ""
            if card_img and card_img != "NOT FOUND":
                # Resolve path
                img_path = card_img.split('?')[0].split('#')[0].strip().strip("'\"")
                if img_path.startswith('/'):
                    disk_path = os.path.join(repo_root, img_path.lstrip('/'))
                else:
                    disk_path = os.path.normpath(os.path.join(os.path.dirname(hub_path), img_path))
                    
                if not os.path.isfile(disk_path):
                    missing_flag = " [MISSING FROM DISK]"
                    cards_with_missing_images += 1
            else:
                missing_flag = " [NO IMAGE FOUND]"
                cards_with_missing_images += 1
                
            print(f"  {hub} -> {target_subsector} -> {card_img}{missing_flag}")

print("\nSummary:")
print(f"  -rel files referenced: {referenced_rel_count} of 18")
print(f"  -rel files not referenced: {not_referenced_rel_count} of 18")
print(f"  Cards with missing images: {cards_with_missing_images}")
