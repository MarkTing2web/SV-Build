import os
import re
from bs4 import BeautifulSoup, Comment

fix7_files = [
    "brands/akuvox-intercom.html",
    "brands/dahua-cctv.html",
    "brands/dormer-autogate.html",
    "brands/kocom-intercom.html",
    "brands/mag-autogate.html",
    "brands/suprema-entry-access.html",
    "brands/viro-locks.html",
    "brands/yealink-ip-phone.html",
    "brands/zkteco-cvsecurity.html",
    "brands/zkteco-entry-access.html"
]

fix8_files = [
    "brands/aiphone-intercom.html",
    "brands/ebelco-locks.html",
    "brands/fanvil-intercom.html",
    "brands/hikvision-intercom.html",
    "brands/mag-autogate.html",
    "brands/zkteco-cvsecurity.html"
]

fix9_files = [
    "brands/akuvox-access.html",
    "brands/akuvox-intercom.html",
    "brands/apollo-access.html",
    "brands/ebelco-locks.html",
    "brands/faac-autogate.html",
    "brands/hid-entry-access.html",
    "brands/hikvision-access.html",
    "brands/hikvision-intercom.html",
    "brands/hrui-network.html",
    "brands/kocom-intercom.html",
    "brands/omada-network.html",
    "brands/ruijie-reyee-network.html",
    "brands/suprema-entry-access.html",
    "brands/vesta.html",
    "brands/viro-locks.html",
    "brands/yealink-ip-phone.html",
    "brands/yeastar-ippbx.html",
    "brands/zkteco-entry-access.html"
]

fix10_files = [
    "brands/aiphone-intercom.html",
    "brands/akuvox-access.html",
    "brands/akuvox-intercom.html",
    "brands/apollo-access.html",
    "brands/dahua-cctv.html",
    "brands/dormer-autogate.html",
    "brands/ebelco-locks.html",
    "brands/entrypass-entry-access.html",
    "brands/faac-autogate.html",
    "brands/fanvil-intercom.html",
    "brands/fanvil-ip-phone.html",
    "brands/gantrygo.html",
    "brands/hid-entry-access.html",
    "brands/hikcentral.html",
    "brands/hikvision-access.html",
    "brands/hikvision-intercom.html",
    "brands/hrui-network.html",
    "brands/kocom-intercom.html",
    "brands/mag-autogate.html",
    "brands/microengine-entry-access.html",
    "brands/omada-network.html",
    "brands/ruijie-reyee-network.html",
    "brands/suprema-entry-access.html",
    "brands/vesta.html",
    "brands/viro-locks.html",
    "brands/yealink-ip-phone.html",
    "brands/yeastar-ippbx.html",
    "brands/zkteco-cvsecurity.html",
    "brands/zkteco-entry-access.html"
]

all_files = set(fix7_files + fix8_files + fix9_files + fix10_files)
base_dir = "C:/Projects/SV-Build"

fix7_count = 0
fix8_count = 0
fix9_count = 0
fix10_count = 0

audit_A = []
audit_B = []
audit_C = []

pages_with_issues = set()
total_files = len(all_files)

# Patterns
lib_pattern = r'<section class="sv-section-(?:grey|white)"[^>]*?style="padding:\s*32px\s+0;?"[^>]*>\s*<div class="container">\s*<div style="display:flex;[^>]*border-left:4px solid var\(--primary-blue\)[^>]*">\s*<span[^>]*>(.*?)</span>\s*<div[^>]*>\s*<p[^>]*>(.*?)</p>\s*<p[^>]*>(.*?)</p>\s*</div>\s*<a href="([^"]+)"[^>]*>(.*?)</a>\s*</div>\s*</div>\s*</section>'
repl_lib = r'''<section class="sv-section-grey brand-contact-section">
  <div class="container">
    <div class="brand-contact-card">
      <span class="brand-contact-icon">\1</span>
      <div class="brand-contact-body">
        <p class="brand-contact-name">\2</p>
        <p class="brand-contact-detail">\3</p>
      </div>
      <a href="\4" class="btn btn-outline-dark brand-contact-cta">\5</a>
    </div>
  </div>
</section>'''

def repl_notice(m):
    div = m.group(0)
    div = re.sub(r'style="margin-top:\s*40px;\s*border-color:\s*#d97706;\s*background:\s*#fffbeb;?"', '', div)
    div = re.sub(r'style="color:\s*#92400e;?"', '', div)
    div = div.replace('class="brand-scope-box"', 'class="brand-notice-box"')
    div = re.sub(r'class="brand-scope-label"\s*', '', div)
    return div

margin_pattern = r'<div([^>]*)style="margin-top:\s*(40|32)px;?"([^>]*)>'

def repl_margin(m):
    before = m.group(1)
    val = m.group(2)
    after = m.group(3)
    attrs = before + " " + after
    if 'class="' in attrs:
        attrs = re.sub(r'class="([^"]*)"', rf'class="\1 mt-{val}"', attrs)
    else:
        attrs += f' class="mt-{val}"'
    attrs = re.sub(r'\s+', ' ', attrs).strip()
    return f'<div {attrs}>' if attrs else '<div>'

for relpath in all_files:
    filepath = os.path.join(base_dir, relpath)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    orig_html = html
    
    # FIX 7
    if relpath in fix7_files:
        html, n = re.subn(lib_pattern, repl_lib, html, flags=re.DOTALL)
        if n > 0: fix7_count += 1

    # FIX 8
    if relpath in fix8_files:
        html, n = re.subn(r'<div[^>]*style="margin-top:\s*40px;\s*border-color:\s*#d97706;\s*background:\s*#fffbeb;?"[^>]*>.*?</div>', repl_notice, html, flags=re.DOTALL)
        if n > 0: fix8_count += 1

    # FIX 9
    if relpath in fix9_files:
        html, n = re.subn(margin_pattern, repl_margin, html)
        if n > 0: fix9_count += 1

    # FIX 10
    if relpath in fix10_files:
        head_body = html.split('<body', 1)
        if len(head_body) == 2:
            body_content = '<body' + head_body[1]
            body_content, _ = re.subn(r'<p[^>]*>\s*L/PS/\d+/\d{4}P\s*</p>', r'<span class="sv-licence"></span>', body_content)
            body_content, _ = re.subn(r'<span[^>]*>\s*L/PS/\d+/\d{4}P\s*</span>', r'<span class="sv-licence"></span>', body_content)
            body_content, n = re.subn(r'L/PS/\d+/\d{4}P', r'<span class="sv-licence"></span>', body_content)
            if n > 0: fix10_count += 1
            html = head_body[0] + body_content

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

    # B. Remaining hardcoded licence
    def extract_visible_text(s_obj):
        texts = []
        for text in s_obj.find_all(string=True):
            if text.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']: continue
            if isinstance(text, Comment): continue
            ss = text.strip()
            if ss: texts.append((text.parent.sourceline, ss, text.parent))
        return texts

    for line, text, parent in extract_visible_text(soup):
        if re.search(r'L/PS/', text):
            audit_B.append(f"{relpath}:{line}: L/PS/ licence number")
            page_has_issues = True

    # C. Remaining margin-top inline styles on divs
    for div in soup.find_all('div', style=True):
        if 'margin-top:' in div['style']:
            audit_C.append(f"{relpath}:{div.sourceline}: style='{div['style']}'")
            page_has_issues = True

    if page_has_issues:
        pages_with_issues.add(relpath)

out = f"""BRANDS SECTION FIX — WAVE 2 COMPLETION REPORT
Files processed: {total_files}
Files modified: {fix7_count + fix8_count + fix9_count + fix10_count} (logical updates)

FIX 7  — Missed brand-contact-card conversions: {fix7_count} pages updated
FIX 8  — Amber notice boxes replaced: {fix8_count} pages updated
FIX 9  — Lone margin-top inline styles replaced: {fix9_count} pages updated
FIX 10 — Hardcoded licence numbers replaced: {fix10_count} pages updated

AUDIT FINDINGS (report only — not auto-fixed):
A. Remaining inline styles:
{chr(10).join(audit_A) if audit_A else "None"}

B. Remaining licence numbers:
{chr(10).join(audit_B) if audit_B else "None"}

C. Remaining margin-top inline styles:
{chr(10).join(audit_C) if audit_C else "None"}

Pages with no remaining issues after Wave 2: {total_files - len(pages_with_issues)}
Pages still requiring manual review:
{chr(10).join(sorted(list(pages_with_issues))) if pages_with_issues else "None"}
"""

with open("C:/Projects/SV-Build/_ai/audit-brands-wave2-completion.md", "w", encoding='utf-8') as f:
    f.write(out)

print("Wave 2 completion report generated.")
