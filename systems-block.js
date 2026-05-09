(function () {
  "use strict";

  /* ─── SYSTEMS DATA ───────────────────────────────────────────────────
     Single source of truth for all 5 system cards.
     The platform card is always rendered separately as the unifying layer.
  ──────────────────────────────────────────────────────────────────── */
  var SYSTEMS = [
    {
      href: "/systems/premises-security.html",
      img:  "/images/systems/premises-security-singapore-rel.webp",
      alt:  "Premises Security — CCTV, Alarms & Sensors",
      name: "Premises Security",
      desc: "CCTV, AI analytics, burglar alarms, and sensors — monitor your property and detect what matters."
    },
    {
      href: "/systems/entry-access-control.html",
      img:  "/images/systems/entry-access-control-singapore-rel.webp",
      alt:  "Entry & Access Control — Biometrics & Intercom",
      name: "Entry &amp; Access Control",
      desc: "Door access, biometrics, intercom, and visitor management — control who enters and track movement."
    },
    {
      href: "/systems/vehicle-lpr-management.html",
      img:  "/images/systems/vehicle-lpr-management-singapore-rel.webp",
      alt:  "Vehicle & LPR Management — Auto-gates & Barriers",
      name: "Vehicle &amp; LPR Management",
      desc: "Auto-gates, barriers, LPR, and car park systems — automate vehicle flow and reduce guard dependency."
    },
    {
      href: "/systems/ip-phone-communications.html",
      img:  "/images/systems/ip-phone-communications-singapore-rel.webp",
      alt:  "IP Phone & Communications — IPPBX & Desk Phones",
      name: "IP Phone &amp; Communications",
      desc: "IP phones and IPPBX systems — replace legacy keyphones with modern office communications."
    }
  ];

  var PLATFORM = {
    href:  "/systems/security-management-platform.html",
    img:   "/images/systems/security-management-platform-singapore-rel.webp",
    alt:   "Security Management Platform — VESTA & HikCentral",
    name:  "Platform &amp; Management",
    badge: "Unifying Layer",
    desc:  "VESTA, Milestone, HikCentral — connect every system above into one operational view across your property. The intelligence layer that turns five separate systems into one coordinated security architecture."
  };

  /* ─── RENDER ─────────────────────────────────────────────────────────
     Reads data-* attributes from the placeholder div, builds the block,
     then replaces the placeholder with rendered HTML.
  ──────────────────────────────────────────────────────────────────── */
  function renderBlock(el) {
    var eyebrow = el.getAttribute("data-eyebrow") || "";
    var heading = el.getAttribute("data-heading") || "Five System Groups. One Integrated Architecture.";
    var intro   = el.getAttribute("data-intro")   || "";
    var cta     = el.getAttribute("data-cta")     || "";   /* optional "Explore all technologies →" link */
    var ctaHref = el.getAttribute("data-cta-href")|| "/systems/";

    /* Header — only rendered if heading exists */
    var headerHtml = "";
    if (heading) {
      headerHtml  = '<div class="section-header">';
      if (eyebrow) headerHtml += '<span class="eyebrow">' + eyebrow + '</span>';
      headerHtml += '<h2>' + heading + '</h2>';
      if (intro)   headerHtml += '<p class="section-intro">' + intro + '</p>';
      headerHtml += '</div>';
    }

    /* 4-card grid */
    var cardsHtml = '<div class="sv-systems-grid mt-48">';
    for (var i = 0; i < SYSTEMS.length; i++) {
      var s = SYSTEMS[i];
      cardsHtml +=
        '<a href="' + s.href + '" class="sv-sys-card">' +
          '<div class="sv-sys-img"><img src="' + s.img + '" alt="' + s.alt + '" loading="lazy"></div>' +
          '<h3>' + s.name + '</h3>' +
          '<p>' + s.desc + '</p>' +
          '<div class="sv-sys-link">Explore &rarr;</div>' +
        '</a>';
    }
    cardsHtml += '</div>';

    /* Platform card */
    var platformHtml =
      '<a href="' + PLATFORM.href + '" class="sv-sys-platform">' +
        '<div class="sv-sys-platform-img">' +
          '<img src="' + PLATFORM.img + '" alt="' + PLATFORM.alt + '" loading="lazy">' +
        '</div>' +
        '<div class="sv-sys-platform-body">' +
          '<span class="sv-sys-platform-badge">' + PLATFORM.badge + '</span>' +
          '<h3>' + PLATFORM.name + '</h3>' +
          '<p>' + PLATFORM.desc + '</p>' +
          '<div class="sv-sys-link">Explore &rarr;</div>' +
        '</div>' +
      '</a>';

    /* Optional CTA button */
    var ctaHtml = "";
    if (cta) {
      ctaHtml = '<div class="text-center mt-48"><a href="' + ctaHref + '" class="btn btn-primary">' + cta + '</a></div>';
    }

    /* Assemble and replace placeholder */
    var wrapper = document.createElement("div");
    wrapper.innerHTML = headerHtml + cardsHtml + platformHtml + ctaHtml;

    el.parentNode.replaceChild(wrapper, el);
  }

  /* ─── INIT ───────────────────────────────────────────────────────────
     Runs on DOMContentLoaded. Finds all .sv-systems-block placeholders.
  ──────────────────────────────────────────────────────────────────── */
  document.addEventListener("DOMContentLoaded", function () {
    var blocks = document.querySelectorAll(".sv-systems-block");
    for (var i = 0; i < blocks.length; i++) {
      renderBlock(blocks[i]);
    }
  });

})();
