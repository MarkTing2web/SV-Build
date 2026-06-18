with open("solutions/data-centres.html", encoding="utf-8") as fh:
    content = fh.read()

old = "institutions-security-singapore-rel.webp" in content
new = "solution-institutions-schools-hero.webp" in content
print(f"Old image removed: {not old}  (expected: True)")
print(f"New image present: {new}  (expected: True)")
