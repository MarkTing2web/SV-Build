import os
import re
from bs4 import BeautifulSoup

REPO_ROOT     = r"C:\Projects\SV-Build"
SOLUTIONS_DIR = os.path.join(REPO_ROOT, "solutions")
SECTORS_WITH_PERSONAS = [
    "residential", "condominiums", "commercial",
    "healthcare", "managed-living"
]

def page_type(filepath):
    fname  = os.path.basename(filepath)
    parent = os.path.basename(os.path.dirname(filepath))
    if fname == "index.html" and parent == "solutions":
        return "hub"
    if parent == "solutions":
        return "sector"
    return "persona"

def process_file(filepath):
    ptype = page_type(filepath)
    is_hub = ptype == "hub"
    is_sector = ptype == "sector"
    is_persona = ptype == "persona"
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    soup = BeautifulSoup(html, "html.parser")
    modified = False

    # 1. CSS Ordering
    sheets = soup.find_all("link", rel="stylesheet")
    if sheets:
        head = soup.find("head")
        if head:
            # Remove all existing stylesheet links
            for s in sheets:
                s.extract()
            # Re-insert them in correct order: sv-shared, sv-solutions, then rest
            shared = None
            solutions = None
            rest = []
            for s in sheets:
                href = s.get("href", "")
                if href.endswith("sv-shared.css"):
                    shared = s
                elif href.endswith("sv-solutions.css"):
                    solutions = s
                else:
                    rest.append(s)
            
            # Find insertion point: usually before the first <script> or <style> in head
            target_el = head.find(["script", "style"])
            
            links_to_insert = []
            if shared: links_to_insert.append(shared)
            if solutions: links_to_insert.append(solutions)
            links_to_insert.extend(rest)
            
            if target_el:
                for lnk in links_to_insert:
                    target_el.insert_before(lnk)
                    target_el.insert_before("\n  ")
            else:
                for lnk in links_to_insert:
                    head.append(lnk)
                    head.append("\n  ")
            modified = True

    # 2. Extract <style> background-image to inline <header> (REMOVED - NOT NEEDED)

    head = soup.find("head")
    header_el = soup.find("header")

    # 3. Trust Bar in hotel and retail
    if "commercial/hotel.html" in filepath.replace("\\", "/") or "commercial/retail.html" in filepath.replace("\\", "/"):
        trust_note = soup.find(class_=re.compile(r"\bsv-trust-note\b"))
        if trust_note:
            new_trust_bar = BeautifulSoup('''<div class="trust-bar">
    <div class="container">
      <div class="trust-bar-inner">
        <span>Police Licensed</span>
        <span class="trust-divider">|</span>
        <span class="sv-bizsafe"></span>
        <span class="trust-divider">|</span>
        <span><strong class="sv-sites"></strong> Sites Protected</span>
      </div>
    </div>
  </div>''', "html.parser")
            trust_note.replace_with(new_trust_bar)
            modified = True

    # 4. Hero classes
    if header_el:
        cls_list = header_el.get("class", [])
        if is_persona:
            if "hero-standard" in cls_list:
                cls_list.remove("hero-standard")
                modified = True
            if "hero-compact" not in cls_list:
                cls_list.append("hero-compact")
                modified = True
        elif is_sector or is_hub:
            if "hero-compact" in cls_list:
                cls_list.remove("hero-compact")
                modified = True
            if "hero-standard" not in cls_list:
                cls_list.append("hero-standard")
                modified = True
        header_el["class"] = cls_list

    # 5. Heading hierarchy (H2 -> H4 skips)
    h4s = soup.find_all("h4")
    for h4 in h4s:
        # Check if it skipped h3. Simplified: just change known "What to consider:" to h3
        text = h4.get_text().strip()
        if "What to consider:" in text or "Environment Currently Secured" in text or "Intercom Not Working" in text or "Burglar Alarm Fix" in text or "Assessment" in text:
            h4.name = "h3"
            modified = True

    # 6. Sector missing .solution-personas
    if is_sector and not is_hub and os.path.basename(filepath).replace(".html", "") in SECTORS_WITH_PERSONAS:
        if not soup.find(class_=re.compile(r"\bsolution-personas\b")):
            # Find the grid containing personas, usually .sol-grid-3 or .sol-grid-4
            grids = soup.find_all(class_=re.compile(r"\bsol-grid-\d+\b|\bgrid-\d+\b"))
            for g in grids:
                if g.find("a", href=re.compile(r"/solutions/.*\.html")):
                    cls = g.get("class", [])
                    cls.append("solution-personas")
                    g["class"] = cls
                    modified = True
                    break

    # 7. Persona missing content grids
    if is_persona:
        PERSONA_CONTENT_CLASSES = [
            "pain-grid", "split-grid", "framework-grid", "framework-card",
            "problem-grid", "service-upgrade-grid", "callout-box"
        ]
        has_content = any(soup.find(class_=c) for c in PERSONA_CONTENT_CLASSES)
        if not has_content:
            # Add framework-grid to the first grid-X or sol-grid-X we find in a grey/white section
            grids = soup.find_all(class_=re.compile(r"\bsol-grid-\d+\b|\bgrid-\d+\b"))
            if grids:
                cls = grids[0].get("class", [])
                cls.append("framework-grid")
                grids[0]["class"] = cls
                modified = True

    # 8. CTA Labels
    cta = soup.find(class_=re.compile(r"\bcta-section\b"))
    if cta:
        btns = cta.find_all(class_="btn")
        for btn in btns:
            if is_persona and "Request a Proposal" not in btn.get_text():
                btn.string = "Request a Proposal"
                modified = True
            elif not is_persona and "Book a Site Assessment" not in btn.get_text():
                btn.string = "Book a Site Assessment"
                modified = True

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        return True
    return False

def main():
    file_list = []
    hub = os.path.join(SOLUTIONS_DIR, "index.html")
    if os.path.isfile(hub): file_list.append(hub)
    for fname in sorted(os.listdir(SOLUTIONS_DIR)):
        if fname.endswith(".html") and fname != "index.html":
            file_list.append(os.path.join(SOLUTIONS_DIR, fname))
    for sector in SECTORS_WITH_PERSONAS:
        sector_dir = os.path.join(SOLUTIONS_DIR, sector)
        if os.path.isdir(sector_dir):
            for fname in sorted(os.listdir(sector_dir)):
                if fname.endswith(".html"):
                    file_list.append(os.path.join(sector_dir, fname))
                    
    count = 0
    for f in file_list:
        if process_file(f):
            count += 1
            print(f"Modified: {os.path.basename(f)}")
    print(f"Total files modified: {count}")

if __name__ == "__main__":
    main()
