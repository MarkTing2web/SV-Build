import re

file_path = r"d:\Ler Wee Meng\Project-Web\SV-Build\sv-shared.css"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. hero-compact
m_compact = re.search(r'\.hero-compact\s*{[^}]*min-height:\s*([^;]+);', content)
print(f"1. hero-compact min-height: {m_compact.group(1) if m_compact else 'NOT FOUND'}")

# 2. hero-standard
m_standard = re.search(r'\.hero-standard\s*{[^}]*min-height:\s*([^;]+);', content)
print(f"2. hero-standard min-height: {m_standard.group(1) if m_standard else 'NOT FOUND'}")

# 3. hero-full
m_full = re.search(r'\.hero-full\s*{[^}]*min-height:\s*([^;]+);', content)
print(f"3. hero-full min-height: {m_full.group(1) if m_full else 'NOT FOUND'}")

# 4. v2.9
has_v29 = "v2.9  June 2026      hero-compact min-height increased" in content
print(f"4. v2.9 entry present: {'Yes' if has_v29 else 'No'}")
