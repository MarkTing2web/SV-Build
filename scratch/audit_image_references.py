import os
import re

insights_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\insights"
images_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights"
output_file = r"d:\Ler Wee Meng\Project-Web\SV-Build\insights-image-audit.md"

# Collect all HTML files directly in the insights folder
html_files = [f for f in os.listdir(insights_dir) if f.endswith('.html')]

# We must exclude portfolio-index.html if it exists.
html_files = [f for f in html_files if f != 'portfolio-index.html']

# To store all extracted image references
# format: (slug, filename, tag_type)
references = []

# Helper to extract filename from URL or path
def get_filename(path):
    # e.g., "https://www.securevision.com.sg/images/insights/video-verification-feature.webp"
    # or "/images/insights/video-verification-feature.webp"
    match = re.search(r'/images/insights/([^/\'"?\s>#]+)', path)
    if match:
        return match.group(1)
    return None

for filename in html_files:
    slug = filename[:-5]
    filepath = os.path.join(insights_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Parse body images: <img[^>]+src="..." ...>
    # We find all <img > tags
    img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
    for tag in img_tags:
        src_match = re.search(r'src=["\']([^"\']+)["\']', tag, re.IGNORECASE)
        if src_match:
            src = src_match.group(1)
            if '/images/insights/' in src:
                img_name = get_filename(src)
                if img_name:
                    # Let's verify this is a body image by ensuring it's in body and not head
                    # Actually, since <img src> is not standard in <head>, it's safe to assume it's body img.
                    references.append((slug, img_name, "body img"))
                    
    # 2. Parse og:image meta tags
    # <meta property="og:image" content="..." /> or similar
    meta_tags = re.findall(r'<meta[^>]+>', content, re.IGNORECASE)
    for tag in meta_tags:
        # Check if it's og:image
        is_og = re.search(r'property=["\']og:image["\']', tag, re.IGNORECASE)
        is_twitter = re.search(r'name=["\']twitter:image["\']', tag, re.IGNORECASE)
        
        content_match = re.search(r'content=["\']([^"\']+)["\']', tag, re.IGNORECASE)
        if content_match:
            val = content_match.group(1)
            if '/images/insights/' in val:
                img_name = get_filename(val)
                if img_name:
                    if is_og:
                        references.append((slug, img_name, "og:image"))
                    elif is_twitter:
                        references.append((slug, img_name, "twitter:image"))
                        
    # 3. Parse JSON-LD script tags
    # Find all <script type="application/ld+json">...</script>
    json_ld_scripts = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', content, re.IGNORECASE | re.DOTALL)
    for script_content in json_ld_scripts:
        # Let's find any strings in JSON-LD containing "/images/insights/"
        # Typically structured as "image": "URL" or "url": "URL" inside an image object
        # We can find all string values that contain "/images/insights/"
        string_matches = re.findall(r'["\']([^"\']*/images/insights/[^"\']+)["\']', script_content)
        for val in string_matches:
            img_name = get_filename(val)
            if img_name:
                references.append((slug, img_name, "json-ld"))

# Check file existence on disk
# Let's get list of files on disk in images/insights/
existing_images = set(os.listdir(images_dir))

audit_results = []
missing_body_images = []

for slug, img_name, tag_type in references:
    status = "OK" if img_name in existing_images else "MISSING"
    audit_results.append((slug, img_name, tag_type, status))
    if status == "MISSING" and tag_type == "body img":
        missing_body_images.append((slug, img_name))

# Sort: MISSING first, then OK. Within MISSING, sort alphabetically by article slug.
# Also, within same slug, let's sort by tag_type.
# Let's define a custom sort key: (status != "MISSING", slug, tag_type, img_name)
def sort_key(item):
    slug, img_name, tag_type, status = item
    return (0 if status == "MISSING" else 1, slug, tag_type, img_name)

sorted_results = sorted(audit_results, key=sort_key)

# Unique counts
all_referenced_files = set(img_name for _, img_name, _, _ in audit_results)
unique_missing = set(img_name for _, img_name, _, status in audit_results if status == "MISSING")
unique_ok = set(img_name for _, img_name, _, status in audit_results if status == "OK")

# Build Markdown output
md = []
md.append("# Insights Image Audit Report\n")
md.append("## Image Reference Audit Details\n")
md.append("| Article slug | Image filename | Tag type | Status |")
md.append("|---|---|---|---|")
for slug, img_name, tag_type, status in sorted_results:
    status_label = f"**{status}**" if status == "MISSING" else status
    md.append(f"| {slug} | {img_name} | {tag_type} | {status_label} |")

md.append("\n## Summary Counts\n")
md.append(f"- **Total image references scanned:** {len(audit_results)}")
md.append(f"- **Total unique image files referenced:** {len(all_referenced_files)}")
md.append(f"- **Total unique image files MISSING:** {len(unique_missing)}")
md.append(f"- **Total unique image files OK:** {len(unique_ok)}\n")

md.append("## Missing Body Images Only\n")
md.append("Below are the articles missing a body `<img>` tag (where the referenced image does not exist on disk):\n")

if missing_body_images:
    # Sort missing body images by slug
    missing_body_images = sorted(list(set(missing_body_images))) # unique pairs
    md.append("| Article slug | Missing body image filename |")
    md.append("|---|---|")
    for slug, img_name in missing_body_images:
        md.append(f"| {slug} | {img_name} |")
else:
    md.append("No missing body images found! All body image files exist on disk. ✅")

# Write to file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

# Print summary for chat
print(f"Total image references scanned: {len(audit_results)}")
print(f"Total unique image files referenced: {len(all_referenced_files)}")
print(f"Total unique image files MISSING: {len(unique_missing)}")
print(f"Total unique image files OK: {len(unique_ok)}")
print(f"Missing body image file list size: {len(missing_body_images)}")
