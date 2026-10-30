# Contracts and Orders

Website route: `/procurement/contracts`. Audience: Own organisation owners, authorised contract contacts and Billing members.

[Screen contract](README.md) · [Policy owner](../CONTRACTS_AND_FULFILMENT.md).

## Components and layout

Themed contract/order lists with status/company filters and detail tabs for agreed scope, signed evidence, milestones, orders and obligations.

## Displayed fields and context

Accepted award, contract dates/ceiling/currency, vendor-visible terms, approved variations, PO quantities/dates, required guarantees and pending acknowledgements.

## Actions by state

Accept/decline offer; upload signed evidence; acknowledge PO; propose delivery change; submit obligation/guarantee evidence. Internal activation/variation approval stays staff-only.

## Permission boundaries

Expose only relevant vendor contract/order projections. Internal estimates, company budgets, unrelated financial records and reviewer comments remain private.

## Validation, loading and exception states

Unsigned/conditional/held states explain next action; a proposal is not an approved change. Expired financial/insurance requirements block only the defined action, not history access.

## Responsive and keyboard behaviour

Contract summary and next obligation lead; line/milestone details open within the same navigation context and preserve currency/status labels.

## Acceptance links

[PROC-A19](../TESTING_AND_ACCEPTANCE.md#proc-a19), [PROC-A20](../TESTING_AND_ACCEPTANCE.md#proc-a20), [PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21).
