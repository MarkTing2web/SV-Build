/**
 * nav-footer.js — Securevision Global Navigation & Footer
 * Version: 4.2 — May 2026
 * Changes: Portfolio dropdown updated to all 8 property types.
 *          Brands dropdown restructured to 5 system groups matching new taxonomy.
 *          Mobile nav Portfolio and Brands submenus updated to match.
 *          Brand anchor IDs updated: #premises #entry #vehicle #comms #platform.
 * Source of truth: /index.html (homepage)
 *
 * HOW TO USE ON ANY PAGE:
 * 1. Replace <nav>...</nav> with: <nav id="sv-nav"></nav>
 * 2. Replace <footer>...</footer> + WhatsApp float with: <footer id="sv-footer"></footer>
 * 3. Add before </body>: <script src="/nav-footer.js"></script>
 * 4. Remove inline toggleMobileMenu, toggleSubmenu, scroll scripts from the page.
 */
(function () {
  "use strict";

  var NAV_HTML = "<nav class=\"main-nav\"><div class=\"nav-container\"><a href=\"/\" class=\"nav-logo-link\" aria-label=\"Securevision Home\"><img src=\"/images/securevision-logo-white.png\" alt=\"Securevision Logo\" class=\"nav-logo-img\"><span class=\"wordmark nav-wordmark\">SECUREVISION</span></a><button class=\"mobile-toggle\" id=\"mobileToggle\" onclick=\"toggleMobileMenu()\" aria-label=\"Toggle Menu\"><svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><line x1=\"3\" y1=\"12\" x2=\"21\" y2=\"12\"></line><line x1=\"3\" y1=\"6\" x2=\"21\" y2=\"6\"></line><line x1=\"3\" y1=\"18\" x2=\"21\" y2=\"18\"></line></svg></button><ul class=\"nav-menu\"><li class=\"nav-item\" data-section=\"solutions\"><a href=\"/solutions/\" class=\"nav-link has-dropdown\">Solutions</a><div class=\"simple-dropdown\"><a href=\"/solutions/residential.html\">Residential</a><a href=\"/solutions/condominiums.html\">Condominiums</a><a href=\"/solutions/commercial.html\">Commercial</a><a href=\"/solutions/industrial.html\">Industrial</a><a href=\"/solutions/institutions.html\">Institutions</a><a href=\"/solutions/healthcare.html\">Healthcare</a><a href=\"/solutions/managed-living.html\">Managed Living</a><a href=\"/solutions/data-centres.html\">Data Centres</a><a href=\"/solutions/\"><strong>&rarr; View All Solutions</strong></a></div></li><li class=\"nav-item\" data-section=\"systems\"><a href=\"/systems/\" class=\"nav-link has-dropdown\">Systems</a><div class=\"simple-dropdown\"><a href=\"/systems/premises-security.html\">Premises Security</a><a href=\"/systems/entry-access-control.html\">Entry &amp; Access</a><a href=\"/systems/vehicle-lpr-management.html\">Vehicle Management</a><a href=\"/systems/ip-phone-communications.html\">Communications</a><a href=\"/systems/security-management-platform.html\">Platform &amp; Management</a></div></li><li class=\"nav-item\" data-section=\"brands\"><a href=\"/brands/\" class=\"nav-link has-dropdown\">Brands</a><div class=\"simple-dropdown wide-dropdown\"><a href=\"/brands/#premises\"><strong>Premises Security</strong> &mdash; Hikvision &middot; Hanwha &middot; Uniview &middot; Milesight &middot; AJAX &middot; RISCO</a><a href=\"/brands/#entry\"><strong>Entry &amp; Access</strong> &mdash; Suprema &middot; ZKTeco &middot; HID &middot; Akuvox &middot; Aiphone &middot; Kocom</a><a href=\"/brands/#vehicle\"><strong>Vehicle Management</strong> &mdash; FAAC &middot; MAG &middot; Dormer &middot; Milesight LPR</a><a href=\"/brands/#comms\"><strong>Communications</strong> &mdash; Yeastar &middot; Fanvil &middot; Yealink &middot; Omada &middot; Ruijie</a><a href=\"/brands/#platform\"><strong>Platform &amp; Management</strong> &mdash; VESTA &middot; Milestone &middot; HikCentral &middot; CVSecurity</a><hr><a href=\"/brands/\"><strong>&rarr; View All Technology Partners</strong></a></div></li><li class=\"nav-item\" data-section=\"portfolio\"><a href=\"/portfolio/\" class=\"nav-link has-dropdown\">Portfolio</a><div class=\"simple-dropdown\"><a href=\"/portfolio/\">All Projects</a><a href=\"/portfolio/?sector=residential\">Residential</a><a href=\"/portfolio/?sector=condominiums\">Condominiums</a><a href=\"/portfolio/?sector=commercial\">Commercial</a><a href=\"/portfolio/?sector=industrial\">Industrial</a><a href=\"/portfolio/?sector=institutions\">Institutions</a><a href=\"/portfolio/?sector=healthcare\">Healthcare</a><a href=\"/portfolio/?sector=managed-living\">Managed Living</a><a href=\"/portfolio/?sector=data-centres\">Data Centres</a><hr><a href=\"/portfolio/\"><strong>&rarr; View Full Portfolio</strong></a></div></li><li class=\"nav-item\" data-section=\"resources\"><a href=\"/resources/\" class=\"nav-link has-dropdown\">Resources</a><div class=\"simple-dropdown\"><a href=\"/resources/guides/\">Technical Guides</a><a href=\"/resources/#tools\">Planning Tools</a><a href=\"/resources/#library\">Product Library</a><a href=\"/resources/#videos\">Training Videos</a><a href=\"/resources/#faq\">FAQ</a><a href=\"/resources/#trade\">For Trade &amp; Professionals</a><a href=\"/resources/\"><strong>&rarr; All Resources</strong></a></div></li><li class=\"nav-item\" data-section=\"insights\"><a href=\"/insights/\" class=\"nav-link\">Insights</a></li><li class=\"nav-item\" data-section=\"about\"><a href=\"/about/\" class=\"nav-link has-dropdown\">About</a><div class=\"simple-dropdown\"><a href=\"/about/\">Our Story</a><a href=\"/about/\">Contact Us</a></div></li></ul><div class=\"nav-right\"><button class=\"nav-search-btn\" id=\"desktopSearchBtn\" aria-label=\"Search\" onclick=\"alert(&quot;Search coming soon&quot;)\"><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"8\"/><line x1=\"21\" y1=\"21\" x2=\"16.65\" y2=\"16.65\"/></svg></button></div><button class=\"mobile-search-btn\" id=\"mobileSearchBtn\" aria-label=\"Search\" onclick=\"alert(&quot;Search coming soon&quot;)\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"8\"/><line x1=\"21\" y1=\"21\" x2=\"16.65\" y2=\"16.65\"/></svg></button><div class=\"mobile-menu\" id=\"mobileMenu\"><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;solSub&quot;)\">Solutions &#9662;<div class=\"mobile-submenu\" id=\"solSub\"><a href=\"/solutions/\"><strong>&rarr; View All Solutions</strong></a><a href=\"/solutions/residential.html\">Residential</a><a href=\"/solutions/condominiums.html\">Condominiums</a><a href=\"/solutions/commercial.html\">Commercial</a><a href=\"/solutions/industrial.html\">Industrial</a><a href=\"/solutions/institutions.html\">Institutions</a><a href=\"/solutions/healthcare.html\">Healthcare</a><a href=\"/solutions/managed-living.html\">Managed Living</a><a href=\"/solutions/data-centres.html\">Data Centres</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;sysSub&quot;)\">Systems &#9662;<div class=\"mobile-submenu\" id=\"sysSub\"><a href=\"/systems/premises-security.html\">Premises Security</a><a href=\"/systems/entry-access-control.html\">Entry &amp; Access</a><a href=\"/systems/vehicle-lpr-management.html\">Vehicle Management</a><a href=\"/systems/ip-phone-communications.html\">Communications</a><a href=\"/systems/security-management-platform.html\">Platform &amp; Management</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;brandSub&quot;)\">Brands &#9662;<div class=\"mobile-submenu\" id=\"brandSub\"><a href=\"/brands/\"><strong>&rarr; View All Partners</strong></a><a href=\"/brands/#premises\">Premises &mdash; Hik &middot; Han &middot; AJAX &middot; RISCO</a><a href=\"/brands/#entry\">Entry &mdash; Suprema &middot; ZKTeco &middot; Akuvox &middot; Aiphone</a><a href=\"/brands/#vehicle\">Vehicles &mdash; FAAC &middot; MAG &middot; Dormer</a><a href=\"/brands/#comms\">Comms &mdash; Yeastar &middot; Fanvil &middot; Omada</a><a href=\"/brands/#platform\">Platform &mdash; VESTA &middot; Milestone &middot; HikCentral</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;portSub&quot;)\">Portfolio &#9662;<div class=\"mobile-submenu\" id=\"portSub\"><a href=\"/portfolio/\"><strong>&rarr; All Projects</strong></a><a href=\"/portfolio/?sector=residential\">Residential</a><a href=\"/portfolio/?sector=condominiums\">Condominiums</a><a href=\"/portfolio/?sector=commercial\">Commercial</a><a href=\"/portfolio/?sector=industrial\">Industrial</a><a href=\"/portfolio/?sector=institutions\">Institutions</a><a href=\"/portfolio/?sector=healthcare\">Healthcare</a><a href=\"/portfolio/?sector=managed-living\">Managed Living</a><a href=\"/portfolio/?sector=data-centres\">Data Centres</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;resSub&quot;)\">Resources &#9662;<div class=\"mobile-submenu\" id=\"resSub\"><a href=\"/resources/\"><strong>&rarr; All Resources</strong></a><a href=\"/resources/guides/\">Technical Guides</a><a href=\"/resources/#tools\">Planning Tools</a><a href=\"/resources/#library\">Product Library</a><a href=\"/resources/#videos\">Training Videos</a><a href=\"/resources/#faq\">FAQ</a><a href=\"/resources/#trade\">For Trade &amp; Professionals</a></div></div><a href=\"/insights/\" class=\"mobile-menu-item\">Insights</a><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;abtSub&quot;)\">About &#9662;<div class=\"mobile-submenu\" id=\"abtSub\"><a href=\"/about/\"><strong>&rarr; Our Story</strong></a><a href=\"/about/\">Contact Us</a></div></div></div></div></nav>";

  var FOOTER_HTML = "<footer class=\"site-footer\"><div class=\"footer-container\"><div class=\"footer-grid\" style=\"display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr 1fr 1.2fr;gap:32px;margin-bottom:32px;\"><div class=\"footer-brand\"><div class=\"f-logo-wrap\"><img src=\"/images/securevision-logo-white.png\" alt=\"Securevision Logo\"><span class=\"brand-name\">Securevision</span></div><p style=\"font-family:Montserrat,sans-serif;font-weight:700;font-size:14px;margin-bottom:6px;\">Connecting People, Securing Places</p><p>Smart security and integrated systems for homes, condominiums, and businesses across Singapore.</p><div class=\"f-socials\"><a href=\"https://www.facebook.com/securevision\" target=\"_blank\" rel=\"noopener\" aria-label=\"Facebook\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z\"/></svg></a><a href=\"https://www.linkedin.com/company/securevision-pte-ltd\" target=\"_blank\" rel=\"noopener\" aria-label=\"LinkedIn\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z\"/><rect x=\"2\" y=\"9\" width=\"4\" height=\"12\"/><circle cx=\"4\" cy=\"4\" r=\"2\"/></svg></a><a href=\"https://www.youtube.com/@securevision\" target=\"_blank\" rel=\"noopener\" aria-label=\"YouTube\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z\"/></svg></a></div></div><div class=\"footer-links\"><h4>Solutions</h4><ul><li><a href=\"/solutions/residential.html\">Residential</a></li><li><a href=\"/solutions/condominiums.html\">Condominiums</a></li><li><a href=\"/solutions/commercial.html\">Commercial</a></li><li><a href=\"/solutions/industrial.html\">Industrial</a></li><li><a href=\"/solutions/institutions.html\">Institutions</a></li><li><a href=\"/solutions/healthcare.html\">Healthcare</a></li><li><a href=\"/solutions/managed-living.html\">Managed Living</a></li><li><a href=\"/solutions/data-centres.html\">Data Centres</a></li></ul></div><div class=\"footer-links\"><h4>Systems</h4><ul><li><a href=\"/systems/premises-security.html\">Premises Security</a></li><li><a href=\"/systems/entry-access-control.html\">Entry &amp; Access</a></li><li><a href=\"/systems/vehicle-lpr-management.html\">Vehicle Management</a></li><li><a href=\"/systems/ip-phone-communications.html\">Communications</a></li><li><a href=\"/systems/security-management-platform.html\">Platform &amp; Management</a></li></ul></div><div class=\"footer-links\"><h4>Resources</h4><ul><li><a href=\"/resources/guides/\">Technical Guides</a></li><li><a href=\"/resources/#tools\">Planning Tools</a></li><li><a href=\"/resources/#library\">Product Library</a></li><li><a href=\"/resources/#videos\">Training Videos</a></li><li><a href=\"/resources/#faq\">Search &amp; FAQ</a></li><li><a href=\"/resources/\"><strong>Full Resource Hub</strong></a></li></ul></div><div class=\"footer-links\"><h4>Company</h4><ul><li><a href=\"/about/\">Our Story</a></li><li><a href=\"/brands/\">Brands</a></li><li><a href=\"/portfolio/\">Project Portfolio</a></li><li><a href=\"/insights/\">Insights</a></li><li><a href=\"/about/\">Contact Us</a></li></ul></div><div class=\"footer-contact\"><h4>Get In Touch</h4><div class=\"footer-contact-item\"><span style=\"background:#25d366;border-radius:50%;width:32px;height:32px;min-width:32px;display:flex;align-items:center;justify-content:center;\"><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"white\"><path d=\"M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z\"/></svg></span><a href=\"https://wa.me/6593860466\">WhatsApp an Engineer</a></div><div class=\"footer-contact-item\"><span style=\"background:none;border-radius:0;width:auto;height:auto;\"><svg width=\"22\" height=\"22\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"white\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2\"/><path d=\"m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7\"/></svg></span><a href=\"mailto:enquiry@securevision.com.sg\">Email Us</a></div><div class=\"footer-contact-item\"><span style=\"background:none;border-radius:0;width:auto;height:auto;\"><svg width=\"22\" height=\"22\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"white\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.5 19.79 19.79 0 0 1 1.61 5a2 2 0 0 1 1.99-2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 10.91a16 16 0 0 0 6.13 6.13l.91-.91a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 18.35z\"/></svg></span><a href=\"tel:+6562864796\">+65 6286 4796</a></div></div></div><div class=\"footer-bottom\"><p>&copy; <span class=\"sv-current-year\"></span> Securevision Pte Ltd &middot; Police Licence <span class=\"sv-licence\"></span> &middot; bizSAFE Level 3 &middot; BCA Registered</p><div class=\"footer-bottom-links\"><a href=\"/sitemap.html\">Sitemap</a><a href=\"/privacy.html\">Privacy Policy</a><a href=\"/terms.html\">Terms of Service</a></div></div></div></footer><a href=\"https://wa.me/6593860466\" class=\"sv-wa-float\" target=\"_blank\" rel=\"noopener\" aria-label=\"Chat on WhatsApp\"><svg width=\"26\" height=\"26\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z\"/></svg></a>";

  function injectNavFooter() {
    var navEl = document.getElementById("sv-nav");
    if (navEl) navEl.outerHTML = NAV_HTML;
    var footerEl = document.getElementById("sv-footer");
    if (footerEl) footerEl.outerHTML = FOOTER_HTML;
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", injectNavFooter);
  } else {
    injectNavFooter();
  }

  function setActiveNav() {
    var path = window.location.pathname;
    var map = [
      ["/solutions/", "solutions"],
      ["/systems/", "systems"],
      ["/brands/", "brands"],
      ["/portfolio/", "portfolio"],
      ["/resources/", "resources"],
      ["/insights/", "insights"],
      ["/about/", "about"],
      ["/contact.html", "about"]
    ];
    for (var i = 0; i < map.length; i++) {
      if (path.indexOf(map[i][0]) === 0) {
        var link = document.querySelector(".nav-item[data-section=\"" + map[i][1] + "\"] .nav-link");
        if (link) link.classList.add("active");
        break;
      }
    }
  }

  window.toggleMobileMenu = function () {
    var menu = document.getElementById("mobileMenu");
    if (menu) menu.classList.toggle("active");
  };

  window.toggleSubmenu = function (id) {
    var sub = document.getElementById(id);
    if (sub) {
      var isActive = sub.classList.contains("active");
      document.querySelectorAll(".mobile-submenu").forEach(function (s) { s.classList.remove("active"); });
      if (!isActive) sub.classList.add("active");
    }
  };

  document.addEventListener("click", function (e) {
    var nav = document.querySelector(".main-nav");
    var menu = document.getElementById("mobileMenu");
    if (nav && menu && !nav.contains(e.target)) menu.classList.remove("active");
  });

  window.addEventListener("scroll", function () {
    var nav = document.querySelector(".main-nav");
    var logo = document.querySelector(".nav-logo-img");
    if (nav) nav.classList.toggle("scrolled", window.scrollY > 50);
    if (logo) logo.src = window.scrollY > 50 ? "/images/securevision-logo-blue.png" : "/images/securevision-logo-white.png";
  });

  document.addEventListener("DOMContentLoaded", function () {
    setActiveNav();
    document.querySelectorAll(".sv-current-year").forEach(function (el) { el.textContent = new Date().getFullYear(); });
    if (typeof SECUREVISION !== "undefined") {
      var SV = SECUREVISION;
      document.querySelectorAll(".sv-licence").forEach(function (el) { el.textContent = SV.licenceNumber || ""; });
      document.querySelectorAll(".sv-bizsafe").forEach(function (el) { el.textContent = SV.bizSAFE || "bizSAFE Level 3"; });
      document.querySelectorAll(".sv-sites").forEach(function (el) { el.textContent = SV.siteDisplay || ""; });
      document.querySelectorAll(".sv-founded").forEach(function (el) { el.textContent = SV.foundedDisplay || ""; });
    }
  });

})();
