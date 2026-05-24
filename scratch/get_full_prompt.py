import json

log_path = r'c:\Users\ler\.gemini\antigravity-ide\brain\b9918e31-fa1c-4fdf-977c-4c588c98b1cd\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('source') == 'USER_EXPLICIT' and 'content' in data:
                text = data['content']
                if 'Full Fix Pass' in text and 'Condominiums Portfolio' in text:
                    with open(r'c:\Projects\SV-Build\scratch\full_condo_prompt.txt', 'w', encoding='utf-8') as out:
                        out.write(text)
        except:
            pass
