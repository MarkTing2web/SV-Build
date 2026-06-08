import os
import re

RESOURCES_DIR = r"C:\Projects\SV-Build\resources"

TRUST_BAR_CORRECT = """<div class="trust-bar">
<div class="trust-bar-inner">
<span>Police Licensed · <span class="sv-licence"></span></span>
<span class="trust-divider"></span>
<span>bizSAFE <span class="sv-bizsafe"></span></span>
<span class="trust-divider"></span>
<span><strong class="sv-sites"></strong> Sites Protected</span>
</div>
</div>"""

def fix_css_order(content):
    # Remove google fonts
    content = re.sub(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*', '', content)
    content = re.sub(r'<link rel="preconnect" href="https://fonts\.gstatic\.com"[^>]*>\s*', '', content)
    content = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet">\s*', '', content)
    
    # We want sv-shared.css then sv-resources.css
    # Find them and extract
    shared_match = re.search(r'<link[^>]*href="/sv-shared\.css"[^>]*>\s*', content)
    resources_match = re.search(r'<link[^>]*href="/sv-resources\.css"[^>]*>\s*', content)
    
    if shared_match and resources_match:
        content = content.replace(shared_match.group(0), '')
        content = content.replace(resources_match.group(0), '')
        
        # Insert them right after <head> or right before <script src="/site-config.js">
        config_match = re.search(r'<script src="/site-config\.js"></script>', content)
        if config_match:
            insert_str = '<link rel="stylesheet" href="/sv-shared.css">\n  <link rel="stylesheet" href="/sv-resources.css">\n  '
            content = content.replace(config_match.group(0), insert_str + config_match.group(0))
    return content

def fix_wa_float(content):
    # Match <a ... class="sv-wa-float" ...> ... </a> or wa-float
    # Using regex to find the <a> block
    content = re.sub(r'<a[^>]*class="[^"]*(?:wa-float|sv-wa-float)[^"]*"[^>]*>.*?</a>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<div[^>]*class="[^"]*(?:wa-float|sv-wa-float)[^"]*"[^>]*>.*?</div>\s*', '', content, flags=re.DOTALL)
    return content

def fix_trust_bar(content):
    # If sv-trust-bar exists, replace it
    if 'class="sv-trust-bar"' in content:
        content = re.sub(r'<div class="sv-trust-bar">.*?</div>\s*</div>\s*</div>', TRUST_BAR_CORRECT, content, flags=re.DOTALL)
        content = re.sub(r'<div class="sv-trust-bar">.*?</div>\s*</div>', TRUST_BAR_CORRECT, content, flags=re.DOTALL)
    elif 'class="trust-bar"' not in content:
        # Trust bar missing entirely. Insert before sv-breadcrumb
        content = content.replace('<nav class="sv-breadcrumb"', TRUST_BAR_CORRECT + '\n<nav class="sv-breadcrumb"')
    return content

def fix_nav_footer_script(content):
    # Ensure nav-footer.js is right before </body>
    if 'src="/nav-footer.js"' in content:
        # Extract it
        match = re.search(r'<script src="/nav-footer\.js"></script>\s*', content)
        if match:
            content = content.replace(match.group(0), '')
            content = content.replace('</body>', '<script src="/nav-footer.js"></script>\n</body>')
    return content


def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                content = fix_css_order(content)
                content = fix_wa_float(content)
                content = fix_trust_bar(content)
                content = fix_nav_footer_script(content)
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)

if __name__ == "__main__":
    process_directory(RESOURCES_DIR)
    print("Phase 1 fixes applied.")
