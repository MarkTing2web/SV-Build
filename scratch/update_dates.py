import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import re
import glob
from datetime import datetime
import platform

insights_dir = r"C:\Projects\SV-Build\insights"

# ── Step 1: Load all dates from site-config.js (UTF-16) ──
sc_path = r"C:\Projects\SV-Build\site-config.js"
try:
    with open(sc_path, encoding='utf-16') as f:
        sc_content = f.read()
except UnicodeDecodeError:
    with open(sc_path, encoding='utf-8') as f:
        sc_content = f.read()

entries = re.findall(r'\{[^{}]+\}', sc_content)
sc_dates = {}
for entry in entries:
    slug = re.search(r'slug:\s*"([^"]+)"', entry)
    date = re.search(r'date:\s*"([^"]+)"', entry)
    if slug and date:
        sc_dates[slug.group(1)] = date.group(1)

# ── Step 2: Build human-readable date string ──
def human_date(iso_date):
    dt = datetime.strptime(iso_date, '%Y-%m-%d')
    if platform.system() == 'Windows':
        return dt.strftime('%#d %b %Y')
    return dt.strftime('%-d %b %Y')

# ── Step 3: Process each HTML file ──
html_files = glob.glob(os.path.join(insights_dir, '*.html'))
updated = []
skipped_no_date = []
no_change = []

for filepath in sorted(html_files):
    slug = os.path.basename(filepath).replace('.html', '')

    # Skip index
    if slug == 'index':
        continue

    # Skip if no date in site-config
    if slug not in sc_dates:
        skipped_no_date.append(slug)
        continue

    iso_date = sc_dates[slug]
    human = human_date(iso_date)

    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Fix article:published_time meta tag
    content = re.sub(
        r'(property=["\']article:published_time["\'][^>]*content=["\'])([^"\']+)(["\'])',
        lambda m: m.group(1) + iso_date + m.group(3),
        content
    )
    content = re.sub(
        r'(content=["\'])([^"\']+)(["\'][^>]*property=["\']article:published_time["\'])',
        lambda m: m.group(1) + iso_date + m.group(3),
        content
    )

    # 2. Fix JSON-LD datePublished
    content = re.sub(
        r'("datePublished":\s*")([^"]+)(")',
        lambda m: m.group(1) + iso_date + m.group(3),
        content
    )

    # 3. Fix visible byline date
    content = re.sub(
        r'(hero-byline-role[^>]*>.*?)(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{4})(.*?</p>)',
        lambda m: m.group(1) + human + m.group(3),
        content,
        flags=re.DOTALL
    )

    if content != original:
        with open(filepath, encoding='utf-8', mode='w') as f:
            f.write(content)
        updated.append((slug, iso_date, human))
        print(f"UPDATED: {slug} → {iso_date} / {human}")
    else:
        no_change.append(slug)

print()
print(f"Updated:                {len(updated)}")
print(f"No change needed:       {len(no_change)}")
print(f"Skipped (not in SC):    {len(skipped_no_date)}")
if skipped_no_date:
    print("Not in site-config:")
    for s in skipped_no_date:
        print(f"  {s}")
