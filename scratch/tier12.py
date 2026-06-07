import os
import glob
from bs4 import BeautifulSoup
import re
import json

base_dir = r"c:\Projects\SV-Build"
target_folders = [
    "solutions", "systems", "brands", "portfolio", 
    "insights", "resources"
]

def get_html_files():
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        # Exclude common ignore dirs
        if any(ignore in root for ignore in ['.git', 'node_modules', '.next', 'scratch']):
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

html_files = get_html_files()

report = []

# Task 1A - Page Inventory
report.append("## Task 1A — Page inventory\n")
folder_inventory = {}
for file in html_files:
    rel_path = os.path.relpath(file, base_dir)
    folder = os.path.dirname(rel_path)
    if not folder:
        folder = "/"
    if folder not in folder_inventory:
        folder_inventory[folder] = []
    folder_inventory[folder].append(os.path.basename(file))

for folder, files in sorted(folder_inventory.items()):
    report.append(f"### Folder: {folder}")
    report.append(f"Number of HTML files: {len(files)}")
    report.append(f"Files: {', '.join(sorted(files))}\n")


# Task 1B - Structure check
report.append("## Task 1B — Structure check\n")

target_folders_1b = [
    "solutions", "systems", "brands", "portfolio", "insights",
    r"resources\guides", r"resources\checklists"
]

report.append("| Page | nav | hero | trust-bar | breadcrumb | sections alternate? | final-cta | footer | wa-float | sidebar present? | sidebar correct? |")
report.append("|---|---|---|---|---|---|---|---|---|---|---|")

def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    return BeautifulSoup(content, 'html.parser'), content

for file in html_files:
    rel_path = os.path.relpath(file, base_dir)
    folder = os.path.dirname(rel_path)
    is_target = False
    for t in target_folders_1b:
        if folder.startswith(t):
            is_target = True
            break
    if file.endswith("resources\\faq.html"):
        is_target = True
        
    if not is_target:
        continue

    soup, _ = parse_html(file)
    
    # Check elements
    nav = "✓" if soup.find("nav", id="sv-nav") else "✗"
    hero = "✓" if soup.find("header") else "✗"  # assuming header is hero
    trust_bar = "✓" if soup.select(".sv-trust-bar") else "✗"
    breadcrumb = "✓" if soup.select(".sv-breadcrumb") else "✗"
    
    # Alternating sections (simplified for table, checked properly in 1C)
    sections = soup.select("section.section")
    # Let's say check if classes alternate bg-light vs nothing
    alternates = "✓"
    prev_bg = None
    for sec in sections:
        classes = sec.get('class', [])
        is_light = 'bg-light' in classes
        if prev_bg is not None and prev_bg == is_light:
            alternates = "✗"
            break
        prev_bg = is_light
        
    final_cta = "✗"
    if sections:
        last_sec = sections[-1]
        if 'cta-section' in last_sec.get('class', []):
            final_cta = "✓"
            
    footer = "✓" if soup.find("footer", id="sv-footer") else "✗"
    wa_float = "✓" if soup.select(".sv-wa-float") else "✗"
    
    has_sidebar = "yes" if soup.select(".layout-with-sidebar, .sv-sidebar") else "no"
    
    # Sidebar rule: Only /insights/ and /resources/guides/
    should_have_sidebar = folder.startswith("insights") or folder.startswith(r"resources\guides")
    sidebar_correct = "correct" if (has_sidebar == "yes") == should_have_sidebar else "wrong"
    
    # Standardize windows paths for output
    rel_path_str = rel_path.replace('\\', '/')
    report.append(f"| {rel_path_str} | {nav} | {hero} | {trust_bar} | {breadcrumb} | {alternates} | {final_cta} | {footer} | {wa_float} | {has_sidebar} | {sidebar_correct} |")

report.append("\n")

# Task 1C - Section background alternation
report.append("## Task 1C — Section background alternation check\n")
for file in html_files:
    rel_path = os.path.relpath(file, base_dir)
    folder = os.path.dirname(rel_path)
    if folder.startswith("solutions") or folder.startswith("systems"):
        soup, _ = parse_html(file)
        sections = soup.select("section.section")
        bg_sequence = []
        is_ok = True
        for sec in sections:
            classes = sec.get('class', [])
            style = sec.get('style', '')
            
            if 'cta-section' in classes:
                bg_sequence.append("CTA (dark)")
                continue
                
            if 'background' in style or 'bg-color' in style or '#' in style:
                bg_sequence.append("HARDCODED")
                is_ok = False
            elif 'bg-light' in classes:
                bg_sequence.append("grey")
            else:
                bg_sequence.append("white")
                
        # Check alternates
        for i in range(len(bg_sequence)-1):
            if bg_sequence[i] == bg_sequence[i+1] and "CTA" not in bg_sequence[i]:
                is_ok = False
                break
                
        status = "✓" if is_ok else "✗ FLAG"
        report.append(f"Page: {rel_path.replace('\\', '/')}")
        report.append(f"Section order: {' → '.join(bg_sequence)} {status}")

report.append("\n")

# Task 2A - Font Size
report.append("## Task 2A — CSS Consistency Audit (Font Sizes)\n")
css_files = [
    "assets/css/sv-shared.css",
    "assets/css/sv-solutions.css",
    "assets/css/sv-systems.css",
    "assets/css/sv-brands.css",
    "assets/css/sv-insights.css",
    "assets/css/sv-resources.css",
    "assets/css/sv-portfolio.css"
]

for css_file in css_files:
    full_path = os.path.join(base_dir, css_file.replace('/', '\\'))
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
            
        font_sizes = re.findall(r'(\.[a-zA-Z0-9_-]+|\w+)\s*{[^}]*?font-size:\s*([^;]+);', css_content, re.IGNORECASE | re.DOTALL)
        if font_sizes:
            report.append(f"### {os.path.basename(css_file)}")
            for sel, val in font_sizes:
                sel = sel.strip()
                val = val.strip()
                report.append(f"- `{sel}`: `font-size: {val}`")
    else:
        report.append(f"### {os.path.basename(css_file)} (NOT FOUND)")

report.append("\n")

# Task 2E - Buttons
report.append("## Task 2E — Button consistency audit\n")
buttons = {}
for file in html_files:
    soup, _ = parse_html(file)
    btns = soup.select("a.btn, button.btn")
    for b in btns:
        text = b.get_text(strip=True)
        if text not in buttons:
            buttons[text] = []
        rel_path = os.path.relpath(file, base_dir).replace('\\', '/')
        if rel_path not in buttons[text]:
            buttons[text].append(rel_path)

report.append("| Label | Count | Canonical? | Files |")
report.append("|---|---|---|---|")

canonical = [
    "Book a Site Assessment",
    "Request a Proposal",
    "💬 WhatsApp",
    "💬 Discuss a Similar Project"
]

retired = [
    "Book Free Site Assessment",
    "WhatsApp an Engineer",
    "💬 WhatsApp an Engineer",
    "Book Site Assessment"
]

for label, files in buttons.items():
    if not label:
        continue
    status = "?"
    if label in canonical:
        status = "✓"
    elif label in retired:
        status = "✗ RETIRED"
    elif "WhatsApp an Engineer" in label:
        status = "✗ RETIRED"
        
    file_list = ", ".join(files[:3]) + ("..." if len(files)>3 else "")
    report.append(f"| `{label}` | {len(files)} | {status} | {file_list} |")


with open(os.path.join(base_dir, 'scratch', 'audit_report_tier1_2.md'), 'w', encoding='utf-8') as f:
    f.write("\n".join(report))

print("Tier 1 and 2 report generated.")
