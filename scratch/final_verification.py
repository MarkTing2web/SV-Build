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

pgrid_content = content[div_start:pgrid_end]
links = re.findall(r'<a\s+(?:[^>]*?\s+)?class="[^"]*project-card[^"]*"\s+(?:[^>]*?\s+)?href="([^"]+)"|<a\s+(?:[^>]*?\s+)?href="([^"]+)"\s+(?:[^>]*?\s+)?class="[^"]*project-card[^"]*"', pgrid_content)
hrefs = [l[0] or l[1] for l in links]

print("1. Total number of <a class=\"project-card\"> elements inside #pGrid (expected: 53)")
print(f"   Actual: {len(hrefs)}")

def find_first(lst, item):
    for idx, val in enumerate(lst):
        if val == item:
            return idx
    return -1

idx1 = find_first(hrefs, "/portfolio/commercial/scape-commercial.html")
print(f"2. The href of the card inserted after scape-commercial.html: {hrefs[idx1+1] if idx1 != -1 else 'Not found'}")

idx2 = find_first(hrefs, "/portfolio/data-centres/fort-data-centre-access-upgrade.html")
print(f"3. The href of the card inserted after fort-data-centre-access-upgrade.html: {hrefs[idx2+1] if idx2 != -1 else 'Not found'}")

idx3 = find_first(hrefs, "/portfolio/commercial/catholic-centre-security-partnership.html")
print(f"4. The href of the card inserted after catholic-centre-security-partnership.html: {hrefs[idx3+1] if idx3 != -1 else 'Not found'}")

print(f"5. The href of the last card in #pGrid: {hrefs[-1]}")

fyear_start = content.find('id="fYear"')
fyear_end = content.find('</select>', fyear_start)
fyear_content = content[fyear_start:fyear_end]
opts = re.findall(r'<option[^>]*>(.*?)</option>', fyear_content)
print(f"6. The options present in <select id=\"fYear\">: {opts}")
