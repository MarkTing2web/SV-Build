import os
import re
from bs4 import BeautifulSoup
from collections import defaultdict

# ─── CONFIGURE PATHS ─────────────────────────────────────────────────────────
REPO_ROOT    = r"C:\Projects\SV-Build"
OUT_FILE     = r"C:\Projects\SV-Build\resources-audit-report-v1.md"
# ─────────────────────────────────────────────────────────────────────────────

RESOURCES_DIR       = os.path.join(REPO_ROOT, "resources")
RESOURCES_GUIDES_DIR = os.path.join(RESOURCES_DIR, "guides")

SEVERITIES = {
    "A1.1": "BLOCKER", "A1.2": "BLOCKER", "A1.3": "BLOCKER", "A1.4": "BLOCKER",
    "A1.5": "BLOCKER", "A1.6": "BLOCKER", "A1.7": "MAJOR",   "A1.8": "MAJOR",
    "A2.1": "BLOCKER", "A2.2": "MAJOR",   "A2.3": "MINOR",   "A2.4": "BLOCKER",
    "A2.5": "MAJOR",   "A2.6": "MINOR",   "A2.7": "BLOCKER", "A2.8": "BLOCKER",
    "A2.9": "MAJOR",   "A2.10": "MAJOR",
    "A3.1": "BLOCKER", "A3.2": "BLOCKER", "A3.3": "BLOCKER", "A3.4": "BLOCKER",
    "A3.5": "BLOCKER", "A3.6": "MAJOR",   "A3.7": "BLOCKER", "A3.8": "BLOCKER",
    "A4.1": "MAJOR",   "A4.2": "MAJOR",   "A4.3": "BLOCKER", "A4.4": "MAJOR",
    "A4.5": "MAJOR",   "A4.6": "MAJOR",   "A4.7": "MINOR",   "A4.8": "MAJOR",
    "A4.9": "MAJOR",   "A4.10": "MAJOR",
    "A5.1": "MAJOR",   "A5.2": "MAJOR",   "A5.3": "MAJOR",   "A5.4": "MAJOR",
    "A5.5": "MAJOR",   "A5.6": "MAJOR",   "A5.7": "MAJOR",   "A5.8": "MAJOR",
    "A6.1": "MAJOR",   "A6.2": "MINOR",   "A6.3": "MAJOR",   "A6.4": "MAJOR",
    "A6.5": "MINOR",
    "A7.1": "BLOCKER", "A7.4": "MAJOR",
    "A8.1": "BLOCKER", "A8.2": "MAJOR",   "A8.3": "MAJOR",   "A8.4": "MAJOR",
    "A8.5": "MINOR",   "A8.6": "MINOR",   "A8.7": "MAJOR",   "A8.8": "MAJOR",
    "A8.9": "MAJOR",
    "A9.1": "MAJOR",   "A9.2": "MAJOR",   "A9.3": "MAJOR",   "A9.4": "MAJOR",
    "A9.5": "MAJOR",
    "A10.1": "MAJOR",  "A10.2": "MAJOR",  "A10.3": "MAJOR",  "A10.4": "MAJOR",
    "A10.5": "MINOR",
    "A11.1": "MAJOR",  "A11.2": "MAJOR",  "A11.3": "MINOR",  "A11.4": "MINOR",
    "A11.5": "MAJOR",
    "A12.1": "BLOCKER","A12.2": "MAJOR",  "A12.3": "MINOR",  "A12.4": "BLOCKER",
    "A12.5": "MAJOR",  "A12.6": "MAJOR",
    "A13.1": "MAJOR",  "A13.2": "MAJOR",  "A13.3": "MAJOR",
    "A14.1": "BLOCKER","A14.2": "MAJOR",  "A14.3": "MAJOR",  "A14.4": "MINOR",
    "A15.1": "BLOCKER","A15.2": "MAJOR",  "A15.3": "MINOR",  "A15.4": "MINOR",
    # Guide-specific checks
    "B1.1": "MAJOR",   "B1.2": "MAJOR",   "B1.3": "MAJOR",   "B1.4": "MAJOR",
    "B2.1": "MAJOR",   "B2.2": "MAJOR",   "B2.3": "MAJOR",   "B2.4": "MAJOR",
    "B2.5": "MAJOR",   "B2.6": "MAJOR",
    "B3.1": "MAJOR",   "B3.2": "MAJOR",   "B3.3": "MAJOR",
    # Hub-specific checks
    "C1.1": "MAJOR",   "C1.2": "MAJOR",   "C1.3": "MAJOR",
    "C2.1": "MAJOR",   "C2.2": "MAJOR",
}

all_issues   = []
file_issues  = defaultdict(list)
summary      = defaultdict(lambda: {"files": set(), "count": 0, "desc": defaultdict(int)})


def rel_path(filepath):
    """Return /resources/... path for display."""
    norm = filepath.replace("\\", "/")
    idx = norm.find("/resources/")
    return norm[idx:] if idx >= 0 else "/" + os.path.basename(filepath)


def add_issue(filepath, check_id, desc):
    sev  = SEVERITIES.get(check_id, "MINOR")
    rp   = rel_path(filepath)
    row  = f"| {rp} | {check_id} | {desc} | {sev} |"
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


def page_type(filepath):
    """Return 'hub', 'guide', or 'sub'."""
    fname = os.path.basename(filepath)
    parent = os.path.basename(os.path.dirname(filepath))
    if fname == "index.html" and parent == "resources":
        return "hub"
    if parent == "guides":
        return "guide"
    return "sub"


def check_file(filepath):
    ptype = page_type(filepath)
    is_hub   = ptype == "hub"
    is_guide = ptype == "guide"
    is_sub   = ptype == "sub"

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    head    = soup.head or soup
    body    = soup.body or soup
    scripts = soup.find_all("script")
    sheets  = soup.find_all("link", rel="stylesheet")

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

    resources_css_idx = next(
        (i for i, s in enumerate(sheets) if s.get("href", "").endswith("sv-resources.css")),
        None
    )
    if resources_css_idx is None:
        add_issue(filepath, "A1.6", "sv-resources.css not loaded")
    elif resources_css_idx != 1:
        add_issue(filepath, "A1.6", f"sv-resources.css loaded at position {resources_css_idx+1}, expected position 2")

    for s in sheets:
        href = s.get("href", "")
        if any(x in href for x in ("sv-systems", "sv-solutions", "sv-brands", "sv-insights", "sv-portfolio")):
            add_issue(filepath, "A1.7", f"Wrong section CSS loaded: {href}")

    wa_float_div = soup.find(class_=re.compile(r"\bwa-float\b"))
    if wa_float_div:
        add_issue(filepath, "A1.8", "WhatsApp float hardcoded (wa-float class found in HTML — injected by nav-footer.js)")

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
        stripped = re.sub(r':root\s*\{[^}]*\}', '', sb_text).strip()
        if stripped:
            add_issue(filepath, "A2.9", "Extra CSS in <head> <style> block beyond :root accent variable")
            break

    header_el = soup.find("header")
    if header_el and inline_has(header_el, "background-image"):
        add_issue(filepath, "A2.10", "Inline background-image on <header> element")

    # ══════════════════════════════════════════════════════════════════════════
    # A3. PAGE STRUCTURE (presence checks)
    # ══════════════════════════════════════════════════════════════════════════

    if not soup.find("nav", id="sv-nav"):
        add_issue(filepath, "A3.1", "Nav placeholder missing")

    if not soup.find("header", class_=re.compile(r"hero")):
        add_issue(filepath, "A3.2", "Hero <header> with hero class missing")

    if not soup.find(class_=re.compile(r"\btrust-bar\b")):
        add_issue(filepath, "A3.3", "Trust bar missing")

    if not soup.find("nav", class_=re.compile(r"sv-breadcrumb")):
        add_issue(filepath, "A3.4", "Breadcrumb nav missing")

    # A3.5 — body content structure (guide-specific, checked in B2)
    if not soup.find(class_=re.compile(r"\bcta-section\b")):
        add_issue(filepath, "A3.7", "CTA section missing")

    if not soup.find("footer", id="sv-footer"):
        add_issue(filepath, "A3.8", "Footer placeholder missing")

    # ══════════════════════════════════════════════════════════════════════════
    # A4. HERO (standard hero — applies to all resource pages)
    # ══════════════════════════════════════════════════════════════════════════

    if header_el:
        cls_str = " ".join(get_classes(header_el))

        if "hero-high-impact" not in cls_str:
            add_issue(filepath, "A4.1", "Hero missing hero-high-impact class")

        # hero-compact for guides and sub-pages; hub uses hero-standard
        if is_hub:
            if "hero-standard" not in cls_str:
                add_issue(filepath, "A4.2", "Hub hero missing hero-standard class (should be 65vh)")
        else:
            if "hero-compact" not in cls_str:
                add_issue(filepath, "A4.2", "Page hero missing hero-compact class (should be 52vh)")

        if inline_has(header_el, "background-image"):
            add_issue(filepath, "A4.9", "Inline background-image on hero element (use <style> block in <head>)")

        h1s = soup.find_all("h1")
        if len(h1s) != 1:
            add_issue(filepath, "A4.3", f"Page has {len(h1s)} H1 elements — exactly 1 required")
        else:
            if not has_class(h1s[0], "hero-title-main"):
                add_issue(filepath, "A4.4", "H1 missing hero-title-main class")

        eyebrow = header_el.find(class_=re.compile(r"\beyebrow\b"))
        if eyebrow and not has_class(eyebrow, "eyebrow-light"):
            add_issue(filepath, "A4.5", "Eyebrow missing eyebrow-light class")

        subtitle = header_el.find(class_=re.compile(r"hero-subtitle-main"))
        if not subtitle:
            # Check for any subtitle-like element without the class
            plain_sub = header_el.find(class_=re.compile(r"subtitle"))
            if plain_sub and not has_class(plain_sub, "hero-subtitle-main"):
                add_issue(filepath, "A4.6", "Hero subtitle missing hero-subtitle-main class")

        for el in header_el.find_all(style=True):
            st = (el.get("style") or "").lower()
            if "color" in st or "font" in st:
                add_issue(filepath, "A4.10", f"Inline color/font style on <{el.name}> inside hero")
                break

    # ══════════════════════════════════════════════════════════════════════════
    # A5. TRUST BAR
    # ══════════════════════════════════════════════════════════════════════════

    tb = soup.find(class_=re.compile(r"\btrust-bar\b"))
    if not tb:
        add_issue(filepath, "A5.4", "Trust bar element not found")
    else:
        if "sv-trust-bar" in get_classes(tb):
            add_issue(filepath, "A5.1", "Trust bar outer uses sv-trust-bar (should be trust-bar)")

        inner = tb.find(class_=re.compile(r"trust-bar-inner|trust-flex-inline"))
        if inner and "trust-flex-inline" in get_classes(inner):
            add_issue(filepath, "A5.2", "Trust bar inner uses trust-flex-inline (should be trust-bar-inner)")
        elif not inner:
            add_issue(filepath, "A5.2", "Trust bar inner wrapper missing (expected trust-bar-inner)")

        for div_el in tb.find_all(class_=re.compile(r"\b(sep|divider)\b")):
            if "trust-divider" not in get_classes(div_el):
                add_issue(filepath, "A5.3", f"Divider uses wrong class: {' '.join(get_classes(div_el))}")

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
            add_issue(filepath, "A6.3", "Breadcrumb has no links at all")
        else:
            if bc_links[0].get("href") != "/":
                add_issue(filepath, "A6.3", f"First breadcrumb link is '{bc_links[0].get('href')}', expected '/'")
            # Second crumb should link to /resources/ for all resource pages
            if not is_hub:
                if len(bc_links) < 2:
                    add_issue(filepath, "A6.4", "Breadcrumb missing second link to /resources/")
                elif bc_links[1].get("href") not in ("/resources/", "/resources/index.html"):
                    add_issue(filepath, "A6.4", f"Second breadcrumb link is '{bc_links[1].get('href')}', expected '/resources/'")

        # Last item should not be a link
        bc_text_els = bc.find_all(["li", "span", "a"])
        if bc_text_els and bc_text_els[-1].name == "a":
            add_issue(filepath, "A6.5", "Last breadcrumb item is a link — should be plain text")

    # ══════════════════════════════════════════════════════════════════════════
    # A7. HEADING HIERARCHY
    # ══════════════════════════════════════════════════════════════════════════

    all_h1 = soup.find_all("h1")
    if len(all_h1) != 1:
        add_issue(filepath, "A7.1", f"Page has {len(all_h1)} H1 elements — exactly 1 required")

    # Heading hierarchy — exclude aside/sidebar elements (TOC h3 etc. are UI, not content)
    headings  = [h for h in soup.find_all(re.compile(r"^h[1-6]$"))
                 if not any(p.name == "aside" for p in h.parents)]
    prev_level = 0
    for hx in headings:
        level = int(hx.name[1])
        if level > prev_level + 1 and prev_level != 0:
            add_issue(filepath, "A7.4", f"Heading level skipped: H{prev_level} → H{level} ('{hx.get_text()[:40]}')")
        prev_level = level

    # ══════════════════════════════════════════════════════════════════════════
    # A8. BODY CONTENT STRUCTURE (guide pages only)
    # Guides can use EITHER the legacy or new .rg- template.
    # ══════════════════════════════════════════════════════════════════════════

    if is_guide:
        has_rg_layout     = bool(soup.find(class_="rg-layout"))
        has_legacy_layout = bool(soup.find(class_="layout-with-sidebar"))

        if not has_rg_layout and not has_legacy_layout:
            add_issue(filepath, "A8.1", "Guide missing both .rg-layout (new) and .layout-with-sidebar (legacy) — no content layout found")
        
        if has_rg_layout:
            # New .rg- template checks
            if not soup.find(class_="rg-sidebar"):
                add_issue(filepath, "A8.2", "New template: missing .rg-sidebar")
            if not soup.find(class_="rg-toc"):
                add_issue(filepath, "A8.3", "New template: missing .rg-toc (table of contents)")
            if not soup.find(class_="rg-content"):
                add_issue(filepath, "A8.4", "New template: missing .rg-content")

        if has_legacy_layout:
            # Legacy template checks
            ab = soup.find(class_="layout-with-sidebar")
            if not ab and soup.find(class_="article-body"):
                ab = soup.find(class_="article-body") # fallback to prevent crash
            if ab and not ab.find("aside"):
                add_issue(filepath, "A8.5", "Legacy template: missing <aside> inside layout-with-sidebar")
            if not soup.find(class_="sticky-toc"):
                add_issue(filepath, "A8.6", "Legacy template: missing .sticky-toc")

        # Author strip — required on all guide pages (either class pattern)
        has_rg_author   = bool(soup.find(class_="rg-hero-author"))
        has_bio_strip   = bool(soup.find(class_="author-bio-strip"))
        if not has_rg_author and not has_bio_strip:
            add_issue(filepath, "A8.7", "Guide missing author element (no .rg-hero-author or .author-bio-strip found)")

        # Founder card in sidebar — required
        if not soup.find(class_="founder-card"):
            add_issue(filepath, "A8.8", "Guide missing .founder-card in sidebar")

        # sv-years-experience dynamic class in founder card
        fc = soup.find(class_="founder-card")
        if fc and "sv-years-experience" not in str(fc):
            add_issue(filepath, "A8.9", "sv-years-experience dynamic class not found in founder-card")

    # ══════════════════════════════════════════════════════════════════════════
    # A9. INLINE ARTICLE COMPONENTS (guide pages — check .rg- vs legacy classes)
    # ══════════════════════════════════════════════════════════════════════════

    if is_guide:
        # Callout / recommendation boxes — should use .rg-callout (new) or .recommendation-box (legacy)
        # Do NOT flag .rg-callout-label (child of .rg-callout) — same ancestor fix as insights
        for el in soup.find_all(class_=re.compile(r"callout")):
            classes = get_classes(el)
            has_rg_ancestor = any(
                "rg-callout" in (a.get("class") or []) for a in el.parents
            )
            is_valid = "rg-callout" in classes or "callout-box" in classes
            if not is_valid and not has_rg_ancestor:
                add_issue(filepath, "A9.1", f"Callout element uses unrecognised class: {' '.join(classes)}")

        for el in soup.find_all(class_=re.compile(r"verdict")):
            classes = get_classes(el)
            has_rg_ancestor = any(
                "rg-verdict" in (a.get("class") or []) for a in el.parents
            )
            is_valid = "rg-verdict" in classes or "verdict-box" in classes
            if not is_valid and not has_rg_ancestor:
                add_issue(filepath, "A9.2", f"Verdict element uses unrecognised class: {' '.join(classes)}")

        for el in soup.find_all(class_=re.compile(r"recommendation")):
            classes = get_classes(el)
            has_rg_ancestor = any(
                "rg-recommendation" in (a.get("class") or []) for a in el.parents
            )
            is_valid = "rg-recommendation" in classes or "recommendation-box" in classes
            if not is_valid and not has_rg_ancestor:
                add_issue(filepath, "A9.3", f"Recommendation element uses unrecognised class: {' '.join(classes)}")

    # ══════════════════════════════════════════════════════════════════════════
    # A10. DYNAMIC VALUES
    # ══════════════════════════════════════════════════════════════════════════

    html_lower = html.lower()

    if re.search(r'\b(20|1[5-9])\s*years?\s+in\s+business', html_lower) and "sv-years-business" not in html:
        add_issue(filepath, "A10.1", "sv-years-business appears hardcoded")

    if re.search(r'\b(30|3[0-9]|4[0-9])\s*years?\s+(of\s+)?experience', html_lower) and "sv-years-experience" not in html:
        add_issue(filepath, "A10.2", "sv-years-experience appears hardcoded (year number found near 'years experience')")

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
            has_assessment = any("book" in b.get_text().lower() and "assessment" in b.get_text().lower() for b in cta_btns)
            # Resources = Request a Proposal (same as insights)
            if not has_proposal:
                btn_labels = " / ".join(b.get_text().strip() for b in cta_btns)
                add_issue(filepath, "A11.2", f"CTA button label is not 'Request a Proposal' — found: {btn_labels[:80]}")

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
    # A13. RELATED GUIDES (guide pages)
    # .guides-related-grid may be empty (JS-injected) or contain static links.
    # Only flag if the element is ABSENT entirely.
    # ══════════════════════════════════════════════════════════════════════════

    if is_guide:
        has_guides_grid = bool(soup.find(class_="guides-related-grid"))
        has_insights_grid = bool(soup.find(class_="insights-related-grid"))

        if not has_guides_grid and not has_insights_grid:
            add_issue(filepath, "A13.1", "No related guides grid found (.guides-related-grid or .insights-related-grid)")
        elif has_insights_grid and not has_guides_grid:
            add_issue(filepath, "A13.2", "Using .insights-related-grid on a guide page — should use .guides-related-grid")

        # If static links present, verify they're absolute
        grid = soup.find(class_="guides-related-grid") or soup.find(class_="insights-related-grid")
        if grid:
            for lnk in grid.find_all("a", href=True):
                if not lnk["href"].startswith("/") and not lnk["href"].startswith("http"):
                    add_issue(filepath, "A13.3", f"Related guide link not absolute: {lnk['href'][:60]}")

    # ══════════════════════════════════════════════════════════════════════════
    # A14. INLINE STYLES — ZERO TOLERANCE
    # ══════════════════════════════════════════════════════════════════════════

    styled_els = soup.find_all(style=True)
    if styled_els:
        el_tags = [f"<{el.name}>" for el in styled_els]
        tag_counts = {}
        for t in el_tags:
            tag_counts[t] = tag_counts.get(t, 0) + 1
        tag_summary = ", ".join(f"{t}×{n}" if n > 1 else t for t, n in sorted(tag_counts.items()))
        add_issue(filepath, "A14.1", f"{len(styled_els)} element(s) with style= attribute: {tag_summary}")

        font_color_tags = set()
        layout_tags = set()
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

    # ══════════════════════════════════════════════════════════════════════════
    # SECTION B — GUIDE-SPECIFIC HERO CHECKS
    # ══════════════════════════════════════════════════════════════════════════

    if is_guide and header_el:
        cls_str = " ".join(get_classes(header_el))

        # All guide pages must use hero-guide OR one of the legacy hero-[system] classes
        VALID_GUIDE_HEROES = {
            "hero-guide", "hero-cctv", "hero-alarm", "hero-access",
            "hero-vehicle", "hero-intercom", "hero-telephony"
        }
        has_valid_guide_hero = any(c in cls_str for c in VALID_GUIDE_HEROES)
        if not has_valid_guide_hero:
            add_issue(filepath, "B1.1", f"Guide hero missing hero-guide (or legacy hero-[system]) class — classes: {cls_str}")

        # Flag legacy hero classes (not hero-guide) — informational MAJOR
        LEGACY_HEROES = {"hero-cctv", "hero-alarm", "hero-access", "hero-vehicle", "hero-intercom", "hero-telephony"}
        used_legacy = [c for c in LEGACY_HEROES if c in cls_str]
        if used_legacy:
            add_issue(filepath, "B1.2", f"Using legacy hero class {used_legacy[0]} — should migrate to hero-guide with inline background-image in <style> block")

        # Guide hero must not use insights-header class
        if "insights-header" in cls_str:
            add_issue(filepath, "B1.3", "Guide hero uses insights-header class — wrong template")

        # Author in hero (new template uses .rg-hero-author)
        rg_author = header_el.find(class_="rg-hero-author")
        if not rg_author:
            # Legacy: author-bio-strip may be outside header — acceptable
            pass

    # ══════════════════════════════════════════════════════════════════════════
    # SECTION C — HUB PAGE CHECKS (/resources/index.html)
    # ══════════════════════════════════════════════════════════════════════════

    if is_hub:
        if header_el:
            cls_str = " ".join(get_classes(header_el))
            if "hero-high-impact" not in cls_str:
                add_issue(filepath, "C1.1", "Hub hero missing hero-high-impact class")
            if "hero-standard" not in cls_str:
                add_issue(filepath, "C1.2", "Hub hero missing hero-standard class (should be 65vh)")
            if inline_has(header_el, "background-image"):
                add_issue(filepath, "C1.3", "Inline background-image on hub hero")

        # Hub should have guide cards grid
        if not soup.find(class_=re.compile(r"\bguides-grid\b")):
            add_issue(filepath, "C2.1", "Hub missing .guides-grid")

        # Hub should have quick-access or filter elements
        if not soup.find(class_=re.compile(r"quick-card|filter-btn|guide-card")):
            add_issue(filepath, "C2.2", "Hub missing quick-card, filter-btn, or guide-card elements")


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if not os.path.isdir(RESOURCES_DIR):
        print(f"ERROR: resources directory not found: {RESOURCES_DIR}")
        exit(1)

    file_list = []

    # Collect /resources/*.html
    for fname in sorted(os.listdir(RESOURCES_DIR)):
        if fname.endswith(".html"):
            file_list.append(os.path.join(RESOURCES_DIR, fname))

    # Collect /resources/guides/*.html
    if os.path.isdir(RESOURCES_GUIDES_DIR):
        for fname in sorted(os.listdir(RESOURCES_GUIDES_DIR)):
            if fname.endswith(".html"):
                file_list.append(os.path.join(RESOURCES_GUIDES_DIR, fname))
    else:
        print(f"NOTE: /resources/guides/ directory not found at {RESOURCES_GUIDES_DIR}")

    print(f"Auditing {len(file_list)} files...")
    for fpath in file_list:
        ptype = page_type(fpath)
        print(f"  [{ptype:5s}] {rel_path(fpath)}")
        check_file(fpath)

    # ── Build report ──────────────────────────────────────────────────────────
    out = []
    out.append("# Resources Section Audit Report")
    out.append("## Securevision SV-Web · Generated by audit_resources_v1.py")
    out.append("")
    out.append(f"**Files audited:** {len(file_list)}")
    out.append(f"**Total issues:** {len(all_issues)}")
    b = sum(1 for i in all_issues if "BLOCKER" in i)
    m = sum(1 for i in all_issues if "MAJOR"   in i)
    n = sum(1 for i in all_issues if "MINOR"   in i)
    out.append(f"**Severity breakdown:** BLOCKER: {b} · MAJOR: {m} · MINOR: {n}")
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
    out.append("*Securevision · Resources Audit · v1.0 · June 2026*")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"\nDone. Report saved to: {OUT_FILE}")
    print(f"BLOCKER: {b}  MAJOR: {m}  MINOR: {n}  TOTAL: {len(all_issues)}")
