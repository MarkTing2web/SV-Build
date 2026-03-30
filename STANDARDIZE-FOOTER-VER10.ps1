# Site-Wide Footer Standardization Script (Ver 10)
# This script ensures every page has the same 5-column footer structure.

$standardFooter = @"
<footer class="site-footer">
    <div class="footer-container">
        <div class="footer-grid">
            <div class="footer-brand">
                <div class="f-logo-wrap">
                    <img src="images/securevision-logo-white.png" alt="Securevision Logo">
                    <span class="brand-name">Securevision</span>
                </div>
                <p>Your partner in building smart, secure, and connected communities — powered by intelligent security systems since 2006.</p>
                <div class="f-socials">
                    <a href="https://www.facebook.com/securevision" target="_blank" rel="noopener" aria-label="Facebook">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
                    </a>
                    <a href="https://www.linkedin.com/company/securevision-pte-ltd" target="_blank" rel="noopener" aria-label="LinkedIn">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
                    </a>
                    <a href="https://www.youtube.com/@securevision" target="_blank" rel="noopener" aria-label="YouTube">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
                    </a>
                </div>
            </div>
            
            <div class="footer-links">
                <h4>Solutions</h4>
                <ul>
                    <li><a href="residential-security-singapore.html">Private Homes</a></li>
                    <li><a href="condominiums.html">Condominiums</a></li>
                    <li><a href="commercial-security-singapore.html">Commercial &amp; Retail</a></li>
                    <li><a href="industrial-security-singapore.html">Industrial &amp; Logistics</a></li>
                    <li><a href="government-institution-security-singapore.html">Institutions &amp; Government</a></li>
                    <li><a href="healthcare-security-singapore.html">Healthcare &amp; Managed Living</a></li>
                </ul>
            </div>
            
            <div class="footer-links">
                <h4>Systems</h4>
                <ul>
                    <li><a href="surveillance-detection.html">Surveillance &amp; Detection</a></li>
                    <li><a href="people-access-control.html">People Access Control</a></li>
                    <li><a href="vehicle-access-control.html">Vehicle Access &amp; Barriers</a></li>
                    <li><a href="integrated-security-platform.html">Platform Management</a></li>
                </ul>
            </div>
            
            <div class="footer-links">
                <h4>Resources</h4>
                <ul>
                    <li><a href="resources.html#guides">Technical Guides</a></li>
                    <li><a href="resources.html#tools">Planning Tools</a></li>
                    <li><a href="resources.html#library">Product Library</a></li>
                    <li><a href="resources.html#videos">Training Videos</a></li>
                    <li><a href="resources.html#faq">Search &amp; FAQ</a></li>
                    <li><a href="resources.html"><strong>Full Resource Hub</strong></a></li>
                </ul>
            </div>
            
            <div class="footer-links">
                <h4>Company</h4>
                <ul>
                    <li><a href="about.html">Our Story</a></li>
                    <li><a href="awards-certifications.html">Awards &amp; Certs</a></li>
                    <li><a href="security-brands-singapore.html"><strong>Technology Partners</strong></a></li>
                    <li><a href="portfolio.html">Project Portfolio</a></li>
                    <li><a href="security-articles-singapore.html">Insights</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                </ul>
            </div>
            
            <div class="footer-contact">
                <h4>Get In Touch</h4>
                <div class="footer-contact-item">
                    <span>💬</span>
                    <a href="https://wa.me/6593860466">WhatsApp Us</a>
                </div>
                <div class="footer-contact-item">
                    <span>✉️</span>
                    <a href="mailto:enquiry@securevision.com.sg">Email Us</a>
                </div>
                <div class="footer-contact-item">
                    <span>📞</span>
                    <a href="tel:+6562864796">+65 6286 4796</a>
                </div>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p>&copy; 2026 Securevision Pte Ltd &middot; Police Licence L/PS/000267/2023P &middot; bizSAFE Level 3 &middot; BCA Registered</p>
            <div class="footer-bottom-links">
                <a href="sitemap.html">Sitemap</a>
                <a href="privacy.html">Privacy Policy</a>
                <a href="terms.html">Terms of Service</a>
            </div>
        </div>
    </div>
</footer>
"@

$files = Get-ChildItem *.html -Exclude "index_full.html", "index-copy.html", "door-access-backup.html"

foreach ($f in $files) {
    $filePath = $f.FullName
    $content = Get-Content $filePath -Raw

    # Targeted replacement of the entire footer block
    $pattern = '(?s)<footer class="site-footer">.*?</footer>'
    
    if ($content -match $pattern) {
        $content = [regex]::Replace($content, $pattern, $standardFooter)
        Set-Content $filePath $content -NoNewline
        Write-Host "Standardized Footer in $($f.Name)" -ForegroundColor Cyan
    }
}

Write-Host "Site-Wide Footer Standardization Complete." -ForegroundColor Green
