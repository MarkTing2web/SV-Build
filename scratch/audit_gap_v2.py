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

    # 1. Key Takeaways
    has_takeaways = "article-takeaways" in content

    # 2. In Short
    has_in_short = "In Short" in content

    # 3. FAQ — multiple detection methods
    # Method A: H2 or H3 containing FAQ/frequently asked (case-insensitive)
    faq_heading = bool(re.search(
        r'<h[23][^>]*>[^<]*(?:FAQ|[Ff]requently\s+[Aa]sked)[^<]*</h[23]>',
        content
    ))

    # Method B: 3+ H3 questions in prose section
    prose = re.search(r'<main[^>]*class=["\']prose["\'][^>]*>(.*?)</main>', content, re.DOTALL)
    prose_content = prose.group(1) if prose else ''
    h3_questions = re.findall(r'<h3[^>]*>[^<]*\?[^<]*</h3>', prose_content)

    # Method C: 3+ <p><strong> questions
    strong_questions = re.findall(r'<p[^>]*>\s*<strong>[^<]*\?[^<]*</strong>\s*</p>', prose_content)

    has_faq = (
        faq_heading or
        len(h3_questions) >= 3 or
        len(strong_questions) >= 3
    )

    # Count FAQ questions for reporting
    faq_q_count = max(len(h3_questions), len(strong_questions))
    if faq_heading and faq_q_count == 0:
        # FAQ heading found but questions in different format — mark as present
        faq_q_count = "heading only"

    results.append((slug, has_takeaways, has_in_short, has_faq, faq_q_count))

# Counts
missing_takeaways = [r[0] for r in results if not r[1]]
missing_in_short  = [r[0] for r in results if not r[2]]
missing_faq       = [r[0] for r in results if not r[3]]
missing_any       = [r[0] for r in results if not r[1] or not r[2] or not r[3]]
complete          = [r[0] for r in results if r[1] and r[2] and r[3]]

# Write report
lines = []
lines.append("# Insights Gap Audit v2 — All 63 Articles")
lines.append("## Checking: Key Takeaways · In Short · FAQ (corrected detection)")
lines.append("")
lines.append("## Summary")
lines.append("")
lines.append(f"| Element | ✅ Present | ❌ Missing |")
lines.append(f"|---|---|---|")
lines.append(f"| Key Takeaways | {len(results) - len(missing_takeaways)} | {len(missing_takeaways)} |")
lines.append(f"| In Short      | {len(results) - len(missing_in_short)} | {len(missing_in_short)} |")
lines.append(f"| FAQ           | {len(results) - len(missing_faq)} | {len(missing_faq)} |")
lines.append("")
lines.append(f"Articles fully complete (0 gaps): {len(complete)}")
lines.append(f"Articles missing at least 1 element: {len(missing_any)}")
lines.append("")

lines.append("## Full Article Status")
lines.append("")
lines.append("| Slug | Key Takeaways | In Short | FAQ | FAQ Q count | Gaps |")
lines.append("|---|---|---|---|---|---|")
for slug, kt, ins, faq, faq_count in results:
    kt_str  = "✅" if kt  else "❌"
    ins_str = "✅" if ins else "❌"
    faq_str = "✅" if faq else "❌"
    gaps = sum([not kt, not ins, not faq])
    gaps_str = str(gaps) if gaps > 0 else "—"
    lines.append(f"| {slug} | {kt_str} | {ins_str} | {faq_str} | {faq_count} | {gaps_str} |")

lines.append("")
lines.append("## Missing Key Takeaways")
if missing_takeaways:
    for s in missing_takeaways:
        lines.append(f"- {s}")
else:
    lines.append("None — all 63 articles have Key Takeaways ✅")

lines.append("")
lines.append("## Missing In Short")
if missing_in_short:
    for s in missing_in_short:
        lines.append(f"- {s}")
else:
    lines.append("None ✅")

lines.append("")
lines.append("## Missing FAQ")
if missing_faq:
    for s in missing_faq:
        lines.append(f"- {s}")
else:
    lines.append("None ✅")

lines.append("")
lines.append("## Fully Complete Articles")
for s in complete:
    lines.append(f"- {s}")

with open(os.path.join(output_dir, "insights-gap-audit-v2.md"), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Articles scanned:          {len(results)}")
print(f"Missing Key Takeaways:     {len(missing_takeaways)}")
print(f"Missing In Short:          {len(missing_in_short)}")
print(f"Missing FAQ:               {len(missing_faq)}")
print(f"Fully complete:            {len(complete)}")
print(f"Missing at least 1:        {len(missing_any)}")
