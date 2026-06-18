import re

files = [
    "solutions/commercial.html",
    "solutions/condominiums.html",
    "solutions/data-centres.html",
    "solutions/healthcare.html",
    "solutions/industrial.html",
    "solutions/institutions.html",
    "solutions/managed-living.html",
    "solutions/residential.html",
]

for f in files:
    with open(f, encoding="utf-8") as fh:
        content = fh.read()
    match = re.search(r'min-height:\s*([^;]+);', content)
    height = match.group(1).strip() if match else "NOT FOUND"
    print(f"{f}: {height}")
