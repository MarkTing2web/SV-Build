import os
import re

guides_dir = r"d:\Ler Wee Meng\Project-Web\SV-Build\resources\guides"
output_file = r"d:\Ler Wee Meng\Project-Web\SV-Build\_ai\resources-quality-audit.md"

results = []
read_errors = []

for fname in os.listdir(guides_dir):
    if not fname.endswith(".html"):
        continue
    if fname == "index.html":
        continue

    slug = fname.replace(".html", "")
    try:
        with open(os.path.join(guides_dir, fname), encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        read_errors.append(f"{fname}: {str(e)}")
        continue

    scores = {}

    # ── SEO ──
    seo = 0
    if re.search(r'<title>[^<]{10,}</title>', content):
        title_match = re.search(r'<title>([^<]+)</title>', content)
        if title_match and re.search(r'CCTV|access|alarm|gate|intercom|telephone|wifi|network|renovation|contractor|security|Singapore', title_match.group(1), re.IGNORECASE):
            seo += 2
    meta_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content)
    if meta_desc and 120 <= len(meta_desc.group(1)) <= 160:
        seo += 2
    if re.search(r'<link\s+rel=["\']canonical["\']', content):
        seo += 1
    h1_matches = re.findall(r'<h1[^>]*>(.+?)</h1>', content, re.DOTALL)
    if len(h1_matches) == 1 and re.search(r'CCTV|access|alarm|gate|intercom|telephone|wifi|network|renovation|contractor|security|Singapore', h1_matches[0], re.IGNORECASE):
        seo += 2
    h2_count = len(re.findall(r'<h2[^>]*>', content))
    if h2_count >= 4:
        seo += 1
    if 'application/ld+json' in content:
        seo += 1
    internal_links = len(re.findall(r'href=["\']/', content))
    if internal_links >= 3:
        seo += 1
    scores['seo'] = min(seo, 10)

    # ── AEO ──
    aeo = 0
    if re.search(r'Key Takeaways|rg-callout', content, re.IGNORECASE):
        aeo += 2
    if re.search(r'Frequently Asked|rg-faq|FAQ', content, re.IGNORECASE):
        aeo += 2
        faq_qs = re.findall(r'<(?:h3|strong|dt)[^>]*>[^<]*\?[^<]*</(?:h3|strong|dt)>', content)
        if len(faq_qs) >= 5:
            aeo += 1
        if len(faq_qs) >= 1:
            aeo += 1
    if re.search(r'<h2[^>]*>\d+\.', content):
        aeo += 1
    if re.search(r'rg-callout|rg-recommendation', content):
        aeo += 1
    # Snippet-ready: short <p> tags under 200 chars
    short_ps = [p for p in re.findall(r'<p[^>]*>([^<]{20,200})</p>', content) if '?' not in p]
    if len(short_ps) >= 5:
        aeo += 2
    elif len(short_ps) >= 2:
        aeo += 1
    scores['aeo'] = min(aeo, 10)

    # ── GEO ──
    geo = 0
    rec_count = len(re.findall(r'rg-recommendation', content))
    if rec_count >= 2:
        geo += 3
    elif rec_count >= 1:
        geo += 2
    if re.search(r'rg-verdict', content):
        geo += 2
    if 'Ler Wee Meng' in content:
        geo += 1
    if '"author"' in content and 'Ler Wee Meng' in content:
        geo += 1
    words = len(re.findall(r'\b\w+\b', re.sub(r'<[^>]+>', '', content)))
    if words >= 1500:
        geo += 2
    elif words >= 1000:
        geo += 1
    sg_terms = len(re.findall(r'Singapore|MCST|HDB|condo|landed|Managing Agent|estate', content))
    if sg_terms >= 2:
        geo += 1
    scores['geo'] = min(geo, 10)

    # ── E-E-A-T ──
    eeat = 0
    if re.search(r'author-attribution|rg-author', content):
        eeat += 2
    if 'Founder &amp; Director' in content or 'Founder & Director' in content:
        eeat += 1
    if re.search(r'37.{0,20}year|year.{0,20}experience', content, re.IGNORECASE):
        eeat += 1
    if 'linkedin.com' in content:
        eeat += 1
    if re.search(r'SCDF|PDPA|PLRD|BCA|bizSAFE|Police Licen', content):
        eeat += 2
    if re.search(r'\bwe\b.{0,40}\brecommend\b|\bwe have\b|\bin our experience\b|\bwe\b.{0,20}\bseen\b', content, re.IGNORECASE):
        eeat += 2
    if re.search(r'since 2006|established 2006|Serving Singapore Since 2006', content, re.IGNORECASE):
        eeat += 1
    scores['eeat'] = min(eeat, 10)

    overall = round((scores['seo'] + scores['aeo'] + scores['geo'] + scores['eeat']) / 4, 1)
    results.append((slug, scores, overall))

# Sort by overall score descending
results.sort(key=lambda x: x[2], reverse=True)

# Write report
lines = []
lines.append("# Resources Guides Quality Audit")
lines.append("## SEO · AEO · GEO · E-E-A-T")
lines.append(f"## {len(results)} guides scored — June 2026")
lines.append("")
lines.append("Scores out of 10. Overall = average of 4 dimensions.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## RANKED RESULTS")
lines.append("")
lines.append(f"| Rank | Guide | SEO | AEO | GEO | E-E-A-T | Overall |")
lines.append(f"|---|---|---|---|---|---|---|")

for i, (slug, scores, overall) in enumerate(results, 1):
    lines.append(
        f"| {i} | {slug} | {scores['seo']} | {scores['aeo']} | {scores['geo']} | {scores['eeat']} | **{overall}** |"
    )

lines.append("")
lines.append("---")
lines.append("")
lines.append("## PER-GUIDE DETAIL")
lines.append("")

for slug, scores, overall in results:
    lines.append(f"### {slug}")
    lines.append(f"**Overall: {overall}/10**")
    lines.append("")
    lines.append(f"- SEO: {scores['seo']}/10")
    lines.append(f"- AEO: {scores['aeo']}/10")
    lines.append(f"- GEO: {scores['geo']}/10")
    lines.append(f"- E-E-A-T: {scores['eeat']}/10")
    lines.append("")

if read_errors:
    lines.append("---")
    lines.append("")
    lines.append("## READ ERRORS")
    lines.append("")
    for err in read_errors:
        lines.append(f"- {err}")
    lines.append("")

output = "\n".join(lines)
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "w", encoding="utf-8") as f:
    f.write(output)

print(f"Done. {len(results)} guides scored.")
print(f"Report saved to: {output_file}")
