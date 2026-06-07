import os

base_dir = r"c:\Projects\SV-Build"

portfolio_css = """
/* WAVE 2 PORTFOLIO ADDITIONS */
.portfolio-card-icon { width: 14px; height: 14px; display: inline-block; vertical-align: middle; margin-right: 4px; }
.portfolio-card-tag { font-size: 0.8rem; color: #3182ce; font-weight: 700; margin-top: 12px; }
.portfolio-hub-hero { padding: 160px 0 100px; background-size: cover; background-position: center; color: #fff; text-align: left; }
.portfolio-hub-eyebrow { color: #63b3ed; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; display: block; margin-bottom: 20px; }
.portfolio-hub-title { font-family: 'Outfit', sans-serif; font-size: clamp(2.5rem, 6vw, 4.5rem); margin-bottom: 20px; max-width: 900px; text-align: left; }
.portfolio-hub-subtitle { font-size: 1.5rem; font-weight: 600; margin-bottom: 24px; color: #cbd5e1; max-width: 800px; margin-left: 0; text-align: left; padding: 0; }
.portfolio-hub-desc { font-size: 1.15rem; opacity: 0.95; max-width: 900px; margin: 0 0 48px; line-height: 1.8; color: #e2e8f0; text-align: left; }
.portfolio-hub-cta-row { display: flex; justify-content: flex-start; gap: 20px; }
.portfolio-overview-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start; }
.portfolio-systems-list { margin-top: 24px; display: flex; flex-direction: column; gap: 12px; }
.portfolio-system-link { display: flex; align-items: center; gap: 12px; padding: 16px 20px; background: var(--bg-light); border-radius: 8px; text-decoration: none; color: var(--text-dark); font-weight: 600; font-size: 14px; border: 1px solid var(--border-light); transition: 0.2s; }
.portfolio-system-link:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
.portfolio-result-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; margin: 48px 0; }
.portfolio-result-stat { font-family: 'Montserrat', sans-serif; font-size: 48px; font-weight: 800; color: var(--primary-blue); margin-bottom: 8px; }
.portfolio-related-link { display: block; text-decoration: none; }
.portfolio-read-more { color: var(--primary-blue); font-weight: 600; font-size: 13px; margin-top: 16px; display: block; }
"""

brands_css = """
/* WAVE 2 BRANDS ADDITIONS */
.brand-contact-card { display: flex; align-items: center; gap: 20px; flex-wrap: wrap; background: #fff; border: 1.5px solid #CBD5E0; border-left: 4px solid var(--primary-blue); border-radius: 10px; padding: 20px 24px; }
.brand-contact-icon { font-size: 24px; flex-shrink: 0; }
.brand-contact-body { flex: 1; min-width: 200px; }
.brand-contact-name { font-family: 'Montserrat', sans-serif; font-size: 13px; font-weight: 700; color: var(--text-dark); margin: 0 0 4px; }
.brand-contact-detail { font-family: 'Inter', sans-serif; font-size: 13px; color: var(--text-light); margin: 0; }
.brand-contact-cta { white-space: nowrap; flex-shrink: 0; }
.brand-contact-section { padding: 32px 0; }
.brand-integration-callout { margin-top: 40px; background: #0E1A2B; border-radius: 12px; padding: 32px 40px; display: flex; align-items: flex-start; gap: 24px; }
.brand-integration-icon { font-size: 32px; flex-shrink: 0; }
.brand-integration-label { font-family: 'Montserrat', sans-serif; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: rgba(255,255,255,0.5); margin-bottom: 8px; }
.brand-integration-text { font-family: 'Inter', sans-serif; font-size: 15px; color: rgba(255,255,255,0.85); line-height: 1.7; margin: 0; }
.brand-group-heading { font-size: 36px; margin-bottom: 12px; text-align: left; }
.brand-group-intro { margin-left: 0; margin-right: auto; color: var(--text-dark); font-size: 18px; max-width: 600px; text-align: left; }
.brand-group-cta-link { margin-top: 16px; }
.brand-featured-card { border: 2px solid var(--primary-blue); background: rgba(0,86,179,0.02); }
.brand-featured-badge { background: var(--primary-blue); color: var(--white); margin-bottom: 16px; display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; text-transform: uppercase; }
.brand-group-cta-row { display: flex; justify-content: center; margin-top: 40px; }
"""

systems_css = """
/* WAVE 2 SYSTEMS ADDITIONS */
.sys-two-col { display: flex; gap: 48px; align-items: start; }
.sys-deployment-panel { margin-top: 64px; padding: 24px; background: var(--bg-light); border-radius: 12px; }
.sys-brand-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 32px; margin-bottom: 48px; }
.sys-brand-item { margin-top: 24px; }
.net-stat-card { background: var(--white); border: 1px solid var(--border-light); border-radius: 12px; padding: 32px 40px; text-align: center; }
.net-stat-card-intro { font-family: 'Inter', sans-serif; color: var(--text-gray); max-width: 640px; margin: 0 auto 20px; }
.net-stat-icon { font-size: 32px; margin-bottom: 16px; display: block; }
.net-stat-eyebrow { font-family: 'Montserrat', sans-serif; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: var(--text-light); margin-bottom: 24px; display: block; }
.net-stat-value { font-size: 28px; margin-bottom: 10px; display: block; }
.net-stat-label { font-family: 'Montserrat', sans-serif; font-size: 13px; font-weight: 700; color: var(--text-dark); margin-bottom: 6px; display: block; }
.net-stat-desc { font-size: 13px; color: var(--text-gray); }
"""

def append_to_file(filepath, content):
    with open(filepath, "a", encoding="utf-8") as f:
        f.write("\n" + content + "\n")

append_to_file(os.path.join(base_dir, "sv-portfolio.css"), portfolio_css)
append_to_file(os.path.join(base_dir, "sv-brands.css"), brands_css)
append_to_file(os.path.join(base_dir, "sv-systems.css"), systems_css)

print("CSS additions appended successfully.")
