import os
import re
from bs4 import BeautifulSoup

repo_root = r"c:\Projects\SV-Build"
solutions_dir = os.path.join(repo_root, "solutions")

solutions_html_files = []
for root, dirs, files in os.walk(solutions_dir):
    for f in files:
        if f.lower().endswith('.html'):
            solutions_html_files.append(os.path.join(root, f))
solutions_html_files.sort()

url_pattern = re.compile(r'url\(\s*[\'"]?([^\'")\s]+)[\'"]?\s*\)', re.IGNORECASE)

for filepath in solutions_html_files:
    rel_path = os.path.relpath(filepath, repo_root).replace('\\', '/')
    print(f"=== {rel_path} ===")
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Style tags
    for style in soup.find_all('style'):
        matches = url_pattern.findall(style.string or '')
        if matches:
            print("  Style tags urls:", matches)
            
    # Header inline style
    for header in soup.find_all('header'):
        style_attr = header.get('style') or ''
        matches = url_pattern.findall(style_attr)
        if matches:
            print("  Header style urls:", matches)
            
    # og:image
    for meta in soup.find_all('meta', property='og:image'):
        print("  og:image:", meta.get('content'))
    for meta in soup.find_all('meta', attrs={"name": "og:image"}):
        print("  og:image (name):", meta.get('content'))
        
    # Any other image references with 'hero' or '-mobile' or '-rel' in text
    all_refs = re.findall(r'[\w\-./]+\.(?:webp|png|jpg|jpeg)', content, re.IGNORECASE)
    hero_refs = [r for r in all_refs if 'hero' in r.lower() or 'mobile' in r.lower() or 'rel' in r.lower()]
    if hero_refs:
        print("  Other hero/mobile/rel refs:", sorted(list(set(hero_refs))))
    print()
