
import os

files = [
    "insights/after-security-installation-support.html",
    "insights/home-security-system-cost-singapore.html",
    "insights/is-my-security-system-still-working.html",
    "insights/security-system-refresh.html"
]

replacements = [
    ("â€”", "—"),
    ("â€“", "–"),
    ("â€™", "'"),
    ("â€œ", "“"),
    ("â€", "”"),
    ("â„¢", "™"),
    ("Â·", "·"),
    ("ðŸ’¬", "💬"),
    ("ðŸ“…", "📅"),
    ("â€¦", "…"),
    ("Â", ""), # Often a stray character before other symbols
]

for file_path in files:
    if os.path.exists(file_path):
        print(f"Cleaning {file_path}...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        new_content = content
        for old, new in replacements:
            new_content = new_content.replace(old, new)
        
        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Fixed mojibake in {file_path}")
        else:
            print(f"No mojibake found in {file_path}")
