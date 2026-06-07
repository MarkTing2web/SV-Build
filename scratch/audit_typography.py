import os
import re
from bs4 import BeautifulSoup
import json

files = [
    "C:/Projects/SV-Build/systems/index.html",
    "C:/Projects/SV-Build/systems/premises-security.html",
    "C:/Projects/SV-Build/systems/entry-access-control.html",
    "C:/Projects/SV-Build/systems/vehicle-lpr-management.html",
    "C:/Projects/SV-Build/systems/ip-phone-communications.html",
    "C:/Projects/SV-Build/systems/security-management-platform.html",
    "C:/Projects/SV-Build/systems/network-infrastructure.html"
]

def check_inline_font(style_str):
    if not style_str: return None
    violations = []
    for prop in style_str.split(';'):
        prop = prop.strip()
        if prop.startswith('color:') or prop.startswith('font-size:') or prop.startswith('font-family:') or prop.startswith('font-weight:'):
            violations.append(prop)
    return "; ".join(violations) if violations else None

def get_text_clean(element):
    if not element: return ""
    return re.sub(r'\s+', ' ', element.get_text()).strip()

report = ""
all_hierarchy_issues = []
all_inline_violations = []
all_coloured_eyebrows = []
all_wrong_ctas = []

card_classes = ["feature-card", "sys-group-card", "property-fit-card", "callout-box", "scenario-card", "arch-card", "rel-card", "sv-sys-card", "card"]

for filepath in files:
    filename = os.path.basename(filepath)
    report += f"---\n## {filename}\n\n"
    
    if not os.path.exists(filepath):
        report += "File not found.\n\n"
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Heading structure
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
    h_issues = []
    h1_count = len(soup.find_all('h1'))
    
    if h1_count == 0:
        h_issues.append("H1 is missing")
    elif h1_count > 1:
        h_issues.append(f"Multiple H1s found ({h1_count})")
        
    expected_level = 1
    report += "### Heading Structure\n"
    report += "| Line | Tag | Text | Issues |\n"
    report += "|---|---|---|---|\n"
    
    if not headings:
        report += "| - | - | No headings found | - |\n"
    
    for h in headings:
        level = int(h.name[1])
        text = get_text_clean(h)
        line = h.sourceline
        issue = ""
        
        if level > expected_level + 1:
            issue = f"Skipped level (expected H{expected_level+1} or lower, got H{level})"
            h_issues.append(issue)
        
        # update expected level based on current level
        if level == 1:
            expected_level = 1
        elif level > 1:
            expected_level = level
            
        report += f"| {line} | {h.name.upper()} | {text} | {issue or '—'} |\n"
    
    report += f"\nHeading issues: {', '.join(h_issues) if h_issues else 'none'}\n\n---\n\n"
    
    if h_issues:
        all_hierarchy_issues.append(filename)
        
    # 2. Hero Typography
    hero = soup.find('section', class_=lambda c: c and 'hero' in c) or soup.find('header')
    report += "### Hero Typography\n"
    
    h1_status = "missing"
    if h1_count == 1: h1_status = "present"
    elif h1_count > 1: h1_status = "multiple"
    
    eyebrow_class = "missing"
    subtitle_class = "missing"
    color_overrides = []
    
    if hero:
        # eyebrow usually precedes h1
        h1 = hero.find('h1')
        if h1:
            # find eyebrow
            eyebrow = h1.find_previous_sibling()
            if eyebrow:
                classes = eyebrow.get('class', [])
                inline = check_inline_font(eyebrow.get('style'))
                if inline:
                    eyebrow_class = f"inline style: {inline}"
                    color_overrides.append(f"Line {eyebrow.sourceline}: inline style {inline}")
                else:
                    eyebrow_class = " ".join(classes) if classes else "no class"
                
                # Check for color classes
                if any('text-' in c and c not in ['text-white', 'text-light'] for c in classes):
                    color_overrides.append(f"Line {eyebrow.sourceline}: color class {' '.join(classes)}")
                    all_coloured_eyebrows.append(f"{filename}: {' '.join(classes)}")
                    
            # find subtitle
            sub = h1.find_next_sibling()
            if sub:
                classes = sub.get('class', [])
                inline = check_inline_font(sub.get('style'))
                if inline:
                    subtitle_class = f"inline style: {inline}"
                    color_overrides.append(f"Line {sub.sourceline}: inline style {inline}")
                else:
                    subtitle_class = " ".join(classes) if classes else "no class"
                    
        # check all text in hero for overrides
        for el in hero.find_all(['h1', 'h2', 'h3', 'p', 'span', 'div']):
            inline = check_inline_font(el.get('style'))
            if inline and el.sourceline:
                color_overrides.append(f"Line {el.sourceline}: {inline}")
    
    report += f"- H1: {h1_status}\n"
    report += f"- Eyebrow class: {eyebrow_class}\n"
    report += f"- Subtitle class: {subtitle_class}\n"
    report += f"- Colour overrides: {', '.join(color_overrides) if color_overrides else 'none'}\n\n---\n\n"

    # 3. Trust Bar & Breadcrumb
    report += "### Trust Bar & Breadcrumb\n"
    trust_bar = soup.find(class_=lambda c: c and 'trust-bar' in c)
    breadcrumb = soup.find(class_=lambda c: c and 'breadcrumb' in c)
    
    trust_outer = "missing"
    trust_inner = "missing"
    trust_div = "missing"
    hardcoded = []
    
    if trust_bar:
        trust_outer = " ".join(trust_bar.get('class', []))
        inner = trust_bar.find(class_=lambda c: c and ('inner' in c or 'flex' in c))
        if inner: trust_inner = " ".join(inner.get('class', []))
        divs = trust_bar.find_all(class_=lambda c: c and ('divider' in c or 'sep' in c))
        if divs: trust_div = " ".join(divs[0].get('class', []))
        
        trust_text = get_text_clean(trust_bar).lower()
        if "licence" in trust_text or "license" in trust_text: hardcoded.append("licence number")
        if "year" in trust_text: hardcoded.append("years")
        if "site" in trust_text: hardcoded.append("sites")
        if "bizsafe" in trust_text: hardcoded.append("bizSAFE")
        
    bread_class = "missing"
    if breadcrumb:
        bread_class = " ".join(breadcrumb.get('class', []))
        
    report += f"- Trust bar outer: {trust_outer}\n"
    report += f"- Trust bar inner: {trust_inner}\n"
    report += f"- Divider class: {trust_div}\n"
    report += f"- Breadcrumb: {bread_class}\n"
    report += f"- Hardcoded values: {', '.join(hardcoded) if hardcoded else 'none'}\n\n---\n\n"
    
    # 4. Section Typography Audit
    report += "### Section Typography Audit\n"
    report += "| Section | H2 class | Body class / inline | Inline font violations |\n"
    report += "|---|---|---|---|\n"
    
    sections = soup.find_all('section')
    inline_violations_count = 0
    
    for sec in sections:
        sec_name = "Unnamed Section"
        h2 = sec.find('h2')
        if h2:
            sec_name = get_text_clean(h2)
        else:
            eyebrow = sec.find(class_=lambda c: c and 'eyebrow' in c)
            if eyebrow: sec_name = get_text_clean(eyebrow)
            
        h2_class = " ".join(h2.get('class', [])) if h2 else "no h2"
        
        body_classes = set()
        violations = []
        for p in sec.find_all('p'):
            cls = " ".join(p.get('class', []))
            if cls: body_classes.add(f"p.{cls.replace(' ', '.')}")
            else: body_classes.add("p")
            
        for el in sec.find_all(['p', 'span', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'li']):
            inline = check_inline_font(el.get('style'))
            if inline:
                violations.append(f"LINE {el.sourceline}: {inline}")
                inline_violations_count += 1
                
        body_str = ", ".join(body_classes) if body_classes else "no p tags"
        viol_str = "<br>".join(violations) if violations else "none"
        
        report += f"| {sec_name} | {h2_class} | {body_str} | {viol_str} |\n"
        
    report += "\n---\n\n"
    
    # 5. Card Audit
    report += "### Card Audit\n"
    report += "| Card type | Heading tag | Body tag | Inline font violations |\n"
    report += "|---|---|---|---|\n"
    
    # find any element whose class contains one of the card_classes
    def is_card(classes):
        if not classes: return False
        for c in classes:
            if c in card_classes or c.startswith("card-pad"): return True
        return False

    cards = soup.find_all(class_=is_card)
    
    if not cards:
        report += "| - | - | - | No cards found |\n"
        
    for card in cards:
        ctype = " ".join([c for c in card.get('class', []) if c in card_classes or c.startswith("card-pad")])
        h = card.find(['h2', 'h3', 'h4', 'h5', 'h6'])
        htag = f"{h.name.upper()} ({get_text_clean(h)})" if h else "—"
        
        p = card.find('p')
        ptag = "p" if p else "—"
        
        violations = []
        for el in card.find_all(['p', 'span', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'li']):
            inline = check_inline_font(el.get('style'))
            if inline:
                violations.append(f"LINE {el.sourceline}: {inline}")
                inline_violations_count += 1
                
        viol_str = "<br>".join(violations) if violations else "none"
        
        report += f"| {ctype} | {htag} | {ptag} | {viol_str} |\n"
        
    report += "\n---\n\n"
    
    # 6. CTA Section
    report += "### CTA Section\n"
    cta = soup.find(class_=lambda c: c and 'cta' in c)
    
    cta_class = "missing"
    h2_pres = "missing"
    sub_class = "missing"
    btn_label = "missing"
    cta_flag = "missing"
    
    if cta:
        cta_class = " ".join(cta.get('class', []))
        h2 = cta.find('h2')
        h2_pres = "present" if h2 else "missing"
        
        if h2:
            sub = h2.find_next_sibling()
            if sub:
                classes = sub.get('class', [])
                inline = check_inline_font(sub.get('style'))
                if inline:
                    sub_class = f"inline style: {inline}"
                else:
                    sub_class = " ".join(classes) if classes else "no class"
                    
        btn = cta.find('a', class_=lambda c: c and 'btn' in c)
        if btn:
            btn_label = get_text_clean(btn)
            if btn_label == "Book a Site Assessment":
                cta_flag = "correct"
            else:
                cta_flag = "WRONG — should be \"Book a Site Assessment\""
                all_wrong_ctas.append(f"{filename}: {btn_label}")
                
    report += f"- Class: {cta_class}\n"
    report += f"- H2: {h2_pres}\n"
    report += f"- Subtitle: {sub_class}\n"
    report += f"- Button label: \"{btn_label}\"\n"
    report += f"- CTA flag: {cta_flag}\n\n---\n\n"
    
    # 7. Summary
    if inline_violations_count > 0:
        all_inline_violations.append((filename, inline_violations_count))
        
    overall = "PASS" if not h_issues and inline_violations_count == 0 and cta_flag == "correct" else "NEEDS ATTENTION"
    
    report += "### Summary for this page\n"
    report += f"- Total inline font violations: {inline_violations_count}\n"
    report += f"- Heading hierarchy: {'clean' if not h_issues else 'issues: ' + ', '.join(h_issues)}\n"
    report += f"- Overall: {overall}\n\n"

# Cross-Page Summary
report += "---\n## Cross-Page Summary\n\n"

report += "### Pages with heading hierarchy issues:\n"
if all_hierarchy_issues:
    for page in all_hierarchy_issues:
        report += f"- {page}\n"
else:
    report += "None\n"
    
report += "\n### Pages with inline font violations:\n"
if all_inline_violations:
    for page, count in all_inline_violations:
        report += f"- {page}: {count} violations\n"
else:
    report += "None\n"
    
report += "\n### Coloured eyebrows found (non-standard):\n"
if all_coloured_eyebrows:
    for eb in all_coloured_eyebrows:
        report += f"- {eb}\n"
else:
    report += "None\n"
    
report += "\n### Wrong CTA labels:\n"
if all_wrong_ctas:
    for cta in all_wrong_ctas:
        report += f"- {cta}\n"
else:
    report += "None\n"
    
total_issues = len(all_hierarchy_issues) + len(all_inline_violations) + len(all_coloured_eyebrows) + len(all_wrong_ctas)
pages_with_issues = len(set(all_hierarchy_issues + [p[0] for p in all_inline_violations] + [c.split(':')[0] for c in all_coloured_eyebrows] + [c.split(':')[0] for c in all_wrong_ctas]))

status = "PASS" if total_issues == 0 else f"NEEDS ATTENTION — {total_issues} issues across {pages_with_issues} pages"

report += f"\n### Overall systems section typography status:\n{status}\n"

with open("C:/Projects/SV-Build/_ai/audit-systems-typography.md", "w", encoding='utf-8') as f:
    f.write(report)

print("Audit completed and saved.")
