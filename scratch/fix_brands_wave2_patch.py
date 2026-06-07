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

all_files = set(fix7_files + fix8_files)
base_dir = "C:/Projects/SV-Build"

fix7_count = 0
fix8_count = 0

audit_A = []
audit_B = []
audit_C = []

total_files = 29

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
        # Match the div and replace attributes
        def repl_notice(m):
            div = m.group(0)
            div = re.sub(r'style="margin-top:\s*40px;\s*border-color:\s*#d97706;\s*background:\s*#fffbeb;?"', '', div)
            div = re.sub(r'style="color:\s*#92400e;?"', '', div)
            div = div.replace('class="brand-scope-box"', 'class="brand-notice-box"')
            div = re.sub(r'class="brand-scope-label"\s*', '', div)
            return div
        
        html, n = re.subn(r'<div[^>]*style="margin-top:\s*40px;\s*border-color:\s*#d97706;\s*background:\s*#fffbeb;?"[^>]*>.*?</div>', repl_notice, html, flags=re.DOTALL)
        if n > 0: fix8_count += 1

    if html != orig_html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

print(f"Fix 7 applied to {fix7_count} files")
print(f"Fix 8 applied to {fix8_count} files")
