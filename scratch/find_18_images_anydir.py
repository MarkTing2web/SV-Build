import os

repo_root = r"c:\Projects\SV-Build"

files_to_check = [
    "commercial-security-systems-hero.webp",
    "condominium-security-systems-hero.webp",
    "solution-condominiums-managing-agents-hero.webp",
    "solution-condominiums-mcst-hero.webp",
    "solution-condominiums-security-contractors-hero.webp",
    "data-centre-security-systems-hero.webp",
    "solution-healthcare-daycare-hero.webp",
    "healthcare-security-systems-hero.webp",
    "industrial-security-systems-hero.webp",
    "solution-industrial-logistics-hero.webp",
    "solution-industrial-manufacturing-hero.webp",
    "solution-industrial-tech-park-hero.webp",
    "solution-institutions-community-hero.webp",
    "solution-institutions-govt-office-hero.webp",
    "institutions-security-systems-hero.webp",
    "solution-institutions-schools-hero.webp",
    "solution-managed-living-co-living-hero.webp",
    "managed-living-security-systems-hero.webp"
]

found = {}
for file in files_to_check:
    found[file] = []

for root, dirs, filenames in os.walk(repo_root):
    for filename in filenames:
        if filename in found:
            found[filename].append(os.path.join(root, filename))

for i, file in enumerate(files_to_check, 1):
    paths = found[file]
    if paths:
        print(f"{i}. {file}: FOUND AT {paths}")
    else:
        print(f"{i}. {file}: NOT FOUND ANYWHERE IN REPO")
