import re, os, glob

files = sorted(glob.glob("solutions/*.html"))
for path in files:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    cta = re.search(r'cta-section.*?</section>', content, re.S)
    if not cta:
        continue
    has_wa = "wa.me" in cta.group(0)
    btn_count = len(re.findall(r'class="btn ', cta.group(0)))
    flag = "✅" if has_wa else "❌"
    print(f"{flag} {os.path.basename(path)}: buttons={btn_count}, whatsapp={has_wa}")
