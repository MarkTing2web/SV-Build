import os
import re

portfolio_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio"

results = []

def remove_media_blocks(css):
    result = []
    in_media = False
    brace_depth = 0
    i = 0
    while i < len(css):
        if not in_media:
            if css.startswith('@media', i):
                in_media = True
                brace_depth = 0
                while i < len(css) and css[i] != '{':
                    i += 1
                if i < len(css):
                    brace_depth = 1
            else:
                result.append(css[i])
        else:
            if css[i] == '{':
                brace_depth += 1
            elif css[i] == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    in_media = False
        i += 1
    return "".join(result)

for root, _, files in os.walk(portfolio_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            rel_path = os.path.relpath(filepath, portfolio_dir).replace('\\', '/')
            if rel_path.lower() == 'index.html':
                continue
            
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                
                hero_style = "NOT FOUND"
                hero_match = re.search(r'<[^>]*class="[^"]*portfolio-hero[^"]*"[^>]*>', content)
                if hero_match:
                    tag_content = hero_match.group(0)
                    style_match = re.search(r'style="([^"]*)"', tag_content)
                    if style_match:
                        hero_style = style_match.group(1).strip()
                    else:
                        hero_style = "NO INLINE STYLE"
                        
                has_desktop_rule = "no"
                style_block_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                if style_block_match:
                    style_content = style_block_match.group(1)
                    desktop_css = remove_media_blocks(style_content)
                    if 'background-image' in desktop_css:
                        has_desktop_rule = "yes"
                        
                results.append((rel_path, hero_style, has_desktop_rule))

with open(r"d:\Ler Wee Meng\Project-Web\SV-Build\scratch\portfolio_styles_output.txt", "w", encoding="utf-8") as f:
    for rel_path, style, has_desktop in sorted(results):
        f.write(f"- {rel_path} -> {style} -> has desktop rule: {has_desktop}\n")
