import os
import re

def fix_duplication(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    content = "".join(lines)
    header_marker = '<!-- ═══════════════════════════════════════════════════════════\n     ARTICLE HEADER'
    
    parts = content.split(header_marker)
    if len(parts) < 3:
        return # No duplication found
    
    # parts[0] = Head section
    # parts[1] = First header + first body + partial footer
    # parts[2] = Second header + full body + sidebar + footer
    
    # 1. Extract real links from parts[1]
    nav_card_pattern = re.compile(r'<a href="([^"]+)" class="nav-card">.*?<span>(.*?)</span>.*?<strong>(.*?)</strong>.*?</a>', re.DOTALL)
    real_links = nav_card_pattern.findall(parts[1])
    
    # 2. Extract tags if parts[1] has them and parts[2] doesn't
    # Actually, parts[2] usually has the template placeholders.
    
    # 3. Clean parts[2] - remove the extra CSS info at the bottom
    if '</html>' in parts[2]:
        parts[2] = parts[2].split('</html>')[0] + '</html>\n'

    # 4. Replace placeholders in parts[2] with real links from parts[1]
    new_parts2 = parts[2]
    placeholder_nav_pattern = re.compile(r'<nav class="prev-next-nav".*?</nav>', re.DOTALL)
    
    # Build the new nav block
    if real_links:
        new_nav = '<nav class="prev-next-nav" aria-label="Article navigation">\n'
        for i, (href, span, strong) in enumerate(real_links):
            style = ' style="text-align:right;"' if i == 1 else ''
            new_nav += f'          <a href="{href}" class="nav-card"{style}>\n'
            new_nav += f'            <span>{span}</span>\n'
            new_nav += f'            <strong>{strong}</strong>\n'
            new_nav += f'          </a>\n'
        new_nav += '        </nav>'
        new_parts2 = placeholder_nav_pattern.sub(new_nav, new_parts2)

    # 5. Assemble
    new_content = parts[0] + header_marker + new_parts2
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Fixed: {file_path}")

if __name__ == "__main__":
    # Test on one file
    fix_duplication(r"c:\Projects\SV-Build\insights\why-mechanical-locks-not-enough.html")
