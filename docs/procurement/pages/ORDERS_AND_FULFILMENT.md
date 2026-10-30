# Orders and Fulfilment

Native destination: `Report Procurement Fulfilment`. Audience: Buyers, contract managers and receiving/acceptance officers.

[Screen contract](README.md) · [Policy owner](../CONTRACTS_AND_FULFILMENT.md).

## Components and layout

Native report/list links to native PO/receipt/inspection and owned fulfilment/service-acceptance forms. Filters retain company, contract, work type and outstanding status.

## Displayed fields and context

Ordered/reserved/accepted/returned/outstanding quantities, delivery dates, milestone evidence, inspection outcomes, native document status and source allocation references.

## Actions by state

Create authorised draft order/call-off; review vendor acknowledgement/dispatch; internally accept partially/fully; request correction; create native receipt/return; reconcile cancellations.

## Permission boundaries

Vendor submissions cannot post stock. Receiving rights differ from request/award rights; conflicts trigger independent service acceptance.

## Validation, loading and exception states

Recheck company, compliance, budget, balance and native quantity rules. Preserve a previous effective acceptance on failed correction; downstream invoices block unsafe reversal.

## Responsive and keyboard behaviour

Use labelled line summaries and a dedicated acceptance dialog; distinguish vendor-reported completion from internally accepted work.

## Acceptance links

[PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21), [PROC-A22](../TESTING_AND_ACCEPTANCE.md#proc-a22), [PROC-A23](../TESTING_AND_ACCEPTANCE.md#proc-a23).
