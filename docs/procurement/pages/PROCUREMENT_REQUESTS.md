# Procurement Requests

Native destination: `PROC Procurement Request`. Audience: Requesters, budget reviewers and company buyers.

[Screen contract](README.md) · [Policy owner](../PROCUREMENT_POLICY.md).

## Components and layout

Native List and Form. Tabs: Demand, Lines and dimensions, Budget/authority, Sourcing, History. A summary shows company, estimate/currency, required date and current decision.

## Displayed fields and context

Purpose, work type/category, goods/service/works lines, Item/UOM/quantity, locations, schedule, project/cost centre/account, estimate/tax/rate basis, attachments and linked Material Request.

## Actions by state

Draft: save/submit. Pending: assigned decision or return. Approved: start the authorised route. Material revision: resubmit. Ordered: inspect links/remaining demand; cancel only with impact review.

## Permission boundaries

Requester sees own/authorised department demand; budget and buyer actions require company authority. Generic native order creation must still enforce the managed perimeter.

## Validation, loading and exception states

Validate company dimensions, positive quantities, dates, complete policy and native budget result. Distinguish planned estimate from commitment. Missing policy/budget Stop keeps the action blocked with reasons.

## Responsive and keyboard behaviour

Line summaries collapse with an accessible detail editor; preserve entered data on network error and show last saved revision.

## Acceptance links

[PROC-A11](../TESTING_AND_ACCEPTANCE.md#proc-a11), [PROC-A12](../TESTING_AND_ACCEPTANCE.md#proc-a12), [PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21).
