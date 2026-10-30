# P4 — Requests, authority and publication

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P4-001

- [ ] **Implement requests and native budget approval**

**Depends on:** `PROC-P3-004`

**Requirements:** PROC-R11, PROC-R12. **Acceptance:** [PROC-A11](../TESTING_AND_ACCEPTANCE.md#proc-a11), [PROC-A12](../TESTING_AND_ACCEPTANCE.md#proc-a12).

**Read first:** [Procurement Policy](../PROCUREMENT_POLICY.md) · [Procurement Requests](../pages/PROCUREMENT_REQUESTS.md).

**Implementation and boundaries:** Complete goods/services/works demand forms, native Material Request mapping, financial dimensions, gross approval basis and policy-driven decision snapshots.

**Failure cases and verification:** Test cross-company dimensions, material changes, missing policy/rates, budget Stop/Warn and concurrency.

**Completion evidence:** Request/budget native integration and approval form results.

## PROC-P4-002

- [ ] **Implement sourcing routes and controlled exceptions**

**Depends on:** `PROC-P4-001`

**Requirements:** PROC-R12, PROC-R21. **Acceptance:** [PROC-A12](../TESTING_AND_ACCEPTANCE.md#proc-a12), [PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21).

**Read first:** [Procurement Policy](../PROCUREMENT_POLICY.md) · [Erpnext Integration](../ERPNext_INTEGRATION.md).

**Implementation and boundaries:** Implement formal/RFQ/direct/emergency routing, route-specific request/quotation/exception award references without dummy formal records, quotation minimum, independent exceptions and managed-company native guards. Disable duplicate RFQ notification paths.

**Failure cases and verification:** Try omitted links/native CRUD bypass, expired exceptions, threshold edges, insufficient responses and missing authority.

**Completion evidence:** All three route fixtures and perimeter/exception denial tests.

## PROC-P4-003

- [ ] **Implement immutable tender publication and public discovery**

**Depends on:** `PROC-P4-002`

**Requirements:** PROC-R13, PROC-R02. **Acceptance:** [PROC-A13](../TESTING_AND_ACCEPTANCE.md#proc-a13), [PROC-A02](../TESTING_AND_ACCEPTANCE.md#proc-a02).

**Read first:** [Tendering And Evaluation](../TENDERING_AND_EVALUATION.md) · [Public Opportunities](../portal/PUBLIC_OPPORTUNITIES.md).

**Implementation and boundaries:** Build tender/lots/schedule/evaluation/panel forms, approval/hash validation, immutable versions and safe public/invited website projections with public-document allowlists.

**Failure cases and verification:** Reject stale approval, invalid weights/dates/panel, invited ID discovery and public confidential fields/files.

**Completion evidence:** Publication/version integration tests and Desk/public responsive screens.

## PROC-P4-004

- [ ] **Implement matching, clarifications and addenda**

**Depends on:** `PROC-P4-003`

**Requirements:** PROC-R14, PROC-R15, PROC-R26. **Acceptance:** [PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A15](../TESTING_AND_ACCEPTANCE.md#proc-a15), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26).

**Read first:** [Tendering And Evaluation](../TENDERING_AND_EVALUATION.md) · [Publication And Matching](../flows/PUBLICATION_AND_MATCHING.md).

**Implementation and boundaries:** Build explainable matching/invitations, participation, private questions/shared safe answers, briefing attendance, approved addenda and mandatory acknowledgements. Persist purpose-specific notice work.

**Failure cases and verification:** Test opt-out versus essential notices, stale terms, post-close/structural changes, revoked invitations and Q&A price/XSS exposure.

**Completion evidence:** Matching/addendum/briefing scenarios and portal invitation/detail evidence.
