import re

files = [
    "solutions/data-centres.html",
    "solutions/healthcare.html",
    "solutions/industrial.html",
    "solutions/institutions.html",
    "solutions/managed-living.html",
    "solutions/residential.html"
]

patterns = [
    re.compile(r"min-height"),
    re.compile(r"hero-standard"),
    re.compile(r"background-image")
]

for file_path in files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                if any(pat.search(line) for pat in patterns):
                    print(f"{file_path}:{line_no}:{line.strip()}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
