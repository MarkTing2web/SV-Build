import os

filepath = r'c:\Projects\SV-Build\sv-shared.css'

def try_convert(filepath):
    encodings = ['utf-16', 'utf-16le', 'utf-16be', 'cp1252', 'latin1']
    for enc in encodings:
        try:
            with open(filepath, 'rb') as f:
                blob = f.read()
            content = blob.decode(enc)
            print(f"Successfully decoded with {enc}")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Converted {filepath} to UTF-8 using {enc}")
            return True
        except:
            continue
    return False

with open(filepath, 'rb') as f:
    start = f.read(4)
    print(f"File starts with: {start}")

if not try_convert(filepath):
    print("Could not convert file.")
