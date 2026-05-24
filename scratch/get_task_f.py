import json

log_path = r'c:\Users\ler\.gemini\antigravity-ide\brain\b9918e31-fa1c-4fdf-977c-4c588c98b1cd\.system_generated\logs\transcript.jsonl'
full_text = ""

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if 'content' in data and data['content']:
                full_text += data['content'] + "\n"
        except:
            pass

idx = full_text.find('TASK F')
if idx != -1:
    print(full_text[max(0, idx-200):idx+2000])
else:
    print("TASK F not found")
