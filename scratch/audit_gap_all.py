import os
import re
import glob

insights_dir = r"C:\Projects\SV-Build\insights"
output_dir = r"C:\Projects\SV-Build\_ai"
os.makedirs(output_dir, exist_ok=True)

html_files = sorted(glob.glob(os.path.join(insights_dir, "*.html")))
results = []

for filepath in html_files:
    slug = os.path.basename(filepath).replace('.html', '')
    if slug == 'index':
        continue

    with open(filepath, encoding='utf-8', errors='ignore') as f:
        content = f.read()

    has_takeaways = "article-takeaways" in content
    has_in_short  = "In Short" in content
    has_faq       = bool(re.search(r'[Ff]requently asked', content))

    results.append((slug, has_takeaways, has_in_short, has_faq))

# Counts
missing_takeaways = [r[0] for r in results if not r[1]]
missing_in_short  = [r[0] for r in results if not r[2]]
missing_faq       = [r[0] for r in results if not r[3]]

# Articles missing ALL 3
missing_all = [r[0] for r in results if not r[1] and not r[2] and not r[3]]

# Articles missing at least 1
missing_any = [r[0] for r in results if not r[1] or not r[2] or not r[3]]

# Write report
lines = []
lines.append("# Insights Gap Audit — All 63 Articles")
lines.append("## Checking: Key Takeaways · In Short · FAQ")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append(f"| Element | ✅ Present | ❌ Missing |")
lines.append(f"|---|---|---|")
lines.append(f"| Key Takeaways | {len(results) - len(missing_takeaways)} | {len(missing_takeaways)} |")
lines.append(f"| In Short      | {len(results) - len(missing_in_short)} | {len(missing_in_short)} |")
lines.append(f"| FAQ           | {len(results) - len(missing_faq)} | {len(missing_faq)} |")
lines.append("")
lines.append(f"Articles missing ALL 3 elements: {len(missing_all)}")
lines.append(f"Articles missing at least 1 element: {len(missing_any)}")
lines.append("")

lines.append("## Full Article Status")
lines.append("")
lines.append("| Slug | Key Takeaways | In Short | FAQ | Gaps |")
lines.append("|---|---|---|---|---|")
for slug, kt, ins, faq in results:
    kt_str  = "✅" if kt  else "❌"
    ins_str = "✅" if ins else "❌"
    faq_str = "✅" if faq else "❌"
    gaps = sum([not kt, not ins, not faq])
    gaps_str = str(gaps) if gaps > 0 else "—"
    lines.append(f"| {slug} | {kt_str} | {ins_str} | {faq_str} | {gaps_str} |")

lines.append("")
lines.append("## Missing Key Takeaways")
for s in missing_takeaways:
    lines.append(f"- {s}")

lines.append("")
lines.append("## Missing In Short")
for s in missing_in_short:
    lines.append(f"- {s}")

lines.append("")
lines.append("## Missing FAQ")
for s in missing_faq:
    lines.append(f"- {s}")

lines.append("")
lines.append("## Missing ALL 3")
for s in missing_all:
    lines.append(f"- {s}")

with open(os.path.join(output_dir, "insights-gap-audit.md"), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Articles scanned:       {len(results)}")
print(f"Missing Key Takeaways:  {len(missing_takeaways)}")
print(f"Missing In Short:       {len(missing_in_short)}")
print(f"Missing FAQ:            {len(missing_faq)}")
print(f"Missing all 3:          {len(missing_all)}")
print(f"Missing at least 1:     {len(missing_any)}")
