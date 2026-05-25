import os

base_dir = r"c:\Projects\SV-Build\portfolio\institutions"
files = [
    "catholic-centre-waterloo.html",
    "changi-airport-lpr-barriers.html",
    "cpf-maxwell-institution.html",
    "das-learning-centre-woodlands.html",
    "my-world-preschool-cctv.html",
    "sengkang-interim-bus-interchange.html",
    "sfx-retreat-centre-punggol.html"
]

count = 0
for filename in files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<script src="/portfolio-block.js"></script>' not in content:
        if '<script src="/nav-footer.js"></script>' in content:
            content = content.replace('<script src="/nav-footer.js"></script>', '<script src="/portfolio-block.js"></script>\n  <script src="/nav-footer.js"></script>')
        else:
            content = content.replace('</body>', '<script src="/portfolio-block.js"></script>\n</body>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {filename}")

print(f"Task F updated {count} files.")
