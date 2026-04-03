import os

f = r"c:\Users\ler\OneDrive - Securevision Pte Ltd\1 SV Build\insights-how-to-choose-multi-door-access.html"
with open(f, 'r', encoding='utf-8') as file:
    content = file.read()

content = content.replace("Final CT", "Final CTA")
content = content.replace("dY\".", "📅")
content = content.replace("dY'", "💬")

with open(f, 'w', encoding='utf-8') as file:
    file.write(content)
