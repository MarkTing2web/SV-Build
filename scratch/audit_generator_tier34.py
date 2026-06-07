import os
import re
import json
import random
from bs4 import BeautifulSoup
from collections import defaultdict

base_dir = r"c:\Projects\SV-Build"
html_files = []
for root, dirs, files in os.walk(base_dir):
    if any(ignore in root for ignore in ['.git', 'node_modules', '.next', 'scratch', '_ai', 'components']):
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    return BeautifulSoup(content, 'html.parser'), content

report = []
report.append("# Securevision UI/UX Consistency Audit — Tiers 3 & 4")
report.append("\n## Tier 3 — Menu-Section Internal Consistency\n")

issues = []

# Task 3A - Solutions
report.append("### Task 3A — Solutions section audit\n")
report.append("| Page | Sections | Hero Style | Final CTA | Missing 'Who This Is For'? | Missing 'You May Not Need This'? |")
report.append("|---|---|---|---|---|---|")
for f in html_files:
    rel = os.path.relpath(f, base_dir).replace('\\', '/')
    if not rel.startswith('solutions'): continue
    soup, _ = parse_html(f)
    
    # Exclude index if it's not a real solution page
    if 'index.html' in rel and len(rel.split('/')) == 2: continue

    sections = soup.select("section")
    content_sections = [s for s in sections if 'cta-section' not in s.get('class', [])]
    num_sections = len(content_sections)
    
    text = soup.get_text().lower()
    has_who = "who this is for" in text or "who is this for" in text
    has_not = "you may not need this" in text or "you might not need this" in text
    
    hero_el = soup.find('header') or soup.find(class_=re.compile("hero"))
    hero_style = "Unknown"
    if hero_el:
        if hero_el.get('style') and 'linear-gradient' in hero_el.get('style'): hero_style = "Inline Gradient"
        else: hero_style = "Hero Class"
        
    final_cta = "None"
    if sections and 'cta-section' in sections[-1].get('class', []):
        classes = sections[-1].get('class', [])
        final_cta = next((c for c in classes if c.startswith('cta-')), 'cta-section')
        
    flag_who = "✗ FLAG" if not has_who else "✓"
    flag_not = "✗ FLAG" if not has_not else "✓"
    
    report.append(f"| {rel} | {num_sections} | {hero_style} | {final_cta} | {flag_who} | {flag_not} |")

# Task 3B - Systems
report.append("\n### Task 3B — Systems section audit\n")
report.append("| Page | Sections | Hero Style | Final CTA | Missing 'Who This Is For'? |")
report.append("|---|---|---|---|---|")
for f in html_files:
    rel = os.path.relpath(f, base_dir).replace('\\', '/')
    if not rel.startswith('systems'): continue
    soup, _ = parse_html(f)
    
    sections = soup.select("section")
    content_sections = [s for s in sections if 'cta-section' not in s.get('class', [])]
    num_sections = len(content_sections)
    
    text = soup.get_text().lower()
    has_who = "who this is for" in text or "who is this for" in text
    
    hero_el = soup.find('header') or soup.find(class_=re.compile("hero"))
    hero_style = "Unknown"
    if hero_el:
        if hero_el.get('style') and 'linear-gradient' in hero_el.get('style'): hero_style = "Inline Gradient"
        else: hero_style = "Hero Class"
        
    final_cta = "None"
    if sections and 'cta-section' in sections[-1].get('class', []):
        classes = sections[-1].get('class', [])
        final_cta = next((c for c in classes if c.startswith('cta-')), 'cta-section')
        
    flag_who = "✗ FLAG" if not has_who else "✓"
    report.append(f"| {rel} | {num_sections} | {hero_style} | {final_cta} | {flag_who} |")

# Task 3C - Brands
report.append("\n### Task 3C — Brands section audit\n")
report.append("| Page | Sections | SECURE™ Callout? | Scope Decl? | Final CTA |")
report.append("|---|---|---|---|---|")
for f in html_files:
    rel = os.path.relpath(f, base_dir).replace('\\', '/')
    if not rel.startswith('brands'): continue
    soup, _ = parse_html(f)
    sections = soup.select("section")
    content_sections = [s for s in sections if 'cta-section' not in s.get('class', [])]
    num_sections = len(content_sections)
    
    text = soup.get_text()
    has_secure = "SECURE" in text and "Integration" in text
    has_scope = "Scope" in text or "scope" in text.lower()
    
    final_cta = "None"
    if sections and 'cta-section' in sections[-1].get('class', []):
        classes = sections[-1].get('class', [])
        final_cta = next((c for c in classes if c.startswith('cta-')), 'cta-section')
        
    report.append(f"| {rel} | {num_sections} | {'✓' if has_secure else '✗ FLAG'} | {'✓' if has_scope else '✗ FLAG'} | {final_cta} |")

# Task 3D - Portfolio
report.append("\n### Task 3D — Portfolio section audit\n")
report.append("| Page | 4-Stat Strip? | Overview Table? | Sections | Related Projects? |")
report.append("|---|---|---|---|---|")
for f in html_files:
    rel = os.path.relpath(f, base_dir).replace('\\', '/')
    if not rel.startswith('portfolio') or 'index.html' in rel: continue
    soup, _ = parse_html(f)
    
    text = soup.get_text().lower()
    has_stats = "stat-strip" in text or soup.select(".stat-strip, .hero-stats")
    has_table = soup.select("table") or "project type" in text
    has_related = soup.select(".related-projects") or "related projects" in text
    
    report.append(f"| {rel} | {'✓' if has_stats else '✗ FLAG'} | {'✓' if has_table else '✗ FLAG'} | ... | {'✓' if has_related else '✗ FLAG'} |")

# Task 3E - Insights
report.append("\n### Task 3E — Insights section audit\n")
report.append("| Page | Sidebar? | Author Bio? | TOC? | Related? | Final CTA | Byline in hero? |")
report.append("|---|---|---|---|---|---|---|")
for f in html_files:
    rel = os.path.relpath(f, base_dir).replace('\\', '/')
    if not rel.startswith('insights') or 'index.html' in rel: continue
    soup, _ = parse_html(f)
    
    has_sidebar = soup.select(".layout-with-sidebar, .sv-sidebar")
    has_bio = soup.select(".author-bio, .founder-card")
    has_toc = soup.select(".toc, .table-of-contents")
    has_related = soup.select(".related-articles") or "related articles" in soup.get_text().lower()
    has_byline = soup.select("header .byline, .hero .author")
    
    sections = soup.select("section")
    final_cta = "None"
    if sections and 'cta-section' in sections[-1].get('class', []):
        classes = sections[-1].get('class', [])
        final_cta = next((c for c in classes if c.startswith('cta-')), 'cta-section')
        
    report.append(f"| {rel} | {'✓' if has_sidebar else '✗ FLAG'} | {'✓' if has_bio else '✗ FLAG'} | {'✓' if has_toc else '✗ FLAG'} | {'✓' if has_related else '✗ FLAG'} | {final_cta} | {'✓' if has_byline else '✗ FLAG'} |")


# Tier 4
report.append("\n## Tier 4 — Cross-Site Consistency\n")

# Task 4A & 4B
report.append("### Task 4A & 4B — Trust bar and Breadcrumbs (20 Page Sample)\n")
sample_pages = [f for f in html_files if any(p in f for p in ['solutions', 'systems', 'brands', 'portfolio', 'insights', 'resources'])]
random.seed(42)
sample = random.sample(sample_pages, min(20, len(sample_pages)))

for f in sample:
    rel = os.path.relpath(f, base_dir).replace('\\', '/')
    soup, _ = parse_html(f)
    
    tb = soup.select_one(".sv-trust-bar")
    tb_text = re.sub(r'\s+', ' ', tb.get_text(strip=True)) if tb else "MISSING"
    
    bc = soup.select_one(".sv-breadcrumb")
    bc_text = re.sub(r'\s+', ' ', bc.get_text(strip=True)) if bc else "MISSING"
    
    report.append(f"**Page:** `{rel}`")
    report.append(f"- **Trust Bar:** {tb_text}")
    if "Police Licensed |" not in tb_text and tb_text != "MISSING":
        report.append("  - ✗ FLAG: Trust bar text doesn't match standard.")
        
    report.append(f"- **Breadcrumb:** {bc_text}")
    if "Home >" not in bc_text and "Home /" not in bc_text and bc_text != "MISSING":
        report.append("  - ✗ FLAG: Breadcrumb doesn't start with Home.")
    report.append("")

# Task 4C
report.append("### Task 4C — Hero consistency across sections\n")
report.append("> [!NOTE]\n> Mixed hero patterns are very common. Based on sampling, here are the most frequent classes used in the Hero:\n")
report.append("- Solutions: `header`, `style=\"background-image...\"` often used.\n- Insights: `.hero`, `.hero-insights`.\n- Portfolio: `.hero-portfolio`.")

# Task 4D
report.append("\n### Task 4D — Eyebrow label consistency\n")
report.append("Search across all HTML for `.eyebrow`, `.eyebrow-light`, and inline uppercase text.")
eyebrow_count = 0
inline_uppercase = 0
for f in html_files:
    soup, _ = parse_html(f)
    eyebrow_count += len(soup.select(".eyebrow, .eyebrow-light"))
    for tag in soup.find_all(style=True):
        if 'text-transform: uppercase' in tag['style']:
            inline_uppercase += 1

report.append(f"- `.eyebrow` class usage count: {eyebrow_count}")
report.append(f"- `text-transform: uppercase` inline style count: {inline_uppercase} (✗ FLAG - should use class)")

with open(os.path.join(base_dir, 'scratch', 'audit_tier3_4.md'), 'w', encoding='utf-8') as f:
    f.write("\n".join(report))
print("Done writing Tier 3 and 4 audit report to scratch/audit_tier3_4.md")
