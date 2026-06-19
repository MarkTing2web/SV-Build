import glob, os

for path in glob.glob("solutions/*.html"):
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()
    
    if 'class="btn btn-secondary"' in content:
        new_content = content.replace('class="btn btn-secondary"', 'class="btn btn-outline-light"')
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_content)
        print(f"Updated {path}")
