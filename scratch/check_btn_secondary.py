import re, glob, os

for path in sorted(glob.glob("solutions/*.html")):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    if "btn-secondary" in content:
        count = len(re.findall(r'btn-secondary', content))
        print(f"❌ {os.path.basename(path)}: btn-secondary found ({count}x)")
    else:
        print(f"✅ {os.path.basename(path)}: clean")
