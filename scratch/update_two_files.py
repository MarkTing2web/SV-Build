import os
import re

base_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build"

# FILE 1: cpf-maxwell-institution.html
file1 = os.path.join(base_dir, "portfolio/institutions/cpf-maxwell-institution.html")
with open(file1, "r", encoding="utf-8") as f:
    content1 = f.read()

# Change 1: cs-grid
content1 = content1.replace('<div class="cs-grid">', '<div class="grid-2 mt-40">')
content1 = re.sub(r'<div class="cs-col-head challenge">.*?</div>', r'<h3>Challenges</h3>', content1, flags=re.DOTALL)
content1 = re.sub(r'<div class="cs-col-head solution">.*?</div>', r'<h3>Solutions Implemented</h3>', content1, flags=re.DOTALL)

# remove cs-items wrapper
content1 = re.sub(r'<div class="cs-items">\s*(.*?)\s*</div>\s*</div>\s*<div>', r'\1\n      </div>\n      <div>', content1, flags=re.DOTALL)
content1 = re.sub(r'<div class="cs-items">\s*(.*?)\s*</div>\s*</div>\s*</div>', r'\1\n      </div>\n    </div>', content1, flags=re.DOTALL)
# wait, removing `<div class="cs-items">` and its closing div is tricky with regex. Let's do it carefully.
# In the original file, it was:
# <div>
#   <div class="cs-col-head challenge">Challenges</div>
#   <div class="cs-items">
#     <div class="cs-item c-item">...</div> ...
#   </div>
# </div>
# The regex above might be too brittle. Let's do a more robust approach.
content1 = content1.replace('<div class="cs-items">', '')
# And we need to remove the matching </div> for cs-items.
# It is located right before the closing </div> of the column.
content1 = content1.replace('          </div>\n        </div>\n      </div>', '        </div>\n      </div>')
content1 = content1.replace('          </div>\n        </div>\n      <div>', '        </div>\n      <div>')
# Actually, the simplest is to just regex away the `<div class="cs-items">` and we know there are exactly two `</div>` that need to be removed (one for each cs-items). Let's see.
# Let's just remove `<div class="cs-item c-item">` and its closing `</div>` first.
content1 = re.sub(r'<div class="cs-item c-item">\s*(.*?)\s*</div>', r'\1', content1, flags=re.DOTALL)
content1 = re.sub(r'<div class="cs-item s-item">\s*(.*?)\s*</div>', r'\1', content1, flags=re.DOTALL)

# Let's fix the </div> mismatch by parsing or specific replace.
# The original structure:
#       <div>
#         <div class="cs-col-head challenge">Challenges</div>
#         <div class="cs-items">
#           ... items ...
#         </div>
#       </div>
# After replacing the wrappers:
#       <div>
#         <h3>Challenges</h3>
#           ... items ...
#         </div>
#       </div>
# Notice we removed `<div class="cs-items">` but left its `</div>`. We should remove exactly two `</div>`s that correspond to cs-items.
content1 = content1.replace('        </div>\n      </div>\n      <div>', '      </div>\n      <div>')
content1 = content1.replace('        </div>\n      </div>\n    </div>\n  </div>\n</section>', '      </div>\n    </div>\n  </div>\n</section>')

# Change 2: dual-grid and dual-card
content1 = content1.replace('<div class="dual-grid">', '<div class="grid-2 mt-40">')
content1 = content1.replace('<div class="dual-card members">', '<div class="card p-32">')
content1 = content1.replace('<div class="dual-card officers">', '<div class="card p-32">')
content1 = content1.replace('<div class="dual-card">', '<div class="card p-32">')

# Change 3: impact classes
content1 = content1.replace('<div class="impact-strip">', '<div class="grid-3 mt-40">')
content1 = content1.replace('<div class="impact-card">', '<div class="portfolio-result-card">')
content1 = re.sub(r'<span class="impact-val">(.*?)</span>', r'<h4 class="portfolio-result-title">\1</h4>', content1, flags=re.DOTALL)
content1 = re.sub(r'<span class="impact-desc">(.*?)</span>', r'<p class="portfolio-result-text">\1</p>', content1, flags=re.DOTALL)

with open(file1, "w", encoding="utf-8") as f:
    f.write(content1)

# Verification for FILE 1
legacy_classes = ["cs-grid", "cs-col-head", "cs-items", "cs-item", "dual-grid", "dual-card", "impact-strip", "impact-card", "impact-val", "impact-desc"]
found_legacy1 = [c for c in legacy_classes if c in content1]
print("FILE 1:")
print(f"1,2,3. Legacy classes remaining: {found_legacy1 if found_legacy1 else 'None'}")


# FILE 2: siglap-bank-landed-home.html
file2 = os.path.join(base_dir, "portfolio/residential/siglap-bank-landed-home.html")
with open(file2, "r", encoding="utf-8") as f:
    content2 = f.read()

# Change 1: Remove literal \n
content2 = content2.replace('\\n\n', '')
content2 = content2.replace('\\n', '')

# Change 2: Remove duplicate old breadcrumb
# The second one looks like:
# <!-- ═══ BREADCRUMB ═══ -->
# <nav class="sv-breadcrumb sv-section-grey">
# ...
# </nav>
breadcrumb_pattern = re.compile(r'<!-- ═══ BREADCRUMB ═══ -->\s*<nav class="sv-breadcrumb sv-section-grey".*?</nav>', re.DOTALL | re.IGNORECASE)
content2 = breadcrumb_pattern.sub('', content2)

with open(file2, "w", encoding="utf-8") as f:
    f.write(content2)

# Verification for FILE 2
b_count_nodes = content2.count('<nav class="sv-breadcrumb"')
has_literal_n = '\\n' in content2
b_levels = 0
b_match = re.search(r'<nav class="sv-breadcrumb"[^>]*>.*?</nav>', content2, re.DOTALL)
if b_match:
    b_levels = b_match.group(0).count('<li>')

print("\nFILE 2:")
print(f"1. Only one breadcrumb: {'Yes' if b_count_nodes == 1 else 'No (' + str(b_count_nodes) + ')'}")
print(f"2. Literal \\n remaining: {'Yes' if has_literal_n else 'No'}")
print(f"3. Breadcrumb levels: {b_levels}")
