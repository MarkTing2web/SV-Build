import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import re

insights_dir = r"C:\Projects\SV-Build\insights"
dry_run = False  # WRITE MODE

# ── Part 1: Standard numbering for 19 articles ──
slugs = [
    "access-control-multi-door",
    "alarm-usage-habits",
    "architect-security-guide",
    "auto-gate-motor",
    "break-in-nearby-security-review",
    "cctv-ai-upgrade",
    "cctv-cable-upgrade",
    "cctv-pdpa-compliance",
    "cctv-retail-analytics",
    "cctv-system-components",
    "compare-security-integrators",
    "condo-security-upgrade-proposals",
    "gate-remote-smartphone",
    "installer-leaves",
    "lpr-vs-rfid-condo",
    "mcst-security-tender",
    "mechanical-locks-not-enough",
    "network-security-systems",
    "system-repair-or-replace",
]

print("--- RUNNING SCRIPT 1 ---")
for slug in slugs:
    filepath = os.path.join(insights_dir, f"{slug}.html")
    if not os.path.exists(filepath):
        print(f"MISSING: {slug}.html")
        continue

    with open(filepath, encoding='utf-8', errors='ignore') as f:
        content = f.read()

    prose_match = re.search(
        r'(<main[^>]*class=["\']prose["\'][^>]*>)(.*?)(</main>)',
        content, re.DOTALL
    )
    if not prose_match:
        print(f"NO PROSE BLOCK: {slug}")
        continue

    prose = prose_match.group(2)
    counter = [0]

    def fix_heading(match):
        tag_open = match.group(1)
        text = match.group(2).strip()
        tag_close = match.group(3)
        if re.match(r'^\d+\.', text):
            return match.group(0)
        if re.search(r'frequently asked|FAQ', text, re.IGNORECASE):
            return match.group(0)
        counter[0] += 1
        return f"{tag_open}{counter[0]}. {text}{tag_close}"

    new_prose = re.sub(r'(<h2[^>]*>)([^<]+)(</h2>)', fix_heading, prose)

    if new_prose != prose:
        new_content = content.replace(prose_match.group(2), new_prose)
        if not dry_run:
            with open(filepath, encoding='utf-8', mode='w') as f:
                f.write(new_content)
        print(f"UPDATED: {slug}")
    else:
        print(f"NO CHANGE: {slug}")

print()

# ── Part 2: Special handling for choose-intercom-for-home ──
print("--- RUNNING SCRIPT 2 ---")
filepath = r"C:\Projects\SV-Build\insights\choose-intercom-for-home.html"

with open(filepath, encoding='utf-8') as f:
    content = f.read()

prose_match = re.search(
    r'(<main[^>]*class=["\']prose["\'][^>]*>)(.*?)(</main>)',
    content, re.DOTALL
)

counter = [0]

def fix_heading_intercom(match):
    tag_open = match.group(1)
    text = match.group(2).strip()
    tag_close = match.group(3)
    # Strip "Question N: " prefix if present
    text = re.sub(r'^Question\s+\d+:\s*', '', text)
    # Skip if already numbered
    if re.match(r'^\d+\.', text):
        return match.group(0)
    # Skip FAQ
    if re.search(r'frequently asked|FAQ', text, re.IGNORECASE):
        return match.group(0)
    counter[0] += 1
    return f"{tag_open}{counter[0]}. {text}{tag_close}"

new_prose = re.sub(
    r'(<h2[^>]*>)([^<]+)(</h2>)',
    fix_heading_intercom,
    prose_match.group(2)
)

new_content = content.replace(prose_match.group(2), new_prose)

if not dry_run:
    with open(filepath, encoding='utf-8', mode='w') as f:
        f.write(new_content)

print("UPDATED: choose-intercom-for-home")
print()
print("Verify headings:")
prose_check = re.search(
    r'<main[^>]*class=["\']prose["\'][^>]*>(.*?)</main>',
    new_content, re.DOTALL
)
for h in re.findall(r'<h2[^>]*>([^<]+)</h2>', prose_check.group(1)):
    print(f"  {h.strip()}")
