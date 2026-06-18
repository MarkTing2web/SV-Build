import re

pages = [
    ("data-centres",   "solutions/data-centres.html"),
    ("managed-living", "solutions/managed-living.html"),
]

for slug, path in pages:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    block = re.search(r'<div class="sv-systems-block"([^>]+)>', content, re.S)
    if not block:
        print(f"{slug}: NOT FOUND")
        continue
    attrs = block.group(1)
    systems = re.search(r'data-systems="([^"]+)"', attrs)
    intro   = re.search(r'data-intro="([^"]+)"', attrs)
    has_desc = 'data-desc-vehicle-lpr=' in attrs
    keys = systems.group(1).split(",") if systems else []
    print(f"\n{slug}:")
    print(f"  systems count: {len(keys)}  (expected: 6)")
    print(f"  vehicle-lpr present: {'vehicle-lpr' in keys}  (expected: True)")
    print(f"  data-desc-vehicle-lpr: {has_desc}  (expected: True)")
    print(f"  intro: {intro.group(1) if intro else 'n/a'}")
