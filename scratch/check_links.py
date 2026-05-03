import os
import re
from pathlib import Path

def check_links(root_dir):
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    # Existing files for mapping
    all_files = set()
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), root_dir).replace('\\', '/')
            all_files.add('/' + rel_path)
            # Also add versions without .html for links that omit it (if any)
            if rel_path.endswith('.html'):
                all_files.add('/' + rel_path[:-5])
            # Add directory paths
            if file == 'index.html':
                all_files.add('/' + os.path.dirname(rel_path) + '/')
                if os.path.dirname(rel_path) == '':
                    all_files.add('/')

    broken_links = []
    link_pattern = re.compile(r'href=["\']([^"\']+)["\']')

    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            links = link_pattern.findall(content)
            
            rel_dir = os.path.dirname(os.path.relpath(html_file, root_dir)).replace('\\', '/')
            if rel_dir == '.':
                rel_dir = ''
            else:
                rel_dir = '/' + rel_dir

            for link in links:
                # Ignore external links, anchors, mailto, tel
                if link.startswith(('http', 'mailto:', 'tel:', '#', 'https:')):
                    continue
                
                # Normalize link
                if link.startswith('/'):
                    target = link
                else:
                    # Relative link
                    target = os.path.normpath(os.path.join(rel_dir, link)).replace('\\', '/')
                    if not target.startswith('/'):
                        target = '/' + target

                # Remove anchors or query params
                target = target.split('#')[0].split('?')[0]
                
                if target == '' or target == '/':
                    continue

                # Check if target exists
                if target not in all_files and target + '/' not in all_files and target + 'index.html' not in all_files:
                    broken_links.append({
                        'source': os.path.relpath(html_file, root_dir),
                        'link': link,
                        'normalized': target
                    })

    return broken_links

if __name__ == "__main__":
    root = r"c:\Projects\SV-Build"
    broken = check_links(root)
    if not broken:
        print("No broken internal links found.")
    else:
        print(f"Found {len(broken)} potentially broken internal links:")
        for b in broken:
            print(f"Source: {b['source']} -> Link: {b['link']}")
