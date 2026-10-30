# Contracts

Native destination: `PROC Contract Control`. Audience: Contract managers, legal/signature reviewers and finance within company scope.

[Screen contract](README.md) · [Policy owner](../CONTRACTS_AND_FULFILMENT.md).

## Components and layout

Native Form/List, linked native Contract. Tabs: Award/terms, Signed evidence, Milestones, Obligations, Financial schedule, Variations, Closeout.

## Displayed fields and context

Company/vendor, accepted award, dates, ceiling/currency, guarantees/insurance, signed documents, acceptance owners, advance/retention treatment, call-off balance and outstanding disputes.

## Actions by state

Prepare/request signatures; verify/activate; propose/approve variation or renewal; create qualified call-off; record termination; close operationally then financially after obligations clear.

## Permission boundaries

Only relevant contract evidence reaches the vendor. Business approval is not inferred from native is_signed. Variations and financial terms require independent authority.

## Validation, loading and exception states

Missing signatures, unsupported financial posting template, expired guarantee, open complaint or exceeded balance blocks the applicable action. Pending settlement prevents a false Closed state.

## Responsive and keyboard behaviour

Prioritise contract status/dates and next obligation; milestones/variation tables scroll within panels and keep value/currency labels.

## Acceptance links

[PROC-A20](../TESTING_AND_ACCEPTANCE.md#proc-a20), [PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21), [PROC-A25](../TESTING_AND_ACCEPTANCE.md#proc-a25).
