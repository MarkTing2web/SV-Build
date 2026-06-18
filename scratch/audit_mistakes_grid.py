import re, os, glob

files = sorted(glob.glob("solutions/**/*.html", recursive=True))

for path in files:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    if not re.search(r'Common Mistakes', content, re.I):
        continue
    m = re.search(r'Common Mistakes.{0,2000}', content, re.S | re.I)
    if not m:
        continue
    snippet = m.group(0)
    grids = re.findall(r'class="([^"]*(?:grid|stack)[^"]*)"', snippet)
    print(f"{path}: {grids[:3]}")
