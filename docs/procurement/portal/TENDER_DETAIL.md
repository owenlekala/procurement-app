# Tender Detail

Website route: `/procurement/opportunities/<id>`. Audience: Public visitors or specifically invited vendor memberships.

[Screen contract](README.md) · [Policy owner](../TENDERING_AND_EVALUATION.md).

## Components and layout

Themed detail page with scope, lots, required eligibility, public files, dates, briefing, Q&A and addenda sections. Signed-in context strip shows selected organisation/company eligibility.

## Displayed fields and context

Published version, bidding currency, deadline/offset, requirements, scoring policy, terms, briefing rules and applicant-safe exclusion reasons. Show registration needs without disclosing another company application.

## Actions by state

Guest: register/sign in. Eligible member: start bid, ask question, acknowledge addendum or review receipt. Closed/cancelled: read permitted history/outcome, no submit.

## Permission boundaries

Invitation-only detail/download requires the invited organisation membership. Follow/subscription does not bypass eligibility or file classification.

## Validation, loading and exception states

Stale version clearly shows the newest addendum; missing approval links to own application. Deadline countdown is advisory; unavailable requirements block action with saved context.

## Responsive and keyboard behaviour

Use expandable native sections with an accessible table of contents; keep tender reference/version/deadline near bid actions.

## Acceptance links

[PROC-A13](../TESTING_AND_ACCEPTANCE.md#proc-a13), [PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A15](../TESTING_AND_ACCEPTANCE.md#proc-a15), [PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16).
