# Invoice Claims

Native destination: `PROC Invoice Claim`. Audience: Company finance reviewers and authorised contract/receiving staff.

[Screen contract](README.md) · [Policy owner](../CONTRACTS_AND_FULFILMENT.md).

## Components and layout

Native queue/Form with Claim, Match results, Evidence, Disputes, Native invoice and Payment status tabs. Match discrepancies are line-level and explain their basis.

## Displayed fields and context

Invoice number/date/currency, contract/PO, claim revisions, quantities/tax, net accepted evidence, duplicate registry results, tolerances/exceptions and native posting links.

## Actions by state

Review/request correction/dispute/reject; independently approve discrepancy exception; create one native invoice draft; open finance submission flow; handle credit request or cancellation.

## Permission boundaries

Finance company rights and bank secrecy apply independently. Approval of a claim never grants a vendor direct invoice submission or payment execution.

## Validation, loading and exception states

Duplicate native or portal invoice keys, overclaim, unmatched quantities and native validation failures block draft/posting. A stale claim cannot create a new draft. Unknown mapping creates reconciliation work.

## Responsive and keyboard behaviour

Compare claim and source totals in stacked labelled groups; retain visible currency and status distinction between claim approval, invoice posting and settlement.

## Acceptance links

[PROC-A09](../TESTING_AND_ACCEPTANCE.md#proc-a09), [PROC-A22](../TESTING_AND_ACCEPTANCE.md#proc-a22), [PROC-A23](../TESTING_AND_ACCEPTANCE.md#proc-a23), [PROC-A24](../TESTING_AND_ACCEPTANCE.md#proc-a24).
