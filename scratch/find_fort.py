with open('portfolio/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'fort-data' in line.lower() or 'data-centres/fort' in line.lower():
        print(f"Line {i+1}: {line.strip()}")
