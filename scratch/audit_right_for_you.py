import re, os, glob

# Scan entire solutions folder including subfolders
files = sorted(glob.glob("solutions/**/*.html", recursive=True))
# Exclude portfolio-index and known orphans
exclude = ["portfolio-index.html"]

results = []
for path in files:
    if any(e in path for e in exclude):
        continue
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    has_yes = bool(re.search(r'This Is For You If', content))
    has_no  = bool(re.search(r'You May Not Need This Yet If', content))

    if not (has_yes and has_no):
        continue

    yes_card = re.search(
        r'<div class="([^"]*card[^"]*)"[^>]*>\s*(?:<[^/][^>]*>\s*)*<h3>This Is For You If',
        content, re.S)
    no_card = re.search(
        r'<div class="([^"]*card[^"]*)"[^>]*>\s*(?:<[^/][^>]*>\s*)*<h3>You May Not Need This Yet If',
        content, re.S)

    yes_cls = yes_card.group(1) if yes_card else "NOT FOUND"
    no_cls  = no_card.group(1) if no_card else "NOT FOUND"

    yes_ok = "card--featured" in yes_cls
    no_ok  = yes_ok or no_cls == "card"

    status = "OK" if (yes_ok and no_cls == "card") else "NEEDS FIX"
    results.append((status, path, yes_cls, no_cls))
    print(f"[{status}]  {path}")
    print(f"       'This Is For You':  \"{yes_cls}\"")
    print(f"       'You May Not Need': \"{no_cls}\"")
    print()

needs_fix = [r for r in results if r[0] == "NEEDS FIX"]
print(f"--- Summary: {len(results)} pages with this section, {len(needs_fix)} need fixing ---")
