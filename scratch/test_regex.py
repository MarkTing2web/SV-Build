import sys
sys.stdout.reconfigure(encoding='utf-8')

import re
with open(r'C:\Projects\SV-Build\insights\choose-intercom-for-home.html', encoding='utf-8', errors='ignore') as f:
    content = f.read()
prose = re.search(r'<main[^>]*class=[\"\'`]prose[\"\'`][^>]*>(.*?)</main>', content, re.DOTALL)
if prose:
    h2s = re.findall(r'<h2[^>]*>([^<]+)</h2>', prose.group(1))
    for i, h in enumerate(h2s, 1):
        print(f'{i}. {h.strip()}')
