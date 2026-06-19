import re

files = [
    "solutions/reduce-guard-manpower.html",
    "solutions/improve-visitor-management.html",
    "solutions/upgrade-intercom-system.html",
    "solutions/improve-cctv-visibility.html",
    "solutions/automate-vehicle-access.html",
]

for path in files:
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()
    
    sections = re.split(r'(<section[^>]*>)', content)
    
    new_content = ""
    in_target_section = False
    
    for part in sections:
        if part.startswith("<section"):
            new_content += part
        else:
            if "Project Planning" in part:
                # Replace the first occurrence of grid-4 mt-48 with grid-3 mt-48 in this section
                part = part.replace('class="grid-4 mt-48"', 'class="grid-3 mt-48"', 1)
            new_content += part
            
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_content)
    print(f"Updated {path}")
