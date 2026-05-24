import os

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images")

target_bases = [
    "commercial-building-turnstile-lift-access-singapore",
    "commercial-security-overview-singapore",
    "hotel-cctv-access-lift-control-singapore",
    "mall-cctv-crowd-analytics-singapore",
    "office-access-control-intercom-singapore",
    "retail-cctv-analytics-pos-singapore",
    "akuvox-visitor-call-panel-condominium-lobby",
    "cctv-wide-angle-car-park-corridor",
    "condominium-guardhouse-control-room",
    "lpr-camera-vehicle-barrier-condominium",
    "remote-monitoring-estate-security-dashboard",
    "vesta-platform-dashboard-estate-management",
    "data-centre-biometric-card-access-data-hall",
    "data-centre-cctv-corridor-camera-coverage",
    "data-centre-security-tiered-zones-singapore",
    "data-centre-visitor-management-reception-log",
    "care-facility-security-overview-singapore",
    "day-care-specialist-centre-carer-alert-visitor-management",
    "nursing-home-safe-zone-monitoring-carer-alert",
    "factory-cctv-access-control-production-floor",
    "industrial-facility-perimeter-security-singapore",
    "logistics-lpr-gantry-loading-bay-surveillance",
    "ppe-compliance-ai-camera-wsh-audit-singapore",
    "tech-park-estate-access-control-turnstile",
    "government-office-visitor-management-access-control",
    "institutions-security-overview-singapore",
    "religious-community-cctv-crowd-monitoring-singapore",
    "school-cctv-visitor-management-lockdown-singapore",
    "co-living-mobile-keyless-access-visitor-intercom",
    "dormitory-lpr-gantry-facial-recognition-entry",
    "hostel-shared-living-access-cctv-intercom",
    "managed-living-security-overview-singapore"
]

# We scan the images_dir recursively and collect all existing files.
# Map of lowercase filename -> relative path from repo root starting with /images/
on_disk_files = {}
for root, dirs, files in os.walk(images_dir):
    for f in files:
        full_path = os.path.join(root, f)
        rel_path = "/" + os.path.relpath(full_path, repo_root).replace('\\', '/')
        on_disk_files[f.lower()] = rel_path

results = []
found_count = 0
not_found_bases = []

for base in target_bases:
    webp_filename = f"{base}.webp".lower()
    png_filename = f"{base}.png".lower()
    
    found_paths = []
    if webp_filename in on_disk_files:
        found_paths.append(on_disk_files[webp_filename])
    if png_filename in on_disk_files:
        found_paths.append(on_disk_files[png_filename])
        
    if found_paths:
        # We report all found formats
        for path in found_paths:
            results.append(f"{base} — FOUND: {path}")
        found_count += 1
    else:
        results.append(f"{base} — NOT FOUND")
        not_found_bases.append(base)

output_file = r"c:\Projects\SV-Build\scratch\search_specific_images_on_disk_output.txt"
with open(output_file, 'w', encoding='utf-8') as out_f:
    for line in results:
        out_f.write(f"{line}\n")
    out_f.write("\n")
    out_f.write("Summary:\n")
    out_f.write(f"  Found: {found_count} of 32\n")
    out_f.write(f"  Not found: {len(not_found_bases)} of 32\n")
    out_f.write("\nList of not found:\n")
    for nf in not_found_bases:
        out_f.write(f"  {nf}\n")
