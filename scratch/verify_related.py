import re

with open("solutions/upgrade-intercom-system.html", encoding="utf-8") as fh:
    content = fh.read()

m = re.search(r'Explore Related Insights.*?class="(grid-\d[^"]*)"', content, re.S)
actual = m.group(1) if m else "NOT FOUND"
print(f"Related Insights grid: {actual}  (expected: grid-2 mt-48)")
