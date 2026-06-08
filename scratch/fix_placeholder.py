import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r'<input[^>]*id="pSearch"[^>]*>', 
    '<input type="text" id="pSearch" placeholder="Search projects..." onkeyup="filterP()">', 
    content
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
