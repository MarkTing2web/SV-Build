import os

repo_root = r"c:\Projects\SV-Build"

from_paths = [
    "images/solutions/automate-vehicle-access-hero.webp",
    "images/solutions/healthcare-hero.webp",
    "images/solutions/improve-visitor-management-hero.webp",
    "images/solutions/intercom-upgrade-hero.webp",
    "images/solutions/reduce-manpower-with-technology-mobile.webp",
    "images/solutions/reduce-manpower-with-technology-rel.webp",
    "images/solutions/solution-commercial-office-hero.webp",
    "images/solutions/solution-commercial-retail-hero.webp",
    "images/solutions/solution-data-centres-hero.webp",
    "images/solutions/solution-healthcare-aged-care-hero.webp",
    "images/solutions/solution-improve-cctv-visibility-hero.webp",
    "images/solutions/solution-industrial-industrial-analysis.webp",
    "images/solutions/solution-managed-living-dormitories-hero.webp",
    "images/solutions/solution-managed-living-hero.webp",
    "images/solutions/solution-managed-living-hostels-hero.webp",
    "images/solutions/solutions-hub-singapore-mobile.webp",
    "images/solutions/solutions-hub-singapore-rel.webp",
    "images/solutions/solutions-hub-singapore.webp",
    "images/solutions/commercial/commercial-security-singapore-mobile.webp",
    "images/solutions/commercial/commercial-security-singapore-rel.webp",
    "images/solutions/commercial/commercial-security-singapore.webp",
    "images/solutions/commercial/solution-commercial-hotel-hero.webp",
    "images/solutions/condominiums/condominium-estate-security-singapore-mobile.webp",
    "images/solutions/condominiums/condominium-estate-security-singapore-rel.webp",
    "images/solutions/condominiums/condominium-estate-security-singapore.webp",
    "images/solutions/data-centres/data-centre-security-singapore-mobile.webp",
    "images/solutions/data-centres/data-centre-security-singapore-rel.webp",
    "images/solutions/data-centres/data-centre-security-singapore.webp",
    "images/solutions/healthcare/healthcare-security-singapore-mobile.webp",
    "images/solutions/healthcare/healthcare-security-singapore-rel.webp",
    "images/solutions/healthcare/healthcare-security-singapore.webp",
    "images/solutions/industrial/industrial-security-singapore-mobile.webp",
    "images/solutions/industrial/industrial-security-singapore-rel.webp",
    "images/solutions/industrial/industrial-security-singapore.webp",
    "images/solutions/industrial/industrial-security-singapore.webp", # Duplicated in list, let's keep it to check
    "images/solutions/institutions/institutional-security-singapore-mobile.webp",
    "images/solutions/institutions/institutional-security-singapore-rel.webp",
    "images/solutions/institutions/institutional-security-singapore.webp",
    "images/solutions/managed-living/dormitories-hero.webp",
    "images/solutions/managed-living/hostels-hero.webp",
    "images/solutions/managed-living/managed-living-hero.webp",
    "images/solutions/managed-living/managed-living-security-singapore-rel.webp",
    "images/solutions/managed-living/managed-living-security-singapore.webp",
    "images/solutions/managed-living/managed-living-singapore-mobile.webp",
    "images/solutions/residential/landed-home-security-singapore-mobile.webp",
    "images/solutions/residential/landed-home-security-singapore-rel.webp",
    "images/solutions/residential/landed-home-security-singapore.webp",
    "images/solutions/residential/landed-home-security-warmlight-dusk-mobile.webp",
    "images/solutions/residential/landed-home-security-warmlight-dusk.webp",
    "images/solutions/residential/partnering-architects-and-designers-mobile.webp",
    "images/solutions/residential/partnering-architects-and-designers-rel.webp",
    "images/solutions/residential/planning-to-build-new-house-mobile.webp",
    "images/solutions/residential/planning-to-build-new-house-rel.webp",
    "images/solutions/residential/planning-to-build-new-house.webp",
    "images/solutions/residential/upgrade-fix-residential-security-system-mobile.webp",
    "images/solutions/residential/upgrade-fix-residential-security-system-rel.webp",
    "images/solutions/residential/upgrade-fix-residential-security-system.webp"
]

# Deduplicate from_paths maintaining order
unique_from_paths = []
for p in from_paths:
    if p not in unique_from_paths:
        unique_from_paths.append(p)

print(f"Total unique input paths: {len(unique_from_paths)}")

existing = []
missing = []
for p in unique_from_paths:
    full_path = os.path.join(repo_root, p)
    if os.path.exists(full_path):
        existing.append(p)
    else:
        missing.append(p)

print("\n--- EXISTING FILES ---")
for p in existing:
    print(f"  EXISTS: {p}")

print("\n--- MISSING FILES ---")
for p in missing:
    print(f"  MISSING: {p}")
