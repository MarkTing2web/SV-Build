import os

repo_root = r"c:\Projects\SV-Build"

paths = [
    "/images/solutions/commercial/commercial-security-systems-hero.webp",
    "/images/solutions/condominiums/condominium-security-systems-hero.webp",
    "/images/solutions/condominiums/solution-condominiums-managing-agents-hero.webp",
    "/images/solutions/condominiums/solution-condominiums-mcst-hero.webp",
    "/images/solutions/condominiums/solution-condominiums-security-contractors-hero.webp",
    "/images/solutions/data-centres/data-centre-security-systems-hero.webp",
    "/images/solutions/solution-healthcare-daycare-hero.webp",
    "/images/solutions/healthcare/healthcare-security-systems-hero.webp",
    "/images/solutions/industrial/industrial-security-systems-hero.webp",
    "/images/solutions/solution-industrial-logistics-hero.webp",
    "/images/solutions/solution-industrial-manufacturing-hero.webp",
    "/images/solutions/solution-industrial-tech-park-hero.webp",
    "/images/solutions/solution-institutions-community-hero.webp",
    "/images/solutions/solution-institutions-govt-office-hero.webp",
    "/images/solutions/institutions/institutions-security-systems-hero.webp",
    "/images/solutions/solution-institutions-schools-hero.webp",
    "/images/solutions/solution-managed-living-co-living-hero.webp",
    "/images/solutions/managed-living/managed-living-security-systems-hero.webp",
    "/images/solutions/reduce-manpower-with-technology.webp"
]

for p in paths:
    full_path = repo_root + p.replace("/", "\\")
    if os.path.exists(full_path):
        print(f"{p} — EXISTS")
    else:
        print(f"{p} — MISSING")
