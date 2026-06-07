import os
import glob
from bs4 import BeautifulSoup

base_dir = r"c:\Projects\SV-Build\brands"
html_files = [f for f in glob.glob(os.path.join(base_dir, "*.html")) if not f.endswith("index.html")]

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    modified = False

    # Fix 1A: Contact / Distributor Card
    for div in soup.find_all("div", style=lambda value: value and "border-left:4px solid var(--primary-blue)" in value):
        div["class"] = ["brand-contact-card"]
        del div["style"]
        modified = True
        
        # Children
        icon_span = div.find("span", style=lambda value: value and "24px" in value)
        if icon_span:
            icon_span["class"] = ["brand-contact-icon"]
            del icon_span["style"]
            
        body_div = div.find("div", style=lambda value: value and "min-width:200px" in value.replace(" ", ""))
        if body_div:
            body_div["class"] = ["brand-contact-body"]
            del body_div["style"]
            
            name_p = body_div.find("p", style=lambda v: v and "Montserrat" in v)
            if name_p:
                name_p["class"] = ["brand-contact-name"]
                del name_p["style"]
                
            detail_p = body_div.find("p", style=lambda v: v and "Inter" in v)
            if detail_p:
                detail_p["class"] = ["brand-contact-detail"]
                del detail_p["style"]
                
        cta_a = div.find("a")
        if cta_a:
            cta_classes = cta_a.get("class", [])
            # Keep existing href and label, add classes, remove style
            new_classes = [c for c in cta_classes if c not in ["btn", "btn-primary", "brand-contact-cta"]]
            cta_a["class"] = new_classes + ["btn", "btn-primary", "brand-contact-cta"]
            if "style" in cta_a.attrs:
                del cta_a["style"]

        # Check wrapping section
        parent_section = div.find_parent("section")
        if parent_section and parent_section.get("style", "").replace(" ", "") == "padding:32px0;":
            parent_section["class"] = ["brand-contact-section"]
            del parent_section["style"]

    # Fix 1B: SECURE Integration Callout
    for div in soup.find_all("div", style=lambda value: value and "background:#0E1A2B" in value.replace(" ", "")):
        div["class"] = ["brand-integration-callout"]
        del div["style"]
        modified = True
        
        icon_div = div.find("div", style=lambda value: value and "32px" in value)
        if icon_div:
            icon_div["class"] = ["brand-integration-icon"]
            del icon_div["style"]
            
        text_container = div.find("div", style=lambda value: not value) # The other div has no style
        if text_container:
            label_p = text_container.find("p", style=lambda v: v and "Montserrat" in v)
            if label_p:
                label_p["class"] = ["brand-integration-label"]
                del label_p["style"]
            
            text_p = text_container.find("p", style=lambda v: v and "Inter" in v)
            if text_p:
                text_p["class"] = ["brand-integration-text"]
                del text_p["style"]

    # Fix 1C: Missing hero class
    heroes = soup.find_all("header")
    for hero in heroes:
        classes = hero.get("class", [])
        if "hero-compact" not in classes:
            # remove hero-high-impact if present
            if "hero-high-impact" in classes:
                classes.remove("hero-high-impact")
            # insert hero-compact right after hero- if there's another, else first
            classes.insert(0, "hero-compact")
            hero["class"] = classes
            modified = True

    if modified:
        # Save keeping original structure as much as possible, use formatter to prevent self closing tags expansion etc if possible
        # However BS4 might reformat a bit. We'll write back.
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
print("Batch 1 completed.")
