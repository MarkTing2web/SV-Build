import os
import glob
import re

workspace = r"c:\Projects\SV-Build"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

# To avoid auditing things in _ai, scratch, etc.
html_files = [f for f in html_files if not ('_ai' in f or 'scratch' in f or 'node_modules' in f or '.git' in f)]

results = {
    "correct": [],
    "wrong_domain": [],
    "path_mismatch": [],
    "missing": [],
    "trailing_slash": []
}

for full_path in html_files:
    rel_path = os.path.relpath(full_path, workspace).replace('\\', '/')
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    canon_m = re.search(r'<link[^>]*rel="canonical"[^>]*href="([^"]+)"', content, re.IGNORECASE)
    if not canon_m:
        # Check alternative order: href first then rel
        canon_m = re.search(r'<link[^>]*href="([^"]+)"[^>]*rel="canonical"', content, re.IGNORECASE)
        
    if not canon_m:
        results["missing"].append(rel_path)
        continue
        
    canon_url = canon_m.group(1)
    
    # 1. Domain check
    if not canon_url.startswith("https://www.securevision.com.sg"):
        results["wrong_domain"].append((rel_path, canon_url))
        continue
        
    # Remove domain to get the path
    url_path = canon_url.replace("https://www.securevision.com.sg", "")
    if not url_path.startswith("/"):
        url_path = "/" + url_path
        
    # 4. Trailing slash consistency (for index.html)
    is_index = rel_path.endswith("index.html")
    if is_index:
        expected_path = "/" + rel_path.replace("index.html", "")
        # e.g., if rel_path is index.html, expected_path is /
        # if rel_path is portfolio/index.html, expected_path is /portfolio/
        if url_path.endswith("index.html"):
            results["trailing_slash"].append((rel_path, canon_url))
            continue
        elif url_path != expected_path:
            # It might have path mismatch as well
            results["path_mismatch"].append((rel_path, canon_url, "https://www.securevision.com.sg" + expected_path))
            continue
    else:
        expected_path = "/" + rel_path
        if url_path != expected_path:
            results["path_mismatch"].append((rel_path, canon_url, "https://www.securevision.com.sg" + expected_path))
            continue
            
    results["correct"].append(rel_path)

print("### Wrong domain (svbuild.vercel.app or http:// or missing www)")
for rel_path, current in results["wrong_domain"]:
    print(f"- `{rel_path}`: `{current}`")
if not results["wrong_domain"]: print("None")
print()

print("### Path mismatch (canonical doesn't match file location)")
for rel_path, current, expected in results["path_mismatch"]:
    print(f"- `{rel_path}`: current: `{current}`, should be: `{expected}`")
if not results["path_mismatch"]: print("None")
print()

print("### Missing canonical")
for rel_path in results["missing"]:
    print(f"- `{rel_path}`")
if not results["missing"]: print("None")
print()

print("### Trailing slash issue")
for rel_path, current in results["trailing_slash"]:
    print(f"- `{rel_path}`: `{current}`")
if not results["trailing_slash"]: print("None")
print()

print("### Summary")
total_checked = len(html_files)
print(f"- Total files checked: {total_checked}")
print(f"- Files with correct canonical: {len(results['correct'])}")
print(f"- Files with wrong domain: {len(results['wrong_domain'])}")
print(f"- Files with path mismatch: {len(results['path_mismatch'])}")
print(f"- Files missing canonical: {len(results['missing'])}")
print(f"- Files with trailing slash issues: {len(results['trailing_slash'])}")
