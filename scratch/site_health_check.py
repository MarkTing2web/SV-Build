import os
import re

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
out_file = os.path.join(root_dir, '_ai', 'full-site-health-check.txt')

exclude_dirs = {'.git', '.vercel', 'scratch', 'node_modules', 'templates', 'images', 'artifacts', 'temp-solutions', 'instructions', '.github', '_ai'}

html_files = []
for root, dirs, files in os.walk(root_dir):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            if '_template' in file:
                continue
            html_files.append(os.path.join(root, file))

html_files.sort()

def analyze_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {"error": str(e)}

    # Title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "MISSING"

    # Meta Description
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', content, re.IGNORECASE | re.DOTALL)
    desc = desc_match.group(1).strip() if desc_match else "MISSING"

    # Find body content
    body_match = re.search(r'<body.*?>(.*?)</body>', content, re.IGNORECASE | re.DOTALL)
    body_content = body_match.group(1) if body_match else ""

    # Count inline styles and style blocks inside body
    inline_styles = len(re.findall(r'\bstyle\s*=\s*["\']', body_content, re.IGNORECASE))
    style_blocks = len(re.findall(r'<style\b[^>]*>', body_content, re.IGNORECASE))

    # Total styles check
    total_styles = inline_styles + style_blocks

    # JS Calls
    calls_solutions = 'solutions-block.js' in content
    calls_systems = 'systems-block.js' in content
    calls_nav = 'nav-footer.js' in content

    return {
        "title": title,
        "desc": desc,
        "inline_styles": inline_styles,
        "style_blocks": style_blocks,
        "total_styles": total_styles,
        "calls_solutions": calls_solutions,
        "calls_systems": calls_systems,
        "calls_nav": calls_nav
    }

os.makedirs(os.path.dirname(out_file), exist_ok=True)

with open(out_file, 'w', encoding='utf-8') as f:
    f.write("=== FULL SITE HEALTH CHECK ===\n\n")
    f.write(f"Total HTML files scanned: {len(html_files)}\n")
    f.write("=" * 60 + "\n\n")
    
    for filepath in html_files:
        rel_path = os.path.relpath(filepath, root_dir).replace('\\', '/')
        res = analyze_file(filepath)
        
        f.write(f"File Path: /{rel_path}\n")
        f.write(f"Filename: {os.path.basename(filepath)}\n")
        
        if "error" in res:
            f.write(f"Error reading file: {res['error']}\n")
        else:
            f.write(f"<title>: {res['title']}\n")
            f.write(f"<meta description>: {res['desc']}\n")
            
            style_msg = f"Found {res['total_styles']} total (Inline: {res['inline_styles']}, <style> blocks: {res['style_blocks']})"
            if res['total_styles'] == 0:
                style_msg = "0 (Clean)"
            f.write(f"Body Styles: {style_msg}\n")
            
            js_calls = []
            if res['calls_solutions']: js_calls.append("solutions-block.js")
            if res['calls_systems']: js_calls.append("systems-block.js")
            if res['calls_nav']: js_calls.append("nav-footer.js")
            
            js_msg = ", ".join(js_calls) if js_calls else "None"
            f.write(f"JS Calls Found: {js_msg}\n")
        
        f.write("-" * 60 + "\n\n")

print(f"Health check complete! Report saved to {out_file} with {len(html_files)} files analyzed.")
