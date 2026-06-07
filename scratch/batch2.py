import os
from bs4 import BeautifulSoup

filepath = r"c:\Projects\SV-Build\brands\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
modified = False

# Fix 2A
for h3 in soup.find_all("h3", style=lambda v: v and "36px" in v):
    h3["class"] = ["brand-group-heading"]
    del h3["style"]
    modified = True

for p in soup.find_all("p", style=lambda v: v and "max-width:600px" in v.replace(" ", "")):
    p["class"] = ["brand-group-intro"]
    del p["style"]
    modified = True

for a in soup.find_all("a", style=lambda v: v and "margin-top:16px" in v.replace(" ", "")):
    a["class"] = ["btn", "btn-secondary", "brand-group-cta-link"]
    del a["style"]
    modified = True

# Fix 2B
for div in soup.find_all("div", style=lambda v: v and "border:2px solid var(--primary-blue)" in v.replace(" ", "")):
    div["class"] = ["brand-featured-card"]
    del div["style"]
    modified = True
    
for span in soup.find_all("span", style=lambda v: v and "background:var(--primary-blue)" in v.replace(" ", "")):
    span["class"] = ["brand-featured-badge"]
    del span["style"]
    modified = True

# Fix 2C
for div in soup.find_all("div", style=lambda v: v and "justify-content:center" in v.replace(" ", "") and "margin-top:40px" in v.replace(" ", "")):
    div["class"] = ["brand-group-cta-row"]
    del div["style"]
    modified = True

if modified:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
print("Batch 2 completed.")
