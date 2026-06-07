import os
from bs4 import BeautifulSoup

filepath = r"c:\Projects\SV-Build\systems\network-infrastructure.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
modified = False

# Fix 4A
for div in soup.find_all("div", style=lambda v: v and "padding:32px 40px" in v.replace(" ", "") and "text-align:center" in v.replace(" ", "")):
    div["class"] = div.get("class", []) + ["net-stat-card"]
    del div["style"]
    modified = True
    
    # Children
    for child in div.find_all(recursive=False):
        style = child.get("style", "").replace(" ", "")
        if child.name == "p" and "max-width:640px" in style:
            child["class"] = child.get("class", []) + ["net-stat-card-intro"]
            del child["style"]
        elif child.name == "div" and "font-size:32px" in style:
            child.name = "span"
            child["class"] = child.get("class", []) + ["net-stat-icon"]
            del child["style"]
        elif child.name == "p" and "uppercase" in style:
            child.name = "span"
            child["class"] = child.get("class", []) + ["net-stat-eyebrow"]
            del child["style"]
        elif child.name == "div" and "font-size:28px" in style:
            child.name = "span"
            child["class"] = child.get("class", []) + ["net-stat-value"]
            del child["style"]
        elif child.name == "p" and "Montserrat" in child.get("style", "") and "font-weight:700" in style and "color:var(--text-dark)" in style:
            child.name = "span"
            child["class"] = child.get("class", []) + ["net-stat-label"]
            del child["style"]
        elif child.name == "p" and "font-size:13px" in style and "color:var(--text-gray)" in style:
            child["class"] = child.get("class", []) + ["net-stat-desc"]
            del child["style"]

# Fix 4B
for a in soup.find_all("a", style=lambda v: v and "align-self:start" in v.replace(" ", "")):
    classes = a.get("class", [])
    if "btn" not in classes: classes.append("btn")
    if "btn-secondary" not in classes: classes.append("btn-secondary")
    a["class"] = classes
    del a["style"]
    modified = True

# Fix 4C
for sec in soup.find_all("section", style=lambda v: v and "padding:64px 0" in v.replace(" ", "")):
    style = sec.get("style", "").replace(" ", "")
    classes = sec.get("class", [])
    if "background:var(--bg-light)" in style or "background:#f8f9fa" in style.lower() or "background:#eef2f7" in style.lower() or "background:#f0f2f5" in style.lower():
        classes.append("sv-section-grey")
    else:
        # Default to white if no background was explicitly grey
        classes.append("sv-section-white")
    sec["class"] = classes
    del sec["style"]
    modified = True

if modified:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
print("Batch 4 completed.")
