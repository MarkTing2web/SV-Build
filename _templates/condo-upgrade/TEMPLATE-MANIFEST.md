# Condo Upgrade page templates (from Nathan Place)

Source: the live Nathan Place pages in SV-Build, copied 9 Nov 2026 and converted to placeholders.
Nothing here is live. These files are not linked from the site and are not published until copied.

## Files
| Template file | Copy to (new condo) |
|---|---|
| pages/index.html | /{{CONDO_SLUG}}/index.html (home + registration form) |
| pages/how-it-works/index.html | /{{CONDO_SLUG}}/how-it-works/index.html |
| pages/faq/index.html | /{{CONDO_SLUG}}/faq/index.html |
| pages/confirmed/index.html | /{{CONDO_SLUG}}/confirmed/index.html |
| pages/feedback/index.html | /{{CONDO_SLUG}}/feedback/index.html |
| sv-condo-template.css | /sv-{{CONDO_SLUG}}.css (class prefix `np-` can stay) |
| dashboard/index.html | /internal/condo/{{CONDO_SLUG}}/index.html |
| akuvox-smartplus-user-guide.pdf | /{{CONDO_SLUG}}/ (attached to the welcome email; change only if the equipment differs) |

## Placeholders already in the files (search and replace)
{{CONDO_NAME}} {{CONDO_SLUG}} {{P}} (database prefix, e.g. nathan_place) {{ADDRESS}} (full line, e.g. "18 Nathan Road, Singapore") {{ADDRESS_SHORT}}
{{SUPABASE_URL}} {{SUPABASE_PUBLISHABLE_KEY}} (ask the user; the publishable key is safe in a page)
{{REG_PERIOD}} (e.g. "30 Sep – 18 Oct 2026") {{VERIFY_DATE}} / {{VERIFY_DATE_LONG}} {{ACTIVATE_DATE}} / {{ACTIVATE_DATE_LONG}}
{{INSTALL_PERIOD}} {{GO_LIVE}} / {{GO_LIVE_LONG}} {{HELP_DATE_LONG}} (on-site help day)
{{BRIEFING_1}} / {{BRIEFING_2}} (e.g. "Saturday, 10 October 2026 at 11:00 am")
{{ADDON_PRICE}} (optional add-on price, e.g. S$580) {{UNIT_COUNT}} (dashboard total units) {{GOOGLE_REVIEW_URL}} (Securevision's Google review link; the same for every condo)
{{BLOCK_OPTIONS}} (comment above the first Block option: add one option per block)

## Still Nathan Place specific: edit by hand
1. Equipment text and counts on the home page, how-it-works and FAQ: Akuvox X915 (11 units, Lobbies 1 to 3 and Main Gate), Akuvox A05C (5 units, 4 side gates and gym), 16 pedestrian access points, LPR, SmartPlus app, S562W indoor monitor. Replace with the new condo's equipment or delete the card.
2. Block list: the Block select (Blk 16, Blk 18) and the database check constraint.
3. Times and dates not covered by a placeholder: the 6:00 pm to 9:00 pm help session, the short dates in "What happens next" (10 Oct, 15 Oct, 18 Oct, 20 Oct, 21 Oct) and the timeline step dates.
4. Add-on pricing detail: the installation range "S$150 to S$300 before GST" and the cabling statement.
5. FAQ answers that quote Nathan Place specifics (gates, lobbies, gym, LPR start date, tenants rules). Read every FAQ answer.
6. Images: /images/{{CONDO_SLUG}}/ needs the condo exterior (hero and og:image), the X915, A05C, S562W, LPR camera, barrier gate and app screenshots. Reuse the Nathan Place images only for the same equipment.
7. Meta tags: title, description, canonical and og tags carry the condo name and dates.
8. Registration wording "Registration closes 18 October" is a deliberate stated date: the form itself never closes.

## Form rules built into pages/index.html (do not remove)
Up to 4 App Users per unit; App User 1 is the Master User (Owner, Main Occupant or Main Tenant) with administrative rights; slots already taken greyed out via RPC {{P}}_unit_slots; "Are you the Master User?" confirmation that moves details to the first free slot of 2 to 4; "Not the Master User? Register as App User 2, 3 or 4" link; live duplicate-email check inside the household and a server check via RPC {{P}}_emails_taken; add-on tick box for the Master User only; honeypot field sv_human_verify; 4 second minimum; PDPA consent required; thank-you panel with summary and What happens next.
