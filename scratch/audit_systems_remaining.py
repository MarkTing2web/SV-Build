import os
import re
import json
from bs4 import BeautifulSoup, Comment

files = [
    "C:/Projects/SV-Build/systems/index.html",
    "C:/Projects/SV-Build/systems/premises-security.html",
    "C:/Projects/SV-Build/systems/entry-access-control.html",
    "C:/Projects/SV-Build/systems/vehicle-lpr-management.html",
    "C:/Projects/SV-Build/systems/ip-phone-communications.html",
    "C:/Projects/SV-Build/systems/security-management-platform.html",
    "C:/Projects/SV-Build/systems/network-infrastructure.html"
]

base_dir = "C:/Projects/SV-Build"

def is_benefit_led(desc):
    # simple heuristic
    lower = desc.lower()
    product_led = ["we provide", "we are", "this is a", "our product", "securevision is", "securevision provides", "a system", "systems for"]
    for p in product_led:
        if lower.startswith(p): return "no"
    return "yes"

def suggest_title(title):
    # just an approximation
    if "Singapore" not in title:
        return title[:45] + " in Singapore"
    return title

def check_link_exists(href):
    if not href.startswith('/'): return True
    path = href.split('#')[0].split('?')[0]
    if path == '/':
        path = '/index.html'
    elif not path.endswith('.html') and not path.endswith('/'):
        # could be a folder
        pass
    
    # map absolute to local
    local_path = os.path.join(base_dir, path.lstrip('/'))
    if os.path.isdir(local_path):
        local_path = os.path.join(local_path, "index.html")
    
    return os.path.exists(local_path)

def extract_visible_text(soup):
    texts = []
    for text in soup.find_all(string=True):
        if text.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            continue
        if isinstance(text, Comment):
            continue
        texts.append((text.parent.sourceline, text.strip()))
    return [t for t in texts if t[1]]

results = {}

for filepath in files:
    filename = os.path.basename(filepath)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    res = {}
    
    # 1. SEO METADATA
    title_tag = soup.find('title')
    title = title_tag.string.strip() if title_tag and title_tag.string else ""
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    desc = desc_tag['content'].strip() if desc_tag and 'content' in desc_tag.attrs else ""
    canonical_tag = soup.find('link', rel='canonical')
    canonical = canonical_tag['href'].strip() if canonical_tag and 'href' in canonical_tag.attrs else ""
    
    og_title = soup.find('meta', property='og:title')
    og_title = og_title['content'] if og_title else "MISSING"
    og_desc = soup.find('meta', property='og:description')
    og_desc = og_desc['content'] if og_desc else "MISSING"
    og_image = soup.find('meta', property='og:image')
    og_image = og_image['content'] if og_image else "MISSING"
    og_url = soup.find('meta', property='og:url')
    og_url = og_url['content'] if og_url else "MISSING"
    
    res['seo'] = {
        'title': title,
        'desc': desc,
        'canonical': canonical,
        'og_title': og_title,
        'og_desc': og_desc,
        'og_image': og_image,
        'og_url': og_url
    }
    
    # 2. STYLE BLOCK
    style_tags = soup.find_all('style')
    style_content = ""
    for s in style_tags:
        if s.string: style_content += s.string + "\n"
        
    accent = "MISSING"
    m = re.search(r'--page-accent:\s*([^;]+);', style_content)
    if m: accent = m.group(1).strip()
    
    desk_hero = "MISSING"
    m2 = re.search(r'\.hero-[^{]*{[^}]*background-image:\s*(url\([^)]+\))', style_content)
    if m2: desk_hero = m2.group(1)
    # fallbacks
    if desk_hero == "MISSING":
        m2 = re.search(r'background-image:\s*(url\([^)]+\))', style_content)
        if m2: desk_hero = m2.group(1)
        
    mob_hero = "MISSING"
    m3 = re.search(r'@media[^{]+768px[^{]+{[^}]+background-image:\s*(url\([^)]+\))', style_content, re.DOTALL)
    if m3: mob_hero = m3.group(1)
    
    # other css?
    # Strip known patterns
    clean_style = re.sub(r':root\s*{[^}]+}', '', style_content)
    clean_style = re.sub(r'(\.hero-[^{]*|header)[^{]*{[^}]*background-image:[^}]+}', '', clean_style)
    clean_style = re.sub(r'@media[^{]+768px[^{]+{[^}]+background-image:[^}]+}', '', clean_style)
    clean_style = clean_style.strip()
    other_css = "YES" if len(clean_style) > 20 else "NO"
    
    res['style'] = {
        'accent': accent,
        'desk_hero': desk_hero,
        'mob_hero': mob_hero,
        'other_css': other_css
    }
    
    # 3. INTERNAL LINKS
    links = []
    old_patterns = ['-security-singapore.html', 'surveillance-detection.html', 'people-access-control.html', 'vehicle-access-control.html', 'integrated-security-platform.html', 'door-access.html', 'intercom-system-singapore.html', 'auto-gate-singapore.html']
    
    for a in soup.find_all('a', href=True):
        href = a['href']
        ltype = "relative"
        if href.startswith('http'): ltype = "external"
        elif href.startswith('/'): ltype = "internal"
        elif href.startswith('#'): ltype = "anchor"
        elif href.startswith('mailto:') or href.startswith('tel:'): ltype = "protocol"
        
        issues = []
        if ltype == "relative":
            issues.append("Relative path")
            
        for p in old_patterns:
            if p in href:
                issues.append(f"Old URL pattern ({p})")
        
        if "burglar-alarm.html" in href and "/systems/" not in href:
            issues.append("Old URL pattern (burglar-alarm.html without /systems/)")
            
        if ltype in ["internal", "relative"]:
            if not check_link_exists(href):
                issues.append("File does not exist")
                
        if issues:
            links.append({'line': a.sourceline, 'href': href, 'issue': " | ".join(issues)})
    
    res['links'] = links
    
    # 4. IMAGE ALT TEXT
    alts = []
    generics = ['image', 'photo', 'banner', 'hero', 'logo']
    for img in soup.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt')
        classes = img.get('class', [])
        
        issue = None
        if alt is None:
            issue = "Missing alt attribute"
        elif alt.strip() == "":
            is_decorative = False
            for c in classes:
                if 'icon' in c or 'decorative' in c: is_decorative = True
            if 'icon' in src.lower(): is_decorative = True
            if not is_decorative:
                issue = "Empty alt on content image"
        else:
            al = alt.strip().lower()
            if al in generics:
                issue = "Generic placeholder alt"
            elif src.lower().endswith(al) or al.endswith('.jpg') or al.endswith('.png'):
                issue = "Alt is just filename"
                
        if issue:
            trunc_src = src if len(src) < 40 else src[:20] + "..." + src[-15:]
            alts.append({'line': img.sourceline, 'src': trunc_src, 'issue': issue})
            
    res['alts'] = alts
    
    # 5. FEATURE CARD NEUTRAL
    feature_cards = {'pos': None, 'neg': None}
    if filename != "index.html":
        # find headings with This Is For You and You May Not Need
        pos_h3 = soup.find(string=re.compile("This Is For You"))
        neg_h3 = soup.find(string=re.compile("You May Not Need"))
        
        if pos_h3:
            card = pos_h3.find_parent(class_=re.compile('feature-card'))
            if card: feature_cards['pos'] = " ".join(card.get('class', []))
        if neg_h3:
            card = neg_h3.find_parent(class_=re.compile('feature-card'))
            if card: feature_cards['neg'] = " ".join(card.get('class', []))
            
    res['feature_cards'] = feature_cards
    
    # 6. DYNAMIC VALUES
    dyn_issues = []
    vis_texts = extract_visible_text(soup)
    for line, text in vis_texts:
        if re.search(r'\b202[456]\b', text):
            dyn_issues.append({'line': line, 'text': text, 'should': 'current year class'})
        if re.search(r'\b2,?000\b', text):
            dyn_issues.append({'line': line, 'text': text, 'should': 'sv-sites'})
        if 'L/PS/' in text:
            dyn_issues.append({'line': line, 'text': text, 'should': 'licence number variable'})
        if 'bizSAFE Level 3' in text:
            dyn_issues.append({'line': line, 'text': text, 'should': 'sv-bizsafe'})
        if re.search(r'\b(?:19|20)\s+years\b', text.lower()):
            dyn_issues.append({'line': line, 'text': text, 'should': 'sv-years'})
            
    res['dyn'] = dyn_issues
    
    # 7. BRITISH ENGLISH
    brit_issues = []
    american_words = {
        r'\bauthorization\b': 'authorisation',
        r'\boptimize\b': 'optimise',
        r'\bcolor\b': 'colour',
        r'\bcenter\b': 'centre',
        r'\blicense\b': 'licence', # simple check, but maybe wrong if used as verb
        r'\brecognize\b': 'recognise',
        r'\banalyze\b': 'analyse',
        r'\bfiber\b': 'fibre',
        r'\blabeled\b': 'labelled'
    }
    
    for line, text in vis_texts:
        for p, corr in american_words.items():
            if p == r'\blicense\b' and 'licensed' in text.lower():
                continue # simple exclusion for Police Licensed
            if re.search(p, text, re.IGNORECASE):
                # double check license verb
                if 'police license' in text.lower() or 'license' in text.lower():
                    # it's tricky. Let's just flag it.
                    pass
                brit_issues.append({'line': line, 'text': text, 'corr': corr})
                
    res['brit'] = brit_issues
    results[filename] = res

with open('C:/Projects/SV-Build/scratch/audit_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Extraction complete.")
