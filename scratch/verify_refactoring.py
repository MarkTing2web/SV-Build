import os
import re

repo_root = r"c:\Projects\SV-Build"
dest_dir = os.path.join(repo_root, "images", "solutions", "hero-solutions")

target_filenames = [
    "automate-vehicle-access-hero.webp",
    "healthcare-hero.webp",
    "improve-visitor-management-hero.webp",
    "intercom-upgrade-hero.webp",
    "reduce-manpower-with-technology-mobile.webp",
    "reduce-manpower-with-technology-rel.webp",
    "solution-commercial-office-hero.webp",
    "solution-commercial-retail-hero.webp",
    "solution-data-centres-hero.webp",
    "solution-healthcare-aged-care-hero.webp",
    "solution-improve-cctv-visibility-hero.webp",
    "solution-industrial-industrial-analysis.webp",
    "solution-managed-living-dormitories-hero.webp",
    "solution-managed-living-hero.webp",
    "solution-managed-living-hostels-hero.webp",
    "solutions-hub-singapore-mobile.webp",
    "solutions-hub-singapore-rel.webp",
    "solutions-hub-singapore.webp",
    "commercial-security-singapore-mobile.webp",
    "commercial-security-singapore-rel.webp",
    "commercial-security-singapore.webp",
    "solution-commercial-hotel-hero.webp",
    "condominium-estate-security-singapore-mobile.webp",
    "condominium-estate-security-singapore-rel.webp",
    "condominium-estate-security-singapore.webp",
    "data-centre-security-singapore-mobile.webp",
    "data-centre-security-singapore-rel.webp",
    "data-centre-security-singapore.webp",
    "healthcare-security-singapore-mobile.webp",
    "healthcare-security-singapore-rel.webp",
    "healthcare-security-singapore.webp",
    "industrial-security-singapore-mobile.webp",
    "industrial-security-singapore-rel.webp",
    "industrial-security-singapore.webp",
    "institutional-security-singapore-mobile.webp",
    "institutional-security-singapore-rel.webp",
    "institutional-security-singapore.webp",
    "dormitories-hero.webp",
    "hostels-hero.webp",
    "managed-living-hero.webp",
    "managed-living-security-singapore-rel.webp",
    "managed-living-security-singapore.webp",
    "managed-living-singapore-mobile.webp",
    "landed-home-security-singapore-mobile.webp",
    "landed-home-security-singapore-rel.webp",
    "landed-home-security-singapore.webp",
    "landed-home-security-warmlight-dusk-mobile.webp",
    "landed-home-security-warmlight-dusk.webp",
    "partnering-architects-and-designers-mobile.webp",
    "partnering-architects-and-designers-rel.webp",
    "planning-to-build-new-house-mobile.webp",
    "planning-to-build-new-house-rel.webp",
    "planning-to-build-new-house.webp",
    "upgrade-fix-residential-security-system-mobile.webp",
    "upgrade-fix-residential-security-system-rel.webp",
    "upgrade-fix-residential-security-system.webp"
]

print("--- VERIFYING FILE MOVEMENTS ---")
# Check if all 53 files exist in c:\Projects\SV-Build\images\solutions\hero-solutions
missing_in_dest = []
for fn in target_filenames:
    # 3 files were known missing originally, let's skip them or verify they are not there
    if fn in ["solution-managed-living-dormitories-hero.webp", "solution-managed-living-hero.webp", "solution-managed-living-hostels-hero.webp"]:
        continue
    full_dest_path = os.path.join(dest_dir, fn)
    if not os.path.exists(full_dest_path):
        missing_in_dest.append(fn)

print(f"Total files missing in hero-solutions: {len(missing_in_dest)}")
if missing_in_dest:
    for m in missing_in_dest:
        print(f"  Missing: {m}")
else:
    print("  All 53 existing files successfully verified in images/solutions/hero-solutions/!")

print("\n--- VERIFYING HTML REFERENCES ---")
# Find all HTML files recursively
html_files = []
for root, dirs, files in os.walk(repo_root):
    if any(p in root.split(os.sep) for p in [".git", "node_modules", ".vercel"]):
        continue
    for f in files:
        if f.lower().endswith('.html'):
            html_files.append(os.path.join(root, f))

incorrect_references = []
for filepath in html_files:
    rel_path = os.path.relpath(filepath, repo_root).replace('\\', '/')
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    lines = content.split('\n')
    for line_idx, line in enumerate(lines):
        # Find all image paths in the line
        pattern = r'[\w\:\.\-/]*/?images/[\w\.\-/]*\.webp'
        matches = re.findall(pattern, line)
        for m in matches:
            # Check if this matched path contains any of our target filenames
            matched_fn = None
            # Find the longest matching filename to avoid substring false positives
            for fn in sorted(target_filenames, key=len, reverse=True):
                if m.endswith(fn):
                    matched_fn = fn
                    break
            
            if matched_fn:
                # This path refers to one of our moved files!
                # It must be correctly prefixed
                is_correct = False
                if m.endswith(f"/images/solutions/hero-solutions/{matched_fn}"):
                    is_correct = True
                elif m.endswith(f"https://www.securevision.com.sg/images/solutions/hero-solutions/{matched_fn}"):
                    is_correct = True
                
                if not is_correct:
                    incorrect_references.append((rel_path, line_idx + 1, matched_fn, m))

print(f"Total incorrect/unconverted references found: {len(incorrect_references)}")
if incorrect_references:
    for r, line, fn, matched in incorrect_references:
        print(f"  {r}:{line} -> found '{fn}' in '{matched}' (Expected to contain '/images/solutions/hero-solutions/{fn}')")
else:
    print("  All HTML references verified successfully! No unconverted references found.")
