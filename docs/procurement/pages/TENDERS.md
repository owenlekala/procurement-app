# Tenders

Native destination: `PROC Tender`. Audience: Company buyers, publication approvers and opening officers.

[Screen contract](README.md) · [Policy owner](../TENDERING_AND_EVALUATION.md).

## Components and layout

Native List/Form with tabs for Scope/lots, Eligibility, Schedule/briefing, Evaluation policy, Panel, Publication/addenda and Outcome. Review dialog displays the frozen version and material changes.

## Displayed fields and context

Approved request, public/invited mode, currency, lots/price schedule, requirements, dates/timezone, briefing, technical gates/quorum/weights, panel and publication approvals.

## Actions by state

Draft: prepare/request approval. Approved: publish. Open: invite, answer, addendum, extend or cancel under authority. Closed: opening workflow. Failed/no-bid: disposition/reissue. Never edit published terms in place.

## Permission boundaries

Buyers may manage terms but cannot inspect sealed bids. Public preview uses the safe publication DTO; panel/estimate/recipient data remain internal.

## Validation, loading and exception states

Validate weights, assignments, deadline ordering, requirement versions and policy. Structural post-submission changes require reissue. Stale publish/addendum fails with a version comparison.

## Responsive and keyboard behaviour

Use native form sections and scrollable lot rows; show exact deadline offset in summaries and all publication confirmations.

## Acceptance links

[PROC-A12](../TESTING_AND_ACCEPTANCE.md#proc-a12), [PROC-A13](../TESTING_AND_ACCEPTANCE.md#proc-a13), [PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A15](../TESTING_AND_ACCEPTANCE.md#proc-a15), [PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16), [PROC-A17](../TESTING_AND_ACCEPTANCE.md#proc-a17).
