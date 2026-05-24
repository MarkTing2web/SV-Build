import json

log_path = r'c:\Users\ler\.gemini\antigravity-ide\brain\b9918e31-fa1c-4fdf-977c-4c588c98b1cd\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('source') == 'USER_EXPLICIT' and 'content' in data:
                text = data['content']
                if 'Task F' in text or 'TASK F' in text or 'task f' in text.lower():
                    print("--- USER PROMPT ---")
                    print(text[:2000]) # First 2000 chars to see context
        except:
            pass
