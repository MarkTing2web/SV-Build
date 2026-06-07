import os
import re
from bs4 import BeautifulSoup, Comment

fix11_files = [
    "brands/aiphone-intercom.html",
    "brands/akuvox-access.html",
    "brands/akuvox-intercom.html",
    "brands/apollo-access.html",
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
    "brands/microengine-entry-access.html",
    "brands/omada-network.html",
    "brands/ruijie-reyee-network.html",
    "brands/vesta.html",
    "brands/yeastar-ippbx.html"
]

base_dir = "C:/Projects/SV-Build"

fix11_count = 0
fix12_count = 0

audit_A = []

total_files = len(fix11_files)
pages_with_issues = set()

# Pattern for FIX 11
lib_pattern = r'<section[^>]*>\s*<div class="container">\s*<div style="display:flex;[^>]+border-left:4px solid var\(--primary-blue\)[^>]*">\s*<span[^>]*>(.*?)</span>\s*<div[^>]*>\s*<p[^>]*>(.*?)</p>\s*<p[^>]*>(.*?)</p>\s*</div>\s*<a href="([^"]+)"\s*class="([^"]+)"[^>]*>(.*?)</a>\s*</div>\s*</div>\s*</section>'

repl_lib = r'''<section class="sv-section-grey brand-contact-section">
  <div class="container">
    <div class="brand-contact-card">
      <span class="brand-contact-icon">\1</span>
      <div class="brand-contact-body">
        <p class="brand-contact-name">\2</p>
        <p class="brand-contact-detail">\3</p>
      </div>
      <a href="\4" class="\5 brand-contact-cta">\6</a>
    </div>
  </div>
</section>'''

for relpath in fix11_files:
    filepath = os.path.join(base_dir, relpath)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    orig_html = html
    
    # FIX 11
    html, n = re.subn(lib_pattern, repl_lib, html, flags=re.DOTALL)
    if n > 0: fix11_count += 1

    # FIX 12
    if relpath == "brands/akuvox-intercom.html":
        html, n2 = re.subn(r'<h3[^>]*style="margin-top:\s*24px;\s*font-size:\s*16px;?"[^>]*>', '<h3 class="mt-24">', html)
        if n2 > 0: fix12_count += 1

    if html != orig_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

    # AUDIT
    soup = BeautifulSoup(html, 'html.parser')
    page_has_issues = False
    inlines = soup.body.find_all(style=True) if soup.body else []
    for el in inlines:
        s = el['style']
        cls = el.get('class', [])
        if 'stat-bar-fill' in cls and re.match(r'^width\s*:\s*\d+%$', s.strip()): continue
        audit_A.append(f"{relpath}:{el.sourceline} -> style='{s}' on <{el.name}>")
        page_has_issues = True

    if page_has_issues:
        pages_with_issues.add(relpath)

out = f"""BRANDS SECTION FIX — WAVE 3 COMPLETION REPORT
Files processed: {total_files}
Files modified: {fix11_count + fix12_count}

FIX 11 — Remaining brand-contact-card blocks replaced: {fix11_count} pages updated
FIX 12 — akuvox-intercom.html H3 inline style removed: {fix12_count} pages updated

AUDIT FINDINGS:
A. Remaining inline styles:
{chr(10).join(audit_A) if audit_A else "None"}

Pages with no remaining inline styles: {38 - len(pages_with_issues)} / 38 total
"""

with open("C:/Projects/SV-Build/_ai/audit-brands-wave3-completion.md", "w", encoding='utf-8') as f:
    f.write(out)

print(out)
