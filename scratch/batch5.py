import os
import re
from bs4 import BeautifulSoup

filepath = r"c:\Projects\SV-Build\portfolio\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
modified = False

# Fix 5A: SVG icons
for svg in soup.find_all("svg", style=lambda v: v and "width:14px" in v.replace(" ", "") and "height:14px" in v.replace(" ", "")):
    svg["class"] = svg.get("class", []) + ["portfolio-card-icon"]
    del svg["style"]
    modified = True

# Fix 5B: Tag labels
for p in soup.find_all("p", style=lambda v: v and "font-size:0.8rem" in v.replace(" ", "") and "color:#3182ce" in v.replace(" ", "")):
    p["class"] = p.get("class", []) + ["portfolio-card-tag"]
    del p["style"]
    modified = True

# Fix 5C: Hero section
for sec in soup.find_all("section", style=lambda v: v and "padding:160px" in v.replace(" ", "") and "url('/images/portfolio-hero.webp')" in v.replace(" ", "")):
    sec["class"] = sec.get("class", []) + ["portfolio-hub-hero"]
    sec["style"] = "background-image:url('/images/portfolio-hero.webp');"
    modified = True
    
    # Children of Hero
    for span in sec.find_all("span", style=lambda v: v and "color:#63b3ed" in v.replace(" ", "")):
        span["class"] = span.get("class", []) + ["portfolio-hub-eyebrow"]
        del span["style"]
        
    for h1 in sec.find_all("h1", style=lambda v: v and "Outfit" in v and "clamp(" in v):
        h1["class"] = h1.get("class", []) + ["portfolio-hub-title"]
        del h1["style"]
        
    for p in sec.find_all("p", style=lambda v: v and "font-size:1.5rem" in v.replace(" ", "") and "font-weight:600" in v.replace(" ", "")):
        p["class"] = p.get("class", []) + ["portfolio-hub-subtitle"]
        del p["style"]
        
    for p in sec.find_all("p", style=lambda v: v and "font-size:1.15rem" in v.replace(" ", "") and "opacity:0.95" in v.replace(" ", "")):
        p["class"] = p.get("class", []) + ["portfolio-hub-desc"]
        del p["style"]
        
    for div in sec.find_all("div", style=lambda v: v and "display:flex" in v.replace(" ", "") and "justify-content:flex-start" in v.replace(" ", "") and "gap:20px" in v.replace(" ", "")):
        div["class"] = div.get("class", []) + ["portfolio-hub-cta-row"]
        del div["style"]

if modified:
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
print("Batch 5 completed.")
