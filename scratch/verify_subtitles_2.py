import re

files = [
    ("industrial",     "solutions/industrial.html"),
    ("managed-living", "solutions/managed-living.html"),
]

for slug, path in files:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    sub = re.search(r'<p class="hero-subtitle-main">(.*?)</p>', content, re.S)
    text = re.sub(r'<[^>]+>', '', sub.group(1)).strip() if sub else "NOT FOUND"
    print(f"{slug} ({len(text)} chars): {text}")
