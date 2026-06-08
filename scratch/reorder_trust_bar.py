import os
import re

files = [
    "portfolio/condominiums/newton21-newton-condo.html",
    "portfolio/condominiums/the-lviv-newton-condo.html",
    "portfolio/condominiums/the-verte-telok-kurau-condo.html",
    "portfolio/condominiums/village-pasir-panjang-condo.html"
]

print("File | Trust bar line before fix | Hero closing tag line | Trust bar line after fix | Order correct")

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find trust bar block
        tb_match = re.search(r'<div\s+class="trust-bar"[^>]*>', content)
        if not tb_match:
            print(f"{filepath} | N/A | N/A | N/A | No")
            continue
            
        tb_start = tb_match.start()
        
        # Get line number before fix
        tb_line_before = content.count('\n', 0, tb_start) + 1
        
        # Find end of trust bar block
        div_count = 0
        current_idx = tb_start
        tb_end = -1
        while current_idx < len(content):
            next_open = content.find('<div', current_idx)
            next_close = content.find('</div', current_idx)
            
            if next_close == -1:
                break
                
            if next_open != -1 and next_open < next_close:
                div_count += 1
                current_idx = next_open + 4
            else:
                div_count -= 1
                current_idx = next_close + 5
                if div_count == 0:
                    tb_end = content.find('>', current_idx) + 1
                    break
                    
        if tb_end == -1:
            print(f"{filepath} | {tb_line_before} | N/A | N/A | No (Malformed)")
            continue
            
        # Extract trust bar block and remove it from content
        tb_block = content[tb_start:tb_end]
        
        # Let's remove the block and any immediate trailing whitespace to avoid double newlines
        trailing_whitespace_end = tb_end
        while trailing_whitespace_end < len(content) and content[trailing_whitespace_end] in [' ', '\t', '\n', '\r']:
            trailing_whitespace_end += 1
            
        content_without_tb = content[:tb_start] + content[trailing_whitespace_end:]
        
        # Find </header> in the content WITHOUT the trust bar
        header_end_idx = content_without_tb.find('</header>')
        if header_end_idx == -1:
            print(f"{filepath} | {tb_line_before} | N/A | N/A | No (No </header>)")
            continue
            
        header_end_tag_end = header_end_idx + len('</header>')
        
        # Original hero closing line
        hero_closing_line = content.count('\n', 0, content.find('</header>')) + 1
        
        # Insert trust bar block
        new_content = content_without_tb[:header_end_tag_end] + '\n\n' + tb_block + '\n' + content_without_tb[header_end_tag_end:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        # Read back to find new positions
        with open(filepath, 'r', encoding='utf-8') as f:
            final_content = f.read()
            
        tb_match_new = re.search(r'<div\s+class="trust-bar"[^>]*>', final_content)
        tb_line_after = final_content.count('\n', 0, tb_match_new.start()) + 1
        header_idx_new = final_content.find('<header')
        header_line_new = final_content.count('\n', 0, header_idx_new) + 1
        
        order_correct = "Yes" if tb_line_after > header_line_new else "No"
        
        print(f"{filepath} | {tb_line_before} | {hero_closing_line} | {tb_line_after} | {order_correct}")
        
    except Exception as e:
        print(f"{filepath} | Error | Error | Error | No")
