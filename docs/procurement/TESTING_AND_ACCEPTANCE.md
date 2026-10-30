# Testing and acceptance

Owner: PROC-R29, PROC-R30. Application tests have not run. Use synthetic identities, a disposable site, fake clock and deterministic mail/scanner adapters. Disable unexpected outbound networking. [Progress](PROGRESS.md) records execution evidence; this file owns acceptance definitions.

## Verification layers

Pure domain tests cover conditions, eligibility, policy bands, state transitions, hashing, scoring and allocation. Frappe integration tests use actual supported database constraints/locks, source hooks and native controllers. Browser tests exercise real Desk/website rendering, two companies/vendors, supported themes and responsive keyboard flows. Operational tests inject crashes/outages and qualify migrations, backup restore and limited authorised pilot.

P0 establishes exact lint/type/browser scripts. Future app checks from the confirmed Bench root include `bench --site <test-site> run-tests --app tag_procurement` and `bench build --app tag_procurement`; placeholders require actual disposable identifiers. No script or working runtime is claimed to exist yet.

## Acceptance scenarios

### PROC-A01

**Foundation and migrations.** Install on a fresh compatible site with ERPNext and no payroll/marketing app. Verify dependency errors, owned roles/navigation and built assets. Run install seeds/migrate twice; alter an administrator-owned navigation preference and repeat. Assert no duplicate records, no erased customisations, no unrelated repository changes and a discoverable app-level handbook bridge. Record exact commits, image digests, runtime versions and commands.

### PROC-A02

**Native UI and accessibility.** Capture every Desk/portal destination against same-version Buying and active website references at 1440px, 1024px and 390px. Exercise supported light/dark themes, keyboard-only use, focus return, accessible validation, loading/empty/denied/network states and saved drafts. Assert native header/action/widget alignment, no global CSS leakage, no horizontal page overflow and no fabricated overview metrics.

### PROC-A03

**Company and organisation isolation.** Create TAG company A/B and vendors X/Y, one vendor approved only in A, a user with one company permission, and a user holding two explicit vendor memberships. Attempt direct IDs, link search, counts, dashboard drill-down, native Supplier routes, downloads, reports, exports and realtime across boundaries. Assert shared identity never grants B approval or evidence, and company suspension does not disable the global Supplier. Revocation must deny the next request.

### PROC-A04

**Identity, membership and ownership.** Attempt same-domain takeover, exact/ambiguous duplicate registration, invitation token replay/expiry, changed invitation target, self-granted Billing capability, last-owner removal and unauthorised ownership transfer. Assert generic claimant responses reveal no existing private organisation. Verify claimant-scoped identity uploads and global membership/account notices before any company approval, non-null command receipt scope/replay protection, independent duplicate/recovery evidence, explicit switching between authorised organisations and preserved historical authorship after membership revocation.

### PROC-A05

**Configurable requirement builder.** Publish base/category/work-type packs with conditional text/date/select/declaration/attachment questions; add a new ordinary requirement without code changes. Verify preview/server parity, stricter repeated-key resolution, hidden-field handling and version pinning. Reject unknown keys, cycles, invalid types/options, incompatible repeated definitions and over-limit conditions. Confirm new publication does not silently rewrite an existing submission and waivers cannot bypass identity or scanning.

### PROC-A06

**Registration, corrections and progress.** Register a synthetic verified vendor for two buying companies with different checklists. Save/reload, lose network during save, upload pending/clean/rejected files and submit with/without required declarations. Confirm immutable receipts, independent per-company progress, zero-required denominator text, and 100% completeness remaining distinct from approval. Request correction, resubmit a new revision and verify original answers/evidence remain auditable; applicant sees no internal note.

### PROC-A07

**Review, independent activation and rejection.** Assign sequential/quorum review stages, attempt unassigned and self-review, miss an approver, delegate within/outside authority and race two final approvals. Require all effective evidence-specific decisions and a distinct final actor; assert at most one Supplier link/company activation and atomic rollback if Supplier creation fails. Rejection/withdrawal closes tasks with safe reasons; resubmission resets only affected decisions unless a material change requires full review.

### PROC-A08

**Expiry, renewal, sharing and remediation.** Use a fake clock around document end-of-day expiry and waiver expiry, including a stopped scheduler. Confirm live eligibility blocks affected bids/awards/orders while preserving historical bids and settlement. Renew before/after expiry, suspend/reinstate, publish a new pack and explicitly migrate/remediate with acknowledgement/deadline. Grant/revoke cross-company evidence reuse and confirm receiving verification remains independent and legal holds preserve relied-on evidence.

### PROC-A09

**Bank verification and payment protection.** Propose a bank change and try to activate it as requester, ordinary compliance reviewer and generic REST/import caller. Require independent finance verification through a trusted contact and restricted proof access. Keep prior verified account historical, block affected new payment preparation while pending, and invalidate approval bound to an old account/payment revision. Confirm no full bank/tax PIN values in logs, snapshots, lists, email or ordinary exports.

### PROC-A10

**Supplier import and duplicate reconciliation.** Preview a synthetic UTF-8 CSV import containing valid, duplicate, ambiguous, malformed and existing Supplier rows; reject excessive rows/bytes and CSV submitted through ordinary vendor-file upload. Confirm a preview hash, crash/resume in batches and replay confirmation. Assert no duplicate legal identity/Supplier mapping, no automatic company approval, bank verification or portal membership. Preserve submitted financial records and audit native Supplier portal grants before launch; unsupported conflicting rows stay in a resolvable operation error state.

### PROC-A11

**Requests, estimates and budget controls.** Submit goods/service/works lines with valid and cross-company dimensions, zero/negative quantities, missing accounts and non-tender currency conversion. Confirm explicit gross approval basis, native Budget Stop/Warn/Ignore treatment, request approval versus commitment distinction and renewed checks at order submit. Race concurrent commitments; native budget checks must remain effective. Material amount/scope/company changes invalidate approval; finance reallocation is required for a native Stop.

### PROC-A12

**Sourcing routes, authority and exceptions.** Publish complete company/category threshold bands including boundary amounts. Reject overlaps, gaps, missing reviewer slots and authority expansion by delegation. Complete formal tender, unsealed RFQ and direct/emergency routes, including awards with valid native RFQ/quotation or exception sources and no fabricated tender/score records; prove required independent sensitive decisions, below-minimum-response exceptions and no duplicated native RFQ mail. Attempt policy bypass by omitting procurement links, native Desk/REST/import, request splitting and expired exception use; managed-company guards must reject it.

### PROC-A13

**Publication, visibility and re-tendering.** Publish approved public/invited tenders with scoped lots, requirements, currency and deadlines; reject invalid ordering, missing panel, incomplete policy and stale publication hashes. Guests see only safe public fields/files and cannot discover invited identifiers. Test cancellation, no bids, insufficient responses and reissue under a new ID with history preserved. Structural criteria/currency/lot changes after submission cannot silently edit the original tender.

### PROC-A14

**Matching, invitations and subscriptions.** Seed vendors with intersecting/nonintersecting services/regions, approval in the wrong company, suspension, expired evidence and missing subscriptions. Verify explainable match/exclusion preview and dispatch-time eligibility. Replay publication events, withdraw optional subscriptions while queued, revoke invitations and switch digest timing. Assert one logical portal notice, bounded email attempts, essential participant notices despite opt-out and no invited-tender access merely from a matching subscription.

### PROC-A15

**Clarifications, addenda and briefings.** Ask vendor-private questions containing unsafe HTML/price content, publish sanitised shared answers, record briefing evidence and publish a material addendum with deadline review. Ensure no vendor identity or private price leaks in shared Q&A. A submitted bid becomes acknowledgement-required; acknowledgement alone leaves the old receipt/version immutable, reaffirmation creates a new version/receipt through the same gate, failed reaffirmation preserves the prior version, replacement before close works, unacknowledged bids get explicit nonresponsive review. Late/post-close addenda and unauthorised attendance edits fail; structural changes require reissue.

### PROC-A16

**Bid deadlines, receipts and immutable revisions.** Submit separate clean technical/commercial drafts just before, exactly at and after close with fake server time and delayed scheduler. Race duplicate requests, replacement, withdrawal and readiness-switch changes. Assert atomic receipt/envelopes, single effective version, successful replay with same key and conflict for changed payload. Failed replacement preserves old bid; lost response is resolved by receipt lookup. Vendors cannot mutate or withdraw received content after close.

### PROC-A17

**Sealed content and controlled opening.** Attempt pre-close and pre-commercial access via raw DocTypes, REST, File URLs, attachment metadata, Version, print/PDF, reports, exports, search, boot payloads, realtime and alternate RFQ paths. Require two distinct authorised officers and correct frozen manifest. Release technical only after close and commercial only for qualified bids after technical finalisation. Disqualified commercial stays sealed; vendor own access still requires capability. Record privileged infrastructure trust limits honestly.

### PROC-A18

**Conflicts, scoring, moderation and ranking.** Assign different evaluator criteria/lots; declare conflicts/recusal, try viewing others scores before own submission and editing submitted sheets. Verify quorum, immutable superseding corrections, published maxima/weights/pass gates, arithmetic-mean technical moderation and Incomplete treatment. Open qualified commercial offers, validate same-currency/tax basis and price formula, handle zero/negative/incomplete totals and four-decimal combined-score ties. Expire an offer before recommendation/award; require explicit vendor validity-extension consent and independent review in a separate revision, then renew the summary without changing sealed content. After timely award acceptance and contract activation, later orders follow contract validity rather than original offer expiry. Summary/source hash changes require renewed recommendation; no automated award or invented preference score.

### PROC-A19

**Awards, allocations, acceptance and complaints.** Race split awards against lot quantity/value ceilings; attempt proposer/recommendation-author approval, expired compliance, missing budget and stale summary. Exercise conditional award, condition clearance, vendor accept/decline/timeout, partial/no award, timely complaint hold and independent resolution. Assert no automatic runner-up award, no order while held, safe unsuccessful feedback, separately approved public results and native cancellation handling after withdrawal.

### PROC-A20

**Contracts, variations, guarantees and frameworks.** Create control/native contract from an accepted cleared award; test missing signatures, guarantee, insurance or financial template. Independently activate and vary scope/value/schedule with cumulative authority and vendor acceptance. Race framework call-offs, expire contract/guarantee, propose renewal/termination and preserve native amendments. No is_signed flag alone authorises purchasing; no closed contract with outstanding obligations/settlement. Submitted records retain revision history.

### PROC-A21

**Quotation/order mappings and native guards.** Create quotations only from released commercial offers or authorised unsealed sourcing. Retry order creation after a lost response and inject rollback before/after mapping. Assert at most one mapped draft, correct line references, locked reservations, native budget/quantity/company checks and current eligibility at submit. Attempt bypass through native CRUD/import with absent links. Cancel/amend a native order and reconcile source allowance without double-counting drafts and submitted commitments.

### PROC-A22

**Goods, service and works acceptance.** Acknowledge a PO or propose a schedule/quantity change, requiring internal review/native amendment before changed terms take effect. Submit dispatch/partial delivery/milestone evidence as a vendor and confirm no stock/acceptance posting. Internally inspect, partially accept, reject, return and replace goods; complete service/works acceptance with independent conflict review and no fabricated warehouse movement. Assert line bounds, linked native receipt/inspection, clean evidence, backlog and reversal constraints after invoicing. Reported completion and accepted work remain separate in UI and reports.

### PROC-A23

**Invoice claims, matching, credits and duplicates.** Submit claims with duplicate portal/native invoice keys, mismatched supplier/company/currency, excess quantities, unaccepted services, invalid taxes and missing evidence. Test exact/default and configured tolerance matching, independent discrepancy exception, correction revision, dispute and credit request. Crash/retry native invoice draft creation; assert one draft per approved revision and no portal submit/post capability. Concurrent claims cannot consume the same remaining allowance twice; native validation remains authoritative.

### PROC-A24

**Payment status, reversals and independent approval.** Prepare native payments with pending/unverified bank changes, same proposer/approver, modified content and stale bank revision through all native entry paths. Require valid independent approval and finance permissions. Post synthetic invoice/credit/payment allocation, reverse/cancel and reconcile. Portal displays currency, outstanding/allocated amounts and as-of accounting state only; zero outstanding does not assert actual bank clearance. No mark-paid or execute-transfer endpoint exists.

### PROC-A25

**Performance, disputes, closeout and offboarding.** Derive evidence-backed timeliness/quality/service reviews from accepted and returned work; record vendor response and corrective action. A score cannot auto-award/suspend. Attempt closeout with outstanding claim, guarantee, retention, return or dispute; require Operationally complete versus Financially closed distinction. Offboard/revoke access while preserving legitimate settlement, authored evidence, configured retention and legal holds.

### PROC-A26

**Durable automation and notification recovery.** Validate every allowlisted trigger/action, depth/step bound and cycle rejection; simulation makes no mutations. Publish a new rule while old runs wait and retain old version. Inject rollback, commit-before-enqueue loss, duplicate events, worker death, stale lease, SMTP rejection and timeout after possible acceptance. Assert one logical task/portal effect, at most five mail attempts with four proven-safe retries, no retry of potentially accepted mail, evidence-backed Unknown reconciliation and dispatch-time scope/subscription checks. Automation cannot approve/open/post/pay.

### PROC-A27

**Report reconciliation and private exports.** Seed known multi-company fixtures including bid revisions, cancelled/reissued tenders, split awards, partial returns, amended orders, credits and reversed payments. Reconcile cards/report rows to authorised source/native finance values. Assert identical drill-down predicates, explicit denominators/as-of basis, N/A versus Unknown, no mixed-currency sum or false savings. Revoke export access mid-generation/download and test formula escaping/private output and no sealed/bank fields.

### PROC-A28

**Security, uploads, retention and audit.** Attempt XSS, CSRF, guessed IDs, excessive queries, malicious/oversize/mismatched MIME uploads, scan outage, raw private URLs, evidence reassignment and managed-field edits via all alternate paths. Test quotas, clean-before-submit, download authorisation after revocation and no-store caching. Preview/execute cleanup with holds and identity-verified access/erasure requests. Confirm append-only redacted audit and no bid/bank secrets in logs, source snapshots or browser storage.

### PROC-A29

**Operational, capacity, upgrade and restore qualification.** Use the documented synthetic load/concurrency targets on recorded staging resources; measure latency, memory, lock contention, query plans and queue age. Stop workers/scheduler/scanner/storage/mail and exercise readiness/incident recovery without backdating bids. Migrate twice and restore populated DB/files/key material into isolation with features/outbound disabled; reconcile mappings, receipt hashes and possible mail acceptance before enablement. Run a limited explicitly authorised pilot and record release owners/remaining blockers.

### PROC-A30

**Documentation structure and semantic coverage.** Run the checked-in validator for exact file inventory, links/anchors/source paths, unique IDs, task dependencies/cycles, requirement-to-task-to-acceptance traceability, all Desk/portal destinations and flow diagrams. Review state/authority/time/sealing/financial definitions semantically and render diagrams/UI during implementation qualification. Deliberately corrupt in-memory links/dependencies/IDs, copy shared prose and omit a requirement’s task mapping to verify checker failure. Documentation success never checks an application task or substitutes for runtime tests.

## Repeatable documentation validation

From the workspace root run:

```sh
python3 docs/procurement/validate_docs.py
python3 docs/procurement/validate_docs.py --self-test
```

The checker reads files only and fails on inventory, relative links/anchors, source references, unknown/duplicate IDs, task contract/dependencies/cycles, missing traceability/screen/flow coverage, misplaced task checkboxes, malformed code fences, repeated substantive paragraphs or mismatched per-requirement traceability. The self-test introduces nine in-memory faults without changing documents, including copied prose within/across files and an incomplete per-requirement task mapping. Its expected inventory is explicit, so intentional additions require updating it.

The checker validates Mermaid source structure, not graphical rendering, and cannot prove runtime authorisation or semantic correctness. Review the owning policies for agreement, then render diagrams/screens when an appropriate runtime is available. Record this limitation honestly rather than declaring application release readiness.

## Evidence requirements

Capture test commands/results, app commits/image, synthetic fixture basis, acceptance IDs, screenshots/artifacts, unresolved failures and next action in [progress](PROGRESS.md). Only [phase task definitions](tasks/README.md) own completion checkboxes. Required live checks unavailable means the affected task remains open; passing offline documentation checks qualifies only the handbook.
