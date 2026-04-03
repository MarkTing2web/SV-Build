import os
import glob

# Mapping of corrupted sequences to correct ones
MAPPING = {
    "Â·": "·",
    "Â ": " ",
    "â€”": "—",
    "ðŸ“…": "📅",
    "ðŸ’¬": "💬",
    "â€¢": "•",
    "â€¦": "…",
    "SECURET": "SECURE™",
    "VESTAA": "VESTA",
    "dY\":": "📅", # handling the dY escaped
    "dY\"": "📅",
    "dY'": "💬"
}

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old, new in MAPPING.items():
        if old in content:
            content = content.replace(old, new)
            modified = True
            
    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {path}")

if __name__ == "__main__":
    for f in glob.glob("insights-*.html"):
        try:
            fix_file(f)
        except Exception as e:
            print(f"Error {f}: {e}")
