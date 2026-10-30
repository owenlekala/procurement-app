# P6 — Evaluation, awards and complaints

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P6-001

- [ ] **Implement assignments, conflicts and immutable scoring**

**Depends on:** `PROC-P5-004`

**Requirements:** PROC-R18, PROC-R28. **Acceptance:** [PROC-A18](../TESTING_AND_ACCEPTANCE.md#proc-a18), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Tendering And Evaluation](../TENDERING_AND_EVALUATION.md) · [Evaluation](../pages/EVALUATION.md).

**Implementation and boundaries:** Build conflict declarations/recusal, criterion/lot assignments, native scoring controls, immutable sheet submission and superseding corrections.

**Failure cases and verification:** Prevent others draft/score edits, unassigned access, stale sheets and continued access after recusal.

**Completion evidence:** Multi-evaluator permission and scoring UI evidence.

## PROC-P6-002

- [ ] **Implement moderation and commercial comparison**

**Depends on:** `PROC-P6-001`

**Requirements:** PROC-R18, PROC-R17. **Acceptance:** [PROC-A18](../TESTING_AND_ACCEPTANCE.md#proc-a18), [PROC-A17](../TESTING_AND_ACCEPTANCE.md#proc-a17).

**Read first:** [Tendering And Evaluation](../TENDERING_AND_EVALUATION.md) · [Data Model](../DATA_MODEL.md).

**Implementation and boundaries:** Calculate published quorum/technical gates and moderated means, stage release, valid commercial totals, fixed-precision price/combined scores and tie flags with source manifests. Handle expired offer validity through a separately consented/reviewed offer revision and renewed recommendation.

**Failure cases and verification:** Test missing/zero/invalid totals, weights, ties, revised sheets and blocked recommendation on stale summary.

**Completion evidence:** Worked deterministic scoring fixtures and comparison grid results.

## PROC-P6-003

- [ ] **Implement independent awards and vendor response**

**Depends on:** `PROC-P6-002`

**Requirements:** PROC-R19, PROC-R21, PROC-R26. **Acceptance:** [PROC-A19](../TESTING_AND_ACCEPTANCE.md#proc-a19), [PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26).

**Read first:** [Tendering And Evaluation](../TENDERING_AND_EVALUATION.md) · [Awards](../pages/AWARDS.md).

**Implementation and boundaries:** Implement split/lot allocations, current compliance/budget authority, independent award approval, independently cleared conditions and controlled accept/decline deadline extensions with private outcome notices.

**Failure cases and verification:** Race over-allocation, self-approval, expiry, condition clearance and declined/expired offers; never auto-select runner-up.

**Completion evidence:** Award allocation concurrency and vendor-response end-to-end evidence.

## PROC-P6-004

- [ ] **Implement complaints, withdrawal and sourcing outcomes**

**Depends on:** `PROC-P6-003`

**Requirements:** PROC-R19, PROC-R13, PROC-R12. **Acceptance:** [PROC-A19](../TESTING_AND_ACCEPTANCE.md#proc-a19), [PROC-A13](../TESTING_AND_ACCEPTANCE.md#proc-a13), [PROC-A12](../TESTING_AND_ACCEPTANCE.md#proc-a12).

**Read first:** [Tendering And Evaluation](../TENDERING_AND_EVALUATION.md) · [Award Acceptance And Complaint](../flows/AWARD_ACCEPTANCE_AND_COMPLAINT.md).

**Implementation and boundaries:** Build independent complaint cases/holds/resolution, approved public result projection, withdrawal, no-bid/insufficient-response and cancellation/reissue flows.

**Failure cases and verification:** Prevent downstream order during hold, sensitive outcome publication and deletion of native financial history.

**Completion evidence:** Complaint/withdrawal/reissue fixtures and linked decision audit.
