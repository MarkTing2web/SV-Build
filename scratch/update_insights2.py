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
        
    content1 = original_content
    if not already_has_slug:
        # insert data-article right after <body
        content1 = re.sub(r'<body(?![^>]*data-article=)([^>]*)>', f'<body data-article="{slug}"\\1>', content1)

    # Change 2: Replace related grid
    already_has_grid_id = False
    grid_found = False
    content2 = content1
    
    if 'class="insights-related-grid"' in content2:
        if 'id="related-insights-grid"' in content2:
            already_has_grid_id = True
            grid_found = True
        else:
            grid_found = True
            # Find the starting tag <div class="insights-related-grid">
            # and replace everything up to the next </div> that closes it.
            # A robust way is to just use re.sub with a regex that looks ahead to </section> or the end of the container
            # Since the structure is known:
            # <div class="insights-related-grid">
            #   ...
            # </div>
            # </div> (closes container)
            # </section>
            
            pattern = r'<div\s+class="insights-related-grid"[^>]*>.*?</div>\s*</div>\s*</section>'
            replacement = f'<div class="insights-related-grid"\n      id="related-insights-grid"></div>\n    </div>\n  </section>'
            
            # actually better:
            pattern = r'<div\s+class="insights-related-grid"[^>]*>.*?(?=</div>\s*</section>|</div>\s*</div>\s*</section>)'
            
            # Let's use a simple string manipulation
            start_idx = content2.find('class="insights-related-grid"')
            if start_idx != -1:
                # find the <div before it
                div_start = content2.rfind('<div', 0, start_idx)
                
                # find the closing </div> of the container or section to know where to stop
                # Let's just find the next </section> and work backwards
                section_end = content2.find('</section>', start_idx)
                if section_end != -1:
                    # we want to replace from div_start to the </div> right before </section>
                    # Actually, we can just replace the whole section inner part.
                    pass
            
            # A much safer regex that works for this specific structure:
            # We want to replace <div class="insights-related-grid"> ... </div>
            # with <div class="insights-related-grid" id="related-insights-grid"></div>
            # Let's match from <div class="insights-related-grid" to the last </div> before </section>
            
            content2 = re.sub(
                r'(<div[^>]*class="insights-related-grid"[^>]*>).*?(</div>\s*</div>\s*</section>|</div>\s*</section>)',
                r'<div class="insights-related-grid"\n      id="related-insights-grid"></div>\n    \2',
                content2,
                flags=re.DOTALL
            )
            
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

print("--- SUMMARY ---")
print(f"Total files updated: {len(files_updated)}")
for f, s in files_updated:
    print(f"  - {f} (slug: {s})")

print(f"\nFiles skipped (changes already applied): {len(files_skipped)}")
for f in files_skipped:
    print(f"  - {f}")

print(f"\nFiles where related grid was not found: {len(grid_not_found)}")
for f in grid_not_found:
    print(f"  - {f}")
