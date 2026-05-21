import os
import shutil

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images")

targets = [
    "reduce-manpower-with-technology.png",
    "solution-data-centres-hero.webp",
    "solution-healthcare-aged-care-hero.webp",
    "solution-industrial-industrial-analysis.webp"
]

# Find current locations of targets recursively under images/
# Exclude the target destination if it's already there (though we want to know if it's there)
found_paths = {t: [] for t in targets}

for root, dirs, files in os.walk(images_dir):
    for f in files:
        if f in found_paths:
            found_paths[f].append(os.path.join(root, f))

for t, paths in found_paths.items():
    print(f"File '{t}' found at:")
    for p in paths:
        rel = os.path.relpath(p, repo_root)
        print(f"  - {rel}")
