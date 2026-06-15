import os
import re

site_config_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\site-config.js"
insights_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\insights"

# Read site-config.js
with open(site_config_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract slugs from SECUREVISION.insights
# Example format: { slug: "burglar-alarm-design", ... }
# Or { slug: 'burglar-alarm-design', ... }
slug_matches = re.findall(r'slug:\s*["\']([^"\']+)["\']', content)

# Keep only those under SECUREVISION.insights (or all of them, but let's be careful. The registry list starts at SECUREVISION.insights = [ ... ])
# Let's find the section for SECUREVISION.insights
insights_section_match = re.search(r'SECUREVISION\.insights\s*=\s*\[(.*?)\];', content, re.DOTALL)
if insights_section_match:
    insights_section = insights_section_match.group(1)
    slugs = re.findall(r'slug:\s*["\']([^"\']+)["\']', insights_section)
else:
    print("Could not find SECUREVISION.insights section!")
    slugs = []

# List html files in insights/ folder
html_files = [f for f in os.listdir(insights_dir) if f.endswith('.html')]
html_slugs = [f[:-5] for f in html_files]

print(f"Total slugs in config: {len(slugs)}")
print(f"Total html files in folder: {len(html_files)}")

matching = []
missing_html = []
for slug in slugs:
    if slug in html_slugs:
        matching.append(slug)
    else:
        missing_html.append(slug)

unregistered = []
for h_slug in html_slugs:
    # exclude index.html
    if h_slug == 'index':
        continue
    if h_slug not in slugs:
        unregistered.append(h_slug + ".html")

print("\n--- MATCHING ---")
for m in sorted(matching):
    print(f"- {m}")

print("\n--- MISSING HTML ---")
for m in sorted(missing_html):
    print(f"- {m}")

print("\n--- UNREGISTERED ---")
for u in sorted(unregistered):
    print(f"- {u}")
