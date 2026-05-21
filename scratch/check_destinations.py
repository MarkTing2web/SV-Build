import os

repo_root = r"c:\Projects\SV-Build"
destinations = [
    "images/solutions/reduce-manpower-with-technology.png",
    "images/solutions/solution-data-centres-hero.webp",
    "images/solutions/solution-healthcare-aged-care-hero.webp",
    "images/solutions/solution-industrial-industrial-analysis.webp"
]

for d in destinations:
    abs_d = os.path.join(repo_root, d)
    exists = os.path.exists(abs_d)
    print(f"Destination '{d}' exists: {exists}")
