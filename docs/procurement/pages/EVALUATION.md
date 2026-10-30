# Evaluation

Native destination: `Page proc-evaluation`. Audience: Assigned evaluators, moderators and authorised opening officers.

[Screen contract](README.md) · [Policy owner](../TENDERING_AND_EVALUATION.md).

## Components and layout

Owned Page inside native Desk shell: assignment/lot filters, released evidence panel, native score controls, then moderated comparison after sheets submit. Commercial panel appears only after release.

## Displayed fields and context

Conflict declaration, effective bid version, criterion/max/weight, evidence-linked score/reason, quorum, pass/fail, commercial basis, ranking/tie flags and recommendation hash.

## Actions by state

Accept assignment or recuse; save/submit own sheet; request a superseding correction; propose/confirm opening; build moderation summary; submit recommendation. Each action requires its stage.

## Permission boundaries

Assignment, conflict status and released envelope constrain every query/download. No other evaluator’s draft or still-sealed price is in page boot/realtime data.

## Validation, loading and exception states

Missing scores remain Incomplete. Stale score manifest blocks recommendation/opening; expired commercial validity blocks recommendation approval; permitted `PROC Offer Revision` consent/review requires a new summary. A lost score-submit response queries the receipt. Empty queue explains no assignment or unreleased stage.

## Responsive and keyboard behaviour

Switch between evidence and scoring using labelled controls; preserve unsaved scores and focus when returning from a document.

## Acceptance links

[PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16), [PROC-A17](../TESTING_AND_ACCEPTANCE.md#proc-a17), [PROC-A18](../TESTING_AND_ACCEPTANCE.md#proc-a18), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
