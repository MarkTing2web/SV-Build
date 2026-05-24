import os

repo_root = r"c:\Projects\SV-Build"

files_to_check = [
    "images/solutions/hero-solutions/solution-industrial-logistics-hero-rel.webp",
    "images/solutions/hero-solutions/solution-industrial-manufacturing-hero-rel.webp",
    "images/solutions/hero-solutions/solution-industrial-tech-park-hero-rel.webp",
    "images/solutions/hero-solutions/solution-commercial-office-hero-rel.webp",
    "images/solutions/hero-solutions/solution-commercial-retail-hero-rel.webp",
    "images/solutions/hero-solutions/solution-institutions-schools-hero-rel.webp",
    "images/solutions/hero-solutions/solution-institutions-govt-office-hero-rel.webp",
    "images/solutions/hero-solutions/solution-healthcare-aged-care-hero-rel.webp",
    "images/solutions/hero-solutions/hostels-hero-rel.webp",
    "images/solutions/hero-solutions/industrial-security-singapore-rel.webp",
    "images/solutions/hero-solutions/healthcare-security-singapore-rel.webp",
    "images/solutions/hero-solutions/condominium-estate-security-singapore-rel.webp",
    "images/solutions/hero-solutions/commercial-security-singapore-rel.webp"
]

missing = []
for f in files_to_check:
    path = os.path.join(repo_root, f)
    exists = os.path.exists(path)
    print(f"{f} — {'EXISTS' if exists else 'MISSING'}")
    if not exists:
        missing.append(f)

print(f"\nTotal checked: {len(files_to_check)}")
print(f"Total missing: {len(missing)}")
