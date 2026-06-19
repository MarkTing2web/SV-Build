with open("solutions/improve-visitor-management.html", encoding="utf-8") as fh:
    content = fh.read()

old = 'class="impact-list-label"' in content
new = 'class="callout-box"' in content
print(f"impact-list-label removed: {not old}  (expected: True)")
print(f"callout-box present:       {new}  (expected: True)")
