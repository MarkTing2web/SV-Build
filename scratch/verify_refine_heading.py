import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start = content.find('class="filter-section"')
section_start = content.rfind('<section', 0, start)
section_end = content.find('</section>', section_start)
section_text = content[section_start:section_end]

# 1. NOT present inside filter-section
print(f"1. Is 'Refine' inside <section class=\"filter-section\">? {'Yes' if 'Refine' in section_text else 'No'}")

# 2. IS present before filter-section
before_section = content[section_start-200:section_start]
print(f"2. Is 'Refine' before <section class=\"filter-section\">? {'Yes' if 'Refine' in before_section else 'No'}")

# 3. filter-section contains only filter-bar
# Look at what is inside the container in filter-section
container_start = section_text.find('<div class="container">')
if container_start != -1:
    container_inner = section_text[container_start + len('<div class="container">'):].strip()
    if container_inner.startswith('<div class="filter-bar">'):
        print("3. <section class=\"filter-section\"> container starts directly with filter-bar: Yes")
    else:
        print("3. <section class=\"filter-section\"> container starts directly with filter-bar: No")

# 4. sticky behavior
css_block = re.search(r'\.filter-section\s*{[^}]*}', content)
if css_block:
    print(f"4. Is 'position: sticky' in .filter-section? {'Yes' if 'position: sticky' in css_block.group(0) else 'No'}")
