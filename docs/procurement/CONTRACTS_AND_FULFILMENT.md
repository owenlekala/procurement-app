# Contracts, fulfilment and financial claims

Owners: PROC-R20–PROC-R25. Native ownership is defined in [ERPNext integration](ERPNext_INTEGRATION.md); authority in [policy](PROCUREMENT_POLICY.md). No portal action initiates a bank transfer.

## Contract formation

An accepted, unconditional award creates a procurement contract control record linked to a Supplier-party native Contract. The owned control record supplies buying company, award allocations, currencies, value ceiling, version, authorised signatories, signed-file evidence, obligations, milestones and approval history. The native Contract's `is_signed` flag alone is not procurement authorisation.

The contract manager prepares terms, start/end dates, service levels, required guarantees/insurance, dispute route, delivery schedule, acceptance conditions, payment schedule, advance recovery and retention/release conditions. Both parties' signed evidence is recorded and independently checked before activation. V1 records signed documents and acknowledgement; it makes no certified electronic-signature claim. A contract without complete financial treatment or required signed evidence cannot become Active.

A framework agreement may link a Purchasing Blanket Order. Each call-off has an approved order allocation, validity checks and remaining quantity/value. Lock the owned balance during draft creation and again at submission; reservations count pending order drafts so concurrent call-offs cannot oversubscribe. Expired/abandoned draft reservations release through an audited reconciliation command; submitted commitments release only through native cancellation/amendment evidence.

## Variation and termination

A variation freezes proposed scope, quantity, value, schedule and obligations; compare cumulative commitment against the original award and configured authority band. Independent approval updates the control revision and creates appropriate native amendments/drafts. No variation silently edits submitted PO/invoice rows. Material change beyond policy limits requires new sourcing. Preserve before/after values and supplier acceptance.

Renewals are explicit proposals with current compliance, budget and authority review, not auto-renewal by scheduler. Termination records effective date, unfulfilled obligations, approved settlement and downstream cancellation steps. A parent contract cannot claim Closed while open financial/return obligations remain; use Closing pending settlement. Suspended vendor status blocks new commitments but does not automatically void existing contracts or prevent settling legitimate liabilities.

## Goods execution

Create Purchase Orders through native mapping from opened approved quotations or approved direct-purchase requests. Vendor may acknowledge dates/quantities or propose delivery changes; internal buyer approves changes through the native amendment process.

The portal records dispatch advice and delivery evidence as a `PROC Fulfilment Submission`. Receiving staff verify quantities, location and inspection. Goods acceptance creates or links a native Purchase Receipt, retaining PO/item references. Stock receipt is never posted by the vendor. Support partial acceptance, damaged/rejected quantities, quality inspection, outstanding backorders and replacement deliveries. Returns use native return receipts and subsequent credit adjustments; aggregate accepted/returned quantities reconcile to native records.

## Services and contractor works

Each milestone has scope, planned dates, agreed value/quantity, evidence checklist, acceptance owner and payment eligibility. Vendors submit completion evidence; an assigned internal officer accepts, partially accepts or requests correction with reasons. An independent approver is required when the acceptance owner is the work requester or has a recorded conflict. Accepted quantities/value cannot exceed the approved milestone after variations.

Create native non-stock receipts where the site's configured service buying process requires them; otherwise service acceptance is the controlled invoice-match evidence. Do not fabricate warehouse movements for service work. Site access, safety, guarantees and insurance are category requirements or contract obligations. Subcontractor disclosure does not give the subcontractor access to the prime vendor's portal.

## Invoice claims and matching

A vendor creates an invoice claim with buying company, PO/contract, supplier invoice number/date, currency, line quantities/amounts/tax, file and relevant delivery/milestone references. Store a canonical invoice-number key (trim and casefold; retain punctuation) unique across the Supplier's non-cancelled claims and invoices for that company. Cross-check existing native Purchase Invoices even if created outside the portal. Fingerprint/file/value/date similarity raises a review warning; it never silently merges claims.

Validate currency, company, supplier, invoice dates and allocation bounds. Goods use three-way match against PO, net accepted receipts and invoice lines. Services use PO, approved service acceptance and invoice lines. Configured tolerances must be explicit per company; missing tolerances mean exact match at native precision. Native taxes/rounding remain authoritative. An approved exception identifies the discrepancy and independent finance approver; it cannot override a native financial validation failure.

The [data model](DATA_MODEL.md#contract-and-execution) owns claim state names. Vendor correction creates a new claim revision; submitted history remains. Approval creates at most one native invoice draft per approved claim revision. Finance reviews and submits using normal accounting permissions and controls. “Approved claim” is not “Posted invoice” or “Paid”.

Credit-note/return requests are separately linked to the original claim/invoice, internally reviewed and mapped to native return/credit documents. Amounts already invoiced, credited or pending in another approved claim are included in remaining-balance checks under lock.

## Advances, retentions and payment

Record payment milestones, advance limits/recovery and retention percentage/cap/release conditions in the approved contract schedule. Use native advances, allocations and configured accounts only after finance qualifies the exact posting method on the inspected ERPNext revision. A dedicated P7 task must provide worked ledger fixtures for each enabled template. Unsupported treatment leaves the template disabled, rather than creating a procurement-side balance pretending to be accounting.

Payment preparation requires a verified bank account and completed independent finance approval bound to payment content/account revision. Enforce the gate through owned hooks on the relevant native submit path, including REST/import; test the deployed native workflow. Execution occurs through existing finance/bank procedures. Payment approval does not prove bank settlement.

The portal shows invoice amount, credits, allocated payment, outstanding amount, due date, accounting posting state and “as of” time. “Settled in ERPNext” means native outstanding balance is zero; reversal/reconciliation can change it. A statement of actual bank clearance requires bank evidence outside v1. Never expose bank balances, other vendors' ledger rows or internal accounts.

## Performance and closeout

Contract managers create scorecard reviews from delivery timeliness, defects/returns, service acceptance and documented conduct, with evidence and an approved rubric. Preserve original values; allow vendor response and corrective-action tasks. A score alone does not automatically suspend a vendor or award a tender.

Closeout checks outstanding orders, returns, claims, retention, guarantees, disputes and evidence. Separate Operationally complete from Financially closed. Offboarding blocks future sourcing and revokes unnecessary memberships while retaining required audit/financial history under legal holds and configured retention.
