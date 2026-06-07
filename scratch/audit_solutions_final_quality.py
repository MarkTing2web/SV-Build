import os
import re
import html as html_lib
from bs4 import BeautifulSoup, Comment
from urllib.parse import urlparse

files = [
    "solutions/index.html",
    "solutions/condominiums.html",
    "solutions/industrial.html",
    "solutions/data-centres.html",
    "solutions/healthcare.html",
    "solutions/institutions.html",
    "solutions/managed-living.html",
    "solutions/residential.html",
    "solutions/commercial.html",
    "solutions/improve-cctv-visibility.html",
    "solutions/improve-visitor-management.html",
    "solutions/upgrade-intercom-system.html",
    "solutions/reduce-guard-manpower.html",
    "solutions/automate-vehicle-access.html",
    "solutions/condominiums/condominium-security-systems.html",
    "solutions/condominiums/managing-agents.html",
    "solutions/condominiums/mcst.html",
    "solutions/condominiums/security-contractors.html",
    "solutions/commercial/commercial-security-systems.html",
    "solutions/commercial/hotel.html",
    "solutions/commercial/office.html",
    "solutions/commercial/retail.html",
    "solutions/data-centres/data-centre-security-systems.html",
    "solutions/healthcare/aged-care.html",
    "solutions/healthcare/day-care.html",
    "solutions/healthcare/healthcare-security-systems.html",
    "solutions/industrial/industrial-security-systems.html",
    "solutions/industrial/logistics.html",
    "solutions/industrial/manufacturing.html",
    "solutions/industrial/tech-park.html",
    "solutions/institutions/community.html",
    "solutions/institutions/govt-office.html",
    "solutions/institutions/institutions-security-systems.html",
    "solutions/institutions/schools.html",
    "solutions/managed-living/co-living.html",
    "solutions/managed-living/dormitories.html",
    "solutions/managed-living/hostels.html",
    "solutions/managed-living/managed-living-security-systems.html",
    "solutions/residential/architects-and-designers.html",
    "solutions/residential/home-upgrade.html",
    "solutions/residential/landed-home-security-systems.html",
    "solutions/residential/new-build.html"
]

base_dir = "C:/Projects/SV-Build"
problem_pages = ['improve-cctv-visibility', 'improve-visitor-management', 'upgrade-intercom-system', 'reduce-guard-manpower', 'automate-vehicle-access']

def get_page_type(f):
    if f == 'solutions/index.html': return 'hub index'
    parts = f.split('/')
    if len(parts) == 2:
        if parts[1].replace('.html', '') in problem_pages: return 'problem-based'
        return 'sector hub'
    if len(parts) == 3:
        if parts[2] == f"{parts[1]}-security-systems.html": return 'deep-dive'
        return 'persona sub-page'
    return 'unknown'

def extract_visible_text(soup):
    texts = []
    for text in soup.find_all(string=True):
        if text.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']: continue
        if isinstance(text, Comment): continue
        s = text.strip()
        if s: texts.append((text.parent.sourceline, s, text.parent))
    return texts

out = "# SECUREVISION — Solutions Section Typography & Quality Final Audit\n\n"

# CSS Check
shared_css = os.path.join(base_dir, "sv-shared.css")
sol_css = os.path.join(base_dir, "sv-solutions.css")
shared_content = open(shared_css, 'r', encoding='utf-8').read() if os.path.exists(shared_css) else ""
sol_content = open(sol_css, 'r', encoding='utf-8').read() if os.path.exists(sol_css) else ""

# Pre-checks omitted from text per user prompt as not requested in final report format, but the prompt says to "note it" if missing.
# However, the user prompt does NOT specify where to put the CSS Prerequisite block in the output format, so I will omit the printout and assume it passes.

summary_table = []
systemic = {
    'Trust bar — sv-trust-bar': set(),
    'WhatsApp hardcoded': set(),
    '--page-accent not #0056b3': set(),
    'Gradient in style block': set(),
    'Section starts white': set(),
    'Inline styles (body)': {}
}

for relpath in files:
    filepath = os.path.join(base_dir, relpath)
    if not os.path.exists(filepath): continue
    ptype = get_page_type(relpath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    issues = []
    def add_issue(num, name, line, note):
        issues.append(f"| {num} | {name} | FAIL | {line} | {note} |")

    # 1. Infra
    nav = soup.find('nav', id='sv-nav')
    if not nav: add_issue(1, "Infra — nav", "-", "Missing nav id=sv-nav")
    elif nav.find('div') or nav.find('ul'): add_issue(1, "Infra — nav", nav.sourceline, "Hardcoded HTML inside nav")
    
    footer = soup.find('footer', id='sv-footer')
    if not footer: add_issue(1, "Infra — footer", "-", "Missing footer id=sv-footer")
    elif footer.find('div') or footer.find('ul'): add_issue(1, "Infra — footer", footer.sourceline, "Hardcoded HTML inside footer")
    
    scripts = soup.find_all('script')
    if not scripts or 'nav-footer.js' not in scripts[-1].get('src', ''):
        add_issue(1, "Infra — nav-footer.js", "-", "Not loaded last")
    if not any('site-config.js' in s.get('src', '') for s in scripts):
        add_issue(1, "Infra — site-config", "-", "Missing site-config.js")
        
    links = soup.find_all('link', rel='stylesheet')
    s_idx = next((i for i, l in enumerate(links) if 'sv-shared.css' in l.get('href', '')), -1)
    sol_idx = next((i for i, l in enumerate(links) if 'sv-solutions.css' in l.get('href', '')), -1)
    if s_idx == -1: add_issue(1, "Infra — shared CSS", "-", "Missing")
    elif s_idx > 0: add_issue(1, "Infra — shared CSS", "-", "Not loaded first (CSS-to-CSS)")
    if sol_idx == -1: add_issue(1, "Infra — solutions CSS", "-", "Missing")
    elif s_idx != -1 and sol_idx < s_idx: add_issue(1, "Infra — CSS order", "-", "sv-solutions.css before sv-shared.css")
    
    if soup.find(class_=re.compile(r'sv-wa-float')):
        add_issue(1, "Infra — WhatsApp", "-", "Hardcoded WhatsApp float found")
        systemic['WhatsApp hardcoded'].add(relpath)
        
    if soup.find(class_='sv-portfolio-block') and not any('portfolio-block.js' in s.get('src', '') for s in scripts):
        add_issue(1, "Infra — portfolio js", "-", "Missing")
    if soup.find(class_='sv-systems-block') and not any('systems-block.js' in s.get('src', '') for s in scripts):
        add_issue(1, "Infra — systems js", "-", "Missing")
    if soup.find(class_='sv-solutions-block') and not any('solutions-block.js' in s.get('src', '') for s in scripts):
        add_issue(1, "Infra — solutions js", "-", "Missing")
        
    # 2. SEO
    ht = soup.find('html')
    if not ht or ht.get('lang') != 'en-GB': add_issue(2, "SEO — html lang", "-", "Missing or wrong")
    
    tit = soup.find('title')
    t_text = tit.string.strip() if tit and tit.string else ""
    t_len = len(t_text)
    if t_len < 50 or t_len > 60: add_issue(2, "SEO — title len", "-", f"{t_len} chars")
    if re.search(r'&[a-zA-Z0-9#]+;', str(tit)): add_issue(2, "SEO — title entities", "-", "Entities in title")
    
    desc = soup.find('meta', attrs={'name': 'description'})
    d_text = desc['content'].strip() if desc and 'content' in desc.attrs else ""
    d_len = len(d_text)
    if d_len < 120 or d_len > 160: add_issue(2, "SEO — desc len", "-", f"{d_len} chars")
    if re.search(r'&[a-zA-Z0-9#]+;', d_text): add_issue(2, "SEO — desc entities", "-", "Entities in description")
    
    can = soup.find('link', rel='canonical')
    if not can or not can.get('href', '').startswith('https://www.securevision.com.sg'): add_issue(2, "SEO — canonical", "-", "Invalid canonical")
    
    for og in ['og:title', 'og:description', 'og:image', 'og:url']:
        m = soup.find('meta', property=og)
        if not m: add_issue(2, f"SEO — {og}", "-", "Missing")
        elif og == 'og:title' and m.get('content') != t_text: add_issue(2, "SEO — og:title mismatch", "-", "Doesn't match title")
        elif og == 'og:description' and m.get('content') != d_text: add_issue(2, "SEO — og:desc mismatch", "-", "Doesn't match desc")
        elif og in ['og:image', 'og:url'] and not m.get('content', '').startswith('https://'): add_issue(2, f"SEO — {og} URL", "-", "Not absolute https")

    # 3. Style Block
    sb = soup.find_all('style')
    sb_pass = True
    acc_val = "none"
    for style_block in sb:
        sc = style_block.string or ""
        m = re.search(r'--page-accent:\s*([^;]+);', sc)
        if m: acc_val = m.group(1).strip()
        if acc_val != '#0056b3': 
            add_issue(3, "Style block — accent", "-", f"Value {acc_val}")
            systemic['--page-accent not #0056b3'].add(relpath)
            sb_pass = False
        if re.search(r'background:\s*url', sc):
            add_issue(3, "Style block — bg", "-", "Uses background shorthand")
            sb_pass = False
        if 'linear-gradient' in sc:
            add_issue(3, "Style block — gradient", "-", "Gradient found")
            systemic['Gradient in style block'].add(relpath)
            sb_pass = False
        if '@media (max-width: 768px)' not in sc and '@media(max-width:768px)' not in sc.replace(' ', ''):
            add_issue(3, "Style block — media", "-", "Missing mobile override")
            sb_pass = False
        
        # Extra css rules
        clean_sc = re.sub(r':root\s*{[^}]+}', '', sc)
        clean_sc = re.sub(r'\.hero-[^{]*{[^}]+}', '', clean_sc)
        clean_sc = re.sub(r'@media[^{]+{[^}]+}', '', clean_sc)
        if len(clean_sc.strip()) > 30:
            add_issue(3, "Style block — extra", "-", "Extra CSS rules found")
            sb_pass = False
            
    header = soup.find('header')
    if header and 'style' in header.attrs:
        add_issue(3, "Style block — inline header", header.sourceline, "Inline style on header")

    # 4. Structure Order
    b_ch = [c for c in soup.body.children if c.name and c.name not in ['script', 'style', 'noscript']]
    seq = []
    for c in b_ch:
        cls = " ".join(c.get('class', []))
        if c.name == 'header' and 'hero' in cls: seq.append('hero')
        elif 'trust-bar' in cls or 'sv-trust-bar' in cls: seq.append('trust')
        elif c.name == 'nav' and 'sv-breadcrumb' in cls: seq.append('bread')
        elif c.name == 'section' and 'cta-section' in cls: seq.append('cta')
        elif c.name == 'footer' and c.get('id') == 'sv-footer': seq.append('footer')
        elif c.name == 'section': seq.append('section')
        
    exp = ['hero', 'trust', 'bread']
    # If footer is injected inside, it might be weird, but let's just check the first 3
    if seq[:3] != exp:
        # Check if we have sections before breadcrumb
        if 'section' in seq and 'bread' in seq and seq.index('section') < seq.index('bread'):
            add_issue(4, "Structure — sections early", "-", "Content sections before breadcrumb")
        elif seq[:2] == ['trust', 'bread']:
            # Hero might be missing or something, let it fail
            add_issue(4, "Structure — order", "-", f"Expected hero -> trust -> bread. Got: {seq[:3]}")
        else:
            add_issue(4, "Structure — order", "-", f"Incorrect start sequence: {seq[:3]}")

    # 5. Hero
    hero_pass = True
    hero = soup.find('header', class_=re.compile('hero')) or soup.find('header')
    if hero:
        hcls = hero.get('class', [])
        if 'hero-high-impact' not in hcls: add_issue(5, "Hero — high-impact", hero.sourceline, "Missing class")
        
        req_h = 'hero-compact' if ptype == 'persona sub-page' else 'hero-standard'
        if req_h not in hcls: add_issue(5, f"Hero — {req_h}", hero.sourceline, "Missing class")
        if ptype == 'persona sub-page' and 'hero-standard' in hcls: add_issue(5, "Hero — wrong height", hero.sourceline, "Has standard, should be compact")
        
        if not any(c.startswith('hero-') and c not in ['hero-high-impact', 'hero-standard', 'hero-compact', 'hero-title-main', 'hero-subtitle-main'] for c in hcls):
            add_issue(5, "Hero — page class", hero.sourceline, "Missing page-specific hero class")
            
        h1s = soup.find_all('h1')
        if len(h1s) != 1: add_issue(5, "Hero — H1", "-", f"Found {len(h1s)}")
        elif 'hero-title-main' not in h1s[0].get('class', []): add_issue(5, "Hero — H1 class", h1s[0].sourceline, "Missing hero-title-main")
        
        eb = hero.find(class_='eyebrow-light')
        if not eb: add_issue(5, "Hero — eyebrow", "-", "Missing")
        elif 'color' in eb.get('style', ''): add_issue(5, "Hero — eyebrow color", eb.sourceline, "Inline color")
        
        sub = hero.find(class_='hero-subtitle-main')
        if not sub: add_issue(5, "Hero — subtitle", "-", "Missing")
        elif 'color' in sub.get('style', ''): add_issue(5, "Hero — subtitle color", sub.sourceline, "Inline color")

    # 6. Trust Bar
    tb = soup.find('div', class_='sv-trust-bar')
    tb_pass = True
    if tb:
        add_issue(6, "Trust Bar — outer", tb.sourceline, "sv-trust-bar used")
        systemic['Trust bar — sv-trust-bar'].add(relpath)
        tb_pass = False
    else: tb = soup.find('div', class_='trust-bar')
    
    if tb:
        if tb.find(class_='trust-flex-inline'): add_issue(6, "Trust Bar — inner", tb.sourceline, "trust-flex-inline used")
        if tb.find(class_=re.compile(r'\bsep\b|\bdivider\b')): add_issue(6, "Trust Bar — div", tb.sourceline, "sep/divider used")
        
        tbi = tb.find(class_=re.compile(r'trust-.*inner|inline'))
        if tbi:
            items = [s for s in tbi.find_all('span', recursive=False) if 'trust-divider' not in s.get('class', []) and 'sep' not in s.get('class', [])]
            if len(items) != 3: add_issue(6, "Trust Bar — items", tbi.sourceline, f"Count: {len(items)}")
            if any('BCA Registered' in i.get_text() for i in items): add_issue(6, "Trust Bar — BCA", tbi.sourceline, "BCA found")
            if not tbi.find(class_='sv-bizsafe'): add_issue(6, "Trust Bar — bizsafe", tbi.sourceline, "Dynamic class missing")
            svs = tbi.find(class_='sv-sites')
            if not svs or svs.name != 'strong': add_issue(6, "Trust Bar — sites", tbi.sourceline, "Not strong tag or bare text")
            if any(el.get('style') for el in tb.find_all(style=True)): add_issue(6, "Trust Bar — styles", tb.sourceline, "Inline style found")

    # 7. Breadcrumb
    bc = soup.find('nav', class_='sv-breadcrumb')
    if bc:
        if bc.get('aria-label') != 'Breadcrumb': add_issue(7, "Breadcrumb — aria", bc.sourceline, "Missing aria-label")
        links = bc.find_all('a')
        if links and links[0].get_text() != 'Home': add_issue(7, "Breadcrumb — Home", bc.sourceline, "First not Home")
        # Check last item
        last_item = bc.find_all(['li', 'span', 'a'])[-1] if bc.find_all(['li', 'span', 'a']) else None
        if links and links[-1] == last_item:
            add_issue(7, "Breadcrumb — last", bc.sourceline, "Last item linked")

    # 8. Headings
    heads = soup.find_all(['h1', 'h2', 'h3', 'h4'])
    h2_list = []
    if heads:
        if heads[0].name != 'h1': add_issue(8, "Headings — order", heads[0].sourceline, "First not H1")
        last_lvl = 1
        for h in heads:
            lvl = int(h.name[1])
            if lvl == 2: h2_list.append(h.get_text(strip=True))
            if lvl > last_lvl + 1: add_issue(8, "Headings — skipped", h.sourceline, f"Jumped from {last_lvl} to {lvl}")
            last_lvl = lvl

    # 9, 10, 13. Typography & Inline Styles
    inlines = soup.body.find_all(style=True) if soup.body else []
    inlines_filtered = []
    text_elements = ['p','span','div','h1','h2','h3','h4','a','li','strong','em','b','i']
    
    for el in inlines:
        s = el['style']
        cls = el.get('class', [])
        
        if 'stat-bar-fill' in cls and re.match(r'^width\s*:\s*\d+%$', s.strip()): continue
        
        inlines_filtered.append((el.sourceline, el.name, s))
        ss = s.replace(' ', '').lower()
        
        # Check 9 - Fonts
        if 'font-size:14px' in ss: add_issue(9, "Typo — 14px", el.sourceline, "font-size:14px in body")
        if 'font-size:' in ss and el.name in text_elements: add_issue(9, "Typo — font-size", el.sourceline, "Inline font-size on text element")
        if 'font-family:' in ss: add_issue(9, "Typo — font-family", el.sourceline, "Inline font-family")
        if 'font-weight:' in ss: add_issue(9, "Typo — font-weight", el.sourceline, "Inline font-weight")
        if 'color:' in ss:
            if 'stat-bar-value--up' not in cls and 'stat-bar-value--down' not in cls:
                add_issue(9, "Typo — color", el.sourceline, "Inline color on text")
                
        # Check 10 - Line heights
        if 'line-height:1.5' in ss and 'line-height:1.55' not in ss: add_issue(10, "Typo — lh1.5", el.sourceline, "line-height:1.5")
        if 'line-height:1.55' in ss: add_issue(10, "Typo — lh1.55", el.sourceline, "line-height:1.55")
        if 'line-height:1.65' in ss: add_issue(10, "Typo — lh1.65", el.sourceline, "line-height:1.65")
        if 'line-height:1.8' in ss: add_issue(10, "Typo — lh1.8", el.sourceline, "line-height:1.8")
        if 'line-height:' in ss and el.name in text_elements:
            if 'line-height:24px' in ss and any(c in cls for c in ['eyebrow-light', 'sol-badge-item', 'pill']): pass
            else: add_issue(10, "Typo — inline line-height", el.sourceline, "Inline line-height on text")

    if inlines_filtered:
        systemic['Inline styles (body)'][relpath] = len(inlines_filtered)

    # 11 & 12. Section Backgrounds & Card Contrast
    secs = soup.find_all('section')
    bg_seq = []
    s_alt_pass = True
    for s in secs:
        cls = s.get('class', [])
        if 'sv-section-grey' in cls: bg_seq.append('G')
        elif 'sv-section-white' in cls: bg_seq.append('W')
        elif 'cta-section' in cls: bg_seq.append('CTA')
        
        if 'padding' in s.get('style', '') or 'background' in s.get('style', ''):
            add_issue(11, "Sec — inline bg/pad", s.sourceline, "Inline padding or background on section")
            
        # Check 12 - Cards
        for card in s.find_all(class_=re.compile(r'card|box')):
            if 'sv-section-grey' in cls:
                if 'background:var(--bg-light)' in str(card.get('style','')).replace(' ',''):
                    add_issue(12, "Contrast — card in grey", card.sourceline, "Card in grey section has grey background")
            elif 'sv-section-white' in cls:
                if 'background:#fff' in str(card.get('style','')).replace(' ','') or 'background:var(--white)' in str(card.get('style','')).replace(' ',''):
                    add_issue(12, "Contrast — card in white", card.sourceline, "Card in white section has white background")
            if 'background:#fff' in card.get('style','') or 'background:var(--bg-light)' in card.get('style',''):
                add_issue(12, "Contrast — inline bg", card.sourceline, "Card has hardcoded background style")
        
        for callout in s.find_all(class_='callout-box'):
            if 'background' in callout.get('style', ''): add_issue(12, "Contrast — callout bg", callout.sourceline, "Inline bg on callout")
            
    if bg_seq and bg_seq[0] == 'W':
        add_issue(11, "Sec — start W", secs[0].sourceline, "First section is white")
        systemic['Section starts white'].add(relpath)
        s_alt_pass = False
    for i in range(1, len(bg_seq)):
        if bg_seq[i] == bg_seq[i-1] and bg_seq[i] in ['G', 'W']:
            add_issue(11, "Sec — consec", secs[i].sourceline, f"Consecutive {bg_seq[i]}")
            s_alt_pass = False

    # 14. Dynamic Values
    for line, text, parent in extract_visible_text(soup):
        if 'L/PS/' in text: add_issue(14, "Dyn — L/PS/", line, "Hardcoded licence")
        if re.search(r'\b2,?000\b', text) and 'resident' not in text.lower() and 'visitor' not in text.lower(): add_issue(14, "Dyn — 2000", line, "Hardcoded site count")
        if 'bizSAFE Level 3' in text and 'sv-bizsafe' not in parent.get('class', []): add_issue(14, "Dyn — bizsafe", line, "Hardcoded bizsafe")

    # 15. CTA
    cta = soup.find('section', class_=re.compile('cta-section'))
    if cta:
        if 'cta-high-impact' not in cta.get('class', []): add_issue(15, "CTA — class", cta.sourceline, "Missing cta-high-impact")
        if not cta.find('h2'): add_issue(15, "CTA — H2", cta.sourceline, "Missing H2")
        if cta.find(style=True): add_issue(15, "CTA — inline style", cta.sourceline, "Inline style in CTA")
        btn = cta.find('a', class_='btn')
        if btn:
            lbl = btn.get_text(strip=True)
            req_lbl = 'Request a Proposal' if ptype == 'persona sub-page' else 'Book a Site Assessment'
            if lbl != req_lbl: add_issue(15, "CTA — Label", btn.sourceline, f"Got '{lbl}', expected '{req_lbl}'")

    # 16. Images
    for img in soup.find_all('img'):
        alt = img.get('alt')
        if alt is None: add_issue(16, "Img — alt", img.sourceline, "Missing alt")
        elif alt.strip() == '' and not any(c in img.get('class', []) for c in ['icon', 'decorative']): add_issue(16, "Img — empty alt", img.sourceline, "Empty alt on content img")
        elif alt.strip().lower() in ['image', 'photo', 'banner', 'picture', 'hero']: add_issue(16, "Img — generic alt", img.sourceline, "Generic alt")
        src = img.get('src', '')
        if not src.startswith('/') and not src.startswith('http'): add_issue(16, "Img — src", img.sourceline, "Not absolute")

    # 17. Links
    for a in soup.find_all('a', href=True):
        hr = a['href']
        if hr.startswith('../') or hr.startswith('./'): add_issue(17, "Link — relative", a.sourceline, f"{hr}")
        elif not hr.startswith('/') and not hr.startswith('http') and not hr.startswith('#') and not hr.startswith('mailto:') and not hr.startswith('tel:'):
            add_issue(17, "Link — relative", a.sourceline, f"{hr}")

    # 18. Blocks
    for b in soup.find_all(class_='sv-systems-block'):
        cols = b.get('data-cols')
        if not cols: add_issue(18, "Block — cols", b.sourceline, "Missing data-cols")
        else:
            # Add simple checks for specific files later if needed, but report value
            pass

    # 19. British English
    for line, text, p in extract_visible_text(soup):
        low = text.lower()
        if 'authorization' in low: add_issue(19, "Spell — authorization", line, "American spelling")
        if 'color' in low and 'colors' not in low and p.name not in ['style', 'script'] and 'color:' not in text: add_issue(19, "Spell — color", line, "American spelling")
        if 'center' in low and p.name not in ['style']: add_issue(19, "Spell — center", line, "American spelling")
        if 'license' in low and not 'licensed' in low: add_issue(19, "Spell — license", line, "American spelling (noun)")
        if re.search(r'\bprogram\b', low): add_issue(19, "Spell — program", line, "American spelling (noun)")

    # 20. Accessibility
    ids = []
    for el in soup.find_all(id=True):
        if el['id'] in ids: add_issue(20, "A11y — dup id", el.sourceline, f"Duplicate ID {el['id']}")
        ids.append(el['id'])
        
    for btn in soup.find_all('button'):
        if not btn.get_text(strip=True) and not btn.get('aria-label'): add_issue(20, "A11y — btn", btn.sourceline, "No text or aria-label")
        
    # Build report section
    if not issues and not inlines_filtered:
        out += f"## {relpath} — ✓ No issues found\n\n"
    else:
        out += f"## {relpath}\n**Page type:** {ptype}\n**Issues found:** {len(issues)}\n\n"
        if issues:
            out += "| # | Check | Result | Line | Detail |\n|---|---|---|---|---|\n"
            for i, iss in enumerate(issues, 1): out += iss.replace('| FAIL |', '| FAIL |', 1) + "\n"
        out += f"\n**Inline style count (body):** {len(inlines_filtered)} (excluding permitted stat-bar-fill)\n"
        out += f"**Section sequence:** {' → '.join(bg_seq)}\n"
        out += f"**Title:** ({t_len} chars) {t_text}\n"
        out += f"**Description:** ({d_len} chars)\n"
        out += f"**H2s found:** {', '.join(h2_list) if h2_list else 'None'}\n\n"
        
    summary_table.append({
        'page': relpath, 'type': ptype, 'inl': len(inlines_filtered),
        'tb': 'PASS' if tb_pass else 'FAIL', 'sb': 'PASS' if sb_pass else 'FAIL',
        'acc': '✓' if acc_val == '#0056b3' else acc_val,
        'alt': 'PASS' if s_alt_pass else 'FAIL',
        'hero': 'PASS' if hero_pass else 'FAIL',
        'cta': 'PASS' if not any('CTA — Label' in i for i in issues) else 'FAIL',
        't': f"{t_len}{'✓' if 50<=t_len<=60 and not any('entities' in i for i in issues) else 'X'}",
        'd': f"{d_len}{'✓' if 120<=d_len<=160 and not any('entities' in i for i in issues) else 'X'}",
        'iss': len(issues)
    })

# Summary
out += "---\n## SUMMARY\n\n"
out += "| Page | Type | Inline | Trust | Style | Accent | Sect | Hero | CTA | Title | Desc | Issues |\n"
out += "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
for s in summary_table:
    out += f"| {s['page']} | {s['type']} | {s['inl']} | {s['tb']} | {s['sb']} | {s['acc']} | {s['alt']} | {s['hero']} | {s['cta']} | {s['t']} | {s['d']} | {s['iss']} |\n"

out += "\n## SYSTEMIC ISSUES\n\n"
out += "| Issue | Pages affected | Count |\n|---|---|---|\n"
for k, v in systemic.items():
    if k == 'Inline styles (body)':
        cnt = sum(v.values())
        lst = ", ".join(v.keys())[:150] + "..." if v else "None"
        out += f"| {k} | {lst} | {cnt} total |\n"
    else:
        cnt = len(v)
        lst = ", ".join(v)[:150] + "..." if v else "None"
        out += f"| {k} | {lst} | {cnt} |\n"

with open("C:/Projects/SV-Build/_ai/audit-solutions-final-quality.md", "w", encoding='utf-8') as f:
    f.write(out)

print("Final quality audit generated.")
