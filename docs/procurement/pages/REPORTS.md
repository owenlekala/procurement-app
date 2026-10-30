# Reports

Native destination: `Native Script Reports`. Audience: Managers, finance and auditors with explicit company/data permissions.

[Screen contract](README.md) · [Policy owner](../REPORTING.md).

## Components and layout

Native report picker, filter bar, chart/table and permission-aware drill-down. Reports include visible metric definitions, timezone, currency grouping and as-of basis.

## Displayed fields and context

Application ageing, compliance, sourcing cycle, participation, evaluation progress, awards, commitments, fulfilment, invoice/payment ageing, performance and operational health.

## Actions by state

Run/filter; inspect authorised source; request bounded private export and track its operation. Export is offered only where field-level permissions permit it.

## Permission boundaries

Aggregate access does not reveal restricted evidence or sealed prices. Same predicates govern counters, rows, export and download.

## Validation, loading and exception states

Zero denominator displays N/A; missing/unknown dates stay Unknown. Reconcile cancellation/amendment chains and reject mixed-currency totals. No actual-as-of claim from current-only data.

## Responsive and keyboard behaviour

Filter controls wrap; wide native tables remain internally scrollable and carry accessible headers; export progress survives navigation.

## Acceptance links

[PROC-A18](../TESTING_AND_ACCEPTANCE.md#proc-a18), [PROC-A24](../TESTING_AND_ACCEPTANCE.md#proc-a24), [PROC-A25](../TESTING_AND_ACCEPTANCE.md#proc-a25), [PROC-A27](../TESTING_AND_ACCEPTANCE.md#proc-a27), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
