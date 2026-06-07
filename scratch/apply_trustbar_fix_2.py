import os
import re

files_5 = [
    "C:/Projects/SV-Build/systems/premises-security.html",
    "C:/Projects/SV-Build/systems/entry-access-control.html",
    "C:/Projects/SV-Build/systems/vehicle-lpr-management.html",
    "C:/Projects/SV-Build/systems/ip-phone-communications.html",
    "C:/Projects/SV-Build/systems/security-management-platform.html"
]

file_1 = "C:/Projects/SV-Build/systems/network-infrastructure.html"

def make_regex(text):
    # Escape special regex chars
    escaped = re.escape(text.strip())
    # Replace all literal whitespaces with \s+
    pattern = re.sub(r'\\\s+', r'\\s+', escaped) # replace escaped whitespace with \s+
    # Actually simpler: split by whitespace, escape each word, join with \s+
    words = text.split()
    escaped_words = [re.escape(w) for w in words]
    return re.compile(r'\s+'.join(escaped_words))

f1_5 = make_regex('<div class="sv-trust-bar">')
r1_5 = '<div class="trust-bar">'

f2_5 = make_regex('<div class="trust-flex-inline">')
r2_5 = '<div class="trust-bar-inner">'

f3_5 = make_regex("""<span>Police Licensed</span>
      <span class="sep">|</span>
      <span class="sv-bizsafe"></span>
      <span class="sep">|</span>
      <span>BCA Registered</span>
      <span class="sep">|</span>
      <span><span class="sv-sites"></span> Sites Protected</span>""")
r3_5 = """<span>Police Licensed</span>
      <span class="trust-divider">|</span>
      <span class="sv-bizsafe"></span>
      <span class="trust-divider">|</span>
      <span><strong class="sv-sites"></strong> Sites Protected</span>"""

# For file 6
f1_6 = make_regex('<div class="sv-trust-bar">')
r1_6 = '<div class="trust-bar">'

f2_6_inner = "N/A for file 6" # No inner class replacement requested for file 6 in Prompt

f3_6 = make_regex("""<span>BCA Registered</span>
          <span class="trust-divider">|</span>
          <span><strong class="sv-sites"></strong> Sites Protected</span>""")
r3_6 = """<span><strong class="sv-sites"></strong> Sites Protected</span>"""

report = "# Trust Bar Fix 2 — Completion Report\n\n"
report += "| File | sv-trust-bar replaced | inner class replaced | items updated |\n"
report += "|---|---|---|---|\n"

files_fully_updated = 0
not_found_list = []

all_files = files_5 + [file_1]

for filepath in all_files:
    filename = os.path.basename(filepath)
    if not os.path.exists(filepath):
        report += f"| {filename} | NOT FOUND | NOT FOUND | NOT FOUND |\n"
        not_found_list.append(f"{filename} (File not found)")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    status_1 = "NOT FOUND"
    status_2 = "NOT FOUND"
    status_3 = "NOT FOUND"

    is_file_6 = (filepath == file_1)

    if is_file_6:
        # f1_6
        if f1_6.search(content):
            content = f1_6.sub(r1_6, content)
            status_1 = "DONE"
        else:
            not_found_list.append(f"{filename} (sv-trust-bar)")
            
        status_2 = "N/A" # Not requested
        
        # f3_6
        if f3_6.search(content):
            # preserve leading whitespace? We can just do a simple sub.
            content = f3_6.sub(r3_6, content)
            status_3 = "DONE"
        else:
            not_found_list.append(f"{filename} (items updated)")
            
        if status_1 == "DONE" and status_3 == "DONE":
            files_fully_updated += 1
            
    else:
        if f1_5.search(content):
            content = f1_5.sub(r1_5, content)
            status_1 = "DONE"
        else:
            not_found_list.append(f"{filename} (sv-trust-bar)")
            
        if f2_5.search(content):
            content = f2_5.sub(r2_5, content)
            status_2 = "DONE"
        else:
            not_found_list.append(f"{filename} (inner class)")
            
        if f3_5.search(content):
            # We want to replace it but keep the indentation somewhat intact. sub() will replace exactly.
            content = f3_5.sub(r3_5, content)
            status_3 = "DONE"
        else:
            not_found_list.append(f"{filename} (items updated)")
            
        if status_1 == "DONE" and status_2 == "DONE" and status_3 == "DONE":
            files_fully_updated += 1
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # File 6 doesn't have an "inner class replaced" column in the prompt, but the table requires 3 columns
    if is_file_6:
        report += f"| {filename} | {status_1} | {status_2} | {status_3} |\n"
    else:
        report += f"| {filename} | {status_1} | {status_2} | {status_3} |\n"

report += f"\n## Summary\n"
report += f"- Files fully updated: {files_fully_updated}/6\n"
report += "- Any not found: "
if not_found_list:
    report += ", ".join(not_found_list) + "\n"
else:
    report += "None\n"

with open("C:/Projects/SV-Build/_ai/audit-trustbar-fix-2.md", "w", encoding='utf-8') as f:
    f.write(report)
    
print("Trust bar direct fixes applied.")
