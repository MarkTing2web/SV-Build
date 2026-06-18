import re, os, glob

files = sorted(glob.glob("solutions/*.html"))
# Exclude non-sector pages
exclude = ["automate-vehicle-access.html", "improve-cctv-visibility.html",
           "improve-visitor-management.html", "reduce-guard-manpower.html",
           "upgrade-intercom-system.html"]

print(f"{'File':<30} {'Systems':>8} {'data-cols':>10} {'Status'}")
print("-" * 60)

all_ok = True
for path in files:
    fname = os.path.basename(path)
    if fname in exclude:
        continue
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    block = re.search(r'<div class="sv-systems-block"([^>]+)>', content, re.S)
    if not block:
        continue
    attrs = block.group(1)
    systems = re.search(r'data-systems="([^"]+)"', attrs)
    cols    = re.search(r'data-cols="([^"]+)"', attrs)
    keys     = systems.group(1).split(",") if systems else []
    cols_val = cols.group(1) if cols else "NOT SET"
    ok = len(keys) == 6 and cols_val == "3"
    if not ok:
        all_ok = False
    status = "OK" if ok else f"NEEDS FIX (systems={len(keys)}, cols={cols_val})"
    print(f"{fname:<30} {len(keys):>8} {cols_val:>10}   [{status}]")

print()
print("All OK:" if all_ok else "ISSUES FOUND — fix flagged files before proceeding.")
