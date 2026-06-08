import os
import re
import json
from bs4 import BeautifulSoup, Comment

repo_root = r"c:\Projects\SV-Build"
insights_dir = os.path.join(repo_root, "insights")

# Global dict to store titles for cannibalisation check
all_titles = {}

# Words to check
british_english_flags = ["authorization", "optimization", "labor", "center", "program", "license"]
superlatives = ["best", "leading", "most advanced", "top"]
sg_context = ["HDB", "MCST", "BCA", "URA", "NEA", "MOM"]

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def check_geo_signals(text):
    text_lower = text.lower()
    words = text_lower.split()
    first_100 = " ".join(words[:100])
    has_sv = "securevision" in first_100
    has_sg = "singapore" in text_lower
    has_proof = bool(re.search(r'\d+%|\$|2,000|bizsafe|bca|police licence', text_lower))
    return has_sv, has_sg, has_proof

def audit_file(filepath):
    filename = os.path.basename(filepath)
    slug = filename.replace('.html', '')
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    issues = []
    strengths = []
    
    def add_issue(desc, sev, impact, fix, fix_lvl, code=""):
        issues.append({
            "desc": desc, "severity": sev, "impact": impact, 
            "fix": fix, "fix_level": fix_lvl, "code": code
        })

    # 1. HEAD METADATA
    title_tag = soup.find('title')
    title_text = title_tag.text.strip() if title_tag else ""
    if title_text:
        all_titles[filename] = title_text
        if len(title_text) < 50 or len(title_text) > 60:
            add_issue("Title is not 50-60 characters", "Medium", "SEO", "Adjust title length", "Page HTML", title_text)
        if "Singapore" not in title_text:
            add_issue("Title missing 'Singapore'", "Medium", "SEO", "Add 'Singapore' to title", "Page HTML", title_text)
    else:
        add_issue("Missing <title>", "Critical", "SEO", "Add <title>", "Page HTML")

    desc_tag = soup.find('meta', attrs={'name': 'description'})
    if desc_tag:
        desc_len = len(desc_tag.get('content', ''))
        if desc_len < 120 or desc_len > 160:
            add_issue("Meta description not 120-160 characters", "Medium", "SEO", "Adjust description length", "Page HTML", desc_tag.get('content'))
    else:
        add_issue("Missing meta description", "High", "SEO", "Add meta description", "Page HTML")

    canon = soup.find('link', rel='canonical')
    expected_canon = f"https://www.securevision.com.sg/insights/{slug}.html"
    if not canon or canon.get('href') != expected_canon:
        add_issue("Canonical URL incorrect or missing", "High", "SEO", f"Set canonical to {expected_canon}", "Page HTML", canon.get('href') if canon else "")

    og_title = soup.find('meta', property='og:title')
    if not og_title: add_issue("Missing og:title", "High", "SEO", "Add og:title", "Page HTML")
    
    og_desc = soup.find('meta', property='og:description')
    if not og_desc: add_issue("Missing og:description", "High", "SEO", "Add og:description", "Page HTML")
    
    og_img = soup.find('meta', property='og:image')
    if not og_img: 
        add_issue("Missing og:image", "High", "SEO", "Add og:image", "Page HTML")
    elif "-rel.webp" not in og_img.get('content', ''):
        add_issue("og:image does not use -rel.webp variant", "Low", "SEO", "Update og:image to -rel.webp", "Page HTML", og_img.get('content'))
        
    og_url = soup.find('meta', property='og:url')
    if not og_url: add_issue("Missing og:url", "High", "SEO", "Add og:url", "Page HTML")

    schemas = soup.find_all('script', type='application/ld+json')
    has_article_schema = False
    has_dates = False
    for schema in schemas:
        try:
            data = json.loads(schema.string)
            if data.get('@type') in ['Article', 'BlogPosting']:
                has_article_schema = True
                if 'datePublished' in data and 'dateModified' in data:
                    has_dates = True
        except:
            pass
    if not has_article_schema:
        add_issue("Missing Article schema", "Medium", "SEO", "Add JSON-LD Article schema", "Page HTML")
    elif not has_dates:
        add_issue("Schema missing datePublished or dateModified", "Low", "SEO", "Add dates to schema", "Page HTML")

    # 2. CSS LOAD ORDER
    css_files = [link.get('href', '') for link in soup.find_all('link', rel='stylesheet')]
    js_files = [script.get('src', '') for script in soup.find_all('script') if script.get('src')]
    
    if '/sv-shared.css' not in css_files:
        add_issue("Missing /sv-shared.css", "Critical", "UX", "Add /sv-shared.css", "Page HTML")
    if '/sv-insights.css' not in css_files:
        add_issue("Missing /sv-insights.css", "Critical", "UX", "Add /sv-insights.css", "Page HTML")
    if soup.find('form') and '/sv-forms.css' not in css_files:
        add_issue("Missing /sv-forms.css when form is present", "High", "UX", "Add /sv-forms.css", "Page HTML")
        
    if '/site-config.js' not in js_files:
        add_issue("Missing /site-config.js", "Critical", "Architecture", "Add /site-config.js", "Page HTML")
    if '/nav-footer.js' not in js_files:
        add_issue("Missing /nav-footer.js", "Critical", "Architecture", "Add /nav-footer.js", "Page HTML")

    # 3. HERO
    hero = soup.find(class_=re.compile(r'hero'))
    if not hero:
        add_issue("No hero section found", "Critical", "UX", "Add hero section", "Page HTML")
    else:
        if 'hero-compact' not in hero.get('class', []):
            add_issue("Hero doesn't use hero-compact", "High", "UX", "Use hero-compact class", "HTML class")
        
    h1s = soup.find_all('h1')
    if len(h1s) == 0:
        add_issue("Missing H1", "Critical", "SEO", "Add one H1", "Page HTML")
    elif len(h1s) > 1:
        add_issue("Multiple H1s found", "Critical", "SEO", "Ensure only one H1 on the page", "Page HTML")
        
    if hero and not hero.find('p', class_='lead'):
        # heuristic for lead paragraph
        has_lead = False
        for p in hero.find_all('p'):
            if 'lead' in p.get('class', []): has_lead = True
        if not has_lead:
            add_issue("Hero missing lead paragraph", "Medium", "Conversion", "Add lead paragraph to hero", "Page HTML")

    # 4. TRUST BAR
    trust_bar = soup.find(class_=re.compile(r'trust-bar|trust'))
    if not trust_bar:
        add_issue("Trust bar absent", "Critical", "Trust", "Add standard verbatim trust bar", "Page HTML")
    else:
        tb_text = trust_bar.text.lower()
        if 'police licence' not in tb_text: add_issue("Trust bar missing Police Licence", "High", "Trust", "Add Police Licence", "Page HTML")
        if 'bizsafe' not in tb_text: add_issue("Trust bar missing bizSAFE", "High", "Trust", "Add bizSAFE", "Page HTML")
        if 'bca' not in tb_text: add_issue("Trust bar missing BCA", "High", "Trust", "Add BCA", "Page HTML")

    # 5. BREADCRUMB
    breadcrumbs = soup.find(class_=re.compile(r'breadcrumb'))
    if not breadcrumbs:
        add_issue("Breadcrumb absent", "High", "UX", "Add breadcrumbs", "Page HTML")
    else:
        links = breadcrumbs.find_all('a')
        if len(links) > 0 and links[0].get('href') != '/':
            add_issue("Breadcrumb Home link is not /", "High", "Architecture", "Link Home to /", "Page HTML")

    # 6. ARTICLE BODY
    body_text = soup.get_text()
    for b_word in british_english_flags:
        if b_word in body_text.lower().split():
            add_issue(f"American English used: {b_word}", "Medium", "Trust", "Change to British English", "Page HTML", b_word)

    for s_word in superlatives:
        if s_word in body_text.lower().split():
            add_issue(f"Superlative used without evidence: {s_word}", "Medium", "Trust", "Remove superlative or add evidence", "Page HTML", s_word)

    # 7. AUTHOR BIO STRIP
    bio = soup.find(class_=re.compile(r'author-bio|author'))
    if not bio:
        add_issue("Author bio strip absent", "High", "Trust", "Add author bio strip", "Page HTML")

    # 8. RELATED INSIGHTS
    related_links = 0
    related_section = soup.find(class_=re.compile(r'related'))
    if related_section:
        related_links = len(related_section.find_all('a'))
    if related_links < 3:
        add_issue("Related Insights absent or fewer than 3", "High", "UX", "Add min 3 related insights", "Page HTML")

    # 9. CTA SECTION
    ctas = soup.find_all('a', class_=re.compile(r'btn-primary'))
    has_cta_proposal = False
    for c in ctas:
        if 'request a proposal' in c.text.lower():
            has_cta_proposal = True
    if not has_cta_proposal:
        add_issue("CTA 'Request a Proposal' absent", "Critical", "Conversion", "Add CTA section with btn-primary", "Page HTML")

    # 10. ARCHITECTURE
    nav = soup.find('nav', id='sv-nav')
    if not nav:
        add_issue("Missing <nav id='sv-nav'>", "Critical", "Architecture", "Add standard nav wrapper", "Page HTML")
    elif len(nav.find_all()) > 0:
        add_issue("Hardcoded nav HTML present", "Critical", "Architecture", "Remove hardcoded nav", "Page HTML")

    footer = soup.find('footer', id='sv-footer')
    if not footer:
        add_issue("Missing <footer id='sv-footer'>", "Critical", "Architecture", "Add standard footer wrapper", "Page HTML")
    elif len(footer.find_all()) > 0:
        add_issue("Hardcoded footer HTML present", "Critical", "Architecture", "Remove hardcoded footer", "Page HTML")

    # Absolute paths
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src and not src.startswith('/') and not src.startswith('http'):
            add_issue("Image src not absolute", "High", "Architecture", "Use absolute path", "Page HTML", src)
        if not img.get('alt'):
            add_issue("Missing alt text on image", "Medium", "SEO", "Add alt text", "Page HTML", src)

    # 11. GEO SIGNALS
    has_sv, has_sg, has_proof = check_geo_signals(body_text)
    if not has_sg: add_issue("No Singapore-specific context", "Medium", "SEO", "Add Singapore context", "Page HTML")
    
    # Calculate Scores
    total_issues = len(issues)
    criticals = len([i for i in issues if i['severity'] == 'Critical'])
    highs = len([i for i in issues if i['severity'] == 'High'])
    
    ux_score = max(0, 10 - criticals*2 - highs)
    seo_score = max(0, 10 - criticals*2 - highs)
    conv_score = max(0, 10 - criticals*2 - highs)
    trust_score = max(0, 10 - criticals*2 - highs)
    consistency = max(0, 10 - criticals*2 - highs)
    
    # Sort issues by severity
    sev_map = {"Critical": 1, "High": 2, "Medium": 3, "Low": 4}
    issues.sort(key=lambda x: sev_map.get(x['severity'], 5))
    
    report = []
    report.append("### 1. Page Identity")
    report.append(f"- File path: `{filepath}`")
    report.append("- Page type: Insights article")
    report.append("- Primary audience: MCST / Facility Managers")
    report.append(f"- Primary keyword / topic: {title_text}")
    report.append("- Primary conversion goal: Request a Proposal")
    
    report.append("\n### 2. Summary Assessment")
    if criticals > 0:
        report.append("This page has critical structural issues that need immediate attention.")
    else:
        report.append("This page is well-structured and aligns well with the guidelines.")
        
    report.append("\n### 3. Strengths")
    if criticals == 0: report.append("- Clean HTML structure")
    if has_sg: report.append("- Good local Singapore context")
    if has_proof: report.append("- Includes trust signals and proof points")
    if len(report) == 7: report.append("- Standard template followed")
    
    report.append("\n### 4. Issues Identified")
    for i in issues:
        report.append(f"- **Issue:** {i['desc']}")
        report.append(f"  - **Severity:** {i['severity']}")
        report.append(f"  - **Impact:** {i['impact']}")
        report.append(f"  - **Recommended Fix:** {i['fix']}")
        report.append(f"  - **Fix Level:** {i['fix_level']}")
        if i['code']: report.append(f"  - **Suggested code:** `{i['code']}`")
        
    report.append("\n### 5. Scores (out of 10)")
    report.append(f"- UX Score: [{ux_score}/10] — Programmatic heuristic")
    report.append(f"- Consistency Score: [{consistency}/10] — Programmatic heuristic")
    report.append(f"- Conversion Score: [{conv_score}/10] — Programmatic heuristic")
    report.append(f"- Trust Score: [{trust_score}/10] — Programmatic heuristic")
    report.append(f"- SEO Score: [{seo_score}/10] — Programmatic heuristic")
    
    report.append("\n### 6. Priority Fix List")
    report.append("| Priority | Issue | Fix Level | Estimated Effort |")
    report.append("|---|---|---|---|")
    for i in issues:
        report.append(f"| {i['severity']} | {i['desc']} | {i['fix_level']} | Low |")
        
    report.append("\n### 7. Content Quality Assessment")
    report.append("- **Tone:** Cannot be fully evaluated via script. Needs human review.")
    report.append("- **Specificity:** Cannot be fully evaluated via script.")
    report.append("- **Utility:** Cannot be fully evaluated via script.")
    report.append(f"- **GEO Readiness:** Singapore Context: {has_sg}, SV in first 100: {has_sv}, Proof points: {has_proof}")
    report.append("- **Cannibalisation Risk:** Checked at the end of report.")
    report.append("- **Recommended Enhancement:** Fix critical structural issues first.")
    
    report.append("\n---\n")
    return "\n".join(report)

if __name__ == "__main__":
    out_file = r"C:\Users\ler\.gemini\antigravity-ide\brain\dc4d6fca-626f-43e9-8606-63c5190c142f\artifacts\insights-audit-report.md"
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    
    all_reports = ["# Securevision Insights Bulk Audit Report\n\n"]
    
    for root, dirs, files in os.walk(insights_dir):
        for f in files:
            if f.endswith('.html') and f != 'index.html':
                filepath = os.path.join(root, f)
                all_reports.append(audit_file(filepath))
                
    # Basic cannibalisation check (word overlap in titles)
    all_reports.append("\n## Cannibalisation Risk Analysis (Title Overlap)")
    titles_list = list(all_titles.items())
    for i in range(len(titles_list)):
        for j in range(i+1, len(titles_list)):
            f1, t1 = titles_list[i]
            f2, t2 = titles_list[j]
            words1 = set(t1.lower().split())
            words2 = set(t2.lower().split())
            common = words1.intersection(words2)
            if len(common) > 4: # heuristics
                all_reports.append(f"- **{f1}** and **{f2}** share keywords: {', '.join(common)}")

    with open(out_file, 'w', encoding='utf-8') as out:
        out.write("\n".join(all_reports))
        
    print(f"Audit completed. Report generated at {out_file}")
