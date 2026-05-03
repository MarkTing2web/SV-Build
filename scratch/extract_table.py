import json
import os

log_path = r'C:\Users\ler\.gemini\antigravity\brain\36317c77-f316-4ebe-957d-bc7946eeeb52\.system_generated\logs\overview.txt'
output_path = r'c:\Projects\SV-Build\scratch\full_rewrite_table.md'

with open(log_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 82: # Line 83
            data = json.loads(line)
            content = data.get('content', '')
            # Find the Rewrite Table
            if 'Rewrite Table' in content:
                table_part = content.split('Rewrite Table')[1]
                with open(output_path, 'w', encoding='utf-8') as out:
                    out.write(table_part)
            break
