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

    scores = {}

    # ── SEO ──
    seo = 0
    title = re.search(r'<title>([^<]+)</title>', content)
    if title and len(title.group(1)) < 70 and len(title.group(1)) > 20:
        seo += 2
    elif title:
        seo += 1
    desc = re.search(r'name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', content)
    if not desc:
        desc = re.search(r'content=["\']([^"\']+)["\'][^>]*name=["\']description["\']', content)
    if desc and 50 < len(desc.group(1)) < 160:
        seo += 2
    elif desc:
        seo += 1
    if f'{slug}-feature-og.webp' in content:
        seo += 2
    elif 'securevision-insights.webp' not in content and 'og:image' in content:
        seo += 1
    if 'rel="canonical"' in content:
        seo += 1
    if re.search(r'<h1[^>]*>[^<]+</h1>', content):
        seo += 1
    if re.search(r'"datePublished"', content):
        seo += 1
    if '"@type": "Article"' in content:
        seo += 1
    scores['seo'] = min(seo, 10)

    # ── AEO ──
    aeo = 0
    if 'article-takeaways' in content:
        takeaways = re.findall(r'<li>[^<]{20,}</li>', content)
        if len(takeaways) >= 4:
            aeo += 3
        elif len(takeaways) >= 2:
            aeo += 1
    faq_match = re.search(r'[Ff]requently asked', content)
    if faq_match:
        aeo += 3
        strong_qs = re.findall(r'<strong>[^<\?]+\?</strong>', content)
        if len(strong_qs) >= 10:
            aeo += 2
        elif len(strong_qs) >= 5:
            aeo += 1
    if re.search(r'<h2[^>]*>\d+\.', content):
        aeo += 1
    if re.search(r'callout-box', content):
        aeo += 1
    scores['aeo'] = min(aeo, 10)

    # ── GEO ──
    geo = 0
    verdict_count = content.count('verdict-box')
    if verdict_count >= 3:
        geo += 3
    elif verdict_count >= 1:
        geo += 2
    if "Securevision's View" in content or 'Securevision&#39;s View' in content:
        geo += 1
    if 'In Short' in content:
        geo += 1
    if '"author"' in content and 'Ler Wee Meng' in content:
        geo += 1
    if 'securevision-logo-blue.png' in content:
        geo += 1
    words = len(re.findall(r'\b\w+\b', re.sub(r'<[^>]+>', '', content)))
    if words >= 1500:
        geo += 2
    elif words >= 1000:
        geo += 1
    if re.search(r'Singapore|MCST|HDB|condo|landed', content):
        geo += 1
    scores['geo'] = min(geo, 10)

    # ── E-E-A-T ──
    eeat = 0
    if 'author-attribution' in content:
        eeat += 3
    if 'Founder &amp; Director' in content:
        eeat += 2
    if 'sv-years-experience' in content:
        eeat += 1
    if re.search(r'linkedin\.com/in/lerwm', content):
        eeat += 1
    if re.search(r'SCDF|PDPA|PLRD|BCA|bizSAFE|Police Licen', content):
        eeat += 1
    if 'Serving Singapore Since 2006' in content:
        eeat += 1
    if re.search(r'sv-licence|sv-bizsafe', content):
        eeat += 1
    scores['eeat'] = min(eeat, 10)

    overall = round((scores['seo'] + scores['aeo'] + scores['geo'] + scores['eeat']) / 4, 1)
    results.append((slug, scores, overall))

# Sort by overall score descending
results.sort(key=lambda x: x[2], reverse=True)

# Write report
lines = []
lines.append("# Insights Article Quality Audit")
lines.append("## SEO · AEO · GEO · E-E-A-T")
lines.append(f"## {len(results)} articles scored — June 2026")
lines.append("")
lines.append("Scores out of 10. Overall = average of 4 dimensions.")
lines.append("")
lines.append("| Rank | Slug | SEO | AEO | GEO | E-E-A-T | Overall |")
lines.append("|---|---|---|---|---|---|---|")

for i, (slug, scores, overall) in enumerate(results, 1):
    lines.append(
        f"| {i} | {slug} | {scores['seo']} | {scores['aeo']} | "
        f"{scores['geo']} | {scores['eeat']} | **{overall}** |"
    )

lines.append("")

# Summary stats
seo_avg = round(sum(r[1]['seo'] for r in results) / len(results), 1)
aeo_avg = round(sum(r[1]['aeo'] for r in results) / len(results), 1)
geo_avg = round(sum(r[1]['geo'] for r in results) / len(results), 1)
eeat_avg = round(sum(r[1]['eeat'] for r in results) / len(results), 1)
overall_avg = round(sum(r[2] for r in results) / len(results), 1)

lines.append("## Dimension Averages")
lines.append("")
lines.append(f"| SEO | AEO | GEO | E-E-A-T | Overall |")
lines.append(f"|---|---|---|---|---|")
lines.append(f"| {seo_avg} | {aeo_avg} | {geo_avg} | {eeat_avg} | {overall_avg} |")
lines.append("")

# Bottom 10
lines.append("## Bottom 10 — Lowest Overall Scores")
lines.append("")
for slug, scores, overall in results[-10:]:
    lines.append(f"- **{slug}** — Overall: {overall} (SEO:{scores['seo']} AEO:{scores['aeo']} GEO:{scores['geo']} E-E-A-T:{scores['eeat']})")

with open(os.path.join(output_dir, "insights-quality-audit.md"), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Report written to C:\\Projects\\SV-Build\\_ai\\insights-quality-audit.md")
print(f"Articles scored: {len(results)}")
print(f"Average overall score: {overall_avg}")
print(f"Highest: {results[0][0]} — {results[0][2]}")
print(f"Lowest:  {results[-1][0]} — {results[-1][2]}")
