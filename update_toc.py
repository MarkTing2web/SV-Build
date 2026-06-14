import os
import re

dir_path = r"c:\Projects\SV-Build\insights"
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

updated_files = {}
untouched_files = []
error_files = []

for file in html_files:
    file_path = os.path.join(dir_path, file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the tocList block
        toc_match = re.search(r'(<ul[^>]*id="tocList"[^>]*>.*?</ul>)', content, re.DOTALL)
        if not toc_match:
            continue

        toc_block = toc_match.group(1)
        
        # Check if already numbered
        items = re.findall(r'<li>\s*<a[^>]*>(.*?)</a>\s*</li>', toc_block)
        
        needs_numbering = False
        for text in items:
            if not re.match(r'^\s*\d+\.', text):
                needs_numbering = True
                break
                
        if not needs_numbering and len(items) > 0:
            untouched_files.append(file)
            continue
            
        if needs_numbering:
            class Counter:
                def __init__(self):
                    self.val = 1
            
            c = Counter()

            def replace_item_cls(match):
                prefix = match.group(1)
                text = match.group(2)
                suffix = match.group(3)
                
                if not re.match(r'^\s*\d+\.', text):
                    new_text = f"{c.val}. {text}"
                    c.val += 1
                    return f"{prefix}{new_text}{suffix}"
                else:
                    c.val += 1
                    return match.group(0)

            new_toc_block = re.sub(r'(<li>\s*<a[^>]*>)(.*?)(</a>\s*</li>)', replace_item_cls, toc_block)
            
            if new_toc_block != toc_block:
                new_content = content.replace(toc_block, new_toc_block)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                updated_files[file] = c.val - 1
            else:
                untouched_files.append(file)
                
    except Exception as e:
        error_files.append(f"{file}: {str(e)}")

print("UPDATED_FILES_START")
for f, count in updated_files.items():
    print(f"- {f} ({count} items numbered)")
print("UPDATED_FILES_END")

print("UNTOUCHED_FILES_START")
for f in untouched_files:
    print(f"- {f}")
print("UNTOUCHED_FILES_END")

print("ERRORS_START")
for f in error_files:
    print(f"- {f}")
print("ERRORS_END")
