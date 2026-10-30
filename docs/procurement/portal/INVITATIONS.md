# Invitations

Website route: `/procurement/invitations`. Audience: Members of approved or participating vendor organisations.

[Screen contract](README.md) · [Policy owner](../TENDERING_AND_EVALUATION.md).

## Components and layout

Themed paginated invitation list with company/category/status/deadline filters, explicit organisation switcher and essential addendum indicators.

## Displayed fields and context

Tender reference/version, company, match/invitation reason, deadline, current eligibility, acknowledgement state and any cancellation/revocation notice.

## Actions by state

Open invitation; acknowledge addendum; prepare eligible bid; update optional public-job subscription. Essential notices remain visible after optional opt-out.

## Permission boundaries

Only invited organisation sees private opportunities. Being invited never substitutes for current company/category approval; expired participants retain their own notices/receipts.

## Validation, loading and exception states

Explain revoked invitation, eligibility hold or closed tender. Failed email does not remove portal invitation. No hidden action that backdates an invitation or submission.

## Responsive and keyboard behaviour

Prioritise action-required/deadline indicators and use one-column list rows with complete tender/company labels.

## Acceptance links

[PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A08](../TESTING_AND_ACCEPTANCE.md#proc-a08), [PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A15](../TESTING_AND_ACCEPTANCE.md#proc-a15), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26).
