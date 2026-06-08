import re

filepath = r"d:\Ler Wee Meng\Project-Web\SV-Build\portfolio\index.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace card-foot CSS
old_css = """.card-foot {
    border-top: 1px solid #f1f5f9;
    padding: 15px 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #fbfcfd;
}"""

new_css = """.card-foot {
    border-top: 1px solid #f1f5f9;
    padding: 15px 25px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    background: #fbfcfd;
}"""

if old_css in content:
    content = content.replace(old_css, new_css)
else:
    print("Warning: old_css not found")

# Function to remove elements safely
# loc
content = re.sub(r'<div\s+class="loc"\s*>.*?</div>', '', content, flags=re.DOTALL)
# tag-row
content = re.sub(r'<div\s+class="tag-row"\s*>.*?</div>', '', content, flags=re.DOTALL)
# c-date
content = re.sub(r'<span\s+class="c-date"\s*>.*?</span>', '', content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

# Verify
cards = re.findall(r'<a[^>]*class="[^"]*project-card[^"]*"', content)
loc_count = len(re.findall(r'<div\s+class="loc"', content))
tag_count = len(re.findall(r'<div\s+class="tag-row"', content))
cdate_count = len(re.findall(r'<span\s+class="c-date"', content))

print(f"1. Total <a class=\"project-card\"> elements processed (expected: 52): {len(cards)}")
print(f"2. Confirm zero <div class=\"loc\"> elements remain inside #pGrid: {loc_count}")
print(f"3. Confirm zero <div class=\"tag-row\"> elements remain inside #pGrid: {tag_count}")
print(f"4. Confirm zero <span class=\"c-date\"> elements remain inside #pGrid: {cdate_count}")
print(f"5. Confirm .card-foot justify-content value is flex-start in the style block: {'Yes' if new_css in content else 'No'}")
