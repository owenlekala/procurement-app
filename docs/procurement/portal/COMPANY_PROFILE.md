# Company Profile

Website route: `/procurement/profile`. Audience: Active organisation owners and permitted contributors.

[Screen contract](README.md) · [Policy owner](../REGISTRATION_AND_COMPLIANCE.md).

## Components and layout

Themed native-style form sections for identity, contacts/address, services/coverage and company approvals. Separate a proposed revision from the currently approved facts.

## Displayed fields and context

Legal/trading name, country/registration reference, contacts, categories/work types/regions, Supplier linkage status and each buying company eligibility summary.

## Actions by state

Prepare profile changes; owner submits material identity proposal; add buying-company application; request bank change through restricted capability; inspect approved revision/history.

## Permission boundaries

Profile editing does not grant company approval. Contributors cannot take ownership or change banking. Cross-company evidence requires a specific grant.

## Validation, loading and exception states

Registration-identifier changes route to identity review. Pending proposal cannot overwrite current approved identity. Duplicate/stale edits show a comparison and retain local entries.

## Responsive and keyboard behaviour

Organisation context appears before company approval cards; long coverage lists use searchable native controls and readable summaries.

## Acceptance links

[PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A04](../TESTING_AND_ACCEPTANCE.md#proc-a04), [PROC-A08](../TESTING_AND_ACCEPTANCE.md#proc-a08), [PROC-A09](../TESTING_AND_ACCEPTANCE.md#proc-a09).
