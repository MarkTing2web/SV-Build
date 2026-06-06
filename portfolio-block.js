(function () {
  "use strict";

  /* ─── PORTFOLIO PROJECT REGISTRY ────────────────────────────────────
     Master data for all portfolio case study pages.
     Each entry requires: slug, category, image, badge, title, text.

     category values (use for data-category on the block element):
       commercial | condominiums | data-centres | healthcare |
       industrial | institutions | managed-living | residential

     Pages excluded (no rel image available yet):
       healthcare/surya-home
       industrial/sta-compliance-imaging
       institutions/sengkang-interim-bus-interchange
       managed-living/scb-worker-dormitory-jalan-papan

     Version history:
       v1.0  May 2026   Initial build. All sectors covered.
                        Excludes 5 pages pending photography.
       v1.1  Jun 2026   Multi-category mode added.
                        data-categories (comma-separated) picks 1
                        project per listed category. Used on homepage
                        for the 6-sector cross-sell block.
  ─────────────────────────────────────────────────────────────────── */

  var PROJECTS = [

    /* ── COMMERCIAL ─────────────────────────────────────────────── */
    {
      slug:     "/portfolio/commercial/altitudex-sentosa-commercial.html",
      category: "commercial",
      image:    "/images/portfolio/commercial/altitudex-sentosa-rel.webp",
      badge:    "Commercial",
      title:    "AltitudeX Sentosa",
      text:     "Migrating a decade-old EntryPass system to ZKTeco CV Security — 50 doors, mixed credentials, zero operational disruption."
    },
    {
      slug:     "/portfolio/commercial/catholic-centre-security-partnership.html",
      category: "commercial",
      image:    "/images/portfolio/commercial/catholic-centre-rel.webp",
      badge:    "Commercial",
      title:    "Catholic Centre",
      text:     "A decade-long security partnership — complete fit-out for a 9-storey institutional hub, followed by CCTV and access upgrades in 2022 and 2024."
    },
    {
      slug:     "/portfolio/commercial/em-services-call-centre-redhill.html",
      category: "commercial",
      image:    "/images/portfolio/commercial/em-engineering-at-jalan-kilang-rel.webp",
      badge:    "Commercial",
      title:    "EM Services Call Centre",
      text:     "Biometric access and high-definition surveillance protecting high-density call centre operations at One@Redhill Centre."
    },
    {
      slug:     "/portfolio/commercial/hilton-singapore-orchard-fire-door.html",
      category: "commercial",
      image:    "/images/portfolio/commercial/hilton-singapore-orchard-rel.webp",
      badge:    "Commercial",
      title:    "Hilton Singapore Orchard",
      text:     "EM lock access control and fire alarm integration for 50+ emergency stairwell doors across Asia-Pacific's largest Hilton property."
    },
    {
      slug:     "/portfolio/commercial/scape-commercial.html",
      category: "commercial",
      image:    "/images/portfolio/commercial/scape-rel.webp",
      badge:    "Commercial",
      title:    "SCAPE Singapore",
      text:     "209 AI cameras, 37 biometric access points, and a Salesforce integration that automated credential management end-to-end across all six levels."
    },
    {
      slug:     "/portfolio/commercial/scape-smart-booking-access.html",
      category: "commercial",
      image:    "/images/portfolio/commercial/scape-rel.webp",
      badge:    "Commercial",
      title:    "SCAPE Smart Booking & Access",
      text:     "Connecting an online booking platform to physical room access — a confirmed reservation automatically becomes a valid entry credential."
    },
    {
      slug:     "/portfolio/commercial/st-engineering-mobility-cctv.html",
      category: "commercial",
      image:    "/images/portfolio/commercial/st-engineering-mobility-rel.webp",
      badge:    "Commercial",
      title:    "ST Engineering Mobility",
      text:     "28 cameras and a 32-channel NVR for a vehicle services facility — with a wireless bridge solving a cross-building cabling problem."
    },

    /* ── CONDOMINIUMS ───────────────────────────────────────────── */
    {
      slug:     "/portfolio/condominiums/clearwater-access-salto-partnership.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/the-clearwater-rel.webp",
      badge:    "Condominium",
      title:    "The Clearwater — Access Partnership",
      text:     "Eight years of security partnership — from a Salto Virtual Network installation in 2017 to a cloud-based Akuvox access upgrade in progress."
    },
    {
      slug:     "/portfolio/condominiums/clearwater-cctv-upgrade.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/the-clearwater-rel.webp",
      badge:    "Condominium",
      title:    "The Clearwater — CCTV Upgrade",
      text:     "Full IP CCTV upgrade completing a long-term security modernisation programme at The Clearwater condominium."
    },
    {
      slug:     "/portfolio/condominiums/country-grandeur-upper-thomson-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/country-grandeur-rel.webp",
      badge:    "Condominium",
      title:    "Country Grandeur",
      text:     "Restoring reliability to a boutique Upper Thomson estate with modernised visitor access and intercom infrastructure."
    },
    {
      slug:     "/portfolio/condominiums/d-elias-pasir-ris-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/d-elias-rel.webp",
      badge:    "Condominium",
      title:    "D'Elias Singapore",
      text:     "Future-proofing residential security with cloud-ready access management for a mid-rise condominium in Pasir Ris."
    },
    {
      slug:     "/portfolio/condominiums/high-oak-condominium-cctv.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/high-oak-condominium-rel.webp",
      badge:    "Condominium",
      title:    "High Oak Condominium",
      text:     "Full CCTV upgrade with colour night vision — super wide-angle cameras for the basement carpark and ColorVu for lobbies across a 194-unit Bukit Timah estate."
    },
    {
      slug:     "/portfolio/condominiums/hillview-park-cctv-upgrade.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/hillview-park-condo-rel.webp",
      badge:    "Condominium",
      title:    "Hillview Park",
      text:     "48-camera surveillance upgrade replacing legacy analogue systems with HD colour-at-night IP technology across three towers."
    },
    {
      slug:     "/portfolio/condominiums/idyllic-suites-geylang-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/idyllic-suites-rel.webp",
      badge:    "Condominium",
      title:    "Idyllic Suites",
      text:     "Credential overhaul and access modernisation for a 71-unit condominium in Geylang."
    },
    {
      slug:     "/portfolio/condominiums/light-cairnhill-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/light-cairnhill-rel.webp",
      badge:    "Condominium",
      title:    "Light@Cairnhill",
      text:     "Consolidating fragmented intercom and lift access systems into a single coordinated workflow for a 121-unit Cairnhill estate."
    },
    {
      slug:     "/portfolio/condominiums/mergui-mansions-novena-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/mergui-mansions-rel.webp",
      badge:    "Condominium",
      title:    "Mergui Mansions",
      text:     "System recovery and security restoration for a boutique Novena condominium after infrastructure failure."
    },
    {
      slug:     "/portfolio/condominiums/newton21-newton-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/newton21-rel.webp",
      badge:    "Condominium",
      title:    "Newton 21",
      text:     "Dual-infrastructure modernisation — replacing legacy intercom and access protocols while expanding site-wide CCTV visibility at a 69-unit Newton estate."
    },
    {
      slug:     "/portfolio/condominiums/rezi-3two-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/rezi32-rel.webp",
      badge:    "Condominium",
      title:    "Rezi 3Two",
      text:     "Complete new-build security installation — CCTV, card access, swing gate automation, and audio-video intercom for 65 freehold residents."
    },
    {
      slug:     "/portfolio/condominiums/suites-cairnhill-intercom-lpr.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/suites-cairnhill-rel.webp",
      badge:    "Condominium",
      title:    "Suites@Cairnhill",
      text:     "Akuvox video intercoms, mobile app entry, custom Mifare credentials, and LPR-enabled vehicle management for a boutique District 9 condominium."
    },
    {
      slug:     "/portfolio/condominiums/the-bale-intercom-cctv.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/the-bale-telok-kurau-rel.webp",
      badge:    "Condominium",
      title:    "The Bale",
      text:     "Replacing telephony intercom and upgrading CCTV for a 36-unit freehold estate in Bedok — new video access at every entry point and 15 fresh surveillance cameras."
    },
    {
      slug:     "/portfolio/condominiums/the-lviv-newton-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/the-lviv-rel.webp",
      badge:    "Condominium",
      title:    "L'viv Residences",
      text:     "Eliminating resident friction by replacing an obsolete intercom with a modern 2-wire retrofit — restoring reliable visitor communication at a 147-unit Newton estate."
    },
    {
      slug:     "/portfolio/condominiums/the-verte-telok-kurau-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/the-verte-rel.webp",
      badge:    "Condominium",
      title:    "The Verte",
      text:     "Upgrading from delayed telephony systems to instant visual access and mobile control for a boutique Telok Kurau condominium."
    },
    {
      slug:     "/portfolio/condominiums/village-pasir-panjang-condo.html",
      category: "condominiums",
      image:    "/images/portfolio/condominiums/the-village-at-pasir-panjang-rel.webp",
      badge:    "Condominium",
      title:    "The Village @ Pasir Panjang",
      text:     "Scalable security infrastructure for a low-rise luxury residential cluster — LPR vehicle management, intercom, and estate-wide CCTV."
    },

    /* ── DATA CENTRES ───────────────────────────────────────────── */
    {
      slug:     "/portfolio/data-centres/fort-data-centre-access-upgrade.html",
      category: "data-centres",
      image:    "/images/portfolio/data-centres/fort-data-centre-rel.webp",
      badge:    "Data Centre",
      title:    "FORT Data Centre — Access Upgrade",
      text:     "Upgrading access control infrastructure for a mission-critical data centre facility — precision engineering in a zero-tolerance environment."
    },
    {
      slug:     "/portfolio/data-centres/fort-st-engineering.html",
      category: "data-centres",
      image:    "/images/portfolio/data-centres/fort-st-engineering-rel.webp",
      badge:    "Data Centre",
      title:    "FORT by ST Engineering",
      text:     "Live-environment access control upgrade across active data hall floors."
    },

    /* ── HEALTHCARE ─────────────────────────────────────────────── */
    {
      slug:     "/portfolio/healthcare/sunlove-mental-wellness-centre-haig-road.html",
      category: "healthcare",
      image:    "/images/portfolio/healthcare/sunlove-rel.webp",
      badge:    "Healthcare",
      title:    "Sunlove Mental Wellness Centre",
      text:     "Sensitive security design for a mental wellness facility on Haig Road — balancing safety requirements with a therapeutic environment."
    },

    /* ── INDUSTRIAL ─────────────────────────────────────────────── */
    {
      slug:     "/portfolio/industrial/cogent-logistics-hub-cctv.html",
      category: "industrial",
      image:    "/images/portfolio/industrial/cogent-1-logistics-hub-rel.webp",
      badge:    "Industrial",
      title:    "Cogent Logistics Hub",
      text:     "CCTV surveillance across a major Singapore logistics hub — wide-area coverage for a large-footprint industrial facility."
    },
    {
      slug:     "/portfolio/industrial/cyrus-tech-industrial.html",
      category: "industrial",
      image:    "/images/portfolio/industrial/cyrus-tech-at-loyang-rel.webp",
      badge:    "Industrial",
      title:    "Cyrus Tech",
      text:     "Industrial security upgrade at Loyang — access control and surveillance for a technology facility in the eastern industrial belt."
    },
    {
      slug:     "/portfolio/industrial/hoy-san-industrial.html",
      category: "industrial",
      image:    "/images/portfolio/industrial/hoy-san-rel.webp",
      badge:    "Industrial",
      title:    "Hoy San Industrial",
      text:     "LPR-enabled vehicle barrier system and gate automation for an industrial facility — streamlining vehicle entry without a guardhouse queue."
    },
    {
      slug:     "/portfolio/industrial/mitsubishi-elevator-face-access-bms.html",
      category: "industrial",
      image:    "/images/portfolio/industrial/mitsubishi-elevator-singapore-rel.webp",
      badge:    "Industrial",
      title:    "Mitsubishi Elevator Singapore",
      text:     "Facial recognition access control integrated with BMS for Mitsubishi Elevator's Singapore facility."
    },
    {
      slug:     "/portfolio/industrial/multibase-construction-security-upgrade.html",
      category: "industrial",
      image:    "/images/portfolio/industrial/multibase-construction-rel.webp",
      badge:    "Industrial",
      title:    "Multibase Construction",
      text:     "Full security upgrade for a construction company facility — access control, surveillance, and perimeter protection."
    },
    {
      slug:     "/portfolio/industrial/smartflex-tampines.html",
      category: "industrial",
      image:    "/images/portfolio/industrial/smartflex-at-tampines-rel.webp",
      badge:    "Industrial",
      title:    "Smartflex Tampines",
      text:     "Security infrastructure for a Tampines industrial facility — CCTV and access control for a modern light industrial space."
    },
    {
      slug:     "/portfolio/industrial/sta-inspection-industrial.html",
      category: "industrial",
      image:    "/images/portfolio/industrial/sta-inspection-centre-sin-ming-rel.webp",
      badge:    "Industrial",
      title:    "STA Inspection Centre",
      text:     "Access control and surveillance for Singapore's vehicle inspection infrastructure — a critical public service facility at Sin Ming."
    },
    {
      slug:     "/portfolio/industrial/stmicroelectronics-loyang-perimeter-alarm.html",
      category: "industrial",
      image:    "/images/portfolio/industrial/st-microelectronics-loyang-rel.webp",
      badge:    "Industrial",
      title:    "STMicroelectronics Loyang",
      text:     "Perimeter alarm system for STMicroelectronics' Loyang facility — protecting a semiconductor manufacturing site with precision intrusion detection."
    },

    /* ── INSTITUTIONS ───────────────────────────────────────────── */
    {
      slug:     "/portfolio/institutions/catholic-centre-waterloo.html",
      category: "institutions",
      image:    "/images/portfolio/institutions/catholic-centre-waterloo-rel.webp",
      badge:    "Institution",
      title:    "Catholic Centre Waterloo",
      text:     "A decade-long security partnership for the Catholic Centre at 55 Waterloo Street — complete fit-out in 2014 followed by CCTV and access upgrades in 2022 and 2024."
    },
    {
      slug:     "/portfolio/institutions/changi-airport-lpr-barriers.html",
      category: "institutions",
      image:    "/images/portfolio/institutions/changi-airside-rel.webp",
      badge:    "Institution",
      title:    "Changi Airport — LPR Barriers",
      text:     "LPR-controlled vehicle barriers for airside access management at Changi Airport — precision vehicle flow control in a high-security environment."
    },
    {
      slug:     "/portfolio/institutions/cpf-maxwell-institution.html",
      category: "institutions",
      image:    "/images/portfolio/institutions/cpf-maxwell-rel.webp",
      badge:    "Institution",
      title:    "CPF Maxwell",
      text:     "Security infrastructure for a CPF Board facility at Maxwell — access control and surveillance for a high-footfall government service centre."
    },
    {
      slug:     "/portfolio/institutions/das-learning-centre-woodlands.html",
      category: "institutions",
      image:    "/images/portfolio/institutions/das-learning-centre-rel.webp",
      badge:    "Institution",
      title:    "DAS Learning Centre Woodlands",
      text:     "Security design for a specialist learning centre — balancing open access for students with controlled entry for staff and restricted areas."
    },
    {
      slug:     "/portfolio/institutions/my-world-preschool-cctv.html",
      category: "institutions",
      image:    "/images/portfolio/institutions/my-world-preschool-rel.webp",
      badge:    "Institution",
      title:    "My World Preschool",
      text:     "CCTV surveillance for a preschool campus — child-safe camera placement and coverage designed around safeguarding requirements."
    },
    {
      slug:     "/portfolio/institutions/sfx-retreat-centre-punggol.html",
      category: "institutions",
      image:    "/images/portfolio/institutions/st-francis-xavier-retreat-centre-rel.webp",
      badge:    "Institution",
      title:    "SFX Retreat Centre",
      text:     "Security for a religious retreat centre in Punggol — unobtrusive surveillance and access control for a contemplative environment."
    },

    /* ── MANAGED LIVING ─────────────────────────────────────────── */
    {
      slug:     "/portfolio/managed-living/nursing-hostel-jalan-seh-chuan.html",
      category: "managed-living",
      image:    "/images/portfolio/managed-living/nursing-hostel-at-jln-seh-chuan-rel.webp",
      badge:    "Managed Living",
      title:    "Nursing Hostel @ Jln Seh Chuan",
      text:     "Security infrastructure for a nursing hostel — access control and surveillance balancing resident welfare with operational oversight."
    },

    /* ── RESIDENTIAL ────────────────────────────────────────────── */
    {
      slug:     "/portfolio/residential/dunbar-walk-landed-home.html",
      category: "residential",
      image:    "/images/portfolio/residential/dunbar-walk-rel.webp",
      badge:    "Landed Home",
      title:    "22 Dunbar Walk",
      text:     "Security upgrade for a Dunbar Walk landed property — driveway surveillance, gate automation, and perimeter coverage."
    },
    {
      slug:     "/portfolio/residential/dyson-8-residences-landed-home.html",
      category: "residential",
      image:    "/images/portfolio/residential/dyson-8-rel.webp",
      badge:    "Landed Home",
      title:    "8 Dyson Road",
      text:     "Full residential security installation for a Dyson Road property — intercom, auto gate, and surveillance working as one system."
    },
    {
      slug:     "/portfolio/residential/lengkok-mariam-landed-home.html",
      category: "residential",
      image:    "/images/portfolio/residential/lengkok-mariam-rel.webp",
      badge:    "Landed Home",
      title:    "26 Lengkok Mariam",
      text:     "Residential security for a Lengkok Mariam landed home — camera coverage and access control designed around the property layout."
    },
    {
      slug:     "/portfolio/residential/merryn-road-landed-home.html",
      category: "residential",
      image:    "/images/portfolio/residential/merryn-road-rel.webp",
      badge:    "Landed Home",
      title:    "Merryn Road",
      text:     "Security upgrade for a Merryn Road property — replacing ageing infrastructure with a modern integrated system."
    },
    {
      slug:     "/portfolio/residential/shelford-landed-home.html",
      category: "residential",
      image:    "/images/portfolio/residential/shelford-rel.webp",
      badge:    "Landed Home",
      title:    "Shelford Road",
      text:     "Comprehensive security installation for a Shelford Road landed home — surveillance, intercom, and gate access working together."
    },
    {
      slug:     "/portfolio/residential/siglap-bank-landed-home.html",
      category: "residential",
      image:    "/images/portfolio/residential/siglap-bank-rel.webp",
      badge:    "Landed Home",
      title:    "29 Siglap Bank",
      text:     "Full security fit-out for a Siglap Bank landed property — camera positions designed around the driveway approach and perimeter."
    },
    {
      slug:     "/portfolio/residential/upper-east-coast-road-landed-home.html",
      category: "residential",
      image:    "/images/portfolio/residential/upper-east-coast-landed-upgrade-rel.webp",
      badge:    "Landed Home",
      title:    "Upper East Coast Road",
      text:     "Ten years of upgrades for a home that kept evolving — from ageing analogue CCTV to a gate motor that lasted a decade."
    }

  ];

  /* ─── FALLBACK CATEGORY ADJACENCY ───────────────────────────────
     If a category has fewer than 3 projects (after excluding self),
     pull from adjacent categories in this order.
  ─────────────────────────────────────────────────────────────────── */
  var FALLBACK_ORDER = {
    "commercial":     ["institutions", "industrial", "data-centres"],
    "condominiums":   ["residential", "managed-living", "commercial"],
    "data-centres":   ["industrial", "commercial", "institutions"],
    "healthcare":     ["managed-living", "institutions", "condominiums"],
    "industrial":     ["commercial", "data-centres", "institutions"],
    "institutions":   ["commercial", "industrial", "healthcare"],
    "managed-living": ["healthcare", "condominiums", "residential"],
    "residential":    ["condominiums", "managed-living", "healthcare"]
  };

  /* ─── HELPERS ────────────────────────────────────────────────────── */
  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = a[i]; a[i] = a[j]; a[j] = tmp;
    }
    return a;
  }

  function pickProjects(category, exclude, count) {
    count = count || 3;
    var pool = PROJECTS.filter(function (p) {
      return p.category === category && p.slug !== exclude;
    });

    /* Pad from fallback categories if needed */
    if (pool.length < count) {
      var fallbacks = FALLBACK_ORDER[category] || [];
      for (var i = 0; i < fallbacks.length && pool.length < count; i++) {
        var extra = PROJECTS.filter(function (p) {
          return p.category === fallbacks[i] && p.slug !== exclude;
        });
        pool = pool.concat(extra);
      }
    }

    return shuffle(pool).slice(0, count);
  }

  /* ─── RENDER ─────────────────────────────────────────────────────── */
  function renderBlock(el) {
    var categoriesAttr = el.getAttribute("data-categories") || "";
    var category = el.getAttribute("data-category") || "commercial";
    var exclude  = el.getAttribute("data-exclude")  || "";
    var heading  = el.getAttribute("data-heading")  || "Related Case Studies";
    var eyebrow  = el.getAttribute("data-eyebrow")  || "Next Steps in Discovery";
    var intro    = el.getAttribute("data-intro")    || "Explore how we have solved similar security challenges across Singapore.";
    var bgClass  = el.getAttribute("data-bg")       || "sv-section-grey";

    var multiMode = categoriesAttr !== "";
    var picks;

    if (multiMode) {
      /* Multi-category mode: pick 1 random project from each listed category */
      picks = [];
      var cats = categoriesAttr.split(",");
      for (var c = 0; c < cats.length; c++) {
        var cat = cats[c].trim();
        var pool = PROJECTS.filter(function(p) {
          return p.category === cat && p.slug !== exclude;
        });
        if (pool.length > 0) {
          picks.push(shuffle(pool)[0]);
        }
      }
    } else {
      picks = pickProjects(category, exclude, 3);
    }

    var cardsHtml = "";
    for (var i = 0; i < picks.length; i++) {
      var p = picks[i];
      cardsHtml +=
        '<a href="' + p.slug + '" class="card card-clickable related-project-card">' +
          '<img src="' + p.image + '" alt="' + p.title + '" loading="lazy">' +
          '<div class="related-project-body">' +
            '<span class="related-project-badge">' + p.badge + '</span>' +
            '<h3 class="related-project-title">' + p.title + '</h3>' +
            '<p class="related-project-text">' + p.text + '</p>' +
            '<span class="related-project-link">View Case Study &rarr;</span>' +
          '</div>' +
        '</a>';
    }

    /* Single-category mode only: pad to 3 if needed */
    if (!multiMode) while (picks.length < 3) {
      cardsHtml +=
        '<a href="/portfolio/" class="card card-clickable related-project-card">' +
          '<div class="related-project-body" style="display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:200px;text-align:center;">' +
            '<span class="related-project-badge">Portfolio</span>' +
            '<h3 class="related-project-title">Explore More Projects</h3>' +
            '<p class="related-project-text">Browse the full Securevision portfolio — case studies across every sector and property type.</p>' +
            '<span class="related-project-link">View All Projects &rarr;</span>' +
          '</div>' +
        '</a>';
      picks.push({}); /* prevent infinite loop */
    }

    var sectionHtml =
      '<section class="' + bgClass + ' section-spacing">' +
        '<div class="container">' +
          '<div class="section-header text-center">' +
            '<span class="eyebrow">' + eyebrow + '</span>' +
            '<h2>' + heading + '</h2>' +
            '<p class="text-left mt-16">' + intro + '</p>' +
          '</div>' +
          '<div class="grid-3 mt-48">' + cardsHtml + '</div>' +
        '</div>' +
      '</section>';

    var wrapper = document.createElement("div");
    wrapper.innerHTML = sectionHtml;
    el.parentNode.replaceChild(wrapper.firstChild, el);
  }

  /* ─── INIT ───────────────────────────────────────────────────────── */
  document.addEventListener("DOMContentLoaded", function () {
    var blocks = document.querySelectorAll(".sv-portfolio-block");
    for (var i = 0; i < blocks.length; i++) {
      renderBlock(blocks[i]);
    }
  });

})();
