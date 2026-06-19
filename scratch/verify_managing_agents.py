import re

with open("solutions/condominiums/managing-agents.html", encoding="utf-8") as fh:
    content = fh.read()

has_framework = "framework-grid" in content
m = re.search(r'The Operational Challenge.*?</section>', content, re.S)
section = m.group(0) if m else ""
grid = re.search(r'class="([^"]*grid[^"]*)"', section)

print(f"framework-grid removed: {not has_framework}  (expected: True)")
print(f"Grid class: {grid.group(1) if grid else 'NOT FOUND'}  (expected: grid-2 solution-personas mt-48)")
