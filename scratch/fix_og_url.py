import os
import re

workspace = r"c:\Projects\SV-Build"

tasks = [
    ("resources/calculators.html", '<meta property="og:url" content="https://www.securevision.com.sg/resources/calculators/">', '<meta property="og:url" content="https://www.securevision.com.sg/resources/calculators.html">'),
    ("resources/checklists.html", '<meta property="og:url" content="https://www.securevision.com.sg/resources/checklists/">', '<meta property="og:url" content="https://www.securevision.com.sg/resources/checklists.html">'),
    ("resources/faq.html", '<meta property="og:url" content="https://www.securevision.com.sg/resources/faq/">', '<meta property="og:url" content="https://www.securevision.com.sg/resources/faq.html">'),
    ("resources/guides.html", '<meta property="og:url" content="https://www.securevision.com.sg/resources/guides/">', '<meta property="og:url" content="https://www.securevision.com.sg/resources/guides.html">'),
    ("resources/library.html", '<meta property="og:url" content="https://www.securevision.com.sg/resources/library/">', '<meta property="og:url" content="https://www.securevision.com.sg/resources/library.html">'),
    ("insights/why-security-needs-managed-network.html", '<meta property="og:url" content="https://www.securevision.com.sg/insights/why-security-system-needs-managed-network.html">', '<meta property="og:url" content="https://www.securevision.com.sg/insights/why-security-needs-managed-network.html">')
]

for rel_path, old_str, new_str in tasks:
    full_path = os.path.join(workspace, rel_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {rel_path}")
        else:
            print(f"Skipped {rel_path} (string not found)")
    else:
        print(f"File not found: {rel_path}")
