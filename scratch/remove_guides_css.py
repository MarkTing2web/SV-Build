import os

root_dir = r'c:\Projects\SV-Build'
patterns = [
    '<link rel="stylesheet" href="/sv-guides.css">',
    '  <link rel="stylesheet" href="/sv-guides.css">',
    '<link rel="stylesheet" href="/sv-guides.css">\n',
    '  <link rel="stylesheet" href="/sv-guides.css">\n'
]

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            new_content = content
            for p in patterns:
                new_content = new_content.replace(p, '')
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated: {file_path}')
