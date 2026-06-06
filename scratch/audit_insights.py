import os
import glob
import re

workspace = r"c:\Projects\SV-Build"
insights_files = glob.glob(os.path.join(workspace, "insights", "*.html"))

built = []
stub = []

def get_text(html):
    # Try to find <main> or <article> or just the body
    m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL | re.IGNORECASE)
    if not m:
        m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
    if not m:
        m = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
    
    if m:
        content = m.group(1)
    else:
        content = html
        
    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', ' ', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', content)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

for full_path in insights_files:
    filename = os.path.basename(full_path)
    if filename == "index.html":
        continue
        
    with open(full_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    text = get_text(html)
    word_count = len(text.split())
    
    lower_text = text.lower()
    if word_count < 200 or "coming soon" in lower_text or "article coming" in lower_text or "placeholder" in lower_text:
        stub.append(filename)
    else:
        built.append(filename)

print("### Built — has real content (200+ words)")
for f in built:
    print(f"- {f}")
if not built: print("None")
print()

print("### Stub or missing — needs content")
for f in stub:
    print(f"- {f}")
if not stub: print("None")
print()

print("### Summary")
print(f"- Total insights files found: {len(built) + len(stub)}")
print(f"- Built with content: {len(built)}")
print(f"- Stubs or empty: {len(stub)}")

