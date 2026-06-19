import re, os, glob

files = sorted(glob.glob("solutions/**/*.html", recursive=True))
# Exclude solutions root pages — only subfolders
files = [f for f in files if f.count(os.sep) > 1 or f.count("/") > 1]

print(f"{'File':<55} {'min-height':<12} {'H1 chars':<10} {'SUB chars'}")
print("-" * 100)

for path in files:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    # min-height from style block
    height = re.search(r'min-height:\s*([^;!]+?)(?:\s*!important)?;', content)
    h_val = height.group(1).strip() if height else "NOT SET"

    # H1 text
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.S)
    h1_text = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else ""

    # Subtitle
    sub = re.search(r'<p class="hero-subtitle-main">(.*?)</p>', content, re.S)
    sub_text = re.sub(r'<[^>]+>', '', sub.group(1)).strip() if sub else ""

    # Flag
    ok = h_val == "45vh"
    flag = "[OK]" if ok else "[FAIL]"

    print(f"{flag} {path:<53} {h_val:<12} {len(h1_text):<10} {len(sub_text)}")
    if h1_text:
        print(f"   H1:  {h1_text[:90]}")
    if sub_text:
        print(f"   SUB: {sub_text[:90]}")
    print()
