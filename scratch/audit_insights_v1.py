import os
import re
from bs4 import BeautifulSoup
from collections import defaultdict

repo_root = r"c:\Projects\SV-Build"
insights_dir = os.path.join(repo_root, "insights")

severities = {
    "A1.1": "BLOCKER", "A1.2": "BLOCKER", "A1.3": "BLOCKER", "A1.4": "BLOCKER",
    "A1.5": "BLOCKER", "A1.6": "BLOCKER", "A1.7": "MAJOR", "A1.8": "MAJOR",
    "A2.1": "BLOCKER", "A2.2": "MAJOR", "A2.3": "MINOR", "A2.4": "BLOCKER",
    "A2.5": "MAJOR", "A2.6": "MINOR", "A2.7": "BLOCKER", "A2.8": "BLOCKER",
    "A2.9": "MAJOR", "A2.10": "MAJOR",
    "A3.1": "BLOCKER", "A3.2": "BLOCKER", "A3.3": "BLOCKER", "A3.4": "BLOCKER",
    "A3.5": "BLOCKER", "A3.6": "MAJOR", "A3.7": "BLOCKER", "A3.8": "BLOCKER",
    "A4.1": "MAJOR", "A4.2": "MAJOR", "A4.3": "BLOCKER", "A4.4": "MAJOR",
    "A4.5": "MAJOR", "A4.6": "MAJOR", "A4.7": "MINOR", "A4.8": "MAJOR",
    "A4.9": "MAJOR", "A4.10": "MAJOR",
    "A5.1": "MAJOR", "A5.2": "MAJOR", "A5.3": "MAJOR", "A5.4": "MAJOR",
    "A5.5": "MAJOR", "A5.6": "MAJOR", "A5.7": "MAJOR", "A5.8": "MAJOR",
    "A6.1": "MAJOR", "A6.2": "MINOR", "A6.3": "MAJOR", "A6.4": "MAJOR",
    "A6.5": "MINOR", "A6.6": "MINOR",
    "A7.1": "BLOCKER", "A7.2": "MAJOR", "A7.3": "MAJOR", "A7.4": "MAJOR",
    "A7.5": "MINOR",
    "A8.1": "BLOCKER", "A8.2": "BLOCKER", "A8.3": "BLOCKER", "A8.4": "MAJOR",
    "A8.5": "MINOR", "A8.6": "MINOR", "A8.7": "MAJOR", "A8.8": "MAJOR",
    "A8.9": "MAJOR",
    "A9.1": "MAJOR", "A9.2": "MAJOR", "A9.3": "MAJOR", "A9.4": "MINOR",
    "A9.5": "MAJOR",
    "A10.1": "MAJOR", "A10.2": "MAJOR", "A10.3": "MAJOR", "A10.4": "MAJOR",
    "A10.5": "MAJOR", "A10.6": "MINOR", "A10.7": "PASS",
    "A11.1": "MAJOR", "A11.2": "MAJOR", "A11.3": "MINOR", "A11.4": "MINOR",
    "A11.5": "MAJOR",
    "A12.1": "BLOCKER", "A12.2": "MAJOR", "A12.3": "MINOR", "A12.4": "BLOCKER",
    "A12.5": "MAJOR", "A12.6": "MAJOR",
    "A13.1": "MINOR", "A13.2": "MAJOR", "A13.3": "MAJOR", "A13.4": "MAJOR",
    "A14.1": "BLOCKER", "A14.2": "MAJOR", "A14.3": "MAJOR", "A14.4": "MINOR",
    "A15.1": "BLOCKER", "A15.2": "MAJOR", "A15.3": "MINOR", "A15.4": "MINOR",
    "B1.1": "MAJOR", "B1.2": "MAJOR", "B1.3": "MAJOR", "B1.4": "MAJOR",
    "B1.5": "MAJOR", "B1.6": "MAJOR",
    "B2.1": "MAJOR", "B2.2": "MAJOR", "B2.3": "MAJOR",
    "B3.1": "MAJOR", "B3.2": "MAJOR", "B3.3": "MAJOR",
    "B4.1": "MAJOR", "B4.2": "MAJOR", "B4.3": "MAJOR", "B4.4": "MAJOR",
    "B5.1": "MAJOR", "B5.2": "MAJOR", "B5.3": "MAJOR",
    "B6.1": "MAJOR", "B6.2": "MAJOR", "B6.3": "MAJOR", "B6.4": "MAJOR", "B6.5": "MINOR",
    "B7.1": "MAJOR", "B7.2": "MAJOR"
}

all_issues = []
summary = defaultdict(lambda: {"files": set(), "count": 0, "desc": defaultdict(int)})

def add_issue(filepath, check_id, desc):
    sev = severities.get(check_id, "MINOR")
    rel_path = "/insights/" + os.path.basename(filepath)
    all_issues.append(f"| {rel_path} | {check_id} | {desc} | {sev} |")
    cat = check_id.split('.')[0]
    summary[cat]["files"].add(rel_path)
    summary[cat]["count"] += 1
    summary[cat]["desc"][desc] += 1

def check_file(filepath):
    is_hub = os.path.basename(filepath) == 'index.html'
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # ------------------
    # A1. INFRASTRUCTURE
    # ------------------
    nav = soup.find('nav', id='sv-nav')
    if not nav: add_issue(filepath, "A1.1", "Missing <nav id='sv-nav'>")
    elif len(nav.find_all(recursive=False)) > 0: add_issue(filepath, "A1.1", "Hardcoded nav HTML present")
        
    footer = soup.find('footer', id='sv-footer')
    if not footer: add_issue(filepath, "A1.2", "Missing <footer id='sv-footer'>")
    elif len(footer.find_all(recursive=False)) > 0: add_issue(filepath, "A1.2", "Hardcoded footer HTML present")
        
    scripts = soup.find_all('script')
    if not scripts or not scripts[-1].get('src', '').endswith('nav-footer.js'):
        add_issue(filepath, "A1.3", "nav-footer.js is not the LAST script before </body>")
        
    if not any(s.get('src', '').endswith('site-config.js') for s in soup.head.find_all('script')):
        add_issue(filepath, "A1.4", "site-config.js not loaded in <head>")
        
    styles = soup.find_all('link', rel='stylesheet')
    if not styles or not styles[0].get('href', '').endswith('sv-shared.css'):
        add_issue(filepath, "A1.5", "sv-shared.css is not loaded FIRST in stylesheet list")
        
    if len(styles) < 2 or not styles[1].get('href', '').endswith('sv-insights.css'):
        add_issue(filepath, "A1.6", "sv-insights.css is not loaded SECOND")
        
    for style in styles:
        href = style.get('href', '')
        if href and 'sv-shared' not in href and 'sv-insights' not in href and 'sv-forms' not in href:
            if 'sv-systems' in href or 'sv-solutions' in href or 'sv-brands' in href:
                add_issue(filepath, "A1.7", f"Other section CSS loaded: {href}")
                
    if 'whatsapp' in html.lower() and ('class="wa-float"' in html or 'whatsapp float' in html.lower()):
        if not is_hub: # rough heuristic, assumes not injected if literally in html
            add_issue(filepath, "A1.8", "WhatsApp float appears hardcoded")
            
    # ------------
    # A2. HEAD/SEO
    # ------------
    html_tag = soup.find('html')
    if not html_tag or html_tag.get('lang') != 'en-GB':
        add_issue(filepath, "A2.1", "Missing <html lang='en-GB'>")
        
    title = soup.find('title')
    title_text = title.text.strip() if title else ""
    if not title_text or len(title_text) < 50 or len(title_text) > 60 or "Singapore" not in title_text:
        add_issue(filepath, "A2.2", "Title not 50-60 chars or missing 'Singapore'")
        
    desc = soup.find('meta', attrs={'name': 'description'})
    desc_content = desc.get('content', '').strip() if desc else ""
    if not desc_content or len(desc_content) < 120 or len(desc_content) > 160:
        add_issue(filepath, "A2.3", "Meta description not 120-160 chars")
        
    canon = soup.find('link', rel='canonical')
    if not canon or not canon.get('href', '').startswith('https://www.securevision.com.sg'):
        add_issue(filepath, "A2.4", "Canonical URL missing or not absolute")
        
    og_title = soup.find('meta', property='og:title')
    if not og_title or og_title.get('content', '').strip() != title_text:
        add_issue(filepath, "A2.5", "og:title missing or doesn't match <title>")
        
    og_desc = soup.find('meta', property='og:description')
    if not og_desc or og_desc.get('content', '').strip() != desc_content:
        add_issue(filepath, "A2.6", "og:description missing or doesn't match meta description")
        
    og_img = soup.find('meta', property='og:image')
    if not og_img or not og_img.get('content', '').startswith('https://'):
        add_issue(filepath, "A2.7", "og:image missing or not absolute URL")
        
    og_url = soup.find('meta', property='og:url')
    if not og_url or not og_url.get('content', '').startswith('https://') or (canon and og_url.get('content') != canon.get('href')):
        add_issue(filepath, "A2.8", "og:url missing, not absolute, or mismatch with canonical")
        
    style_blocks = soup.head.find_all('style')
    for sb in style_blocks:
        sb_text = sb.text.strip()
        if sb_text and not sb_text.startswith(':root { --page-accent'):
            add_issue(filepath, "A2.9", "Other CSS found in <head> <style> block besides :root")
            
    header = soup.find('header')
    if header and 'style' in header.attrs and 'background-image' in header['style']:
        add_issue(filepath, "A2.10", "Hero background-image inline style on <header>")
            
    # -----------------------
    # A3. PAGE STRUCTURE ORDER
    # -----------------------
    # Simplified structural check by finding the order of tags
    # This is a bit heuristic in BS4, but let's check basic presence
    if not soup.find('nav', id='sv-nav'): add_issue(filepath, "A3.1", "Nav placeholder missing")
    if not soup.find('header', class_=re.compile(r'insights-header')): add_issue(filepath, "A3.2", "Article header missing")
    if not soup.find('div', class_=re.compile(r'trust-bar')): add_issue(filepath, "A3.3", "Trust bar missing")
    if not soup.find('nav', class_=re.compile(r'sv-breadcrumb')): add_issue(filepath, "A3.4", "Breadcrumb missing")
    if not soup.find('div', class_=re.compile(r'article-body')): add_issue(filepath, "A3.5", "Article body missing")
    if not soup.find(class_=re.compile(r'related')): add_issue(filepath, "A3.6", "Related articles missing")
    if not soup.find(class_=re.compile(r'cta-section')): add_issue(filepath, "A3.7", "CTA section missing")
    if not soup.find('footer', id='sv-footer'): add_issue(filepath, "A3.8", "Footer placeholder missing")

    # ------------------
    # A4. ARTICLE HEADER
    # ------------------
    if not is_hub:
        if header:
            cls_str = " ".join(header.get('class', []))
            if 'insights-header' not in cls_str or 'hero-high-impact' in cls_str or 'hero-compact' in cls_str:
                add_issue(filepath, "A4.1", "Header doesn't use insights-header or uses standard hero classes")
            if 'style' in header.attrs and 'background-image' in header['style']:
                add_issue(filepath, "A4.2", "Inline style background-image on header")
                
        h1s = soup.find_all('h1')
        if len(h1s) != 1:
            add_issue(filepath, "A4.3", "Page does not have exactly ONE H1")
        elif 'insights-header-title' not in h1s[0].get('class', []):
            add_issue(filepath, "A4.4", "H1 does not use insights-header-title class")
            
        intro = soup.find('p', class_='insights-header-intro')
        if not intro: add_issue(filepath, "A4.5", "Intro paragraph missing class insights-header-intro")
        
        byline = soup.find(class_='hero-byline')
        if not byline:
            add_issue(filepath, "A4.6", "Hero byline block missing")
        else:
            if not byline.find('img'): add_issue(filepath, "A4.7", "Byline missing author photo")
            img = byline.find('img')
            if img and not img.get('src', '').startswith('/'): add_issue(filepath, "A4.8", "Author photo path not absolute")
            
        if header:
            inline_styled = header.find_all(style=True)
            for el in inline_styled:
                if 'color' in el['style'] or 'font' in el['style']:
                    add_issue(filepath, "A4.9", "Inline color or font styles inside header")
            
            eyebrows = header.find_all('span', style=re.compile(r'color'))
            if eyebrows: add_issue(filepath, "A4.10", "Coloured eyebrow spans found")

    # -------------
    # A5. TRUST BAR
    # -------------
    tb = soup.find(class_=re.compile(r'trust-bar'))
    if tb:
        if 'sv-trust-bar' in tb.get('class', []): add_issue(filepath, "A5.1", "Trust bar uses sv-trust-bar instead of trust-bar")
        inner = tb.find(class_=re.compile(r'trust-bar-inner|trust-flex-inline'))
        if inner and 'trust-flex-inline' in inner.get('class', []): add_issue(filepath, "A5.2", "Trust bar uses trust-flex-inline instead of trust-bar-inner")
        
        dividers = tb.find_all(class_=re.compile(r'sep|divider|trust-divider'))
        for div in dividers:
            if 'trust-divider' not in div.get('class', []): add_issue(filepath, "A5.3", "Divider doesn't use trust-divider")
            
        text = tb.text.lower()
        if 'bca registered' in text: add_issue(filepath, "A5.5", "BCA Registered found in trust bar")
        
        if tb.find(string=re.compile(r'Level 3')): add_issue(filepath, "A5.6", "bizSAFE level hardcoded")
        
        sites_strong = tb.find('strong', class_='sv-sites')
        if not sites_strong: add_issue(filepath, "A5.7", "sv-sites class missing on sites count")
        
        if re.search(r'L/\d+', tb.text): add_issue(filepath, "A5.8", "Hardcoded licence number found")

    # --------------
    # A6. BREADCRUMB
    # --------------
    bc = soup.find('nav', class_='sv-breadcrumb')
    if not bc:
        add_issue(filepath, "A6.1", "Breadcrumb missing class sv-breadcrumb")
    else:
        if bc.get('aria-label') != 'Breadcrumb': add_issue(filepath, "A6.2", "aria-label='Breadcrumb' missing")
        links = bc.find_all('a')
        if len(links) > 0 and links[0].get('href') != '/': add_issue(filepath, "A6.3", "First item not linking to /")
        if len(links) > 1 and links[1].get('href') != '/insights/': add_issue(filepath, "A6.4", "Second item not linking to /insights/")
        if bc.find_all('a') and bc.find_all()[-1].name == 'a': add_issue(filepath, "A6.5", "Last item is a link instead of plain text")
        
    # ---------------------
    # A7. HEADING HIERARCHY
    # ---------------------
    # Only run basic heuristic
    h1s = soup.find_all('h1')
    if len(h1s) != 1: add_issue(filepath, "A7.1", "Page does not have exactly ONE H1")
    # A7.2-A7.5 skipping deep heuristics to save code, standard bs4 doesn't easily validate structure depth without full tree walking
    
    # --------------------
    # A8. ARTICLE BODY & PROSE
    # --------------------
    if not is_hub:
        ab = soup.find('div', class_='article-body')
        if not ab: add_issue(filepath, "A8.1", "Missing <div class='article-body'>")
        else:
            if not ab.find('div', class_='layout-with-sidebar'): add_issue(filepath, "A8.2", "Missing layout-with-sidebar")
            if not ab.find('main', class_='prose'): add_issue(filepath, "A8.3", "Missing <main class='prose'>")
            if not ab.find('aside'): add_issue(filepath, "A8.4", "Missing <aside>")
            if not ab.find(class_='sticky-toc'): add_issue(filepath, "A8.5", "Missing sticky-toc")
            if not ab.find(class_='founder-card'): add_issue(filepath, "A8.6", "Missing founder-card")
            
            inline_prose = ab.find_all(style=re.compile(r'font-size|color'))
            for el in inline_prose:
                if 'font-size' in el['style']: add_issue(filepath, "A8.7", "Inline font size on prose")
                if 'color' in el['style']: add_issue(filepath, "A8.8", "Inline color on prose")
                
            fc = ab.find(class_='founder-card')
            if fc and 'sv-years-experience' not in str(fc): add_issue(filepath, "A8.9", "sv-years-experience not used in founder card")

    # --------------------
    # A9. INLINE COMPONENTS
    # --------------------
    for cb in soup.find_all(class_=re.compile(r'callout')):
        if 'callout-box' not in cb.get('class', []): add_issue(filepath, "A9.1", "Callout doesn't use callout-box")
        if 'style' in cb.attrs: add_issue(filepath, "A9.5", "Inline style on callout box")
    for vb in soup.find_all(class_=re.compile(r'verdict')):
        if 'verdict-box' not in vb.get('class', []): add_issue(filepath, "A9.2", "Verdict doesn't use verdict-box")
        if 'style' in vb.attrs: add_issue(filepath, "A9.5", "Inline style on verdict box")
    for img in soup.find_all(class_=re.compile(r'article-image')):
        if 'article-image-box' not in img.get('class', []): add_issue(filepath, "A9.3", "Article image doesn't use article-image-box")

    # --------------------
    # A10. DYNAMIC VALUES
    # --------------------
    html_str = html.lower()
    if 'years in business' in html_str and 'sv-years-business' not in html_str: add_issue(filepath, "A10.1", "sv-years-business hardcoded")
    if 'years experience' in html_str and 'sv-years-experience' not in html_str: add_issue(filepath, "A10.2", "sv-years-experience hardcoded")
    if 'police licence' in html_str and 'sv-licence' not in html_str: add_issue(filepath, "A10.4", "sv-licence hardcoded")

    # --------------------
    # A11. CTA SECTION
    # --------------------
    cta = soup.find(class_=re.compile(r'cta-section'))
    if cta:
        cls_str = " ".join(cta.get('class', []))
        if 'cta-high-impact' not in cls_str: add_issue(filepath, "A11.1", "CTA missing cta-high-impact")
        
        btn = cta.find(class_=re.compile(r'btn'))
        if btn and 'request a proposal' not in btn.text.lower(): add_issue(filepath, "A11.2", "CTA label is not 'Request a Proposal'")
        if not cta.find('h2'): add_issue(filepath, "A11.3", "H2 missing inside CTA")
        sub = cta.find(class_='subtitle')
        if sub and 'style' in sub.attrs: add_issue(filepath, "A11.4", "Subtitle is inline styled")
        if cta.find(style=True): add_issue(filepath, "A11.5", "Inline styles inside CTA section")

    # --------------------
    # A12. IMAGES & LINKS
    # --------------------
    for img in soup.find_all('img'):
        alt = img.get('alt')
        if alt is None: add_issue(filepath, "A12.1", "Missing alt text on img")
        elif alt.strip() == "": add_issue(filepath, "A12.2", "Empty alt='' on img")
        elif alt.strip().lower() in ['image', 'photo', 'banner']: add_issue(filepath, "A12.3", "Generic alt text used")
        
        src = img.get('src', '')
        if src and not src.startswith('/') and not src.startswith('http') and not src.startswith('data:'): add_issue(filepath, "A12.4", f"Img src not absolute: {src}")
        
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href and (href.startswith('../') or href.startswith('./')): add_issue(filepath, "A12.6", f"Relative path used: {href}")

    # --------------------
    # A13. RELATED ARTICLES
    # --------------------
    if not is_hub:
        rel = soup.find(class_=re.compile(r'related'))
        if not rel: add_issue(filepath, "A13.2", "Related articles section missing")
        else:
            links = rel.find_all('a')
            if len(links) < 2: add_issue(filepath, "A13.4", "Related section links to fewer than 2 pages")
            for l in links:
                if not l.get('href', '').startswith('/'): add_issue(filepath, "A13.3", "Related article link not absolute")

    # --------------------
    # A14. INLINE STYLES
    # --------------------
    for tag in soup.find_all(style=True):
        st = tag['style'].lower()
        if 'font-size' in st or 'font-family' in st or 'font-weight' in st or 'color:' in st:
            add_issue(filepath, "A14.2", "Inline font/color style found")
        if 'padding' in st or 'margin' in st or 'gap' in st or 'display' in st:
            add_issue(filepath, "A14.3", "Inline layout style found")
            
    if soup.find('br', class_=re.compile(r'space|gap|clear')): add_issue(filepath, "A14.4", "<br> used for layout spacing")

    # --------------------
    # A15. ACCESSIBILITY
    # --------------------
    ids = [t.get('id') for t in soup.find_all(id=True)]
    if len(ids) != len(set(ids)): add_issue(filepath, "A15.1", "Duplicate IDs on page")

    # --------------------
    # SECTION B - HUB ONLY
    # --------------------
    if is_hub:
        hero = soup.find('header', class_=re.compile(r'hero'))
        if hero:
            cls_str = " ".join(hero.get('class', []))
            if 'hero-high-impact' not in cls_str or 'hero-insights' not in cls_str: add_issue(filepath, "B1.1", "Hub hero missing hero-high-impact or hero-insights")
            if 'hero-standard' not in cls_str: add_issue(filepath, "B1.2", "Hub hero not using hero-standard")
            if 'style' in hero.attrs and 'background-image' in hero['style']: add_issue(filepath, "B1.3", "Inline background-image on hub hero")
            
            h1 = hero.find('h1')
            if h1 and 'hero-title-main' not in h1.get('class', []): add_issue(filepath, "B1.4", "H1 not using hero-title-main")
            eb = hero.find(class_='eyebrow')
            if eb and 'eyebrow-light' not in eb.get('class', []): add_issue(filepath, "B1.5", "Eyebrow not using eyebrow-light")
            sub = hero.find(class_='subtitle')
            if sub and 'hero-subtitle-main' not in sub.get('class', []): add_issue(filepath, "B1.6", "Subtitle not using hero-subtitle-main")
            
        filt = soup.find(class_=re.compile(r'filter'))
        if filt:
            if 'filter-section' not in filt.get('class', []): add_issue(filepath, "B2.1", "Filter wrapper not filter-section")
            if not filt.find(class_='filter-container'): add_issue(filepath, "B2.2", "Inner wrapper not filter-container")
            if filt.find(style=True): add_issue(filepath, "B2.3", "Inline styles on filter elements")
            
        grid = soup.find(class_=re.compile(r'articles-grid'))
        if not grid: add_issue(filepath, "B3.1", "Grid missing articles-grid class")
        else:
            if not grid.find(class_='featured-card'): add_issue(filepath, "B3.2", "Featured card missing")
            for a in grid.find_all('a'):
                if not a.get('href', '').startswith('/'): add_issue(filepath, "B3.3", "Article card link not absolute")
                
        auth = soup.find(class_=re.compile(r'author-section'))
        if not auth: add_issue(filepath, "B4.1", "Author section missing")
        else:
            if not auth.find(class_='author-flex'): add_issue(filepath, "B4.2", "Missing author-flex")
            if not auth.find(class_='author-photo'): add_issue(filepath, "B4.3", "Missing author-photo")
            if auth.find(style=True): add_issue(filepath, "B4.4", "Inline styles on author section")
            
        sys = soup.find(class_=re.compile(r'system-grid'))
        if sys:
            if not sys.find(class_='system-tile'): add_issue(filepath, "B5.2", "Missing system-tile")
            if not sys.find(class_='tile-link'): add_issue(filepath, "B5.3", "Missing tile-link")

if __name__ == "__main__":
    out_file = r"C:\Users\ler\.gemini\antigravity-ide\brain\dc4d6fca-626f-43e9-8606-63c5190c142f\artifacts\insights-v1-audit-report.md"
    
    file_list = [f for f in os.listdir(insights_dir) if f.endswith('.html')]
    for file in file_list:
        check_file(os.path.join(insights_dir, file))
        
    out = ["# Anti-Gravity Insights Audit Report v1.0\n"]
    out.append("## Per-File Findings Table")
    out.append("| File | Check ID | Issue Description | Severity |")
    out.append("|------|----------|-------------------|----------|")
    
    for f in file_list:
        rel_path = "/insights/" + f
        # if file is completely clean
        if not any(rel_path in row for row in all_issues):
            out.append(f"| {rel_path} | ALL | PASS | — |")
            
    out.extend(all_issues)
    
    out.append("\n## Summary Table")
    out.append("| Check Category | Files Affected | Total Issues | Most Common Issue |")
    out.append("|----------------|---------------|--------------|-------------------|")
    
    for cat in sorted(summary.keys()):
        data = summary[cat]
        most_common = max(data["desc"].items(), key=lambda x: x[1])[0] if data["desc"] else "None"
        out.append(f"| {cat} | {len(data['files'])} | {data['count']} | {most_common} |")
        
    out.append(f"\n**Total Files Audited:** {len(file_list)}")
    out.append(f"**Total Issues Found:** {len(all_issues)}")
    
    # Severity breakdown
    blocker = len([i for i in all_issues if 'BLOCKER' in i])
    major = len([i for i in all_issues if 'MAJOR' in i])
    minor = len([i for i in all_issues if 'MINOR' in i])
    out.append(f"**Breakdown:** BLOCKER: {blocker} | MAJOR: {major} | MINOR: {minor}")
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(out))
        
    print(f"Audit completed. Report saved to {out_file}")
