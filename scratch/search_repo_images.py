import os

repo_root = r"c:\Projects\SV-Build"

targets = [
    "reduce-manpower-with-technology",
    "solution-data-centres-hero",
    "solution-healthcare-aged-care-hero",
    "solution-industrial-industrial-analysis"
]

for root, dirs, files in os.walk(repo_root):
    # Skip node_modules and .git
    if "node_modules" in root or ".git" in root:
        continue
    for f in files:
        for t in targets:
            if t.lower() in f.lower():
                print(f"MATCH: '{f}' in '{root}'")
