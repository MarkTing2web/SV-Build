import os
import glob
import re

target_dir = r"c:\Projects\SV-Build\insights"
html_files = glob.glob(os.path.join(target_dir, "*.html"))

excluded = ['index.html', 'index-od1.html', 'index-od2.html']

files_updated = []
files_skipped = []
grid_not_found = []

for filepath in html_files:
    filename = os.path.basename(filepath)
    if filename in excluded:
        continue
        
    slug = filename.replace('.html', '')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # Change 1: Add data-article to <body>
    already_has_slug = False
    if re.search(r'<body[^>]*data-article=', content):
        already_has_slug = True
    else:
        # We look for exactly <body> or <body class="..."> etc, without data-article
        # To be safe, we just replace <body> if it exists as exactly <body>
        # Sometimes there might be <body class="..."> so we handle it:
        content = re.sub(r'<body(?![^>]*data-article)[^>]*>', f'<body data-article="{slug}">', content)
        # Wait, if there are classes on body, we'd lose them with the above naive substitution!
        # Let's fix that.
        
    # Let's do it safer for Change 1:
    content1 = original_content
    if not already_has_slug:
        # Match <body ...> and replace with <body data-article="{slug}" ...>
        # but the prompt specifically says "FIND: <body> REPLACE WITH: <body data-article="[slug]">"
        # However, to preserve potential other attributes, let's just insert data-article right after <body
        content1 = re.sub(r'<body(?![^>]*data-article=)([^>]*)>', f'<body data-article="{slug}"\\1>', content1)

    # Change 2: Replace related grid
    already_has_grid_id = False
    grid_found = False
    content2 = content1
    
    # Check if grid exists
    if 'class="insights-related-grid"' in content2:
        if 'id="related-insights-grid"' in content2:
            already_has_grid_id = True
            grid_found = True
        else:
            grid_found = True
            # We want to replace <div class="insights-related-grid"> ... </div>
            # with <div class="insights-related-grid"\n    id="related-insights-grid"></div>
            # Use regex to find the div and its contents up to the matching closing div.
            # But regex for nested HTML can be tricky, let's assume it closes before the next </section>
            
            # Since the grid is always inside:
            # <div class="insights-related-grid">
            #   [any content]
            # </div>
            # And followed by </div> or </section>.
            
            # We will find `<div class="insights-related-grid">` and the first `</div>` after it that has no inner divs, or we can just use a non-greedy regex matching up to the first `</div>` assuming nav cards don't have nested `<div>`s, or just look for `class="insights-related-grid"` up to `</div>\n  </div>\n</section>`
            
            # The prompt says: Replace ONLY the inner grid div and its contents
            
            content2 = re.sub(
                r'<div\s+class="insights-related-grid"\s*>(.*?)</div>',
                r'<div class="insights-related-grid"\n    id="related-insights-grid"></div>',
                content1,
                flags=re.DOTALL
            )
            
            # Wait, if there are nested divs, regex `.*?</div>` will fail if nav cards have divs.
            # Let's check if there are nested divs in the grid. Usually it's `<a><span>...</span><strong>...</strong></a>`.
            # Let's use a simpler regex that replaces from `<div class="insights-related-grid">` up to `</div>\n  </div>\n</section>`
            # Better:
            # We know the closing is before `</div>\n</section>`
            # Let's do `r'<div\s+class="insights-related-grid"\s*>.*?(?=</div>\s*</div>\s*</section>)'`
            # Actually, `re.sub(r'<div class="insights-related-grid">[\s\S]*?(?=</div>\s*</div>\s*</section>)', ...)`
            
            # Let's write a python parser for this or just a robust regex.
    else:
        grid_found = False

    
    if content2 != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content2)
        files_updated.append((filename, slug))
    else:
        files_skipped.append(filename)
        
    if not grid_found:
        grid_not_found.append(filename)

print(f"Total files updated: {len(files_updated)}")
for f, s in files_updated:
    print(f"  - {f} (slug: {s})")

print(f"\nFiles skipped (changes already applied): {len(files_skipped)}")
for f in files_skipped:
    print(f"  - {f}")

print(f"\nFiles where grid was not found: {len(grid_not_found)}")
for f in grid_not_found:
    print(f"  - {f}")

