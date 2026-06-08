import os
import re
from bs4 import BeautifulSoup

REPO_ROOT = r"C:\Projects\SV-Build"

FORM_PAGES = {
    "contact.html",
    "request-site-assessment-singapore.html",
    "book-assessment.html",
    "book-site-assessment.html",
    "contact-gateway.html",
}

SUCCESS_PAGES = {
    "thank-you.html",
    "success.html",
    "confirmation.html",
    "booking-success.html",
    "contact-success.html",
    "thank-you-booking.html",
    "thank-you-proposal.html",
}

SEO_DATA = {
    "index.html": {
        "title": "Security Systems & Solutions Singapore | Securevision",
        "desc": "Securevision delivers expert security systems in Singapore. Explore our CCTV, access control, intercom, and alarm solutions for your property."
    },
    "about.html": {
        "title": "About Securevision Singapore | Trusted Security Experts",
        "desc": "Learn about Securevision Singapore. With over 15 years of experience, we provide premier security solutions and reliable systems integration across the island."
    },
    "contact.html": {
        "title": "Contact Securevision Singapore | Security Systems Support",
        "desc": "Get in touch with Securevision Singapore for expert advice, quotes, or support on your security systems. Our specialists are ready to assist you."
    },
    "privacy.html": {
        "title": "Privacy Policy | Securevision Singapore Security Systems",
        "desc": "Read the Privacy Policy of Securevision Singapore. We are committed to protecting your personal data and ensuring secure communication for all our clients."
    },
    "terms.html": {
        "title": "Terms of Service | Securevision Singapore Security Systems",
        "desc": "Review the Terms of Service for Securevision Singapore. Understand the terms, conditions, and policies governing our security installations and services."
    },
    "sitemap.html": {
        "title": "Website Sitemap | Securevision Singapore Security Systems",
        "desc": "Navigate the Securevision Singapore website easily with our comprehensive sitemap. Find all our security solutions, insights, portfolio, and contact pages."
    },
    "request-site-assessment-singapore.html": {
        "title": "Book a Site Assessment in Singapore | Securevision",
        "desc": "Book a comprehensive security site assessment with Securevision Singapore. Our experts will evaluate your property and recommend the best security solutions."
    },
    "contact-gateway.html": {
        "title": "Contact Gateway in Singapore | Securevision Systems",
        "desc": "Choose the best way to connect with Securevision Singapore. Request a formal proposal, chat with us on WhatsApp, or speak directly to a security specialist."
    }
}

def clean_inline_styles(soup):
    for tag in soup.find_all(style=True):
        st = tag['style'].lower()
        new_classes = []
        if 'padding-top: 68px' in st or 'padding-top:68px' in st:
            new_classes.append('pt-68')
        if 'margin-bottom: 64px' in st or 'margin-bottom:64px' in st:
            new_classes.append('mb-64')
        if 'margin-bottom: 80px' in st or 'margin-bottom:80px' in st:
            new_classes.append('mb-80')
        if 'margin-bottom: 32px' in st or 'margin-bottom:32px' in st:
            new_classes.append('mb-32')
        if 'margin-bottom: 24px' in st or 'margin-bottom:24px' in st:
            new_classes.append('mb-24')
        if 'margin-bottom: 40px' in st or 'margin-bottom:40px' in st:
            new_classes.append('mb-40')
        if 'margin-bottom: 48px' in st or 'margin-bottom:48px' in st:
            new_classes.append('mb-48')
        if 'display: block' in st or 'display:block' in st:
            new_classes.append('d-block')
            
        if new_classes:
            tag['class'] = tag.get('class', []) + new_classes
            
        del tag['style']

def fix_seo(soup, fname):
    data = SEO_DATA.get(fname)
    if not data:
        return

    # Title
    title_tag = soup.find("title")
    if not title_tag:
        title_tag = soup.new_tag("title")
        if soup.head: soup.head.insert(0, title_tag)
    title_tag.string = data['title']

    # Meta Description
    desc_meta = soup.find("meta", attrs={"name": "description"})
    if not desc_meta:
        desc_meta = soup.new_tag("meta", attrs={"name": "description", "content": ""})
        if title_tag: title_tag.insert_after(desc_meta)
    desc_meta["content"] = data['desc']

    # OG Title
    og_title = soup.find("meta", property="og:title")
    if not og_title:
        og_title = soup.new_tag("meta", property="og:title", content="")
        if desc_meta: desc_meta.insert_after(og_title)
    og_title["content"] = data['title']

    # OG Description
    og_desc = soup.find("meta", property="og:description")
    if not og_desc:
        og_desc = soup.new_tag("meta", property="og:description", content="")
        if og_title: og_title.insert_after(og_desc)
    og_desc["content"] = data['desc']

    # Canonical
    canon = soup.find("link", rel="canonical")
    canon_url = f"https://www.securevision.com.sg/{fname}" if fname != "index.html" else "https://www.securevision.com.sg/"
    if not canon:
        canon = soup.new_tag("link", rel="canonical", href=canon_url)
        if og_desc: og_desc.insert_after(canon)
    canon["href"] = canon_url

    # OG URL
    og_url = soup.find("meta", property="og:url")
    if not og_url:
        og_url = soup.new_tag("meta", property="og:url", content=canon_url)
        if og_desc: og_desc.insert_after(og_url)
    og_url["content"] = canon_url

    # OG Image
    og_img = soup.find("meta", property="og:image")
    if not og_img:
        og_img = soup.new_tag("meta", property="og:image", content="https://www.securevision.com.sg/images/hero-security-solutions-singapore.webp")
        if og_url: og_url.insert_after(og_img)

def fix_file(filepath):
    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    
    # 1. HTML lang
    if soup.html:
        soup.html["lang"] = "en-GB"

    # 2. CSS Ordering
    sheets = soup.find_all("link", rel="stylesheet")
    head = soup.head
    if sheets and head:
        # Remove bad sheets
        for s in sheets:
            if any(x in s.get("href", "") for x in ("sv-solutions", "sv-insights")):
                s.decompose()
        
        # Ensure sv-shared is first, sv-forms is present if needed
        shared_sheet = soup.find("link", href=re.compile(r"sv-shared\.css"))
        if shared_sheet:
            shared_sheet.decompose()
            
        new_shared = soup.new_tag("link", rel="stylesheet", href="/sv-shared.css")
        current_sheets = soup.find_all("link", rel="stylesheet")
        if current_sheets:
            current_sheets[0].insert_before(new_shared)
        else:
            head.append(new_shared)
        
        if fname in FORM_PAGES:
            form_sheet = soup.find("link", href=re.compile(r"sv-forms\.css"))
            if not form_sheet:
                new_form = soup.new_tag("link", rel="stylesheet", href="/sv-forms.css")
                current_sheets = soup.find_all("link", rel="stylesheet")
                if current_sheets:
                    current_sheets[0].insert_after(new_form)
                else:
                    head.append(new_form)

    # 3. Clean <style>
    for style in soup.find_all("style"):
        style.decompose()

    # 4. SEO Updates
    fix_seo(soup, fname)

    # 5. Clean Inline Styles
    clean_inline_styles(soup)

    # 6. Hero Classes
    if fname in ("about.html", "contact.html"):
        header = soup.find("header")
        if header:
            classes = header.get("class", [])
            if "hero-high-impact" not in classes:
                classes.append("hero-high-impact")
            if "hero-compact" not in classes and "hero-standard" not in classes:
                classes.append("hero-compact")
            if "hero-about" in classes:
                classes.remove("hero-about")
            header["class"] = classes
            
            h1 = header.find("h1")
            if h1:
                h1_classes = h1.get("class", [])
                if "hero-title-main" not in h1_classes:
                    h1_classes.append("hero-title-main")
                h1["class"] = h1_classes

    # 7. Trust Bar & Breadcrumb (about.html)
    if fname == "about.html":
        # Inject Breadcrumb
        nav = soup.find("nav", id="sv-nav")
        if nav and not soup.find("nav", class_="sv-breadcrumb"):
            bc = BeautifulSoup('''
<!-- ── BREADCRUMB ── -->
<nav class="sv-breadcrumb" aria-label="Breadcrumb">
  <div class="container">
    <ul>
      <li><a href="/">Home</a></li>
      <li>About Securevision</li>
    </ul>
  </div>
</nav>''', "html.parser")
            nav.insert_after(bc)
            
        # Inject Trust Bar
        header = soup.find("header")
        if header and not soup.find(class_=re.compile(r"trust-bar")):
            tb = BeautifulSoup('''
<!-- TRUST BAR -->
<div class="trust-bar">
    <div class="container">
        <div class="trust-bar-inner">
            <span class="trust-item"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg> Police Licensed <span class="sv-licence"></span></span>
            <span class="trust-divider"></span>
            <span class="trust-item"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> <span class="sv-bizsafe"></span></span>
            <span class="trust-divider"></span>
            <span class="trust-item"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg> Over <strong class="sv-sites">1,000+</strong> Sites</span>
        </div>
    </div>
</div>''', "html.parser")
            header.insert_after(tb)

    # 8. Hardcodes (wa-float, Police Licence)
    wa = soup.find(class_=re.compile(r"wa-float"))
    if wa:
        wa.decompose()
        
    html_text = str(soup)
    # Fix remaining hardcoded police licences (outside of trust-bar)
    html_text = re.sub(r'L/PS/\d{6}/\d{4}P', r'<span class="sv-licence"></span>', html_text)
    # Fix hardcoded bizsafe
    html_text = re.sub(r'bizSAFE Level 3', r'<span class="sv-bizsafe"></span>', html_text)
    
    # 9. Heading Skips
    # Find all h3/h4 that skip a level
    # Simple regex replace for known issues
    if fname in ("contact-gateway.html", "contact.html", "request-site-assessment-singapore.html"):
        html_text = re.sub(r'<h3([^>]*)>Direct Chat</h3>', r'<h2\1>Direct Chat</h2>', html_text)
        html_text = re.sub(r'<h3([^>]*)>Proposal Request</h3>', r'<h2\1>Proposal Request</h2>', html_text)
        html_text = re.sub(r'<h3([^>]*)>Speak to a Specialist</h3>', r'<h2\1>Speak to a Specialist</h2>', html_text)
        html_text = re.sub(r'<h3([^>]*)>WhatsApp</h3>', r'<h2\1>WhatsApp</h2>', html_text)
        html_text = re.sub(r'<h3([^>]*)>1. How should we connect\?</h3>', r'<h2\1>1. How should we connect?</h2>', html_text)
        
    if fname in ("index.html", "privacy.html", "contact.html"):
        html_text = re.sub(r'<h4([^>]*)>Site Assessment</h4>', r'<h3\1>Site Assessment</h3>', html_text)
        html_text = re.sub(r'<h4([^>]*)>Enquiries and Feedback</h4>', r'<h3\1>Enquiries and Feedback</h3>', html_text)
        html_text = re.sub(r'<h4([^>]*)>Office Address</h4>', r'<h3\1>Office Address</h3>', html_text)

    soup = BeautifulSoup(html_text, "html.parser")
    
    # 10. Nav-footer script ordering for thank-you pages
    if fname in SUCCESS_PAGES:
        scripts = soup.body.find_all("script") if soup.body else []
        nav_footer = None
        for s in scripts:
            if s.get("src", "").endswith("nav-footer.js"):
                nav_footer = s.extract()
        
        if nav_footer and soup.body:
            soup.body.append(nav_footer)

    with open(filepath, "w", encoding="utf-8") as f:
        # Use str() to prevent BS4 from aggressively reformatting everything
        f.write(str(soup))


def main():
    file_list = [f for f in os.listdir(REPO_ROOT) if f.endswith(".html") and os.path.isfile(os.path.join(REPO_ROOT, f))]
    for f in file_list:
        print(f"Fixing {f}...")
        fix_file(os.path.join(REPO_ROOT, f))
    print("Done!")

if __name__ == "__main__":
    main()
