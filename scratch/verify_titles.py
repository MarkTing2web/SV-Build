import re

for path, label in [
    ("solutions/commercial.html", "commercial.html"),
    ("solutions/commercial/commercial-security-systems.html", "commercial-security-systems.html"),
]:
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    title = re.search(r'<title>(.*?)</title>', content)
    print(f"{label}:\n  {title.group(1) if title else 'NOT FOUND'}\n")
