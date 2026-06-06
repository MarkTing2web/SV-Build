import re

# TASK A
p1 = r'c:\Projects\SV-Build\portfolio\data-centres\fort-st-engineering.html'
with open(p1, 'r', encoding='utf-8') as f:
    c1 = f.read()

c1 = c1.replace('<span class="badge badge-primary">COMMERCIAL CASE STUDY</span>', '<span class="badge badge-primary">DATA CENTRE CASE STUDY</span>')

with open(p1, 'w', encoding='utf-8') as f:
    f.write(c1)

# TASK B
p2 = r'c:\Projects\SV-Build\portfolio\index.html'
with open(p2, 'r', encoding='utf-8') as f:
    c2 = f.read()

# We need to find the card with href="/portfolio/data-centres/fort-data-centre-access-upgrade.html"
# and change its data-prop="Industrial" to "Data Centres"
pattern = r'(<a href="/portfolio/data-centres/fort-data-centre-access-upgrade\.html"[^>]*?data-prop=")Industrial(")'
c2 = re.sub(pattern, r'\1Data Centres\2', c2)

with open(p2, 'w', encoding='utf-8') as f:
    f.write(c2)

print("Tasks done.")
