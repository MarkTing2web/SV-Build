import re

site_config_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\site-config.js"

with open(site_config_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract SECUREVISION.insights section
insights_section_match = re.search(r'SECUREVISION\.insights\s*=\s*\[(.*?)\];', content, re.DOTALL)
if not insights_section_match:
    print("Could not find SECUREVISION.insights!")
    exit(1)

insights_section = insights_section_match.group(1)

# Each entry is on its own line (or spans multiple lines). Let's extract each object dictionary.
# Since the entries are structured as { ... }, we can find all matches of {...}
entries_raw = re.findall(r'\{([^}]+)\}', insights_section)

with_image = []
no_image = []

for entry in entries_raw:
    # Extract slug
    slug_match = re.search(r'slug:\s*["\']([^"\']+)["\']', entry)
    if not slug_match:
        continue
    slug = slug_match.group(1)
    
    # Extract image
    image_match = re.search(r'image:\s*["\']([^"\']+)["\']', entry)
    
    # Extract title
    title_match = re.search(r'title:\s*["\']([^"\']+)["\']', entry)
    title = title_match.group(1) if title_match else ""
    
    if image_match:
        image_filename = image_match.group(1)
        with_image.append((slug, image_filename))
    else:
        no_image.append((slug, title))

print("--- Entries WITH an image field ---")
for slug, image_filename in with_image:
    print(f"{slug} | {image_filename}")

print("\n--- Entries with NO image field ---")
for slug, title in no_image:
    print(f"{slug} | {title}")
