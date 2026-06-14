import os
import re
import glob

insight_dir = r"C:\Projects\SV-Build\insights"

def process_files():
    report = []
    
    for filepath in glob.glob(os.path.join(insight_dir, "*.html")):
        filename = os.path.basename(filepath)
        if filename == "index.html":
            continue
            
        slug = filename[:-5]
        expected_og = f"https://www.securevision.com.sg/images/insights/{slug}-feature.webp"
        expected_src = f"/images/insights/{slug}-feature.webp"
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        og_status = "MISSING"
        tw_status = "MISSING"
        body_status = "MISSING"
        
        # 1. og:image
        og_img_match = re.search(r'<meta[^>]*?property="og:image"[^>]*?>|<meta[^>]*?property="og:image"\s*/>', content)
        if not og_img_match:
            og_img_match = re.search(r'<meta[^>]*?property=[\'"]og:image[\'"][^>]*?>', content)
            
        if og_img_match:
            tag = og_img_match.group(0)
            current_content = re.search(r'content="([^"]*)"', tag)
            if current_content:
                if current_content.group(1) == expected_og:
                    og_status = "OK"
                else:
                    new_tag = re.sub(r'content="[^"]*"', f'content="{expected_og}"', tag)
                    content = content[:og_img_match.start()] + new_tag + content[og_img_match.end():]
                    og_status = "FIXED"
            else:
                og_status = "MISSING"
        
        # Fix width and height
        # Need to search again because string might have changed length
        og_width_match = re.search(r'<meta[^>]*?property="og:image:width"[^>]*?>', content)
        if og_width_match:
            tag = og_width_match.group(0)
            current_content = re.search(r'content="([^"]*)"', tag)
            if current_content and current_content.group(1) != "1200":
                new_tag = re.sub(r'content="[^"]*"', 'content="1200"', tag)
                content = content[:og_width_match.start()] + new_tag + content[og_width_match.end():]
                if og_status == "OK": og_status = "FIXED"

        og_height_match = re.search(r'<meta[^>]*?property="og:image:height"[^>]*?>', content)
        if og_height_match:
            tag = og_height_match.group(0)
            current_content = re.search(r'content="([^"]*)"', tag)
            if current_content and current_content.group(1) != "630":
                new_tag = re.sub(r'content="[^"]*"', 'content="630"', tag)
                content = content[:og_height_match.start()] + new_tag + content[og_height_match.end():]
                if og_status == "OK": og_status = "FIXED"

        # 2. twitter:image
        tw_img_match = re.search(r'<meta[^>]*?name="twitter:image"[^>]*?>', content)
        if tw_img_match:
            tag = tw_img_match.group(0)
            current_content = re.search(r'content="([^"]*)"', tag)
            if current_content:
                if current_content.group(1) == expected_og:
                    tw_status = "OK"
                else:
                    new_tag = re.sub(r'content="[^"]*"', f'content="{expected_og}"', tag)
                    content = content[:tw_img_match.start()] + new_tag + content[tw_img_match.end():]
                    tw_status = "FIXED"
        
        # 3. body image
        body_img_matches = list(re.finditer(r'<img[^>]+>', content))
        for match in body_img_matches:
            tag = match.group(0)
            if 'article-img-float-right' in tag and '/images/insights/' in tag:
                current_src = re.search(r'src="([^"]*)"', tag)
                if current_src:
                    if current_src.group(1) == expected_src:
                        body_status = "OK"
                    else:
                        new_tag = re.sub(r'src="[^"]*"', f'src="{expected_src}"', tag)
                        content = content[:match.start()] + new_tag + content[match.end():]
                        body_status = "FIXED"
                break
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        report.append({
            "file": filename,
            "og": og_status,
            "tw": tw_status,
            "body": body_status
        })

    # Output report
    print("| File | og:image status | twitter:image status | Body img status |")
    print("|------|----------------|---------------------|-----------------|")
    for r in report:
        print(f"| {r['file']} | {r['og']} | {r['tw']} | {r['body']} |")
        
    total = len(report)
    fixed = sum(1 for r in report if r['og'] == 'FIXED' or r['tw'] == 'FIXED' or r['body'] == 'FIXED')
    missing = sum(1 for r in report if r['og'] == 'MISSING' or r['tw'] == 'MISSING' or r['body'] == 'MISSING')
    
    print(f"\nTotal files checked: {total}")
    print(f"Files with fixes applied: {fixed}")
    print(f"Files with MISSING tags: {missing}")

if __name__ == "__main__":
    process_files()
