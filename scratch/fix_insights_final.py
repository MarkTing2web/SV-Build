import os
import re
from bs4 import BeautifulSoup

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

def fix_why_security():
    fpath = os.path.join(INSIGHTS_DIR, "why-security-needs-managed-network.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    main = soup.find("main")
    if main and "prose" not in main.get("class", []):
        classes = main.get("class", [])
        classes.append("prose")
        main["class"] = classes
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

def fix_managing():
    fpath = os.path.join(INSIGHTS_DIR, "managing-multiple-estates-with-vesta.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    authors = soup.find_all(id="author")
    if len(authors) > 1:
        # Keep the section one, remove the div one
        for a in authors:
            if a.name == "div":
                a.decompose()
                
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

def fix_index():
    fpath = os.path.join(INSIGHTS_DIR, "index.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    # fix A5.6 and A5.7 in index
    trust_bar = soup.find("div", class_="trust-bar-inner")
    if trust_bar:
        # Re-build the trust bar correctly
        trust_bar.clear()
        span1 = soup.new_tag("span")
        span1.string = "Police Licensed · "
        lic = soup.new_tag("span", class_="sv-licence")
        span1.append(lic)
        
        div1 = soup.new_tag("span", class_="trust-divider")
        
        span2 = soup.new_tag("span")
        span2.string = "bizSAFE "
        biz = soup.new_tag("span", class_="sv-bizsafe")
        span2.append(biz)
        
        div2 = soup.new_tag("span", class_="trust-divider")
        
        span3 = soup.new_tag("span")
        strong = soup.new_tag("strong", class_="sv-sites")
        span3.append(strong)
        span3.append(" Sites Protected")
        
        trust_bar.append(span1)
        trust_bar.append(div1)
        trust_bar.append(span2)
        trust_bar.append(div2)
        trust_bar.append(span3)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    fix_why_security()
    fix_managing()
    fix_index()
    print("Final structural fixes done.")
