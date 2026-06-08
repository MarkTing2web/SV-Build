import os
import re

changes = {
    "portfolio/condominiums/rezi-3two-condo.html": {
        "og_title": "Rezi 3Two Condominium — Security Case Study | Securevision Singapore"
    },
    "portfolio/institutions/my-world-preschool-cctv.html": {
        "og_title": "MY World Preschool — Child Safety CCTV & Surveillance | Securevision"
    },
    "portfolio/commercial/scape-commercial.html": {
        "og_desc": "Securevision deployed 209 AI cameras and face recognition access control at SCAPE Orchard Road — with Salesforce integration — cutting incident response time by 87%. Completed December 2024."
    },
    "portfolio/healthcare/surya-home.html": {
        "og_desc": "Securevision delivered the CCTV, MicroEngine door access, lift control, and central UPS for the rebuilt Surya Home — a residential care facility supporting adults with intellectual disability.",
        "og_image": "https://www.securevision.com.sg/images/portfolio/healthcare/surya-home-hero.webp"
    },
    "portfolio/industrial/hoy-san-industrial.html": {
        "og_desc": "Operational case study on automating vehicle access at Hoy San Group using smart plate recognition and LiDAR safety detection at 5 Penjuru Lane."
    },
    "portfolio/industrial/smartflex-tampines.html": {
        "og_desc": "Securevision delivered the full security relocation for Smartflex — full IP CCTV upgrade, expanded card access on MicroEngine, and reinstalled DSC PowerSeries alarm moving from Ubi to Tampines."
    },
    "portfolio/residential/upper-east-coast-road-landed-home.html": {
        "og_desc": "A decade-long security partnership with a private landed home at Upper East Coast Road — covering IP CCTV, keyphone, and two generations of motorised gate automation."
    },
    "portfolio/industrial/sta-compliance-imaging.html": {
        "og_image": "https://www.securevision.com.sg/images/portfolio/industrial/sta-compliance-imaging-hero.webp"
    },
    "portfolio/institutions/sengkang-interim-bus-interchange.html": {
        "og_image": "https://www.securevision.com.sg/images/portfolio/institutions/sengkang-interim-bus-interchange-hero.webp"
    },
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html": {
        "og_image": "https://www.securevision.com.sg/images/portfolio/managed-living/scb-worker-dormitory-jalan-papan-hero.webp"
    }
}

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

print("File | og:title matches title | og:description matches description | og:image present")
print("---|---|---|---")

for fpath, rules in changes.items():
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        print(f"{fpath} | NOT FOUND | NOT FOUND | NOT FOUND")
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content

    if "og_title" in rules:
        val = rules["og_title"]
        pattern = re.compile(r'(<meta[^>]*property=["\']og:title["\'][^>]*content=["\'])([^"\']*)(["\'])', re.IGNORECASE)
        if pattern.search(new_content):
            new_content = pattern.sub(r'\g<1>' + val + r'\g<3>', new_content)
        else:
            pattern2 = re.compile(r'(<meta[^>]*content=["\'])([^"\']*)(["\'][^>]*property=["\']og:title["\'])', re.IGNORECASE)
            if pattern2.search(new_content):
                new_content = pattern2.sub(r'\g<1>' + val + r'\g<3>', new_content)

    if "og_desc" in rules:
        val = rules["og_desc"]
        pattern = re.compile(r'(<meta[^>]*property=["\']og:description["\'][^>]*content=["\'])([^"\']*)(["\'])', re.IGNORECASE)
        if pattern.search(new_content):
            new_content = pattern.sub(r'\g<1>' + val + r'\g<3>', new_content)
        else:
            pattern2 = re.compile(r'(<meta[^>]*content=["\'])([^"\']*)(["\'][^>]*property=["\']og:description["\'])', re.IGNORECASE)
            if pattern2.search(new_content):
                new_content = pattern2.sub(r'\g<1>' + val + r'\g<3>', new_content)

    if "og_image" in rules:
        val = rules["og_image"]
        pattern = re.compile(r'<meta[^>]*property=["\']og:image["\'][^>]*>', re.IGNORECASE)
        if not pattern.search(new_content):
            pattern2 = re.compile(r'<meta[^>]*content=["\'][^"\']*["\'][^>]*property=["\']og:image["\']', re.IGNORECASE)
            if not pattern2.search(new_content):
                # insert after og:description
                desc_pattern = re.compile(r'(<meta[^>]*property=["\']og:description["\'][^>]*>|<meta[^>]*content=["\'][^"\']*["\'][^>]*property=["\']og:description["\']>)', re.IGNORECASE)
                insert_str = f'\n  <meta property="og:image" content="{val}">'
                new_content = desc_pattern.sub(r'\g<1>' + insert_str, new_content)
        else:
            # Set content if already exists
            new_content = re.sub(
                r'(<meta[^>]*property=["\']og:image["\'][^>]*content=["\'])([^"\']*)(["\'])',
                r'\g<1>' + val + r'\g<3>',
                new_content, flags=re.IGNORECASE
            )

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    # Verification
    # 1. title
    title_match = re.search(r'<title>(.*?)</title>', new_content, re.IGNORECASE | re.DOTALL)
    title_val = title_match.group(1).strip() if title_match else ""

    # 2. desc
    desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', new_content, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', new_content, re.IGNORECASE)
    desc_val = desc_match.group(1).strip() if desc_match else ""

    # 3. og_title
    og_title_match = re.search(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\']([^"\']*)["\']', new_content, re.IGNORECASE)
    if not og_title_match:
        og_title_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*property=["\']og:title["\']', new_content, re.IGNORECASE)
    og_title_val = og_title_match.group(1).strip() if og_title_match else ""

    # 4. og_desc
    og_desc_match = re.search(r'<meta[^>]*property=["\']og:description["\'][^>]*content=["\']([^"\']*)["\']', new_content, re.IGNORECASE)
    if not og_desc_match:
        og_desc_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*property=["\']og:description["\']', new_content, re.IGNORECASE)
    og_desc_val = og_desc_match.group(1).strip() if og_desc_match else ""

    # 5. og_image
    og_image_match = re.search(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\']([^"\']*)["\']', new_content, re.IGNORECASE)
    if not og_image_match:
        og_image_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*property=["\']og:image["\']', new_content, re.IGNORECASE)
    og_image_present = bool(og_image_match)

    match_title = title_val == og_title_val
    match_desc = desc_val == og_desc_val

    t_str = "Yes" if match_title else "No [FLAG]"
    d_str = "Yes" if match_desc else "No [FLAG]"
    i_str = "Yes" if og_image_present else "No [FLAG]"

    print(f"{fpath} | {t_str} | {d_str} | {i_str}")
