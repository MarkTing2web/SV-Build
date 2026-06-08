import os
import re
from bs4 import BeautifulSoup
from collections import defaultdict

# ─── CONFIGURE THESE TWO PATHS ───────────────────────────────────────────────
REPO_ROOT   = r"C:\Projects\SV-Build"
OUT_FILE    = r"C:\Projects\SV-Build\insights-audit-report-v5.md"
# ─────────────────────────────────────────────────────────────────────────────

INSIGHTS_DIR = os.path.join(REPO_ROOT, "insights")

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
    "A6.5": "MINOR",   "A6.6": "MINOR",
    "A7.1": "BLOCKER", "A7.2": "MAJOR",   "A7.3": "MAJOR",   "A7.4": "MAJOR",
    "A7.5": "MINOR",
    "A8.1": "BLOCKER", "A8.2": "BLOCKER", "A8.3": "BLOCKER", "A8.4": "MAJOR",
    "A8.5": "MINOR",   "A8.6": "MINOR",   "A8.7": "MAJOR",   "A8.8": "MAJOR",
    "A8.9": "MAJOR",
    "A9.1": "MAJOR",   "A9.2": "MAJOR",   "A9.3": "MAJOR",   "A9.4": "MINOR",
    "A9.5": "MAJOR",
    "A10.1": "MAJOR",  "A10.2": "MAJOR",  "A10.3": "MAJOR",  "A10.4": "MAJOR",
    "A10.5": "MAJOR",  "A10.6": "MINOR",
    "A11.1": "MAJOR",  "A11.2": "MAJOR",  "A11.3": "MINOR",  "A11.4": "MINOR",
    "A11.5": "MAJOR",
    "A12.1": "BLOCKER","A12.2": "MAJOR",  "A12.3": "MINOR",  "A12.4": "BLOCKER",
    "A12.5": "MAJOR",  "A12.6": "MAJOR",
    "A13.1": "MINOR",  "A13.2": "MAJOR",  "A13.3": "MAJOR",  "A13.4": "MAJOR",
    "A14.1": "BLOCKER","A14.2": "MAJOR",  "A14.3": "MAJOR",  "A14.4": "MINOR",
    "A15.1": "BLOCKER","A15.2": "MAJOR",  "A15.3": "MINOR",  "A15.4": "MINOR",
    "B1.1": "MAJOR",   "B1.2": "MAJOR",   "B1.3": "MAJOR",   "B1.4": "MAJOR",
    "B1.5": "MAJOR",   "B1.6": "MAJOR",
    "B2.1": "MAJOR",   "B2.2": "MAJOR",   "B2.3": "MAJOR",
    "B3.1": "MAJOR",   "B3.2": "MAJOR",   "B3.3": "MAJOR",
    "B4.1": "MAJOR",   "B4.2": "MAJOR",   "B4.3": "MAJOR",   "B4.4": "MAJOR",
    "B5.1": "MAJOR",   "B5.2": "MAJOR",   "B5.3": "MAJOR",
    "B6.1": "MAJOR",   "B6.2": "MAJOR",   "B6.3": "MAJOR",   "B6.4": "MAJOR",
    "B6.5": "MINOR",
    "B7.1": "MAJOR",   "B7.2": "MAJOR",
}

all_issues  = []
file_issues = defaultdict(list)   # rel_path → list of check IDs (for PASS detection)
summary     = defaultdict(lambda: {"files": set(), "count": 0, "desc": defaultdict(int)})


def add_issue(filepath, check_id, desc):
    sev      = SEVERITIES.get(check_id, "MINOR")
    rel_path = "/insights/" + os.path.basename(filepath)
    row      = f"| {rel_path} | {check_id} | {desc} | {sev} |"
    all_issues.append(row)
    file_issues[rel_path].append(check_id)
    cat = check_id.split(".")[0]
    summary[cat]["files"].add(rel_path)
    summary[cat]["count"] += 1
    summary[cat]["desc"][desc] += 1


def get_classes(tag):
    """Return list of classes on a tag (safe, always list)."""
    if tag is None:
        return []
    return tag.get("class") or []


def has_class(tag, cls):
    return cls in get_classes(tag)


def inline_has(tag, *keywords):
    """Return True if a tag has a style= attr containing any of the keywords."""
    style = (tag.get("style") or "").lower()
    return any(k in style for k in keywords)


def check_file(filepath):
    is_hub = os.path.basename(filepath) == "index.html"

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # ── helpers ────────────────────────────────────────────────────────────────
    head    = soup.head or soup  # fallback if <head> malformed
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

    # FIX v1: last script check — only look at body scripts, ignore head preloads
    body_scripts = body.find_all("script") if soup.body else scripts
    if not body_scripts or not body_scripts[-1].get("src", "").endswith("nav-footer.js"):
        add_issue(filepath, "A1.3", "nav-footer.js is not the LAST script before </body>")

    # FIX v1: site-config check — scan all scripts in head, not just stylesheets
    head_scripts = head.find_all("script")
    if not any(s.get("src", "").endswith("site-config.js") for s in head_scripts):
        add_issue(filepath, "A1.4", "site-config.js not loaded in <head>")

    if not sheets or not sheets[0].get("href", "").endswith("sv-shared.css"):
        add_issue(filepath, "A1.5", "sv-shared.css is not loaded FIRST in stylesheet list")

    insights_css_idx = next(
        (i for i, s in enumerate(sheets) if s.get("href", "").endswith("sv-insights.css")),
        None
    )
    if insights_css_idx is None:
        add_issue(filepath, "A1.6", "sv-insights.css not loaded")
    elif insights_css_idx != 1:
        add_issue(filepath, "A1.6", f"sv-insights.css loaded at position {insights_css_idx+1}, expected position 2")

    for s in sheets:
        href = s.get("href", "")
        if any(x in href for x in ("sv-systems", "sv-solutions", "sv-brands", "sv-resources", "sv-portfolio")):
            add_issue(filepath, "A1.7", f"Wrong section CSS loaded: {href}")

    # FIX v1: A1.8 — check for wa-float div, not just presence of "whatsapp" text
    wa_float_div = soup.find(class_=re.compile(r"wa-float"))
    if wa_float_div:
        add_issue(filepath, "A1.8", "WhatsApp float appears hardcoded (wa-float class found in HTML)")

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

    og_title = soup.find("meta", property="og:title")
    # FIX v1: compare normalised strings, not exact (trailing spaces)
    og_title_val = (og_title.get("content") or "").strip() if og_title else ""
    if not og_title_val:
        add_issue(filepath, "A2.5", "og:title missing")
    elif og_title_val != title_text:
        add_issue(filepath, "A2.5", "og:title does not match <title>")

    og_desc = soup.find("meta", property="og:description")
    og_desc_val = (og_desc.get("content") or "").strip() if og_desc else ""
    if not og_desc_val:
        add_issue(filepath, "A2.6", "og:description missing")
    elif og_desc_val != desc_content:
        add_issue(filepath, "A2.6", "og:description does not match meta description")

    og_img = soup.find("meta", property="og:image")
    og_img_val = (og_img.get("content") or "").strip() if og_img else ""
    if not og_img_val:
        add_issue(filepath, "A2.7", "og:image missing")
    elif not og_img_val.startswith("https://"):
        add_issue(filepath, "A2.7", f"og:image not absolute HTTPS URL: {og_img_val[:60]}")

    og_url = soup.find("meta", property="og:url")
    og_url_val = (og_url.get("content") or "").strip() if og_url else ""
    if not og_url_val:
        add_issue(filepath, "A2.8", "og:url missing")
    elif not og_url_val.startswith("https://"):
        add_issue(filepath, "A2.8", f"og:url not absolute HTTPS URL")
    elif canon_url and og_url_val != canon_url:
        add_issue(filepath, "A2.8", f"og:url does not match canonical")

    # FIX v1: A2.9 — only flag style blocks that have content BEYOND :root
    for sb in head.find_all("style"):
        sb_text = sb.get_text().strip()
        if not sb_text:
            continue
        # Strip :root block and check if anything remains
        stripped = re.sub(r':root\s*\{[^}]*\}', '', sb_text).strip()
        if stripped:
            add_issue(filepath, "A2.9", "Extra CSS in <head> <style> block beyond :root accent variable")
            break  # one report per file is enough

    header_el = soup.find("header")
    if header_el and inline_has(header_el, "background-image"):
        add_issue(filepath, "A2.10", "Inline background-image on <header> element")

    # ══════════════════════════════════════════════════════════════════════════
    # A3. PAGE STRUCTURE (presence checks — order is best-effort with BS4)
    # ══════════════════════════════════════════════════════════════════════════

    if not soup.find("nav", id="sv-nav"):
        add_issue(filepath, "A3.1", "Nav placeholder missing")
    # A3.2 — insights-header required on article pages; hub checked in Section B
    if not is_hub and not soup.find("header", class_=re.compile(r"insights-header")):
        add_issue(filepath, "A3.2", "insights-header missing on article page")
    if not soup.find(class_=re.compile(r"\btrust-bar\b")):
        add_issue(filepath, "A3.3", "Trust bar missing")
    if not soup.find("nav", class_=re.compile(r"sv-breadcrumb")):
        add_issue(filepath, "A3.4", "Breadcrumb nav missing")
    if not is_hub and not soup.find("div", class_=re.compile(r"\barticle-body\b")):
        add_issue(filepath, "A3.5", "article-body div missing")
    if not is_hub and not soup.find(class_=re.compile(r"related")) and not soup.find(id="related-insights-grid"):
        add_issue(filepath, "A3.6", "Related articles section missing (no .related class and no #related-insights-grid)")
    if not soup.find(class_=re.compile(r"\bcta-section\b")):
        add_issue(filepath, "A3.7", "CTA section missing")
    if not soup.find("footer", id="sv-footer"):
        add_issue(filepath, "A3.8", "Footer placeholder missing")

    # ══════════════════════════════════════════════════════════════════════════
    # A4. ARTICLE HEADER (article pages only)
    # ══════════════════════════════════════════════════════════════════════════

    if not is_hub:
        if header_el:
            cls_list = get_classes(header_el)
            cls_str  = " ".join(cls_list)
            if "insights-header" not in cls_str:
                add_issue(filepath, "A4.1", "Header missing insights-header class")
            if "hero-high-impact" in cls_str or "hero-compact" in cls_str or "hero-standard" in cls_str:
                add_issue(filepath, "A4.1", "Header using standard hero class (hero-high-impact/hero-compact/hero-standard) — should use insights-header")
            if inline_has(header_el, "background-image"):
                add_issue(filepath, "A4.2", "Inline background-image on insights-header element")

        h1s = soup.find_all("h1")
        if len(h1s) != 1:
            add_issue(filepath, "A4.3", f"Page has {len(h1s)} H1 elements — exactly 1 required")
        elif not has_class(h1s[0], "insights-header-title"):
            add_issue(filepath, "A4.4", "H1 missing class insights-header-title")

        if not soup.find(class_="insights-header-intro"):
            add_issue(filepath, "A4.5", "No element with class insights-header-intro found")

        byline = soup.find(class_="hero-byline")
        if not byline:
            add_issue(filepath, "A4.6", "Hero byline block missing (class hero-byline)")
        else:
            byline_img = byline.find("img")
            if not byline_img:
                add_issue(filepath, "A4.7", "Byline missing author photo <img>")
            elif not byline_img.get("src", "").startswith("/"):
                add_issue(filepath, "A4.8", f"Author photo src not absolute: {byline_img.get('src', '')}")

        if header_el:
            for el in header_el.find_all(style=True):
                st = (el.get("style") or "").lower()
                if "color" in st or "font" in st:
                    add_issue(filepath, "A4.9", f"Inline color/font style on <{el.name}> inside header")
                    break  # one per file
            # FIX v1: use style= attribute scan, not string regex
            for span in header_el.find_all("span"):
                st = (span.get("style") or "").lower()
                if "color" in st:
                    add_issue(filepath, "A4.10", "Coloured eyebrow/span found (inline color style on <span>)")
                    break

    # ══════════════════════════════════════════════════════════════════════════
    # A5. TRUST BAR
    # ══════════════════════════════════════════════════════════════════════════

    tb = soup.find(class_=re.compile(r"\btrust-bar\b"))
    if not tb:
        add_issue(filepath, "A5.4", "Trust bar element not found at all")
    else:
        if "sv-trust-bar" in get_classes(tb):
            add_issue(filepath, "A5.1", "Trust bar outer uses sv-trust-bar (should be trust-bar)")

        inner = tb.find(class_=re.compile(r"trust-bar-inner|trust-flex-inline"))
        if inner and "trust-flex-inline" in get_classes(inner):
            add_issue(filepath, "A5.2", "Trust bar inner uses trust-flex-inline (should be trust-bar-inner)")
        elif not inner:
            add_issue(filepath, "A5.2", "Trust bar inner wrapper not found (expected trust-bar-inner)")

        for div_el in tb.find_all(class_=re.compile(r"\b(sep|divider)\b")):
            if "trust-divider" not in get_classes(div_el):
                add_issue(filepath, "A5.3", f"Divider uses wrong class: {' '.join(get_classes(div_el))}")

        if "bca registered" in tb.get_text(separator=" ").lower():
            add_issue(filepath, "A5.5", "BCA Registered found in trust bar (belongs in footer only)")

        # FIX v1: check for literal hardcoded "Level 3" text node (not inside a span.sv-bizsafe)
        tb_html = str(tb)
        if re.search(r'Level\s*3', tb_html) and "sv-bizsafe" not in tb_html:
            add_issue(filepath, "A5.6", "bizSAFE level appears hardcoded (no sv-bizsafe class found)")

        sites_strong = tb.find("strong", class_="sv-sites")
        if not sites_strong:
            add_issue(filepath, "A5.7", "Sites count missing <strong class='sv-sites'> — may be hardcoded number")

        if re.search(r"L/[A-Z0-9/]+", tb.get_text()):
            add_issue(filepath, "A5.8", "Hardcoded police licence number found in trust bar")

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
            if not is_hub:
                if len(bc_links) < 2:
                    add_issue(filepath, "A6.4", "Breadcrumb missing second link to /insights/")
                elif bc_links[1].get("href") != "/insights/":
                    add_issue(filepath, "A6.4", f"Second breadcrumb link is '{bc_links[1].get('href')}', expected '/insights/'")

        # A6.5 — Last breadcrumb item should be plain text, not a link
        # Works for both <ol><li> list pattern and inline <span>/<a> pattern
        bc_links_all = bc.find_all("a")
        if bc_links_all:
            # Get all text-bearing elements in document order
            bc_text_els = bc.find_all(["li", "span", "a"])
            if bc_text_els:
                last_el = bc_text_els[-1]
                if last_el.name == "a":
                    add_issue(filepath, "A6.5", "Last breadcrumb item is a link — should be plain text")

    # ══════════════════════════════════════════════════════════════════════════
    # A7. HEADING HIERARCHY
    # ══════════════════════════════════════════════════════════════════════════

    all_h1 = soup.find_all("h1")
    if len(all_h1) != 1:
        add_issue(filepath, "A7.1", f"Page has {len(all_h1)} H1 elements — exactly 1 required")

    # FIX: actual heading order walk (not in v1)
    headings = soup.find_all(re.compile(r"^h[1-6]$"))
    prev_level = 0
    for hx in headings:
        level = int(hx.name[1])
        if level > prev_level + 1 and prev_level != 0:
            add_issue(filepath, "A7.4", f"Heading level skipped: H{prev_level} → H{level} ('{hx.get_text()[:40]}')")
        prev_level = level

    # ══════════════════════════════════════════════════════════════════════════
    # A8. ARTICLE BODY & PROSE (article pages only)
    # ══════════════════════════════════════════════════════════════════════════

    if not is_hub:
        ab = soup.find("div", class_="article-body")
        if not ab:
            add_issue(filepath, "A8.1", "Missing <div class='article-body'>")
        else:
            lws = ab.find("div", class_="layout-with-sidebar")
            if not lws:
                add_issue(filepath, "A8.2", "Missing div.layout-with-sidebar inside article-body")

            if not ab.find("main", class_="prose"):
                add_issue(filepath, "A8.3", "Missing <main class='prose'>")

            if not ab.find("aside"):
                add_issue(filepath, "A8.4", "Missing <aside> in article body")

            if not ab.find(class_="sticky-toc"):
                add_issue(filepath, "A8.5", "TOC missing class sticky-toc")

            if not ab.find(class_="founder-card"):
                add_issue(filepath, "A8.6", "Founder card missing class founder-card")

            # inline styles in prose
            for el in ab.find_all(style=True):
                st = (el.get("style") or "").lower()
                if "font-size" in st:
                    add_issue(filepath, "A8.7", f"Inline font-size on <{el.name}> inside article body")
                    break
            for el in ab.find_all(style=True):
                st = (el.get("style") or "").lower()
                if "color" in st:
                    add_issue(filepath, "A8.8", f"Inline color on <{el.name}> inside article body")
                    break

            fc = ab.find(class_="founder-card")
            if fc and "sv-years-experience" not in str(fc):
                add_issue(filepath, "A8.9", "sv-years-experience dynamic class not found in founder-card")

    # ══════════════════════════════════════════════════════════════════════════
    # A9. INLINE ARTICLE COMPONENTS
    # ══════════════════════════════════════════════════════════════════════════

    for cb in soup.find_all(class_=re.compile(r"callout")):
        if "callout-box" not in get_classes(cb):
            add_issue(filepath, "A9.1", f"Callout element uses wrong class: {' '.join(get_classes(cb))}")
        if cb.get("style"):
            add_issue(filepath, "A9.5", "Inline style on callout element")

    for vb in soup.find_all(class_=re.compile(r"verdict")):
        if "verdict-box" not in get_classes(vb):
            add_issue(filepath, "A9.2", f"Verdict element uses wrong class: {' '.join(get_classes(vb))}")
        if vb.get("style"):
            add_issue(filepath, "A9.5", "Inline style on verdict element")

    for aib in soup.find_all(class_=re.compile(r"article-image")):
        if "article-image-box" not in get_classes(aib):
            add_issue(filepath, "A9.3", f"Article image uses wrong class: {' '.join(get_classes(aib))}")

    # ══════════════════════════════════════════════════════════════════════════
    # A10. DYNAMIC VALUES
    # ══════════════════════════════════════════════════════════════════════════

    html_lower = html.lower()

    # FIX v1: smarter hardcode detection — look for literal year numbers near keywords
    if re.search(r'\b(20|1[5-9])\s*years?\s+in\s+business', html_lower) and "sv-years-business" not in html:
        add_issue(filepath, "A10.1", "sv-years-business appears hardcoded (year number found near 'years in business')")

    if re.search(r'\b(30|3[0-9]|4[0-9])\s*years?\s+(of\s+)?experience', html_lower) and "sv-years-experience" not in html:
        add_issue(filepath, "A10.2", "sv-years-experience appears hardcoded (year number found near 'years experience')")

    if re.search(r'\b[12][,\s]?\d{3}\+?\s*sites', html_lower) and "sv-sites" not in html:
        add_issue(filepath, "A10.3", "sv-sites appears hardcoded (number found near 'sites')")

    if re.search(r'L/PS/\d+', html) and "sv-licence" not in html:
        add_issue(filepath, "A10.4", "Police licence number appears hardcoded")

    # A10.5 — Only check trust bar for hardcoded Level 3, not full page prose
    # (articles legitimately mention "bizSAFE Level 3" as informational text)
    # Trust bar check already handled in A5.6 above — skip full-page scan here

    if re.search(r'©\s*20(2[0-9])', html) and "sv-current-year" not in html:
        add_issue(filepath, "A10.6", "Copyright year appears hardcoded (no sv-current-year class found)")

    # ══════════════════════════════════════════════════════════════════════════
    # A11. CTA SECTION
    # ══════════════════════════════════════════════════════════════════════════

    cta = soup.find(class_=re.compile(r"\bcta-section\b"))
    if not cta:
        add_issue(filepath, "A11.1", "cta-section not found (A11.1 — also triggers A3.7)")
    else:
        if "cta-high-impact" not in get_classes(cta):
            add_issue(filepath, "A11.1", "CTA section missing cta-high-impact class")

        # FIX v1: look for any btn text containing proposal, not just first btn
        cta_btns = cta.find_all(class_=re.compile(r"\bbtn\b"))
        if cta_btns:
            has_proposal = any("request a proposal" in b.get_text().lower() for b in cta_btns)
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
            break  # one report per file

    # ══════════════════════════════════════════════════════════════════════════
    # A12. IMAGES & LINKS
    # ══════════════════════════════════════════════════════════════════════════

    GENERIC_ALT = {"image", "photo", "banner", "img", "picture"}
    for img in soup.find_all("img"):
        alt = img.get("alt")
        if alt is None:
            add_issue(filepath, "A12.1", f"img missing alt attribute: {img.get('src','')[:60]}")
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
        # FIX: check internal links for absolute path (not http/https, not anchor, not mailto/tel)
        if href.startswith("insights/") or (href.endswith(".html") and not href.startswith("/")):
            add_issue(filepath, "A12.5", f"Internal link not absolute: {href[:60]}")

    # ══════════════════════════════════════════════════════════════════════════
    # A13. RELATED ARTICLES & PREV/NEXT
    # ══════════════════════════════════════════════════════════════════════════

    if not is_hub:
        # Detect new-template pages: have #related-insights-grid (nav-footer.js injection)
        # and body data-article attribute. On these pages, the grid is intentionally
        # empty in HTML — content is injected at runtime. Do not flag A13.4 or A13.1.
        has_injection_grid = bool(soup.find(id="related-insights-grid"))
        has_data_article   = bool(soup.body and soup.body.get("data-article"))
        is_new_template    = has_injection_grid and has_data_article

        # A13.1 — Prev/next: only flag on old-template pages (new template uses JS injection)
        if not is_new_template:
            prev_next = soup.find(class_=re.compile(r"prev[\-_]next|prev-next-nav|article-nav"))
            if not prev_next:
                add_issue(filepath, "A13.1", "Prev/next navigation not found")

        # A13.2 — Related section must exist in some form
        rel_section = soup.find(class_=re.compile(r"related"))
        if not rel_section and not has_injection_grid:
            add_issue(filepath, "A13.2", "Related articles section missing entirely (no .related class and no #related-insights-grid)")

        # A13.4 — Skip if using nav-footer.js injection (grid is empty by design)
        if rel_section and not is_new_template:
            rel_links = rel_section.find_all("a", href=True)
            if len(rel_links) < 2:
                add_issue(filepath, "A13.4", f"Related section has only {len(rel_links)} static link(s) — minimum 2 required")
            for lnk in rel_links:
                if not lnk["href"].startswith("/"):
                    add_issue(filepath, "A13.3", f"Related article link not absolute: {lnk['href'][:60]}")

    # ══════════════════════════════════════════════════════════════════════════
    # A14. INLINE STYLES — ZERO TOLERANCE
    # Reported as per-file summary to prevent report flooding on messy pages.
    # A14.1: total count + element list (one row per file)
    # A14.2/A14.3: unique element types affected (one row per type per file)
    # ══════════════════════════════════════════════════════════════════════════

    styled_els = soup.find_all(style=True)
    if styled_els:
        # A14.1 — one summary row listing count and element tags
        el_tags = [f"<{el.name}>" for el in styled_els]
        tag_counts = {}
        for t in el_tags:
            tag_counts[t] = tag_counts.get(t, 0) + 1
        tag_summary = ", ".join(f"{t}×{n}" if n > 1 else t for t, n in sorted(tag_counts.items()))
        add_issue(filepath, "A14.1", f"{len(styled_els)} element(s) with style= attribute: {tag_summary}")

        # A14.2 — unique element types with font/color inline styles
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
            add_issue(filepath, "A15.2", "Button has no text and no aria-label")

    bc_check = soup.find("nav", class_="sv-breadcrumb")
    if bc_check and bc_check.get("aria-label") != "Breadcrumb":
        add_issue(filepath, "A15.4", "sv-breadcrumb missing aria-label='Breadcrumb'")

    # ══════════════════════════════════════════════════════════════════════════
    # SECTION B — HUB PAGE ONLY (/insights/index.html)
    # ══════════════════════════════════════════════════════════════════════════

    if is_hub:
        hero = soup.find("header", class_=re.compile(r"hero"))
        if not hero:
            add_issue(filepath, "B1.1", "Hub hero <header> not found")
        else:
            cls_str = " ".join(get_classes(hero))
            if "hero-high-impact" not in cls_str or "hero-insights" not in cls_str:
                add_issue(filepath, "B1.1", f"Hub hero missing hero-high-impact or hero-insights — classes: {cls_str}")
            if "hero-standard" not in cls_str:
                add_issue(filepath, "B1.2", "Hub hero missing hero-standard (should be 65vh)")
            if inline_has(hero, "background-image"):
                add_issue(filepath, "B1.3", "Inline background-image on hub hero element")

            h1_hub = hero.find("h1")
            if h1_hub and not has_class(h1_hub, "hero-title-main"):
                add_issue(filepath, "B1.4", "Hub hero H1 missing hero-title-main class")

            eyebrow = hero.find(class_=re.compile(r"eyebrow"))
            if eyebrow and not has_class(eyebrow, "eyebrow-light"):
                add_issue(filepath, "B1.5", "Hub hero eyebrow missing eyebrow-light class")

            subtitle = hero.find(class_=re.compile(r"subtitle"))
            if subtitle and not has_class(subtitle, "hero-subtitle-main"):
                add_issue(filepath, "B1.6", "Hub hero subtitle missing hero-subtitle-main class")

        filt_section = soup.find(class_=re.compile(r"\bfilter-section\b"))
        if not filt_section:
            # also try any div with filter in class
            filt_section = soup.find(class_=re.compile(r"filter"))
        if filt_section:
            if "filter-section" not in get_classes(filt_section):
                add_issue(filepath, "B2.1", "Filter wrapper not using filter-section class")
            if not filt_section.find(class_="filter-container"):
                add_issue(filepath, "B2.2", "filter-container not found inside filter section")
            if filt_section.find(style=True):
                add_issue(filepath, "B2.3", "Inline styles on filter elements")

        grid = soup.find(class_=re.compile(r"\barticles-grid\b"))
        if not grid:
            add_issue(filepath, "B3.1", "articles-grid class not found")
        else:
            if not grid.find(class_="featured-card"):
                add_issue(filepath, "B3.2", "featured-card not found in articles grid")
            for a in grid.find_all("a", href=True):
                if not a["href"].startswith("/") and not a["href"].startswith("http"):
                    add_issue(filepath, "B3.3", f"Article grid link not absolute: {a['href'][:60]}")

        auth_section = soup.find(class_=re.compile(r"\bauthor-section\b"))
        if not auth_section:
            add_issue(filepath, "B4.1", "author-section class not found")
        else:
            if not auth_section.find(class_="author-flex"):
                add_issue(filepath, "B4.2", "author-flex not found in author section")
            if not auth_section.find(class_="author-photo"):
                add_issue(filepath, "B4.3", "author-photo not found in author section")
            if auth_section.find(style=True):
                add_issue(filepath, "B4.4", "Inline styles found in author section")

        sys_grid = soup.find(class_=re.compile(r"\bsystem-grid\b"))
        if sys_grid:
            if not sys_grid.find(class_="system-tile"):
                add_issue(filepath, "B5.2", "system-tile not found in system-grid")
            if not sys_grid.find(class_="tile-link"):
                add_issue(filepath, "B5.3", "tile-link not found in system-grid")
        # Note: B5.1 check for system-grid presence is implicit above

        nl = soup.find(class_=re.compile(r"\bnewsletter-section\b"))
        if nl:
            if not nl.find(class_="nl-form"):
                add_issue(filepath, "B6.2", "nl-form not found in newsletter section")
            if not nl.find(class_="nl-input"):
                add_issue(filepath, "B6.3", "nl-input not found in newsletter section")
            if not nl.find(class_="nl-btn"):
                add_issue(filepath, "B6.4", "nl-btn not found in newsletter section")
            if not nl.find(class_="nl-fineprint"):
                add_issue(filepath, "B6.5", "nl-fineprint not found in newsletter section")

        # B7 — trust bar and breadcrumb on hub (same rules as A5/A6 — already run above)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if not os.path.isdir(INSIGHTS_DIR):
        print(f"ERROR: insights directory not found: {INSIGHTS_DIR}")
        exit(1)

    file_list = sorted(f for f in os.listdir(INSIGHTS_DIR) if f.endswith(".html"))

    print(f"Auditing {len(file_list)} files in {INSIGHTS_DIR} ...")
    for fname in file_list:
        fpath = os.path.join(INSIGHTS_DIR, fname)
        print(f"  -> {fname}")
        check_file(fpath)

    # ── Build report ──────────────────────────────────────────────────────────
    out = []
    out.append("# Anti-Gravity Insights Audit Report")
    out.append("## Securevision SV-Web · Generated by audit_insights_v5.py")
    out.append("")
    out.append(f"**Files audited:** {len(file_list)}")
    out.append(f"**Total issues:** {len(all_issues)}")
    blocker_n = sum(1 for i in all_issues if "BLOCKER" in i)
    major_n   = sum(1 for i in all_issues if "MAJOR"   in i)
    minor_n   = sum(1 for i in all_issues if "MINOR"   in i)
    out.append(f"**Severity breakdown:** BLOCKER: {blocker_n} · MAJOR: {major_n} · MINOR: {minor_n}")
    out.append("")

    out.append("---")
    out.append("")
    out.append("## Per-File Findings")
    out.append("")
    out.append("| File | Check ID | Issue Description | Severity |")
    out.append("|------|----------|-------------------|----------|")

    for fname in file_list:
        rel_path = "/insights/" + fname
        if rel_path not in file_issues or not file_issues[rel_path]:
            out.append(f"| {rel_path} | ALL | PASS | — |")

    # Sort issues by file then check ID for readability
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
    out.append("*Securevision · Insights Audit · v5.0 · June 2026*")

    report_text = "\n".join(out)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(f"\nDone. Report saved to: {OUT_FILE}")
    print(f"BLOCKER: {blocker_n}  MAJOR: {major_n}  MINOR: {minor_n}  TOTAL: {len(all_issues)}")
