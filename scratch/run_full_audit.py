import os
import re
from bs4 import BeautifulSoup

repo_root = r"c:\Projects\SV-Build"
solutions_dir = os.path.join(repo_root, "solutions")

excluded_images = {
    "/images/ler-wee-meng-bio.webp",
    "/images/portfolio/portfolio-light-cairnhill.webp",
    "/images/portfolio/portfolio-industrial.png"
}

# Regex for CSS url() inline styles
css_url_pattern = re.compile(r'url\(\s*[\'"]?([^\'")\s]+)[\'"]?\s*\)', re.IGNORECASE)

scanned_count = 0
files_with_missing_images = 0
files_with_broken_links = 0

all_missing_images = set()
all_broken_links = set()

# Track results per file
file_results = []

def clean_path(ref):
    # Remove query parameters and hash anchors
    return ref.split('?')[0].split('#')[0].strip().strip("'\"")

def is_external(ref):
    ref_lower = ref.lower()
    return (ref_lower.startswith('http://') or 
            ref_lower.startswith('https://') or 
            ref_lower.startswith('//') or 
            ref_lower.startswith('mailto:') or 
            ref_lower.startswith('tel:') or 
            'wa.me' in ref_lower)

def check_image_exists(img_ref, current_file_dir):
    if not img_ref or is_external(img_ref):
        return True, None
        
    cleaned = clean_path(img_ref)
    if not cleaned:
        return True, None
        
    # Check exclusion list
    # Normalize to start with / for checking exclusion
    norm_path = cleaned
    if not norm_path.startswith('/'):
        # Resolve to root-relative path
        abs_p = os.path.normpath(os.path.join(current_file_dir, norm_path))
        norm_path = '/' + os.path.relpath(abs_p, repo_root).replace('\\', '/')
        
    if norm_path in excluded_images:
        return True, None
        
    # Resolve disk path
    if cleaned.startswith('/'):
        disk_path = os.path.join(repo_root, cleaned.lstrip('/'))
    else:
        disk_path = os.path.normpath(os.path.join(current_file_dir, cleaned))
        
    exists = os.path.isfile(disk_path)
    report_path = '/' + os.path.relpath(disk_path, repo_root).replace('\\', '/')
    return exists, report_path

def check_link_exists(link_ref):
    if not link_ref:
        return True, None
        
    # Strip domain prefix if it exists
    domain = "https://www.securevision.com.sg"
    if link_ref.startswith(domain):
        link_ref = link_ref[len(domain):]
        
    if is_external(link_ref) or link_ref.startswith('#'):
        return True, None
        
    cleaned = clean_path(link_ref)
    if not cleaned:
        return True, None
        
    # Check if it's css/js
    cleaned_lower = cleaned.lower()
    if cleaned_lower.endswith('.css') or cleaned_lower.endswith('.js'):
        return True, None
        
    # Resolve disk path
    if cleaned.startswith('/'):
        path_to_check = cleaned.lstrip('/')
    else:
        # If it doesn't start with /, we don't flag in Check 2 for <a> tags
        # but for canonical/og:url we stripped domain, so it will start with /
        # If it doesn't start with /, return True
        return True, None
        
    # Handle empty/index directory paths
    if not path_to_check or path_to_check == '/':
        disk_path = os.path.join(repo_root, 'index.html')
    elif path_to_check.endswith('/'):
        disk_path = os.path.join(repo_root, path_to_check + 'index.html')
    else:
        disk_path = os.path.join(repo_root, path_to_check)
        
    # Check existence
    if os.path.isfile(disk_path):
        return True, None
    elif os.path.isdir(disk_path):
        # check for index.html in the directory
        if os.path.isfile(os.path.join(disk_path, 'index.html')):
            return True, None
            
    # Check if adding .html helps (clean URLs)
    if not disk_path.endswith('.html'):
        disk_path_html = disk_path + '.html'
        if os.path.isfile(disk_path_html):
            return True, None
            
    report_path = '/' + path_to_check
    return False, report_path

# Traverse solutions directory
for root, dirs, files in os.walk(solutions_dir):
    # Sort files and directories for consistent/alphabetical order
    dirs.sort()
    files.sort()
    
    for file in files:
        if not file.endswith('.html'):
            continue
            
        scanned_count += 1
        filepath = os.path.join(root, file)
        current_file_dir = os.path.dirname(filepath)
        rel_filepath = os.path.relpath(filepath, repo_root).replace('\\', '/')
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
            
        soup = BeautifulSoup(html_content, 'html.parser')
        
        missing_images = []
        broken_links = []
        
        # --- Check 1: Image References ---
        # 1. img src
        for img in soup.find_all('img'):
            src = img.get('src')
            exists, path = check_image_exists(src, current_file_dir)
            if not exists and path:
                missing_images.append(path)
                all_missing_images.add(path)
                
        # 2. source srcset
        for source in soup.find_all('source'):
            srcset = source.get('srcset')
            if srcset:
                parts = [p.strip().split()[0] for p in srcset.split(',') if p.strip()]
                for p in parts:
                    exists, path = check_image_exists(p, current_file_dir)
                    if not exists and path:
                        missing_images.append(path)
                        all_missing_images.add(path)
                        
        # 3. CSS inline styles
        for tag in soup.find_all(style=True):
            style = tag.get('style')
            urls = css_url_pattern.findall(style)
            for u in urls:
                exists, path = check_image_exists(u, current_file_dir)
                if not exists and path:
                    missing_images.append(path)
                    all_missing_images.add(path)
                    
        # 4. og:image
        for meta in soup.find_all('meta'):
            prop = meta.get('property', '') or meta.get('name', '')
            if prop.lower() == 'og:image':
                content = meta.get('content')
                exists, path = check_image_exists(content, current_file_dir)
                if not exists and path:
                    missing_images.append(path)
                    all_missing_images.add(path)
                    
        # 5. data-src
        for tag in soup.find_all(attrs={"data-src": True}):
            data_src = tag.get('data-src')
            exists, path = check_image_exists(data_src, current_file_dir)
            if not exists and path:
                missing_images.append(path)
                all_missing_images.add(path)
                
        # --- Check 2: Internal Links ---
        # 1. a href starting with /
        for a in soup.find_all('a'):
            href = a.get('href')
            if href and href.startswith('/'):
                exists, path = check_link_exists(href)
                if not exists and path:
                    broken_links.append(path)
                    all_broken_links.add(path)
                    
        # 2. link rel="canonical"
        for link in soup.find_all('link', rel='canonical'):
            href = link.get('href')
            exists, path = check_link_exists(href)
            if not exists and path:
                broken_links.append(path)
                all_broken_links.add(path)
                
        # 3. og:url
        for meta in soup.find_all('meta'):
            prop = meta.get('property', '') or meta.get('name', '')
            if prop.lower() == 'og:url':
                content = meta.get('content')
                exists, path = check_link_exists(content)
                if not exists and path:
                    broken_links.append(path)
                    all_broken_links.add(path)
                    
        # Deduplicate per file
        missing_images = sorted(list(set(missing_images)))
        broken_links = sorted(list(set(broken_links)))
        
        file_results.append({
            "rel_path": rel_filepath,
            "missing_images": missing_images,
            "broken_links": broken_links
        })
        
        if missing_images:
            files_with_missing_images += 1
        if broken_links:
            files_with_broken_links += 1

# Output results in requested format
for res in file_results:
    fn = res["rel_path"]
    has_issues = False
    
    if res["missing_images"]:
        has_issues = True
        for p in res["missing_images"]:
            print(f"{fn} — MISSING IMAGE: {p}")
            
    if res["broken_links"]:
        has_issues = True
        for p in res["broken_links"]:
            print(f"{fn} — BROKEN LINK: {p}")
            
    if not has_issues:
        print(f"{fn} — OK")

print("\n" + "="*50)
print(f"Total files scanned: {scanned_count}")
print(f"Files with missing images: {files_with_missing_images}")
print(f"Files with broken links: {files_with_broken_links}")
print("All missing images (deduplicated):")
for p in sorted(list(all_missing_images)):
    print(f"  - {p}")
print("All broken links (deduplicated):")
for p in sorted(list(all_broken_links)):
    print(f"  - {p}")
