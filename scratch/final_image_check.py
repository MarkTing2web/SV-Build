import glob
import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

insights_dir = r"C:\Projects\SV-Build\insights"
images_dir = r"C:\Projects\SV-Build\images\insights"

# Find all html files except index.html
html_files = glob.glob(os.path.join(insights_dir, "*.html"))
html_files = [f for f in html_files if os.path.basename(f) != "index.html"]

issues = []
total_references_checked = 0

for html_path in sorted(html_files):
    slug = os.path.basename(html_path).replace(".html", "")
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all /images/insights/... references
    # 1. <img> tags
    img_refs = re.findall(r'src=["\']/images/insights/([^"\']+)["\']', content)
    
    # 2. meta og:image and twitter:image
    meta_refs = re.findall(r'content=["\'](?:https://www\.securevision\.com\.sg)?/images/insights/([^"\']+)["\']', content)
    
    # 3. JSON-LD image references
    json_ld_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    json_refs = []
    for block in json_ld_blocks:
        try:
            data = json.loads(block)
            if "image" in data:
                img_val = data["image"]
                if isinstance(img_val, str):
                    m = re.search(r'/images/insights/([^/]+)$', img_val)
                    if m:
                        json_refs.append(m.group(1))
                elif isinstance(img_val, list):
                    for val in img_val:
                        m = re.search(r'/images/insights/([^/]+)$', val)
                        if m:
                            json_refs.append(m.group(1))
        except Exception:
            pass

    # Combine all referenced files for this article
    referenced_files = set(img_refs + meta_refs + json_refs)
    total_references_checked += len(referenced_files)

    for filename in sorted(referenced_files):
        filename_clean = filename.split("?")[0]
        file_path = os.path.join(images_dir, filename_clean)
        if not os.path.exists(file_path):
            issues.append((slug, filename_clean, "MISSING"))
        elif os.path.getsize(file_path) == 0:
            issues.append((slug, filename_clean, "0 BYTES"))

missing_count = sum(1 for _, _, issue in issues if issue == "MISSING")
zerobyte_count = sum(1 for _, _, issue in issues if issue == "0 BYTES")

if not issues:
    print("✅ ALL CLEAR")
    print(f"Total files scanned: {len(html_files)}")
    print(f"Total image references checked: {total_references_checked}")
    print("Missing: 0")
    print("Zero-byte: 0")
else:
    print("| article-slug | filename | issue |")
    print("|---|---|---|")
    for slug, filename, issue in issues:
        print(f"| {slug} | {filename} | {issue} |")
