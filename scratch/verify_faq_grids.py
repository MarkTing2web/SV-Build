import re, os

pages = [
    "solutions/commercial.html",
    "solutions/condominiums.html",
    "solutions/healthcare.html",
    "solutions/industrial.html",
    "solutions/institutions.html",
    "solutions/managed-living.html",
    "solutions/residential.html",
    "solutions/data-centres.html",
]

for p in pages:
    with open(p, encoding="utf-8") as fh:
        content = fh.read()
    m = re.search(r'class="(faq-grid[^"]*)"', content)
    cls = m.group(1) if m else "NO FAQ GRID"
    print(f"{os.path.basename(p)}: {cls}")
