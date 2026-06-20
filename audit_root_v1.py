"""
audit_root_v1.py — Securevision Root Pages Audit Script
Scope:  All .html files directly in the repo root (REPO_ROOT/*.html)
        Excludes subdirectories — those are handled by section-specific scripts.

Action: READ ONLY — no file modifications. Produces markdown report.
Run:    python audit_root_v1.py
Output: root-audit-report-v1.md (set OUT_FILE below)

PAGE TYPES:
  TYPE A — index.html          (homepage — unique: hero-full, no breadcrumb)
  TYPE B — about.html          (content pages with hero + CTA)
  TYPE C — contact.html        (form page — sv-forms.css, CTA optional)
  TYPE D — privacy.html        (utility — no hero, no CTA required)
           terms.html
           sitemap.html
  TYPE E — request-site-assessment-singapore.html
           (form/booking page — sv-forms.css, IS the conversion page)

KEY DIFFERENCES FROM SECTION SCRIPTS:
  - CSS: sv-shared.css only (+ sv-forms.css on form pages)
    No sv-solutions, sv-brands, sv-systems, sv-insights, sv-resources
  - Homepage: hero-full (85vh), NO breadcrumb, NO trust bar required
  - Utility pages (privacy, terms, sitemap): no hero or CTA required
  - Form pages: sv-forms.css required, CTA section optional
  - Flexible CTA check: Book a Site Assessment OR Request a Proposal accepted
    (root pages vary; only flag if neither is present)
"""

import os
import re
from bs4 import BeautifulSoup
from collections import defaultdict

# ─── CONFIGURE PATHS ─────────────────────────────────────────────────────────
REPO_ROOT = r"C:\Projects\SV-Build"
OUT_FILE  = r"C:\Projects\SV-Build\root-audit-report-v1.md"
# ─────────────────────────────────────────────────────────────────────────────

# Pages that are the form/conversion destination — CTA section not expected
FORM_PAGES = {
    "contact.html",
    "request-site-assessment-singapore.html",
    "book-assessment.html",
    "book-site-assessment.html",
    "contact-gateway.html",
}

# Pages that need sv-forms.css
FORM_CSS_PAGES = {
    "contact.html",
    "request-site-assessment-singapore.html",
    "book-assessment.html",
    "book-site-assessment.html",
    "contact-gateway.html",
}

# Utility pages — no hero, no CTA, no trust bar required
UTILITY_PAGES = {
    "privacy.html",
    "terms.html",
    "sitemap.html",
    "404.html",
}

# Pages that are thank-you / success confirmations — very minimal checks
SUCCESS_PAGES = {
    "thank-you.html",
    "success.html",
    "confirmation.html",
    "booking-success.html",
    "contact-success.html",
    "thank-you-booking.html",
    "thank-you-proposal.html",
}

SEVERITIES = {
    "A1.1": "BLOCKER", "A1.2": "BLOCKER", "A1.3": "BLOCKER", "A1.4": "BLOCKER",
    "A1.5": "BLOCKER", "A1.6": "BLOCKER", "A1.7": "MAJOR",   "A1.8": "MAJOR",
    "A1.9": "MAJOR",   # sv-forms.css missing on form page
    "A2.1": "BLOCKER", "A2.2": "MAJOR",   "A2.3": "MINOR",   "A2.4": "BLOCKER",
    "A2.5": "MAJOR",   "A2.6": "MINOR",   "A2.7": "BLOCKER", "A2.8": "BLOCKER",
    "A2.9": "MAJOR",
    "A3.2": "BLOCKER", "A3.3": "MAJOR",   "A3.4": "MAJOR",
    "A3.7": "MAJOR",   "A3.8": "BLOCKER",
    "A4.1": "MAJOR",   "A4.2": "MAJOR",   "A4.3": "BLOCKER", "A4.4": "MAJOR",
    "A5.1": "MAJOR",   "A5.2": "MAJOR",   "A5.3": "MAJOR",   "A5.4": "MAJOR",
    "A5.5": "MAJOR",   "A5.6": "MAJOR",   "A5.7": "MAJOR",   "A5.8": "MAJOR",
    "A6.1": "MAJOR",   "A6.2": "MINOR",   "A6.3": "MAJOR",   "A6.5": "MINOR",
    "A7.1": "BLOCKER", "A7.4": "MAJOR",
    "A8.1": "MAJOR",   "A8.2": "MAJOR",
    "A9.1": "BLOCKER", "A9.2": "MAJOR",   "A9.3": "MINOR",
    "A10.1": "MAJOR",  "A10.2": "MAJOR",  "A10.3": "MAJOR",
    "A10.4": "MAJOR",  "A10.5": "MINOR",
    "A11.1": "BLOCKER","A11.2": "MAJOR",  "A11.3": "MINOR",  "A11.4": "BLOCKER",
    "A11.5": "MAJOR",  "A11.6": "MAJOR",
    "A12.1": "BLOCKER","A12.2": "MAJOR",  "A12.3": "MAJOR",
    "A14.1": "BLOCKER","A14.2": "MAJOR",  "A14.4": "MINOR",
}

all_issues  = []
file_issues = defaultdict(list)
summary     = defaultdict(lambda: {"files": set(), "count": 0, "desc": defaultdict(int)})


def rel_path(filepath):
    fname = os.path.basename(filepath)
    return f"/{fname}"


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


def check_file(filepath):
    fname      = os.path.basename(filepath)
    is_home    = fname == "index.html"
    is_utility = fname in UTILITY_PAGES
    is_form    = fname in FORM_PAGES
    is_success = fname in SUCCESS_PAGES
    needs_form_css = fname in FORM_CSS_PAGES

    # Success/thank-you pages: only check nav/footer infrastructure
    if is_success:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
        soup = BeautifulSoup(html, "html.parser")
        if not soup.find("nav", id="sv-nav"):
            add_issue(filepath, "A1.1", "Missing <nav id='sv-nav'>")
        if not soup.find("footer", id="sv-footer"):
            add_issue(filepath, "A1.2", "Missing <footer id='sv-footer'>")
        body_scripts = soup.body.find_all("script") if soup.body else []
        if not body_scripts or not body_scripts[-1].get("src", "").endswith("nav-footer.js"):
            add_issue(filepath, "A1.3", "nav-footer.js is not the LAST script before </body>")
        return

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

    # Root pages should NOT load section-specific CSS
    for s in sheets:
        href = s.get("href", "")
        if any(x in href for x in ("sv-systems", "sv-solutions", "sv-brands",
                                    "sv-insights", "sv-resources", "sv-portfolio")):
            add_issue(filepath, "A1.7", f"Section-specific CSS loaded on root page: {href}")

    # sv-forms.css required on form pages
    has_forms_css = any(s.get("href", "").endswith("sv-forms.css") for s in sheets)
    if needs_form_css and not has_forms_css:
        add_issue(filepath, "A1.9", "sv-forms.css not loaded — required on form/booking pages")

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
        if "Singapore" not in title_text and not is_utility:
            issues.append("missing 'Singapore'")
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
        stripped = re.sub(r':root\s*\{[^}]*\}', '', sb_text).strip()
        if stripped:
            add_issue(filepath, "A2.9", "Extra CSS in <head> <style> block beyond :root accent variable")
            break

    # ══════════════════════════════════════════════════════════════════════════
    # A3. PAGE STRUCTURE
    # Note: homepage has no breadcrumb; utility pages have no hero or CTA
    # ══════════════════════════════════════════════════════════════════════════

    if not header_el and not is_utility and not is_form:
        add_issue(filepath, "A3.2", "No <header> element found")

    # Trust bar — not required on homepage (it has its own credential section)
    # Required on about, contact, and all others with a hero
    if not is_home and not is_utility and not is_form:
        if not soup.find(class_=re.compile(r"\btrust-bar\b|\bsv-trust-bar\b")):
            add_issue(filepath, "A3.3", "Trust bar missing")

    # Breadcrumb — NOT on homepage; required on all other non-utility pages
    if not is_home and not is_utility:
        if not soup.find("nav", class_=re.compile(r"sv-breadcrumb")):
            add_issue(filepath, "A3.4", "Breadcrumb nav missing")

    if not soup.find("footer", id="sv-footer"):
        add_issue(filepath, "A3.8", "Footer placeholder missing")

    # CTA section — required on homepage and about; optional on form/utility pages
    if is_home or (not is_utility and not is_form and not is_success):
        if not soup.find(class_=re.compile(r"\bcta-section\b")):
            add_issue(filepath, "A3.7", "CTA section missing")

    # ══════════════════════════════════════════════════════════════════════════
    # A4. HERO
    # ══════════════════════════════════════════════════════════════════════════

    if header_el and not is_utility:
        cls_str = " ".join(get_classes(header_el))

        if "hero-high-impact" not in cls_str:
            add_issue(filepath, "A4.1", f"Hero missing hero-high-impact class — classes: {cls_str[:80]}")

        if is_home:
            if "hero-full" not in cls_str:
                add_issue(filepath, "A4.2", "Homepage hero missing hero-full class (should be 85vh)")
        else:
            if "hero-compact" not in cls_str and "hero-standard" not in cls_str:
                add_issue(filepath, "A4.2", "Hero missing hero-compact or hero-standard class")

        h1s = soup.find_all("h1")
        if len(h1s) != 1:
            add_issue(filepath, "A4.3", f"Page has {len(h1s)} H1 elements — exactly 1 required")
        else:
            if not has_class(h1s[0], "hero-title-main"):
                add_issue(filepath, "A4.4", f"H1 missing hero-title-main class — classes: {' '.join(get_classes(h1s[0]))}")

    # ══════════════════════════════════════════════════════════════════════════
    # A5. TRUST BAR (skip homepage and utility pages)
    # ══════════════════════════════════════════════════════════════════════════

    if not is_home and not is_utility and not is_form:
        tb = soup.find(class_=re.compile(r"\btrust-bar\b|\bsv-trust-bar\b"))
        if not tb:
            add_issue(filepath, "A5.4", "Trust bar element not found")
        else:
            if "sv-trust-bar" in get_classes(tb) and "trust-bar" not in get_classes(tb):
                add_issue(filepath, "A5.1", "Trust bar uses legacy sv-trust-bar — migrate to trust-bar")

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
                add_issue(filepath, "A5.6", "bizSAFE level hardcoded (no sv-bizsafe class)")

            if not tb.find("strong", class_="sv-sites"):
                add_issue(filepath, "A5.7", "Sites count missing <strong class='sv-sites'>")

            if re.search(r"L/[A-Z0-9/]+", tb.get_text()):
                add_issue(filepath, "A5.8", "Hardcoded police licence number in trust bar")

    # ══════════════════════════════════════════════════════════════════════════
    # A6. BREADCRUMB (skip homepage and utility pages)
    # ══════════════════════════════════════════════════════════════════════════

    if not is_home and not is_utility:
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
                    add_issue(filepath, "A6.3", f"First crumb is '{bc_links[0].get('href')}', expected '/'")

            bc_text_els = bc.find_all(["li", "span", "a"])
            if bc_text_els and bc_text_els[-1].name == "a":
                add_issue(filepath, "A6.5", "Last breadcrumb item is a link — should be plain text")

    # ══════════════════════════════════════════════════════════════════════════
    # A7. HEADING HIERARCHY
    # ══════════════════════════════════════════════════════════════════════════

    all_h1 = soup.find_all("h1")
    if not is_utility and len(all_h1) != 1:
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
    # A8. FORM STRUCTURE (form pages only)
    # ══════════════════════════════════════════════════════════════════════════

    if is_form or needs_form_css:
        form_el = soup.find("form")
        if not form_el:
            add_issue(filepath, "A8.1", "Form page has no <form> element")
        else:
            # Form should have a submit button
            submit = form_el.find("button", attrs={"type": "submit"}) or \
                     form_el.find("input", attrs={"type": "submit"})
            if not submit:
                add_issue(filepath, "A8.2", "Form missing submit button")

    # ══════════════════════════════════════════════════════════════════════════
    # A9. CTA SECTION (homepage and non-utility, non-form pages)
    # ══════════════════════════════════════════════════════════════════════════

    if not is_utility and not is_form and not is_success:
        cta = soup.find(class_=re.compile(r"\bcta-section\b"))
        if not cta:
            add_issue(filepath, "A9.1", "cta-section not found")
        else:
            if "cta-high-impact" not in get_classes(cta):
                add_issue(filepath, "A9.1", "CTA missing cta-high-impact class")

            cta_btns = cta.find_all(class_=re.compile(r"\bbtn\b"))
            if cta_btns:
                btn_text = " ".join(b.get_text().lower() for b in cta_btns)
                has_assessment = "book" in btn_text and "assessment" in btn_text
                has_proposal   = "request" in btn_text and "proposal" in btn_text
                if not has_assessment and not has_proposal:
                    labels = " / ".join(b.get_text().strip() for b in cta_btns)
                    add_issue(filepath, "A9.2", f"CTA button not 'Book a Site Assessment' or 'Request a Proposal' — found: {labels[:80]}")

            if not cta.find("h2"):
                add_issue(filepath, "A9.3", "H2 missing inside CTA section")

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
    # A12. INLINE STYLES
    # ══════════════════════════════════════════════════════════════════════════

    styled_els = soup.find_all(style=True)
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
# MAIN — scan all .html files directly in REPO_ROOT (no subdirectories)
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if not os.path.isdir(REPO_ROOT):
        print(f"ERROR: repo root not found: {REPO_ROOT}")
        exit(1)

    file_list = sorted(
        os.path.join(REPO_ROOT, f)
        for f in os.listdir(REPO_ROOT)
        if f.endswith(".html") and os.path.isfile(os.path.join(REPO_ROOT, f))
    )

    print(f"Found {len(file_list)} HTML files in repo root")
    print()
    for fpath in file_list:
        fname = os.path.basename(fpath)
        ptype = ("home    " if fname == "index.html" else
                 "utility " if fname in UTILITY_PAGES else
                 "form    " if fname in FORM_PAGES else
                 "success " if fname in SUCCESS_PAGES else
                 "content ")
        print(f"  [{ptype}] /{fname}")
        check_file(fpath)

    out = []
    out.append("# Root Pages Audit Report")
    out.append("## Securevision SV-Web · Generated by audit_root_v1.py")
    out.append("")
    out.append(f"**Files audited:** {len(file_list)}")
    out.append(f"**Total issues:** {len(all_issues)}")
    b = sum(1 for i in all_issues if "BLOCKER" in i)
    m = sum(1 for i in all_issues if "MAJOR"   in i)
    n = sum(1 for i in all_issues if "MINOR"   in i)
    out.append(f"**Severity breakdown:** BLOCKER: {b} · MAJOR: {m} · MINOR: {n}")
    out.append("")
    out.append("**Page type rules:**")
    out.append("  Homepage (index.html): hero-full, no breadcrumb, no trust bar required")
    out.append("  Utility (privacy, terms, sitemap): no hero or CTA required")
    out.append("  Form pages: sv-forms.css required, CTA section optional")
    out.append("  Content pages (about): full checks apply")
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
    out.append("*Securevision · Root Pages Audit · v1.0 · June 2026*")

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"\nDone. Report saved to: {OUT_FILE}")
    print(f"BLOCKER: {b}  MAJOR: {m}  MINOR: {n}  TOTAL: {len(all_issues)}")
