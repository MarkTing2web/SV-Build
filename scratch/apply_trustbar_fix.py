import os
from bs4 import BeautifulSoup

files = [
    "C:/Projects/SV-Build/systems/premises-security.html",
    "C:/Projects/SV-Build/systems/entry-access-control.html",
    "C:/Projects/SV-Build/systems/vehicle-lpr-management.html",
    "C:/Projects/SV-Build/systems/ip-phone-communications.html",
    "C:/Projects/SV-Build/systems/security-management-platform.html",
    "C:/Projects/SV-Build/systems/network-infrastructure.html"
]

report = "# Trust Bar Fix — Completion Report\n\n"
fully_updated = 0
issues = []

for filepath in files:
    filename = os.path.basename(filepath)
    report += f"### {filename}\n"
    
    if not os.path.exists(filepath):
        report += "- File NOT FOUND\n\n"
        issues.append(f"{filename} not found")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Change A
    sv_trust_bar = soup.find('div', class_='sv-trust-bar')
    change_a = "NOT FOUND"
    if sv_trust_bar:
        # Update class list
        classes = sv_trust_bar.get('class', [])
        sv_trust_bar['class'] = [c if c != 'sv-trust-bar' else 'trust-bar' for c in classes]
        if 'sv-trust-bar' not in classes: # in case it was a single string not a list but bs4 returns list
            pass
        change_a = "DONE"
        
    trust_bar = sv_trust_bar or soup.find('div', class_='trust-bar')
    
    # Change B
    change_b = "NOT FOUND"
    if trust_bar:
        trust_flex_inline = trust_bar.find('div', class_='trust-flex-inline')
        if trust_flex_inline:
            classes = trust_flex_inline.get('class', [])
            trust_flex_inline['class'] = [c if c != 'trust-flex-inline' else 'trust-bar-inner' for c in classes]
            change_b = "DONE"
            
    # Change C
    change_c = "NOT FOUND"
    sep_count = 0
    if trust_bar:
        seps = trust_bar.find_all('span', class_='sep')
        for sep in seps:
            classes = sep.get('class', [])
            sep['class'] = [c if c != 'sep' else 'trust-divider' for c in classes]
            sep_count += 1
        if sep_count > 0:
            change_c = f"DONE — {sep_count} instances"
            
    # Change D
    change_d = "NOT FOUND"
    if trust_bar:
        bca_span = None
        for span in trust_bar.find_all('span'):
            if span.string and 'BCA Registered' in span.string:
                bca_span = span
                break
        if bca_span:
            prev = bca_span.find_previous_sibling('span')
            if prev and ('trust-divider' in prev.get('class', []) or 'sep' in prev.get('class', [])):
                prev.decompose()
            bca_span.decompose()
            change_d = "DONE"
            
    # Change E
    change_e = "NOT FOUND"
    if trust_bar:
        sv_sites = trust_bar.find('span', class_='sv-sites')
        if sv_sites:
            sv_sites.name = 'strong'
            change_e = "DONE"
            
    report += f"- Change A (sv-trust-bar → trust-bar): {change_a}\n"
    report += f"- Change B (trust-flex-inline → trust-bar-inner): {change_b}\n"
    report += f"- Change C (sep → trust-divider): {change_c}\n"
    report += f"- Change D (BCA Registered removed): {change_d}\n"
    report += f"- Change E (sv-sites wrapped in strong): {change_e}\n\n"
    
    if change_a == "DONE" and change_b == "DONE" and "DONE" in change_c and change_d == "DONE" and change_e == "DONE":
        fully_updated += 1
    else:
        missing = []
        if change_a == "NOT FOUND": missing.append("A")
        if change_b == "NOT FOUND": missing.append("B")
        if change_c == "NOT FOUND": missing.append("C")
        if change_d == "NOT FOUND": missing.append("D")
        if change_e == "NOT FOUND": missing.append("E")
        if missing:
            issues.append(f"{filename}: Missing changes {', '.join(missing)}")
            
    with open(filepath, 'w', encoding='utf-8') as f:
        # Use HTML formatter that doesn't modify empty tags too much
        # By default str(soup) is pretty safe
        f.write(str(soup))

report += f"## Summary\n"
report += f"- Files fully updated: {fully_updated}/6\n"
report += f"- Any issues: "
if issues:
    report += ", ".join(issues) + "\n"
else:
    report += "None\n"

with open("C:/Projects/SV-Build/_ai/audit-trustbar-fix.md", "w", encoding='utf-8') as f:
    f.write(report)
    
print("Trust bar fixes applied using DOM parser.")
