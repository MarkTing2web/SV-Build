filepath = r'c:\Projects\SV-Build\sv-shared.css'
with open(filepath, 'rb') as f:
    blob = f.read()

if b'\x00' in blob:
    print("Null bytes found. Likely UTF-16LE.")
    try:
        content = blob.decode('utf-16le')
        print("Successfully decoded as UTF-16LE.")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Converted to UTF-8.")
    except Exception as e:
        print(f"Failed to decode as UTF-16LE: {e}")
else:
    print("No null bytes found.")
