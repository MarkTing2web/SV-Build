import re, os, glob

files = sorted(glob.glob("solutions/**/*.html", recursive=True))
files = [f for f in files if os.path.dirname(f) != "solutions"]

print(f"{'File':<58} {'min-height':<12} {'SUB chars':>9}  {'Status'}")
print("-" * 90)

all_ok = True
for path in files:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    height = re.search(r'min-height:\s*([^;!]+?)(?:\s*!important)?;', content)
    h_val = height.group(1).strip() if height else "NOT SET"
    sub = re.search(r'<p class="hero-subtitle-main">(.*?)</p>', content, re.S)
    sub_text = re.sub(r'<[^>]+>', '', sub.group(1)).strip() if sub else ""
    h_ok = h_val == "45vh"
    s_ok = len(sub_text) <= 150
    ok = h_ok and s_ok
    if not ok:
        all_ok = False
    flag = "[OK]" if ok else "[FAIL]"
    print(f"{flag} {path:<56} {h_val:<12} {len(sub_text):>9}  {'OK' if ok else 'FAIL'}")

print()
print("All OK" if all_ok else "ISSUES REMAIN - check flagged files")
