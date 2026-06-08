import os
import re
from bs4 import BeautifulSoup

REPO_ROOT = r"C:\Projects\SV-Build"
BRANDS_DIR = os.path.join(REPO_ROOT, "brands")

def get_classes(tag):
    if not tag or not tag.get("class"):
        return []
    return tag.get("class")

def add_class(tag, cls):
    classes = get_classes(tag)
    if cls not in classes:
        classes.append(cls)
        tag["class"] = classes

def remove_class(tag, cls):
    classes = get_classes(tag)
    if cls in classes:
        classes.remove(cls)
        if not classes:
            del tag["class"]
        else:
            tag["class"] = classes

def process_file(filepath):
    is_hub = os.path.basename(filepath) == "index.html"
    
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    modified = False

    # 1. CSS Ordering (sv-shared.css first, sv-brands.css second)
    head = soup.head
    if head:
        sheets = head.find_all("link", rel="stylesheet")
        if sheets:
            # Gather all stylesheets
            sheet_tags = []
            for s in sheets:
                sheet_tags.append(s.extract())
                
            shared = next((s for s in sheet_tags if "sv-shared.css" in s.get("href", "")), None)
            brands = next((s for s in sheet_tags if "sv-brands.css" in s.get("href", "")), None)
            
            others = [s for s in sheet_tags if s not in (shared, brands)]
            
            # Find insertion point (after last non-stylesheet tag before where sheets were, or at end of head)
            # Actually, easiest is to append to head, but better to put them before the first script
            first_script = head.find("script")
            
            reordered = []
            if shared: reordered.append(shared)
            if brands: reordered.append(brands)
            reordered.extend(others)
            
            if first_script:
                for s in reordered:
                    first_script.insert_before(s)
                    first_script.insert_before("\n  ")
            else:
                for s in reordered:
                    head.append(s)
                    head.append("\n  ")
            modified = True

    # 2. Extract hero background-image and clean <style> blocks
    header_el = soup.find("header")
    bg_url = None
    if head and not is_hub:
        style_tags = head.find_all("style")
        for tag in style_tags:
            text = tag.string or ""
            # Look for background-image url
            m = re.search(r'\.hero-[^\s]+\s*\{\s*background-image:\s*url\(([\'"]?)(.*?)\1\);?\s*\}', text)
            if m:
                bg_url = m.group(2)
            
            # Keep only :root
            root_match = re.search(r':root\s*\{[^}]*\}', text)
            if root_match:
                tag.string = "\n    " + root_match.group(0) + "\n  "
                modified = True
            else:
                tag.decompose()
                modified = True
                
        if bg_url and header_el:
            # Add inline style
            current_style = header_el.get("style", "")
            if "background-image" not in current_style:
                new_style = f"background-image: url('{bg_url}');"
                if current_style:
                    new_style = current_style.rstrip(";") + "; " + new_style
                header_el["style"] = new_style
                modified = True

    # 3. Trust Bar Migration
    for tb in soup.find_all(class_=re.compile(r"sv-trust-bar|trust-bar")):
        if "sv-trust-bar" in get_classes(tb):
            remove_class(tb, "sv-trust-bar")
            add_class(tb, "trust-bar")
            modified = True
        
        inner = tb.find(class_=re.compile(r"trust-flex-inline|trust-inner"))
        if inner and "trust-bar-inner" not in get_classes(inner):
            if "trust-flex-inline" in get_classes(inner): remove_class(inner, "trust-flex-inline")
            if "trust-inner" in get_classes(inner): remove_class(inner, "trust-inner")
            add_class(inner, "trust-bar-inner")
            modified = True
            
        for sep in tb.find_all(class_="sep"):
            remove_class(sep, "sep")
            add_class(sep, "trust-divider")
            modified = True
            
        # Hardcoded bizSAFE
        if "bizSAFE" in tb.get_text():
            for child in tb.children:
                if child.name == "span" and "bizsafe" in child.get_text().lower():
                    if "sv-bizsafe" not in get_classes(child):
                        child.string = ""
                        add_class(child, "sv-bizsafe")
                        modified = True
                        
        # Hardcoded sites
        for child in tb.find_all(["span", "div"]):
            text = child.get_text()
            if "sites" in text.lower() and re.search(r'\d', text):
                if not child.find("strong", class_="sv-sites"):
                    child.clear()
                    st = soup.new_tag("strong", attrs={"class": "sv-sites"})
                    child.append(st)
                    child.append(" Sites Protected")
                    modified = True

    # 4. Hero classes and rogue styles
    if header_el:
        if is_hub:
            if "hero-standard" not in get_classes(header_el):
                add_class(header_el, "hero-standard")
                modified = True
            if "hero-solid" in get_classes(header_el):
                remove_class(header_el, "hero-solid")
                modified = True
        else:
            if "hero-high-impact" in get_classes(header_el):
                remove_class(header_el, "hero-high-impact")
                modified = True
            if "hero-solid" not in get_classes(header_el):
                add_class(header_el, "hero-solid")
                modified = True
            
        # Strip inline styles from children (font/color/layout)
        # Note: we do not strip style from header_el itself
        for el in header_el.find_all(style=True):
            if el is header_el: continue
            st = el.get("style", "").lower()
            if any(k in st for k in ["color", "font-", "padding", "margin", "gap:", "display:"]):
                del el["style"]
                modified = True

    # 5. sv-brands.css v1.1 Pattern Migration
    # A9.1 Contact card
    for el in soup.find_all(style=True):
        st = el.get("style", "").lower()
        if "border-left" in st and "1.5px" in st:
            add_class(el, "brand-contact-card")
            del el["style"]
            modified = True

    # A9.2 Integration callout
    for el in soup.find_all(style=True):
        st = el.get("style", "").lower()
        if "0e1a2b" in st and "border-radius" in st:
            add_class(el, "brand-integration-callout")
            del el["style"]
            modified = True

    # A9.3 Notice box
    for el in soup.find_all(style=True):
        st = el.get("style", "").lower()
        if "fffbeb" in st:
            add_class(el, "brand-notice-box")
            del el["style"]
            modified = True

    # A9.4 Lone margin-top
    for el in soup.find_all(style=True):
        st = el.get("style", "").strip()
        m = re.match(r'^margin-top:\s*(40|32)px;?$', st, re.IGNORECASE)
        if m:
            val = m.group(1)
            add_class(el, f"mt-{val}")
            del el["style"]
            modified = True

    # 6. Content & Consistency
    bc = soup.find("nav", class_="sv-breadcrumb")
    if bc and bc.get("aria-label") != "Breadcrumb":
        bc["aria-label"] = "Breadcrumb"
        modified = True
        
        # Also check for "None" or empty aria-label, wait I just overwrote it
        # Ensure we have the second link to /brands/
        if not is_hub:
            ul = bc.find("ul")
            if ul:
                lis = ul.find_all("li")
                if len(lis) >= 2:
                    a = lis[1].find("a")
                    if a and a.get("href") != "/brands/":
                        a["href"] = "/brands/"
                        a.string = "Brands"
                        modified = True
                    elif not a:
                        a = soup.new_tag("a", href="/brands/")
                        a.string = lis[1].get_text().strip()
                        lis[1].clear()
                        lis[1].append(a)
                        modified = True

                # Make sure last item is not a link
                if len(lis) > 0:
                    last_li = lis[-1]
                    a = last_li.find("a")
                    if a:
                        text = a.get_text()
                        last_li.clear()
                        last_li.append(text)
                        modified = True

    # CTA section fixes
    cta = soup.find(class_=re.compile(r"\bcta-section\b"))
    if cta:
        if "cta-high-impact" not in get_classes(cta):
            add_class(cta, "cta-high-impact")
            modified = True
        
        btns = cta.find_all("a", class_="btn")
        for btn in btns:
            if "request a demo" in btn.get_text().lower() or "request a quote" in btn.get_text().lower():
                btn.string = "Request a Proposal"
                modified = True

        for el in cta.find_all(style=True):
            del el["style"]
            modified = True

    # WhatsApp floats
    wa_floats = soup.find_all(class_=re.compile(r"\bwa-float\b"))
    for w in wa_floats:
        w.decompose()
        modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        return True
    return False

if __name__ == "__main__":
    count = 0
    for f in os.listdir(BRANDS_DIR):
        if f.endswith(".html"):
            path = os.path.join(BRANDS_DIR, f)
            if process_file(path):
                count += 1
                print(f"Modified: {f}")
    print(f"Total files modified: {count}")
