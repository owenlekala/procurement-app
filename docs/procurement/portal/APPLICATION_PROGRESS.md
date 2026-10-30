# Application Progress

Website route: `/procurement/applications/<id>`. Audience: Own organisation members with access to the selected company application.

[Screen contract](README.md) · [Policy owner](../REGISTRATION_AND_COMPLIANCE.md).

## Components and layout

Status/next-action summary, completeness indicators, requirement review list and applicant-safe chronological timeline. Provide direct correction links into the relevant draft section.

## Displayed fields and context

Current company/category application, pinned requirement versions, completed/required totals, document Accepted/Rejected/More information state, current review stage and target times.

## Actions by state

Draft: resume/submit. Needs correction: start/resume response revision. Under review: inspect receipt or withdraw. Approved: maintain evidence/find jobs. Rejected: read reason/start a linked reapplication.

## Permission boundaries

No confidential reviewer notes, other company responses, full bank information or internal duplicate matches. Company selection uses authorised context.

## Validation, loading and exception states

100% completeness remains distinct from Under review/Approved. Stale corrections reload safely; zero required items gets an explicit label. No SLA-based promise of approval.

## Responsive and keyboard behaviour

Progress/timeline use ordered text and icons; section-level next actions precede long history and remain keyboard accessible.

## Acceptance links

[PROC-A05](../TESTING_AND_ACCEPTANCE.md#proc-a05), [PROC-A06](../TESTING_AND_ACCEPTANCE.md#proc-a06), [PROC-A07](../TESTING_AND_ACCEPTANCE.md#proc-a07), [PROC-A08](../TESTING_AND_ACCEPTANCE.md#proc-a08).
