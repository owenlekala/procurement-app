# Vendor Applications

Native destination: `PROC Vendor Application`. Audience: Assigned compliance reviewers and independent activation approvers.

[Screen contract](README.md) · [Policy owner](../REGISTRATION_AND_COMPLIANCE.md).

## Components and layout

Native review List with company/stage/age/assignee filters. Form tabs: Summary, Responses, Evidence, Decisions, Applicant timeline and Internal notes.

## Displayed fields and context

Resolved requirement versions, completeness, document scan/verification status, company/categories, waiver indicators, review SLA and response revision. Secret fields appear only through restricted verification controls.

## Actions by state

Submitted: claim assigned task. Under review: accept/reject/request correction per item. All stages complete: independent approve. Rejection needs safe reason. Renewal/migration opens a new linked flow.

## Permission boundaries

Assignment and company rights govern evidence access. Final approver differs from submitter/proposer; internal notes never feed applicant projections.

## Validation, loading and exception states

Pending scan, stale response, missing stage, expired waiver and unresolved duplicate show actionable blockers. Changing evidence resets affected reviews; review decisions remain immutable.

## Responsive and keyboard behaviour

Summary precedes each evidence group; provide keyboard links to requested corrections and a clearly separated confidential note area.

## Acceptance links

[PROC-A05](../TESTING_AND_ACCEPTANCE.md#proc-a05), [PROC-A06](../TESTING_AND_ACCEPTANCE.md#proc-a06), [PROC-A07](../TESTING_AND_ACCEPTANCE.md#proc-a07), [PROC-A08](../TESTING_AND_ACCEPTANCE.md#proc-a08), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
