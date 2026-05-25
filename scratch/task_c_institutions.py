import os

base_dir = r"c:\Projects\SV-Build\portfolio\institutions"

files = [
    "catholic-centre-waterloo.html",
    "changi-airport-lpr-barriers.html",
    "cpf-maxwell-institution.html",
    "das-learning-centre-woodlands.html",
    "my-world-preschool-cctv.html",
    "sengkang-interim-bus-interchange.html",
    "sfx-retreat-centre-punggol.html"
]

replacements = [
    ("/images/pillar_surveillance.webp", "/images/solutions/root-solutions/solution-commercial-pillar_surveillance.webp"),
    ("/images/pillar_people_access.webp", "/images/solutions/root-solutions/solution-commercial-pillar_people_access.webp"),
    ("/images/pillar_vehicle_access.webp", "/images/solutions/root-solutions/solution-automate-vehicle-access-pillar_vehicle_access.webp")
]

count = 0
for filename in files:
    filepath = os.path.join(base_dir, filename)
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
        print(f"Updated {filename}")

print(f"Task C updated {count} files.")
