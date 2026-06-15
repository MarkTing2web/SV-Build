import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import re

insights_dir = r"C:\Projects\SV-Build\insights"
dry_run = True  # SET TO FALSE ONLY WHEN INSTRUCTED TO WRITE

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
    "choose-intercom-for-home",
    "compare-security-integrators",
    "condo-security-upgrade-proposals",
    "gate-remote-smartphone",
    "installer-leaves",
    "lpr-vs-rfid-condo",
    "mcst-security-tender",
    "mechanical-locks-not-enough",
    "network-security-systems",
    "security-assessment-10-things",
    "system-repair-or-replace",
]

for slug in slugs:
    filepath = os.path.join(insights_dir, f"{slug}.html")
    if not os.path.exists(filepath):
        print(f"MISSING: {slug}.html")
        continue

    with open(filepath, encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find the prose block
    prose_match = re.search(
        r'(<main[^>]*class=["\']prose["\'][^>]*>)(.*?)(</main>)',
        content, re.DOTALL
    )
    if not prose_match:
        print(f"NO PROSE BLOCK: {slug}")
        continue

    prose = prose_match.group(2)

    # Find all H2 tags and their text
    h2_pattern = re.compile(r'(<h2[^>]*>)([^<]+)(</h2>)')
    h2_matches = list(h2_pattern.finditer(prose))

    if not h2_matches:
        print(f"NO H2s: {slug}")
        continue

    print(f"\n{'='*60}")
    print(f"ARTICLE: {slug}")
    print(f"{'='*60}")

    new_prose = prose
    counter = 1

    for match in h2_matches:
        tag_open = match.group(1)
        original_text = match.group(2).strip()
        tag_close = match.group(3)

        # Strip "Question N: " prefix if present
        cleaned_text = re.sub(r'^Question\s+\d+:\s*', '', original_text)

        # Skip if already numbered
        if re.match(r'^\d+\.', cleaned_text):
            print(f"  SKIP (already numbered): {cleaned_text}")
            continue

        # Skip FAQ heading
        if re.search(r'frequently asked|FAQ', cleaned_text, re.IGNORECASE):
            print(f"  SKIP (FAQ): {cleaned_text}")
            continue

        new_text = f"{counter}. {cleaned_text}"
        print(f"  {original_text}")
        print(f"  → {new_text}")
        counter += 1

        if not dry_run:
            new_prose = new_prose.replace(
                match.group(0),
                tag_open + new_text + tag_close,
                1
            )

    if not dry_run:
        new_content = content.replace(prose_match.group(2), new_prose)
        with open(filepath, encoding='utf-8', mode='w') as f:
            f.write(new_content)
        print(f"  ✅ WRITTEN")

if dry_run:
    print()
    print("DRY RUN COMPLETE — no files were modified")
    print("Review the proposed changes above, then set dry_run = False to apply")
