# P5 — Sealed submissions and opening

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P5-001

- [ ] **Implement separate envelope drafts and protected evidence**

**Depends on:** `PROC-P4-004`

**Requirements:** PROC-R16, PROC-R28. **Acceptance:** [PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Data Model](../DATA_MODEL.md) · [Permissions And Privacy](../PERMISSIONS_AND_PRIVACY.md).

**Implementation and boundaries:** Create distinct technical/commercial payload storage, own-draft DTOs and bid workspace with classified uploads and scan gates; exclude payloads from generic Version/search/boot/attachments.

**Failure cases and verification:** Attempt buyer/other-vendor access through every raw record/File/print/export path; test quotas and sensitive browser storage.

**Completion evidence:** Pre-opening leak matrix and responsive bid form evidence.

## PROC-P5-002

- [ ] **Implement atomic submit, receipt, replacement and withdrawal**

**Depends on:** `PROC-P5-001`

**Requirements:** PROC-R16, PROC-R15. **Acceptance:** [PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16), [PROC-A15](../TESTING_AND_ACCEPTANCE.md#proc-a15).

**Read first:** [Tendering And Evaluation](../TENDERING_AND_EVALUATION.md) · [Bid Submission And Revision](../flows/BID_SUBMISSION_AND_REVISION.md).

**Implementation and boundaries:** Implement locking/time/eligibility/addendum gates, immutable full-version receipt, explicit bid start/revision/reaffirmation, idempotency replay and effective-head changes; preserve earlier bid until replacement commit.

**Failure cases and verification:** Race deadline/duplicate/replacement/withdrawal/readiness controls; inject lost response and rollback; reject exact-close and backdating.

**Completion evidence:** Actual database concurrency/receipt fixtures with server-clock boundaries.

## PROC-P5-003

- [ ] **Implement staged two-actor opening**

**Depends on:** `PROC-P5-002`

**Requirements:** PROC-R17, PROC-R16, PROC-R28. **Acceptance:** [PROC-A17](../TESTING_AND_ACCEPTANCE.md#proc-a17), [PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Tendering And Evaluation](../TENDERING_AND_EVALUATION.md) · [Evaluation](../pages/EVALUATION.md).

**Implementation and boundaries:** Freeze effective manifest after close, implement distinct proposer/confirmer technical release and commercial release conditional on final qualification; keep disqualified commercial sealed.

**Failure cases and verification:** Test same actor, stale manifests, early access, incomplete technical decisions and alternate download/API routes.

**Completion evidence:** Opening audit/manifests and full stage-gate negative-path results.

## PROC-P5-004

- [ ] **Qualify bid fairness and sealed-content boundaries**

**Depends on:** `PROC-P5-003`

**Requirements:** PROC-R15, PROC-R16, PROC-R17, PROC-R28. **Acceptance:** [PROC-A15](../TESTING_AND_ACCEPTANCE.md#proc-a15), [PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16), [PROC-A17](../TESTING_AND_ACCEPTANCE.md#proc-a17), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Testing And Acceptance](../TESTING_AND_ACCEPTANCE.md) · [Adr-003-Sealed-Bids-And-Durable-Work](../decisions/ADR-003-SEALED-BIDS-AND-DURABLE-WORK.md).

**Implementation and boundaries:** Exercise complete bid/addendum/opening journey including accidental technical price disclosure, revoked access and policy-preserved privileged infrastructure trust limits.

**Failure cases and verification:** Check logs, history, reports, File metadata, native RFQ/quotation paths and realtime; no ordinary-path leakage is acceptable.

**Completion evidence:** Cross-surface leak/concurrency review and bidder/committee screenshot evidence.
