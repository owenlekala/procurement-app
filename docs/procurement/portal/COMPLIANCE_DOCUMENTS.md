# Compliance Documents

Website route: `/procurement/documents`. Audience: Authorised owners and document contributors; restricted bank maintainers for bank proof.

[Screen contract](README.md) · [Policy owner](../REGISTRATION_AND_COMPLIANCE.md).

## Components and layout

Document checklist grouped by buying company/category, with file revision, scan/review state, expiry and permitted sharing controls. Keep upload distinct from verification.

## Displayed fields and context

Requirement/help, allowed formats/size, issue/expiry date, current evidence revision, accepted verification time and renewal action. Secret PIN values remain masked.

## Actions by state

Upload replacement draft; submit renewal/remediation; grant/revoke reuse for a named company; view safe reviewer feedback and permitted clean own evidence.

## Permission boundaries

Own organisation and per-document capability apply. Reuse permission is explicit; recipient company still verifies. Revocation does not erase evidence already lawfully relied upon.

## Validation, loading and exception states

Rejected scan/format/expiry has specific safe feedback. Pending scan cannot satisfy submission. Expired originals remain in history and cannot be silently replaced.

## Responsive and keyboard behaviour

Use compact labelled cards instead of a wide file grid; announce upload/scan progress without exposing storage URLs.

## Acceptance links

[PROC-A05](../TESTING_AND_ACCEPTANCE.md#proc-a05), [PROC-A08](../TESTING_AND_ACCEPTANCE.md#proc-a08), [PROC-A09](../TESTING_AND_ACCEPTANCE.md#proc-a09), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
