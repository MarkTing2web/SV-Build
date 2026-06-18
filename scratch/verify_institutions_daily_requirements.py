with open("solutions/institutions.html", encoding="utf-8") as fh:
    content = fh.read()

old = "sol-grid-4-auto" in content
new = "Daily Requirements" in content and "grid-2 mt-48" in content
print(f"sol-grid-4-auto removed: {not old}  (expected: True)")
print(f"grid-2 mt-48 in Daily Requirements: {new}  (expected: True)")
