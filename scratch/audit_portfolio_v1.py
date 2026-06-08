import os
import re
from bs4 import BeautifulSoup
from collections import defaultdict

# ─── CONFIGURE PATHS ─────────────────────────────────────────────────────────
REPO_ROOT      = r"C:\Projects\SV-Build"
OUT_FILE       = r"C:\Projects\SV-Build\portfolio-audit-report-v1.md"
# ─────────────────────────────────────────────────────────────────────────────

PORTFOLIO_DIR = os.path.join(REPO_ROOT, "portfolio")

# Sector subdirectories to scan
SECTORS = [
    "commercial", "condominiums", "data-centres", "healthcare",
    "industrial", "institutions", "managed-living", "residential"
]

SEVERITIES = {
    # Infrastructure
    "A1.1": "BLOCKER", "A1.2": "BLOCKER", "A1.3": "BLOCKER", "A1.4": "BLOCKER",
    "A1.5": "BLOCKER", "A1.6": "BLOCKER", "A1.7": "MAJOR",   "A1.8": "MAJOR",
    "A1.9": "BLOCKER",  # portfolio-block.js not loaded
    # SEO
    "A2.1": "BLOCKER", "A2.2": "MAJOR",   "A2.3": "MINOR",   "A2.4": "BLOCKER",
    "A2.5": "MAJOR",   "A2.6": "MINOR",   "A2.7": "BLOCKER", "A2.8": "BLOCKER",
    "A2.9": "MAJOR",   "A2.10": "MAJOR",
    # Structure
    "A3.1": "BLOCKER", "A3.2": "BLOCKER", "A3.3": "BLOCKER", "A3.4": "BLOCKER",
    "A3.7": "BLOCKER", "A3.8": "BLOCKER",
    # Hero
    "A4.1": "MAJOR",   "A4.2": "MAJOR",   "A4.3": "BLOCKER", "A4.4": "MAJOR",
    "A4.5": "MAJOR",   "A4.6": "MAJOR",   "A4.7": "MAJOR",   "A4.8": "MAJOR",
    "A4.9": "MAJOR",
    # Trust bar
    "A5.1": "MAJOR",   "A5.2": "MAJOR",   "A5.3": "MAJOR",   "A5.4": "MAJOR",
    "A5.5": "MAJOR",   "A5.6": "MAJOR",   "A5.7": "MAJOR",   "A5.8": "MAJOR",
    # Breadcrumb
    "A6.1": "MAJOR",   "A6.2": "MINOR",   "A6.3": "MAJOR",   "A6.4": "MAJOR",
    "A6.5": "MINOR",
    # Headings
    "A7.1": "BLOCKER", "A7.4": "MAJOR",
    # Portfolio body
    "A8.1": "MAJOR",   "A8.2": "MAJOR",   "A8.3": "MAJOR",
    # Related projects block
    "A9.1": "BLOCKER", "A9.2": "MAJOR",   "A9.3": "MAJOR",
    # Dynamic values
    "A10.1": "MAJOR",  "A10.2": "MAJOR",  "A10.3": "MAJOR",
    "A10.4": "MAJOR",  "A10.5": "MINOR",
    # CTA
    "A11.1": "MAJOR",  "A11.2": "MAJOR",  "A11.3": "MINOR",
    "A11.4": "MINOR",  "A11.5": "MAJOR",
    # Images & links
    "A12.1": "BLOCKER","A12.2": "MAJOR",  "A12.3": "MINOR",  "A12.4": "BLOCKER",
    "A12.5": "MAJOR",  "A12.6": "MAJOR",
    # Inline styles
    "A14.1": "BLOCKER","A14.2": "MAJOR",  "A14.3": "MAJOR",
    # Accessibility
    "A15.1": "BLOCKER","A15.2": "MAJOR",  "A15.4": "MINOR",
}

all_issues  = []
file_issues = defaultdict(list)
summary     = defaultdict(lambda: {"files": set(), "count": 0, "desc": defaultdict(int)})


def rel_path(filepath):
    norm = filepath.replace("\\", "/")
    idx  = norm.find("/portfolio/")
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
    if tag is None:
        return []
    return tag.get("class") or []


def has_class(tag, cls):
    return cls in get_classes(tag)


def inline_has(tag, *keywords):
    style = (tag.get("style") or "").lower()
    return any(k in style for k in keywords)


def check_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    head         = soup.head or soup
    body         = soup.body or soup
    scripts      = soup.find_all("script")
    sheets       = soup.find_all("link", rel="stylesheet")
    header_el    = soup.find("header")

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

    portfolio_css_idx = next(
        (i for i, s in enumerate(sheets) if s.get("href", "").endswith("sv-portfolio.css")),
        None
    )
    if portfolio_css_idx is None:
        add_issue(filepath, "A1.6", "sv-portfolio.css not loaded")
    elif portfolio_css_idx != 1:
        add_issue(filepath, "A1.6", f"sv-portfolio.css loaded at position {portfolio_css_idx+1}, expected position 2")

    for s in sheets:
        href = s.get("href", "")
        if any(x in href for x in ("sv-systems", "sv-solutions", "sv-brands", "sv-insights", "sv-resources")):
            add_issue(filepath, "A1.7", f"Wrong section CSS loaded: {href}")

    wa_float = soup.find(class_=re.compile(r"\bwa-float\b"))
    if wa_float:
        add_issue(filepath, "A1.8", "WhatsApp float hardcoded (wa-float class in HTML — injected by nav-footer.js)")

    # portfolio-block.js must be loaded (before nav-footer.js)
    has_pb_script = any(s.get("src", "").endswith("portfolio-block.js") for s in scripts)
    if not has_pb_script:
        add_issue(filepath, "A1.9", "portfolio-block.js not loaded — required for .sv-portfolio-block injection")

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

    og_title     = soup.find("meta", property="og:title")
    og_title_val = (og_title.get("content") or "").strip() if og_title else ""
    if not og_title_val:
        add_issue(filepath, "A2.5", "og:title missing")
    elif og_title_val != title_text:
        add_issue(filepath, "A2.5", "og:title does not match <title>")

    og_desc     = soup.find("meta", property="og:description")
    og_desc_val = (og_desc.get("content") or "").strip() if og_desc else ""
    if not og_desc_val:
        add_issue(filepath, "A2.6", "og:description missing")
    elif og_desc_val != desc_content:
        add_issue(filepath, "A2.6", "og:description does not match meta description")

    og_img     = soup.find("meta", property="og:image")
    og_img_val = (og_img.get("content") or "").strip() if og_img else ""
    if not og_img_val:
        add_issue(filepath, "A2.7", "og:image missing")
    elif not og_img_val.startswith("https://"):
        add_issue(filepath, "A2.7", f"og:image not absolute HTTPS URL: {og_img_val[:60]}")

    og_url     = soup.find("meta", property="og:url")
    og_url_val = (og_url.get("content") or "").strip() if og_url else ""
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
        stripped = re.sub(r'@media[^{]+\{\s*\.hero-[^\s{]+\s*\{[^}]*\}\s*\}', '', sb_text)
        stripped = re.sub(r'\.hero-[^\s{]+\s*\{[^}]*\}', '', stripped)
        stripped = re.sub(r':root\s*\{[^}]*\}', '', stripped)
        stripped = stripped.strip()
        if stripped:
            add_issue(filepath, "A2.9", "Extra CSS in <head> <style> block beyond :root accent variable")
            break

    if header_el and inline_has(header_el, "background-image"):
        add_issue(filepath, "A2.10", "Inline background-image on <header> element — use <style> block in <head>")

    # ══════════════════════════════════════════════════════════════════════════
    # A3. PAGE STRUCTURE (presence)
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
    # A4. HERO — two valid patterns (legacy + new)
    # ══════════════════════════════════════════════════════════════════════════

    if header_el:
        cls_str  = " ".join(get_classes(header_el))
        is_legacy_hero = "portfolio-hero" in cls_str
        is_new_hero    = "hero-high-impact" in cls_str and "hero-compact" in cls_str

        if not is_legacy_hero and not is_new_hero:
            add_issue(filepath, "A4.1", f"Hero missing both portfolio-hero (legacy) and hero-high-impact hero-compact (new) — classes: {cls_str}")

        # Flag legacy hero as MAJOR (migration target)
        if is_legacy_hero and not is_new_hero:
            add_issue(filepath, "A4.2", "Hero still using legacy .portfolio-hero — migrate to hero hero-compact hero-high-impact hero-[slug]")

        # Inline background-image on header element (should be in <style> block)
        if inline_has(header_el, "background-image"):
            add_issue(filepath, "A4.9", "Inline background-image on <header> — move to <style> block in <head>")

        # H1 — exactly one
        h1s = soup.find_all("h1")
        if len(h1s) != 1:
            add_issue(filepath, "A4.3", f"Page has {len(h1s)} H1 elements — exactly 1 required")
        else:
            h1 = h1s[0]
            # New template: hero-title-main. Legacy: portfolio-hero-title. Both valid.
            has_new_title    = has_class(h1, "hero-title-main")
            has_legacy_title = has_class(h1, "portfolio-hero-title")
            if not has_new_title and not has_legacy_title:
                add_issue(filepath, "A4.4", f"H1 missing both hero-title-main (new) and portfolio-hero-title (legacy) — classes: {' '.join(get_classes(h1))}")
            if has_legacy_title and not has_new_title:
                add_issue(filepath, "A4.5", "H1 uses legacy .portfolio-hero-title — migrate to .hero-title-main")

        # Check for inline colour/font on any header element
        for el in header_el.find_all(style=True):
            st = (el.get("style") or "").lower()
            if "color" in st or "font" in st:
                add_issue(filepath, "A4.8", f"Inline color/font style on <{el.name}> inside hero")
                break

    # ══════════════════════════════════════════════════════════════════════════
    # A5. TRUST BAR — legacy classes flagged as MAJOR (not BLOCKER)
    # sv-shared.css confirms sv-trust-bar / trust-inner / sep all still work.
    # ══════════════════════════════════════════════════════════════════════════

    tb = soup.find(class_=re.compile(r"\btrust-bar\b|\bsv-trust-bar\b"))
    if not tb:
        add_issue(filepath, "A5.4", "Trust bar element not found")
    else:
        tb_classes = get_classes(tb)
        if "sv-trust-bar" in tb_classes and "trust-bar" not in tb_classes:
            add_issue(filepath, "A5.1", "Trust bar outer uses legacy sv-trust-bar — migrate to trust-bar")

        inner = tb.find(class_=re.compile(r"trust-bar-inner|trust-flex-inline|trust-inner"))
        if not inner:
            add_issue(filepath, "A5.2", "Trust bar inner wrapper missing (expected trust-bar-inner, trust-flex-inline, or trust-inner)")
        elif "trust-bar-inner" not in get_classes(inner) and "trust-flex-inline" in get_classes(inner):
            add_issue(filepath, "A5.2", "Trust bar inner uses trust-flex-inline — migrate to trust-bar-inner")
        elif "trust-bar-inner" not in get_classes(inner) and "trust-inner" in get_classes(inner):
            add_issue(filepath, "A5.2", "Trust bar inner uses legacy trust-inner — migrate to trust-bar-inner")

        for div_el in tb.find_all(class_=re.compile(r"\bsep\b|\bdivider\b")):
            if "trust-divider" not in get_classes(div_el):
                add_issue(filepath, "A5.3", f"Divider uses legacy class {' '.join(get_classes(div_el))} — migrate to trust-divider")

        if "bca registered" in tb.get_text(separator=" ").lower():
            add_issue(filepath, "A5.5", "BCA Registered in trust bar (belongs in footer only)")

        tb_html = str(tb)
        if re.search(r'Level\s*3', tb_html) and "sv-bizsafe" not in tb_html:
            add_issue(filepath, "A5.6", "bizSAFE level appears hardcoded (no sv-bizsafe class found)")

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
            if len(bc_links) < 2:
                add_issue(filepath, "A6.4", "Breadcrumb missing second link to /portfolio/")
            elif bc_links[1].get("href") not in ("/portfolio/", "/portfolio/index.html"):
                add_issue(filepath, "A6.4", f"Second breadcrumb link is '{bc_links[1].get('href')}', expected '/portfolio/'")

        bc_text_els = bc.find_all(["li", "span", "a"])
        if bc_text_els and bc_text_els[-1].name == "a":
            add_issue(filepath, "A6.5", "Last breadcrumb item is a link — should be plain text")

    # ══════════════════════════════════════════════════════════════════════════
    # A7. HEADING HIERARCHY (exclude aside/nav from walk)
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
    # A8. PORTFOLIO BODY CONTENT
    # ══════════════════════════════════════════════════════════════════════════

    # Project snapshot section (required — the overview table lives here)
    has_snapshot = bool(
        soup.find(class_="portfolio-snapshot") or
        soup.find(class_="portfolio-snapshot-grid")
    )
    if not has_snapshot:
        add_issue(filepath, "A8.1", "Missing .portfolio-snapshot or .portfolio-snapshot-grid")

    # Overview table (required)
    if not soup.find(class_="portfolio-overview-table"):
        add_issue(filepath, "A8.2", "Missing .portfolio-overview-table")

    # Kicker (sector badge row in hero) — required
    if not soup.find(class_="portfolio-kicker"):
        add_issue(filepath, "A8.3", "Missing .portfolio-kicker (sector badge row in hero)")

    # ══════════════════════════════════════════════════════════════════════════
    # A9. RELATED PROJECTS BLOCK
    # portfolio-block.js replaces .sv-portfolio-block at runtime.
    # The placeholder must exist. Its content will be empty or absent — correct.
    # ══════════════════════════════════════════════════════════════════════════

    pb_placeholder = soup.find(class_="sv-portfolio-block")
    if not pb_placeholder:
        add_issue(filepath, "A9.1", "Missing .sv-portfolio-block placeholder — related projects will not render")
    else:
        # data-category is required for the renderer to know which sector to use
        if not pb_placeholder.get("data-category"):
            add_issue(filepath, "A9.2", ".sv-portfolio-block missing data-category attribute")
        # data-exclude should reference the current page slug to avoid self-linking
        if not pb_placeholder.get("data-exclude"):
            add_issue(filepath, "A9.3", ".sv-portfolio-block missing data-exclude attribute (should contain current page slug)")

    # ══════════════════════════════════════════════════════════════════════════
    # A10. DYNAMIC VALUES
    # ══════════════════════════════════════════════════════════════════════════

    html_lower = html.lower()

    if re.search(r'\b(20|1[5-9])\s*years?\s+in\s+business', html_lower) and "sv-years-business" not in html:
        add_issue(filepath, "A10.1", "sv-years-business appears hardcoded")

    if re.search(r'\b(30|3[0-9]|4[0-9])\s*years?\s+(of\s+)?experience', html_lower) and "sv-years-experience" not in html:
        add_issue(filepath, "A10.2", "sv-years-experience appears hardcoded")

    if re.search(r'\b[12][,\s]?\d{3}\+?\s*sites', html_lower) and "sv-sites" not in html:
        add_issue(filepath, "A10.3", "sv-sites appears hardcoded (number found near 'sites')")

    if re.search(r'L/PS/\d+', html) and "sv-licence" not in html:
        add_issue(filepath, "A10.4", "Police licence number appears hardcoded")

    if re.search(r'©\s*20(2[0-9])', html) and "sv-current-year" not in html:
        add_issue(filepath, "A10.5", "Copyright year appears hardcoded (no sv-current-year class found)")

    # ══════════════════════════════════════════════════════════════════════════
    # A11. CTA SECTION
    # ══════════════════════════════════════════════════════════════════════════

    cta = soup.find(class_=re.compile(r"\bcta-section\b"))
    if not cta:
        add_issue(filepath, "A11.1", "cta-section not found")
    else:
        if "cta-high-impact" not in get_classes(cta):
            add_issue(filepath, "A11.1", "CTA missing cta-high-impact class")

        cta_btns = cta.find_all(class_=re.compile(r"\bbtn\b"))
        if cta_btns:
            has_proposal = any("request a proposal" in b.get_text().lower() for b in cta_btns)
            if not has_proposal:
                btn_labels = " / ".join(b.get_text().strip() for b in cta_btns)
                add_issue(filepath, "A11.2", f"CTA label is not 'Request a Proposal' — found: {btn_labels[:80]}")

        if not cta.find("h2"):
            add_issue(filepath, "A11.3", "H2 missing inside CTA section")

        sub = cta.find(class_="subtitle")
        if sub and sub.get("style"):
            add_issue(filepath, "A11.4", "CTA subtitle has inline style")

        for el in cta.find_all(style=True):
            add_issue(filepath, "A11.5", f"Inline style on <{el.name}> inside CTA section")
            break

    # ══════════════════════════════════════════════════════════════════════════
    # A12. IMAGES & LINKS
    # ══════════════════════════════════════════════════════════════════════════

    GENERIC_ALT = {"image", "photo", "banner", "img", "picture"}
    for img in soup.find_all("img"):
        alt = img.get("alt")
        if alt is None:
            add_issue(filepath, "A12.1", f"img missing alt: {img.get('src','')[:60]}")
        elif alt.strip() == "":
            add_issue(filepath, "A12.2", f"img has empty alt='': {img.get('src','')[:60]}")
        elif alt.strip().lower() in GENERIC_ALT:
            add_issue(filepath, "A12.3", f"Generic alt text '{alt}' on img")
        src = img.get("src", "")
        if src and not src.startswith("/") and not src.startswith("http") and not src.startswith("data:"):
            add_issue(filepath, "A12.4", f"img src not absolute: {src[:60]}")

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("../") or href.startswith("./"):
            add_issue(filepath, "A12.6", f"Relative path: {href[:60]}")
        if href.endswith(".html") and not href.startswith("/") and not href.startswith("http"):
            add_issue(filepath, "A12.5", f"Internal link not absolute: {href[:60]}")

    # ══════════════════════════════════════════════════════════════════════════
    # A14. INLINE STYLES — per-file summary (not per-element)
    # ══════════════════════════════════════════════════════════════════════════

    styled_els = soup.find_all(style=True)
    if styled_els:
        el_tags   = [f"<{el.name}>" for el in styled_els]
        tag_counts = {}
        for t in el_tags:
            tag_counts[t] = tag_counts.get(t, 0) + 1
        tag_summary = ", ".join(
            f"{t}×{n}" if n > 1 else t for t, n in sorted(tag_counts.items())
        )
        add_issue(filepath, "A14.1", f"{len(styled_els)} element(s) with style= attribute: {tag_summary}")

        font_color_tags = set()
        layout_tags     = set()
        for el in styled_els:
            st = (el.get("style") or "").lower()
            if any(k in st for k in ("font-size", "font-family", "font-weight", "color:")):
                font_color_tags.add(el.name)
            if any(k in st for k in ("padding", "margin", "gap:", "display:")):
                layout_tags.add(el.name)

        if font_color_tags:
            add_issue(filepath, "A14.2", f"Inline font/color on: {', '.join(f'<{t}>' for t in sorted(font_color_tags))}")
        if layout_tags:
            add_issue(filepath, "A14.3", f"Inline layout styles on: {', '.join(f'<{t}>' for t in sorted(layout_tags))}")

    # ══════════════════════════════════════════════════════════════════════════
    # A15. ACCESSIBILITY
    # ══════════════════════════════════════════════════════════════════════════

    ids_found = [el["id"] for el in soup.find_all(id=True)]
    if len(ids_found) != len(set(ids_found)):
        dupes = [i for i in set(ids_found) if ids_found.count(i) > 1]
        add_issue(filepath, "A15.1", f"Duplicate IDs: {', '.join(dupes[:5])}")

    for btn in soup.find_all("button"):
        if not btn.get_text(strip=True) and not btn.get("aria-label"):
            add_issue(filepath, "A15.2", "Button missing text and aria-label")

    bc_check = soup.find("nav", class_="sv-breadcrumb")
    if bc_check and bc_check.get("aria-label") != "Breadcrumb":
        add_issue(filepath, "A15.4", "sv-breadcrumb missing aria-label='Breadcrumb'")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if not os.path.isdir(PORTFOLIO_DIR):
        print(f"ERROR: portfolio directory not found: {PORTFOLIO_DIR}")
        exit(1)

    file_list = []

    # Collect case study pages from each sector subdirectory
    for sector in SECTORS:
        sector_dir = os.path.join(PORTFOLIO_DIR, sector)
        if os.path.isdir(sector_dir):
            for fname in sorted(os.listdir(sector_dir)):
                if fname.endswith(".html"):
                    file_list.append(os.path.join(sector_dir, fname))
        else:
            print(f"  NOTE: sector directory not found: {sector_dir}")

    # Do NOT include portfolio/index.html — bespoke, excluded from all batch audits
    print(f"Auditing {len(file_list)} portfolio case study files")
    print(f"(portfolio/index.html excluded — bespoke page)")
    print()

    for fpath in file_list:
        print(f"  {rel_path(fpath)}")
        check_file(fpath)

    # ── Build report ──────────────────────────────────────────────────────────
    out = []
    out.append("# Portfolio Section Audit Report")
    out.append("## Securevision SV-Web · Generated by audit_portfolio_v1.py")
    out.append("")
    out.append(f"**Files audited:** {len(file_list)}")
    out.append(f"**Total issues:** {len(all_issues)}")
    b = sum(1 for i in all_issues if "BLOCKER" in i)
    m = sum(1 for i in all_issues if "MAJOR"   in i)
    n = sum(1 for i in all_issues if "MINOR"   in i)
    out.append(f"**Severity breakdown:** BLOCKER: {b} · MAJOR: {m} · MINOR: {n}")
    out.append("")
    out.append("**Note:** portfolio/index.html is EXCLUDED (bespoke page).")
    out.append("**Note:** A4.2 (legacy portfolio-hero) and A4.5 (legacy portfolio-hero-title)")
    out.append("  are MAJOR, not BLOCKER — migration is in progress (sv-portfolio.css v1.3).")
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
    out.append("*Securevision · Portfolio Audit · v1.0 · June 2026*")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"\nDone. Report saved to: {OUT_FILE}")
    print(f"BLOCKER: {b}  MAJOR: {m}  MINOR: {n}  TOTAL: {len(all_issues)}")
