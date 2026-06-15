import os

filepath = r"d:\Ler Wee Meng\Project-Web\SV-Build\site-config.js"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (
        'tags: ["maintenance","contract","sla","service"]',
        'tags: ["maintenance","contract","sla","service"], excerpt: "A maintenance contract is not the same as a warranty. Most disputes arise not from bad faith but from misread scope — a client expecting four-hour response against a contract that commits only to next-business-day."'
    )
]

for old_str, new_str in replacements:
    if old_str in content:
        content = content.replace(old_str, new_str)
    else:
        print(f"Warning: String not found: {old_str}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final replacement complete.")
