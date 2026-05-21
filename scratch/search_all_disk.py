import os

repo_root = r"c:\Projects\SV-Build"
targets = [
    "reduce-manpower-with-technology.png",
    "solution-data-centres-hero.webp",
    "solution-healthcare-aged-care-hero.webp",
    "solution-industrial-industrial-analysis.webp"
]

print("Searching absolutely everywhere under workspace root...")
for root, dirs, files in os.walk(repo_root):
    for f in files:
        for t in targets:
            if f.lower() == t.lower():
                print(f"FOUND MATCH: '{t}' at '{os.path.join(root, f)}'")
