import os
import glob
from bs4 import BeautifulSoup

base_dir = r"c:\Projects\SV-Build\systems"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    modified = False

    # Fix 3A: Two-column layout wrapper
    for div in soup.find_all("div", style=lambda v: v and "gap:48px" in v.replace(" ", "") and "align-items:start" in v.replace(" ", "")):
        div["class"] = div.get("class", []) + ["sys-two-col"]
        del div["style"]
        modified = True

    # Fix 3B: Deployment panel
    for div in soup.find_all("div", style=lambda v: v and "margin-top:64px" in v.replace(" ", "") and "padding:24px" in v.replace(" ", "")):
        div["class"] = div.get("class", []) + ["sys-deployment-panel"]
        del div["style"]
        modified = True

    # Fix 3C & 3D: Brand logo grid and items
    for grid_div in soup.find_all("div", style=lambda v: v and "gap:32px" in v.replace(" ", "") and "margin-bottom:48px" in v.replace(" ", "")):
        grid_div["class"] = grid_div.get("class", []) + ["sys-brand-grid"]
        del grid_div["style"]
        modified = True
        
        # Fix 3D: Items inside this grid
        for item_div in grid_div.find_all("div", style=lambda v: v and "margin-top:24px" in v.replace(" ", "") and len(v.replace(" ", "").split(";")) <= 2):
            item_div["class"] = item_div.get("class", []) + ["sys-brand-item"]
            del item_div["style"]

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
print("Batch 3 completed.")
