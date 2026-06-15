import os
import re

insights_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\insights"
images_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\images\insights"

html_files = [f for f in os.listdir(insights_dir) if f.endswith('.html') and f not in ('index.html', 'portfolio-index.html')]

results = []
total_scanned = len(html_files)
total_references_checked = 0
unique_filenames_checked = set()

existing_images = set(os.listdir(images_dir))

for filename in html_files:
    slug = filename[:-5]
    filepath = os.path.join(insights_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    def check_and_add(match_url, tag_type):
        global total_references_checked
        if not match_url: return
        img_filename = match_url.split('/')[-1]
        if not img_filename: return
        
        total_references_checked += 1
        unique_filenames_checked.add(img_filename)
        
        if img_filename not in existing_images:
            results.append((slug, img_filename, tag_type))

    # Body images
    img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    for src in img_tags:
        if '/images/insights/' in src:
            check_and_add(src, 'body img')
            
    # OG / Twitter images
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
                
    # JSON-LD image
    json_images = re.findall(r'"image"\s*:\s*["\']([^"\']+)["\']', content, re.IGNORECASE)
    for src in json_images:
        if '/images/insights/' in src:
            check_and_add(src, 'json-ld')

if not results:
    print("✅ ALL CLEAR")
    print(f"Total HTML files scanned: {total_scanned}")
    print(f"Total image references checked: {total_references_checked}")
    print(f"Unique image filenames checked: {len(unique_filenames_checked)}")
    print("Broken references found: 0")
    print("All images present on disk.")
else:
    results.sort(key=lambda x: x[0])
    print("| article-slug | image-filename | tag-type |")
    print("|---|---|---|")
    for slug, img, t in results:
        print(f"| {slug} | {img} | {t} |")
    
    unique_missing = len(set([x[1] for x in results]))
    print(f"\nTotal broken references found: {len(results)}")
    print(f"Unique missing filenames: {unique_missing}")
