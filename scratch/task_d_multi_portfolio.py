import os

base_dir = r"c:\Projects\SV-Build"

files = [
    "portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
    "portfolio/healthcare/surya-home.html",
    "portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html",
    "portfolio/managed-living/scb-worker-dormitory-jalan-papan.html",
    "portfolio/data-centres/fort-data-centre-access-upgrade.html",
    "portfolio/data-centres/fort-st-engineering.html"
]

replacements = [
    ("/images/pillar_surveillance.webp", "/images/solutions/root-solutions/solution-commercial-pillar_surveillance.webp"),
    ("/images/pillar_people_access.webp", "/images/solutions/root-solutions/solution-commercial-pillar_people_access.webp"),
    ("/images/pillar_vehicle_access.webp", "/images/solutions/root-solutions/solution-automate-vehicle-access-pillar_vehicle_access.webp")
]

count = 0
for rel_path in files:
    filepath = os.path.join(base_dir, rel_path.replace('/', '\\'))
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    for old_val, new_val in replacements:
        if old_val in content:
            content = content.replace(old_val, new_val)
            changed = True
            
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {rel_path}")

print(f"Task D updated {count} files.")
