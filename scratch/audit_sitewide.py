import os
import re
import urllib.parse
import sys
import collections
from html.parser import HTMLParser

# Force UTF-8 output for Windows terminal
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

repo_root = r"c:\Projects\SV-Build"

class AuditHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = [] # list of (url, type, line_no)
        self.links = []  # list of (url, type, line_no)
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = {name.lower(): val for name, val in attrs}
        line_no = self.getpos()[0]
        
        # Check 1: Images
        if tag == 'img':
            if 'src' in attrs_dict:
                self.images.append((attrs_dict['src'], 'img_src', line_no))
            if 'data-src' in attrs_dict:
                self.images.append((attrs_dict['data-src'], 'data_src', line_no))
        elif tag == 'source':
            if 'srcset' in attrs_dict:
                self.images.append((attrs_dict['srcset'], 'source_srcset', line_no))
        elif tag == 'meta':
            prop = attrs_dict.get('property', '').lower() or attrs_dict.get('name', '').lower()
            if prop == 'og:image' and 'content' in attrs_dict:
                self.images.append((attrs_dict['content'], 'og_image', line_no))
            elif prop == 'og:url' and 'content' in attrs_dict:
                self.links.append((attrs_dict['content'], 'og_url', line_no))
        elif tag == 'link':
            rel = attrs_dict.get('rel', '').lower()
            if rel == 'canonical' and 'href' in attrs_dict:
                self.links.append((attrs_dict['href'], 'canonical', line_no))
        elif tag == 'a':
            if 'href' in attrs_dict:
                self.links.append((attrs_dict['href'], 'a_href', line_no))
                
        # data-src on any tag
        if 'data-src' in attrs_dict and tag != 'img':
            self.images.append((attrs_dict['data-src'], 'data_src', line_no))
            
        # background-image in inline style attribute
        if 'style' in attrs_dict:
            style_val = attrs_dict['style']
            bg_matches = re.findall(r'background-image\s*:\s*url\(\s*[\'"]?([^\'"\)]+)[\'"]?\s*\)', style_val, re.IGNORECASE)
            for url in bg_matches:
                self.images.append((url, 'bg_url', line_no))

def check_image(url, filepath):
    url_clean = url.strip()
    if not url_clean:
        return None, True
        
    # Check if external URL
    if url_clean.startswith('http://') or url_clean.startswith('https://'):
        is_internal = False
        for domain in ["https://www.securevision.com.sg", "http://www.securevision.com.sg", "https://securevision.com.sg", "http://securevision.com.sg"]:
            if url_clean.startswith(domain):
                url_clean = url_clean[len(domain):]
                is_internal = True
                break
        if not is_internal:
            return None, True # External URL, do not flag
            
    # Remove query/hash
    path = urllib.parse.urlparse(url_clean).path
    path = urllib.parse.unquote(path)
    if not path.strip():
        return None, True
        
    # Convert to root-relative path starting with /
    if path.startswith('/'):
        root_rel = path
    else:
        abs_path = os.path.normpath(os.path.join(os.path.dirname(filepath), path))
        rel_to_root = os.path.relpath(abs_path, repo_root)
        root_rel = '/' + rel_to_root.replace('\\', '/')
        
    # Ignore /images/ler-wee-meng-bio.webp
    if root_rel == "/images/ler-wee-meng-bio.webp":
        return None, True
        
    # Check physical existence
    abs_disk_path = os.path.normpath(os.path.join(repo_root, root_rel.lstrip('/')))
    exists = os.path.exists(abs_disk_path)
    return root_rel, exists

def check_link(url, filepath, is_a_href):
    # For a-href, only starting with / are checked
    if is_a_href and not url.startswith('/'):
        return None, True
        
    url_clean = url.strip()
    
    # Anchor-only links (#section) do not flag
    if url_clean.startswith('#'):
        return None, True
        
    # mailto:, tel:, https://wa.me/ do not flag
    if url_clean.startswith('mailto:') or url_clean.startswith('tel:') or url_clean.startswith('https://wa.me/'):
        return None, True
        
    # Check external URLs
    if url_clean.startswith('http://') or url_clean.startswith('https://'):
        is_internal = False
        for domain in ["https://www.securevision.com.sg", "http://www.securevision.com.sg", "https://securevision.com.sg", "http://securevision.com.sg"]:
            if url_clean.startswith(domain):
                url_clean = url_clean[len(domain):]
                is_internal = True
                break
        if not is_internal:
            return None, True # External URL, do not flag
            
    # Extract path from URL (removes query/hash)
    path = urllib.parse.urlparse(url_clean).path
    path = urllib.parse.unquote(path)
    if not path.strip():
        return None, True
        
    # Do NOT flag .css and .js asset files
    if path.lower().endswith(('.css', '.js')):
        return None, True
        
    # Convert to root-relative path starting with /
    if path.startswith('/'):
        root_rel = path
    else:
        abs_path = os.path.normpath(os.path.join(os.path.dirname(filepath), path))
        rel_to_root = os.path.relpath(abs_path, repo_root)
        root_rel = '/' + rel_to_root.replace('\\', '/')
        
    # Check physical existence
    path_to_check = root_rel.lstrip('/')
    abs_disk_path = os.path.normpath(os.path.join(repo_root, path_to_check))
    
    # If no file extension in the last segment
    last_segment = path_to_check.split('/')[-1]
    if not last_segment or '.' not in last_segment:
        # Check both path.html and path/index.html
        p1 = path_to_check.rstrip('/') + ".html"
        p2 = path_to_check if path_to_check.endswith('/') else path_to_check + '/'
        p2 = p2 + "index.html"
        
        abs_p1 = os.path.normpath(os.path.join(repo_root, p1.lstrip('/')))
        abs_p2 = os.path.normpath(os.path.join(repo_root, p2.lstrip('/')))
        
        exists = os.path.exists(abs_p1) or os.path.exists(abs_p2)
    else:
        exists = os.path.exists(abs_disk_path)
        
    return root_rel, exists

def main():
    html_files = []
    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in ('.git', '.vercel', 'node_modules')]
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.normpath(os.path.join(root, file)))
                
    html_files.sort()
    
    files_by_folder = collections.defaultdict(list)
    for f in html_files:
        dir_path = os.path.dirname(f)
        rel_dir = os.path.relpath(dir_path, repo_root)
        if rel_dir == '.':
            rel_dir = '/'
        else:
            rel_dir = '/' + rel_dir.replace('\\', '/')
        files_by_folder[rel_dir].append(f)
        
    sorted_folders = sorted(files_by_folder.keys())
    
    total_files = 0
    files_with_missing_images = 0
    files_with_broken_links = 0
    all_missing_images = set()
    all_broken_links = set()
    
    output_lines = []
    
    for folder in sorted_folders:
        output_lines.append(f"Folder: {folder}")
        for filepath in sorted(files_by_folder[folder]):
            total_files += 1
            rel_filepath = '/' + os.path.relpath(filepath, repo_root).replace('\\', '/')
            
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            except Exception as e:
                output_lines.append(f"{rel_filepath} — ERROR: Could not read file ({str(e)})")
                continue
                
            parser = AuditHTMLParser()
            try:
                parser.feed(content)
            except Exception as e:
                output_lines.append(f"{rel_filepath} — ERROR: Could not parse HTML ({str(e)})")
                continue
                
            file_missing_images = []
            file_broken_links = []
            
            for img_url, img_type, line_no in parser.images:
                if img_type == 'source_srcset':
                    for part in img_url.split(','):
                        part = part.strip()
                        if part:
                            single_url = part.split()[0]
                            root_rel, exists = check_image(single_url, filepath)
                            if not exists and root_rel:
                                file_missing_images.append(root_rel)
                                all_missing_images.add(root_rel)
                else:
                    root_rel, exists = check_image(img_url, filepath)
                    if not exists and root_rel:
                        file_missing_images.append(root_rel)
                        all_missing_images.add(root_rel)
                        
            for link_url, link_type, line_no in parser.links:
                is_a_href = (link_type == 'a_href')
                root_rel, exists = check_link(link_url, filepath, is_a_href)
                if not exists and root_rel:
                    file_broken_links.append(root_rel)
                    all_broken_links.add(root_rel)
                    
            file_missing_images = sorted(list(set(file_missing_images)))
            file_broken_links = sorted(list(set(file_broken_links)))
            
            if file_missing_images or file_broken_links:
                if file_missing_images:
                    files_with_missing_images += 1
                if file_broken_links:
                    files_with_broken_links += 1
                    
                for mi in file_missing_images:
                    output_lines.append(f"{rel_filepath} — MISSING IMAGE: {mi}")
                for bl in file_broken_links:
                    output_lines.append(f"{rel_filepath} — BROKEN LINK: {bl}")
            else:
                output_lines.append(f"{rel_filepath} — OK")
                
    # Gather all output lines to print and write to file
    out_filepath = os.path.join(repo_root, "scratch", "audit_results_final.txt")
    
    with open(out_filepath, 'w', encoding='utf-8') as outfile:
        def log_write(line=""):
            print(line)
            outfile.write(line + "\n")
            
        for line in output_lines:
            log_write(line)
            
        log_write()
        log_write("--- SUMMARY ---")
        log_write(f"Total files scanned: {total_files}")
        log_write(f"Total files with missing images: {files_with_missing_images}")
        log_write(f"Total files with broken links: {files_with_broken_links}")
        log_write(f"Total missing images (deduplicated): {len(all_missing_images)}")
        log_write(f"Total broken links (deduplicated): {len(all_broken_links)}")
        
        log_write("\nFull deduplicated list of all missing images:")
        for mi in sorted(all_missing_images):
            log_write(f"  {mi}")
            
        log_write("\nFull deduplicated list of all broken links:")
        for bl in sorted(all_broken_links):
            log_write(f"  {bl}")

if __name__ == "__main__":
    main()
