with open("solutions/improve-visitor-management.html", encoding="utf-8") as fh:
    content = fh.read()

old = "card-img-placeholder" in content
new = "pre-registration-app.webp" in content
print(f"Placeholder removed: {not old}  (expected: True)")
print(f"New image present:   {new}  (expected: True)")
