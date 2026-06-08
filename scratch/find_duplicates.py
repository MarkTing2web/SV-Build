import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

pgrid_idx = content.find('id="pGrid"')
div_start = content.rfind('<div', 0, pgrid_idx)

depth = 0
pgrid_end = -1
i = div_start
while i < len(content):
    if content.startswith('<div', i):
        depth += 1
    elif content.startswith('</div', i):
        depth -= 1
        if depth == 0:
            pgrid_end = i
            break
    i += 1

if pgrid_end == -1:
    print("Could not parse #pGrid")
    exit()

pgrid_content = content[div_start:pgrid_end]

cards = []
for m in re.finditer(r'<a\s+(?:[^>]*?\s+)?class="[^"]*project-card[^"]*"\s+(?:[^>]*?\s+)?href="([^"]+)"|<a\s+(?:[^>]*?\s+)?href="([^"]+)"\s+(?:[^>]*?\s+)?class="[^"]*project-card[^"]*"', pgrid_content):
    href = m.group(1) or m.group(2)
    match_start = div_start + m.start()
    line_num = content[:match_start].count('\n') + 1
    cards.append((href, line_num))

from collections import defaultdict
counts = defaultdict(list)
for href, line in cards:
    counts[href].append(line)

for href, occurrences in counts.items():
    if len(occurrences) > 1:
        print(f"- {href}")
        print(f"  Count: {len(occurrences)}")
        print(f"  Lines: {', '.join(map(str, occurrences))}")
