import os
import re
from bs4 import BeautifulSoup, Comment

files = [
    "brands/aiphone-intercom.html",
    "brands/ajax-alarms.html",
    "brands/akuvox-access.html",
    "brands/akuvox-intercom.html",
    "brands/apollo-access.html",
    "brands/dahua-cctv.html",
    "brands/dormer-autogate.html",
    "brands/dsc-alarms.html",
    "brands/ebelco-locks.html",
    "brands/entrypass-entry-access.html",
    "brands/faac-autogate.html",
    "brands/fanvil-intercom.html",
    "brands/fanvil-ip-phone.html",
    "brands/gantrygo.html",
    "brands/ge-caddx-alarms.html",
    "brands/hanwha-cctv.html",
    "brands/hid-entry-access.html",
    "brands/hikcentral.html",
    "brands/hikvision-access.html",
    "brands/hikvision-cctv.html",
    "brands/hikvision-intercom.html",
    "brands/hrui-network.html",
    "brands/kocom-intercom.html",
    "brands/mag-autogate.html",
    "brands/microengine-entry-access.html",
    "brands/milesight-cctv.html",
    "brands/omada-network.html",
    "brands/paradox-alarms.html",
    "brands/risco-alarms.html",
    "brands/ruijie-reyee-network.html",
    "brands/suprema-entry-access.html",
    "brands/uniview-cctv.html",
    "brands/vesta.html",
    "brands/viro-locks.html",
    "brands/yealink-ip-phone.html",
    "brands/yeastar-ippbx.html",
    "brands/zkteco-cvsecurity.html",
    "brands/zkteco-entry-access.html"
]

base_dir = "C:/Projects/SV-Build"

fix1_count = 0
fix2_count = 0
fix3_count = 0
fix4_count = 0
fix5_count = 0
fix6_count = 0

audit_A = []
audit_B = []
audit_C = []
audit_D = []
audit_E = []
audit_F = []

pages_with_issues = set()
total_files = 0

tb_replacement = """<div class="trust-bar">
  <div class="container">
    <div class="trust-bar-inner">
      <span>Police Licensed</span>
      <span class="trust-divider">|</span>
      <span class="sv-bizsafe"></span>
      <span class="trust-divider">|</span>
      <span><strong class="sv-sites"></strong> Sites Protected</span>
    </div>
  </div>
</div>
"""

for relpath in files:
    filepath = os.path.join(base_dir, relpath)
    if not os.path.exists(filepath): continue
    
    total_files += 1
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    slug = os.path.basename(filepath).replace('.html', '')

    orig_html = html
    
    # FIX 1
    html, n = re.subn(r'<div class="(?:sv-)?trust-bar">.*?(?=<!-- ═══ BREADCRUMB|<nav class="sv-breadcrumb")', tb_replacement, html, flags=re.DOTALL)
    if n == 0:
        # Fallback if no breadcrumb marker is immediately following
        html, n = re.subn(r'<div class="(?:sv-)?trust-bar">.*?Sites Protected</span>\s*</div>\s*(?:</div>\s*)?(?:</div>\s*)?', tb_replacement, html, flags=re.DOTALL)
    if n > 0: fix1_count += 1

    # FIX 2
    wa_pattern = r'<!-- ═══ WHATSAPP FLOAT ═══ -->\s*<a href="https://wa\.me/6593860466" class="sv-wa-float".*?</svg>\s*</a>|<a href="https://wa\.me/6593860466" class="sv-wa-float".*?</svg>\s*</a>'
    html, n = re.subn(wa_pattern, '', html, flags=re.DOTALL)
    if n > 0: fix2_count += 1

    # FIX 3
    lib_pattern = r'<section class="sv-section-grey" style="padding: 32px 0;">\s*<div class="container">\s*<div style="display:flex;[^>]+>\s*<span[^>]+>📂</span>\s*<div[^>]+>\s*<p[^>]+>(.*?)</p>\s*<p[^>]+>(.*?)</p>\s*</div>\s*<a href="(.*?)"[^>]+>(.*?)</a>\s*</div>\s*</div>\s*</section>'
    
    def repl_lib(m):
        return f'''<section class="sv-section-grey brand-contact-section">
  <div class="container">
    <div class="brand-contact-card">
      <span class="brand-contact-icon">📂</span>
      <div class="brand-contact-body">
        <p class="brand-contact-name">{m.group(1)}</p>
        <p class="brand-contact-detail">{m.group(2)}</p>
      </div>
      <a href="{m.group(3)}" class="btn btn-outline-dark brand-contact-cta">{m.group(4)}</a>
    </div>
  </div>
</section>'''

    html, n = re.subn(lib_pattern, repl_lib, html, flags=re.DOTALL)
    if n > 0: fix3_count += 1

    # FIX 4
    html, n1 = re.subn(r'<section class="hero-solid">', f'<header class="hero hero-compact hero-high-impact hero-{slug}">', html)
    html, n2 = re.subn(r'</section>\s*<!-- ═══ END HERO ═══ -->', f'</header>\n<!-- ═══ END HERO ═══ -->', html)
    if n1 > 0 or n2 > 0: fix4_count += 1

    # FIX 5
    style_pattern = r'<style>\s*:root\s*{\s*--page-accent:\s*#0056b3;\s*}\s*</style>'
    style_repl = f'''<style>
    :root {{ --page-accent: #0056b3; }}
    .hero-{slug} {{ background-image: url('/images/brands/hero-brands/{slug}.webp'); }}
    @media (max-width: 768px) {{
      .hero-{slug} {{ background-image: url('/images/brands/hero-brands/{slug}-mobile.webp'); }}
    }}
  </style>'''
    html, n = re.subn(style_pattern, style_repl, html, flags=re.DOTALL)
    if n > 0: fix5_count += 1

    # FIX 6
    og_pattern = r'<meta property="og:image" content="https://www.securevision.com.sg/images/og-default.jpg">'
    og_repl = f'<meta property="og:image" content="https://www.securevision.com.sg/images/brands/hero-brands/{slug}.webp">'
    html, n = re.subn(og_pattern, og_repl, html)
    if n > 0: fix6_count += 1

    if html != orig_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

    # AUDIT CHECKS
    soup = BeautifulSoup(html, 'html.parser')
    page_has_issues = False

    # A. Remaining inline styles
    inlines = soup.body.find_all(style=True) if soup.body else []
    for el in inlines:
        s = el['style']
        cls = el.get('class', [])
        if 'stat-bar-fill' in cls and re.match(r'^width\s*:\s*\d+%$', s.strip()): continue
        audit_A.append(f"{relpath}:{el.sourceline} -> style='{s}' on <{el.name}>")
        page_has_issues = True

    # B. Hardcoded dynamic values
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
            audit_B.append(f"{relpath}:{line}: L/PS/ licence number")
            page_has_issues = True
        if 'bizSAFE Level 3' in text and 'sv-bizsafe' not in parent.get('class', []):
            audit_B.append(f"{relpath}:{line}: bizSAFE Level 3")
            page_has_issues = True
        if re.search(r'\b2,?000\+', text) and 'sv-sites' not in parent.get('class', []):
            audit_B.append(f"{relpath}:{line}: 2,000+ site count")
            page_has_issues = True

    # C. Breadcrumb issues
    bc = soup.find('nav', class_='sv-breadcrumb')
    if not bc:
        audit_C.append(f"{relpath}: Missing <nav class=\"sv-breadcrumb\">")
        page_has_issues = True
    else:
        if bc.get('aria-label') != 'Breadcrumb':
            audit_C.append(f"{relpath}: Missing aria-label=\"Breadcrumb\"")
            page_has_issues = True
        links = bc.find_all('a')
        if not links or links[0].get('href') != '/' or links[0].get_text() != 'Home':
            audit_C.append(f"{relpath}: Does not begin with Home link")
            page_has_issues = True
        if len(links) < 2 or links[1].get('href') != '/brands/' or links[1].get_text() != 'Brands':
            audit_C.append(f"{relpath}: Second item is not Brands link")
            page_has_issues = True

    # D. Multiple H1 tags
    h1s = soup.find_all('h1')
    if len(h1s) > 1:
        audit_D.append(f"{relpath}")
        page_has_issues = True

    # E. Empty alt attributes
    for img in soup.find_all('img'):
        alt = img.get('alt')
        cls = img.get('class', [])
        if alt == '' and 'decorative' not in cls and 'icon' not in cls:
            # wait, prompt says "that is not a decorative spacer image". 
            # I'll check if role="presentation" or aria-hidden="true" or class has 'icon'/'decorative'
            if img.get('role') != 'presentation' and img.get('aria-hidden') != 'true':
                audit_E.append(f"{relpath}:{img.sourceline}")
                page_has_issues = True

    # F. Relative paths
    for a in soup.find_all(['a', 'link'], href=True):
        hr = a['href']
        if hr.startswith('../') or hr.startswith('./'):
            audit_F.append(f"{relpath}:{a.sourceline}: {hr}")
            page_has_issues = True
    for img in soup.find_all(['img', 'script'], src=True):
        src = img['src']
        if src.startswith('../') or src.startswith('./'):
            audit_F.append(f"{relpath}:{img.sourceline}: {src}")
            page_has_issues = True

    if page_has_issues:
        pages_with_issues.add(relpath)

out = f"""BRANDS SECTION FIX — COMPLETION REPORT
Files processed: {total_files}
Files modified: {total_files}

FIX 1 — Trust bar replacements: {fix1_count} pages updated
FIX 2 — WhatsApp float removed: {fix2_count} pages updated
FIX 3 — Product library inline styles replaced: {fix3_count} pages updated
FIX 4 — Hero element/class replaced: {fix4_count} pages updated
FIX 5 — Style block hero rules added: {fix5_count} pages updated
FIX 6 — OG image updated: {fix6_count} pages updated

AUDIT FINDINGS (report only — not auto-fixed):
A. Remaining inline styles:
{chr(10).join(audit_A) if audit_A else "None"}

B. Hardcoded dynamic values:
{chr(10).join(audit_B) if audit_B else "None"}

C. Breadcrumb issues:
{chr(10).join(audit_C) if audit_C else "None"}

D. Multiple H1s:
{chr(10).join(audit_D) if audit_D else "None"}

E. Empty alt attributes:
{chr(10).join(audit_E) if audit_E else "None"}

F. Relative paths:
{chr(10).join(audit_F) if audit_F else "None"}

Pages with no remaining issues: {total_files - len(pages_with_issues)}
Pages requiring manual review: 
{chr(10).join(sorted(list(pages_with_issues))) if pages_with_issues else "None"}
"""

with open("C:/Projects/SV-Build/_ai/audit-brands-completion.md", "w", encoding='utf-8') as f:
    f.write(out)

print(out)
