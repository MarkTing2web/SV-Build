import os
import re
import urllib.parse

repo_root = r"c:\Projects\SV-Build"
resources_dir = os.path.join(repo_root, "resources")

# Find all HTML files in resources/ and all its subfolders
html_files = []
for root, dirs, files in os.walk(resources_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.normpath(os.path.join(root, f)))

# Sort alphabetically to keep output deterministic
html_files = sorted(html_files)

# Regex patterns
re_img_src = re.compile(r'<img\s+[^>]*src\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
re_source_srcset = re.compile(r'<source\s+[^>]*srcset\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
re_bg_url = re.compile(r'background-image\s*:\s*url\(\s*[\'"]?([^\'"\)]+)[\'"]?\s*\)', re.IGNORECASE)
re_og_image = re.compile(r'<meta\s+[^>]*(?:property|name)\s*=\s*["\']og:image["\']\s+[^>]*content\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
re_og_image_rev = re.compile(r'<meta\s+[^>]*content\s*=\s*["\']([^"\']+)["\']\s+[^>]*(?:property|name)\s*=\s*["\']og:image["\']', re.IGNORECASE)

re_a_href = re.compile(r'<a\s+[^>]*href\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
re_canonical = re.compile(r'<link\s+[^>]*rel\s*=\s*["\']canonical["\']\s+[^>]*href\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
re_canonical_rev = re.compile(r'<link\s+[^>]*href\s*=\s*["\']([^"\']+)["\']\s+[^>]*rel\s*=\s*["\']canonical["\']', re.IGNORECASE)

# Ignored images
ignored_images = {
    '/images/ler-wee-meng-bio.webp',
    '/images/og-default.jpg'
}

def to_root_relative_path(url, filepath):
    # Determine the root-relative path (starting with /)
    if url.startswith('http://') or url.startswith('https://'):
        parsed = urllib.parse.urlparse(url)
        if 'securevision.com.sg' in parsed.netloc:
            path = parsed.path
        else:
            return url # External URL
    else:
        path = urllib.parse.urlparse(url).path
        
    path = urllib.parse.unquote(path)
    if not path:
        return ''
        
    if path.startswith('/'):
        return path
    else:
        # Resolve relative to the HTML file's folder, then convert to root-relative
        rel_to_root = os.path.relpath(os.path.join(os.path.dirname(filepath), path), repo_root)
        normalized = '/' + rel_to_root.replace('\\', '/')
        return normalized

# Image checker
def check_image_exists(url, filepath):
    if url.startswith('http://') or url.startswith('https://'):
        parsed = urllib.parse.urlparse(url)
        if 'securevision.com.sg' in parsed.netloc:
            path = parsed.path
        else:
            return True # Do not flag external URLs
    else:
        path = urllib.parse.urlparse(url).path
        
    path = urllib.parse.unquote(path)
    if not path:
        return True # Skip empty
        
    # Check if ignored
    match_path = path if path.startswith('/') else '/' + path
    if match_path in ignored_images:
        return True
        
    if path.startswith('/'):
        abs_path = os.path.normpath(os.path.join(repo_root, path.lstrip('/')))
    else:
        abs_path = os.path.normpath(os.path.join(os.path.dirname(filepath), path))
        
    return os.path.exists(abs_path)

# Link checker
def check_link_exists(url, filepath):
    if url.startswith('http://') or url.startswith('https://'):
        parsed = urllib.parse.urlparse(url)
        if 'securevision.com.sg' in parsed.netloc:
            path = parsed.path
        else:
            return True # Do not flag external URLs
    else:
        if not url.startswith('/'):
            return True # Do not flag other links
        path = urllib.parse.urlparse(url).path
        
    path = urllib.parse.unquote(path)
    if not path:
        return True # Empty, don't flag
        
    if path.lower().endswith(('.css', '.js')):
        return True
        
    last_segment = path.split('/')[-1]
    if not last_segment or '.' not in last_segment:
        p1 = path.rstrip('/') + ".html"
        p2 = path if path.endswith('/') else path + '/'
        p2 = p2 + "index.html"
        
        abs_p1 = os.path.normpath(os.path.join(repo_root, p1.lstrip('/')))
        abs_p2 = os.path.normpath(os.path.join(repo_root, p2.lstrip('/')))
        
        return os.path.exists(abs_p1) or os.path.exists(abs_p2)
    else:
        abs_path = os.path.normpath(os.path.join(repo_root, path.lstrip('/')))
        return os.path.exists(abs_path)

total_files = len(html_files)
files_with_missing_images = set()
files_with_broken_links = set()
all_missing_images = set()
all_broken_links = set()

output_lines = []

for filepath in html_files:
    # Get filename relative to repo root starting with /
    rel_filename = '/' + os.path.relpath(filepath, repo_root).replace('\\', '/')
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Extract images
    images = []
    # 1. img src
    for m in re_img_src.finditer(content):
        images.append(m.group(1))
    # 2. source srcset
    for m in re_source_srcset.finditer(content):
        srcset = m.group(1)
        for part in srcset.split(','):
            part = part.strip()
            if part:
                img_url = part.split()[0]
                images.append(img_url)
    # 3. CSS background-image url
    for m in re_bg_url.finditer(content):
        images.append(m.group(1))
    # 4. og:image
    for m in re_og_image.finditer(content):
        images.append(m.group(1))
    for m in re_og_image_rev.finditer(content):
        images.append(m.group(1))
        
    # Extract links
    links = []
    # 1. a href
    for m in re_a_href.finditer(content):
        href = m.group(1).strip()
        links.append(href)
    # 2. link rel="canonical"
    for m in re_canonical.finditer(content):
        links.append(m.group(1).strip())
    for m in re_canonical_rev.finditer(content):
        links.append(m.group(1).strip())
        
    # Filter links for Check 2
    filtered_links = []
    for l in links:
        # Internal links starting with / OR link rel="canonical"
        is_canonical = False
        # We need to recognize canonical link. Let's see if the link tag rel="canonical" matched it.
        # Since we collected all links together, let's check which ones are internal:
        # - Starts with '/'
        # - Starts with http/https but belongs to our domain (representing canonical or full domain links)
        if l.startswith('http://') or l.startswith('https://'):
            parsed = urllib.parse.urlparse(l)
            if 'securevision.com.sg' in parsed.netloc:
                if not l.startswith('https://wa.me/'):
                    filtered_links.append(l)
        elif l.startswith('/'):
            filtered_links.append(l)
            
    # Check images
    missing_imgs_in_file = []
    for img in images:
        if not check_image_exists(img, filepath):
            root_rel = to_root_relative_path(img, filepath)
            missing_imgs_in_file.append(root_rel)
            all_missing_images.add(root_rel)
            
    # Check links
    broken_links_in_file = []
    for l in filtered_links:
        if not check_link_exists(l, filepath):
            root_rel = to_root_relative_path(l, filepath)
            broken_links_in_file.append(root_rel)
            all_broken_links.add(root_rel)
            
    # Remove duplicates from the file list to prevent double reporting
    # but preserve order if possible or just sort
    missing_imgs_in_file = sorted(list(set(missing_imgs_in_file)))
    broken_links_in_file = sorted(list(set(broken_links_in_file)))
    
    if missing_imgs_in_file or broken_links_in_file:
        if missing_imgs_in_file:
            files_with_missing_images.add(rel_filename)
        if broken_links_in_file:
            files_with_broken_links.add(rel_filename)
            
        for mi in missing_imgs_in_file:
            output_lines.append(f"{rel_filename} — MISSING IMAGE: {mi}")
        for bl in broken_links_in_file:
            output_lines.append(f"{rel_filename} — BROKEN LINK: {bl}")
    else:
        output_lines.append(f"{rel_filename} — OK")

# Output the file results
for line in output_lines:
    print(line)

print()
print("Total files scanned:", total_files)
print("Files with missing images:", len(files_with_missing_images))
print("Files with broken links:", len(files_with_broken_links))
print("All missing images (deduplicated):")
for mi in sorted(all_missing_images):
    print(f"  {mi}")
print("All broken links (deduplicated):")
for bl in sorted(all_broken_links):
    print(f"  {bl}")
