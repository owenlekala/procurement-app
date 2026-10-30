# Compliance Reviews

Native destination: `PROC Review Task`. Audience: Assigned document reviewers, compliance managers and restricted finance verifiers.

[Screen contract](README.md) · [Policy owner](../REGISTRATION_AND_COMPLIANCE.md).

## Components and layout

Native queue with due date/type/assignee filters and a protected evidence review dialog. Use separate Bank verification and Requirement remediation views rather than exposing all evidence together.

## Displayed fields and context

Evidence classification, version, scan result, issue/expiry, verification checklist/source/result, waiver expiry, company/category impact and trusted-contact bank check reference.

## Actions by state

Open clean authorised evidence; record immutable verification; request correction; propose/decide a waiver; reassign within authority; publish a previewed remediation campaign.

## Permission boundaries

Bank proof/PINs need explicit finance/verification capability beyond a general reviewer role. Distinct proposer/verifier and grant-based cross-company reuse are enforced.

## Validation, loading and exception states

Quarantine and revoked grant deny retrieval. Expiry is checked live. No scanner override or automatic acceptance of imported evidence. Errors retain the unsent verification form safely.

## Responsive and keyboard behaviour

Evidence and checklist stack with an explicit return-to-task action; status/expiry remain visible without relying on colour.

## Acceptance links

[PROC-A05](../TESTING_AND_ACCEPTANCE.md#proc-a05), [PROC-A07](../TESTING_AND_ACCEPTANCE.md#proc-a07), [PROC-A08](../TESTING_AND_ACCEPTANCE.md#proc-a08), [PROC-A09](../TESTING_AND_ACCEPTANCE.md#proc-a09), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
