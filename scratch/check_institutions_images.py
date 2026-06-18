import os

images = [
    ("Card 1 — Schools",         "images/solutions/root-solutions/solution-hub-prop-school.webp"),
    ("Card 2 — Govt/Public",     "images/solutions/hero-solutions/solution-institutions-govt-office-hero-rel.webp"),
    ("Card 3 — Community",       "images/solutions/hero-solutions/solution-institutions-schools-hero-rel.webp"),
]

print("=== Checking institution card images ===")
for label, path in images:
    exists = os.path.exists(path)
    print(f"{'[EXISTS]' if exists else '[MISSING]'}  {label}: {path}")

print("\n=== All institution-related images on disk ===")
for root, dirs, files in os.walk("images/solutions"):
    for f in files:
        if "institution" in f.lower() or "school" in f.lower() or "govt" in f.lower() or "community" in f.lower():
            print(os.path.join(root, f))
