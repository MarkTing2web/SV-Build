/**
 * nav-footer.js — Securevision Global Navigation & Footer
 * Version: 2.2 — June 2026
 * Updated: UEN 200614644E added to footer copyright line
 * Version: 4.2 — May 2026
 * Changes: Portfolio dropdown updated to all 8 property types.
 *          Brands dropdown restructured to 5 system groups matching new taxonomy.
 *          Mobile nav Portfolio and Brands submenus updated to match.
 *          Brand anchor IDs updated: #premises #entry #vehicle #comms #platform.
 * Source of truth: / (homepage)
 *
 * HOW TO USE ON ANY PAGE:
 * 1. Replace <nav>...</nav> with: <nav id="sv-nav"></nav>
 * 2. Replace <footer>...</footer> + WhatsApp float with: <footer id="sv-footer"></footer>
 * 3. Add before </body>: <script src="/nav-footer.js"></script>
 * 4. Remove inline toggleMobileMenu, toggleSubmenu, scroll scripts from the page.
 */
(function () {  "use strict";
  var NAV_HTML = "<nav class=\"main-nav\"><div class=\"nav-row1\"><div class=\"nav-row1-inner\"><a href=\"/\" class=\"nav-logo-link\" aria-label=\"Securevision home\" style=\"text-decoration:none;display:flex;align-items:center;gap:10px;\"><img src=\"/images/securevision-logo-white.png\" alt=\"Securevision Logo\" class=\"nav-logo-img\"/><span class=\"wordmark nav-wordmark\">SECUREVISION</span></a><div class=\"nav-row1-center\"><span class=\"nav-tagline\">Connecting People, Securing Places</span></div><div class=\"nav-row1-right\"><a href=\"/request-site-assessment-singapore\" class=\"nav-cta-btn\">Book a Site Assessment</a></div></div></div><div class=\"nav-row2\"><div class=\"nav-row2-inner\"><a href=\"/\" class=\"nav-scroll-home\" aria-label=\"Securevision Homepage\"><img src=\"/images/securevision-logo-white.png\" alt=\"Securevision\" class=\"nav-scroll-logo\"/></a><div class=\"nav-mobile-brand\"><a href=\"/\" class=\"nav-logo-link\" aria-label=\"Securevision Home\"><img src=\"/images/securevision-logo-white.png\" alt=\"Securevision Logo\" class=\"nav-logo-img\"/></a></div><a href=\"/request-site-assessment-singapore\" class=\"nav-mobile-cta\">Book Assessment</a><div class=\"nav-mobile-buttons\"><button class=\"mobile-search-btn\" id=\"mobileSearchBtn\" aria-label=\"Search\" onclick=\"openSearch()\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"8\"/><line x1=\"21\" y1=\"21\" x2=\"16.65\" y2=\"16.65\"/></svg></button><button class=\"mobile-toggle\" id=\"mobileToggle\" onclick=\"toggleMobileMenu()\" aria-label=\"Toggle Menu\"><svg width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><line x1=\"3\" y1=\"12\" x2=\"21\" y2=\"12\"></line><line x1=\"3\" y1=\"6\" x2=\"21\" y2=\"6\"></line><line x1=\"3\" y1=\"18\" x2=\"21\" y2=\"18\"></line></svg></button></div><ul class=\"nav-menu\"><li class=\"nav-item\" data-section=\"solutions\"><a href=\"/solutions/\" class=\"nav-link has-dropdown\">Solutions</a><div class=\"simple-dropdown\"><a href=\"/solutions/residential\">Residential</a><a href=\"/solutions/condominiums\">Condominiums</a><a href=\"/solutions/commercial\">Commercial</a><a href=\"/solutions/industrial\">Industrial</a><a href=\"/solutions/institutions\">Institutions</a><a href=\"/solutions/healthcare\">Healthcare</a><a href=\"/solutions/managed-living\">Managed Living</a><a href=\"/solutions/data-centres\">Data Centres</a><a href=\"/solutions/\"><strong>&rarr; View All Solutions</strong></a></div></li><li class=\"nav-item\" data-section=\"systems\"><a href=\"/systems/\" class=\"nav-link has-dropdown\">Systems</a><div class=\"simple-dropdown\"><a href=\"/systems/premises-security\">Premises Security</a><a href=\"/systems/entry-access-control\">Entry Access</a><a href=\"/systems/vehicle-lpr-management\">Vehicle Management</a><a href=\"/systems/ip-phone-communications\">IP Telephony</a><a href=\"/systems/network-infrastructure\">Network Infrastructure</a><a href=\"/systems/security-management-platform\">Management Platforms</a><a href=\"/systems/\"><strong>&rarr; View All Systems</strong></a></div></li><li class=\"nav-item\" data-section=\"brands\"><a href=\"/brands/\" class=\"nav-link has-dropdown\">Brands</a><div class=\"simple-dropdown\"><a href=\"/brands/#burglar\">Burglar Alarm</a><a href=\"/brands/#cctv\">CCTV &amp; Surveillance</a><a href=\"/brands/#access\">Entry &amp; Access Control</a><a href=\"/brands/#intercom\">Intercom &amp; Video Entry</a><a href=\"/brands/#vehicle\">Vehicle Management</a><a href=\"/brands/#telephony\">IP Telephony</a><a href=\"/brands/#network\">Network Infrastructure</a><a href=\"/brands/#platform\">Platform &amp; Management</a><hr><a href=\"/brands/\"><strong>&rarr; View All Brands</strong></a></div></li><li class=\"nav-item\" data-section=\"portfolio\"><a href=\"/portfolio/\" class=\"nav-link has-dropdown\">Portfolio</a><div class=\"simple-dropdown\"><a href=\"/portfolio/\">All Projects</a><a href=\"/portfolio/?sector=residential\">Residential</a><a href=\"/portfolio/?sector=condominiums\">Condominiums</a><a href=\"/portfolio/?sector=commercial\">Commercial</a><a href=\"/portfolio/?sector=industrial\">Industrial</a><a href=\"/portfolio/?sector=institutions\">Institutions</a><a href=\"/portfolio/?sector=healthcare\">Healthcare</a><a href=\"/portfolio/?sector=managed-living\">Managed Living</a><a href=\"/portfolio/?sector=data-centres\">Data Centres</a><hr><a href=\"/portfolio/\"><strong>&rarr; View Full Portfolio</strong></a></div></li><li class=\"nav-item\" data-section=\"resources\"><a href=\"/resources/\" class=\"nav-link has-dropdown\">Resources</a><div class=\"simple-dropdown\"><a href=\"/resources/guides\">Technical Guides</a><a href=\"/resources/checklists\">Planning Checklists</a><a href=\"/resources/calculators\">Planning Calculators</a><a href=\"/resources/library\">Product Library</a><a href=\"/resources/training-videos\">Training Videos</a><a href=\"/resources/faq\">FAQ</a><a href=\"/resources/\"><strong>&rarr; All Resources</strong></a></div></li><li class=\"nav-item\" data-section=\"insights\"><a href=\"/insights/\" class=\"nav-link has-dropdown\">Insights</a><div class=\"simple-dropdown\"><a href=\"/insights/\"><strong>All Insights</strong></a><hr><a href=\"/insights/?category=alarm-intrusion\">Alarm &amp; Intrusion</a><a href=\"/insights/?category=cctv-surveillance\">CCTV &amp; Surveillance</a><a href=\"/insights/?category=access-intercom\">Access &amp; Intercom</a><a href=\"/insights/?category=vehicle-gates\">Vehicle &amp; Gates</a><a href=\"/insights/?category=ip-telephony-network\">IP Telephony &amp; Network</a><a href=\"/insights/?category=platform-integration\">Platform &amp; Integration</a><a href=\"/insights/?category=security-planning\">Security Planning</a></div></li><li class=\"nav-item\" data-section=\"about\"><a href=\"/about\" class=\"nav-link has-dropdown\">About</a><div class=\"simple-dropdown\"><a href=\"/about\">Our Story</a><a href=\"/contact\">Contact Us</a></div></li></ul><div class=\"nav-right\"><button class=\"nav-search-btn\" id=\"desktopSearchBtn\" aria-label=\"Search\" onclick=\"openSearch()\"><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><circle cx=\"11\" cy=\"11\" r=\"8\"/><line x1=\"21\" y1=\"21\" x2=\"16.65\" y2=\"16.65\"/></svg></button></div><div class=\"mobile-menu\" id=\"mobileMenu\"><a href=\"/request-site-assessment-singapore\" class=\"mobile-menu-cta\">Book a Site Assessment</a><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;solSub&quot;)\">Solutions &#9662;<div class=\"mobile-submenu\" id=\"solSub\"><a href=\"/solutions/\"><strong>&rarr; View All Solutions</strong></a><a href=\"/solutions/residential\">Residential</a><a href=\"/solutions/condominiums\">Condominiums</a><a href=\"/solutions/commercial\">Commercial</a><a href=\"/solutions/industrial\">Industrial</a><a href=\"/solutions/institutions\">Institutions</a><a href=\"/solutions/healthcare\">Healthcare</a><a href=\"/solutions/managed-living\">Managed Living</a><a href=\"/solutions/data-centres\">Data Centres</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;sysSub&quot;)\">Systems &#9662;<div class=\"mobile-submenu\" id=\"sysSub\"><a href=\"/systems/premises-security\">Premises Security</a><a href=\"/systems/entry-access-control\">Entry Access</a><a href=\"/systems/vehicle-lpr-management\">Vehicle Management</a><a href=\"/systems/ip-phone-communications\">IP Telephony</a><a href=\"/systems/network-infrastructure\">Network Infrastructure</a><a href=\"/systems/security-management-platform\">Management Platforms</a><a href=\"/systems/\"><strong>&rarr; View All Systems</strong></a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;brandSub&quot;)\">Brands &#9662;<div class=\"mobile-submenu\" id=\"brandSub\"><a href=\"/brands/\"><strong>&rarr; View All Brands</strong></a><a href=\"/brands/#burglar\">Burglar Alarm</a><a href=\"/brands/#cctv\">CCTV &amp; Surveillance</a><a href=\"/brands/#access\">Entry &amp; Access Control</a><a href=\"/brands/#intercom\">Intercom &amp; Video Entry</a><a href=\"/brands/#vehicle\">Vehicle Management</a><a href=\"/brands/#telephony\">IP Telephony</a><a href=\"/brands/#network\">Network Infrastructure</a><a href=\"/brands/#platform\">Platform &amp; Management</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;portSub&quot;)\">Portfolio &#9662;<div class=\"mobile-submenu\" id=\"portSub\"><a href=\"/portfolio/\"><strong>&rarr; All Projects</strong></a><a href=\"/portfolio/?sector=residential\">Residential</a><a href=\"/portfolio/?sector=condominiums\">Condominiums</a><a href=\"/portfolio/?sector=commercial\">Commercial</a><a href=\"/portfolio/?sector=industrial\">Industrial</a><a href=\"/portfolio/?sector=institutions\">Institutions</a><a href=\"/portfolio/?sector=healthcare\">Healthcare</a><a href=\"/portfolio/?sector=managed-living\">Managed Living</a><a href=\"/portfolio/?sector=data-centres\">Data Centres</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;resSub&quot;)\">Resources &#9662;<div class=\"mobile-submenu\" id=\"resSub\"><a href=\"/resources/\"><strong>&rarr; All Resources</strong></a><a href=\"/resources/guides\">Technical Guides</a><a href=\"/resources/checklists\">Planning Checklists</a><a href=\"/resources/calculators\">Planning Calculators</a><a href=\"/resources/library\">Product Library</a><a href=\"/resources/training-videos\">Training Videos</a><a href=\"/resources/faq\">FAQ</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;insSub&quot;)\">Insights &#9662;<div class=\"mobile-submenu\" id=\"insSub\"><a href=\"/insights/\"><strong>&rarr; All Insights</strong></a><a href=\"/insights/?category=alarm-intrusion\">Alarm &amp; Intrusion</a><a href=\"/insights/?category=cctv-surveillance\">CCTV &amp; Surveillance</a><a href=\"/insights/?category=access-intercom\">Access &amp; Intercom</a><a href=\"/insights/?category=vehicle-gates\">Vehicle &amp; Gates</a><a href=\"/insights/?category=ip-telephony-network\">IP Telephony &amp; Network</a><a href=\"/insights/?category=platform-integration\">Platform &amp; Integration</a><a href=\"/insights/?category=security-planning\">Security Planning</a></div></div><div class=\"mobile-menu-item\" onclick=\"toggleSubmenu(&quot;abtSub&quot;)\">About &#9662;<div class=\"mobile-submenu\" id=\"abtSub\"><a href=\"/about\"><strong>&rarr; Our Story</strong></a><a href=\"/contact\">Contact Us</a></div></div></div></div></div></nav>";

  var FOOTER_HTML = "<footer class=\"site-footer\"><div class=\"footer-container\"><div class=\"footer-grid\" style=\"display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr 1fr 1.2fr;gap:32px;margin-bottom:32px;\"><div class=\"footer-brand\"><div class=\"f-logo-wrap\"><img src=\"/images/securevision-logo-white.png\" alt=\"Securevision Logo\"><span class=\"brand-name\">Securevision</span></div><p style=\"font-family:Montserrat,sans-serif;font-weight:700;font-size:14px;margin-bottom:6px;\">Connecting People, Securing Places</p><p>Smart security and integrated systems for homes, condominiums, and businesses across Singapore.</p><div class=\"f-socials\"><a href=\"https://www.facebook.com/securevision\" target=\"_blank\" rel=\"noopener\" aria-label=\"Facebook\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z\"/></svg></a><a href=\"https://www.linkedin.com/company/securevision-pte-ltd\" target=\"_blank\" rel=\"noopener\" aria-label=\"LinkedIn\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z\"/><rect x=\"2\" y=\"9\" width=\"4\" height=\"12\"/><circle cx=\"4\" cy=\"4\" r=\"2\"/></svg></a><a href=\"https://www.youtube.com/@securevision\" target=\"_blank\" rel=\"noopener\" aria-label=\"YouTube\"><svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z\"/></svg></a></div></div><div class=\"footer-links\"><h4>Solutions</h4><ul><li><a href=\"/solutions/residential\">Residential</a></li><li><a href=\"/solutions/condominiums\">Condominiums</a></li><li><a href=\"/solutions/commercial\">Commercial</a></li><li><a href=\"/solutions/industrial\">Industrial</a></li><li><a href=\"/solutions/institutions\">Institutions</a></li><li><a href=\"/solutions/healthcare\">Healthcare</a></li><li><a href=\"/solutions/managed-living\">Managed Living</a></li><li><a href=\"/solutions/data-centres\">Data Centres</a></li></ul></div><div class=\"footer-links\"><h4>Systems</h4><ul><li><a href=\"/systems/premises-security\">Premises Security</a></li><li><a href=\"/systems/entry-access-control\">Entry Access</a></li><li><a href=\"/systems/vehicle-lpr-management\">Vehicle Management</a></li><li><a href=\"/systems/ip-phone-communications\">IP Telephony</a></li><li><a href=\"/systems/network-infrastructure\">Network Infrastructure</a></li><li><a href=\"/systems/security-management-platform\">Management Platforms</a></li></ul></div><div class=\"footer-links\"><h4>Resources</h4><ul><li><a href=\"/resources/guides\">Technical Guides</a></li><li><a href=\"/resources/checklists\">Planning Checklists</a></li><li><a href=\"/resources/calculators\">Planning Calculators</a></li><li><a href=\"/resources/library\">Product Library</a></li><li><a href=\"/resources/training-videos\">Training Videos</a></li><li><a href=\"/resources/faq\">Search &amp; FAQ</a></li><li><a href=\"/resources/\"><strong>Full Resource Hub</strong></a></li></ul></div><div class=\"footer-links\"><h4>Company</h4><ul><li><a href=\"/about\">Our Story</a></li><li><a href=\"/brands/\">Brands</a></li><li><a href=\"/portfolio/\">Project Portfolio</a></li><li><a href=\"/insights/\">Insights</a></li><li><a href=\"/contact\">Contact Us</a></li></ul></div><div class=\"footer-contact\"><h4>Get In Touch</h4><div class=\"footer-contact-item\"><span style=\"background:#25d366;border-radius:50%;width:32px;height:32px;min-width:32px;display:flex;align-items:center;justify-content:center;\"><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"white\"><path d=\"M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z\"/></svg></span><a href=\"https://wa.me/6593860466\">WhatsApp an Engineer</a></div><div class=\"footer-contact-item\"><span style=\"background:none;border-radius:0;width:auto;height:auto;\"><svg width=\"22\" height=\"22\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"white\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2\"/><path d=\"m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7\"/></svg></span><a href=\"mailto:enquiry@securevision.com.sg\">Email Us</a></div><div class=\"footer-contact-item\"><span style=\"background:none;border-radius:0;width:auto;height:auto;\"><svg width=\"22\" height=\"22\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"white\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 13.5 19.79 19.79 0 0 1 1.61 5a2 2 0 0 1 1.99-2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 10.91a16 16 0 0 0 6.13 6.13l.91-.91a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 18.35z\"/></svg></span><a href=\"tel:+6562864796\">+65 6286 4796</a></div></div></div><div class=\"footer-bottom\"><p>&copy; <span class=\"sv-current-year\"></span> Securevision Pte Ltd (UEN: 200614644E) &middot; Police Licenced &middot; bizSAFE Level 3 &middot; BCA Registered</p><div class=\"footer-bottom-links\"><a href=\"/sitemap\">Sitemap</a><a href=\"/privacy\">Privacy Policy</a><a href=\"/terms\">Terms of Service</a></div></div></div></footer><a href=\"https://wa.me/6593860466\" class=\"sv-wa-float\" target=\"_blank\" rel=\"noopener\" aria-label=\"Chat on WhatsApp\"><svg width=\"26\" height=\"26\" viewBox=\"0 0 24 24\" fill=\"currentColor\"><path d=\"M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z\"/></svg></a>";

  function injectNavFooter() {
    var navEl = document.getElementById("sv-nav");
    if (navEl) navEl.outerHTML = NAV_HTML;
    var footerEl = document.getElementById("sv-footer");
    if (footerEl) footerEl.outerHTML = FOOTER_HTML;
    /* Run after injection so dropdown links exist in DOM */
    setActiveNav();
  }


    // ── Related Guides auto-renderer ────────────────────────────────
    // Fires on any page with id="related-guides-grid" and
    // <body data-guide="[slug]">. Renders 3 guide cards using the
    // standard .guide-card structure from sv-resources.css.
    (function () {
      var grid = document.getElementById("related-guides-grid");
      if (!grid) return;
      if (!Array.isArray(SECUREVISION.guides)) return;

      // Apply grid layout class
      grid.className = "guides-grid";

      var currentSlug = document.body.getAttribute("data-guide") || "";
      var currentGuide = SECUREVISION.guides.find(function (g) { return g.slug === currentSlug; });
      var currentTags = currentGuide ? currentGuide.tags : [];

      var pool = SECUREVISION.guides.filter(function (g) { return g.slug !== currentSlug; });

      function shuffle(arr) {
        var a = arr.slice();
        for (var i = a.length - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1));
          var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        }
        return a;
      }

      function score(g) {
        var s = 0;
        currentTags.forEach(function (tag) {
          if (g.tags.indexOf(tag) !== -1) s += 2;
        });
        return s;
      }

      var picks = shuffle(pool).sort(function (a, b) { return score(b) - score(a); }).slice(0, 3);

      var imgMap = {
        "burglar-alarm-guide":                 "/images/insights/alarm-internet-cut-siren.webp",
        "cctv-guide":                          "/images/resources/guides/cctv/hero-cctv.webp",
        "door-access-guide":                   "/images/insights/how-card-access-works-feature.webp",
        "intercom-guide":                      "/images/solutions/condominiums/akuvox-visitor-call-panel-condominium-lobby.webp",
        "auto-gate-guide":                     "/images/resources/guides/autogate/hero-auto-gate.webp",
        "wifi-network-guide":                  "/images/resources/guides/network/hero-wifi-network.webp",
        "office-telephone-guide":              "/images/resources/guides/telephony/fanvil-x6u-desk-phone.webp",
        "security-renovation-guide":           "/images/resources/guides/renovation/hero-security-renovation.webp",
        "how-to-evaluate-security-contractor": "/images/insights/break-in-nearby-security-review-feature.webp"
      };

      grid.innerHTML = picks.map(function (g) {
        var img = imgMap[g.slug] || "";
        return "<a href=\"/resources/guides/" + g.slug + ".html\" class=\"guide-card\">" +
          "<div class=\"guide-card-img-wrap\">" +
          (img ? "<img src=\"" + img + "\" alt=\"" + g.title + "\" loading=\"lazy\"/>" : "") +
          "<span class=\"guide-badge\">" + g.category + "</span>" +
          "</div>" +
          "<div class=\"guide-card-body\">" +
          "<h3>" + g.title + "</h3>" +
          "<hr/>" +
          "<div class=\"guide-meta\"><span>Read Guide &rarr;</span></div>" +
          "</div>" +
          "</a>";
      }).join("");
    })();

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
      ["/about", "about"],
      ["/contact", "about"]
    ];
    for (var i = 0; i < map.length; i++) {
      if (path.indexOf(map[i][0]) === 0) {
        var link = document.querySelector(".nav-item[data-section=\"" + map[i][1] + "\"] .nav-link");
        if (link) link.classList.add("active");
        break;
      }
    }
    /* Mark active dropdown item matching current URL */
    var dropLinks = document.querySelectorAll(".simple-dropdown a");
    for (var j = 0; j < dropLinks.length; j++) {
      var href = dropLinks[j].getAttribute("href");
      if (!href) continue;
      /* Normalise both sides — strip trailing slash and .html for comparison */
      var normHref = href.replace(/\.html$/, "").replace(/\/$/, "");
      var normPath = path.replace(/\.html$/, "").replace(/\/$/, "");
      if (normHref === normPath || href === path) {
        dropLinks[j].classList.add("active");
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
    if (nav) nav.classList.toggle("scrolled", window.scrollY > 10);
  });

  function runHydration() {

    /* ── Desktop dropdown click toggle for touch devices ──
       On touch screens hover doesn't work. This adds a click
       handler so tapping a .has-dropdown link opens the dropdown
       instead of navigating. Second tap navigates to the page.
    ── */
    document.querySelectorAll(".nav-link.has-dropdown").forEach(function (link) {
      link.addEventListener("click", function (e) {
        // Only intercept on touch / narrow screens where hover fails
        if (window.matchMedia("(hover: none)").matches || window.innerWidth <= 991) return;
        var item = link.closest(".nav-item");
        var dropdown = item ? item.querySelector(".simple-dropdown") : null;
        if (!dropdown) return;
        var isOpen = item.classList.contains("dropdown-open");
        // Close all open dropdowns
        document.querySelectorAll(".nav-item.dropdown-open").forEach(function (el) {
          el.classList.remove("dropdown-open");
        });
        if (!isOpen) {
          e.preventDefault();
          item.classList.add("dropdown-open");
        }
      });
    });

    // Close dropdown when clicking outside
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".nav-item")) {
        document.querySelectorAll(".nav-item.dropdown-open").forEach(function (el) {
          el.classList.remove("dropdown-open");
        });
      }
    });

    document.querySelectorAll(".sv-current-year").forEach(function (el) { el.textContent = new Date().getFullYear(); });
    if (typeof SECUREVISION !== "undefined") {
      var SV = SECUREVISION;
      document.querySelectorAll(".sv-licence").forEach(function (el) { el.textContent = SV.licenceNumber || ""; });
      document.querySelectorAll(".sv-bizsafe").forEach(function (el) { el.textContent = SV.bizSAFE || "bizSAFE Level 3"; });
      document.querySelectorAll(".sv-sites").forEach(function (el) { el.textContent = SV.siteDisplay || ""; });
      document.querySelectorAll(".sv-founded").forEach(function (el) { el.textContent = SV.foundedDisplay || ""; });
    }

    // ── Related Insights auto-renderer ──────────────────────────────
    // Fires on any page that has id="related-insights-grid" and
    // a <body data-article="[slug]"> attribute.
    // Selection: same category first, then tag overlap, then any.
    // Always renders exactly 3 cards (or fewer if registry is small).
    (function () {
      var grid = document.getElementById("related-insights-grid");
      if (!grid) return;
      if (!Array.isArray(SECUREVISION.insights)) return;

      var currentSlug = document.body.getAttribute("data-article") || "";
      var currentArticle = SECUREVISION.insights.find(function (a) { return a.slug === currentSlug; });
      var currentCategory = currentArticle ? currentArticle.category : "";
      var currentTags = currentArticle ? currentArticle.tags : [];

      var pool = SECUREVISION.insights.filter(function (a) { return a.slug !== currentSlug; });

      function shuffle(arr) {
        var a = arr.slice();
        for (var i = a.length - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1));
          var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        }
        return a;
      }

      function score(article) {
        var s = 0;
        if (article.category === currentCategory) s += 10;
        currentTags.forEach(function (tag) {
          if (article.tags.indexOf(tag) !== -1) s += 2;
        });
        return s;
      }

      var picks = shuffle(pool).sort(function (a, b) { return score(b) - score(a); }).slice(0, 3);

      grid.innerHTML = picks.map(function (a) {
        var img = a.image
          ? "<img src=\"/images/insights/" + a.image + "\" alt=\"" + a.title + "\" class=\"related-card-img\"/>"
          : "<div class=\"related-card-img-placeholder\"></div>";
        return "<a href=\"/insights/" + a.slug + ".html\" class=\"related-article-card\">" +
          img +
          "<div class=\"related-card-body\">" +
          "<div class=\"related-card-cat\">" + a.category + "</div>" +
          "<p class=\"related-card-title\">" + a.title + "</p>" +
          "<span class=\"related-card-cta\">Read article &rarr;</span>" +
          "</div>" +
          "</a>";
      }).join("");
    })();
  }


    // ── Related Guides auto-renderer ────────────────────────────────
    // Fires on any page with id="related-guides-grid" and
    // <body data-guide="[slug]">. Renders 3 guide cards using the
    // standard .guide-card structure from sv-resources.css.
    (function () {
      var grid = document.getElementById("related-guides-grid");
      if (!grid) return;
      if (!Array.isArray(SECUREVISION.guides)) return;

      // Apply grid layout class
      grid.className = "guides-grid";

      var currentSlug = document.body.getAttribute("data-guide") || "";
      var currentGuide = SECUREVISION.guides.find(function (g) { return g.slug === currentSlug; });
      var currentTags = currentGuide ? currentGuide.tags : [];

      var pool = SECUREVISION.guides.filter(function (g) { return g.slug !== currentSlug; });

      function shuffle(arr) {
        var a = arr.slice();
        for (var i = a.length - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1));
          var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        }
        return a;
      }

      function score(g) {
        var s = 0;
        currentTags.forEach(function (tag) {
          if (g.tags.indexOf(tag) !== -1) s += 2;
        });
        return s;
      }

      var picks = shuffle(pool).sort(function (a, b) { return score(b) - score(a); }).slice(0, 3);

      var imgMap = {
        "burglar-alarm-guide":                 "/images/insights/alarm-internet-cut-siren.webp",
        "cctv-guide":                          "/images/resources/guides/cctv/hero-cctv.webp",
        "door-access-guide":                   "/images/insights/how-card-access-works-feature.webp",
        "intercom-guide":                      "/images/solutions/condominiums/akuvox-visitor-call-panel-condominium-lobby.webp",
        "auto-gate-guide":                     "/images/resources/guides/autogate/hero-auto-gate.webp",
        "wifi-network-guide":                  "/images/resources/guides/network/hero-wifi-network.webp",
        "office-telephone-guide":              "/images/resources/guides/telephony/fanvil-x6u-desk-phone.webp",
        "security-renovation-guide":           "/images/resources/guides/renovation/hero-security-renovation.webp",
        "how-to-evaluate-security-contractor": "/images/insights/break-in-nearby-security-review-feature.webp"
      };

      grid.innerHTML = picks.map(function (g) {
        var img = imgMap[g.slug] || "";
        return "<a href=\"/resources/guides/" + g.slug + ".html\" class=\"guide-card\">" +
          "<div class=\"guide-card-img-wrap\">" +
          (img ? "<img src=\"" + img + "\" alt=\"" + g.title + "\" loading=\"lazy\"/>" : "") +
          "<span class=\"guide-badge\">" + g.category + "</span>" +
          "</div>" +
          "<div class=\"guide-card-body\">" +
          "<h3>" + g.title + "</h3>" +
          "<hr/>" +
          "<div class=\"guide-meta\"><span>Read Guide &rarr;</span></div>" +
          "</div>" +
          "</a>";
      }).join("");
    })();

    if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", runHydration);
  } else {
    runHydration();
  }

})();
  
