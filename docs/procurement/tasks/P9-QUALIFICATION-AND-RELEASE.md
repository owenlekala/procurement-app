# P9 — Production qualification and release

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P9-001

- [ ] **Implement readiness, observability and privacy operations**

**Depends on:** `PROC-P8-004`

**Requirements:** PROC-R28, PROC-R29. **Acceptance:** [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).

**Read first:** [Operations And Release](../OPERATIONS_AND_RELEASE.md) · [Permissions And Privacy](../PERMISSIONS_AND_PRIVACY.md).

**Implementation and boundaries:** Complete scoped feature/pilot switches, diagnostics/alerts, operator incident views, retention preview/execute/holds and verified access/erasure procedures.

**Failure cases and verification:** Fail activation on missing policy/health/evidence; preserve hold records and enforce current membership/export permissions.

**Completion evidence:** Readiness/alert/retention incidents and named operational ownership.

## PROC-P9-002

- [ ] **Run security, capacity, upgrade and restore qualification**

**Depends on:** `PROC-P9-001`

**Requirements:** PROC-R01, PROC-R03, PROC-R16, PROC-R17, PROC-R28, PROC-R29. **Acceptance:** [PROC-A01](../TESTING_AND_ACCEPTANCE.md#proc-a01), [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16), [PROC-A17](../TESTING_AND_ACCEPTANCE.md#proc-a17), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).

**Read first:** [Testing And Acceptance](../TESTING_AND_ACCEPTANCE.md) · [Operations And Release](../OPERATIONS_AND_RELEASE.md).

**Implementation and boundaries:** Run full relevant suites, cross-route security review, stated synthetic load, actual deadline contention, repeated migration and isolated backup restore/reconciliation.

**Failure cases and verification:** Include all unavailable dependencies and restore Submitting outcomes; do not omit failing checks or re-enable sends automatically.

**Completion evidence:** Exact commands, data/resources, measured latency/memory/lock/queue results and restore artifacts.

## PROC-P9-003

- [ ] **Validate handbook traceability and rendered journeys**

**Depends on:** `PROC-P9-002`

**Requirements:** PROC-R02, PROC-R27, PROC-R30. **Acceptance:** [PROC-A02](../TESTING_AND_ACCEPTANCE.md#proc-a02), [PROC-A27](../TESTING_AND_ACCEPTANCE.md#proc-a27), [PROC-A30](../TESTING_AND_ACCEPTANCE.md#proc-a30).

**Read first:** [Traceability](../TRACEABILITY.md) · [Ui Design System](../UI_DESIGN_SYSTEM.md).

**Implementation and boundaries:** Run structural checker/self-tests, review lifecycle/interface agreement, render diagrams and compare all feature screens against current runtime references; correct documentation and implementation mismatches.

**Failure cases and verification:** Reject broken/stale links/IDs, untested pages, hidden alternate access or unsupported production claims.

**Completion evidence:** Validator output, diagram/screen review, resolved findings and complete requirement coverage.

## PROC-P9-004

- [ ] **Complete authorised pilot and release decision**

**Depends on:** `PROC-P9-003`

**Requirements:** PROC-R29, PROC-R30, PROC-R26. **Acceptance:** [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29), [PROC-A30](../TESTING_AND_ACCEPTANCE.md#proc-a30), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26).

**Read first:** [Operations And Release](../OPERATIONS_AND_RELEASE.md) · [Progress](../PROGRESS.md).

**Implementation and boundaries:** On qualified image run limited explicit company/vendor/tender pilot through onboarding, bidding, award, execution and controlled notifications. Record procurement/finance/platform sign-off, rollback ownership and gradual activation.

**Failure cases and verification:** Missing real authorisation/configuration or any required gate keeps affected task open and Live disabled; documentation approval alone authorises no arbitrary sends.

**Completion evidence:** Pilot references without sensitive data, reviewed release evidence, remaining blockers and truthful final status.
