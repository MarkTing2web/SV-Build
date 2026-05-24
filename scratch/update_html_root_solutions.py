import os

repo_root = r"c:\Projects\SV-Build"

filenames = [
    "reduce-manpower-with-technology.webp",
    "service-technicians-fixing-cameras-in-a-retail-outlet-while-boss-looks-on.webp",
    "solution-automate-vehicle-access-manual-bottleneck.webp",
    "solution-automate-vehicle-access-mcst-gantry-inspection.webp",
    "solution-automate-vehicle-access-pillar_vehicle_access.webp",
    "solution-automate-vehicle-access-prop-commercial.webp",
    "solution-automate-vehicle-access-prop-condo.webp",
    "solution-automate-vehicle-access-prop-industrial.webp",
    "solution-automate-vehicle-access-vehicle-lpr-camera.webp",
    "solution-automate-vehicle-access-vehicle-peak-bottleneck.webp",
    "solution-commercial-cover.webp",
    "solution-commercial-hero.webp",
    "solution-commercial-hotel-platform-multi-site.webp",
    "solution-commercial-office-cover.webp",
    "solution-commercial-pillar_people_access.webp",
    "solution-commercial-pillar_surveillance.webp",
    "solution-commercial-retail-video-analytics-of-a-retail-shop.webp",
    "solution-condominiums-condo-estate-operations.webp",
    "solution-condominiums-condo-resident-experience.webp",
    "solution-condominiums-mcst-mcst-proof.webp",
    "solution-condominiums-project-condo-upgrade.webp",
    "solution-condominiums-project-estate-integration.webp",
    "solution-healthcare-healthcare-occupancy.webp",
    "solution-healthcare-healthcare-path-hostel.webp",
    "solution-healthcare-healthcare-path-nursing.webp",
    "solution-hub-prop-school.webp",
    "solution-improve-cctv-visibility-cctv-ai-analytics-square.webp",
    "solution-improve-cctv-visibility-cctv-colorvu-square.webp",
    "solution-improve-cctv-visibility-cctv-panoramic-square.webp",
    "solution-improve-cctv-visibility-cctv-smart-search-square.webp",
    "solution-improve-visitor-management-managed-residential.webp",
    "solution-improve-visitor-management-unified-audit-trail.webp",
    "solution-institutions-project-religious.webp",
    "solution-institutions.webp",
    "solution-residential-home-upgrade-cover.webp",
    "solution-residential-home-upgrade-project-bt-semi-d.webp",
    "solution-residential-home-upgrade-project-holland-semi-d.webp",
    "solution-residential-home-upgrade-project-terrace-east.webp",
    "solution-upgrade-intercom-system-mature-condo.webp",
    "solution-upgrade-intercom-system-solution-condo.webp",
    "solution-upgrade-intercom-system-vesta-app-condo.webp"
]

# Find all html files
exclude_dirs = {'.git', '.vercel', 'scratch', 'node_modules', 'artifacts', '.github'}
html_files = []
for root, dirs, files in os.walk(repo_root):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

html_files.sort()

# Perform replacement and track counts
total_changed = 0
file_changes = {}
filename_found_counts = {fn: 0 for fn in filenames}

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original_content = content
    file_changed_count = 0

    for fn in filenames:
        target = f"images/solutions/{fn}"
        replacement = f"images/solutions/root-solutions/{fn}"
        
        if target in content:
            count = content.count(target)
            content = content.replace(target, replacement)
            file_changed_count += count
            filename_found_counts[fn] += count

    if file_changed_count > 0:
        # Write back to disk
        with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        rel_path = os.path.relpath(filepath, repo_root).replace('\\', '/')
        file_changes[rel_path] = file_changed_count
        total_changed += file_changed_count

# Output details
for rel_path, count in sorted(file_changes.items()):
    print(f"{rel_path} — {count} references updated")

print("\n" + "="*50)
print(f"Total references updated across all files: {total_changed}")

print("\nFilename search results:")
not_found_count = 0
for fn, count in sorted(filename_found_counts.items()):
    if count == 0:
        print(f"  FLAG: {fn} — NOT FOUND")
        not_found_count += 1
    else:
        print(f"  {fn} — Found {count} times")
        
print(f"\nTotal files updated: {len(file_changes)}")
print(f"Total filenames not found: {not_found_count}")
