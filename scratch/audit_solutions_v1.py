"""
audit_solutions_v1.py — Securevision Solutions Section Audit Script
Scope:
  TYPE A — /solutions/index.html               (solutions hub — unique, structural checks only)
  TYPE B — /solutions/[sector].html            (8 sector hub pages)
  TYPE C — /solutions/[sector]/[persona].html  (persona sub-pages in sector subdirs)

Action: READ ONLY — no file modifications. Produces markdown report.
Run:    python audit_solutions_v1.py
Output: solutions-audit-report-v1.md (set OUT_FILE below)

KEY DIFFERENCES FROM OTHER SECTIONS:
  - CSS: sv-solutions.css loaded second (not sv-brands.css, sv-insights.css etc.)
  - Hero: hero-high-impact + hero-[sector] for TYPE B
          hero-high-impact + hero-[persona] for TYPE C
          hero-standard on the solutions/index.html hub
  - CTA label DIFFERS by type:
      TYPE A + TYPE B (hub/sector) → "Book a Site Assessment"
      TYPE C (persona sub-pages)   → "Request a Proposal"
  - Inline exceptions:
      stat-bar-fill: ONLY style="width:X%;" is permitted (bar width)
      All other inline styles flagged
  - sv-section-dark: background:#2d4a6b now has CSS class — flag if inline
  - TYPE B sector hubs expect .solution-personas grid
  - TYPE C persona pages expect .pain-grid OR .split-grid OR .framework-grid
  - solutions/index.html: EXCLUDED from section-specific structural checks
  - systems-block.js may be loaded on solutions/index.html — not required on others
"""

import os
import re
from bs4 import BeautifulSoup
from collections import defaultdict

# ─── CONFIGURE PATHS ─────────────────────────────────────────────────────────
REPO_ROOT     = r"C:\Projects\SV-Build"
OUT_FILE      = r"C:\Projects\SV-Build\solutions-audit-report-v1.md"
# ─────────────────────────────────────────────────────────────────────────────

SOLUTIONS_DIR = os.path.join(REPO_ROOT, "solutions")

# Sector subdirectories that contain persona sub-pages
SECTORS_WITH_PERSONAS = [
    "residential", "condominiums", "commercial",
    "healthcare", "managed-living"
]

SEVERITIES = {
    "A1.1": "BLOCKER", "A1.2": "BLOCKER", "A1.3": "BLOCKER", "A1.4": "BLOCKER",
    "A1.5": "BLOCKER", "A1.6": "BLOCKER", "A1.7": "MAJOR",   "A1.8": "MAJOR",
    "A2.1": "BLOCKER", "A2.2": "MAJOR",   "A2.3": "MINOR",   "A2.4": "BLOCKER",
    "A2.5": "MAJOR",   "A2.6": "MINOR",   "A2.7": "BLOCKER", "A2.8": "BLOCKER",
    "A2.9": "MAJOR",
    "A3.1": "BLOCKER", "A3.2": "BLOCKER", "A3.3": "BLOCKER", "A3.4": "BLOCKER",
    "A3.7": "BLOCKER", "A3.8": "BLOCKER",
    "A4.1": "MAJOR",   "A4.2": "MAJOR",   "A4.3": "BLOCKER", "A4.4": "MAJOR",
    "A4.5": "MAJOR",
    "A5.1": "MAJOR",   "A5.2": "MAJOR",   "A5.3": "MAJOR",   "A5.4": "MAJOR",
    "A5.5": "MAJOR",   "A5.6": "MAJOR",   "A5.7": "MAJOR",   "A5.8": "MAJOR",
    "A6.1": "MAJOR",   "A6.2": "MINOR",   "A6.3": "MAJOR",   "A6.4": "MAJOR",
    "A6.5": "MINOR",
    "A7.1": "BLOCKER", "A7.4": "MAJOR",
    # Structural body checks
    "A8.1": "MAJOR",   "A8.2": "MAJOR",
    # CTA
    "A9.1": "MAJOR",   "A9.2": "MAJOR",   "A9.3": "MINOR",
    "A9.4": "MINOR",   "A9.5": "MAJOR",
    # Dynamic values
    "A10.1": "MAJOR",  "A10.2": "MAJOR",  "A10.3": "MAJOR",
    "A10.4": "MAJOR",  "A10.5": "MINOR",
    # Images & links
    "A11.1": "BLOCKER","A11.2": "MAJOR",  "A11.3": "MINOR",  "A11.4": "BLOCKER",
    "A11.5": "MAJOR",  "A11.6": "MAJOR",
    # Inline styles
    "A12.1": "BLOCKER","A12.2": "MAJOR",  "A12.3": "MAJOR",
    # Inline migration checks
    "A13.1": "MAJOR",
    # Accessibility
    "A14.1": "BLOCKER","A14.2": "MAJOR",  "A14.4": "MINOR",
}

all_issues  = []
file_issues = defaultdict(list)
summary     = defaultdict(lambda: {"files": set(), "count": 0, "desc": defaultdict(int)})


def rel_path(filepath):
    norm = filepath.replace("\\", "/")
    idx  = norm.find("/solutions/")
    return norm[idx:] if idx >= 0 else "/" + os.path.basename(filepath)


def add_issue(filepath, check_id, desc):
    sev = SEVERITIES.get(check_id, "MINOR")
    rp  = rel_path(filepath)
    row = f"| {rp} | {check_id} | {desc} | {sev} |"
    all_issues.append(row)
    file_issues[rp].append(check_id)
    cat = check_id.split(".")[0]
    summary[cat]["files"].add(rp)
    summary[cat]["count"] += 1
    summary[cat]["desc"][desc] += 1


def get_classes(tag):
    return tag.get("class") or [] if tag else []


def has_class(tag, cls):
    return cls in get_classes(tag)


def page_type(filepath):
    """Return 'hub', 'sector', or 'persona'."""
    fname  = os.path.basename(filepath)
    parent = os.path.basename(os.path.dirname(filepath))
    if fname == "index.html" and parent == "solutions":
        return "hub"
    if parent == "solutions":
        return "sector"
    return "persona"


def check_file(filepath):
    ptype     = page_type(filepath)
    is_hub    = ptype == "hub"
    is_sector = ptype == "sector"
    is_persona = ptype == "persona"

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    soup      = BeautifulSoup(html, "html.parser")
    head      = soup.head or soup
    body      = soup.body or soup
    scripts   = soup.find_all("script")
    sheets    = soup.find_all("link", rel="stylesheet")
    header_el = soup.find("header")

    # ══════════════════════════════════════════════════════════════════════════
    # A1. INFRASTRUCTURE
    # ══════════════════════════════════════════════════════════════════════════

    nav_el = soup.find("nav", id="sv-nav")
    if not nav_el:
        add_issue(filepath, "A1.1", "Missing <nav id='sv-nav'>")
    elif nav_el.find_all(recursive=False):
        add_issue(filepath, "A1.1", "Hardcoded nav HTML inside <nav id='sv-nav'>")

    footer_el = soup.find("footer", id="sv-footer")
    if not footer_el:
        add_issue(filepath, "A1.2", "Missing <footer id='sv-footer'>")
    elif footer_el.find_all(recursive=False):
        add_issue(filepath, "A1.2", "Hardcoded footer HTML inside <footer id='sv-footer'>")

    body_scripts = body.find_all("script") if soup.body else scripts
    if not body_scripts or not body_scripts[-1].get("src", "").endswith("nav-footer.js"):
        add_issue(filepath, "A1.3", "nav-footer.js is not the LAST script before </body>")

    head_scripts = head.find_all("script")
    if not any(s.get("src", "").endswith("site-config.js") for s in head_scripts):
        add_issue(filepath, "A1.4", "site-config.js not loaded in <head>")

    if not sheets or not sheets[0].get("href", "").endswith("sv-shared.css"):
        add_issue(filepath, "A1.5", "sv-shared.css is not loaded FIRST in stylesheet list")

    sol_css_idx = next(
        (i for i, s in enumerate(sheets) if s.get("href", "").endswith("sv-solutions.css")),
        None
    )
    if sol_css_idx is None:
        add_issue(filepath, "A1.6", "sv-solutions.css not loaded")
    elif sol_css_idx != 1:
        add_issue(filepath, "A1.6", f"sv-solutions.css loaded at position {sol_css_idx+1}, expected position 2")

    for s in sheets:
        href = s.get("href", "")
        if any(x in href for x in ("sv-systems", "sv-brands", "sv-insights", "sv-resources", "sv-portfolio")):
            add_issue(filepath, "A1.7", f"Wrong section CSS loaded: {href}")

    wa_float = soup.find(class_=re.compile(r"\bwa-float\b"))
    if wa_float:
        add_issue(filepath, "A1.8", "WhatsApp float hardcoded (wa-float in HTML — injected by nav-footer.js)")

    # ══════════════════════════════════════════════════════════════════════════
    # A2. HEAD / SEO
    # ══════════════════════════════════════════════════════════════════════════

    html_tag = soup.find("html")
    if not html_tag or html_tag.get("lang") != "en-GB":
        add_issue(filepath, "A2.1", f"<html lang> is '{html_tag.get('lang') if html_tag else 'missing'}', expected 'en-GB'")

    title_tag  = soup.find("title")
    title_text = title_tag.get_text().strip() if title_tag else ""
    tl = len(title_text)
    if not title_text:
        add_issue(filepath, "A2.2", "Missing <title>")
    else:
        issues = []
        if tl < 50: issues.append(f"too short ({tl} chars, min 50)")
        if tl > 60: issues.append(f"too long ({tl} chars, max 60)")
        if "Singapore" not in title_text: issues.append("missing 'Singapore'")
        if issues:
            add_issue(filepath, "A2.2", "Title: " + "; ".join(issues))

    desc_meta    = soup.find("meta", attrs={"name": "description"})
    desc_content = (desc_meta.get("content") or "").strip() if desc_meta else ""
    dl = len(desc_content)
    if not desc_content:
        add_issue(filepath, "A2.3", "Missing meta description")
    elif dl < 120 or dl > 160:
        add_issue(filepath, "A2.3", f"Meta description {dl} chars (expected 120–160)")

    canon     = soup.find("link", rel="canonical")
    canon_url = (canon.get("href") or "").strip() if canon else ""
    if not canon_url:
        add_issue(filepath, "A2.4", "Missing <link rel='canonical'>")
    elif not canon_url.startswith("https://www.securevision.com.sg"):
        add_issue(filepath, "A2.4", f"Canonical not absolute securevision.com.sg URL: {canon_url}")

    og_title_val = ((soup.find("meta", property="og:title") or {}).get("content") or "").strip()
    if not og_title_val:
        add_issue(filepath, "A2.5", "og:title missing")
    elif og_title_val != title_text:
        add_issue(filepath, "A2.5", "og:title does not match <title>")

    og_desc_val = ((soup.find("meta", property="og:description") or {}).get("content") or "").strip()
    if not og_desc_val:
        add_issue(filepath, "A2.6", "og:description missing")
    elif og_desc_val != desc_content:
        add_issue(filepath, "A2.6", "og:description does not match meta description")

    og_img_val = ((soup.find("meta", property="og:image") or {}).get("content") or "").strip()
    if not og_img_val:
        add_issue(filepath, "A2.7", "og:image missing")
    elif not og_img_val.startswith("https://"):
        add_issue(filepath, "A2.7", f"og:image not absolute HTTPS URL: {og_img_val[:60]}")

    og_url_val = ((soup.find("meta", property="og:url") or {}).get("content") or "").strip()
    if not og_url_val:
        add_issue(filepath, "A2.8", "og:url missing")
    elif not og_url_val.startswith("https://"):
        add_issue(filepath, "A2.8", "og:url not absolute HTTPS URL")
    elif canon_url and og_url_val != canon_url:
        add_issue(filepath, "A2.8", "og:url does not match canonical")

    for sb in head.find_all("style"):
        sb_text = sb.get_text().strip()
        if not sb_text:
            continue
        stripped = re.sub(r':root\s*\{[^}]*\}', '', sb_text)
        stripped = re.sub(r'@media[^{]+\{\s*\.hero-[^\s{]+\s*\{[^}]*\}\s*\}', '', stripped)
        stripped = re.sub(r'\.hero-[^\s{]+\s*\{[^}]*\}', '', stripped)
        stripped = re.sub(r'@media[^{]+\{\s*\}', '', stripped)
        stripped = stripped.strip()
        if stripped:
            add_issue(filepath, "A2.9", "Extra CSS in <head> <style> block beyond :root accent variable and hero images")
            break

    # ══════════════════════════════════════════════════════════════════════════
    # A3. PAGE STRUCTURE
    # ══════════════════════════════════════════════════════════════════════════

    if not soup.find("nav", id="sv-nav"):
        add_issue(filepath, "A3.1", "Nav placeholder missing")
    if not header_el:
        add_issue(filepath, "A3.2", "No <header> element found")
    if not soup.find(class_=re.compile(r"\btrust-bar\b|\bsv-trust-bar\b")):
        add_issue(filepath, "A3.3", "Trust bar missing")
    if not soup.find("nav", class_=re.compile(r"sv-breadcrumb")):
        add_issue(filepath, "A3.4", "Breadcrumb nav missing")
    if not soup.find(class_=re.compile(r"\bcta-section\b")):
        add_issue(filepath, "A3.7", "CTA section missing")
    if not soup.find("footer", id="sv-footer"):
        add_issue(filepath, "A3.8", "Footer placeholder missing")

    # ══════════════════════════════════════════════════════════════════════════
    # A4. HERO
    # Sector hubs: hero-high-impact hero-standard hero-[sector]
    # Persona pages: hero-high-impact hero-compact hero-[persona] (or just hero-high-impact)
    # Hub (index): hero-high-impact hero-standard
    # ══════════════════════════════════════════════════════════════════════════

    if header_el:
        cls_str = " ".join(get_classes(header_el))

        if "hero-high-impact" not in cls_str:
            add_issue(filepath, "A4.1", f"Hero missing hero-high-impact class — classes: {cls_str[:80]}")

        if is_hub or is_sector:
            if "hero-standard" not in cls_str:
                add_issue(filepath, "A4.2", "Sector/hub hero missing hero-standard class (should be 65vh)")
        elif is_persona:
            if "hero-compact" not in cls_str:
                add_issue(filepath, "A4.2", "Persona hero missing hero-compact class (should be 52vh)")

        if is_sector:
            has_sector_cls = any(c.startswith("hero-") and c not in ("hero-high-impact", "hero-standard", "hero-compact", "hero-solid") for c in cls_str.split())
            if not has_sector_cls:
                add_issue(filepath, "A4.5", f"Sector hub hero missing sector class (hero-[sector]) — classes: {cls_str}")

        if is_persona:
            has_persona_cls = any(c.startswith("hero-") and c not in ("hero-high-impact", "hero-standard", "hero-compact", "hero-solid") for c in cls_str.split())
            parent_sector = os.path.basename(os.path.dirname(filepath))
            if not has_persona_cls and parent_sector != "residential":
                add_issue(filepath, "A4.5", f"Persona hero missing persona class (hero-[persona]) — classes: {cls_str}")

        h1s = soup.find_all("h1")
        if len(h1s) != 1:
            add_issue(filepath, "A4.3", f"Page has {len(h1s)} H1 elements — exactly 1 required")
        else:
            if not has_class(h1s[0], "hero-title-main"):
                add_issue(filepath, "A4.4", f"H1 missing hero-title-main class — classes: {' '.join(get_classes(h1s[0]))}")

    # ══════════════════════════════════════════════════════════════════════════
    # A5. TRUST BAR
    # ══════════════════════════════════════════════════════════════════════════

    tb = soup.find(class_=re.compile(r"\btrust-bar\b|\bsv-trust-bar\b"))
    if not tb:
        add_issue(filepath, "A5.4", "Trust bar element not found")
    else:
        if "sv-trust-bar" in get_classes(tb) and "trust-bar" not in get_classes(tb):
            add_issue(filepath, "A5.1", "Trust bar outer uses legacy sv-trust-bar — migrate to trust-bar")

        inner = tb.find(class_=re.compile(r"trust-bar-inner|trust-flex-inline|trust-inner"))
        if not inner:
            add_issue(filepath, "A5.2", "Trust bar inner wrapper missing (expected trust-bar-inner)")
        elif "trust-bar-inner" not in get_classes(inner):
            old = next((c for c in get_classes(inner) if c in ("trust-flex-inline", "trust-inner")), "unknown")
            add_issue(filepath, "A5.2", f"Trust bar inner uses legacy {old} — migrate to trust-bar-inner")

        for div_el in tb.find_all(class_=re.compile(r"\bsep\b|\bdivider\b")):
            if "trust-divider" not in get_classes(div_el):
                add_issue(filepath, "A5.3", "Divider uses legacy class — migrate to trust-divider")

        if "bca registered" in tb.get_text(separator=" ").lower():
            add_issue(filepath, "A5.5", "BCA Registered in trust bar (belongs in footer only)")

        if re.search(r'Level\s*3', str(tb)) and "sv-bizsafe" not in str(tb):
            add_issue(filepath, "A5.6", "bizSAFE level appears hardcoded (no sv-bizsafe class)")

        if not tb.find("strong", class_="sv-sites"):
            add_issue(filepath, "A5.7", "Sites count missing <strong class='sv-sites'>")

        if re.search(r"L/[A-Z0-9/]+", tb.get_text()):
            add_issue(filepath, "A5.8", "Hardcoded police licence number in trust bar")

    # ══════════════════════════════════════════════════════════════════════════
    # A6. BREADCRUMB
    # ══════════════════════════════════════════════════════════════════════════

    bc = soup.find("nav", class_="sv-breadcrumb")
    if not bc:
        add_issue(filepath, "A6.1", "Breadcrumb missing or not using class sv-breadcrumb")
    else:
        if bc.get("aria-label") != "Breadcrumb":
            add_issue(filepath, "A6.2", f"aria-label is '{bc.get('aria-label')}', expected 'Breadcrumb'")

        bc_links = bc.find_all("a")
        if not bc_links:
            add_issue(filepath, "A6.3", "Breadcrumb has no links")
        else:
            if bc_links[0].get("href") != "/":
                add_issue(filepath, "A6.3", f"First breadcrumb link is '{bc_links[0].get('href')}', expected '/'")
            # Sector hubs and persona pages both need /solutions/ as second crumb
            if not is_hub:
                if len(bc_links) < 2:
                    add_issue(filepath, "A6.4", "Breadcrumb missing second link to /solutions/")
                elif bc_links[1].get("href") not in ("/solutions/", "/solutions/index.html"):
                    add_issue(filepath, "A6.4", f"Second crumb is '{bc_links[1].get('href')}', expected '/solutions/'")

        bc_text_els = bc.find_all(["li", "span", "a"])
        if bc_text_els and bc_text_els[-1].name == "a":
            add_issue(filepath, "A6.5", "Last breadcrumb item is a link — should be plain text")

    # ══════════════════════════════════════════════════════════════════════════
    # A7. HEADING HIERARCHY
    # ══════════════════════════════════════════════════════════════════════════

    all_h1 = soup.find_all("h1")
    if len(all_h1) != 1:
        add_issue(filepath, "A7.1", f"Page has {len(all_h1)} H1 elements — exactly 1 required")

    headings   = [h for h in soup.find_all(re.compile(r"^h[1-6]$"))
                  if not any(p.name in ("aside", "nav") for p in h.parents)]
    prev_level = 0
    for hx in headings:
        level = int(hx.name[1])
        if level > prev_level + 1 and prev_level != 0:
            add_issue(filepath, "A7.4", f"Heading level skipped: H{prev_level} → H{level} ('{hx.get_text()[:40]}')")
        prev_level = level

    # ══════════════════════════════════════════════════════════════════════════
    # A8. SECTION-SPECIFIC BODY STRUCTURE
    # ══════════════════════════════════════════════════════════════════════════

    if is_sector and not is_hub:
        # Sector hubs must have a persona links grid
        is_true_sector = os.path.basename(filepath).replace(".html", "") in SECTORS_WITH_PERSONAS
        if is_true_sector and not soup.find(class_=re.compile(r"\bsolution-personas\b")):
            add_issue(filepath, "A8.1", "Sector hub missing .solution-personas grid")

    if is_persona:
        # Persona pages must have at least one of the core content grids
        PERSONA_CONTENT_CLASSES = [
            "pain-grid", "split-grid", "framework-grid", "framework-card",
            "problem-grid", "service-upgrade-grid", "callout-box"
        ]
        has_content = any(soup.find(class_=c) for c in PERSONA_CONTENT_CLASSES)
        if not has_content:
            add_issue(filepath, "A8.2",
                      f"Persona page missing expected content grid — none of: {', '.join('.' + c for c in PERSONA_CONTENT_CLASSES)}")

    # ══════════════════════════════════════════════════════════════════════════
    # A9. CTA SECTION
    # CTA label differs by page type:
    #   hub + sector → "Book a Site Assessment"
    #   persona      → "Request a Proposal"
    # ══════════════════════════════════════════════════════════════════════════

    cta = soup.find(class_=re.compile(r"\bcta-section\b"))
    if not cta:
        add_issue(filepath, "A9.1", "cta-section not found")
    else:
        if "cta-high-impact" not in get_classes(cta):
            add_issue(filepath, "A9.1", "CTA missing cta-high-impact class")

        cta_btns = cta.find_all(class_=re.compile(r"\bbtn\b"))
        if cta_btns:
            btn_text = " ".join(b.get_text().lower() for b in cta_btns)
            if is_persona:
                if "request a proposal" not in btn_text:
                    labels = " / ".join(b.get_text().strip() for b in cta_btns)
                    add_issue(filepath, "A9.2", f"Persona CTA label is not 'Request a Proposal' — found: {labels[:80]}")
            else:
                if "book" not in btn_text or "assessment" not in btn_text:
                    labels = " / ".join(b.get_text().strip() for b in cta_btns)
                    add_issue(filepath, "A9.2", f"Sector/hub CTA label is not 'Book a Site Assessment' — found: {labels[:80]}")

        if not cta.find("h2"):
            add_issue(filepath, "A9.3", "H2 missing inside CTA section")

        sub = cta.find(class_="subtitle")
        if sub and sub.get("style"):
            add_issue(filepath, "A9.4", "CTA subtitle has inline style")

        for el in cta.find_all(style=True):
            add_issue(filepath, "A9.5", f"Inline style on <{el.name}> inside CTA section")
            break

    # ══════════════════════════════════════════════════════════════════════════
    # A10. DYNAMIC VALUES
    # ══════════════════════════════════════════════════════════════════════════

    html_lower = html.lower()
    if re.search(r'\b(20|1[5-9])\s*years?\s+in\s+business', html_lower) and "sv-years-business" not in html:
        add_issue(filepath, "A10.1", "sv-years-business appears hardcoded")
    if re.search(r'\b(30|3[0-9]|4[0-9])\s*years?\s+(of\s+)?experience', html_lower) and "sv-years-experience" not in html:
        add_issue(filepath, "A10.2", "sv-years-experience appears hardcoded")
    if re.search(r'\b[12][,\s]?\d{3}\+?\s*sites', html_lower) and "sv-sites" not in html:
        add_issue(filepath, "A10.3", "sv-sites appears hardcoded")
    if re.search(r'L/PS/\d+', html) and "sv-licence" not in html:
        add_issue(filepath, "A10.4", "Police licence number appears hardcoded")
    if re.search(r'©\s*20(2[0-9])', html) and "sv-current-year" not in html:
        add_issue(filepath, "A10.5", "Copyright year appears hardcoded")

    # ══════════════════════════════════════════════════════════════════════════
    # A11. IMAGES & LINKS
    # ══════════════════════════════════════════════════════════════════════════

    GENERIC_ALT = {"image", "photo", "banner", "img", "picture"}
    for img in soup.find_all("img"):
        alt = img.get("alt")
        if alt is None:
            add_issue(filepath, "A11.1", f"img missing alt: {img.get('src','')[:60]}")
        elif alt.strip() == "":
            add_issue(filepath, "A11.2", f"img has empty alt='': {img.get('src','')[:60]}")
        elif alt.strip().lower() in GENERIC_ALT:
            add_issue(filepath, "A11.3", f"Generic alt text '{alt}' on img")
        src = img.get("src", "")
        if src and not src.startswith("/") and not src.startswith("http") and not src.startswith("data:"):
            add_issue(filepath, "A11.4", f"img src not absolute: {src[:60]}")

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("../") or href.startswith("./"):
            add_issue(filepath, "A11.6", f"Relative path: {href[:60]}")
        if href.endswith(".html") and not href.startswith("/") and not href.startswith("http"):
            add_issue(filepath, "A11.5", f"Internal link not absolute: {href[:60]}")

    # ══════════════════════════════════════════════════════════════════════════
    # A12. INLINE STYLES — with permitted exceptions:
    #   1. stat-bar-fill: ONLY style="width:X%;" is permitted
    #   2. Hero background-image in <head> <style> block (already allowed)
    # ══════════════════════════════════════════════════════════════════════════

    styled_els = []
    for el in soup.find_all(style=True):
        st = (el.get("style") or "").strip()
        # Permitted: stat-bar-fill with only width
        if "stat-bar-fill" in " ".join(get_classes(el)):
            if re.match(r'^width:\s*\d+(\.\d+)?%;?$', st, re.IGNORECASE):
                continue  # permitted
        styled_els.append(el)

    if styled_els:
        el_tags   = [f"<{el.name}>" for el in styled_els]
        tag_counts = {}
        for t in el_tags:
            tag_counts[t] = tag_counts.get(t, 0) + 1
        tag_summary = ", ".join(f"{t}×{n}" if n > 1 else t for t, n in sorted(tag_counts.items()))
        add_issue(filepath, "A12.1", f"{len(styled_els)} element(s) with style= attribute: {tag_summary}")

        font_color_tags, layout_tags = set(), set()
        for el in styled_els:
            st = (el.get("style") or "").lower()
            if any(k in st for k in ("font-size", "font-family", "font-weight", "color:")):
                font_color_tags.add(el.name)
            if any(k in st for k in ("padding", "margin", "gap:", "display:")):
                layout_tags.add(el.name)
        if font_color_tags:
            add_issue(filepath, "A12.2", f"Inline font/color on: {', '.join(f'<{t}>' for t in sorted(font_color_tags))}")
        if layout_tags:
            add_issue(filepath, "A12.3", f"Inline layout styles on: {', '.join(f'<{t}>' for t in sorted(layout_tags))}")

    # ══════════════════════════════════════════════════════════════════════════
    # A13. INLINE MIGRATION — sv-section-dark
    # background:#2d4a6b now has CSS class .sv-section-dark (v1.5).
    # Flag pages still using the old inline pattern.
    # ══════════════════════════════════════════════════════════════════════════

    dark_inline = [
        el for el in soup.find_all(style=True)
        if "2d4a6b" in (el.get("style") or "").lower()
        and "sv-section-dark" not in " ".join(get_classes(el))
    ]
    if dark_inline:
        add_issue(filepath, "A13.1",
                  f"{len(dark_inline)} element(s) with inline background:#2d4a6b — migrate to .sv-section-dark")

    # ══════════════════════════════════════════════════════════════════════════
    # A14. ACCESSIBILITY
    # ══════════════════════════════════════════════════════════════════════════

    ids_found = [el["id"] for el in soup.find_all(id=True)]
    if len(ids_found) != len(set(ids_found)):
        dupes = [i for i in set(ids_found) if ids_found.count(i) > 1]
        add_issue(filepath, "A14.1", f"Duplicate IDs: {', '.join(dupes[:5])}")

    for btn in soup.find_all("button"):
        if not btn.get_text(strip=True) and not btn.get("aria-label"):
            add_issue(filepath, "A14.2", "Button missing text and aria-label")

    bc_check = soup.find("nav", class_="sv-breadcrumb")
    if bc_check and bc_check.get("aria-label") != "Breadcrumb":
        add_issue(filepath, "A14.4", "sv-breadcrumb missing aria-label='Breadcrumb'")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if not os.path.isdir(SOLUTIONS_DIR):
        print(f"ERROR: solutions directory not found: {SOLUTIONS_DIR}")
        exit(1)

    file_list = []

    # solutions/index.html (hub)
    hub = os.path.join(SOLUTIONS_DIR, "index.html")
    if os.path.isfile(hub):
        file_list.append(hub)

    # solutions/[sector].html (8 sector hubs, flat)
    for fname in sorted(os.listdir(SOLUTIONS_DIR)):
        if fname.endswith(".html") and fname != "index.html":
            file_list.append(os.path.join(SOLUTIONS_DIR, fname))

    # solutions/[sector]/[persona].html (persona sub-pages)
    for sector in SECTORS_WITH_PERSONAS:
        sector_dir = os.path.join(SOLUTIONS_DIR, sector)
        if os.path.isdir(sector_dir):
            for fname in sorted(os.listdir(sector_dir)):
                if fname.endswith(".html"):
                    file_list.append(os.path.join(sector_dir, fname))

    print(f"Auditing {len(file_list)} solutions files")
    print()
    for fpath in file_list:
        pt = page_type(fpath)
        print(f"  [{pt:7s}] {rel_path(fpath)}")
        check_file(fpath)

    # ── Build report ──────────────────────────────────────────────────────────
    out = []
    out.append("# Solutions Section Audit Report")
    out.append("## Securevision SV-Web · Generated by audit_solutions_v1.py")
    out.append("")
    out.append(f"**Files audited:** {len(file_list)}")
    out.append(f"**Total issues:** {len(all_issues)}")
    b = sum(1 for i in all_issues if "BLOCKER" in i)
    m = sum(1 for i in all_issues if "MAJOR"   in i)
    n = sum(1 for i in all_issues if "MINOR"   in i)
    out.append(f"**Severity breakdown:** BLOCKER: {b} · MAJOR: {m} · MINOR: {n}")
    out.append("")
    out.append("**CTA rule:** Sector hubs + solutions/index.html → 'Book a Site Assessment'")
    out.append("             Persona sub-pages → 'Request a Proposal'")
    out.append("**Inline exception:** `.stat-bar-fill` with `style=\"width:X%\"` only is permitted.")
    out.append("**A13.1:** flags inline `background:#2d4a6b` — use `.sv-section-dark` (v1.5).")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Per-File Findings")
    out.append("")
    out.append("| File | Check ID | Issue Description | Severity |")
    out.append("|------|----------|-------------------|----------|")

    all_rel_paths = [rel_path(f) for f in file_list]
    for rp in sorted(all_rel_paths):
        if rp not in file_issues or not file_issues[rp]:
            out.append(f"| {rp} | ALL | PASS | — |")

    def sort_key(row):
        parts = row.strip("|").split("|")
        return (parts[0].strip(), parts[1].strip())

    for row in sorted(all_issues, key=sort_key):
        out.append(row)

    out.append("")
    out.append("---")
    out.append("")
    out.append("## Summary by Check Category")
    out.append("")
    out.append("| Category | Files Affected | Total Issues | Most Common Issue |")
    out.append("|----------|---------------|--------------|-------------------|")

    for cat in sorted(summary.keys()):
        d = summary[cat]
        most_common = max(d["desc"].items(), key=lambda x: x[1])[0] if d["desc"] else "—"
        out.append(f"| {cat} | {len(d['files'])} | {d['count']} | {most_common[:70]} |")

    out.append("")
    out.append("---")
    out.append("")
    out.append("*Securevision · Solutions Audit · v1.0 · June 2026*")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"\nDone. Report saved to: {OUT_FILE}")
    print(f"BLOCKER: {b}  MAJOR: {m}  MINOR: {n}  TOTAL: {len(all_issues)}")
