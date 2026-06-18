import re

files = [
    "solutions/healthcare.html",
    "solutions/industrial.html",
    "solutions/institutions.html",
    "solutions/managed-living.html",
    "solutions/data-centres.html"
]

for path in files:
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()

    # Find "Project Planning" section and replace grid-4 inside it
    # We look for "Project Planning" and then the first grid-4 mt-48 within the next 1500 chars
    match = re.search(r'(Project Planning.*?)(class="grid-4 mt-48")', content, re.S)
    if match:
        full_match_str = match.group(0)
        target = match.group(2)
        new_target = 'class="grid-3 mt-48"'
        
        new_full_match_str = full_match_str.replace(target, new_target)
        content = content.replace(full_match_str, new_full_match_str)
        
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"Fixed Project Planning grid in {path}")
    else:
        print(f"No match found for: {path}")
