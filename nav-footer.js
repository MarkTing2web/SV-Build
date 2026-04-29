/**
 * nav-footer.js — Securevision Global Navigation & Footer
 * Version: 4.0 — April 2026
 * Changes: 8-sector structure. Solutions labels simplified to single words.
 *          Added Managed Living + Data Centres to Solutions (desktop + mobile).
 *          Portfolio dropdown: ?type= → ?sector=, added Managed Living.
 *          Footer Solutions column updated to match nav labels.
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

  var NAV_HTML = "<nav class=\"main-nav\"><div class=\"nav-container\"><a href=\"/\" class=\"nav-logo-link\" aria-label=\"Securevision Home\"><img src=\"/images/securevision-logo-white.png\" alt=\"Securevision Logo\" class=\"nav-logo-img\"><span class=\"wordmark nav-wordmark\">SECUREVISION</span></a><button class=\"mobile-toggle\" id=\"mobileToggle\" onclick=\"toggleMobileMenu()\" aria-label=\"Toggle Menu\"><svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><line x1=\"3\" y1=\"12\" x2=\"21\" y2=\"12\"></line><line x1=\"3\" y1=\"6\" x2=\"21\" y2=\"6\"></line><line x1=\"3\" y1=\"18\" x2=\"21\" y2=\"18\"></line></svg></button><ul class=\"nav-menu\"><li class=\"nav-item\" data-section=\"solutions\"><a href=\"/solutions/\" class=\"nav-link has-dropdown\">Solutions</a><div class=\"simple-dropdown\"><a href=\"/solutions/residential.html\">Residential</a><a href=\"/solutions/condominiums.html\">Condominiums</a><a href=\"/solutions/commercial.html\">Commercial</a><a href=\"/solutions/industrial.html\">Industrial</a><a href=\"/solutions/institutions.html\">Institutions</a><a href=\"/solutions/healthcare.html\">Healthcare</a><a href=\"/solutions/managed-living.html\">Managed Living</a><a href=\"/solutions/data-centres.html\">Data Centres</a><a href=\"/solutions/\"><strong>&rarr; View All Solutions</strong></a></div></li><li class=\"nav-item\" data-section=\"systems\"><a href=\"/systems/\" class=\"nav-link has-dropdown\">Systems</a><div class=\"simple-dropdown\"><a href=\"/systems/surveillance.html\">Surveillance &amp; Detection</a><a href=\"/systems/access-control.html\">People Access Control</a><a href=\"/systems/vehicle-access.html\">Vehicle Access &amp; Barriers</a><a href=\"/systems/platform.html\">Platform Management</a></div></li><li class=\"nav-item\" data-section=\"brands\"><a href=\"/brands/\" class=\"nav-link has-dropdown\">Brands</a><div class=\"simple-dropdown wide-dropdown\"><a href=\"/brands/#surveillance\"><strong>Surveillance</strong> &mdash; Hikvision &middot; Hanwha &middot; Uniview &middot; Milesight</a><a href=\"/brands/#access\"><strong>Access Control</strong> &mdash; Suprema &middot; ZKTeco &middot; HID &middot; EntryPass</a><a href=\"/brands/#intercom\"><strong>Intercoms</strong> &mdash; Akuvox &middot; Aiphone &middot; Kocom</a><a href=\"/brands/#alarms\"><strong>Alarms</strong> &mdash; AJAX &middot; RISCO &middot; Paradox &middot; DSC</a><a href=\"/brands/#gates\"><strong>Gates &amp; Barriers</strong> &mdash; FAAC &middot; MAG &middot; Dormer</a><hr><a href=\"/brands/\"><strong>&rarr; View All Technology Partners</strong></a></div></li><li class=\"nav-item\" data-section=\"portfolio\"><a href=\"/portfolio/\" class=\"nav-link has-dropdown\">Portfolio</a><div class=\"simple-dropdown\"><a href=\"/portfolio/\">All Projects</a><a href=\"/portfolio/?sector=residential\">Residential</a><a href=\"/portfolio/?sector=condominiums\">Condominiums</a><a href=\"/portfolio/?sector=commercial\">Commercial</a><a href=\"/portfolio/?sector=industrial\">Industrial</a><a href=\"/portfolio/?sector=managed-living\">Managed Living</a><hr><a href=\"/portfolio/\"><strong>&rarr; View Full Portfolio</strong></a></div></li><li class=\"nav-item\" data-section=\"resources\"><a href=\"/resources/\" class=\"nav-link has-dropdown\">Resources</a><div class=\"simple-dropdown\"><a href=\"/resources/guides/\">Technical Guides</a><a href=\"/resources/#tools\">Planning Tools</a><a href=\"/resources/#library\">Product Library</a><a href=\"/resources/#videos\">Training Videos</a><a href=\"/resources/#faq\">FAQ</a><a href=\"/resources/#trade\">For Trade &amp; Professionals</a><a href=\"/resources/\"><strong>&rarr; All Resources</strong></a></div></li><li class=\"nav-item\" data-section=\"insights\"><a href=\"/insights/\" class=\"nav-link\">Insights</a></li><li class=\"nav-item\" data-section=\"about\"><a href=\"/about.html\" class=\"nav-link has-dropdown\">About</a><div class=\"simple-dropdown\"><a href=\"/about.html\">Our Story</a><a href=\"/contact.html\">Contact Us</a></div></li></ul><div class=\"nav-right\"><button class=\"nav-search-btn\" id=\"desktopSearchBtn\" aria-label=\"Search\" onclick=\"alert(&quot;Search coming soon&quot;)\"><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"8\"/><line x1=\"21\" y1=\"21\" x2=\"16.65\" y2=\"16.65\"/></svg></button></div><button class=\"mobile-search-btn\" id=\"mobileSearchBtn\" aria-label=\"Search\" onclick=\"alert(&quot;Search coming soon&quot;)\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"8\"/><line x1=\"21\" y1=\"21\" x2=\"16.65\" y2=\"16.65\"/></svg></button></div><div class=\"mobile-menu\" id=\"mobileMenu\"><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;solSub&quot;)\">Solutions &#9662;<div class=\"mobile-submenu\" id=\"solSub\"><a href=\"/solutions/\"><strong>&rarr; View All Solutions</strong></a><a href=\"/solutions/residential.html\">Residential</a><a href=\"/solutions/condominiums.html\">Condominiums</a><a href=\"/solutions/commercial.html\">Commercial</a><a href=\"/solutions/industrial.html\">Industrial</a><a href=\"/solutions/institutions.html\">Institutions</a><a href=\"/solutions/healthcare.html\">Healthcare</a><a href=\"/solutions/managed-living.html\">Managed Living</a><a href=\"/solutions/data-centres.html\">Data Centres</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;sysSub&quot;)\">Systems &#9662;<div class=\"mobile-submenu\" id=\"sysSub\"><a href=\"/systems/surveillance.html\">Surveillance &amp; Detection</a><a href=\"/systems/access-control.html\">People Access Control</a><a href=\"/systems/vehicle-access.html\">Vehicle Access &amp; Barriers</a><a href=\"/systems/platform.html\">Platform Management</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;brandSub&quot;)\">Brands &#9662;<div class=\"mobile-submenu\" id=\"brandSub\"><a href=\"/brands/\"><strong>&rarr; View All Partners</strong></a><a href=\"/brands/#surveillance\">Surveillance &mdash; Hik &middot; Han &middot; Uni &middot; Mil</a><a href=\"/brands/#access\">Access &mdash; Sup &middot; ZK &middot; HID &middot; EP</a><a href=\"/brands/#intercom\">Intercoms &mdash; Aku &middot; Aip &middot; Koc</a><a href=\"/brands/#alarms\">Alarms &mdash; AJAX &middot; RIS &middot; Par &middot; DSC</a><a href=\"/brands/#gates\">Gates &mdash; FAAC &middot; MAG &middot; Dor</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;portSub&quot;)\">Portfolio &#9662;<div class=\"mobile-submenu\" id=\"portSub\"><a href=\"/portfolio/\"><strong>&rarr; All Projects</strong></a><a href=\"/portfolio/?sector=residential\">Residential</a><a href=\"/portfolio/?sector=condominiums\">Condominiums</a><a href=\"/portfolio/?sector=commercial\">Commercial</a><a href=\"/portfolio/?sector=industrial\">Industrial</a><a href=\"/portfolio/?sector=managed-living\">Managed Living</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;resSub&quot;)\">Resources &#9662;<div class=\"mobile-submenu\" id=\"resSub\"><a href=\"/resources/\"><strong>&rarr; All Resources</strong></a><a href=\"/resources/guides/\">Technical Guides</a><a href=\"/resources/#tools\">Planning Tools</a><a href=\"/resources/#library\">Product Library</a><a href=\"/resources/#videos\">Training Videos</a><a href=\"/resources/#faq\">FAQ</a><a href=\"/resources/#trade\">For Trade &amp; Professionals</a></div></div><a href=\"/insights/\" class=\"mobile-menu-item\">Insights</a><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;abtSub&quot;)\">About &#9662;<div class=\"mobile-submenu\" id=\"abtSub\"><a href=\"/about.html\"><strong>&rarr; Our Story</strong></a><a href=\"/contact.html\">Contact Us</a></div></div></div></nav>";

  var FOOTER_HTML = "<footer class=\"site-footer\"><div class=\"footer-container\"><div class=\"footer-grid\"><div class=\"footer-brand\"><div class=\"f-logo-wrap\"><img src=\"/images/securevision-logo-white.png\" alt=\"Securevision Logo\"><span class=\"brand-name\">Securevision</span></div><p style=\"font-family:Montserrat,sans-serif;font-weight:700;font-size:14px;margin-bottom:6px;\">Connecting People, Securing Places</p><p>Smart security and integrated systems for homes, condominiums, and businesses across Singapore.</p><div class=\"f-socials\"><a href=\"https://www.facebook.com/securevision\" target=\"_blank\" rel=\"noopener\" aria-label=\"Facebook\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z\"/></svg></a><a href=\"https://www.linkedin.com/company/securevision-pte-ltd\" target=\"_blank\" rel=\"noopener\" aria-label=\"LinkedIn\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z\"/><rect x=\"2\" y=\"9\" width=\"4\" height=\"12\"/><circle cx=\"4\" cy=\"4\" r=\"2\"/></svg></a><a href=\"https://www.youtube.com/@securevision\" target=\"_blank\" rel=\"noopener\" aria-label=\"YouTube\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z\"/></svg></a></div></div><div class=\"footer-links\"><h4>Solutions</h4><ul><li><a href=\"/solutions/residential.html\">Residential</a></li><li><a href=\"/solutions/condominiums.html\">Condominiums</a></li><li><a href=\"/solutions/commercial.html\">Commercial</a></li><li><a href=\"/solutions/industrial.html\">Industrial</a></li><li><a href=\"/solutions/institutions.html\">Institutions</a></li><li><a href=\"/solutions/healthcare.html\">Healthcare</a></li><li><a href=\"/solutions/managed-living.html\">Managed Living</a></li><li><a href=\"/solutions/data-centres.html\">Data Centres</a></li></ul></div><div class=\"footer-links\"><h4>Systems</h4><ul><li><a href=\"/systems/surveillance.html\">Surveillance &amp; Detection</a></li><li><a href=\"/systems/access-control.html\">People Access Control</a></li><li><a href=\"/systems/vehicle-access.html\">Vehicle Access &amp; Barriers</a></li><li><a href=\"/systems/platform.html\">Platform Management</a></li></ul></div><div class=\"footer-links\"><h4>Resources</h4><ul><li><a href=\"/resources/guides/\">Technical Guides</a></li><li><a href=\"/resources/#tools\">Planning Tools</a></li><li><a href=\"/resources/#library\">Product Library</a></li><li><a href=\"/resources/#videos\">Training Videos</a></li><li><a href=\"/resources/#faq\">Search &amp; FAQ</a></li><li><a href=\"/resources/\"><strong>Full Resource Hub</strong></a></li></ul></div><div class=\"footer-links\"><h4>Company</h4><ul><li><a href=\"/about.html\">Our Story</a></li><li><a href=\"/brands/\">Brands</a></li><li><a href=\"/portfolio/\">Project Portfolio</a></li><li><a href=\"/insights/\">Insights</a></li><li><a href=\"/contact.html\">Contact Us</a></li></ul></div><div class=\"footer-contact\"><h4>Get In Touch</h4><div class=\"footer-contact-item\"><span>&#x1F4AC;</span><a href=\"https://wa.me/6593860466\">WhatsApp an Engineer</a></div><div class=\"footer-contact-item\"><span>&#x2709;&#xFE0F;</span><a href=\"mailto:enquiry@securevision.com.sg\">Email Us</a></div><div class=\"footer-contact-item\"><span>&#x1F4DE;</span><a href=\"tel:+6562864796\">+65 6286 4796</a></div></div></div><div class=\"footer-bottom\"><p>&copy; <span class=\"sv-current-year\"></span> Securevision Pte Ltd &middot; Police Licence <span class=\"sv-licence\"></span> &middot; bizSAFE Level 3 &middot; BCA Registered</p><div class=\"footer-bottom-links\"><a href=\"/sitemap.html\">Sitemap</a><a href=\"/privacy.html\">Privacy Policy</a><a href=\"/terms.html\">Terms of Service</a></div></div></div></footer><a href=\"https://wa.me/6593860466\" class=\"sv-wa-float\" target=\"_blank\" rel=\"noopener\" aria-label=\"Chat on WhatsApp\"><svg width=\"26\" height=\"26\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z\"/></svg></a>";

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
      ["/about.html", "about"],
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
