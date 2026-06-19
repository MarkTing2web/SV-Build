import re, os

files = [
    "solutions/reduce-guard-manpower.html",
    "solutions/improve-visitor-management.html",
    "solutions/upgrade-intercom-system.html",
    "solutions/improve-cctv-visibility.html",
    "solutions/automate-vehicle-access.html",
]

for path in files:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    sections = re.findall(r'<section[^>]*>.*?</section>', content, re.S)
    for sec in sections:
        if "Project Planning" not in sec:
            continue
        grid = re.search(r'class="(grid-\d[^"]*)"', sec)
        cards = len(re.findall(r'<div class="card">', sec))
        actual = grid.group(1) if grid else "NOT FOUND"
        ok = actual == "grid-3 mt-48" and cards == 6
        print(f"{'✅' if ok else '❌'} {os.path.basename(path)}: grid={actual}, cards={cards}")
