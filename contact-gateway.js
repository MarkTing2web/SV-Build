/**
 * SOURCE TRACKING — populates hidden fields from URL params and document.referrer
 */
document.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    document.getElementById('hidden_intent').value      = params.get('intent')       || '';
    document.getElementById('hidden_referrer').value    = document.referrer          || '';
    document.getElementById('hidden_source_page').value = window.location.pathname;
    document.getElementById('hidden_utm_source').value  = params.get('utm_source')   || '';
    document.getElementById('hidden_utm_medium').value  = params.get('utm_medium')   || '';
    document.getElementById('hidden_utm_campaign').value= params.get('utm_campaign') || '';
});

/**
 * INTENT HANDLER — pre-fills form fields and updates heading based on ?intent= param
 */
document.addEventListener('DOMContentLoaded', () => {
    const params    = new URLSearchParams(window.location.search);
    const intent    = params.get('intent');
    if (!intent) return;

    const formTitle      = document.getElementById('proposalFormTitle');
    const propertySelect = document.getElementById('prop_type');

    const checkInterests = (values) => {
        values.forEach(val => {
            const cb = document.querySelector(`input[name="interests"][value="${val}"]`);
            if (cb) cb.checked = true;
        });
    };

    const setTitle = (text) => {
        if (formTitle) formTitle.textContent = text;
    };

    switch (intent) {

        /* ── SECTOR / PERSONA INTENTS (from sector pages and persona sub-pages) ── */
        case 'condo-assessment':
            setTitle('Estate Advisory — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Condominium';
            checkInterests(['CCTV', 'Access', 'Intercom']);
            break;

        case 'residential-assessment':
            setTitle('Home Security — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Private Home';
            checkInterests(['CCTV', 'Alarms', 'Intercom']);
            break;

        case 'commercial-assessment':
            setTitle('Business Security — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Commercial/Retail';
            checkInterests(['CCTV', 'Access']);
            break;

        case 'industrial-assessment':
            setTitle('Industrial Facility — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Industrial';
            checkInterests(['CCTV', 'Access', 'Autogate']);
            break;

        case 'gov-assessment':
        case 'govt-office':
            setTitle('Government Office — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Institutions';
            checkInterests(['CCTV', 'Access']);
            break;

        case 'schools-education':
            setTitle('Education Facility — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Institutions';
            checkInterests(['CCTV', 'Access', 'Intercom']);
            break;

        case 'community-sites':
            setTitle('Religious & Community Site — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Institutions';
            checkInterests(['CCTV', 'Access']);
            break;

        case 'managed-living':
        case 'coliving-assessment':
            setTitle('Co-living Security — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Institutions';
            checkInterests(['CCTV', 'Access']);
            break;

        case 'dormitory-security':
            setTitle('Dormitory Security — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Institutions';
            checkInterests(['CCTV', 'Access']);
            break;

        case 'hostel-security':
            setTitle('Hostel Security — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Institutions';
            checkInterests(['CCTV', 'Access']);
            break;

        case 'healthcare-assessment':
            setTitle('Healthcare Facility — Request a Proposal');
            if (propertySelect) propertySelect.value = 'Institutions';
            checkInterests(['CCTV', 'Access', 'Intercom']);
            break;

        case 'cctv-assessment':
        case 'surveillance-assessment':
        case 'thermal-assessment':
        case 'ai-assessment':
            setTitle('Surveillance System — Request a Proposal');
            checkInterests(['CCTV']);
            break;

        case 'access-assessment':
            setTitle('Access Control — Request a Proposal');
            checkInterests(['Access']);
            break;

        case 'vehicle-assessment':
            setTitle('Vehicle Access — Request a Proposal');
            checkInterests(['Autogate']);
            break;

        case 'alarm-assessment':
            setTitle('Intrusion Alarm — Request a Proposal');
            checkInterests(['Alarms']);
            break;

        case 'perimeter-assessment':
            setTitle('Perimeter Security — Request a Proposal');
            checkInterests(['CCTV', 'Alarms']);
            break;

        case 'platform-assessment':
            setTitle('System Integration — Request a Proposal');
            checkInterests(['CCTV', 'Access']);
            break;

        case 'systems-assessment':
        case 'homepage-assessment':
            setTitle('Request a Proposal');
            break;

        /* ── ALARM / INTRUSION BRANDS ── */
        case 'ajax-enquiry':
            setTitle('Request a Proposal — AJAX Alarms');
            checkInterests(['Alarms']);
            break;

        case 'risco-enquiry':
            setTitle('Request a Proposal — RISCO');
            checkInterests(['Alarms']);
            break;

        case 'paradox-enquiry':
            setTitle('Request a Proposal — Paradox');
            checkInterests(['Alarms']);
            break;

        case 'dsc-enquiry':
            setTitle('Request a Proposal — DSC');
            checkInterests(['Alarms']);
            break;

        case 'ge-caddx-enquiry':
            setTitle('Request a Proposal — GE Caddx');
            checkInterests(['Alarms']);
            break;

        /* ── CCTV / SURVEILLANCE BRANDS ── */
        case 'hikvision-enquiry':
            setTitle('Request a Proposal — Hikvision');
            checkInterests(['CCTV']);
            break;

        case 'hanwha-enquiry':
            setTitle('Request a Proposal — Hanwha');
            checkInterests(['CCTV']);
            break;

        case 'uniview-enquiry':
            setTitle('Request a Proposal — Uniview');
            checkInterests(['CCTV']);
            break;

        case 'milesight-enquiry':
            setTitle('Request a Proposal — Milesight');
            checkInterests(['CCTV']);
            break;

        /* ── ACCESS CONTROL BRANDS ── */
        case 'suprema-enquiry':
            setTitle('Request a Proposal — Suprema');
            checkInterests(['Access']);
            break;

        case 'zkteco-enquiry':
            setTitle('Request a Proposal — ZKTeco');
            checkInterests(['Access']);
            break;

        case 'hid-enquiry':
            setTitle('Request a Proposal — HID');
            checkInterests(['Access']);
            break;

        case 'entrypass-enquiry':
            setTitle('Request a Proposal — EntryPass');
            checkInterests(['Access']);
            break;

        case 'microengine-enquiry':
            setTitle('Request a Proposal — MicroEngine');
            checkInterests(['Access']);
            break;

        case 'ebelco-enquiry':
            setTitle('Request a Proposal — Ebelco');
            checkInterests(['Access']);
            break;

        /* ── INTERCOM BRANDS ── */
        case 'aiphone-enquiry':
            setTitle('Request a Proposal — Aiphone');
            checkInterests(['Intercom']);
            break;

        case 'akuvox-enquiry':
            setTitle('Request a Proposal — Akuvox');
            checkInterests(['Intercom']);
            break;

        case 'kocom-enquiry':
            setTitle('Request a Proposal — Kocom');
            checkInterests(['Intercom']);
            break;

        /* ── AUTOGATE BRANDS ── */
        case 'faac-enquiry':
            setTitle('Request a Proposal — FAAC');
            checkInterests(['Autogate']);
            break;

        case 'mag-enquiry':
            setTitle('Request a Proposal — MAG');
            checkInterests(['Autogate']);
            break;

        case 'dormer-enquiry':
            setTitle('Request a Proposal — Dormer');
            checkInterests(['Autogate']);
            break;

        case 'gantrygo-enquiry':
            setTitle('Request a Proposal — GantryGo');
            checkInterests(['Autogate']);
            break;

        case 'viro-enquiry':
            setTitle('Request a Proposal — Viro');
            checkInterests(['Autogate']);
            break;

        /* ── IP PHONE BRANDS ── */
        case 'yealink-enquiry':
            setTitle('Request a Proposal — Yealink');
            checkInterests(['IP Phone']);
            break;

        case 'fanvil-enquiry':
            setTitle('Request a Proposal — Fanvil');
            checkInterests(['IP Phone']);
            break;

        case 'yeastar-enquiry':
            setTitle('Request a Proposal — Yeastar');
            checkInterests(['IP Phone']);
            break;

        /* ── PLATFORM / NETWORK ── */
        case 'omada-enquiry':
            setTitle('Request a Proposal — TP-Link Omada');
            break;

        case 'ruijie-enquiry':
            setTitle('Request a Proposal — Ruijie');
            break;

        case 'milestone-enquiry':
            setTitle('Request a Proposal — Milestone VMS');
            checkInterests(['CCTV']);
            break;
    }
});

// ── SUPABASE CLIENT ──
// Replace the two values below with your actual credentials from Supabase → Project Settings → API
const SUPABASE_URL  = 'https://bppajrzwqeysrnrucwka.supabase.co';
const SUPABASE_ANON = 'sb_publishable_vYPT4DLGgdCKutxGFAHSNA_K-IbcOdT';
const supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON);

// ── PROPOSAL FORM SUBMISSION ──
async function handleProposalSubmit(event) {
    event.preventDefault();

    // Honeypot check — bots fill this, humans don't
    const honeypot = document.querySelector('input[name="sv_human_verify"]');
    if (honeypot && honeypot.value !== '') return false;

    const form      = document.getElementById('proposalForm');
    const submitBtn = form.querySelector('button[type="submit"]');
    const btnText   = submitBtn.querySelector('span');

    // Collect checkbox values into a comma-separated string
    const interests = [...document.querySelectorAll('input[name="interests"]:checked')]
        .map(cb => cb.value).join(', ');

    // Validate at least one system is selected
    if (!interests) {
        alert('Please select at least one system you are interested in.');
        return false;
    }

    // Disable button to prevent double-submit
    submitBtn.disabled = true;
    btnText.textContent = 'Sending...';

    const payload = {
        name:         document.getElementById('name').value.trim(),
        phone:        document.getElementById('phone').value.trim(),
        email:        document.getElementById('email').value.trim(),
        prop_type:    document.getElementById('prop_type').value,
        location:     document.getElementById('location').value.trim(),
        interests:    interests,
        site_details: document.getElementById('site_details').value.trim(),
        intent:       document.getElementById('hidden_intent').value,
        referrer:     document.getElementById('hidden_referrer').value,
        source_page:  document.getElementById('hidden_source_page').value,
        utm_source:   document.getElementById('hidden_utm_source').value,
        utm_medium:   document.getElementById('hidden_utm_medium').value,
        utm_campaign: document.getElementById('hidden_utm_campaign').value,
    };

    const { error } = await supabaseClient
        .from('proposal_submissions')
        .insert([payload]);

    if (error) {
        console.error('Supabase error:', error);
        btnText.textContent = 'Something went wrong — please try again.';
        submitBtn.disabled = false;
        return false;
    }

    // Success — redirect to thank-you page
    window.location.href = '/contact-success.html';
    return false;
}