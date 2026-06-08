import os
import re

changes = {
    "portfolio/industrial/hoy-san-industrial.html": "Operational case study on automating vehicle access at Hoy San Group using smart plate recognition and LiDAR safety detection at 5 Penjuru Lane.",
    "portfolio/industrial/smartflex-tampines.html": "Securevision delivered the full security relocation for Smartflex — full IP CCTV upgrade, expanded card access on MicroEngine, and reinstalled DSC PowerSeries alarm moving from Ubi to Tampines.",
    "portfolio/institutions/sengkang-interim-bus-interchange.html": "Design-and-build CCTV system for the LTA Sengkang Interim Bus Interchange — 53 IP cameras, 5 NVRs, 28-day retention, delivered under W"
}

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

print("File | meta description | og:description | Match")
print("---|---|---|---")

for fpath, new_desc in changes.items():
    full_path = os.path.join(base_dir, fpath)
    if not os.path.exists(full_path):
        print(f"{fpath} | NOT FOUND | NOT FOUND | No 🚩")
        continue

    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content
    pattern = re.compile(r'(<meta[^>]*name=["\']description["\'][^>]*content=["\'])([^"\']*?)(["\'])', re.IGNORECASE)
    if pattern.search(new_content):
        new_content = pattern.sub(r'\g<1>' + new_desc + r'\g<3>', new_content)
    else:
        pattern2 = re.compile(r'(<meta[^>]*content=["\'])([^"\']*?)(["\'][^>]*name=["\']description["\'])', re.IGNORECASE)
        if pattern2.search(new_content):
            new_content = pattern2.sub(r'\g<1>' + new_desc + r'\g<3>', new_content)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    # Verification
    # 1. desc
    desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', new_content, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', new_content, re.IGNORECASE)
    desc_val = desc_match.group(1).strip() if desc_match else "NOT FOUND"

    # 2. og_desc
    og_desc_match = re.search(r'<meta[^>]*property=["\']og:description["\'][^>]*content=["\']([^"\']*)["\']', new_content, re.IGNORECASE)
    if not og_desc_match:
        og_desc_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*property=["\']og:description["\']', new_content, re.IGNORECASE)
    og_desc_val = og_desc_match.group(1).strip() if og_desc_match else "NOT FOUND"

    match_str = "Yes" if desc_val == og_desc_val else "No [FLAG]"

    # truncate display for cleaner table output to avoid wrapping
    short_desc = desc_val[:40] + "..." if len(desc_val) > 40 else desc_val
    short_og = og_desc_val[:40] + "..." if len(og_desc_val) > 40 else og_desc_val

    print(f"{fpath} | {short_desc} | {short_og} | {match_str}")
