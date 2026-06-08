import os
import re
from bs4 import BeautifulSoup

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

def fix_trust_bar(soup):
    tb = soup.find(class_=re.compile(r"sv-trust-bar"))
    if tb:
        # Update classes
        if 'sv-trust-bar' in tb.get('class', []):
            tb['class'].remove('sv-trust-bar')
            tb['class'].append('trust-bar')
            
        inner = tb.find(class_=re.compile(r"trust-flex-inline"))
        if inner:
            if 'trust-flex-inline' in inner.get('class', []):
                inner['class'].remove('trust-flex-inline')
                inner['class'].append('trust-bar-inner')
                
            # Remove BCA Registered
            for span in inner.find_all('span', recursive=False):
                if 'BCA Registered' in span.get_text():
                    # Check if previous sibling is a divider
                    prev = span.find_previous_sibling()
                    if prev and 'trust-divider' in prev.get('class', []):
                        prev.decompose()
                    span.decompose()

            # Fix sv-sites
            for span in inner.find_all('span', recursive=False):
                if 'Sites' in span.get_text():
                    new_span = soup.new_tag("span")
                    strong = soup.new_tag("strong", attrs={"class": "sv-sites"})
                    new_span.append(strong)
                    new_span.append(" Sites Protected")
                    span.replace_with(new_span)

def strip_inline_styles(soup):
    prose = soup.find("main", class_="prose")
    if prose:
        for el in prose.find_all(style=True):
            del el['style']
            
    cta = soup.find(class_=re.compile(r"cta-section"))
    if cta:
        for el in cta.find_all(style=True):
            del el['style']

def change_article_body_tag(soup):
    ab = soup.find("section", class_="article-body")
    if ab:
        ab.name = "div"

def fix_hub():
    fpath = os.path.join(INSIGHTS_DIR, "index.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    fix_trust_bar(soup)
    
    hero = soup.find("header", class_="hero-insights")
    if hero:
        if "hero-high-impact" not in hero['class']:
            hero['class'].append("hero-high-impact")
        if "hero-standard" not in hero['class']:
            hero['class'].append("hero-standard")
            
        h1 = hero.find("h1")
        if h1 and "hero-title-main" not in h1.get('class', []):
            h1['class'] = h1.get('class', []) + ["hero-title-main"]
            
        subtitle = hero.find(class_="subtitle")
        if subtitle and "hero-subtitle-main" not in subtitle.get('class', []):
            subtitle['class'] = subtitle.get('class', []) + ["hero-subtitle-main"]

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

def fix_lpr():
    fpath = os.path.join(INSIGHTS_DIR, "lpr-vs-rfid-vehicle-access-singapore.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    fix_trust_bar(soup)
    strip_inline_styles(soup)
    change_article_body_tag(soup)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

def fix_pdpa():
    fpath = os.path.join(INSIGHTS_DIR, "pdpa-cctv-singapore.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    fix_trust_bar(soup)
    strip_inline_styles(soup)
    change_article_body_tag(soup)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

def fix_video():
    fpath = os.path.join(INSIGHTS_DIR, "video-analytics-retail-singapore.html")
    with open(fpath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    fix_trust_bar(soup)
    strip_inline_styles(soup)
    change_article_body_tag(soup)
    
    title = soup.find("title")
    if title:
        title.string = "Video Analytics for Singapore Retailers | Securevision"

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

if __name__ == "__main__":
    fix_hub()
    fix_lpr()
    fix_pdpa()
    fix_video()
    print("Done specific fixes.")
