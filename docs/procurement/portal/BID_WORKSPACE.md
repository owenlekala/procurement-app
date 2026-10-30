# Bid Workspace

Website route: `/procurement/bids/<id>/edit`. Audience: Own organisation contributors and authorised Bid Submitters.

[Screen contract](README.md) · [Policy owner](../TENDERING_AND_EVALUATION.md).

## Components and layout

Tender/version/deadline header, Technical and Commercial tabs, required-item checklist, addenda/briefing status, review declaration and Submit action. Separate save indicators for envelope drafts.

## Displayed fields and context

Typed technical responses/files; structured lot prices, quantities, tax, delivery/validity and commercial files. Review preview displays only own authorised content and current submission basis.

## Actions by state

Start/resume or clone an own revision; save drafts; attach clean evidence; validate; authorised submitter submits or uses `reaffirm_bid` for unchanged content after an addendum; after receipt create replacement or withdraw before close. A failed replacement preserves the previous effective bid.

## Permission boundaries

Contributor preparation rights do not grant submission. Company/category approval and invitation predicates apply at submit; other vendors and internal evaluators cannot inspect the draft.

## Validation, loading and exception states

Server enforces time, revision, requirements, scanning and current addenda atomically. Unknown network result triggers receipt lookup; do not blank the form or invite an unverified duplicate send.

## Responsive and keyboard behaviour

Tabs use labelled navigation; price tables have accessible detail editing; countdown stays advisory and review confirmation names company/organisation/version.

## Acceptance links

[PROC-A15](../TESTING_AND_ACCEPTANCE.md#proc-a15), [PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16), [PROC-A17](../TESTING_AND_ACCEPTANCE.md#proc-a17), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
