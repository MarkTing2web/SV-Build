import os
import re

workspace = r"c:\Projects\SV-Build"

tasks_A = [
    ("resources/calculators.html", "https://www.securevision.com.sg/resources/calculators/", "https://www.securevision.com.sg/resources/calculators.html"),
    ("resources/checklists.html", "https://www.securevision.com.sg/resources/checklists/", "https://www.securevision.com.sg/resources/checklists.html"),
    ("resources/faq.html", "https://www.securevision.com.sg/resources/faq/", "https://www.securevision.com.sg/resources/faq.html"),
    ("resources/guides.html", "https://www.securevision.com.sg/resources/guides/", "https://www.securevision.com.sg/resources/guides.html"),
    ("resources/library.html", "https://www.securevision.com.sg/resources/library/", "https://www.securevision.com.sg/resources/library.html"),
    ("resources/training-videos.html", "https://www.securevision.com.sg/resources/training-videos/", "https://www.securevision.com.sg/resources/training-videos.html")
]

for rel_path, old_str, new_str in tasks_A:
    full_path = os.path.join(workspace, rel_path)
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Only replace inside <link ... rel="canonical" ... >
        # We can construct the exact string we expect
        old_link = f'<link rel="canonical" href="{old_str}">'
        new_link = f'<link rel="canonical" href="{new_str}">'
        
        if old_link in content:
            content = content.replace(old_link, new_link)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {rel_path}")
        else:
            print(f"Skipped {rel_path} (string not found)")

task_B = ("insights/why-security-needs-managed-network.html", "https://www.securevision.com.sg/insights/why-security-system-needs-managed-network.html", "https://www.securevision.com.sg/insights/why-security-needs-managed-network.html")

rel_path, old_str, new_str = task_B
full_path = os.path.join(workspace, rel_path)
if os.path.exists(full_path):
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    old_link = f'<link rel="canonical" href="{old_str}">'
    new_link = f'<link rel="canonical" href="{new_str}">'
    if old_link in content:
        content = content.replace(old_link, new_link)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {rel_path}")
    else:
        print(f"Skipped {rel_path} (string not found)")
