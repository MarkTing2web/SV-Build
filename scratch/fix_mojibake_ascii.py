# fix_mojibake_ascii.py
import os

# Use hex escapes for everything to be safe
MOJIBAKE_MAP = {
    b'\xe2\x80\x94'.decode('latin-1'): '\u2014', # em dash
    b'\xe2\x80\x93'.decode('latin-1'): '\u2013', # en dash
    b'\xe2\x80\x98'.decode('latin-1'): '\u2018', # left single quote
    b'\xe2\x80\x99'.decode('latin-1'): '\u2019', # right single quote
    b'\xe2\x80\x9c'.decode('latin-1'): '\u201c', # left double quote
    b'\xe2\x80\x9d'.decode('latin-1'): '\u201d', # right double quote
    b'\xe2\x80\xa2'.decode('latin-1'): '\u2022', # bullet
    b'\xe2\x86\x92'.decode('latin-1'): '\u2192', # right arrow
    b'\xc2\xb7'.decode('latin-1'): '\u00b7',     # middle dot
}

directory = r'c:\Projects\SV-Build\insights'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        path = os.path.join(directory, filename)
        try:
            with open(path, 'rb') as f:
                content_bytes = f.read()
            
            # This is the tricky part. If it was saved as UTF-8 but the original 
            # characters were already corrupted into â€” sequences, 
            # then the bytes for â€” are C3 A2 E2\x82\xac\xe2\x80\x9d etc.
            
            content_text = content_bytes.decode('utf-8')
            for bad, good in MOJIBAKE_MAP.items():
                content_text = content_text.replace(bad, good)
            
            # Special case for double-corrupted characters
            content_text = content_text.replace('\u00c2\u00b7', '\u00b7')
            
            with open(path, 'w', encoding='utf-8', newline='\r\n') as f:
                f.write(content_text)
            print(f"Fixed: {filename}")
        except Exception as e:
            print(f"Error fixing {filename}: {e}")
