/* ============================================================
   cctv-calculator.js
   CCTV Bandwidth & Storage Calculator
   Securevision Pte Ltd — securevision.com.sg

   Estimation model
   ─────────────────
   Bitrate basis:  ~1 Mbps per megapixel (H.264, medium scene,
                   15 fps reference). Consistent with Hikvision
                   and Seagate operational defaults.
   H.265:          50% of H.264 equivalent
   H.265+ (Smart): 35% of H.264 equivalent
   FPS scaling:    sub-linear — bitrate ∝ (fps/15)^0.7
   Storage:        1 Mbps continuous ≈ 0.45 GB/hour
   Capacity units: decimal (1 TB = 1,000 GB), matching
                   how drives are sold.
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    /* ── Reference tables ──────────────────────────────────── */

    const RES = [
        { v: '1mp',  label: '1MP (720p)',  base: 1.0 },
        { v: '2mp',  label: '2MP (1080p)', base: 2.0 },
        { v: '3mp',  label: '3MP',         base: 3.5 },
        { v: '4mp',  label: '4MP',         base: 4.0 },
        { v: '5mp',  label: '5MP',         base: 5.0 },
        { v: '6mp',  label: '6MP',         base: 6.0 },
        { v: '8mp',  label: '8MP (4K)',     base: 8.0 },
        { v: '12mp', label: '12MP',        base: 12.0 }
    ];

    const CODEC = [
        { v: 'h264',  label: 'H.264',          factor: 1.00 },
        { v: 'h265',  label: 'H.265',          factor: 0.50 },
        { v: 'h265p', label: 'H.265+ (Smart)', factor: 0.35 }
    ];

    const QUALITY = [
        { v: 'low',  label: 'Low — static / lower quality', factor: 0.70 },
        { v: 'med',  label: 'Medium — typical',             factor: 1.00 },
        { v: 'high', label: 'High — busy / max quality',    factor: 1.40 }
    ];

    const FPS_OPTIONS = [1, 2, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30];

    const MODE = [
        { v: 'cont',   label: 'Continuous (24/7)' },
        { v: 'sched',  label: 'Scheduled hours' },
        { v: 'motion', label: 'Motion / event' }
    ];


    /* ── State ─────────────────────────────────────────────── */

    let groups   = [];
    let advanced = false;
    let gid      = 0;

    function newGroup (preset) {
        return Object.assign({
            id:         ++gid,
            qty:        8,
            res:        '4mp',
            fps:        15,
            codec:      'h265',
            quality:    'med',
            mode:       'cont',
            schedHours: 12,
            dutyPct:    40,
            manualMbps: ''
        }, preset || {});
    }


    /* ── Calculation helpers ───────────────────────────────── */

    function fpsFactor (fps) {
        return Math.pow(fps / 15, 0.7);
    }

    function cameraBitrate (g) {
        if (advanced && g.manualMbps !== '' && !isNaN(parseFloat(g.manualMbps))) {
            return parseFloat(g.manualMbps);
        }
        const base = RES.find(r => r.v === g.res).base;
        const cf   = CODEC.find(c => c.v === g.codec).factor;
        const qf   = QUALITY.find(q => q.v === g.quality).factor;
        return base * fpsFactor(g.fps) * qf * cf;
    }

    function activeHoursPerDay (g) {
        if (g.mode === 'cont')   return 24;
        if (g.mode === 'sched')  return Math.min(24, Math.max(0, g.schedHours));
        if (g.mode === 'motion') return 24 * (Math.max(0, Math.min(100, g.dutyPct)) / 100);
        return 24;
    }

    function dailyGBperCamera (g) {
        return cameraBitrate(g) * 0.45 * activeHoursPerDay(g);
    }


    /* ── Formatting ────────────────────────────────────────── */

    function fmt (n, decimals) {
        return Number(n).toLocaleString('en-GB', {
            minimumFractionDigits: decimals,
            maximumFractionDigits: decimals
        });
    }

    function selectHTML (opts, selected, labelKey, valKey) {
        return opts.map(o => {
            const v = valKey    ? o[valKey]    : o;
            const l = labelKey  ? o[labelKey]  : o;
            return `<option value="${v}" ${String(v) === String(selected) ? 'selected' : ''}>${l}</option>`;
        }).join('');
    }


    /* ── Render groups ─────────────────────────────────────── */

    function renderGroups () {
        const host = document.getElementById('calc-groups');
        if (!host) return;
        host.innerHTML = '';

        groups.forEach(g => {
            const div = document.createElement('div');
            div.className = 'calc-group';
            div.innerHTML = `
                <div class="calc-field-grid">
                    <div class="calc-field">
                        <label>Number of cameras</label>
                        <input type="number" min="1" max="2000" value="${g.qty}"
                               data-f="qty" data-id="${g.id}" toolparamdescription="Total number of cameras in this group.">
                    </div>
                    <div class="calc-field">
                        <label>Resolution</label>
                        <select data-f="res" data-id="${g.id}" toolparamdescription="Resolution in Megapixels (1MP to 12MP).">
                            ${selectHTML(RES, g.res, 'label', 'v')}
                        </select>
                    </div>
                    <div class="calc-field">
                        <label>Frame rate (fps)</label>
                        <select data-f="fps" data-id="${g.id}" toolparamdescription="Frames per second (FPS) from 1 to 30.">
                            ${selectHTML(FPS_OPTIONS, g.fps)}
                        </select>
                    </div>
                    <div class="calc-field">
                        <label>Encoding / codec</label>
                        <select data-f="codec" data-id="${g.id}" toolparamdescription="Compression standard: H.264, H.265, H.265+.">
                            ${selectHTML(CODEC, g.codec, 'label', 'v')}
                        </select>
                    </div>
                    <div class="calc-field">
                        <label>Scene &amp; quality</label>
                        <select data-f="quality" data-id="${g.id}" toolparamdescription="Expected motion activity levels: Low, Medium, High.">
                            ${selectHTML(QUALITY, g.quality, 'label', 'v')}
                        </select>
                    </div>
                    <div class="calc-field">
                        <label>Recording mode</label>
                        <select data-f="mode" data-id="${g.id}">
                            ${selectHTML(MODE, g.mode, 'label', 'v')}
                        </select>
                    </div>
                    <div class="calc-field calc-cond ${g.mode === 'sched' ? 'show' : ''}"
                         data-cond="sched-${g.id}">
                        <label>Hours recorded per day</label>
                        <div class="calc-suffix-row">
                            <input type="number" min="1" max="24" value="${g.schedHours}"
                                   data-f="schedHours" data-id="${g.id}">
                            <span>hrs</span>
                        </div>
                    </div>
                    <div class="calc-field calc-cond ${g.mode === 'motion' ? 'show' : ''}"
                         data-cond="motion-${g.id}">
                        <label>Recording activity (motion)</label>
                        <div class="calc-suffix-row">
                            <input type="number" min="1" max="100" value="${g.dutyPct}"
                                   data-f="dutyPct" data-id="${g.id}">
                            <span>% of time</span>
                        </div>
                    </div>
                    <div class="calc-field calc-cond ${advanced ? 'show' : ''}"
                         data-cond="adv-${g.id}">
                        <label>Manual bitrate override</label>
                        <div class="calc-suffix-row">
                            <input type="number" min="0" step="0.1" placeholder="auto"
                                   value="${g.manualMbps}"
                                   data-f="manualMbps" data-id="${g.id}">
                            <span>Mbps/cam</span>
                        </div>
                    </div>
                </div>
                <p class="calc-group-preview">
                    Estimated per camera:
                    <strong>${fmt(cameraBitrate(g), 2)} Mbps</strong>
                    &nbsp;·&nbsp; ${fmt(dailyGBperCamera(g), 1)} GB/day
                </p>
            `;
            host.appendChild(div);
        });
    }


    /* ── Calculate and update results ──────────────────────── */

    function calculate () {
        let totBandwidth = 0;
        let totDailyGB   = 0;
        let tableRows    = '';

        groups.forEach(g => {
            const br    = cameraBitrate(g);
            const gbDay = dailyGBperCamera(g);
            const gBw   = br * g.qty;
            const gDay  = gbDay * g.qty;
            totBandwidth += gBw;
            totDailyGB   += gDay;

            tableRows += `
                <tr>
                    <td>${g.qty} &times; ${RES.find(r => r.v === g.res).label}
                        &nbsp;&middot;&nbsp; ${CODEC.find(c => c.v === g.codec).label}
                        &nbsp;&middot;&nbsp; ${g.fps}&thinsp;fps</td>
                    <td class="r">${fmt(br, 2)}&thinsp;Mbps</td>
                    <td class="r">${fmt(gBw, 1)}&thinsp;Mbps</td>
                    <td class="r">${fmt(gDay, 0)}&thinsp;GB</td>
                </tr>`;
        });

        const bdBody = document.getElementById('calc-bd-body');
        if (bdBody) bdBody.innerHTML = tableRows;

        /* Bandwidth */
        const bwVal  = document.getElementById('calc-bw-val');
        const bwUnit = document.getElementById('calc-bw-unit');
        if (bwVal && bwUnit) {
            if (totBandwidth >= 1000) {
                bwVal.textContent  = fmt(totBandwidth / 1000, 2);
                bwUnit.textContent = 'Gbps';
            } else {
                bwVal.textContent  = fmt(totBandwidth, 0);
                bwUnit.textContent = 'Mbps';
            }
        }

        /* Storage required */
        const retStr     = (document.getElementById('calc-retention') || {}).value || '';
        const hddStr     = (document.getElementById('calc-hdd')       || {}).value || '';
        const bothBlank  = retStr.trim() === '' && hddStr.trim() === '';
        const retention  = retStr.trim() !== ''
            ? Math.max(1, parseFloat(retStr))
            : (bothBlank ? 30 : null);
        const usingDefault = bothBlank;

        const stVal  = document.getElementById('calc-st-val');
        const stNote = document.getElementById('calc-st-note');
        let totalTB  = 0;

        if (retention !== null && totDailyGB > 0) {
            totalTB = (totDailyGB * retention) / 1000;
            if (stVal)  stVal.textContent  = totalTB >= 10 ? fmt(totalTB, 0) : fmt(totalTB, 1);
            if (stNote) stNote.textContent =
                `For ${retention} days${usingDefault ? ' (default \u2014 enter a value above to change)' : ''}
                 \u00b7 ${fmt(totDailyGB / 1000, 2)} TB added per day.`;
        } else {
            if (stVal)  stVal.textContent  = '\u2014';
            if (stNote) stNote.textContent = 'Enter a retention period above to see the storage you need.';
        }

        /* Recording duration from HDD */
        const hdd    = hddStr.trim() !== '' ? parseFloat(hddStr) : null;
        const dayVal  = document.getElementById('calc-day-val');
        const dayNote = document.getElementById('calc-day-note');

        if (hdd !== null && hdd > 0 && totDailyGB > 0) {
            const days = (hdd * 1000) / totDailyGB;
            if (dayVal)  dayVal.textContent  = fmt(days, 0);
            if (dayNote) dayNote.textContent =
                `A ${fmt(hdd, 1)}\u00a0TB usable array, at this camera load.`;
        } else {
            if (dayVal)  dayVal.textContent  = '\u2014';
            if (dayNote) dayNote.textContent =
                'Enter your recorder\u2019s usable capacity above to see how long it will last.';
        }

        /* Summary subtitle */
        const totalCams = groups.reduce((s, g) => s + (parseInt(g.qty) || 0), 0);
        const resSub = document.getElementById('calc-res-sub');
        if (resSub) {
            resSub.textContent =
                `${totalCams} camera${totalCams !== 1 ? 's' : ''} \u00b7 ${fmt(totDailyGB / 1000, 2)}\u00a0TB recorded per day.`;
        }

        /* Proposal CTA — prefill query string for /contact-gateway */
        const proposalBtn = document.getElementById('calc-proposal-btn');
        if (proposalBtn) {
            proposalBtn.href =
                `/contact-gateway?intent=cctv-calculator`
                + `&cameras=${totalCams}`
                + `&storage=${totalTB.toFixed(1)}TB`
                + `&retention=${retention || ''}d`
                + `&bandwidth=${Math.round(totBandwidth)}Mbps`;
        }
    }


    /* ── Event listeners ───────────────────────────────────── */

    function refresh () { renderGroups(); }

    /* Group input delegation */
    const groupsEl = document.getElementById('calc-groups');
    if (groupsEl) {
        groupsEl.addEventListener('input', e => {
            const id = e.target.dataset.id;
            const f  = e.target.dataset.f;
            if (!id || !f) return;

            const g = groups.find(x => x.id == id);
            if (!g) return;

            if (f === 'manualMbps') {
                g[f] = e.target.value;
            } else if (e.target.type === 'number') {
                g[f] = e.target.value === '' ? '' : parseFloat(e.target.value);
            } else {
                g[f] = e.target.value;
            }

            /* Re-render if mode changes (shows/hides conditional fields) */
            if (f === 'mode') {
                refresh();
            } else {
                /* Update just this group's preview without full re-render */
                const allGroups = document.querySelectorAll('.calc-group');
                const idx = groups.indexOf(g);
                if (allGroups[idx]) {
                    const preview = allGroups[idx].querySelector('.calc-group-preview');
                    if (preview) {
                        preview.innerHTML =
                            `Estimated per camera: <strong>${fmt(cameraBitrate(g), 2)} Mbps</strong>`
                            + `&nbsp;&middot;&nbsp; ${fmt(dailyGBperCamera(g), 1)} GB/day`;
                    }
                }
            }
        });
    }

    /* Advanced toggle */
    const advEl = document.getElementById('calc-adv');
    if (advEl) {
        advEl.addEventListener('change', e => {
            advanced = e.target.checked;
            refresh();
        });
    }

    /* Calculate button */
    const calcBtnEl = document.getElementById('calc-btn');
    if (calcBtnEl) {
        calcBtnEl.addEventListener('click', () => {
            calculate();
            const area = document.getElementById('calc-results-area');
            if (area) {
                area.style.display = 'block';
                setTimeout(() => {
                    area.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }, 50);
            }
        });
    }


    /* ── Initialise ────────────────────────────────────────── */

    groups.push(newGroup({ qty: 8, res: '4mp', fps: 15, codec: 'h265', quality: 'med' }));
    renderGroups();

});
