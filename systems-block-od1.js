(function () {
  "use strict";

  /* ─── SYSTEMS DATA ───────────────────────────────────────────────────
     Master data for all 6 system cards.
     Keys match data-systems and data-desc-[key] attribute values.

     Card name labels updated May 2026 to match nav-footer.js:
       Entry Access (was Entry & Access Control)
       IP Telephony (was IP Phone & Communications)
       Management Platforms (was Platform & Management)

     Grid order preserved: Premises, Entry Access, Vehicle (row 1)
                           IP Telephony, Network, Platform (row 2)
  ──────────────────────────────────────────────────────────────────── */
  var SYSTEMS = {
    "premises": {
      href:  "/systems/premises-security.html",
      img:   "/images/systems/premises-security-singapore-rel.webp",
      alt:   "Premises Security — CCTV, Alarms & Sensors",
      name:  "Premises Security",
      desc:  "CCTV, AI analytics, burglar alarms, and sensors — monitor your property and detect what matters.",
      badge: ""
    },
    "entry-access": {
      href:  "/systems/entry-access-control.html",
      img:   "/images/systems/entry-access-control-singapore-rel.webp",
      alt:   "Entry Access — Biometrics & Intercom",
      name:  "Entry Access",
      desc:  "Door access, biometrics, intercom, and visitor management — control who enters and track movement.",
      badge: ""
    },
    "vehicle-lpr": {
      href:  "/systems/vehicle-lpr-management.html",
      img:   "/images/systems/vehicle-lpr-management-singapore-rel.webp",
      alt:   "Vehicle & LPR Management — Auto-gates & Barriers",
      name:  "Vehicle & LPR Management",
      desc:  "Auto-gates, barriers, LPR, and car park systems — automate vehicle flow and reduce guard dependency.",
      badge: ""
    },
    "ip-telephony": {
      href:  "/systems/ip-phone-communications.html",
      img:   "/images/systems/ip-phone-communications-singapore-rel.webp",
      alt:   "IP Telephony — IPPBX & Desk Phones",
      name:  "IP Telephony",
      desc:  "IP phones and IPPBX systems — replace legacy keyphones with modern, app-enabled communications.",
      badge: ""
    },
    "network": {
      href:  "/systems/network-infrastructure.html",
      img:   "/images/systems/network-infrastructure-singapore-rel.webp",
      alt:   "Network Infrastructure — Managed Switches & WiFi",
      name:  "Network Infrastructure",
      desc:  "Managed PoE switches, WiFi access points, and structured cabling — the IP foundation every system runs on.",
      badge: ""
    },
    "platform": {
      href:  "/systems/security-management-platform.html",
      img:   "/images/systems/security-management-platform-singapore-rel.webp",
      alt:   "Management Platforms — VESTA & HikCentral",
      name:  "Management Platforms",
      desc:  "VESTA, Milestone, HikCentral — connect every system into one operational view across your property.",
      badge: "Unifying Layer"
    }
  };

  /* Canonical key order — preserves grid row sequence */
  var KEY_ORDER = ["premises","entry-access","vehicle-lpr","ip-telephony","network","platform"];

  /* ─── RENDER ─────────────────────────────────────────────────────────
     Supported data-* attributes:
       data-eyebrow        Small label above heading
       data-heading        Section heading
       data-intro          Paragraph below heading
       data-cta            Optional CTA button label
       data-cta-href       Optional CTA button href (default: /systems/)
       data-systems        Comma-separated keys to show.
                           e.g. "premises,entry-access,vehicle-lpr"
                           Omit or "all" to show all 6 in canonical order.
       data-desc-[key]     Override description for a specific card.
                           e.g. data-desc-premises="Custom text..."
                           Falls back to master data desc if not provided.
  ──────────────────────────────────────────────────────────────────── */
  function renderBlock(el) {
    var eyebrow  = el.getAttribute("data-eyebrow")   || "";
    var heading  = el.getAttribute("data-heading")   || "Six System Groups. One Integrated Architecture.";
    var intro    = el.getAttribute("data-intro")     || "";
    var cta      = el.getAttribute("data-cta")       || "";
    var ctaHref  = el.getAttribute("data-cta-href")  || "/systems/";
    var sysAttr  = el.getAttribute("data-systems")   || "all";

    /* Resolve which keys to show */
    var keys = sysAttr === "all" ? KEY_ORDER.slice() : sysAttr.split(",").map(function(k){ return k.trim(); });

    /* Header */
    var headerHtml = "";
    if (heading) {
      headerHtml  = '<div class="section-header">';
      if (eyebrow) headerHtml += '<span class="eyebrow">' + eyebrow + '</span>';
      headerHtml += '<h2>' + heading + '</h2>';
      if (intro)   headerHtml += '<p class="section-intro">' + intro + '</p>';
      headerHtml += '</div>';
    }

    var colsAttr  = el.getAttribute("data-cols") || "";
    /* Grid — data-cols overrides auto logic.
       data-cols="2" forces 2-col; otherwise auto by count */
    var gridClass = colsAttr === "2" ? "grid-2" : (keys.length <= 2 ? "grid-2" : "sv-systems-grid");
    var cardsHtml = '<div class="' + gridClass + ' mt-48">';

    for (var i = 0; i < keys.length; i++) {
      var key = keys[i];
      var s = SYSTEMS[key];
      if (!s) continue;

      /* Per-page description override */
      var desc = el.getAttribute("data-desc-" + key) || s.desc;
      var badgeHtml = s.badge ? '<span class="sv-sys-badge">' + s.badge + '</span>' : '';

      cardsHtml +=
        '<a href="' + s.href + '" class="sv-sys-card' + (s.badge ? ' sv-sys-card--platform' : '') + '">' +
          '<div class="sv-sys-img"><img src="' + s.img + '" alt="' + s.alt + '" loading="lazy"></div>' +
          badgeHtml +
          '<h3>' + s.name + '</h3>' +
          '<p>' + desc + '</p>' +
          '<div class="sv-sys-link">Explore &rarr;</div>' +
        '</a>';
    }
    cardsHtml += '</div>';

    /* Optional CTA */
    var ctaHtml = cta ? '<div class="text-center mt-80"><a href="' + ctaHref + '" class="btn btn-primary">' + cta + '</a></div>' : "";

    /* Replace placeholder */
    var wrapper = document.createElement("div");
    wrapper.innerHTML = headerHtml + cardsHtml + ctaHtml;
    el.parentNode.replaceChild(wrapper, el);
  }

  /* ─── INIT ─────────────────────────────────────────────────────────── */
  document.addEventListener("DOMContentLoaded", function () {
    var blocks = document.querySelectorAll(".sv-systems-block");
    for (var i = 0; i < blocks.length; i++) { renderBlock(blocks[i]); }
  });

})();
