import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Remove all <label class="filter-label"> elements inside <section class="filter-section">
# We can find the filter-section block first
filter_sec_start = content.find('<section class="filter-section"')
if filter_sec_start != -1:
    filter_sec_end = content.find('</section>', filter_sec_start)
    if filter_sec_end != -1:
        filter_section = content[filter_sec_start:filter_sec_end]
        # Remove labels
        # Using regex to remove <label class="filter-label">...</label>
        new_filter_section = re.sub(r'<label class="filter-label"[^>]*>.*?</label>\s*', '', filter_section, flags=re.DOTALL)
        content = content[:filter_sec_start] + new_filter_section + content[filter_sec_end:]

# Step 2: Add placeholder to #pSearch
content = content.replace('<input type="text" id="pSearch" onkeyup="filterP()">', '<input type="text" id="pSearch" placeholder="Search projects..." onkeyup="filterP()">')

# Step 2: Replace "All Properties" with "All Property Types"
content = content.replace('<option value="all">All Properties</option>', '<option value="all">All Property Types</option>')

# Step 2: Replace "All Systems" with "All System Types"
content = content.replace('<option value="all">All Systems</option>', '<option value="all">All System Types</option>')

# Step 3: CSS Replacements
css_old_1 = """.filter-section {
            background: #fff;
            padding: 24px 0;
            border-bottom: 1px solid #e2e8f0;
            position: sticky;
            top: 70px;
            z-index: 100;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        }"""
        
css_new_1 = """.filter-section {
            background: #fff;
            padding: 14px 0;
            border-bottom: 1px solid #e2e8f0;
            position: sticky;
            top: 70px;
            z-index: 100;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        }"""

if css_old_1 in content:
    content = content.replace(css_old_1, css_new_1)
else:
    print("Could not find CSS block 1")

css_old_2 = """.filter-item select,
        .filter-item input {
            width: 100%;
            padding: 12px 16px;
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            font-family: inherit;
            font-size: 0.9rem;
            background: #f8fafc;
            transition: var(--trs);
        }"""
        
css_new_2 = """.filter-item select,
        .filter-item input {
            width: 100%;
            padding: 10px 14px;
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            font-family: inherit;
            font-size: 0.9rem;
            background: #f8fafc;
            transition: var(--trs);
        }"""

if css_old_2 in content:
    content = content.replace(css_old_2, css_new_2)
else:
    print("Could not find CSS block 2")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied successfully.")
