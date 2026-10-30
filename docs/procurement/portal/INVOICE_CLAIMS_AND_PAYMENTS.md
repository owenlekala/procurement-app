# Invoice Claims and Payment Status

Website route: `/procurement/invoice-claims`. Audience: Own organisation Owners and Billing-capable members.

[Screen contract](README.md) · [Policy owner](../CONTRACTS_AND_FULFILMENT.md).

## Components and layout

Themed claim list and form with line/source matching, evidence, dispute history and a separate accounting-derived status panel.

## Displayed fields and context

Invoice number/date, company/currency/taxes, PO/contract and receipt/milestone references, uploaded invoice, claim revision, native posted/outstanding/credited/allocated values and as-of time.

## Actions by state

Draft/submit claim; correct returned claim in a new revision; request credit; inspect posted invoice/payment status. No invoice posting, mark-paid control or payment initiation.

## Permission boundaries

Ordinary bid/document contributors cannot view billing data. Never expose bank balance, full vendor bank proof, other Supplier invoices or GL/account details.

## Validation, loading and exception states

Duplicates and overclaims show safe actionable conflicts; a pending finance draft is distinct from posted/settled. Reversed allocations update status; no promised bank-clearance claim.

## Responsive and keyboard behaviour

Totals and discrepancy reasons stack before lines; exact currency and invoice status remain visible while entering source references.

## Acceptance links

[PROC-A09](../TESTING_AND_ACCEPTANCE.md#proc-a09), [PROC-A22](../TESTING_AND_ACCEPTANCE.md#proc-a22), [PROC-A23](../TESTING_AND_ACCEPTANCE.md#proc-a23), [PROC-A24](../TESTING_AND_ACCEPTANCE.md#proc-a24), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
