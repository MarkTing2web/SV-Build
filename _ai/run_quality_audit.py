import re
import glob
import os

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

    # ── SEO ──
    seo = 0
    title = re.search(r'<title>([^<]+)</title>', content)
    if title and 20 < len(title.group(1)) < 70: seo += 2
    elif title: seo += 1
    desc = re.search(r'name=["\']description["\'][^>]*content=["\']([^"\']+)["\']', content)
    if not desc:
        desc = re.search(r'content=["\']([^"\']+)["\'][^>]*name=["\']description["\']', content)
    if desc and 50 < len(desc.group(1)) < 160: seo += 2
    elif desc: seo += 1
    if f'{slug}-feature-og.webp' in content: seo += 2
    elif 'securevision-insights.webp' not in content and 'og:image' in content: seo += 1
    if 'rel="canonical"' in content: seo += 1
    if re.search(r'<h1[^>]*>[^<]+</h1>', content): seo += 1
    if re.search(r'"datePublished"', content): seo += 1
    if '"@type": "Article"' in content: seo += 1
    scores_seo = min(seo, 10)

    # ── AEO ──
    aeo = 0
    if 'article-takeaways' in content:
        takeaways = re.findall(r'<li>[^<]{20,}</li>', content)
        if len(takeaways) >= 4: aeo += 3
        elif len(takeaways) >= 2: aeo += 1
    # FAQ detection — case insensitive, multiple formats
    has_faq = bool(re.search(r'<h[23][^>]*>[^<]*(?:FAQ|[Ff]requently\s+[Aa]sked)[^<]*</h[23]>', content))
    prose = re.search(r'<main[^>]*class=["\']prose["\'][^>]*>(.*?)</main>', content, re.DOTALL)
    prose_content = prose.group(1) if prose else ''
    h3_qs = re.findall(r'<h3[^>]*>[^<]*\?[^<]*</h3>', prose_content)
    strong_qs = re.findall(r'<p[^>]*>\s*<strong>[^<]*\?[^<]*</strong>\s*</p>', prose_content)
    if has_faq or len(h3_qs) >= 3 or len(strong_qs) >= 3:
        aeo += 3
        q_count = max(len(h3_qs), len(strong_qs))
        if q_count >= 10: aeo += 2
        elif q_count >= 5: aeo += 1
    if re.search(r'<h2[^>]*>\d+\.', content): aeo += 1
    if re.search(r'callout-box', content): aeo += 1
    scores_aeo = min(aeo, 10)

    # ── GEO ──
    geo = 0
    verdict_count = content.count('verdict-box')
    if verdict_count >= 3: geo += 3
    elif verdict_count >= 1: geo += 2
    if "Securevision's View" in content or "Securevision&#39;s View" in content: geo += 1
    if 'In Short' in content: geo += 1
    if '"author"' in content and 'Ler Wee Meng' in content: geo += 1
    if 'securevision-logo-blue.png' in content: geo += 1
    words = len(re.findall(r'\b\w+\b', re.sub(r'<[^>]+>', '', content)))
    if words >= 1500: geo += 2
    elif words >= 1000: geo += 1
    if re.search(r'Singapore|MCST|HDB|condo|landed', content): geo += 1
    scores_geo = min(geo, 10)

    # ── E-E-A-T ──
    eeat = 0
    if 'author-attribution' in content: eeat += 3
    if 'Founder &amp; Director' in content: eeat += 2
    if 'sv-years-experience' in content: eeat += 1
    if re.search(r'linkedin\.com/in/lerwm', content): eeat += 1
    if re.search(r'SCDF|PDPA|PLRD|BCA|bizSAFE|Police Licen', content): eeat += 1
    if 'Serving Singapore Since 2006' in content: eeat += 1
    if re.search(r'sv-licence|sv-bizsafe', content): eeat += 1
    scores_eeat = min(eeat, 10)

    overall = round((scores_seo + scores_aeo + scores_geo + scores_eeat) / 4, 1)
    results.append((slug, scores_seo, scores_aeo, scores_geo, scores_eeat, overall))

results.sort(key=lambda x: x[5], reverse=True)

lines = []
lines.append("# Insights Quality Audit v2")
lines.append("## SEO · AEO · GEO · E-E-A-T — After FAQ + In Short additions")
lines.append(f"## {len(results)} articles scored")
lines.append("")
lines.append("| Rank | Slug | SEO | AEO | GEO | E-E-A-T | Overall |")
lines.append("|---|---|---|---|---|---|---|")
for i, (slug, seo, aeo, geo, eeat, overall) in enumerate(results, 1):
    lines.append(f"| {i} | {slug} | {seo} | {aeo} | {geo} | {eeat} | **{overall}** |")

lines.append("")
seo_avg   = round(sum(r[1] for r in results) / len(results), 1)
aeo_avg   = round(sum(r[2] for r in results) / len(results), 1)
geo_avg   = round(sum(r[3] for r in results) / len(results), 1)
eeat_avg  = round(sum(r[4] for r in results) / len(results), 1)
ovr_avg   = round(sum(r[5] for r in results) / len(results), 1)

lines.append("## Dimension Averages")
lines.append("")
lines.append("| SEO | AEO | GEO | E-E-A-T | Overall |")
lines.append("|---|---|---|---|---|")
lines.append(f"| {seo_avg} | {aeo_avg} | {geo_avg} | {eeat_avg} | {ovr_avg} |")

with open(os.path.join(output_dir, "insights-quality-audit-v2.md"), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Articles scored:    {len(results)}")
print(f"SEO average:        {seo_avg}")
print(f"AEO average:        {aeo_avg}")
print(f"GEO average:        {geo_avg}")
print(f"E-E-A-T average:    {eeat_avg}")
print(f"Overall average:    {ovr_avg}")
print(f"Highest overall:    {results[0][0]} — {results[0][5]}")
print(f"Lowest overall:     {results[-1][0]} — {results[-1][5]}")
