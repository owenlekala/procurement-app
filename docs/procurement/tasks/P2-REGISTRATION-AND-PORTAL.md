# P2 — Requirements, identity and registration

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P2-001

- [ ] **Implement versioned requirement and policy builders**

**Depends on:** `PROC-P1-004`

**Requirements:** PROC-R05, PROC-R12. **Acceptance:** [PROC-A05](../TESTING_AND_ACCEPTANCE.md#proc-a05), [PROC-A12](../TESTING_AND_ACCEPTANCE.md#proc-a12).

**Read first:** [Registration And Compliance](../REGISTRATION_AND_COMPLIANCE.md) · [Procurement Policy](../PROCUREMENT_POLICY.md).

**Implementation and boundaries:** Build native no-code pack/condition/stage editors, preview/resolution, immutable publication and complete authority bands. Add editable disabled SA examples with no legal-mandatory claims.

**Failure cases and verification:** Reject cycles/type conflicts/hidden required traps and overlapping/missing authority bands; prove new fields need no code.

**Completion evidence:** Published version fixtures, preview/server parity and builder screenshots.

## PROC-P2-002

- [ ] **Implement organisation claims and verified memberships**

**Depends on:** `PROC-P2-001`

**Requirements:** PROC-R03, PROC-R04. **Acceptance:** [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A04](../TESTING_AND_ACCEPTANCE.md#proc-a04).

**Read first:** [Registration And Compliance](../REGISTRATION_AND_COMPLIANCE.md) · [Team And Preferences](../portal/TEAM_AND_PREFERENCES.md).

**Implementation and boundaries:** Complete account verification integration, identity/duplicate claims, explicit capabilities, invitation acceptance, owner transfer/recovery and organisation switcher.

**Failure cases and verification:** Test duplicate races, same-domain takeover, token replay, capability escalation and last-owner removal.

**Completion evidence:** Identity/membership negative-path results and team/profile screens.

## PROC-P2-003

- [ ] **Implement resumable applications and quarantined uploads**

**Depends on:** `PROC-P2-002`

**Requirements:** PROC-R05, PROC-R06, PROC-R28. **Acceptance:** [PROC-A05](../TESTING_AND_ACCEPTANCE.md#proc-a05), [PROC-A06](../TESTING_AND_ACCEPTANCE.md#proc-a06), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Data Model](../DATA_MODEL.md) · [Registration](../portal/REGISTRATION.md).

**Implementation and boundaries:** Build resolved company applications, typed draft answers, clean-before-submit evidence intents/scanning and immutable submission receipts. Implement file quotas/classification and current-version validation.

**Failure cases and verification:** Test pending/rejected scan, malicious/oversized files, two-company differing packs, interrupted save and duplicate submission.

**Completion evidence:** Registration/upload/receipt integration results and responsive form screenshots.

## PROC-P2-004

- [ ] **Implement progress, correction and applicant communications**

**Depends on:** `PROC-P2-003`

**Requirements:** PROC-R06, PROC-R07, PROC-R26. **Acceptance:** [PROC-A06](../TESTING_AND_ACCEPTANCE.md#proc-a06), [PROC-A07](../TESTING_AND_ACCEPTANCE.md#proc-a07), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26).

**Read first:** [Application Progress](../portal/APPLICATION_PROGRESS.md) · [Api Contracts](../API_CONTRACTS.md).

**Implementation and boundaries:** Expose safe progress/timeline, separate completeness from review, support explicit correction-revision start/withdrawal/reapplication and persist workflow events/portal notices. Email dispatch waits for qualified P8 transport.

**Failure cases and verification:** Ensure internal notes/secrets never project; 100% is not approval; stale corrections do not erase prior submissions.

**Completion evidence:** Applicant journey evidence with reload/network/zero-denominator cases.
