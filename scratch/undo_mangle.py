filepath = r'c:\Projects\SV-Build\sv-shared.css'
with open(filepath, 'rb') as f:
    blob = f.read()

print(f"Original size: {len(blob)}")

# Fix double CR if it exists
if b'\x0d\x0d\x0a' in blob:
    print("Found CRCRLF, fixing...")
    blob = blob.replace(b'\x0d\x0d\x0a', b'\x0d\x0a')

try:
    # Reverse the latin1 mangling
    content = blob.decode('utf-8')
    original_bytes = content.encode('latin1')
    
    with open(filepath, 'wb') as f:
        f.write(original_bytes)
    print("Mangle reversed.")
except Exception as e:
    print(f"Error reversing mangle: {e}")
