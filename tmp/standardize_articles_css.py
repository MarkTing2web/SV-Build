import os
import re

directory = r'c:\Users\ler\OneDrive - Securevision Pte Ltd\1 SV Build'
pattern = re.compile(r'insights-.*\.html')

# List of CSS selectors to remove (as they are now global)
selectors_to_remove = [
    r'\.article-body\s*\{[^}]*\}',
    r'\.prose\s+h2\s*\{[^}]*\}',
    r'\.prose\s+h3\s*\{[^}]*\}',
    r'\.prose\s+p\s*\{[^}]*\}',
    r'\.prose\s+ul,\s*\.prose\s+ol\s*\{[^}]*\}',
    r'\.prose\s+li\s*\{[^}]*\}',
    r'\.callout-box\s*\{[^}]*\}',
    r'\.callout-box\s+strong\s*\{[^}]*\}',
    r'\.callout-box\s+p\s*\{[^}]*\}',
    r'\.verdict-box\s*\{[^}]*\}',
    r'\.verdict-box\s+p\s*\{[^}]*\}',
    r'\.article-image-box\s*\{[^}]*\}',
    r'\.article-image-box\s+img\s*\{[^}]*\}',
    r'\.image-caption\s*\{[^}]*\}'
]

# Specifically target the article-body padding in media queries as well
media_query_article_body = r'\.article-body\s*\{\s*padding:\s*40px\s*0;\s*\}'

def cleanup_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the style block
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not style_match:
        return False

    style_content = style_match.group(1)
    new_style_content = style_content

    for selector in selectors_to_remove:
        new_style_content = re.sub(selector, '', new_style_content)
    
    new_style_content = re.sub(media_query_article_body, '', new_style_content)

    # Clean up excess whitespace and empty lines
    new_style_content = re.sub(r'\n\s*\n', '\n', new_style_content)
    new_style_content = new_style_content.strip()
    
    # If it's mostly empty or just has a media query left, let's keep it tidy
    if new_style_content:
        # Re-indent a bit
        lines = new_style_content.split('\n')
        indented_lines = []
        for line in lines:
            line = line.strip()
            if line:
                indented_lines.append(f'        {line}')
        new_style_content = '\n'.join(indented_lines)
    
    if new_style_content != style_content.strip():
        # Add the tags back
        final_style_block = f'    <style>\n{new_style_content}\n    </style>'
        new_content = content.replace(style_match.group(0), final_style_block)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

count = 0
for filename in os.listdir(directory):
    if pattern.match(filename):
        if cleanup_file(os.path.join(directory, filename)):
            print(f'Cleaned up: {filename}')
            count += 1

print(f'Total files cleaned: {count}')
