# Vendor Database

Native destination: `PROC Company Approval`. Audience: Company buyers, procurement managers and authorised vendor administrators.

[Screen contract](README.md) · [Policy owner](../REGISTRATION_AND_COMPLIANCE.md).

## Components and layout

Native company-approval List linked to a reviewed organisation summary. Tabs: Identity, Company/category approvals, Coverage, Contracts, Performance and Audit.

## Displayed fields and context

Legal/trading identity, Supplier link, category state/expiry, services/regions, shared-evidence grants, current eligibility reasons and pending profile/bank changes (masked).

## Actions by state

Open application or requirement gap; request renewal; propose suspension/reinstatement; inspect contracts/scorecard; preview imports/duplicate cases through persisted operations.

## Permission boundaries

Global identity basics do not grant another company’s evidence or financial records. Company-specific status controls must not toggle global Supplier disablement.

## Validation, loading and exception states

Explain Unverified versus Active versus Hold. Empty approved list offers application/import review, not mass approval. Detect duplicates before link/merge and preserve historical records.

## Responsive and keyboard behaviour

Prioritise legal name/company/status; put coverage and history in labelled sections and keep sensitive actions in standard menus.

## Acceptance links

[PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A04](../TESTING_AND_ACCEPTANCE.md#proc-a04), [PROC-A08](../TESTING_AND_ACCEPTANCE.md#proc-a08), [PROC-A10](../TESTING_AND_ACCEPTANCE.md#proc-a10), [PROC-A25](../TESTING_AND_ACCEPTANCE.md#proc-a25).
