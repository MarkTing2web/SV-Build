import os
import glob
import re

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

base_dir = r"c:\Projects\SV-Build"
condos_dir = os.path.join(base_dir, "portfolio", "condominiums")

html_files = glob.glob(os.path.join(condos_dir, "*.html"))
html_files.sort()

re_og_image = re.compile(r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']')
re_url = re.compile(r'url\([\'"]?([^\'"\)]+)[\'"]?\)')
re_src_image = re.compile(r'src=["\']([^"\']+)["\']')
re_srcset = re.compile(r'srcset=["\']([^"\']+)["\']')

re_style_tag = re.compile(r'<style[^>]*>(.*?)</style>', re.IGNORECASE | re.DOTALL)
re_hero_tag = re.compile(r'<[^>]*class=["\'][^"\']*\bhero\b[^"\']*["\'][^>]*>', re.IGNORECASE)

old_references = [
    "prop-condo.webp",
    "prop-commercial.webp",
    "portfolio-delias.webp",
    "portfolio-scape.webp",
    "de-elias-hero.webp",
    "trilliant-hero.webp",
    "sentosa-bungalow-hero.webp",
    "sengkang-interim-thumb.webp",
    "surya-home-thumb.webp",
    "smartflex-thumb.webp",
    "pillar_surveillance.webp",
    "pillar_people_access.webp",
    "pillar_vehicle.webp",
    "pillar_vehicle_access.webp",
    "hillview-park-hero.webp",
    "rezi-3two-hero.webp"
]

print("## CHECK 1 - Hero, mobile override and og:image\n")
print("| File | Hero background-image | Mobile @media image | og:image |")
print("|---|---|---|---|")

check2_results = []
check3_results = []

for file in html_files:
    filename = os.path.basename(file)
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # CHECK 1
    og_match = re_og_image.search(content)
    og_image = og_match.group(1) if og_match else "MISSING"

    hero_bg = "MISSING"
    for m in re_hero_tag.finditer(content):
        tag = m.group(0)
        urls = re_url.findall(tag)
        if urls:
            hero_bg = urls[-1] # Usually the last one if linear-gradient is used
            break
            
    mobile_bg = "MISSING"
    for style_match in re_style_tag.finditer(content):
        style_content = style_match.group(1)
        urls = re_url.findall(style_content)
        for u in urls:
            if 'mobile' in u.lower():
                mobile_bg = u
                break
        if mobile_bg != "MISSING":
            break
            
    print(f"| {filename} | {hero_bg} | {mobile_bg} | {og_image} |")

    # CHECK 2
    all_refs = set()
    for m in re_src_image.finditer(content):
        all_refs.add(m.group(1))
    for m in re_srcset.finditer(content):
        parts = m.group(1).split(',')
        for p in parts:
            url = p.strip().split(' ')[0]
            if url:
                all_refs.add(url)
    for m in re_url.finditer(content):
        all_refs.add(m.group(1))
    if og_match:
        all_refs.add(og_image)
        
    broken_refs = []
    for ref in all_refs:
        # ignore pure external links that are not securevision
        if ref.startswith('http') and 'securevision.com.sg' not in ref:
            continue
        if ref.startswith('data:'):
            continue
            
        clean_ref = ref
        if 'securevision.com.sg' in clean_ref:
            # strip domain
            clean_ref = re.sub(r'^https?://(www\.)?securevision\.com\.sg', '', clean_ref)
            
        if clean_ref.startswith('/'):
            path_on_disk = os.path.join(base_dir, clean_ref[1:])
        elif clean_ref.startswith('../'):
            path_on_disk = os.path.normpath(os.path.join(condos_dir, clean_ref))
        else:
            path_on_disk = os.path.normpath(os.path.join(condos_dir, clean_ref))
            
        path_on_disk = path_on_disk.replace('/', '\\').split('?')[0].split('#')[0]
        
        if not os.path.exists(path_on_disk):
            ref_type = 'unknown'
            if ref == og_image:
                ref_type = 'og:image content'
            elif ref == mobile_bg or ref == hero_bg:
                ref_type = 'background-image url()'
            elif f'src="{ref}"' in content or f"src='{ref}'" in content:
                ref_type = 'src'
            elif 'srcset=' in content and ref in content:
                ref_type = 'srcset'
            else:
                ref_type = 'url()'
            
            broken_refs.append((ref, ref_type))
            
    check2_results.append((filename, broken_refs))
    
    # CHECK 3
    found_old_refs = []
    for old_ref in old_references:
        if old_ref in content:
            found_old_refs.append(old_ref)
    check3_results.append((filename, found_old_refs))

print("\n## CHECK 2 - Broken image references\n")
print("| File | Reference value | Type | Exists? |")
print("|---|---|---|---|")
for filename, broken_refs in check2_results:
    if not broken_refs:
        print(f"| {filename} | clean | - | - |")
    else:
        for ref, ref_type in broken_refs:
            print(f"| {filename} | `{ref}` | {ref_type} | No |")

print("\n## CHECK 3 - Old broken references gone\n")
print("| File | Any old references found? | Which ones |")
print("|---|---|---|")
for filename, found_old_refs in check3_results:
    if not found_old_refs:
        print(f"| {filename} | CLEAN | None |")
    else:
        print(f"| {filename} | YES | {', '.join(found_old_refs)} |")

print("\n## CHECK 4 - Mobile dimensions\n")
print("| Image filename | Dimensions (W×H) | Correct (1080×1920)? |")
print("|---|---|---|")

images_condo_dir = os.path.join(base_dir, "images", "portfolio", "condominiums")
mobile_images = glob.glob(os.path.join(images_condo_dir, "*-mobile.webp"))
mobile_images.sort()

if not HAS_PIL:
    print("PIL not installed, cannot read image dimensions.")
else:
    for img_path in mobile_images:
        filename = os.path.basename(img_path)
        try:
            with Image.open(img_path) as img:
                w, h = img.size
                correct = "Yes" if (w == 1080 and h == 1920) else "No"
                print(f"| {filename} | {w}x{h} | {correct} |")
        except Exception as e:
            print(f"| {filename} | ERROR | {str(e)} |")
