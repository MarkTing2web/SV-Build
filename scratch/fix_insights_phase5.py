import os
import glob
import re
from bs4 import BeautifulSoup

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

def clean_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    changed = False

    # 1. Strip Google Fonts
    for link in soup.find_all("link", rel="stylesheet"):
        href = link.get("href", "")
        if "fonts.googleapis.com" in href:
            link.decompose()
            changed = True

    # Also remove the preconnects for google fonts to be clean
    for link in soup.find_all("link", rel="preconnect"):
        href = link.get("href", "")
        if "fonts.googleapis.com" in href or "fonts.gstatic.com" in href:
            link.decompose()
            changed = True

    # 2. Remove wa-float
    for wa in soup.find_all("a", class_=re.compile(r"wa-float")):
        wa.decompose()
        changed = True

    # 3. Strip all inline styles
    for el in soup.find_all(style=True):
        del el['style']
        changed = True

    # 4. Remove any <style> tags
    for style_tag in soup.find_all("style"):
        style_tag.decompose()
        changed = True

    if changed:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(str(soup))

if __name__ == "__main__":
    for fpath in glob.glob(os.path.join(INSIGHTS_DIR, "*.html")):
        clean_file(fpath)
    print("Phase 5 cleanup completed.")
