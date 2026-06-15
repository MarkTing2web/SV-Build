import os
import re
import html

insights_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\insights"
output_file = r"d:\Ler Wee Meng\Project-Web\SV-Build\insights-html-audit.md"

# List all HTML files directly in the insights folder
html_files = [f for f in os.listdir(insights_dir) if f.endswith('.html')]

# Exclude index.html and portfolio-index.html
html_files = [f for f in html_files if f not in ('index.html', 'portfolio-index.html')]

results = []

missing_category_count = 0
missing_date_count = 0
no_image_count = 0

for filename in html_files:
    slug = filename[:-5]
    filepath = os.path.join(insights_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Extract title
    title = "MISSING"
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    if title_match:
        raw_title = title_match.group(1).strip()
        # Clean up any suffix containing Securevision
        # e.g., "How to Design a Burglar Alarm System | Securevision Insights" or " | Securevision"
        cleaned_title = re.sub(r'\s*\|\s*Securevision.*$', '', raw_title, flags=re.IGNORECASE).strip()
        title = html.unescape(cleaned_title)
        
    # 2. Extract category from <span class="insights-cat-label">
    category = "MISSING"
    cat_match = re.search(r'<span[^>]+class=["\']insights-cat-label["\'][^>]*>(.*?)</span>', content, re.IGNORECASE | re.DOTALL)
    if cat_match:
        category = html.unescape(cat_match.group(1).strip())
    else:
        # Check if the class is different or order of attributes is different
        cat_match_alt = re.search(r'<span[^>]+insights-cat-label[^>]*>(.*?)</span>', content, re.IGNORECASE | re.DOTALL)
        if cat_match_alt:
            category = html.unescape(cat_match_alt.group(1).strip())
            
    if category == "MISSING":
        missing_category_count += 1
        
    # 3. Extract date from <meta content="..." property="article:published_time" />
    # Could be property first or content first
    date = "MISSING"
    meta_tags = re.findall(r'<meta[^>]+>', content, re.IGNORECASE)
    for tag in meta_tags:
        is_pub_time = re.search(r'property=["\']article:published_time["\']', tag, re.IGNORECASE) or re.search(r'name=["\']article:published_time["\']', tag, re.IGNORECASE)
        if is_pub_time:
            content_match = re.search(r'content=["\']([^"\']+)["\']', tag, re.IGNORECASE)
            if content_match:
                date = content_match.group(1).strip()
                break
                
    if date == "MISSING":
        missing_date_count += 1
        
    # 4. Extract feature image: the src of the FIRST <img class="article-img-float-right"> tag
    # The class might be in any order, so look for <img> tags that contain class="article-img-float-right"
    feature_image = "NO-IMAGE"
    img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
    for tag in img_tags:
        # Check if class contains article-img-float-right
        class_match = re.search(r'class=["\']([^"\']+)["\']', tag, re.IGNORECASE)
        if class_match:
            classes = class_match.group(1).split()
            if 'article-img-float-right' in classes:
                src_match = re.search(r'src=["\']([^"\']+)["\']', tag, re.IGNORECASE)
                if src_match:
                    src = src_match.group(1)
                    # Strip the /images/insights/ prefix
                    feature_image = src.replace('/images/insights/', '').replace('../images/insights/', '')
                    break
                    
    if feature_image == "NO-IMAGE":
        no_image_count += 1
        
    results.append((slug, title, category, date, feature_image))

# Sort alphabetically by slug
results.sort(key=lambda x: x[0])

# Generate Markdown table
md = []
md.append("# Insights HTML Audit\n")
md.append("| slug | title | category | date | image |")
md.append("|---|---|---|---|---|")
for slug, title, category, date, feature_image in results:
    md.append(f"| {slug} | {title} | {category} | {date} | {feature_image} |")

md.append("\n## Summary\n")
md.append(f"- **Total HTML files scanned:** {len(results)}")
md.append(f"- **Files with MISSING category:** {missing_category_count}")
md.append(f"- **Files with MISSING date:** {missing_date_count}")
md.append(f"- **Files with NO-IMAGE:** {no_image_count}")

# Write to file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

# Print summary
print(f"Total HTML files scanned: {len(results)}")
print(f"Files with MISSING category: {missing_category_count}")
print(f"Files with MISSING date: {missing_date_count}")
print(f"Files with NO-IMAGE: {no_image_count}")
