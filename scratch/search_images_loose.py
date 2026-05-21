import os

repo_root = r"c:\Projects\SV-Build"
images_dir = os.path.join(repo_root, "images")

targets = [
    "reduce-manpower-with-technology.png",
    "solution-data-centres-hero.webp",
    "solution-healthcare-aged-care-hero.webp",
    "solution-industrial-industrial-analysis.webp"
]

for root, dirs, files in os.walk(images_dir):
    for f in files:
        for t in targets:
            # Let's do a case-insensitive check and also strip/clean
            if f.lower() == t.lower():
                print(f"EXACT MATCH: '{f}' in '{root}'")
            elif t.lower().split('.')[0] in f.lower():
                print(f"SUBSTRING MATCH: '{f}' in '{root}' for target '{t}'")
