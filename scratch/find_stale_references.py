import os
import re

repo_root = r"c:\Projects\SV-Build"

exclude_dirs = {'.git', '.vercel', 'scratch', 'node_modules', 'artifacts', '.github'}
html_files = []
for root, dirs, files in os.walk(repo_root):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

html_files.sort()

allowed_prefixes = [
    "images/solutions/hero-solutions/",
    "images/solutions/root-solutions/",
    "images/solutions/commercial/",
    "images/solutions/condominiums/",
    "images/solutions/data-centres/",
    "images/solutions/healthcare/",
    "images/solutions/industrial/",
    "images/solutions/institutions/",
    "images/solutions/managed-living/",
    "images/solutions/residential/"
]

stale_references = []

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find occurrences of "images/solutions/"
    pattern = re.compile(r'(?:https?://[^/]+)?/?images/solutions/[^\'"\s>]+', re.IGNORECASE)
    matches = pattern.findall(content)
    
    for match in matches:
        cleaned = match
        if cleaned.lower().startswith("http"):
            idx = cleaned.lower().find("images/solutions/")
            if idx != -1:
                cleaned = cleaned[idx:]
        else:
            cleaned = cleaned.lstrip('/')
            
        # cleaned now starts with "images/solutions/"
        is_allowed = False
        for prefix in allowed_prefixes:
            if cleaned.lower().startswith(prefix.lower()):
                is_allowed = True
                break
                
        if not is_allowed:
            matched_target = False
            for t in ["solution-", "reduce-manpower", "service-technicians"]:
                if t.lower() in cleaned.lower():
                    matched_target = True
                    break
            if matched_target:
                rel_path = os.path.relpath(filepath, repo_root).replace('\\', '/')
                stale_references.append((rel_path, match))

for rel_path, ref in stale_references:
    print(f"{rel_path}: STALE REFERENCE FOUND -> {ref}")

print(f"\nTotal stale references: {len(stale_references)}")
