import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import re
import glob

insights_dir = r"C:\Projects\SV-Build\insights"
html_files = sorted(glob.glob(os.path.join(insights_dir, "*.html")))

toc_issues = []
h2_issues = []

for filepath in html_files:
    slug = os.path.basename(filepath).replace('.html', '')
    if slug == 'index':
        continue

    with open(filepath, encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # ── Check TOC entries ──
    toc_block = re.search(r'class=["\']toc-list["\'][^>]*>(.*?)</ul>', content, re.DOTALL)
    if toc_block:
        toc_items = re.findall(r'<a[^>]*>([^<]+)</a>', toc_block.group(1))
        unnumbered_toc = [t.strip() for t in toc_items if not re.match(r'^\d+\.', t.strip())]
        if unnumbered_toc:
            toc_issues.append((slug, unnumbered_toc))

    # ── Check H2 section headings ──
    prose_block = re.search(r'<main[^>]*class=["\']prose["\'][^>]*>(.*?)</main>', content, re.DOTALL)
    if prose_block:
        h2_texts = re.findall(r'<h2[^>]*>([^<]+)</h2>', prose_block.group(1))
        unnumbered_h2 = [h.strip() for h in h2_texts if not re.match(r'^\d+\.', h.strip())]
        if unnumbered_h2:
            h2_issues.append((slug, unnumbered_h2))

print(f"Articles with TOC issues: {len(toc_issues)}")
if toc_issues:
    print("Slugs with unnumbered TOC entries:")
    for slug, items in toc_issues:
        print(f"  - {slug} ({len(items)} unnumbered items)")

print()
print(f"Articles with H2 issues: {len(h2_issues)}")
if h2_issues:
    print("Slugs with unnumbered H2 headings:")
    for slug, headings in h2_issues:
        print(f"  - {slug} ({len(headings)} unnumbered headings)")
        # Show first 2 unnumbered headings as examples
        for h in headings[:2]:
            print(f"      * Example: {h}")
        if len(headings) > 2:
            print(f"      * ... and {len(headings)-2} more")
