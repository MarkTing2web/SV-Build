import os
import re

base_dir = 'C:/Projects/SV-Build/'

files = [
    'systems/index.html',
    'systems/premises-security.html',
    'systems/entry-access-control.html',
    'systems/vehicle-lpr-management.html',
    'systems/ip-phone-communications.html',
    'systems/security-management-platform.html',
    'systems/network-infrastructure.html'
]

for f in files:
    full_path = os.path.join(base_dir, f)
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    match = re.search(r'<header[^>]*class="([^"]*)"[^>]*>', content)
    if match:
        print(f'{f}: {match.group(1)}')
    else:
        print(f'{f}: no header found')
