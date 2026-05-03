import os
import re

def fix_duplication(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    header_marker = '<!-- ═══════════════════════════════════════════════════════════\n     ARTICLE HEADER'
    
    parts = content.split(header_marker)
    if len(parts) < 3:
        return # No duplication found
    
    # Extract real links from the FIRST half
    nav_card_pattern = re.compile(r'<a href="([^"]+)" class="nav-card">.*?<span>(.*?)</span>.*?<strong>(.*?)</strong>.*?</a>', re.DOTALL)
    real_links = nav_card_pattern.findall(parts[1])
    
    # Extract tags from the FIRST half
    tags_pattern = re.compile(r'<div class="article-tags">(.*?)</div>', re.DOTALL)
    real_tags_match = tags_pattern.search(parts[1])
    
    # Clean parts[2] - remove extra info at bottom
    if '</html>' in parts[2]:
        parts[2] = parts[2].split('</html>')[0] + '</html>\n'

    # Fix navigation in parts[2]
    new_parts2 = parts[2]
    if real_links:
        placeholder_nav_pattern = re.compile(r'<nav class="prev-next-nav".*?</nav>', re.DOTALL)
        new_nav = '<nav class="prev-next-nav" aria-label="Article navigation">\n'
        for i, (href, span, strong) in enumerate(real_links):
            style = ' style="text-align:right;"' if i == 1 else ''
            new_nav += f'          <a href="{href}" class="nav-card"{style}>\n'
            new_nav += f'            <span>{span}</span>\n'
            new_nav += f'            <strong>{strong}</strong>\n'
            new_nav += f'          </a>\n'
        new_nav += '        </nav>'
        new_parts2 = placeholder_nav_pattern.sub(new_nav, new_parts2)

    # Fix tags in parts[2]
    if real_tags_match:
        real_tags = real_tags_match.group(1).strip()
        # Avoid placeholders like [Category]
        if '[Category]' not in real_tags:
            new_parts2 = tags_pattern.sub(f'<div class="article-tags">\n          {real_tags}\n        </div>', new_parts2)

    # Assemble
    new_content = parts[0] + header_marker + new_parts2
    
    # Final cleanup: remove sv-guides.css if it somehow persisted
    new_content = new_content.replace('<link rel="stylesheet" href="/sv-guides.css">', '')
    new_content = new_content.replace('  <link rel="stylesheet" href="/sv-guides.css">', '')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed duplication in: {file_path}")

if __name__ == "__main__":
    root_dir = r'c:\Projects\SV-Build'
    header_marker = '<!-- ═══════════════════════════════════════════════════════════\n     ARTICLE HEADER'
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                if content.count(header_marker) > 1:
                    fix_duplication(file_path)
