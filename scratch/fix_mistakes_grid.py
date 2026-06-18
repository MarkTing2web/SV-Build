import re, glob

files = sorted(glob.glob("solutions/**/*.html", recursive=True))

for path in files:
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()

    # Find the Common Mistakes section heading
    # Usually followed by a subtitle and then the grid/stack element
    # Let's search for "Common Mistakes" and then look for card-stack or grid-4 within the next 1500 characters
    match = re.search(r'(Common Mistakes.*?)(class="(?:card-stack|grid-4) mt-48")', content, re.S | re.I)
    
    if match:
        full_match_str = match.group(0)
        target = match.group(2)
        new_target = 'class="grid-2 mt-48"'
        
        # Replace only that specific occurrence by replacing the full matched substring
        new_full_match_str = full_match_str.replace(target, new_target)
        content = content.replace(full_match_str, new_full_match_str)
        
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"Fixed {path}")
    else:
        # Check if it already has grid-2 mt-48 under Common Mistakes
        has_grid2 = re.search(r'Common Mistakes.*?(class="grid-2 mt-48")', content, re.S | re.I)
        if has_grid2:
            print(f"Already correct: {path}")
        else:
            print(f"No match found for: {path}")
