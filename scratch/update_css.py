import sys
sys.stdout.reconfigure(encoding='utf-8')

css_path = r"C:\Projects\SV-Build\sv-insights.css"

encodings = ['utf-16-le', 'utf-16', 'utf-8', 'latin-1']
content = None
chosen_enc = None

for enc in encodings:
    try:
        with open(css_path, 'r', encoding=enc) as f:
            content = f.read()
            if ".article-body .toc-list" in content:
                chosen_enc = enc
                break
    except Exception:
        continue

if not chosen_enc:
    print("ERROR: Could not read CSS file!")
    sys.exit(1)

target = """  padding: 5px 0 5px 28px;
  text-indent: -18px;"""

replacement = """  padding: 5px 0 5px 22px;
  text-indent: -12px;"""

if target in content:
    content = content.replace(target, replacement)
    with open(css_path, 'w', encoding=chosen_enc) as f:
        f.write(content)
    print("SUCCESS: Style replaced successfully!")
else:
    # Check if line endings differ (\r\n vs \n)
    target_lf = target.replace("\r\n", "\n")
    content_lf = content.replace("\r\n", "\n")
    if target_lf in content_lf:
        content_lf = content_lf.replace(target_lf, replacement.replace("\r\n", "\n"))
        if "\r\n" in content:
            content_new = content_lf.replace("\n", "\r\n")
        else:
            content_new = content_lf
        with open(css_path, 'w', encoding=chosen_enc) as f:
            f.write(content_new)
        print("SUCCESS: Style replaced (LF match) successfully!")
    else:
        print("ERROR: Target style block not found in CSS file!")
