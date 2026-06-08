import os
import re
from bs4 import BeautifulSoup

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

def remove_wa_float(soup):
    wa = soup.find(class_=re.compile(r"wa-float"))
    if wa:
        wa.decompose()

def strip_all_inline_styles(soup):
    for el in soup.find_all(style=True):
        del el['style']

def fix_index():
    fpath = os.path.join(INSIGHTS_DIR, "index.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    remove_wa_float(soup)
    
    # fix CTA button
    cta = soup.find(class_=re.compile(r"cta-section"))
    if cta:
        btn = cta.find("a", class_="btn-primary")
        if btn and "Book a Site Assessment" in btn.get_text():
            btn.string = "Request a Proposal"
            
    # B3.2 move featured-card inside articles-grid
    grid = soup.find("div", class_="articles-grid")
    wrap = soup.find("div", class_="featured-article-wrap")
    if grid and wrap:
        fc = wrap.find("a", class_=re.compile(r"featured-card"))
        if fc:
            grid.insert(0, fc)
        wrap.decompose()

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

def fix_article(filename):
    fpath = os.path.join(INSIGHTS_DIR, filename)
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    remove_wa_float(soup)
    strip_all_inline_styles(soup)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    fix_index()
    fix_article("lpr-vs-rfid-vehicle-access-singapore.html")
    fix_article("pdpa-cctv-singapore.html")
    fix_article("video-analytics-retail-singapore.html")
    print("Done more specific fixes.")
