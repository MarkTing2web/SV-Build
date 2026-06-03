/* ============================================================
   /data/cctv-pricing.js
   CCTV System Cost Calculator — pricing configuration
   Securevision Pte Ltd · securevision.com.sg

   EDITING GUIDE
   ─────────────
   This is the single source of truth for all prices shown
   in the CCTV System Cost Calculator. Update values here;
   the calculator page reads them automatically on next load.

   Do NOT edit the calculator HTML to change prices.
   All prices in SGD, excluding GST.
   Update the lastUpdated field whenever you change a price.
   ============================================================ */

const CCTV_PRICING = {

    lastUpdated: 'June 2026',

    /* ── NVR units ─────────────────────────────────────────── */
    /* Typical spec, no specific brand. Includes PoE switch     */
    /* functionality built in for PoE NVR models.               */

    nvr: [
        { channels: 4,  label: '4-channel',  price: 280 },
        { channels: 8,  label: '8-channel',  price: 320 },
        { channels: 16, label: '16-channel', price: 480 },
        { channels: 32, label: '32-channel', price: 680 }
    ],

    /* ── Hard disks ────────────────────────────────────────── */
    /* Surveillance-grade, rated for 24/7 continuous write.     */
    /* Do not substitute desktop drives in CCTV recorders.      */

    hdd: [
        { tb: 1,  label: '1 TB',  price: 180 },
        { tb: 2,  label: '2 TB',  price: 220 },
        { tb: 4,  label: '4 TB',  price: 320 },
        { tb: 6,  label: '6 TB',  price: 380 },
        { tb: 8,  label: '8 TB',  price: 480 },
        { tb: 10, label: '10 TB', price: 680 }
    ],

    /* ── Cameras ───────────────────────────────────────────── */
    /* Per-unit supply price, typical specification.            */
    /* Does not imply a specific brand.                         */

    cameras: {
        '2mp': { label: '2MP camera (1080p)', price: 120 },
        '4mp': { label: '4MP camera',         price: 220 }
    },

    /* ── Installation ──────────────────────────────────────── */
    /* perCamera: labour + materials per camera point           */
    /* Includes: Cat6 UTP cabling, PVC conduit, PoE connection, */
    /*           mounting hardware, bracket, cable termination.  */
    /* Assumes standard runs up to 80m. Longer runs, external   */
    /* conduit, or ceiling void work quoted separately.          */
    /*                                                           */
    /* setup: recorder configuration, camera naming, motion     */
    /* detection setup, remote viewing configuration, handover. */

    installation: {
        perCamera:        150,
        setupProgramming: 400
    },

    /* ── Estimate range ────────────────────────────────────── */
    /* Applied to the calculated sub-total to produce a low/    */
    /* high range. Reflects variability in site conditions,     */
    /* cable routing difficulty, and access requirements.        */

    rangeFactorLow:  0.85,
    rangeFactorHigh: 1.15,

    /* ── Disclaimer text ───────────────────────────────────── */
    /* Shown verbatim on the calculator page.                   */

    disclaimers: {
        estimate:     'This is an indicative estimate only. Actual costs depend on site conditions, cable routing complexity, access requirements, and final confirmed specifications. A site survey is required for an accurate quotation.',
        hdd:          'Hard disk must be surveillance-grade (24/7 continuous write rated). Do not use desktop-class drives in CCTV recorders.',
        installation: 'Installation rates assume Cat6 UTP on PVC conduit with cable runs up to 80m. Longer runs, external conduit work, ceiling void access, or high-level mounting are quoted separately.',
        gst:          'All prices exclude prevailing GST.',
        brand:        'Specifications are typical for the category. No specific brand is implied. Final brand and model selection subject to site requirements and availability.'
    }

};
