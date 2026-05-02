
import os
import unicodedata

files = [
    "insights/after-security-installation-support.html",
    "insights/home-security-system-cost-singapore.html",
    "insights/is-my-security-system-still-working.html",
    "insights/security-system-refresh.html"
]

for file_path in files:
    if os.path.exists(file_path):
        print(f"--- {file_path} ---")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            non_ascii = {c for c in content if ord(c) > 127}
            for char in sorted(non_ascii):
                try:
                    name = unicodedata.name(char)
                except:
                    name = "UNKNOWN"
                print(f"U+{ord(char):04X} | {name}")
