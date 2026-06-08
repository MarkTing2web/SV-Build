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
    links = re.findall(r'<a\s+(?:[^>]*?\s+)?class="[^"]*project-card[^"]*"\s+(?:[^>]*?\s+)?href="([^"]+)"|<a\s+(?:[^>]*?\s+)?href="([^"]+)"\s+(?:[^>]*?\s+)?class="[^"]*project-card[^"]*"', pgrid_content)
    hrefs = [l[0] or l[1] for l in links]
    print(f"Total cards strictly inside #pGrid: {len(hrefs)}")
    
    for i, href in enumerate(hrefs):
        if href == "/portfolio/commercial/scape-commercial.html":
            print(f"After scape-commercial: {hrefs[i+1]}")
        if href == "/portfolio/data-centres/fort-data-centre-access-upgrade.html":
            print(f"After fort-data-centre: {hrefs[i+1]}")
        if href == "/portfolio/commercial/catholic-centre-security-partnership.html":
            print(f"After catholic-centre: {hrefs[i+1]}")
            
    print(f"Last card: {hrefs[-1]}")
else:
    print("Could not parse pGrid boundaries")
