import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract #pGrid block
pgrid_start = content.find('id="pGrid"')
# Find the matching closing div for <div class="project-grid" id="pGrid">
# We can just count the number of <div and </div from pgrid_start.
depth = 0
pgrid_end = -1
i = pgrid_start
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
    pgrid_content = content[pgrid_start:pgrid_end]
    # Now find all <a href=... class="project-card"
    # Actually, we can just find all hrefs of a tags
    links = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]+)"[^>]*class="[^"]*project-card[^"]*"|<a\s+(?:[^>]*?\s+)?class="[^"]*project-card[^"]*"\s+(?:[^>]*?\s+)?href="([^"]+)"', pgrid_content)
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

# Extract fYear block
fyear_start = content.find('id="fYear"')
fyear_end = content.find('</select>', fyear_start)
fyear_content = content[fyear_start:fyear_end]
opts = re.findall(r'<option[^>]*value="([^"]+)"', fyear_content)
print(f"Years: {opts}")
