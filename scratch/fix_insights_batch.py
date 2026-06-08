import os
import re

INSIGHTS_DIR = r"C:\Projects\SV-Build\insights"

HAS_OLD_TRUST_BAR = {"index.html", "lpr-vs-rfid-vehicle-access-singapore.html", 
                     "pdpa-cctv-singapore.html", "video-analytics-retail-singapore.html"}

TRUST_BAR_HTML = """
<div class="trust-bar">
  <div class="trust-bar-inner">
    <span>Police Licensed &middot; <span class="sv-licence"></span></span>
    <span class="trust-divider"></span>
    <span>bizSAFE <span class="sv-bizsafe"></span></span>
    <span class="trust-divider"></span>
    <span><strong class="sv-sites"></strong> Sites Protected</span>
  </div>
</div>
"""

def process_file(fpath):
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Pass 1: CSS load order
    links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', content)
    if len(links) >= 3:
        pattern = re.escape(links[0]) + r'\s*' + re.escape(links[1]) + r'\s*' + re.escape(links[2])
        new_css = '<link rel="stylesheet" href="/sv-shared.css">\n    <link rel="stylesheet" href="/sv-insights.css">'
        content = re.sub(pattern, new_css, content, count=1)

    # Pass 2: Remove wa-float
    content = re.sub(r'<div[^>]*class="[^"]*wa-float[^"]*"[^>]*>.*?</div>', '', content, flags=re.DOTALL)

    # Pass 3: nav-footer.js
    content = re.sub(r'<script[^>]*src="[^"]*nav-footer\.js"[^>]*></script>\s*', '', content)
    content = re.sub(r'(</body>)', r'<script src="/nav-footer.js"></script>\n\1', content, flags=re.IGNORECASE)

    # Pass 4: Insert trust bar
    if fname not in HAS_OLD_TRUST_BAR:
        content = re.sub(
            r'(<nav[^>]*class="[^"]*sv-breadcrumb[^"]*")',
            TRUST_BAR_HTML.strip() + r'\n\n    \1',
            content, count=1
        )

    # Pass 5: CTA label
    if fname != "index.html":
        def cta_replacer(m):
            a_tag = m.group(0)
            a_tag = re.sub(r'href="[^"]*"', 'href="/request-proposal.html"', a_tag)
            a_tag = re.sub(r'Book a Site Assessment', 'Request a Proposal', a_tag, flags=re.IGNORECASE)
            return a_tag
        content = re.sub(r'<a[^>]*class="[^"]*\bbtn\b[^"]*"[^>]*>[\s\S]*?Book a Site Assessment[\s\S]*?</a>', cta_replacer, content, flags=re.IGNORECASE)

    # Pass 6: founder-card years
    if fname != "index.html":
        content = re.sub(r'\b(30|3[0-9]|4[0-9])\s*years\s+(of\s+)?experience\b', r'<span class="sv-years-experience"></span> years experience', content, flags=re.IGNORECASE)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

for fname in os.listdir(INSIGHTS_DIR):
    if fname.endswith(".html"):
        process_file(os.path.join(INSIGHTS_DIR, fname))
