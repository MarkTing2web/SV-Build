import os
import glob
from bs4 import BeautifulSoup

base_dir = r"c:\Projects\SV-Build\portfolio"
html_files = glob.glob(os.path.join(base_dir, "*", "*.html"))

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    modified = False

    # Fix 6A
    for div in soup.find_all("div", style=lambda v: v and "grid-template-columns:1fr 1fr" in v.replace(" ", "") and "gap:64px" in v.replace(" ", "")):
        div["class"] = div.get("class", []) + ["portfolio-overview-grid"]
        del div["style"]
        modified = True

    # Fix 6B
    for div in soup.find_all("div", style=lambda v: v and "flex-direction:column" in v.replace(" ", "") and "gap:12px" in v.replace(" ", "")):
        div["class"] = div.get("class", []) + ["portfolio-systems-list"]
        del div["style"]
        modified = True

    # Fix 6C
    for a in soup.find_all("a", style=lambda v: v and "padding:16px 20px" in v.replace(" ", "") and "background:var(--bg-light)" in v.replace(" ", "")):
        a["class"] = a.get("class", []) + ["portfolio-system-link"]
        del a["style"]
        if "onmouseover" in a.attrs: del a["onmouseover"]
        if "onmouseout" in a.attrs: del a["onmouseout"]
        modified = True

    # Fix 6D
    for div in soup.find_all("div", style=lambda v: v and "grid-template-columns:repeat(3,1fr)" in v.replace(" ", "") and "gap:28px" in v.replace(" ", "")):
        div["class"] = div.get("class", []) + ["portfolio-result-grid"]
        del div["style"]
        modified = True

    # Fix 6E
    for div in soup.find_all("div", style=lambda v: v and "font-size:48px" in v.replace(" ", "") and "font-weight:800" in v.replace(" ", "")):
        div["class"] = div.get("class", []) + ["portfolio-result-stat"]
        del div["style"]
        modified = True

    # Fix 6F
    for a in soup.find_all("a", style=lambda v: v and "display:block" in v.replace(" ", "") and "text-decoration:none" in v.replace(" ", "")):
        # Wait, checking if it is specifically the related link...
        # Just check the parent or if it has this exact style.
        if v.replace(" ", "") == "display:block;text-decoration:none;" or v.replace(" ", "") == "display:block;text-decoration:none":
            a["class"] = a.get("class", []) + ["portfolio-related-link"]
            del a["style"]
            modified = True

    # Fix 6G
    for span in soup.find_all("span", style=lambda v: v and "color:var(--primary-blue)" in v.replace(" ", "") and "font-size:13px" in v.replace(" ", "") and "margin-top:16px" in v.replace(" ", "")):
        span["class"] = span.get("class", []) + ["portfolio-read-more"]
        del span["style"]
        modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
print("Batch 6 completed.")
