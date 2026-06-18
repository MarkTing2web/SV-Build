import re, os, glob

checks = {
    "solutions/healthcare.html":         {"Field Observations": "grid-2 mt-48", "Project Planning": "grid-3 mt-48"},
    "solutions/industrial.html":         {"Field Observations": "grid-2 mt-48", "Project Planning": "grid-3 mt-48"},
    "solutions/institutions.html":       {"Field Observations": "grid-2 mt-48", "Project Planning": "grid-3 mt-48"},
    "solutions/managed-living.html":     {"Field Observations": "grid-2 mt-48", "Project Planning": "grid-3 mt-48"},
    "solutions/residential.html":        {"Field Observations": "grid-2 mt-48"},
    "solutions/upgrade-intercom-system.html": {"Field Observations": "grid-2 mt-48"},
    "solutions/data-centres.html":       {"Project Planning": "grid-3 mt-48"},
}

all_ok = True
for path, expected in checks.items():
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    sections = re.split(r'(?=<section)', content)
    fname = os.path.basename(path)
    for eyebrow_label, expected_grid in expected.items():
        found = False
        for sec in sections:
            if eyebrow_label in sec:
                grid = re.search(r'class="(grid-\d[^"]*)"', sec)
                actual = grid.group(1) if grid else "NOT FOUND"
                ok = actual == expected_grid
                if not ok:
                    all_ok = False
                print(f"{'[OK]' if ok else '[NEEDS FIX]'} {fname} | {eyebrow_label} | expected={expected_grid}, actual={actual}")
                found = True
                break
        if not found:
            print(f"[WARN] {fname} | {eyebrow_label} | SECTION NOT FOUND")

print()
print("All OK" if all_ok else "ISSUES FOUND")
