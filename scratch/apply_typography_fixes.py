import os

files_5 = [
    "C:/Projects/SV-Build/systems/premises-security.html",
    "C:/Projects/SV-Build/systems/entry-access-control.html",
    "C:/Projects/SV-Build/systems/vehicle-lpr-management.html",
    "C:/Projects/SV-Build/systems/ip-phone-communications.html",
    "C:/Projects/SV-Build/systems/security-management-platform.html"
]
file_1 = "C:/Projects/SV-Build/systems/network-infrastructure.html"

find_5 = """<div class="sv-trust-bar">
  <div class="container">
    <div class="trust-flex-inline">
      <span>Police Licensed</span>
      <span class="sep">|</span>
      <span class="sv-bizsafe"></span>
      <span class="sep">|</span>
      <span>BCA Registered</span>
      <span class="sep">|</span>
      <span><span class="sv-sites"></span> Sites Protected</span>
    </div>
  </div>
</div>"""

replace_5 = """<div class="trust-bar">
  <div class="container">
    <div class="trust-bar-inner">
      <span>Police Licensed</span>
      <span class="trust-divider">|</span>
      <span class="sv-bizsafe"></span>
      <span class="trust-divider">|</span>
      <span><strong class="sv-sites"></strong> Sites Protected</span>
    </div>
  </div>
</div>"""

find_1 = """    <div class="sv-trust-bar">
      <div class="container">
        <div class="trust-bar-inner">
          <span>Police Licensed</span>
          <span class="trust-divider">|</span>
          <span class="sv-bizsafe"></span>
          <span class="trust-divider">|</span>
          <span>BCA Registered</span>
          <span class="trust-divider">|</span>
          <span><strong class="sv-sites"></strong> Sites Protected</span>
        </div>
      </div>
    </div>"""

replace_1 = """    <div class="trust-bar">
      <div class="container">
        <div class="trust-bar-inner">
          <span>Police Licensed</span>
          <span class="trust-divider">|</span>
          <span class="sv-bizsafe"></span>
          <span class="trust-divider">|</span>
          <span><strong class="sv-sites"></strong> Sites Protected</span>
        </div>
      </div>
    </div>"""

h4_headings = [
    "Premises Security",
    "Entry & Access",
    "Entry &amp; Access",
    "Vehicle Management",
    "Communications",
    "IP Network & Infrastructure",
    "IP Network &amp; Infrastructure",
    "Platform & Management",
    "Platform &amp; Management"
]

def process_file(filepath, is_network_infra=False):
    if not os.path.exists(filepath):
        return "NOT FOUND", "NOT FOUND"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change 1
    find_str = find_1 if is_network_infra else find_5
    replace_str = replace_1 if is_network_infra else replace_5
    
    # Try exact match first
    if find_str in content:
        content = content.replace(find_str, replace_str)
        c1_status = "DONE"
    else:
        # Sometimes line endings might be CRLF instead of LF
        find_str_crlf = find_str.replace('\n', '\r\n')
        replace_str_crlf = replace_str.replace('\n', '\r\n')
        if find_str_crlf in content:
            content = content.replace(find_str_crlf, replace_str_crlf)
            c1_status = "DONE"
        else:
            c1_status = "NOT FOUND — exact string not matched"

    # Change 2
    # Find <div class="arch-grid-3"> block and replace H4 with H3
    c2_status = "NOT FOUND"
    import re
    
    # The arch-grid-3 section usually ends at the closing </div> of the section or grid
    # A safer approach is to find `<div class="arch-grid-3">` and then replace only within that block
    # We can use regex to find the block
    pattern = re.compile(r'(class="arch-grid-3".*?)(</section>|<!--|</div>\s*</div>\s*</section>)', re.DOTALL)
    match = pattern.search(content)
    h4_replaced = 0
    
    if match:
        block = match.group(1)
        original_block = block
        
        for heading in h4_headings:
            find_h4 = f"<h4>{heading}</h4>"
            replace_h3 = f"<h3>{heading}</h3>"
            if find_h4 in block:
                block = block.replace(find_h4, replace_h3)
                h4_replaced += 1
                
        if h4_replaced > 0:
            content = content.replace(original_block, block)
            if h4_replaced == 6:
                c2_status = "DONE — 6 instances"
            else:
                c2_status = f"PARTIAL — {h4_replaced} instances"
    else:
        c2_status = "NOT FOUND"

    if c1_status == "DONE" or "DONE" in c2_status or "PARTIAL" in c2_status:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    return c1_status, c2_status, h4_replaced

report = """# Systems Typography Fix — Completion Report

## CSS Prerequisite Check
- .trust-bar: FOUND
- .trust-bar-inner: FOUND
- .trust-divider: FOUND

## Changes Applied

"""

total_trust_bar = 0
total_h4_files = 0
total_h4_instances = 0
not_found_list = []

all_files = files_5 + [file_1]
results = {}

for f in all_files:
    is_ni = (f == file_1)
    c1, c2, h4_count = process_file(f, is_ni)
    filename = os.path.basename(f)
    
    report += f"### {filename}\n"
    report += f"- Change 1 (trust bar): {c1}\n"
    report += f"- Change 2 (H4→H3): {c2}\n\n"
    
    if c1 == "DONE": total_trust_bar += 1
    elif "NOT FOUND" in c1: not_found_list.append(f"{filename} - Change 1")
    
    if "DONE" in c2: total_h4_files += 1
    elif "NOT FOUND" in c2: not_found_list.append(f"{filename} - Change 2")
    
    total_h4_instances += h4_count

report += "## Any strings not found:\n"
if not_found_list:
    for nf in not_found_list:
        report += f"- {nf}\n"
else:
    report += "None\n"

report += f"""
## Summary
- Trust bar updated: {total_trust_bar}/6 files
- H4→H3 fixed: {total_h4_files}/6 files
- Total H4 instances changed: {total_h4_instances} (expected 36)
"""

with open("C:/Projects/SV-Build/_ai/audit-systems-typography-fixes.md", "w", encoding='utf-8') as f:
    f.write(report)

print("Fixes applied and report generated.")
