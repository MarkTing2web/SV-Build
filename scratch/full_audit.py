import os
import re
from bs4 import BeautifulSoup, Comment
from datetime import datetime
import collections

base_dir = "C:/Projects/SV-Build"
brands_dir = os.path.join(base_dir, "brands")

files_in_scope = [
    "aiphone-intercom.html", "ajax-alarms.html", "akuvox-access.html", "akuvox-intercom.html",
    "apollo-access.html", "dahua-cctv.html", "dormer-autogate.html", "dsc-alarms.html",
    "ebelco-locks.html", "entrypass-entry-access.html", "faac-autogate.html", "fanvil-intercom.html",
    "fanvil-ip-phone.html", "gantrygo.html", "ge-caddx-alarms.html", "hanwha-cctv.html",
    "hid-entry-access.html", "hikcentral.html", "hikvision-access.html", "hikvision-cctv.html",
    "hikvision-intercom.html", "hrui-network.html", "kocom-intercom.html", "mag-autogate.html",
    "microengine-entry-access.html", "milesight-cctv.html", "omada-network.html", "paradox-alarms.html",
    "risco-alarms.html", "ruijie-reyee-network.html", "suprema-entry-access.html", "uniview-cctv.html",
    "vesta.html", "viro-locks.html", "yealink-ip-phone.html", "yeastar-ippbx.html",
    "zkteco-cvsecurity.html", "zkteco-entry-access.html"
]

results = { i: {} for i in range(1, 11) }
for i in range(1, 11):
    for f in files_in_scope:
        results[i][f] = []

def add_fail(group, filename, check_id, msg, line=None):
    if line:
        results[group][filename].append(f"{check_id}  {msg} — line {line}")
    else:
        results[group][filename].append(f"{check_id}  {msg}")

for filename in files_in_scope:
    filepath = os.path.join(brands_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    slug = filename.replace('.html', '')
    soup = BeautifulSoup(html, 'html.parser')
    
    # GROUP 1: Infrastructure
    if not html.strip().lower().startswith('<!doctype html>'): pass
    html_tag = soup.find('html')
    if not html_tag or html_tag.get('lang') != 'en-GB':
        add_fail(1, filename, '1A', '<html lang="en-GB"> missing or incorrect', html_tag.sourceline if html_tag else 1)
        
    nav = soup.find('nav', id='sv-nav')
    if not nav:
        add_fail(1, filename, '1B', '<nav id="sv-nav"></nav> missing')
    else:
        if nav.find(): add_fail(1, filename, '1H', 'Hardcoded HTML inside <nav id="sv-nav">', nav.sourceline)

    footer = soup.find('footer', id='sv-footer')
    if not footer:
        add_fail(1, filename, '1C', '<footer id="sv-footer"></footer> missing')
    else:
        if footer.find(): add_fail(1, filename, '1I', 'Hardcoded HTML inside <footer id="sv-footer">', footer.sourceline)
        
    scripts = soup.find_all('script')
    if scripts:
        last_script = scripts[-1]
        if 'nav-footer.js' not in last_script.get('src', ''):
            add_fail(1, filename, '1D', '<script src="/nav-footer.js"></script> is not the last script', last_script.sourceline)
    else:
        add_fail(1, filename, '1D', 'No scripts found')
        
    config_script = soup.head.find('script', src='/site-config.js') if soup.head else None
    if not config_script:
        add_fail(1, filename, '1E', '<script src="/site-config.js"></script> not loaded in <head>')
        
    links = soup.head.find_all('link', rel='stylesheet') if soup.head else []
    if len(links) >= 2:
        if '/sv-shared.css' not in links[0].get('href', ''):
            add_fail(1, filename, '1F', '<link rel="stylesheet" href="/sv-shared.css"> not loaded first', links[0].sourceline)
        if '/sv-brands.css' not in links[1].get('href', ''):
            add_fail(1, filename, '1G', '<link rel="stylesheet" href="/sv-brands.css"> not loaded second', links[1].sourceline)
    else:
        add_fail(1, filename, '1F', 'Missing sv-shared.css or sv-brands.css')
        
    if soup.find(class_='sv-wa-float') or soup.find(id='sv-wa-float'):
        el = soup.find(class_='sv-wa-float') or soup.find(id='sv-wa-float')
        add_fail(1, filename, '1J', 'sv-wa-float anchor element present in body', el.sourceline)
        
    # GROUP 2: Head / SEO / Meta
    title_tag = soup.head.find('title') if soup.head else None
    title_text = title_tag.string.strip() if title_tag and title_tag.string else ""
    if not title_tag or not (50 <= len(title_text) <= 60):
        add_fail(2, filename, '2A', f'<title> length {len(title_text)} not between 50-60 chars', title_tag.sourceline if title_tag else 1)
    if 'Singapore' not in title_text:
        add_fail(2, filename, '2A', '<title> missing "Singapore"', title_tag.sourceline if title_tag else 1)
    if 'Securevision' not in title_text:
        add_fail(2, filename, '2A', '<title> missing "Securevision"', title_tag.sourceline if title_tag else 1)
        
    desc_tag = soup.head.find('meta', attrs={'name': 'description'}) if soup.head else None
    desc_text = desc_tag.get('content', '').strip() if desc_tag else ""
    if not desc_tag or not (120 <= len(desc_text) <= 160):
        add_fail(2, filename, '2B', f'<meta name="description"> length {len(desc_text)} not between 120-160 chars', desc_tag.sourceline if desc_tag else 1)
        
    canonical = soup.head.find('link', rel='canonical') if soup.head else None
    expected_url = f'https://www.securevision.com.sg/brands/{filename}'
    if not canonical or canonical.get('href') != expected_url:
        add_fail(2, filename, '2C', f'<link rel="canonical"> missing or incorrect. Expected {expected_url}', canonical.sourceline if canonical else 1)
        
    og_title = soup.head.find('meta', property='og:title') if soup.head else None
    if not og_title or og_title.get('content', '').strip() != title_text:
        add_fail(2, filename, '2D', '<meta property="og:title"> does not match <title>', og_title.sourceline if og_title else 1)
        
    og_desc = soup.head.find('meta', property='og:description') if soup.head else None
    if not og_desc or og_desc.get('content', '').strip() != desc_text:
        add_fail(2, filename, '2E', '<meta property="og:description"> does not match <meta name="description">', og_desc.sourceline if og_desc else 1)
        
    og_url = soup.head.find('meta', property='og:url') if soup.head else None
    if not og_url or og_url.get('content') != expected_url:
        add_fail(2, filename, '2F', '<meta property="og:url"> does not match canonical URL', og_url.sourceline if og_url else 1)
        
    og_image = soup.head.find('meta', property='og:image') if soup.head else None
    if not og_image or og_image.get('content') == 'https://www.securevision.com.sg/images/og-default.jpg':
        add_fail(2, filename, '2G', 'og:image is og-default.jpg or missing', og_image.sourceline if og_image else 1)
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html_raw = f.read()
    title_raw = re.search(r'<title>(.*?)</title>', html_raw, re.IGNORECASE)
    desc_raw = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', html_raw, re.IGNORECASE)
    if title_raw and re.search(r'&[a-zA-Z#0-9]+;', title_raw.group(1)):
        add_fail(2, filename, '2H', 'HTML entity found in title')
    if desc_raw and re.search(r'&[a-zA-Z#0-9]+;', desc_raw.group(1)):
        add_fail(2, filename, '2H', 'HTML entity found in meta description')

    # GROUP 3: Style block
    styles = soup.head.find_all('style') if soup.head else []
    if len(styles) != 1:
        add_fail(3, filename, '3A', f'{len(styles)} <style> blocks found in <head> (expected 1)')
        style_content = ""
    else:
        style_content = styles[0].string or ""
        
        if ':root { --page-accent: #0056b3; }' not in style_content.replace(' ', ''):
            if '--page-accent' not in style_content or '#0056b3' not in style_content:
                add_fail(3, filename, '3B', ':root { --page-accent: #0056b3; } not found or different colour', styles[0].sourceline)
                
        hero_rule = f'.hero-{slug} {{ background-image: url(\'/images/brands/hero-brands/{slug}.webp\'); }}'
        if hero_rule.replace(' ', '') not in style_content.replace(' ', ''):
            add_fail(3, filename, '3C', f'Desktop hero rule missing or incorrect: {hero_rule}', styles[0].sourceline)
            
        mobile_rule = f'@media (max-width: 768px) {{ .hero-{slug} {{ background-image: url(\'/images/brands/hero-brands/{slug}-mobile.webp\'); }} }}'
        if mobile_rule.replace(' ', '') not in style_content.replace(' ', '').replace('\n', ''):
            add_fail(3, filename, '3D', f'Mobile hero rule missing or incorrect', styles[0].sourceline)
            
        if 'linear-gradient' in style_content:
            add_fail(3, filename, '3E', 'linear-gradient found in style block', styles[0].sourceline)
            
        num_rules = style_content.count('{')
        if num_rules > 4:
            add_fail(3, filename, '3G', f'Style block contains {num_rules} blocks, expected 4', styles[0].sourceline)

    hero = soup.find('header', class_=lambda c: c and 'hero' in c) or soup.find('section', class_=lambda c: c and 'hero' in c)
    if hero and hero.has_attr('style'):
        add_fail(3, filename, '3F', 'Inline style= found on hero element', hero.sourceline)

    # GROUP 4: Hero
    if hero:
        if hero.name != 'header':
            add_fail(4, filename, '4A', f'Hero element is <{hero.name}> not <header>', hero.sourceline)
        classes = hero.get('class', [])
        if 'hero' not in classes: add_fail(4, filename, '4B', 'Hero missing class "hero"', hero.sourceline)
        if 'hero-compact' not in classes: add_fail(4, filename, '4C', 'Hero missing class "hero-compact" (or uses full/standard)', hero.sourceline)
        if 'hero-high-impact' not in classes: add_fail(4, filename, '4D', 'Hero missing class "hero-high-impact"', hero.sourceline)
        if f'hero-{slug}' not in classes: add_fail(4, filename, '4E', f'Hero missing class "hero-{slug}"', hero.sourceline)
        
        h1s = soup.find_all('h1')
        if len(h1s) != 1:
            add_fail(4, filename, '4F', f'Exactly one <h1> required, found {len(h1s)}')
            if h1s and 'hero-title-main' not in h1s[0].get('class', []):
                add_fail(4, filename, '4G', '<h1> missing class "hero-title-main"', h1s[0].sourceline)
        else:
            if 'hero-title-main' not in h1s[0].get('class', []):
                add_fail(4, filename, '4G', '<h1> missing class "hero-title-main"', h1s[0].sourceline)
            
        eyebrow = hero.find(class_=lambda c: c and 'eyebrow' in c)
        if eyebrow:
            if 'eyebrow-light' not in eyebrow.get('class', []):
                add_fail(4, filename, '4H', 'Eyebrow uses different class than eyebrow-light', eyebrow.sourceline)
            if eyebrow.has_attr('style') and 'line-height' not in eyebrow['style']:
                add_fail(4, filename, '4H', 'Eyebrow has inline style', eyebrow.sourceline)
            
        subtitle = hero.find('p', class_=lambda c: c and 'hero-subtitle-main' in c)
        if not subtitle:
            p = hero.find('div', class_='brand-hero-left').find('p') if hero.find('div', class_='brand-hero-left') else None
            if p and 'hero-subtitle-main' not in p.get('class', []):
                add_fail(4, filename, '4I', 'Hero subtitle missing class "hero-subtitle-main"', p.sourceline)
    else:
        add_fail(4, filename, '4A', 'Hero element missing entirely')

    # GROUP 5: Trust bar
    tb = soup.find(class_='trust-bar') or soup.find(class_='sv-trust-bar')
    if not tb:
        add_fail(5, filename, '5A', 'Trust bar missing entirely')
    else:
        if 'sv-trust-bar' in tb.get('class', []):
            add_fail(5, filename, '5A', 'Trust bar uses class "sv-trust-bar" instead of "trust-bar"', tb.sourceline)
            
        container = tb.find(class_='container')
        if not container:
            add_fail(5, filename, '5B', 'Trust bar missing <div class="container"> wrapper', tb.sourceline)
            
        inner = tb.find(class_='trust-bar-inner') or tb.find(class_='trust-flex-inline') or tb.find(class_='trust-inner')
        if inner:
            if 'trust-bar-inner' not in inner.get('class', []):
                add_fail(5, filename, '5C', f'Trust bar inner uses wrong class: {inner.get("class")}', inner.sourceline)
        else:
            add_fail(5, filename, '5C', 'Trust bar inner missing')
            
        dividers = tb.find_all(class_=lambda c: c and ('divider' in c or 'sep' in c))
        for d in dividers:
            if 'trust-divider' not in d.get('class', []):
                add_fail(5, filename, '5D', f'Divider uses wrong class: {d.get("class")}', d.sourceline)
                
        tb_text = tb.get_text(separator=' ', strip=True).lower()
        if 'bca' in tb_text:
            add_fail(5, filename, '5E', 'BCA Registered appears in trust bar', tb.sourceline)
            
        items = [i for i in tb.stripped_strings if i != '|']
        if len(items) < 3: # rough check since some strings are split
             pass # Not strictly checking exactly 3 items length due to parsing
        
        bizsafe = tb.find(class_='sv-bizsafe')
        if not bizsafe:
            if 'bizsafe level 3' in tb_text:
                add_fail(5, filename, '5F', 'bizSAFE Level 3 appears as plain text', tb.sourceline)
            else:
                add_fail(5, filename, '5F', 'sv-bizsafe dynamic span missing', tb.sourceline)
                
        sites = tb.find(class_='sv-sites')
        if sites:
            if sites.parent.name != 'strong':
                add_fail(5, filename, '5G', 'sv-sites is not wrapped in <strong> tags', sites.sourceline)
        else:
            add_fail(5, filename, '5G', 'sv-sites missing or hardcoded number used', tb.sourceline)
            
    # GROUP 6: Breadcrumb
    bc = soup.find('nav', class_='sv-breadcrumb')
    if not bc:
        add_fail(6, filename, '6A', 'Breadcrumb <nav class="sv-breadcrumb"> missing')
    else:
        if bc.get('aria-label') != 'Breadcrumb':
            add_fail(6, filename, '6A', 'Breadcrumb aria-label="Breadcrumb" missing', bc.sourceline)
            
        lis = bc.find_all('li')
        if len(lis) >= 3:
            if not lis[0].find('a', href='/'):
                add_fail(6, filename, '6C', 'First breadcrumb item not <a href="/">Home</a>', lis[0].sourceline)
            if not lis[1].find('a', href='/brands/'):
                add_fail(6, filename, '6D', 'Second breadcrumb item not <a href="/brands/">Brands</a>', lis[1].sourceline)
            if lis[-1].find('a'):
                add_fail(6, filename, '6E', 'Last breadcrumb item wrapped in <a> tag', lis[-1].sourceline)
        else:
            add_fail(6, filename, '6C', 'Breadcrumb missing items', bc.sourceline)
            
    # GROUP 7: Page structure
    body_children = [c for c in soup.body.children if c.name and c.name not in ['script', 'style']] if soup.body else []
    expected_order = ['nav', 'header', 'div', 'nav', 'main', 'section', 'footer']
    actual_order_filtered = []
    for c in body_children:
        if c.name == 'div' and 'trust-bar' not in c.get('class', []) and 'sv-trust-bar' not in c.get('class', []):
            continue
        if c.name == 'a': continue # Ignore wa-float here, already checked
        actual_order_filtered.append(c.name)
        
    if actual_order_filtered[:7] != expected_order:
        add_fail(7, filename, '7A', f'Page structure order incorrect. Found: {actual_order_filtered[:7]}')
        
    main = soup.find('main')
    if main:
        sections = main.find_all('section', recursive=False)
        if sections:
            if 'sv-section-grey' not in sections[0].get('class', []):
                add_fail(7, filename, '7B', 'First content section after breadcrumb does not use sv-section-grey', sections[0].sourceline)
                
            prev_bg = None
            for s in sections:
                c = s.get('class', [])
                bg = 'grey' if 'sv-section-grey' in c else 'white' if 'sv-section-white' in c else None
                if bg:
                    if prev_bg == bg:
                        add_fail(7, filename, '7C', f'Consecutive sections with same background: {bg}', s.sourceline)
                    prev_bg = bg
                    
                if s.has_attr('style') and 'padding' in s['style'].lower():
                    add_fail(7, filename, '7D', 'Section has inline style="padding..."', s.sourceline)
    
    cta = soup.body.find_all('section')[-1] if soup.body and soup.body.find_all('section') else None
    if cta:
        classes = cta.get('class', [])
        if 'cta-section' not in classes or 'cta-high-impact' not in classes:
            add_fail(7, filename, '7E', 'Final CTA missing cta-section or cta-high-impact', cta.sourceline)
        if not cta.find('h2'):
            add_fail(7, filename, '7F', 'Final CTA missing <h2>', cta.sourceline)
        btn = cta.find('a', class_=lambda c: c and 'btn' in c)
        if btn:
            bt = btn.text.strip()
            if filename != 'vesta.html' and bt != 'Request a Proposal':
                add_fail(7, filename, '7G', f'Final CTA button label is "{bt}"', btn.sourceline)
            if filename == 'vesta.html' and bt != 'Request a Demo':
                add_fail(7, filename, '7G', f'Final CTA button label is "{bt}"', btn.sourceline)

    # GROUP 8: Inline styles
    inlines = soup.body.find_all(style=True) if soup.body else []
    for el in inlines:
        s = el['style']
        cls = el.get('class', [])
        if 'stat-bar-fill' in cls and re.match(r'^width\s*:\s*\d+%$', s.strip()): continue
        add_fail(8, filename, '8A', f'Inline style found on <{el.name}>: {s}', el.sourceline)
        
    # GROUP 9: Dynamic values
    def extract_visible_text(s_obj):
        texts = []
        for text in s_obj.find_all(string=True):
            if text.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']: continue
            if isinstance(text, Comment): continue
            ss = text.strip()
            if ss: texts.append((text.parent.sourceline, ss, text.parent))
        return texts

    for line, text, parent in extract_visible_text(soup):
        if re.search(r'L/PS/\d+', text):
            add_fail(9, filename, '9A', f'Hardcoded licence number found: {text}', line)
        if 'bizsafe level 3' in text.lower():
            add_fail(9, filename, '9B', 'Hardcoded bizSAFE Level 3 found', line)
        if re.search(r'\b2,?000\+\b', text):
            if 'sv-sites' not in parent.get('class', []):
                add_fail(9, filename, '9C', 'Hardcoded site count (2,000+) found', line)
            
    # GROUP 10: Content and Links
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('../') or href.startswith('./') or (not href.startswith('/') and not href.startswith('http') and not href.startswith('mailto:') and not href.startswith('tel:') and not href.startswith('#')):
            add_fail(10, filename, '10A', f'Relative href found: {href}', a.sourceline)
        if href.startswith('/'):
            valid_patterns = ['/solutions/', '/systems/', '/brands/', '/portfolio/', '/insights/', '/resources/', '/contact-gateway.html', '/contact.html', '/about.html', '/request-site-assessment-singapore.html', '/images/', '/images/', '/index.html']
            valid = False
            for p in valid_patterns:
                if href.startswith(p): valid = True
            if href == '/': valid = True
            if not valid:
                add_fail(10, filename, '10F', f'Internal link path unrecognized: {href}', a.sourceline)
                
    for img in soup.find_all('img', src=True):
        src = img['src']
        if src.startswith('../') or src.startswith('./'):
            add_fail(10, filename, '10B', f'Relative src found: {src}', img.sourceline)
        alt = img.get('alt', '').strip().lower()
        if not alt or alt in ['image', 'photo', 'banner']:
            add_fail(10, filename, '10C', f'Empty or generic alt text: "{alt}"', img.sourceline)
            
    hs = soup.find_all(['h1', 'h2', 'h3', 'h4'])
    levels = []
    has_h2 = False
    for h in hs:
        lvl = int(h.name[1])
        if lvl == 2:
            in_cta = False
            p = h.parent
            while p:
                if p.name == 'section' and 'cta-section' in p.get('class', []):
                    in_cta = True
                    break
                p = p.parent
            if not in_cta: has_h2 = True
        if levels:
            if lvl == 3 and 2 not in levels:
                add_fail(10, filename, '10D', 'H3 appears before any H2', h.sourceline)
            if lvl == 4 and 3 not in levels:
                add_fail(10, filename, '10D', 'H4 appears before any H3', h.sourceline)
        levels.append(lvl)
    if not has_h2:
        add_fail(10, filename, '10D', 'No H2 found outside CTA section')
        
    ids = []
    for el in soup.find_all(id=True):
        ids.append(el['id'])
    dups = [item for item, count in collections.Counter(ids).items() if count > 1]
    for d in dups:
        add_fail(10, filename, '10E', f'Duplicate id found: {d}')
        
    for line, text, parent in extract_visible_text(soup):
        text_lower = text.lower()
        for placeholder in ["todo", "placeholder", "lorem ipsum", "update this", "coming soon", "[brand name]", "[insert]"]:
            if placeholder in text_lower:
                add_fail(10, filename, '10G', f'Placeholder text found: {placeholder}', line)
                
        words = re.findall(r'\b[a-z]+\b', text_lower)
        if 'color' in words and 'colorvu' not in text_lower: add_fail(10, filename, '10H', 'American spelling "color"', line)
        if 'center' in words: add_fail(10, filename, '10H', 'American spelling "center"', line)
        if 'optimize' in words: add_fail(10, filename, '10H', 'American spelling "optimize"', line)
        if 'authorization' in words: add_fail(10, filename, '10H', 'American spelling "authorization"', line)
        if 'recognize' in words and 'license plate recognition' not in text_lower and 'lpr' not in text_lower: add_fail(10, filename, '10H', 'American spelling "recognize"', line)
        if 'program' in words: add_fail(10, filename, '10H', 'Noun "program" instead of "programme" (flagged for review)', line)
        if 'license' in words and 'license plate' not in text_lower: add_fail(10, filename, '10H', 'Noun "license" instead of "licence"', line)

# Generate Report
out = []
out.append("BRANDS SECTION — FULL AUDIT REPORT")
out.append(f"Date: {datetime.now().strftime('%B %Y')}")
out.append("Files audited: 38\n")
out.append("═══════════════════════════════════════════════")
out.append("SUMMARY TABLE")
out.append("═══════════════════════════════════════════════\n")
out.append("| Group | Check | Pass | Fail | Fail pages |")
out.append("|-------|-------|------|------|------------|")

group_names = {
    1: "Infrastructure",
    2: "Head/SEO/Meta",
    3: "Style block",
    4: "Hero",
    5: "Trust bar",
    6: "Breadcrumb",
    7: "Page structure",
    8: "Inline styles",
    9: "Dynamic values",
    10: "Content/Links"
}

all_failures = []
clean_pages = set(files_in_scope)
failure_counts = collections.defaultdict(set)

for i in range(1, 11):
    fail_pages = []
    for f in files_in_scope:
        if results[i][f]:
            if f not in fail_pages: fail_pages.append(f)
            if f in clean_pages: clean_pages.remove(f)
            for fail in results[i][f]:
                all_failures.append((f, fail))
                parts = fail.split('  ', 1)
                if len(parts) == 2:
                    desc = parts[1].split(' — line')[0]
                    failure_counts[f"{parts[0]}  {desc}"].add(f)
                
    pass_count = 38 - len(fail_pages)
    fail_count = len(fail_pages)
    if fail_count > 0:
        if fail_count > 5:
            list_str = f"{fail_count} pages"
        else:
            list_str = ", ".join([f.replace('.html', '') for f in fail_pages])
    else:
        list_str = "None"
    out.append(f"| {i:<2} | {group_names[i]:<14} | {pass_count}/38 | {fail_count}/38 | {list_str} |")

out.append("\n═══════════════════════════════════════════════")
out.append("DETAILED FINDINGS")
out.append("═══════════════════════════════════════════════\n")

if not all_failures:
    out.append("No failures found.\n")

current_file = ""
for f, fail in sorted(all_failures):
    if f != current_file:
        out.append(f"\nFILE: brands/{f}")
        current_file = f
    out.append(f"  {fail}")

out.append("\n═══════════════════════════════════════════════")
out.append("CLEAN PAGES")
out.append("═══════════════════════════════════════════════\n")
if clean_pages:
    for cp in sorted(list(clean_pages)):
        out.append(cp)
else:
    out.append("None")

out.append("\n═══════════════════════════════════════════════")
out.append("PRIORITY FINDINGS")
out.append("═══════════════════════════════════════════════\n")
out.append("| Rank | Check | Failure description | Pages affected |")
out.append("|------|-------|---------------------|----------------|")

ranked = sorted([(len(pages), desc) for desc, pages in failure_counts.items()], reverse=True)
for i, (count, desc) in enumerate(ranked[:5]):
    parts = desc.split('  ', 1)
    chk = parts[0]
    txt = parts[1] if len(parts) > 1 else desc
    out.append(f"| {i+1} | {chk} | {txt} | {count} |")

with open(os.path.join(base_dir, '_ai/audit-brands-full.md'), 'w', encoding='utf-8') as f:
    f.write("\n".join(out))

print("Audit complete.")
