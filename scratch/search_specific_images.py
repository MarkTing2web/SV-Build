import os

repo_root = r"c:\Projects\SV-Build"

target_filenames = [
    "reduce-manpower-with-technology.webp",
    "landed-home-security-singapore.webp",
    "landed-home-security-warmlight-dusk.webp",
    "planning-to-build-new-house.webp",
    "solution-commercial-hotel-hero.webp",
    "landed-home-multiple-entry-points-singapore.webp",
    "solution-commercial-hotel-hotel-mobile-key.webp"
]

results = {filename: [] for filename in target_filenames}

# Find all HTML and CSS files recursively
search_files = []
for root, dirs, files in os.walk(repo_root):
    # Skip directories like .git, node_modules, .vercel
    if any(p in root.split(os.sep) for p in [".git", "node_modules", ".vercel"]):
        continue
    for f in files:
        if f.lower().endswith('.html') or f.lower().endswith('.css'):
            search_files.append(os.path.join(root, f))

# Search each file
for filepath in search_files:
    # Compute relative path from repo root
    rel_path = os.path.relpath(filepath, start=repo_root).replace('\\', '/')
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {rel_path}: {e}")
        continue
        
    for filename in target_filenames:
        if filename in content:
            results[filename].append(rel_path)

output_path = r"c:\Projects\SV-Build\scratch\search_specific_images_output.txt"
with open(output_path, 'w', encoding='utf-8') as out_f:
    found_count = 0
    not_found_count = 0
    
    for filename in target_filenames:
        matching_files = sorted(results[filename])
        if matching_files:
            out_f.write(f"{filename} — FOUND IN: {', '.join(matching_files)}\n")
            found_count += 1
        else:
            out_f.write(f"{filename} — NOT FOUND in any file\n")
            not_found_count += 1
            
    out_f.write("\n")
    out_f.write(f"Total found: {found_count}\n")
    out_f.write(f"Total not found: {not_found_count}\n")
