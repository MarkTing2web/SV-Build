import os, glob
import re

files = [
    'guarding-technology-singapore.html',
    'how-to-choose-cctv-revised.html',
    'intercom-system-evolution-singapore.html',
    'is-my-security-system-still-working-revised.html',
    'maintain-burglar-alarm-revised.html',
    'maintenance-contract-revised.html',
    'managing-agents-guide-estate-security-systems-revised.html'
]

os.chdir(r'C:\Projects\SV-Build\insights')

for f in files:
    if not os.path.exists(f): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check for img inside callout-box or verdict-box
    callout_matches = re.finditer(r'<div class=\"(?:callout-box|verdict-box)\".*?>.*?</div>', content, re.DOTALL)
    for m in callout_matches:
        if '<img' in m.group(0):
            print(f'VIOLATION FOUND in {f}:\n', m.group(0)[:150])
