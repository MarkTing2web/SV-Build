import os
import shutil

repo_root = r"c:\Projects\SV-Build"
dest_dir = os.path.join(repo_root, "images", "solutions", "hero-solutions")

# Create destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# List of 56 relative paths from the user prompt
paths_to_move = [
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

# Deduplicate maintaining order
unique_paths = []
for p in paths_to_move:
    if p not in unique_paths:
        unique_paths.append(p)

moved_count = 0
not_found = []

for p in unique_paths:
    src_full = os.path.join(repo_root, p)
    filename = os.path.basename(p)
    dest_full = os.path.join(dest_dir, filename)
    
    if os.path.exists(src_full):
        # Move the file
        print(f"Moving: {p} -> images/solutions/hero-solutions/{filename}")
        shutil.move(src_full, dest_full)
        moved_count += 1
    else:
        print(f"Not found: {p}")
        not_found.append(p)

print("\n--- RESULTS ---")
print(f"Successfully moved: {moved_count} files")
print(f"Not found: {len(not_found)} files")
if not_found:
    print("List of not found files:")
    for nf in not_found:
        print(f"  {nf}")
