#!/usr/bin/env python3
"""
Securevision flipbook generator.

Turns a brochure PDF into a self-hosted flipbook page under /resources/brochures/.
Run from the SV-Build site root (needs poppler's pdftoppm/pdftotext + Pillow):

  python tools/flipbook/make_flipbook.py \
      --pdf "Securevision_Corporate_Profile.pdf" \
      --slug corporate-profile \
      --title "Securevision Corporate Profile" \
      --subtitle "Condominium Security & Integration" \
      --description "Flip through Securevision's corporate profile ..." \
      --summary "One-line description for the brochures hub card."

Writes:
  images/brochures/<slug>/pNN-{th,sm,lg}.webp
  resources/brochures/<slug>.html      (flipbook page)
  resources/brochures/<slug>.pdf       (download copy)
  resources/brochures.html             (hub, rebuilt from the registry)
  tools/flipbook/brochures.json        (registry of all brochures)
"""
import argparse, html, json, os, re, shutil, subprocess, sys, tempfile, glob
from datetime import date
from PIL import Image

SITE = "https://www.securevision.com.sg"

def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout

def esc(s): return html.escape(s, quote=True)

def render_pages(pdf, outdir):
    os.makedirs(outdir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        run(["pdftoppm", "-r", "200", "-png", pdf, os.path.join(tmp, "pg")])
        files = sorted(glob.glob(os.path.join(tmp, "pg-*.png")), key=lambda f: int(re.search(r"-(\d+)\.png$", f).group(1)))
        ratio = None
        for i, f in enumerate(files, 1):
            im = Image.open(f).convert("RGB")
            # Chromium PDFs have a fractional page width, leaving a blended 1-2px sliver on the right edge.
            im = im.crop((0, 0, im.width - 2, im.height - 1))
            ratio = im.width / im.height
            for tag, w in (("lg", 1400), ("sm", 700), ("th", 160)):
                h = round(im.height * w / im.width)
                im.resize((w, h), Image.LANCZOS).save(os.path.join(outdir, f"p{i:02d}-{tag}.webp"), "WEBP", quality=80 if tag != "th" else 70, method=6)
        return len(files), ratio

def page_texts(pdf, n):
    pages = []
    for i in range(1, n + 1):
        t = run(["pdftotext", "-f", str(i), "-l", str(i), pdf, "-"])
        lines = [re.sub(r"\s+", " ", l).strip() for l in t.splitlines()]
        pages.append(lines)
    # drop running headers/footers that repeat on most pages
    from collections import Counter
    c = Counter(l for p in pages for l in set(p) if l)
    repeated = {l for l, k in c.items() if k >= max(3, n // 2)}
    out = []
    for p in pages:
        paras, cur = [], []
        for l in p:
            if not l:
                if cur: paras.append(" ".join(cur)); cur = []
                continue
            if l in repeated: continue
            cur.append(l)
        if cur: paras.append(" ".join(cur))
        out.append(paras)
    return out

HEAD = """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">
  <link rel="shortcut icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
  <meta name="theme-color" content="#0056b3">
<title>{title_tag}</title>
<meta content="{desc}" name="description"/>
<link href="{canonical}" rel="canonical"/>
<meta content="{title_tag}" property="og:title"/>
<meta content="{desc}" property="og:description"/>
<meta name="twitter:description" content="{desc}" />
<meta content="{canonical}" property="og:url"/>
<meta content="{og_image}" property="og:image"/>
<meta content="website" property="og:type"/>
<meta content="Securevision" property="og:site_name"/>
<link href="/sv-shared.css" rel="stylesheet"/>
<link href="/sv-resources-v2.css" rel="stylesheet"/>
<link href="/sv-flipbook.css" rel="stylesheet"/>
<script src="/site-config.js"></script>
<script>
window.SV_PAGE = {{
  breadcrumbs: [
    {{ name: "Home", url: "{site}/" }},
    {{ name: "Resources", url: "{site}/resources/" }},
    {{ name: "Brochures", url: "{site}/resources/brochures" }}{crumb_tail}
  ]
}};
</script>
<script src="/sv-schema.js"></script>
<script type="application/ld+json">
{ld}
</script>
<style>
  :root {{ --page-accent: #0056b3; }}
  .hero-high-impact.hero {{ min-height: 0 !important; padding: 72px 0 52px !important; background: linear-gradient(135deg, #003d82 0%, #0e1a2b 100%) !important; }}
</style>
</head>
<body>
<nav id="sv-nav"></nav>
"""

TRUST_BREAD = """<div class="trust-bar">
<div class="container">
<div class="trust-bar-inner">
<span>Police Licensed · <span class="sv-licence"></span></span>
<span class="trust-divider"></span>
<span>bizSAFE <span class="sv-bizsafe"></span></span>
<span class="trust-divider"></span>
<span><strong class="sv-sites"></strong> Sites Protected</span>
</div>
</div>
</div>
<nav aria-label="Breadcrumb" class="sv-breadcrumb">
<div class="container">
<ul>
<li><a href="/">Home</a></li>
<li><a href="/resources/">Resources</a></li>
{bread}
</ul>
</div>
</nav>
"""

CTA = """<section class="cta-section cta-high-impact cta-property">
<div class="container">
<h2>Ready to Secure Your Property?</h2>
<p class="subtitle">Tell us about your site. We will assess it and design a system that works as one.</p>
<div class="btn-group">
<a class="btn btn-primary" href="/request-site-assessment-singapore?intent=brochures">Book a Site Assessment</a>
<a class="btn btn-outline-light" href="https://wa.me/6593860466">💬 WhatsApp</a>
</div>
<p class="cta-trust-note">Licensed by the Police Force: Licence <span class="sv-licence"></span> · Serving Singapore since 2006</p>
</div>
</section>
<footer id="sv-footer"></footer>
<script src="/nav-footer.js"></script>
<script src="/sv-search.js"></script>
"""

def build_viewer_page(b, n, ratio, texts):
    slug = b["slug"]
    url = f"{SITE}/resources/brochures/{slug}"
    pdf_url = f"/resources/brochures/{slug}.pdf"
    base = f"/images/brochures/{slug}/"
    alts = []
    for i, paras in enumerate(texts, 1):
        lead = paras[0][:80].rstrip(" .,;:") if paras else ""
        alts.append(f"{b['title']}, page {i} of {n}" + (f": {lead}" if lead else ""))
    cfg = {"base": base, "count": n, "ratio": round(ratio, 5), "title": b["title"], "pdf": pdf_url, "alts": alts}
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "WebPage", "name": b["title"], "url": url,
        "description": b["description"],
        "isPartOf": {"@type": "CollectionPage", "name": "Securevision Brochures", "url": f"{SITE}/resources/brochures"},
        "dateModified": date.today().isoformat(),
        "mainEntity": {"@type": "DigitalDocument", "name": b["title"], "encodingFormat": "application/pdf",
                       "url": SITE + pdf_url, "inLanguage": "en-GB",
                       "publisher": {"@type": "Organization", "name": "Securevision Pte Ltd", "url": SITE}}
    }, indent=2, ensure_ascii=False)
    s = HEAD.format(title_tag=esc(f"{b['title']} | Securevision Brochures"), desc=esc(b["description"]), canonical=url,
                    og_image=f"{SITE}{base}p01-lg.webp", site=SITE,
                    crumb_tail=f',\n    {{ name: {json.dumps(b["title"])} }}', ld=ld)
    s += f"""<header class="hero-high-impact hero">
<div class="container">
<span class="eyebrow-light">Resources · Brochures</span>
<h1 class="hero-title-main">{esc(b['title'])}</h1>
<p class="subtitle hero-subtitle-main">{esc(b.get('subtitle',''))}</p>
</div>
</header>
"""
    s += TRUST_BREAD.format(bread=f'<li><a href="/resources/brochures">Brochures</a></li>\n<li>{esc(b["title"])}</li>')
    s += f"""<main>
<section class="sv-section-white">
<div class="container">
<p style="font-size:15px;color:var(--text-gray);max-width:760px;margin:0 0 20px;">{esc(b['summary'])} Click a page, swipe, or use the arrow keys to turn the pages. On a phone, rotate to landscape or tap full screen for a larger view.</p>
<section class="fb" data-fb="{esc(json.dumps(cfg, ensure_ascii=False))}">
<noscript><p>This brochure needs JavaScript to flip through. <a href="{pdf_url}">Download the PDF instead.</a></p></noscript>
</section>
<details class="fb-text">
<summary>Read this brochure as text</summary>
"""
    for i, paras in enumerate(texts, 1):
        s += f"<h3>Page {i}</h3>\n" + "".join(f"<p>{esc(p)}</p>\n" for p in paras)
    s += """</details>
</div>
</section>
</main>
"""
    s += CTA + '<script src="/sv-flipbook.js" defer></script>\n</body>\n</html>\n'
    return s

def build_hub(items):
    url = f"{SITE}/resources/brochures"
    desc = "Securevision brochures you can flip through online: corporate profile and solution brochures for Singapore condominiums, homes and commercial properties."
    ld = json.dumps({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Securevision Brochures",
                     "description": desc, "url": url,
                     "provider": {"@type": "LocalBusiness", "name": "Securevision Pte Ltd", "url": SITE}}, indent=2)
    s = HEAD.format(title_tag="Brochures | Securevision Singapore", desc=esc(desc), canonical=url,
                    og_image=f"{SITE}/images/og-default.jpg", site=SITE, crumb_tail="", ld=ld)
    s = s.replace('<link href="/sv-flipbook.css" rel="stylesheet"/>\n', "")
    s += """<header class="hero-high-impact hero">
<div class="container">
<span class="eyebrow-light">Resources · Brochures</span>
<h1 class="hero-title-main">Brochures</h1>
<p class="subtitle hero-subtitle-main">Flip through our brochures online, or download the PDF to keep and share.</p>
</div>
</header>
"""
    s += TRUST_BREAD.format(bread="<li>Brochures</li>")
    s += '<main>\n<section class="sv-section-grey">\n<div class="container">\n<div class="grid-3" style="margin-top:0;gap:24px;">\n'
    for b in items:
        s += f"""<div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column;">
<a href="/resources/brochures/{b['slug']}" style="display:block;background:#0e1a2b;padding:20px;text-align:center;" aria-label="Open {esc(b['title'])}">
<img src="/images/brochures/{b['slug']}/p01-sm.webp" alt="Cover of {esc(b['title'])}" width="280" height="{round(280/b['ratio'])}" loading="lazy" style="max-width:100%;height:auto;box-shadow:0 8px 24px rgba(0,0,0,.4);">
</a>
<div style="padding:22px;display:flex;flex-direction:column;gap:10px;flex:1;">
<p style="font:700 11px 'Montserrat',sans-serif;text-transform:uppercase;letter-spacing:1.2px;color:var(--primary-blue);margin:0;">{b['pages']} pages</p>
<h2 style="font-size:20px;margin:0;">{esc(b['title'])}</h2>
<p style="font-size:14px;color:var(--text-gray);margin:0;line-height:1.55;">{esc(b['summary'])}</p>
<div class="btn-group" style="margin-top:auto;padding-top:8px;display:flex;flex-direction:row;flex-wrap:wrap;gap:10px;">
<a class="btn btn-primary" href="/resources/brochures/{b['slug']}">Flip through →</a>
<a class="btn btn-outline-dark" href="/resources/brochures/{b['slug']}.pdf" download>PDF</a>
</div>
</div>
</div>
"""
    s += "</div>\n</div>\n</section>\n</main>\n" + CTA + "</body>\n</html>\n"
    return s

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True); ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True); ap.add_argument("--subtitle", default="")
    ap.add_argument("--description", required=True); ap.add_argument("--summary", required=True)
    ap.add_argument("--root", default=".", help="site root (default: current directory)")
    a = ap.parse_args()
    root = a.root
    imgdir = os.path.join(root, "images", "brochures", a.slug)
    n, ratio = render_pages(a.pdf, imgdir)
    texts = page_texts(a.pdf, n)
    os.makedirs(os.path.join(root, "resources", "brochures"), exist_ok=True)
    shutil.copyfile(a.pdf, os.path.join(root, "resources", "brochures", a.slug + ".pdf"))
    b = {"slug": a.slug, "title": a.title, "subtitle": a.subtitle, "description": a.description,
         "summary": a.summary, "pages": n, "ratio": round(ratio, 5)}
    reg_path = os.path.join(root, "tools", "flipbook", "brochures.json")
    os.makedirs(os.path.dirname(reg_path), exist_ok=True)
    reg = json.load(open(reg_path, encoding="utf-8")) if os.path.exists(reg_path) else []
    reg = [r for r in reg if r["slug"] != a.slug] + [b]
    json.dump(reg, open(reg_path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    open(os.path.join(root, "resources", "brochures", a.slug + ".html"), "w", encoding="utf-8").write(build_viewer_page(b, n, ratio, texts))
    open(os.path.join(root, "resources", "brochures.html"), "w", encoding="utf-8").write(build_hub(reg))
    print(f"OK: {n} pages -> {imgdir}")

if __name__ == "__main__":
    main()
