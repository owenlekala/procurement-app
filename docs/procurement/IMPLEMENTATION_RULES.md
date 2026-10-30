# Implementation rules

These rules apply to the planned `tag_procurement` app through its future app-level instruction bridge. Read the [accepted product baseline](PRODUCT_REQUIREMENTS.md) and the relevant task before implementation.

1. Keep pure decisions in domain policies, orchestration/transactions in application services, Frappe persistence and external communication in adapters. Thin controllers must still validate ordinary saves.
2. Own a separate application. Do not put procurement in payroll or marketing, modify framework core, or silently overwrite another app's navigation.
3. Complete vertical slices: schema, command, permissions, UI, exceptions, recovery and meaningful tests. Empty handlers and success-only paths are incomplete.
4. Use native Desk and active website theme components. Scope new CSS; never introduce a second shell or framework.
5. Treat company, vendor membership, assignment, envelope stage and document sensitivity as server-enforced boundaries. Hiding a button is not permission enforcement.
6. Block managed-field changes through REST, Data Import, bulk edit, alternate portal endpoints and direct controller saves. Use supported hooks and scoped permission functions; never trust client-supplied actor/company.
7. Require distinct actors for sensitive approval stages. Policy changes cannot authorise self-approval of vendor activation, awards, bank changes or payments.
8. Freeze published requirements, submitted responses, tender terms, evaluation criteria and decision snapshots. Revisions create new records; material edits invalidate pending approval.
9. Validate deadlines against authoritative server time inside the submission transaction. Lock resource counters and allocations; rely on database uniqueness as well as prechecks.
10. Persist business work before enqueue; enqueue after commit and recover from the database. Never hold business locks across email, storage scanning or other network I/O.
11. Preserve sealed commercial content across files, generic APIs, history, comments, realtime, print, reports and exports. Opening is a controlled audited command.
12. Reuse ERPNext financial validation and ledgers. Never create a parallel payment or stock ledger or let a portal user submit accounting documents.
13. Recheck current compliance and authority before award/order creation; preserve historical submissions when a vendor later expires.
14. Keep uploads private, quarantine until scanned, escape user content and redact secrets. Synthetic test records must not contain real banking or tax data.
15. Preserve administrator customisations; repeat install/migrate and prove backup restore on a disposable site.
16. Update owning specifications and acceptance coverage with each change. Keep implementation tasks open until recorded execution evidence passes.
17. Keep shared guidance in indexes and substantive definitions in their owning specifications; retain feature-specific actions/failures instead of copying common paragraphs. Documentation validation establishes specification structure only. Never claim production qualification without the [release gates](OPERATIONS_AND_RELEASE.md).
