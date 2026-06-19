import re

with open("solutions/improve-cctv-visibility.html", encoding="utf-8") as fh:
    content = fh.read()

m = re.search(r'Strategic Outcomes.*?</section>', content, re.S)
section = m.group(0) if m else ""

grid  = re.search(r'class="(grid-\d[^"]*)"', section)
cards = len(re.findall(r'<div class="card">', section))

print(f"Grid class: {grid.group(1) if grid else 'NOT FOUND'}  (expected: grid-3 mt-48)")
print(f"Card count: {cards}  (expected: 6)")
print(f"Layout:     {cards // 3} rows × 3 columns  (expected: 2 rows × 3 columns)")
