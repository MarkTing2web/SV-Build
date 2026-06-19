import re

with open("solutions/data-centres.html", encoding="utf-8") as fh:
    content = fh.read()

remaining = len(re.findall(r'sol-grid-4-auto', content))
print(f"sol-grid-4-auto remaining: {remaining}  (expected: 0)")

section_blocks = re.findall(r'<section[^>]*>.*?</section>', content, re.S)
for sec in section_blocks:
    eyebrow = re.search(r'<span class="eyebrow[^"]*">(.*?)</span>', sec)
    h2 = re.search(r'<h2[^>]*>(.*?)</h2>', sec, re.S)
    label = eyebrow.group(1) if eyebrow else (re.sub(r'<[^>]+>','',h2.group(1)).strip()[:35] if h2 else "?")
    grid = re.search(r'class="(grid-\d[^"]*|sol-grid[^"]*)"', sec)
    if grid:
        print(f"  {label:<40} | {grid.group(1)}")
