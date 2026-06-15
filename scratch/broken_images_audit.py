import os
import re

insights_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\insights"
images_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights"
output_file = r"d:\Ler Wee Meng\Project-Web\SV-Build\broken-images-audit-2.md"

html_files = [f for f in os.listdir(insights_dir) if f.endswith('.html') and f not in ('index.html', 'portfolio-index.html')]

results = []
total_scanned = len(html_files)

# Pre-fetch existing images for fast lookup
existing_images = set(os.listdir(images_dir))

for filename in html_files:
    slug = filename[:-5]
    filepath = os.path.join(insights_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    def check_and_add(match_url, tag_type):
        if not match_url: return
        # Extract filename only
        img_filename = match_url.split('/')[-1]
        if img_filename and img_filename not in existing_images:
            results.append((slug, img_filename, tag_type))

    # 1. Body images: <img src="...">
    img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    for src in img_tags:
        if '/images/insights/' in src:
            check_and_add(src, 'body img')
            
    # 2. OG / Twitter image:
    meta_tags = re.findall(r'<meta[^>]+>', content, re.IGNORECASE)
    for tag in meta_tags:
        if re.search(r'property=["\']og:image["\']', tag, re.IGNORECASE):
            content_match = re.search(r'content=["\']([^"\']+)["\']', tag, re.IGNORECASE)
            if content_match and '/images/insights/' in content_match.group(1):
                check_and_add(content_match.group(1), 'og:image')
                
        if re.search(r'name=["\']twitter:image["\']', tag, re.IGNORECASE) or re.search(r'property=["\']twitter:image["\']', tag, re.IGNORECASE):
            content_match = re.search(r'content=["\']([^"\']+)["\']', tag, re.IGNORECASE)
            if content_match and '/images/insights/' in content_match.group(1):
                check_and_add(content_match.group(1), 'twitter:image')
                
    # 4. JSON-LD "image": "..."
    json_images = re.findall(r'"image"\s*:\s*["\']([^"\']+)["\']', content, re.IGNORECASE)
    for src in json_images:
        if '/images/insights/' in src:
            check_and_add(src, 'json-ld')

# Sort by slug
results.sort(key=lambda x: x[0])

# Generate output
md = []
md.append("# Broken Images Audit 2\n")
md.append("| article-slug | image-filename | tag-type |")
md.append("|---|---|---|")
for slug, img_filename, tag_type in results:
    md.append(f"| {slug} | {img_filename} | {tag_type} |")
    
md.append("\n## Summary")
md.append(f"- Total HTML files scanned: {total_scanned}")
md.append(f"- Total broken image references found: {len(results)}")

unique_missing_files = sorted(list(set([x[1] for x in results])))
md.append(f"- Total unique missing filenames: {len(unique_missing_files)}")

md.append("\n## Unique Missing Filenames")
for f in unique_missing_files:
    md.append(f"- {f}")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

print(f"Total HTML files scanned: {total_scanned}")
print(f"Total broken image references found: {len(results)}")
print(f"Total unique missing filenames: {len(unique_missing_files)}")
print("Unique Missing Filenames:")
for f in unique_missing_files:
    print(f"- {f}")
