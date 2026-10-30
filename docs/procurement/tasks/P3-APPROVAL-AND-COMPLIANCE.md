# P3 — Approval, renewal and legacy migration

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P3-001

- [ ] **Implement review stages and independent activation**

**Depends on:** `PROC-P2-004`

**Requirements:** PROC-R07, PROC-R03. **Acceptance:** [PROC-A07](../TESTING_AND_ACCEPTANCE.md#proc-a07), [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03).

**Read first:** [Registration And Compliance](../REGISTRATION_AND_COMPLIANCE.md) · [Vendor Applications](../pages/VENDOR_APPLICATIONS.md).

**Implementation and boundaries:** Build assigned/quorum review tasks, immutable verification, confidential versus safe comments, delegation and independent final activation with atomic Supplier linking.

**Failure cases and verification:** Test self/unassigned review, missing slots, stale evidence, duplicate final approval and Supplier creation rollback.

**Completion evidence:** Review-to-activation end-to-end fixtures and native queue/form screenshots.

## PROC-P3-002

- [ ] **Implement expiry, renewal, sharing and remediation**

**Depends on:** `PROC-P3-001`

**Requirements:** PROC-R05, PROC-R08, PROC-R26. **Acceptance:** [PROC-A05](../TESTING_AND_ACCEPTANCE.md#proc-a05), [PROC-A08](../TESTING_AND_ACCEPTANCE.md#proc-a08), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26).

**Read first:** [Registration And Compliance](../REGISTRATION_AND_COMPLIANCE.md) · [Renewal And Remediation](../flows/RENEWAL_AND_REMEDIATION.md).

**Implementation and boundaries:** Implement live eligibility, evidence expiry/waivers, independent suspension/reinstatement, renewal applications, evidence grants and previewed remediation/version migration.

**Failure cases and verification:** Test stopped scheduler, expiry boundaries, revoked grants, current-history preservation and material change re-review.

**Completion evidence:** Clock-controlled eligibility/remediation and vendor document/progress evidence.

## PROC-P3-003

- [ ] **Implement bank-change and native payment protection**

**Depends on:** `PROC-P3-002`

**Requirements:** PROC-R09, PROC-R24, PROC-R28. **Acceptance:** [PROC-A09](../TESTING_AND_ACCEPTANCE.md#proc-a09), [PROC-A24](../TESTING_AND_ACCEPTANCE.md#proc-a24), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Contracts And Fulfilment](../CONTRACTS_AND_FULFILMENT.md) · [Erpnext Integration](../ERPNext_INTEGRATION.md).

**Implementation and boundaries:** Build restricted proposed bank data/proof and independent trusted-channel verification, keep account revisions and enforce payment-content/bank approval guards on native paths.

**Failure cases and verification:** Test proposer activation, secret leaks, pending change holds, stale payment content and generic REST/import bypass.

**Completion evidence:** Bank capability/access tests and qualified native approval-gate fixtures; P7 completes accounting settlement projection.

## PROC-P3-004

- [ ] **Implement legacy import and duplicate reconciliation**

**Depends on:** `PROC-P3-003`

**Requirements:** PROC-R10, PROC-R04, PROC-R03. **Acceptance:** [PROC-A10](../TESTING_AND_ACCEPTANCE.md#proc-a10), [PROC-A04](../TESTING_AND_ACCEPTANCE.md#proc-a04), [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03).

**Read first:** [Registration And Compliance](../REGISTRATION_AND_COMPLIANCE.md) · [Vendor Database](../pages/VENDOR_DATABASE.md).

**Implementation and boundaries:** Build bounded UTF-8 CSV preview/confirm/resume import operations with explicit operation evidence scope, reviewed Supplier linking, conflict resolution and Unverified company approvals; reconcile existing native portal grants.

**Failure cases and verification:** Crash/replay imports, conflicting identities and unsupported access grants; never auto-approve, verify banks or grant membership.

**Completion evidence:** Import reconciliation counts, source preservation and native/owned portal isolation results.
