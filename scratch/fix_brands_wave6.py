import os
import re

base_dir = "C:/Projects/SV-Build"
brands_dir = os.path.join(base_dir, "brands")

files_in_scope = [
    "aiphone-intercom.html", "ajax-alarms.html", "akuvox-access.html", "akuvox-intercom.html",
    "apollo-access.html", "dahua-cctv.html", "dormer-autogate.html", "dsc-alarms.html",
    "ebelco-locks.html", "entrypass-entry-access.html", "faac-autogate.html", "fanvil-intercom.html",
    "fanvil-ip-phone.html", "gantrygo.html", "ge-caddx-alarms.html", "hanwha-cctv.html",
    "hid-entry-access.html", "hikcentral.html", "hikvision-access.html", "hikvision-cctv.html",
    "hikvision-intercom.html", "hrui-network.html", "kocom-intercom.html", "mag-autogate.html",
    "microengine-entry-access.html", "milesight-cctv.html", "omada-network.html", "paradox-alarms.html",
    "risco-alarms.html", "ruijie-reyee-network.html", "suprema-entry-access.html", "uniview-cctv.html",
    "vesta.html", "viro-locks.html", "yealink-ip-phone.html", "yeastar-ippbx.html",
    "zkteco-cvsecurity.html", "zkteco-entry-access.html"
]

stats = {
    'processed': 38,
    'modified': 0,
    'skipped': 0,
    'fixed': 0
}

audit = {
    'A': [],
    'B': [],
    'C': []
}

for filename in files_in_scope:
    filepath = os.path.join(brands_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    orig_html = html
    
    # Check if already correct
    if '</header>' in html.split('<div class="trust-bar">')[0]:
        stats['skipped'] += 1
        audit['C'].append(filename)
    else:
        # Find the first </section> followed by <div class="trust-bar">
        match = re.search(r'</section>(\s*(?:<!--.*?-->\s*)?<div class="trust-bar">)', html)
        if match:
            # Check if this is the FIRST </section>
            first_section_idx = html.find('</section>')
            if first_section_idx == match.start():
                html = html[:match.start()] + '</header>' + html[match.start() + 10:]
                stats['fixed'] += 1
            else:
                # It's not the first </section>, flag for manual review
                pass
        else:
            # Trust bar not found after a section? Let's check with another regex just in case
            pass
            
    if html != orig_html:
        stats['modified'] += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)

# Audit Check
for filename in files_in_scope:
    filepath = os.path.join(brands_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    parts = html.split('<div class="trust-bar">', 1)
    before_trust = parts[0] if len(parts) > 1 else html
    
    # A. Any page where `<header class="hero` appears but is not closed by `</header>` before the first `<div class="trust-bar">`
    if '<header class="hero' in before_trust and '</header>' not in before_trust:
        audit['A'].append(filename)
        
    # B. Any page where `</header>` appears more than once
    if html.count('</header>') > 1:
        audit['B'].append(filename)
        
out = []
out.append("BRANDS SECTION FIX — WAVE 6 COMPLETION REPORT")
out.append(f"Files processed: {stats['processed']}")
out.append(f"Files modified: {stats['modified']}")
out.append(f"Files already correct (skipped): {stats['skipped']}\n")
out.append(f"Hero closing tag fixed: {stats['fixed']} pages\n")
out.append("AUDIT FINDINGS:")
out.append(f"A. Pages with unclosed <header>: {', '.join(audit['A']) if audit['A'] else 'None'}")
out.append(f"B. Pages with multiple </header>: {', '.join(audit['B']) if audit['B'] else 'None'}")
out.append(f"C. Pages already correct (confirmed): {', '.join(audit['C']) if audit['C'] else 'None'}")

with open(os.path.join(base_dir, "_ai/audit-brands-wave6-completion.md"), 'w', encoding='utf-8') as f:
    f.write("\n".join(out))

print("Wave 6 completed.")
