# Reporting and metric definitions

Owner: PROC-R27. Native Script Reports and Workspace widgets use the same permission-scoped query services. Definitions below are intended calculations, not measured results. Dates use the selected company timezone and explicit inclusive-start/exclusive-end ranges.

## Operational and procurement reports

- **Application ageing:** current open applications by stage/company/category; age from current submission, stage age from latest routing event. Show initial application elapsed time separately. Approved/rejected/withdrawn applications leave the open denominator.
- **Vendor compliance:** distinct company/organisation/category approvals as-of time, with Active/Hold/Suspended/Unverified/Closed and explicit expired evidence. Shared vendors across companies are not counted as unique legal vendors unless the report says so.
- **Request and sourcing cycle:** approved requests and time from request submit→approval→publication→award acceptance→first order. Incomplete intervals are outstanding, not zero durations; direct purchase/RFQ/formal tender are separate cohorts.
- **Tender participation:** eligible invited organisations, invitations accepted by email adapter, submitted vendor heads, effective bids, withdrawals/nonresponsive decisions and qualified bids. Bid revisions do not inflate bidder counts; public page views are not identified vendors.
- **Evaluation progress:** assigned score sheets due/submitted/effective, quorum and stage. No score/price detail before caller-specific release. Zero/incomplete panels never appear complete.
- **Awards:** independently approved allocation amounts by company/currency/category/organisation, conditional/offered/accepted/withdrawn separated. Pending award amounts are not actual spend or booked commitments.
- **Contract and order exposure:** approved ceiling, draft reservations, native submitted orders net of cancellations, remaining allowance and accepted fulfilment. Explain forecast versus ERPNext commitment basis; avoid counting a PO and its amended predecessor twice.
- **Delivery/service performance:** promised versus actual accepted dates, accepted/rejected/returned quantities, overdue open quantities, milestone value and documented review rubric. Missing delivery dates remain Unknown, not on-time.
- **Invoice exceptions and payment ageing:** claims by match outcome/status; posted native invoices net of credits, due and outstanding amounts as-of. Payment Entry allocation and reversal determine settlement projection; no implied bank-clearance claim.
- **Automation/delivery health:** oldest work, retries, Unknown mail, bounce/failed essential notices, scanner delay and overdue review tasks. SMTP Accepted, Delivered where evidence exists, and Read portal notifications remain distinct measures.

## Amounts and historical basis

Always display currency. Group totals by currency; company-currency views use stored native rates/dates and disclose basis. Do not convert bid comparisons with live exchange rates. “Savings” is not a default KPI: an estimate-versus-award variance is labelled variance, with its baseline and scope, never a proven realised saving.

Current operational reports apply live permissions and status. Historical reports use source versions, event timestamps and authoritative cancellation chains. An as-of financial report must use native supported ledger/report semantics rather than today's outstanding amount relabelled historically. If historical reconstruction is unsupported, expose current-as-of-now only and state the limit.

## Drill-down, exports and reconciliation

Counts and detail use identical predicates. Auditor/manager aggregate access does not automatically grant bank data, envelope content, private reviewer notes or other companies. Exports persist a filtered manifest and initiating authority, run in batches, escape CSV formulas and produce private files. Recheck permission on generation/download; revoke access after membership/assignment changes.

Acceptance fixtures include duplicate events, bid replacement, cancelled/reissued tenders, split awards, partial receipts/returns, amended orders, credit notes, reversed payments and multiple companies/currencies. Reconcile each card/report with authorised source rows and native financial reports before accepting it. Metric definitions and filter/time basis are visible through report help, not hidden in implementation comments.
