import os

base_dir = r"c:\Projects\SV-Build\portfolio\institutions"

# Fix sengkang
s_path = os.path.join(base_dir, "sengkang-interim-bus-interchange.html")
with open(s_path, 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace("/images/portfolio/sengkang-camera-coverage-diagram.png", "/images/portfolio/institutions/sengkang-camera-coverage-diagram.png")
with open(s_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Fix cpf-maxwell
c_path = os.path.join(base_dir, "cpf-maxwell-institution.html")
with open(c_path, 'r', encoding='utf-8') as f:
    content = f.read()

if '<script src="/nav-footer.js"></script>' not in content:
    content = content.replace('</body>', '<script src="/nav-footer.js"></script>\n</body>')
    with open(c_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed lingering issues")
