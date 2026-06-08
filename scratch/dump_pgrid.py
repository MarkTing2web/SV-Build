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

if pgrid_end != -1:
    pgrid_content = content[div_start:pgrid_end]
    with open(r"d:\Ler Wee Meng\Project-Web\SV-Build\scratch\pgrid_dump.html", "w", encoding="utf-8") as f:
        f.write(pgrid_content)
    print("Dumped pGrid.")
