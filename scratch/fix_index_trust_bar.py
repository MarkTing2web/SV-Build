import os
from bs4 import BeautifulSoup

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

def fix_index_trust_bar():
    fpath = os.path.join(INSIGHTS_DIR, "index.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    trust_bar = soup.find("div", class_="trust-bar-inner")
    if trust_bar:
        # Re-build carefully.
        trust_bar.clear()
        span1 = soup.new_tag("span")
        span1.string = "Police Licensed · "
        lic = soup.new_tag("span", attrs={"class": "sv-licence"})
        span1.append(lic)
        
        div1 = soup.new_tag("span", attrs={"class": "trust-divider"})
        
        span2 = soup.new_tag("span")
        span2.string = "bizSAFE "
        biz = soup.new_tag("span", attrs={"class": "sv-bizsafe"})
        span2.append(biz)
        
        div2 = soup.new_tag("span", attrs={"class": "trust-divider"})
        
        span3 = soup.new_tag("span")
        strong = soup.new_tag("strong", attrs={"class": "sv-sites"})
        span3.append(strong)
        span3.append(" Sites Protected")
        
        trust_bar.append(span1)
        trust_bar.append(div1)
        trust_bar.append(span2)
        trust_bar.append(div2)
        trust_bar.append(span3)
                
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Fixed index.html trust bar class_ issue.")

if __name__ == "__main__":
    fix_index_trust_bar()
