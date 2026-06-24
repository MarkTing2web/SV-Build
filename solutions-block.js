(function () {
  "use strict";

  /* ─── SOLUTIONS MASTER DATA ──────────────────────────────────────────
     All 8 property type cards.
     Each entry has: key, href, img, alt, name, desc (generic fallback).
     Per-page custom descriptions are passed via data-desc-[key] on the
     placeholder div and override the generic desc when present.
  ──────────────────────────────────────────────────────────────────── */
  var SOLUTIONS = {
    "residential": {
      href: "/solutions/residential",
      img:  "/images/solutions/hero-solutions/landed-home-security-singapore-rel.webp",
      alt:  "Landed home security Singapore",
      name: "Landed & Residential",
      desc: "Bungalows, semi-detached, and terrace homes — integrated alarm and CCTV for perimeter and interior protection."
    },
    "condominiums": {
      href: "/solutions/condominiums",
      img:  "/images/solutions/hero-solutions/condominium-estate-security-singapore-rel.webp",
      alt:  "Condominium estate security Singapore",
      name: "Condominiums & MCSTs",
      desc: "MCSTs, managing agents, and strata estates — estate-wide systems managed from a central operations layer."
    },
    "commercial": {
      href: "/solutions/commercial",
      img:  "/images/solutions/hero-solutions/commercial-security-singapore-rel.webp",
      alt:  "Commercial building security Singapore",
      name: "Offices & Commercial",
      desc: "Offices, hotels, retail shops, and commercial buildings — layered security across tenancies and common areas."
    },
    "industrial": {
      href: "/solutions/industrial",
      img:  "/images/solutions/hero-solutions/industrial-security-singapore-rel.webp",
      alt:  "Industrial estate security Singapore",
      name: "Industrial & Logistics",
      desc: "Factories, warehouses, logistics hubs, and tech parks — large-scale perimeter and operational security."
    },
    "institutions": {
      href: "/solutions/institutions",
      img:  "/images/solutions/hero-solutions/institutional-security-singapore-rel.webp",
      alt:  "Institutional building security Singapore",
      name: "Institutions & Government",
      desc: "Schools, government offices, churches, and civic facilities — compliance-grade systems for public environments."
    },
    "healthcare": {
      href: "/solutions/healthcare",
      img:  "/images/solutions/hero-solutions/healthcare-security-singapore-rel.webp",
      alt:  "Healthcare and nursing home security Singapore",
      name: "Healthcare",
      desc: "Nursing homes, day care centres, and specialist care facilities — patient safety and duty-of-care systems."
    },
    "managed-living": {
      href: "/solutions/managed-living",
      img:  "/images/solutions/hero-solutions/managed-living-security-singapore-rel.webp",
      alt:  "Managed living and dormitory security Singapore",
      name: "Managed Living",
      desc: "Worker dormitories, co-living apartments, and managed hostels — access control and monitoring for high-occupancy sites."
    },
    "data-centres": {
      href: "/solutions/data-centres",
      img:  "/images/solutions/hero-solutions/data-centre-security-singapore-rel.webp",
      alt:  "Data centre physical security Singapore",
      name: "Data Centres",
      desc: "Colocation, enterprise, and hyperscale facilities — physical access audit trails and compliance-grade surveillance."
    }
  };

  /* ─── RENDER ─────────────────────────────────────────────────────────
     Reads data-* attributes from the placeholder div, builds the block,
     then replaces the placeholder with rendered HTML.

     Supported data-* attributes:
       data-eyebrow        Small label above heading
       data-heading        Section heading (required)
       data-intro          Paragraph below heading
       data-solutions      Comma-separated list of solution keys
                           e.g. "residential,condominiums,commercial"
                           Omit or set to "all" to show all 8.
       data-desc-[key]     Override description for a specific card
                           e.g. data-desc-residential="Custom text..."
       data-cols           Grid columns: "2" (default) or "4"
  ──────────────────────────────────────────────────────────────────── */
  function renderBlock(el) {
    var eyebrow  = el.getAttribute("data-eyebrow")   || "";
    var heading  = el.getAttribute("data-heading")   || "Where This System Is Used";
    var intro    = el.getAttribute("data-intro")     || "";
    var solKeys  = el.getAttribute("data-solutions") || "all";
    var cols     = el.getAttribute("data-cols")      || "2";

    /* Resolve which solutions to show */
    var keys = [];
    if (solKeys === "all") {
      keys = Object.keys(SOLUTIONS);
    } else {
      keys = solKeys.split(",").map(function (k) { return k.trim(); });
    }

    /* Header */
    var headerHtml = '<div class="section-header">';
    if (eyebrow) headerHtml += '<span class="eyebrow">' + eyebrow + '</span>';
    headerHtml += '<h2>' + heading + '</h2>';
    if (intro)   headerHtml += '<p class="section-intro">' + intro + '</p>';
    headerHtml += '</div>';

    /* Grid */
    var gridClass = cols === "4" ? "grid-4" : "grid-2";
    var cardsHtml = '<div class="' + gridClass + ' mt-48">';

    for (var i = 0; i < keys.length; i++) {
      var key = keys[i];
      var s = SOLUTIONS[key];
      if (!s) continue;

      /* Per-page description override — falls back to master data */
      var desc = el.getAttribute("data-desc-" + key) || s.desc;

      cardsHtml +=
        '<a href="' + s.href + '" class="rel-card">' +
          '<div class="rel-card-img">' +
            '<img src="' + s.img + '" alt="' + s.alt + '" loading="lazy">' +
          '</div>' +
          '<h3>' + s.name + '</h3>' +
          '<p>' + desc + '</p>' +
          '<div class="rel-card-footer">Explore ' + s.name + ' →</div>' +
        '</a>';
    }

    cardsHtml += '</div>';

    /* Assemble and replace placeholder */
    var wrapper = document.createElement("div");
    wrapper.innerHTML = headerHtml + cardsHtml;
    el.parentNode.replaceChild(wrapper, el);
  }

  /* ─── INIT ─────────────────────────────────────────────────────────── */
  document.addEventListener("DOMContentLoaded", function () {
    var blocks = document.querySelectorAll(".sv-solutions-block");
    for (var i = 0; i < blocks.length; i++) {
      renderBlock(blocks[i]);
    }
  });

})();
