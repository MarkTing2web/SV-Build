import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

start = content.find('class="filter-section"')
if start != -1:
    section_start = content.rfind('<section', 0, start)
    section_end = content.find('</section>', section_start)
    if section_end != -1:
        with open(r"d:\Ler Wee Meng\Project-Web\SV-Build\scratch\filter_section_dump.html", "w", encoding="utf-8") as f:
            f.write(content[section_start:section_end+10])
    print("Dumped.")
else:
    print("Not found.")
