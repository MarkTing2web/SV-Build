import os
import re

repo_root = r"c:\Projects\SV-Build"

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

# Find all HTML files recursively
html_files = []
for root, dirs, files in os.walk(repo_root):
    if any(p in root.split(os.sep) for p in [".git", "node_modules", ".vercel"]):
        continue
    for f in files:
        if f.lower().endswith('.html'):
            html_files.append(os.path.join(root, f))

# We want to identify the references that contain these filenames.
# Specifically, we want to find paths that end with /filename (possibly with domain or relative prefix), e.g.:
# /images/solutions/commercial/commercial-security-singapore.webp
# or images/solutions/commercial/commercial-security-singapore.webp
# and replace the path leading to it with /images/solutions/hero-solutions/

# Let's run a dry run scan of HTML files.
html_updates = {}
total_refs = 0

# For matching, let's compile regexes or check for patterns.
# A pattern could be: any string ending in filename, preceded by images/solutions/ or similar.
# To be robust, let's search for any occurrence of the filename, check if it's part of a path in src/srcset/og:image/background-image,
# and print what matches we find.
for filepath in html_files:
    rel_path = os.path.relpath(filepath, repo_root).replace('\\', '/')
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    file_changes = []
    
    # We can check line-by-line to see exactly what would be matched
    lines = content.split('\n')
    for idx, line in enumerate(lines):
        for fn in target_filenames:
            if fn in line:
                # Find the path that contains this filename in this line
                # Let's extract substrings that look like paths containing this filename.
                # A path might be quoted or in url() or srcset:
                # e.g., src="/images/solutions/commercial/commercial-security-singapore.webp"
                # e.g., url('/images/solutions/commercial/commercial-security-singapore.webp')
                # e.g., content="https://www.securevision.com.sg/images/solutions/commercial/commercial-security-singapore.webp"
                # e.g., srcset="/images/solutions/commercial/commercial-security-singapore.webp"
                # Let's write a regex that matches paths containing the filename
                # Typically a path contains letters, numbers, slashes, dashes, dots, underscores, or https?://
                pattern = rf'[\w\:\.\-/]*/?images/[\w\.\-/]*{re.escape(fn)}'
                matches = re.findall(pattern, line)
                if matches:
                    for m in matches:
                        file_changes.append((idx + 1, fn, m))
                        
    if file_changes:
        html_updates[rel_path] = file_changes
        total_refs += len(file_changes)

# Now write to output file
output_path = r"c:\Projects\SV-Build\scratch\dry_run_html_refs_output.txt"
with open(output_path, 'w', encoding='utf-8') as out_f:
    out_f.write(f"Total references found: {total_refs}\n")
    out_f.write(f"Total HTML files with references: {len(html_updates)}\n")
    for f, changes in sorted(html_updates.items()):
        out_f.write(f"\nFILE: {f} ({len(changes)} changes)\n")
        for line_num, fn, matched in changes:
            out_f.write(f"  Line {line_num}: found '{fn}' in '{matched}'\n")

