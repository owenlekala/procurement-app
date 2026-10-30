# Native Desk and vendor portal design system

Owner: PROC-R02. [Desk index](pages/README.md) and [portal index](portal/README.md) own destinations. This specifies intended UI; runtime screenshots have not been collected.

## Shell and components

Desk uses an owned TAG Procurement Desktop Icon, Workspace Sidebar and Workspace registered with the inspected v16 metadata. Keep existing navbar/search/user menu, breadcrumbs, page titles and action placement. Use generated DocType/List/Report routes; verify actual shell navigation rather than hardcoding legacy paths. Sidebar visibility follows roles but server checks still apply.

Configuration/business records use native Form tabs, sections, columns, child tables and field descriptions. Queues use native List filters, paging, saved views and authorised actions. Overview uses permission-checked Number Cards and Dashboard Charts with drill-down matching the same company/time basis. Reports use native Script Reports. Dialogs use `frappe.ui.Dialog`; bounded custom evaluation/progress layouts use `frappe.ui.make_app_page` inside the native shell. Never expose restricted raw payload DocTypes through ordinary forms.

Portal uses Frappe website templates, navbar/footer/sidebar and the active Website Theme. It does not embed Desk or introduce a separate SPA. Reuse native website form controls, tables, alerts and buttons, with scoped enhancements for step progress, split bid preparation and evidence status. Theme branding changes apply through supported theme configuration, not copied global CSS.

## Tokens and visual language

Read actual installed spacing/type/icon definitions. Reuse tokens including `--fg-color`, `--text-color`, `--text-muted`, `--control-bg`, `--border-color`, `--radius` and `--radius-lg` where defined. Scope selectors under `.tag-procurement` for Desk and `.tag-procurement-portal` for website pages. Use app bundles and supported hooks; no hardcoded theme backgrounds, remote font dependency, global button overrides or second CSS framework.

Status always has text/icon meaning: Draft, Action required, Under review, Approved, On hold, Rejected, Closed. Do not use colour alone or conflate expiry, approval and completeness. Display company and organisation context near sensitive actions; retain it in mobile headers and confirmation dialogs. Currency and deadline timezone must accompany values.

## Layout blueprints

**Desk overview:** existing page header/company/date filters; responsive native card row; application/compliance and sourcing charts; “My pending actions” list; operational exceptions visible only to authorised operators. Cards are live scoped values or explicit unavailable states, never placeholder numbers.

**Application review:** native form header and state action; summary/company/requirement versions; tabs for responses, evidence, review decisions and audit; section-level correction actions. Confidential notes are a separate internal area, never reused as applicant feedback.

**Tender form:** tabs for scope/lots, eligibility/requirements, schedule/briefing, evaluation policy, panel, publication history and results. Prepublication review dialog displays exact version/hash, closing offset, audience mode and policy authority. No submitted envelopes appear as ordinary attachment rows.

**Portal registration:** labelled step list (Company, Categories/coverage, Requirements, Documents, Review/submit) beside the current form on desktop; single-column step heading/progress on mobile. Autosave status, unresolved items and next action remain visible without implying approval.

**Portal application progress:** summary status and next action; completeness counters; requirement/document review list; applicant-safe chronological timeline; corrections link back to the exact field/evidence. Both 100% complete and Under review can be shown simultaneously.

**Bid workspace:** tender/version/deadline context, Technical and Commercial tabs, per-tab completion and evidence status, addenda acknowledgement, review declaration and one Submit action. Commercial values never appear in technical previews. Receipt replaces submit after success; a replacement action explains that the old receipt remains effective until the replacement succeeds.

**Evaluation:** tender/lot and assignment context; released technical material next to native score controls; commercial pane absent until release. Moderation uses a bounded comparison grid after evaluator submission. Mobile stacks evidence and scoring with explicit navigation; retain unsaved scores and warn on conflicting revisions.

**Post-award portal:** order/milestone/claim summary with native-style tables, documented outstanding quantities and approved financial status; detail views distinguish vendor submission from internal acceptance/posting.

## Interaction and accessibility contract

Exactly one principal action per state. Other permitted actions sit in standard secondary/action menus. Confirmation identifies company, vendor, version, financial/deadline effect and whether approval is invalidated. Disable duplicate clicks while pending; server idempotency remains the protection. Background actions return durable operation IDs with reload-safe progress.

Loading preserves layout and announces progress politely. Empty states offer an authorised next action. Validation is associated with fields plus a summary that moves focus to the first error. Network errors preserve drafts and show last saved time; stale revision prompts refetch/compare before overwriting. Submission uncertainty shows “Checking receipt” with safe receipt lookup. A countdown is advisory and uses server time/offset; the receipt is authoritative.

Support keyboard-only flow, visible focus, labels, screen-reader status, accessible tables and dialogs, contrast in both supported themes, and non-colour status cues. Reference viewports: 1440px, 1024px and 390px. Large grids scroll within their container with labelled columns; no whole-page horizontal overflow. Sensitive tabs retain authorisation even if navigation state is manipulated.

## Visual acceptance

Capture same-version Buying Workspace, Supplier form/list, RFQ, PO, report and dialog plus active website reference. Compare procurement views under the same user, theme, zoom and viewport. Check navbar/header height, action alignment, typography, field spacing, borders, widget drill-down, focus, errors and responsive states. Verify light/dark Desk and each theme actually supported by the active website; add scoped dark tokens if the portal's active theme lacks required parity.

Attach comparisons to PROC-P1-004 and feature UI evidence. CSS class reuse is not proof of visual parity. All page-specific contracts below the indexes inherit these shared rules without duplicating them.
