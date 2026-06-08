import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Number of <label class="filter-label"> inside filter-section
filter_sec_start = content.find('<section class="filter-section"')
filter_sec_end = content.find('</section>', filter_sec_start)
filter_section = content[filter_sec_start:filter_sec_end]
labels = re.findall(r'<label class="filter-label"', filter_section)
print(f"1. Number of <label class=\"filter-label\"> inside filter-section: {len(labels)}")

# 2. Confirm placeholder attribute on #pSearch
search_input = re.search(r'<input[^>]*id="pSearch"[^>]*>', content)
if search_input:
    placeholder = re.search(r'placeholder="([^"]+)"', search_input.group(0))
    print(f"2. Placeholder attribute on #pSearch: \"{placeholder.group(1) if placeholder else 'NOT FOUND'}\"")

# 3. Confirm first option text in #fProp
fprop_start = content.find('id="fProp"')
fprop_end = content.find('</select>', fprop_start)
fprop_content = content[fprop_start:fprop_end]
fprop_opt = re.search(r'<option[^>]*>([^<]+)</option>', fprop_content)
print(f"3. First option text in #fProp: \"{fprop_opt.group(1) if fprop_opt else 'NOT FOUND'}\"")

# 4. Confirm first option text in #fSys
fsys_start = content.find('id="fSys"')
fsys_end = content.find('</select>', fsys_start)
fsys_content = content[fsys_start:fsys_end]
fsys_opt = re.search(r'<option[^>]*>([^<]+)</option>', fsys_content)
print(f"4. First option text in #fSys: \"{fsys_opt.group(1) if fsys_opt else 'NOT FOUND'}\"")

# 5. Confirm .filter-section padding value
css_block1 = re.search(r'\.filter-section\s*{[^}]*padding:\s*([^;]+);', content)
print(f"5. .filter-section padding value: {css_block1.group(1) if css_block1 else 'NOT FOUND'}")

# 6. Confirm .filter-item select and input padding value
css_block2 = re.search(r'\.filter-item select,\s*\.filter-item input\s*{[^}]*padding:\s*([^;]+);', content)
print(f"6. .filter-item select and input padding value: {css_block2.group(1) if css_block2 else 'NOT FOUND'}")
