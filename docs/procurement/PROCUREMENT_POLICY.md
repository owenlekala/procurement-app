# Procurement authority and sourcing policy

Owners: PROC-R07, PROC-R11, PROC-R12, PROC-R19, PROC-R24. This is private-company governance, not a public-sector compliance pack.

## Configured authority

Each buying company publishes a versioned policy defining category/work-type and inclusive lower/exclusive upper amount bands in company currency, sourcing route, quotation minimum, approval stages, final approver, budget action, complaint window and escalation recipients. Overlapping bands or missing coverage block publication. If a category override exists it must provide a complete band set; otherwise use the complete company default. No “first matching row” ambiguity. Zero-value requests require a configured band too.

The approval basis is the tax-inclusive gross commitment in company currency, including approved options, charges and variations. Use an explicit native currency conversion rate/date for non-tender purchases. Formal tenders require one published bid currency. Store amount/rate/basis in approval snapshots and preserve source currency alongside company currency. Never sum different currencies directly.

No monetary thresholds are invented by this handbook. Live request approval, sourcing publication and commitment fail closed when policy, accountable users, conversion basis or relevant financial dimensions are missing. Draft preparation remains available.

Request approval and purchasing authority are distinct. Sensitive final vendor activation, award, bank-change and payment approval always require an actor different from the proposer/initiator, regardless of configured low-value flexibility. Other chains may allow self-approval only where explicitly configured. An actor cannot approve multiple distinct-person slots of the same stage. An unavailable approver creates an escalation, never a timeout approval.

## Request and budget flow

Capture company, requester, department, purpose, category, goods/services/works lines, UOM/quantity, scope, specification attachments, required dates, location, project/cost centre, budget account and estimate. An approved native Material Request may be linked or created through the adapter. Service/works scopes use native non-stock items where financial mapping requires an Item.

Validate line dimensions belong to the company. Budget review uses native Budget behaviour at the applicable Material Request/Purchase Order/expense stages. Show estimate, current commitment and actual basis separately. An approved procurement request is planning authority, not a new ledger or an automatic budget reservation. Recheck budgets during award recommendation and native order submission. Concurrent commitments rely on qualified native budget enforcement; add an owned serialisation guard only if testing demonstrates a race, without replacing native calculations.

A native Stop cannot be bypassed by a procurement approval. Warn requires a recorded finance acknowledgement; Ignore must be an explicit company policy, never a silent default. To proceed past Stop, finance amends/reallocates the native budget through its authorised process and the procurement decision is rerun.

## Sourcing routes

**Formal tender:** publication approval, sealed technical/commercial envelopes, independent evaluation/award and contract/order handoff. Required for configured higher-risk/value/category bands.

**Simplified RFQ:** approved request, invited approved vendors, native RFQ/quotation comparison, documented compliance and delivery/price review, independent award authorisation. This route is openly unsealed; do not describe its ordinary Supplier Quotation data as confidential sealed bids. The procurement invitation/outbox is the notification owner; disable native RFQ supplier send flags to avoid duplicate mail.

**Direct/emergency purchase:** explicit reason, supplier eligibility, supporting evidence, exception approver independent of requester and normal financial controls. Emergency does not waive bank verification, managed permissions or native budget Stop. Retrospective review has a configured due date and responsible owner; it does not legalise an unapproved system commitment.

Below-minimum responses require either re-sourcing or an independently approved exception with rationale. No-bid, sole-source and urgent cases are distinct reasons and reportable. Aggregated related requests/variations are considered for threshold routing; deliberate splitting must be flagged for review.

## Award source by sourcing route

Formal awards link the approved request, tender and qualified effective bid/evaluation. Simplified RFQ awards link the approved request, native RFQ and selected quotation snapshot with a documented comparison/selection reason; they do not require a fabricated formal tender or sealed score sheet. Direct/emergency awards link the approved request, current sourcing exception and reviewed offer/quotation. Every route still uses independent award authority, current company/category eligibility, native budget checks and locked source-line allocation.

## Authority snapshots and changes

Approval freezes request content, source policy version, value and approval chain. Material changes to company, scope, quantity, amount, currency, sourcing route or supplier invalidate affected approvals. A policy version change does not rewrite history; publication of a remediation policy may explicitly block new commitments from old snapshots.

Delegations specify original authority, delegate, company, value ceiling and validity. They never expand the original authority or erase conflicts. An award approval does not independently authorise a payment: finance uses native payment preparation, independent approval and execution outside the vendor portal.

## Controlled exceptions

Every exception stores type, scope, business reason, evidence, proposer, independent decision, expiry and resulting limits. The command log records rejected attempts as security/audit events without leaking confidential response bodies. Waivers and sourcing exceptions cannot bypass sealed opening, identity ownership, deadline enforcement or immutable bid history.
