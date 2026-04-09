# fix_encoding.py
import os

def fix_mojibake(content):
    # Common mojibake replacements
    replacements = {
        'â€”': '—',
        'â€“': '–',
        'â€™': "'",
        'â€œ': '"',
        'â€?': '"',
        'â€¢': '•',
        'â†’': '→',
        'Â·': '·',
        'â–¾': '▾',
        'Â&': '&',
    }
    for old, new in replacements.items():
        content = content.replace(old, new)
    return content

directory = r'c:\Projects\SV-Build\insights'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='latin-1') as f:
            content = f.read()
        
        fixed_content = fix_mojibake(content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        print(f"Fixed {filename}")
