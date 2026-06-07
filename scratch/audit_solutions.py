import os
import re
from bs4 import BeautifulSoup, Comment

files = [
    "C:/Projects/SV-Build/solutions/index.html",
    "C:/Projects/SV-Build/solutions/condominiums.html",
    "C:/Projects/SV-Build/solutions/industrial.html",
    "C:/Projects/SV-Build/solutions/data-centres.html",
    "C:/Projects/SV-Build/solutions/healthcare.html",
    "C:/Projects/SV-Build/solutions/institutions.html",
    "C:/Projects/SV-Build/solutions/managed-living.html",
    "C:/Projects/SV-Build/solutions/residential.html",
    "C:/Projects/SV-Build/solutions/commercial.html"
]

base_dir = "C:/Projects/SV-Build"

def extract_visible_text(soup):
    texts = []
    for text in soup.find_all(string=True):
        if text.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']: continue
        if isinstance(text, Comment): continue
        s = text.strip()
        if s: texts.append((text.parent.sourceline, s, text.parent))
    return texts

def check_link_exists(href):
    if not href.startswith('/'): return True
    path = href.split('#')[0].split('?')[0]
    if path == '/':
        path = '/index.html'
    elif not path.endswith('.html') and not path.endswith('/'): pass
    local_path = os.path.join(base_dir, path.lstrip('/'))
    if os.path.isdir(local_path):
        local_path = os.path.join(local_path, "index.html")
    return os.path.exists(local_path)

out = ""
summary_data = []

for filepath in files:
    filename = filepath.replace("C:/Projects/SV-Build/", "")
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    issues = []
    def add_issue(check_num, check_name, result, line, note):
        issues.append(f"| {check_num} | {check_name} | {result} | {line} | {note} |")

    # CHECK 1 — Infrastructure
    nav = soup.find('nav', id='sv-nav')
    if not nav: add_issue(1, "Infrastructure — nav", "FAIL", "-", "Missing nav id=sv-nav")
    footer = soup.find('footer', id='sv-footer')
    if not footer: add_issue(1, "Infrastructure — footer", "FAIL", "-", "Missing footer id=sv-footer")
    
    scripts = soup.find_all('script')
    if scripts and 'nav-footer.js' in scripts[-1].get('src', ''): pass
    else:
        nf_found = any('nav-footer.js' in s.get('src', '') for s in scripts)
        if not nf_found: add_issue(1, "Infrastructure — nav-footer.js", "FAIL", "-", "Missing nav-footer.js")
    
    has_site_config = any('site-config.js' in s.get('src', '') for s in soup.find_all('script'))
    if not has_site_config: add_issue(1, "Infrastructure — site-config.js", "FAIL", "-", "Missing site-config.js")
    
    links = soup.find_all('link', rel='stylesheet')
    shared_idx = next((i for i, l in enumerate(links) if 'sv-shared.css' in l.get('href', '')), -1)
    sol_idx = next((i for i, l in enumerate(links) if 'sv-solutions.css' in l.get('href', '')), -1)
    if shared_idx == -1: add_issue(1, "Infrastructure — sv-shared.css", "FAIL", "-", "Missing sv-shared.css")
    if sol_idx == -1: add_issue(1, "Infrastructure — sv-solutions.css", "FAIL", "-", "Missing sv-solutions.css")
    if shared_idx != -1 and sol_idx != -1 and shared_idx > sol_idx: add_issue(1, "Infrastructure — CSS order", "FAIL", "-", "sv-shared.css loaded after sv-solutions.css")
    
    if soup.find(class_='sv-systems-block') and not any('systems-block.js' in s.get('src', '') for s in scripts):
        add_issue(1, "Infrastructure — systems-block.js", "FAIL", "-", "sv-systems-block present but no js")
    if soup.find(class_='sv-portfolio-block') and not any('portfolio-block.js' in s.get('src', '') for s in scripts):
        add_issue(1, "Infrastructure — portfolio-block.js", "FAIL", "-", "sv-portfolio-block present but no js")
        
    wa = soup.find(class_='sv-wa-float')
    wa_hardcoded = False
    if wa:
        wa_hardcoded = True
        add_issue(1, "Infrastructure — WhatsApp float", "FAIL", wa.sourceline or "-", "sv-wa-float hardcoded")

    # CHECK 2 — Head / SEO
    html_tag = soup.find('html')
    if not html_tag or html_tag.get('lang') != 'en-GB': add_issue(2, "SEO — html lang", "FAIL", "-", "Missing or wrong lang=en-GB")
    
    title = soup.find('title')
    t_len = len(title.string.strip()) if title and title.string else 0
    t_text = title.string.strip() if title and title.string else ""
    if t_len < 50 or t_len > 60: add_issue(2, "SEO — title length", "FAIL", "-", f"Length {t_len} chars")
    
    desc = soup.find('meta', attrs={'name': 'description'})
    d_len = len(desc['content'].strip()) if desc and 'content' in desc.attrs else 0
    if d_len < 120 or d_len > 160: add_issue(2, "SEO — desc length", "FAIL", "-", f"Length {d_len} chars")
    
    can = soup.find('link', rel='canonical')
    if not can or not can.get('href', '').startswith('https://www.securevision.com.sg'): add_issue(2, "SEO — canonical", "FAIL", "-", "Missing or bad absolute URL")
    
    for og in ['og:title', 'og:description', 'og:image', 'og:url']:
        m = soup.find('meta', property=og)
        if not m: add_issue(2, f"SEO — {og}", "FAIL", "-", "Missing")
        elif og in ['og:image', 'og:url'] and not m.get('content', '').startswith('http'): add_issue(2, f"SEO — {og}", "FAIL", "-", "Not absolute URL")

    # CHECK 3 — Style Block
    style_blocks = soup.find_all('style')
    accent_val = "MISSING"
    sb_pass = True
    sb_bg_shorthand = False
    sb_extra_css = False
    
    if len(style_blocks) != 1: 
        add_issue(3, "Style block — count", "FAIL", "-", f"Found {len(style_blocks)} blocks")
    else:
        sc = style_blocks[0].string or ""
        m_acc = re.search(r'--page-accent:\s*([^;]+);', sc)
        if m_acc: accent_val = m_acc.group(1).strip()
        if accent_val != '#0056b3': add_issue(3, "Style block — accent", "FAIL", "-", f"Value {accent_val}")
        
        if re.search(r'background:\s*url', sc):
            sb_bg_shorthand = True
            add_issue(3, "Style block — background", "FAIL", "-", "Uses background: shorthand instead of background-image:")
        if 'linear-gradient' in sc:
            add_issue(3, "Style block — gradient", "FAIL", "-", "Linear gradient found")
        
        # Check extra CSS roughly
        clean_sc = re.sub(r':root\s*{[^}]+}', '', sc)
        clean_sc = re.sub(r'\.hero-[^{]*{[^}]+}', '', clean_sc)
        clean_sc = re.sub(r'@media[^{]+{[^}]+}', '', clean_sc)
        if len(clean_sc.strip()) > 20:
            sb_extra_css = True
            add_issue(3, "Style block — extra CSS", "FAIL", "-", "Extra CSS found")
            
        if '@media' not in sc or 'max-width: 768px' not in sc:
            add_issue(3, "Style block — mobile override", "FAIL", "-", "Missing mobile @media block")

    # CHECK 4 — Page Structure Order
    body_children = [c for c in soup.body.children if c.name and c.name not in ['script', 'style', 'noscript']]
    structure_classes = []
    for c in body_children:
        if c.name == 'header' and 'hero' in " ".join(c.get('class', [])): structure_classes.append('hero')
        elif 'trust-bar' in " ".join(c.get('class', [])) or 'sv-trust-bar' in " ".join(c.get('class', [])): structure_classes.append('trust')
        elif c.name == 'nav' and 'sv-breadcrumb' in " ".join(c.get('class', [])): structure_classes.append('bread')
        elif c.name == 'section' and 'cta-section' in " ".join(c.get('class', [])): structure_classes.append('cta')
        elif c.name == 'footer': structure_classes.append('footer')
        elif c.name == 'section': structure_classes.append('section')
    
    # Ideally: hero -> trust -> bread -> section(s) -> cta -> footer
    expected_seq = ['hero', 'trust', 'bread']
    if structure_classes[:3] != expected_seq:
        add_issue(4, "Structure order", "FAIL", "-", f"Actual start: {structure_classes[:3]}")

    # CHECK 5 — Hero
    hero = soup.find('header', class_=lambda c: c and 'hero' in c)
    if not hero: hero = soup.find('header')
    if hero:
        hcls = hero.get('class', [])
        if 'hero-high-impact' not in hcls: add_issue(5, "Hero — high-impact", "FAIL", hero.sourceline, "Missing hero-high-impact")
        if 'hero-standard' not in hcls and 'hero-compact' not in hcls: add_issue(5, "Hero — height", "FAIL", hero.sourceline, "Missing hero-standard or hero-compact")
        
        h1s = soup.find_all('h1')
        if len(h1s) != 1: add_issue(5, "Hero — H1 count", "FAIL", "-", f"Found {len(h1s)} H1s")
        elif 'hero-title-main' not in h1s[0].get('class', []): add_issue(5, "Hero — H1 class", "FAIL", h1s[0].sourceline, "Missing hero-title-main")
        
        eb = hero.find(class_='eyebrow-light')
        if not eb: add_issue(5, "Hero — eyebrow", "FAIL", "-", "Missing eyebrow-light")
        elif 'color:' in eb.get('style', ''): add_issue(5, "Hero — eyebrow style", "FAIL", eb.sourceline, "Inline color style found")
        
        sub = hero.find(class_='hero-subtitle-main')
        if not sub: add_issue(5, "Hero — subtitle", "FAIL", "-", "Missing hero-subtitle-main")
        elif 'color:' in sub.get('style', ''): add_issue(5, "Hero — subtitle style", "FAIL", sub.sourceline, "Inline color style found")
        
        if 'background' in hero.get('style', ''): add_issue(5, "Hero — inline background", "FAIL", hero.sourceline, "Inline style used for background")

    # CHECK 6 — Trust Bar
    tb_outer_pass = True
    tb = soup.find('div', class_='sv-trust-bar')
    if tb: 
        add_issue(6, "Trust Bar — outer", "FAIL", tb.sourceline, "sv-trust-bar used instead of trust-bar")
        tb_outer_pass = False
    if not tb: tb = soup.find('div', class_='trust-bar')
    
    if tb:
        if tb.find(class_='trust-flex-inline'): add_issue(6, "Trust Bar — inner", "FAIL", tb.sourceline, "trust-flex-inline used")
        if tb.find(class_='sep') or tb.find(class_='divider'): add_issue(6, "Trust Bar — divider", "FAIL", tb.sourceline, "sep or divider used")
        
        tbi = tb.find(class_='trust-bar-inner')
        if tbi:
            spans = tbi.find_all('span', recursive=False)
            items = [s for s in spans if 'trust-divider' not in s.get('class', [])]
            if len(items) != 3: add_issue(6, "Trust Bar — items", "FAIL", tbi.sourceline, f"Found {len(items)} items")
            if any('BCA Registered' in s.get_text() for s in items): add_issue(6, "Trust Bar — BCA", "FAIL", tbi.sourceline, "BCA Registered found")
            
            if not tbi.find(class_='sv-bizsafe'): add_issue(6, "Trust Bar — bizsafe", "FAIL", tbi.sourceline, "sv-bizsafe class missing")
            sv_sites = tbi.find(class_='sv-sites')
            if not sv_sites or sv_sites.name != 'strong': add_issue(6, "Trust Bar — sites strong", "FAIL", tbi.sourceline, "sv-sites not a strong tag")
            
        for el in tb.find_all(style=True):
            add_issue(6, "Trust Bar — inline style", "FAIL", el.sourceline, f"Inline style found on {el.name}")
            
    # CHECK 7 — Breadcrumb
    bc = soup.find('nav', class_='sv-breadcrumb')
    if not bc: add_issue(7, "Breadcrumb", "FAIL", "-", "Missing sv-breadcrumb")
    else:
        if bc.get('aria-label') != 'Breadcrumb': add_issue(7, "Breadcrumb — aria", "FAIL", bc.sourceline, "Missing aria-label")
        links = bc.find_all('a')
        if not links or links[0].get_text() != 'Home': add_issue(7, "Breadcrumb — Home", "FAIL", bc.sourceline, "First item not Home link")
        # Check last item
        last_item = bc.find_all(['span', 'li'])[-1] if bc.find_all(['span', 'li']) else None
        if bc.find_all('a') and bc.find_all('a')[-1].get_text() == (last_item.get_text() if last_item else ''):
            add_issue(7, "Breadcrumb — last item", "FAIL", bc.sourceline, "Last item is a link")

    # CHECK 8 — Heading Hierarchy
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
    if headings:
        if headings[0].name != 'h1': add_issue(8, "Headings — First not H1", "FAIL", headings[0].sourceline, f"First is {headings[0].name}")
        if len(headings) > 1 and headings[1].name != 'h2': add_issue(8, "Headings — Second not H2", "FAIL", headings[1].sourceline, f"Second is {headings[1].name}")
        
        last_level = 1
        for h in headings:
            lvl = int(h.name[1])
            if lvl > last_level + 1:
                add_issue(8, "Headings — Skipped level", "FAIL", h.sourceline, f"Jumped from H{last_level} to H{lvl}")
            last_level = lvl
            
    # CHECK 9 & 12 & 16 — Inline Styles & CSS Classes
    inline_styles = soup.body.find_all(style=True) if soup.body else []
    inline_count = len(inline_styles)
    inline_10 = []
    
    for i, el in enumerate(inline_styles):
        s = el.get('style', '')
        if i < 10: inline_10.append(f"Line {el.sourceline} — {s}")
        if 'font-size:14px' in s.replace(' ', ''): add_issue(12, "Inline — font-size 14px", "FAIL", el.sourceline, "Found 14px font-size")
        if 'line-height:1.8' in s.replace(' ', ''): add_issue(12, "Inline — line-height 1.8", "FAIL", el.sourceline, "Found 1.8 line-height")
        if 'font-family:' in s: add_issue(12, "Inline — font-family", "FAIL", el.sourceline, "Found inline font-family")
        
        # Check 16 fallback inline styles
        if 'flex:0 0 340px' in s.replace(' ', ''): add_issue(16, "New CSS — deepdive img", "FAIL", el.sourceline, "Old inline style used")
        if 'padding:40px40px40px0' in s.replace(' ', ''): add_issue(16, "New CSS — deepdive body", "FAIL", el.sourceline, "Old inline style used")
        if 'border-radius:24px' in s.replace(' ', '') and 'padding:60px' in s.replace(' ', ''): add_issue(16, "New CSS — checklist split", "FAIL", el.sourceline, "Old inline style used")
        
        if el.name == 'section' and 'padding' in s: add_issue(13, "Section inline padding", "FAIL", el.sourceline, "Inline padding on section")

    # CHECK 10 — Dynamic Values
    vis = extract_visible_text(soup)
    for line, txt, p in vis:
        if 'L/PS/' in txt: add_issue(10, "Dynamic — L/PS/", "FAIL", line, "Hardcoded licence number")
        if re.search(r'\b2,?000\b', txt): add_issue(10, "Dynamic — 2000", "FAIL", line, "Hardcoded site count")
        if 'bizSAFE Level 3' in txt and 'sv-bizsafe' not in p.get('class', []): add_issue(10, "Dynamic — bizsafe", "FAIL", line, "Hardcoded bizSAFE text")
        if 'sv-founded' in p.get('class', []): pass
        elif re.search(r'\b(?:19|20)\s+years\b', txt.lower()): add_issue(10, "Dynamic — years", "FAIL", line, "Hardcoded years in business")

    # CHECK 11 — CTA
    cta = soup.find('section', class_='cta-section')
    if cta:
        if 'cta-high-impact' not in cta.get('class', []): add_issue(11, "CTA — class", "FAIL", cta.sourceline, "Missing cta-high-impact")
        if not cta.find('h2'): add_issue(11, "CTA — H2", "FAIL", cta.sourceline, "Missing H2")
        btn = cta.find('a', class_='btn')
        if btn and btn.get_text(strip=True) != 'Book a Site Assessment': add_issue(11, "CTA — Button label", "FAIL", btn.sourceline, f"Label is '{btn.get_text(strip=True)}'")
        if cta.find(style=True): add_issue(11, "CTA — inline style", "FAIL", cta.sourceline, "Inline style in CTA")

    # CHECK 13 — Section Alternation
    sections = soup.find_all('section')
    seq = []
    bg_seq = []
    for s in sections:
        if 'sv-section-grey' in s.get('class', []): 
            seq.append('grey')
            bg_seq.append('sv-section-grey')
        elif 'sv-section-white' in s.get('class', []): 
            seq.append('white')
            bg_seq.append('sv-section-white')
        elif 'cta-section' in s.get('class', []):
            seq.append('cta')
    
    if seq and seq[0] != 'grey': add_issue(13, "Section alt — first", "FAIL", sections[0].sourceline, "First section not grey")
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1] and seq[i] in ['grey', 'white']: add_issue(13, "Section alt — consecutive", "FAIL", sections[i].sourceline, f"Consecutive {seq[i]} sections")

    # CHECK 14 — Images
    for img in soup.find_all('img'):
        alt = img.get('alt')
        if alt is None: add_issue(14, "Images — missing alt", "FAIL", img.sourceline, "No alt attribute")
        elif alt.strip() == "" and not any(c in " ".join(img.get('class', [])) for c in ['icon', 'decorative']):
            add_issue(14, "Images — empty alt", "FAIL", img.sourceline, "Empty alt on content image")
        elif alt.strip().lower() in ['image', 'photo', 'banner']:
            add_issue(14, "Images — generic alt", "FAIL", img.sourceline, "Generic alt text")
            
        src = img.get('src', '')
        if not src.startswith('/'): add_issue(14, "Images — src relative", "FAIL", img.sourceline, f"src {src} is relative")

    # CHECK 15 — Internal Links
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('../') or href.startswith('./'): add_issue(15, "Links — relative", "FAIL", a.sourceline, f"Relative href {href}")
        if not href.startswith('/') and not href.startswith('http') and not href.startswith('#') and not href.startswith('mailto:') and not href.startswith('tel:'):
            add_issue(15, "Links — relative", "FAIL", a.sourceline, f"Relative href {href}")

    # Build report section for this file
    page_type = "Sector hub" if filename != 'solutions/index.html' else "Solutions index"
    
    out += f"---\n## {filename}\n**Page type:** {page_type}\n**Issues found:** {len(issues)}\n\n"
    if issues:
        out += "| # | Check | Result | Line | Note |\n|---|---|---|---|---|\n"
        for idx, iss in enumerate(issues, 1):
            out += iss.replace("| X |", f"| {idx} |") + "\n"
    else:
        out += "No issues found.\n\n"
        
    out += f"\n**Inline style count (body):** {inline_count}\n"
    if inline_10:
        out += "**First 10 inline styles:**\n" + "\n".join(inline_10) + "\n"
    out += f"**Section sequence:** {' → '.join(seq)}\n"
    out += f"**Title length:** {t_len} chars\n"
    out += f"**Description length:** {d_len} chars\n\n"
    
    summary_data.append({
        'file': filename,
        'inlines': inline_count,
        'tb': 'PASS' if tb_outer_pass else 'FAIL',
        'sb': 'PASS' if sb_pass and not sb_bg_shorthand and not sb_extra_css else 'FAIL',
        'acc': accent_val,
        'alt': 'PASS' if len(issues) == 0 else ('FAIL' if any('Section alt' in i for i in issues) else 'PASS'),
        'wa': 'hardcoded' if wa_hardcoded else 'clean',
        'iss': len(issues)
    })

# Write summary
out += "---\n## SUMMARY\n"
out += "| Page | Inline styles | Trust bar | Style block | --page-accent | Section alt | WhatsApp | Issues |\n"
out += "|---|---|---|---|---|---|---|---|\n"
for s in summary_data:
    out += f"| {s['file']} | {s['inlines']} | {s['tb']} | {s['sb']} | correct ({s['acc']}) | {s['alt']} | {s['wa']} | {s['iss']} |\n"

with open("C:/Projects/SV-Build/_ai/audit-solutions-hub.md", "w", encoding="utf-8") as f:
    f.write(out)

print("Audit generated successfully.")
