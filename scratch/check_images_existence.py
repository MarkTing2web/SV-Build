import os

root = r"c:\Projects\SV-Build\images\solutions\hero-solutions"

files = [
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

for i, f in enumerate(files, 1):
    path = os.path.join(root, f)
    status = "EXISTS" if os.path.exists(path) else "MISSING"
    print(f"{i}. {f}: {status}")
