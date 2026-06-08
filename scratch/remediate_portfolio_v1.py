import os
import re
from bs4 import BeautifulSoup

REPO_ROOT = r"C:\Projects\SV-Build"
PORTFOLIO_DIR = os.path.join(REPO_ROOT, "portfolio")
SECTORS = [
    "commercial", "condominiums", "data-centres", "healthcare",
    "industrial", "institutions", "managed-living", "residential"
]

EXCLUDE_FILES = ["portfolio-index.html", "cpf-maxwell-institution-old.html"]

def process_file(filepath):
    filename = os.path.basename(filepath)
    if filename in EXCLUDE_FILES or filename == "index.html":
        return

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    modified = False
    
    head = soup.head
    if head:
        # A1.5, A1.6: CSS Ordering
        stylesheets = head.find_all("link", rel="stylesheet")
        sv_shared = None
        sv_portfolio = None
        for s in stylesheets:
            if s.get("href", "").endswith("sv-shared.css"):
                sv_shared = s
            elif s.get("href", "").endswith("sv-portfolio.css"):
                sv_portfolio = s
                
        if sv_shared:
            sv_shared.extract()
            head.insert(0, sv_shared)
            modified = True
        if sv_portfolio:
            sv_portfolio.extract()
            if sv_shared:
                sv_shared.insert_after(sv_portfolio)
            else:
                head.insert(1, sv_portfolio)
            modified = True

        # Ensure we insert a newline after moving for readability (optional)

        # A2.9: Extra CSS in head
        for style in head.find_all("style"):
            content = style.string or ""
            # Strip :root and hero styles
            stripped = re.sub(r'@media[^{]+\{\s*\.hero-[^\s{]+\s*\{[^}]*\}\s*\}', '', content)
            stripped = re.sub(r'\.hero-[^\s{]+\s*\{[^}]*\}', '', stripped)
            stripped = re.sub(r':root\s*\{[^}]*\}', '', stripped)
            if stripped.strip():
                # We have extra css, we should keep only the root and hero parts
                # Match @media first
                media_matches = re.findall(r'@media[^{]+\{\s*\.hero-[^\s{]+\s*\{[^}]*\}\s*\}', content)
                content_no_media = re.sub(r'@media[^{]+\{\s*\.hero-[^\s{]+\s*\{[^}]*\}\s*\}', '', content)
                hero_matches = re.findall(r'\.hero-[^\s{]+\s*\{[^}]*\}', content_no_media)
                root_matches = re.findall(r':root\s*\{[^}]*\}', content_no_media)
                
                kept_css = "\n".join(root_matches + hero_matches + media_matches)
                if kept_css.strip():
                    style.string = kept_css
                else:
                    style.extract()
                modified = True

    header_el = soup.find("header")
    
    # A4: Hero Migration
    if header_el:
        classes = header_el.get("class", [])
        if "portfolio-hero" in classes:
            classes.remove("portfolio-hero")
            if "hero" not in classes: classes.append("hero")
            if "hero-compact" not in classes: classes.append("hero-compact")
            if "hero-high-impact" not in classes: classes.append("hero-high-impact")
            # find the slug
            slug = filename.replace(".html", "")
            hero_slug = f"hero-{slug}"
            if hero_slug not in classes: classes.append(hero_slug)
            header_el["class"] = classes
            modified = True
            
            # Move inline background-image to head
            bg_match = re.search(r'background-image:\s*url\([^)]+\)', header_el.get("style", ""))
            if bg_match:
                bg = bg_match.group(0)
                # Remove from inline style
                new_style = re.sub(r'background-image:\s*url\([^)]+\)[;]?', '', header_el["style"]).strip()
                if new_style:
                    header_el["style"] = new_style
                else:
                    del header_el["style"]
                
                # Add to head
                new_style_tag = soup.new_tag("style")
                new_style_tag.string = f".{hero_slug} {{ {bg}; }}"
                head.append(new_style_tag)
        
        # Also check if it's already new hero but has inline style A4.9
        elif header_el.get("style") and "background-image" in header_el["style"]:
            slug = filename.replace(".html", "")
            hero_slug = f"hero-{slug}"
            if hero_slug not in classes: 
                classes.append(hero_slug)
                header_el["class"] = classes
                
            bg_match = re.search(r'background-image:\s*url\([^)]+\)', header_el.get("style", ""))
            if bg_match:
                bg = bg_match.group(0)
                new_style = re.sub(r'background-image:\s*url\([^)]+\)[;]?', '', header_el["style"]).strip()
                if new_style:
                    header_el["style"] = new_style
                else:
                    del header_el["style"]
                new_style_tag = soup.new_tag("style")
                new_style_tag.string = f"\n.{hero_slug} {{ {bg}; }}\n"
                head.append(new_style_tag)
            modified = True

        h1 = header_el.find("h1")
        if h1:
            classes = h1.get("class", [])
            if "portfolio-hero-title" in classes:
                h1["class"] = [c for c in classes if c != "portfolio-hero-title"]
                h1["class"].append("hero-title-main")
                modified = True
            elif "hero-title" in classes:
                h1["class"] = [c for c in classes if c != "hero-title"]
                h1["class"].append("hero-title-main")
                modified = True

    # A5: Trust bar
    for tb in soup.find_all(class_=re.compile(r"\btrust-bar\b|\bsv-trust-bar\b")):
        tb_classes = tb.get("class", [])
        if "sv-trust-bar" in tb_classes:
            tb_classes.remove("sv-trust-bar")
            if "trust-bar" not in tb_classes: tb_classes.append("trust-bar")
            tb["class"] = tb_classes
            modified = True
            
        inner = tb.find(class_=re.compile(r"trust-bar-inner|trust-flex-inline|trust-inner"))
        if inner:
            inner_classes = inner.get("class", [])
            for old_c in ["trust-flex-inline", "trust-inner"]:
                if old_c in inner_classes:
                    inner_classes.remove(old_c)
                    if "trust-bar-inner" not in inner_classes: inner_classes.append("trust-bar-inner")
                    inner["class"] = inner_classes
                    modified = True
                    
        for div_el in tb.find_all(class_=re.compile(r"\bsep\b|\bdivider\b")):
            div_classes = div_el.get("class", [])
            for old_c in ["sep", "divider"]:
                if old_c in div_classes:
                    div_classes.remove(old_c)
                    if "trust-divider" not in div_classes: div_classes.append("trust-divider")
                    div_el["class"] = div_classes
                    modified = True
    
    # A7.4: H4 to H3 if orphaned. Simple approach: turn all H4 into H3 if not in aside/nav and previous heading is H2
    headings = [h for h in soup.find_all(re.compile(r"^h[1-6]$"))
                if not any(p.name in ("aside", "nav") for p in h.parents)]
    prev_level = 0
    for h in headings:
        level = int(h.name[1])
        if level == 4 and prev_level == 2:
            h.name = "h3"
            modified = True
            prev_level = 3 # now it's H3
        else:
            prev_level = level

    # A8: Structural elements
    if not soup.find(class_="portfolio-snapshot") and not soup.find(class_="portfolio-snapshot-grid"):
        # try to find overview-split and add portfolio-snapshot to its parent section
        split = soup.find(class_=re.compile(r"overview-split|portfolio-split"))
        if split:
            parent_sec = split.find_parent("section")
            if parent_sec:
                parent_classes = parent_sec.get("class", [])
                if "portfolio-snapshot" not in parent_classes:
                    parent_classes.append("portfolio-snapshot")
                    parent_sec["class"] = parent_classes
                    modified = True
                    
    # overview table
    if not soup.find(class_="portfolio-overview-table"):
        old_table = soup.find("table", class_="overview-table")
        if old_table:
            classes = old_table.get("class", [])
            classes.remove("overview-table")
            classes.append("portfolio-overview-table")
            old_table["class"] = classes
            modified = True
        else:
            # Create a placeholder overview table and snapshot if missing
            snapshot = soup.find(class_="portfolio-snapshot")
            if not snapshot:
                snapshot = soup.new_tag("div", **{"class": "sv-section portfolio-snapshot"})
                container = soup.new_tag("div", **{"class": "container"})
                snapshot.append(container)
                # insert after hero or trust bar
                tb = soup.find(class_="trust-bar")
                if tb:
                    tb.insert_after(snapshot)
                else:
                    header_el.insert_after(snapshot)
            else:
                container = snapshot.find(class_="container") or snapshot
                
            new_table = BeautifulSoup('<table class="portfolio-overview-table"><tbody><tr><th>Sector</th><td>TBC</td></tr></tbody></table>', 'html.parser')
            container.append(new_table)
            modified = True
            
    # kicker
    if not soup.find(class_="portfolio-kicker"):
        badges = soup.find(class_=re.compile(r"hero-badges|badge-sector|portfolio-taxonomy"))
        if badges:
            if "badge-sector" in badges.get("class", []):
                badges = badges.find_parent("div")
            if badges and "portfolio-kicker" not in badges.get("class", []):
                classes = badges.get("class", [])
                classes.append("portfolio-kicker")
                badges["class"] = classes
                modified = True
                
    # Fix A2.2 and A2.5 Title and og:title
    title = soup.find("title")
    og_title = soup.find("meta", property="og:title")
    if title and title.string:
        if filename == "catholic-centre-security-partnership.html":
            title.string = "Catholic Centre — Security Singapore | Securevision"
            if og_title: og_title["content"] = title.string
            modified = True
        elif filename == "cpf-maxwell-institution-od1.html":
            title.string = "CPF Maxwell — Security Singapore | Securevision"
            if og_title: og_title["content"] = title.string
            modified = True

    # A9: Missing sv-portfolio-block
    if not soup.find(class_="sv-portfolio-block"):
        cta = soup.find(class_=re.compile(r"\bcta-section\b"))
        if cta:
            sector = os.path.basename(os.path.dirname(filepath))
            slug = filename.replace(".html", "")
            pb = soup.new_tag("div", **{
                "class": "sv-portfolio-block",
                "data-category": sector,
                "data-exclude": slug
            })
            cta.insert_before(pb)
            modified = True

    # A10.4: Hardcoded police licence
    html_str = str(soup)
    if "L/PS/000267/2023P" in html_str and "sv-licence" not in html_str:
        # We will use string replace at the end
        pass

    # A11.2: CTA label
    cta = soup.find(class_=re.compile(r"\bcta-section\b"))
    if cta:
        for a in cta.find_all("a", class_=re.compile(r"\bbtn\b")):
            if a.string and "Book Site Assessment" in a.string:
                a.string = "Request a Proposal"
                modified = True
            elif a.string and "Get Expert Advice" in a.string:
                a.string = "Request a Proposal"
                modified = True
                
        # Also A11.1 cta-high-impact
        cta_classes = cta.get("class", [])
        if "cta-high-impact" not in cta_classes:
            cta_classes.append("cta-high-impact")
            cta["class"] = cta_classes
            modified = True

    if modified or "L/PS/" in html_str:
        final_html = str(soup)
        final_html = re.sub(r'L/PS/\d+(?:/\d+[A-Z]?)?', r'<span class="sv-licence">\g<0></span>', final_html)
        # Fix formatting of link tags we moved to top of head
        final_html = final_html.replace('</link><link', '</link>\n<link').replace('</link><title>', '</link>\n<title>')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(final_html)

for sector in SECTORS:
    sdir = os.path.join(PORTFOLIO_DIR, sector)
    if os.path.isdir(sdir):
        for f in os.listdir(sdir):
            if f.endswith(".html"):
                process_file(os.path.join(sdir, f))

print("Batch remediation completed.")
