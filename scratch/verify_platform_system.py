import re

pages = [
    ("healthcare",  "solutions/healthcare.html"),
    ("residential", "solutions/residential.html"),
]

for slug, path in pages:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    systems = re.search(r'data-systems="([^"]+)"', content)
    intro   = re.search(r'data-intro="([^"]+)"', content)
    has_platform_desc = "data-desc-platform=" in content
    keys = systems.group(1).split(",") if systems else []
    print(f"\n{slug}:")
    print(f"  systems count: {len(keys)}  (expected: 6)")
    print(f"  platform in systems: {'platform' in keys}  (expected: True)")
    print(f"  data-desc-platform present: {has_platform_desc}  (expected: True)")
    print(f"  intro: {intro.group(1)[:60]}...")
