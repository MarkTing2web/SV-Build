import chardet
import os

filepath = r'c:\Projects\SV-Build\sv-shared.css'
with open(filepath, 'rb') as f:
    rawdata = f.read(10000)
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

if encoding and encoding.lower() != 'utf-8':
    print(f"Converting {filepath} to UTF-8...")
    with open(filepath, 'r', encoding=encoding) as f:
        content = f.read()
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done.")
else:
    print("File is already UTF-8 or similar.")
