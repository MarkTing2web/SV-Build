import os
import re

files = [
    "portfolio/condominiums/rezi-3two-condo.html",
    "portfolio/institutions/my-world-preschool-cctv.html",
    "portfolio/commercial/scape-commercial.html",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/industrial/hoy-san-industrial.html",
    "portfolio/industrial/smartflex-tampines.html",
    "portfolio/residential/upper-east-coast-road-landed-home.html",
    "portfolio/industrial/sta-compliance-imaging.html",
    "portfolio/institutions/sengkang-interim-bus-interchange.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html"
]

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

for fpath in files:
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        print(f"### {fpath}")
        print("FILE NOT FOUND\n")
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title_val = title_match.group(1).strip() if title_match else "NOT FOUND"

    # 2. meta description
    desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', content, re.IGNORECASE)
    desc_val = desc_match.group(1).strip() if desc_match else "NOT FOUND"

    # 3. og:title
    og_title_match = re.search(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
    if not og_title_match:
        og_title_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*property=["\']og:title["\']', content, re.IGNORECASE)
    og_title_val = og_title_match.group(1).strip() if og_title_match else "NOT FOUND"

    # 4. og:description
    og_desc_match = re.search(r'<meta[^>]*property=["\']og:description["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
    if not og_desc_match:
        og_desc_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*property=["\']og:description["\']', content, re.IGNORECASE)
    og_desc_val = og_desc_match.group(1).strip() if og_desc_match else "NOT FOUND"

    # 5. og:image
    og_image_match = re.search(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\']([^"\']*)["\']', content, re.IGNORECASE)
    if not og_image_match:
        og_image_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*property=["\']og:image["\']', content, re.IGNORECASE)
    og_image_val = og_image_match.group(1).strip() if og_image_match else "NOT FOUND"

    print(f"### {fpath}")
    print(f"1. <title>                 : {title_val}")
    print(f"2. <meta name=\"description\"> : {desc_val}")
    print(f"3. <meta property=\"og:title\"> : {og_title_val}")
    print(f"4. <meta property=\"og:description\"> : {og_desc_val}")
    print(f"5. <meta property=\"og:image\"> : {og_image_val}")
    print()
