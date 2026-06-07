import os
import re
from bs4 import BeautifulSoup, Comment

all_files = [
    "brands/aiphone-intercom.html",
    "brands/ajax-alarms.html",
    "brands/akuvox-access.html",
    "brands/akuvox-intercom.html",
    "brands/apollo-access.html",
    "brands/dahua-cctv.html",
    "brands/dormer-autogate.html",
    "brands/dsc-alarms.html",
    "brands/ebelco-locks.html",
    "brands/entrypass-entry-access.html",
    "brands/faac-autogate.html",
    "brands/fanvil-intercom.html",
    "brands/fanvil-ip-phone.html",
    "brands/gantrygo.html",
    "brands/ge-caddx-alarms.html",
    "brands/hanwha-cctv.html",
    "brands/hid-entry-access.html",
    "brands/hikcentral.html",
    "brands/hikvision-access.html",
    "brands/hikvision-cctv.html",
    "brands/hikvision-intercom.html",
    "brands/hrui-network.html",
    "brands/kocom-intercom.html",
    "brands/mag-autogate.html",
    "brands/microengine-entry-access.html",
    "brands/milesight-cctv.html",
    "brands/omada-network.html",
    "brands/paradox-alarms.html",
    "brands/risco-alarms.html",
    "brands/ruijie-reyee-network.html",
    "brands/suprema-entry-access.html",
    "brands/uniview-cctv.html",
    "brands/vesta.html",
    "brands/viro-locks.html",
    "brands/yealink-ip-phone.html",
    "brands/yeastar-ippbx.html",
    "brands/zkteco-cvsecurity.html",
    "brands/zkteco-entry-access.html"
]

base_dir = "C:/Projects/SV-Build"
audit_A = []
audit_B = []
audit_C = []
audit_D = []

for relpath in all_files:
    filepath = os.path.join(base_dir, relpath)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    inlines = soup.body.find_all(style=True) if soup.body else []
    for el in inlines:
        s = el['style']
        cls = el.get('class', [])
        if 'stat-bar-fill' in cls and re.match(r'^width\s*:\s*\d+%$', s.strip()): continue
        audit_A.append(f"{relpath}:{el.sourceline} -> style='{s}' on <{el.name}>")

    def extract_visible_text(s_obj):
        texts = []
        for text in s_obj.find_all(string=True):
            if text.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']: continue
            if isinstance(text, Comment): continue
            ss = text.strip()
            if ss: texts.append((text.parent.sourceline, ss, text.parent))
        return texts

    for line, text, parent in extract_visible_text(soup):
        if re.search(r'L/PS/', text):
            audit_B.append(f"{relpath}:{line}: L/PS/ licence number")

    if 'hero-solid' in html:
        audit_C.append(f"{relpath}: hero-solid found")

    if 'sv-wa-float' in html:
        audit_D.append(f"{relpath}: sv-wa-float found")

print("Remaining inline styles:", len(audit_A))
for x in audit_A: print(x)
print("Remaining licenses:", len(audit_B))
for x in audit_B: print(x)
print("Remaining hero-solid:", len(audit_C))
print("Remaining wa floats:", len(audit_D))
