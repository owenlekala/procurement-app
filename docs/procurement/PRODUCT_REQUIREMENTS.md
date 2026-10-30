# Product requirements

Status: accepted design baseline, 27 October 2026, based on the user's requested handbook and selected scope. See [ADR-001](decisions/ADR-001-APP-AND-DESIGN-BASELINE.md).

## Goal and audiences

A company registers once, supplies the requirements configured by each TAG buying company, tracks review, becomes an approved vendor and receives matching opportunities. Internal teams request goods/services/works, obtain authority, run defensible sourcing, evaluate bids, award work and manage execution through ERPNext accounting.

Personas: applicant/vendor owner and contributor; requester; buyer; compliance reviewer; procurement manager; assigned evaluator and opening officer; contract manager; receiving officer; finance reviewer and payment approver; read-only auditor; technical administrator. Permissions are owned by [access policy](PERMISSIONS_AND_PRIVACY.md).

Success means an authorised team can complete every lifecycle and exception using native screens, explain each decision, retrieve a complete audit trail and recover interrupted work without duplicate commitments or unauthorised disclosure.

## Requirement register

- **PROC-R01 — Foundation:** Separate app; pinned compatible Frappe/ERPNext v16; repeatable install/migrate and no payroll/marketing dependency.
- **PROC-R02 — Native UI:** Consistent Desk shell, widgets, forms, lists and reports; themed accessible vendor portal.
- **PROC-R03 — Company boundaries:** Shared vendor identity with independently scoped buying-company approvals, budgets, tenders and financial access.
- **PROC-R04 — Identity and membership:** Verified accounts, explicit organisation membership, duplicate review and recoverable ownership transfer.
- **PROC-R05 — Requirement builder:** No-code versioned questions, conditional documents, applicability, verification, review stages and waivers.
- **PROC-R06 — Registration and progress:** Resumable applications, submissions, corrections, applicant-visible timeline and clear next actions.
- **PROC-R07 — Review and activation:** Assigned review stages, independent final approval, rejection, withdrawal and controlled Supplier activation.
- **PROC-R08 — Continuous compliance:** Verification evidence, expiry, renewal, remediation, suspension, reinstatement and explicit version migrations.
- **PROC-R09 — Bank verification:** Restricted proposed bank changes, independent verification and controlled ERPNext bank activation.
- **PROC-R10 — Existing supplier migration:** Previewed resumable imports, duplicate reconciliation and no automatic approval of legacy suppliers.
- **PROC-R11 — Requests and budgets:** Goods/services/works requests, project/cost-centre allocation, budget checks and approval before commitment.
- **PROC-R12 — Sourcing policy:** Configured company/value/category authority, formal tenders, simplified RFQs and audited direct/emergency exceptions.
- **PROC-R13 — Tender publication:** Approved immutable tender versions, public/invited visibility, lots, terms, deadlines and cancellation/re-tendering.
- **PROC-R14 — Opportunity matching:** Explainable category/coverage matching, approved-company invitations and optional job subscriptions.
- **PROC-R15 — Clarifications and addenda:** Shared answers, controlled changes, acknowledgements, briefing evidence and fair deadline review.
- **PROC-R16 — Sealed bid submission:** Separated technical/commercial envelopes, immutable receipt, atomic deadlines, revisions and withdrawal.
- **PROC-R17 — Controlled opening:** Post-close technical opening and commercial opening only for technically qualified bids; no ordinary-path leaks.
- **PROC-R18 — Evaluation:** Assigned conflict-free evaluators, frozen weighted criteria, moderation, price comparison and justified recommendation.
- **PROC-R19 — Award:** Independent decision, conditional/lot/split awards, allocation bounds, supplier acceptance, complaints and withdrawal.
- **PROC-R20 — Contracts:** Signed evidence, obligations, framework call-offs, variations, guarantees, expiry and termination.
- **PROC-R21 — Orders:** Idempotent linked ERPNext quotations/orders, budget/compliance gates and quantity/value reconciliation.
- **PROC-R22 — Fulfilment:** Partial goods receipts/inspection/returns and service/works milestone evidence with internal acceptance.
- **PROC-R23 — Invoice claims:** Vendor claims, matching, duplicate checks, disputes, credit-note requests and controlled invoice drafts.
- **PROC-R24 — Payment visibility:** Accounting-derived outstanding/paid status and independent payment approval; no portal payment execution.
- **PROC-R25 — Vendor performance:** Evidence-backed performance reviews, corrective action and governed closeout/offboarding.
- **PROC-R26 — Automation and notifications:** Versioned allowlisted rules, durable events/outbox, email/portal notices, preferences and recovery.
- **PROC-R27 — Reporting:** Permission-scoped reconciled metrics, currency-aware amounts and private bounded exports.
- **PROC-R28 — Security and privacy:** Least privilege, protected files/envelopes, audit, retention, legal holds and safe subject requests.
- **PROC-R29 — Operations and quality:** Observable workers, migration/restore/load/security qualification, pilot controls and release evidence.
- **PROC-R30 — Documentation governance:** Canonical linked handbook, stable IDs, phase gates, source references and truthful progress.

## Accepted defaults

- App `tag_procurement`, title/module/sidebar **TAG Procurement**; Frappe 16.53.0 and ERPNext 16.52.1 inspected baseline, compatibility target below v17.
- Multiple TAG buying companies per site, not independent customer tenants. Shared identity does not imply shared confidential evidence or company approval.
- Public and invitation-only formal tenders; approved status for the tender's company and required categories is necessary at bid submission and again before award/order.
- Private-company procurement policies, goods/services/works, technical-before-commercial evaluation for formal tenders. Simplified RFQs remain a separate unsealed sourcing route.
- English labels prepared for translation. Display `Africa/Johannesburg` with UTC offset; temporal API inputs use explicit offsets. Use UTC domain instants and a tested Frappe storage conversion, not naive server-local comparisons.
- Manual official-document verification; uploaded evidence is never itself a verified result. SA examples are editable policy templates, not legal conclusions.
- Independent approval of vendor activation, awards, bank changes and payments. Company amount thresholds, role assignments, budget actions, retention and complaint windows must be configured before live activation.
- Email and portal channels. Optional job subscriptions differ from essential workflow/contract notices. No notification contains bid prices or sensitive attachments.
- Private quarantined uploads. Initial supported business files: PDF/JPEG/PNG; structured bid prices are entered in controlled line tables. Default 10 MiB/file and 100 MiB/application submission or bid version, including referenced evidence; apply the same aggregate limit to its draft. Administrator may lower limits. Upper limits require capacity/security requalification. Executables, archives and macro documents are excluded. Administrative legacy Supplier import additionally accepts UTF-8 CSV through its dedicated operation, limited to 10 MiB/50,000 data rows with streaming parsing and row-level validation; this does not enable CSV in ordinary vendor uploads. Generated private export files are operation outputs, not vendor uploads.
- Approval chains have explicit users/roles, sequential stages, configured deadlines and no automatic approval on timeout. A material change restarts affected decisions.
- Existing vendor files require approved sharing grants before another buying company can reuse them. Reuse evidence does not transfer verification or approval.

## Out of initial scope

Public-sector policy packs; arbitrary scripts/SQL or AI decisions; n8n; WhatsApp/SMS; external verification APIs; external payment initiation; certified electronic signatures; supplier reverse auctions; joint-venture consortium bidding; foreign-currency bid conversion in formal tenders. Formal tenders require one published bidding currency; ERPNext supports authorised multi-currency purchasing outside that comparison.

Vendors may describe subcontractors as disclosures; a consortium requiring its own bid must register as a separately identifiable entity under an approved policy. Standard contract terms and ERPNext postings cover approved advances/retentions; unsupported financial treatment blocks that contract template rather than inventing ledger entries.

## Glossary

**Buying company:** a TAG legal entity represented by ERPNext Company. **Vendor organisation:** shared legal identity. **Company approval:** company/category-specific eligibility, not a Supplier flag. **Application revision:** editable response draft; **submission:** immutable response to resolved requirement versions. **Tender version:** immutable approved terms; **bid version:** immutable submitted envelopes. **Opening:** audited release to assigned reviewers. **Claim:** portal request for internal invoice review, not an accounting invoice. **Operation:** persisted application work; an RQ job is only its transport.
