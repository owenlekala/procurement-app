# P8 — Durable automation, notifications and reports

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P8-001

- [ ] **Implement shared durable transport and recovery workers**

**Depends on:** `PROC-P7-004`

**Requirements:** PROC-R26, PROC-R29. **Acceptance:** [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).

**Read first:** [Automation And Reliability](../AUTOMATION_AND_RELIABILITY.md) · [Architecture](../ARCHITECTURE.md).

**Implementation and boundaries:** Complete Event/Outbox/Operation processing, on-commit enqueue, indexed recovery, fenced claims, wait scheduling, bounded known-safe retries and evidence-backed resolve_unknown_mail disposition using qualified adapters.

**Failure cases and verification:** Inject rollback/enqueue loss/worker death/stale lease/possible SMTP acceptance; no duplicate commitments or blind resend.

**Completion evidence:** Failure-injection matrix, operator work queue and adapter acceptance classifications.

## PROC-P8-002

- [ ] **Implement native automation editor and initial journeys**

**Depends on:** `PROC-P8-001`

**Requirements:** PROC-R26, PROC-R14, PROC-R08. **Acceptance:** [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26), [PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A08](../TESTING_AND_ACCEPTANCE.md#proc-a08).

**Read first:** [Automation And Reliability](../AUTOMATION_AND_RELIABILITY.md) · [Automations](../pages/AUTOMATIONS.md).

**Implementation and boundaries:** Implement allowlisted versioned rules/run-as, side-effect-free simulation, durable steps/waits and all specified review/expiry/tender/award/contract/claim journeys.

**Failure cases and verification:** Reject cycles/scripts/forbidden approvals; preserve old waiting versions and recheck authority/current state at resume.

**Completion evidence:** Published-rule fixtures, initial journey coverage and native editor screenshots.

## PROC-P8-003

- [ ] **Complete email, portal notices and preferences**

**Depends on:** `PROC-P8-002`

**Requirements:** PROC-R14, PROC-R26, PROC-R28. **Acceptance:** [PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Automation And Reliability](../AUTOMATION_AND_RELIABILITY.md) · [Notifications](../portal/NOTIFICATIONS.md).

**Implementation and boundaries:** Connect all persisted feature events to minimal versioned email/portal templates, optional matching/digests, essential notices, read cursors, bounce handling and safe links.

**Failure cases and verification:** Test opt-out while queued, expired membership, obsolete tender messages, failed essential mail and no envelope/secret payload.

**Completion evidence:** Catalogue-to-event reconciliation, fake-provider results and notification/preferences UI evidence.

## PROC-P8-004

- [ ] **Implement reconciled reports and private exports**

**Depends on:** `PROC-P8-003`

**Requirements:** PROC-R27, PROC-R24, PROC-R25, PROC-R28. **Acceptance:** [PROC-A27](../TESTING_AND_ACCEPTANCE.md#proc-a27), [PROC-A24](../TESTING_AND_ACCEPTANCE.md#proc-a24), [PROC-A25](../TESTING_AND_ACCEPTANCE.md#proc-a25), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Reporting](../REPORTING.md) · [Reports](../pages/REPORTS.md).

**Implementation and boundaries:** Build native Script Reports/cards with explicit denominators/time/currency basis and authorised drill-down; persist bounded private exports and current permission checks.

**Failure cases and verification:** Reconcile duplicate/revised/cancelled/amended sources, credits/reversals, Unknowns and export revocation/formula escaping.

**Completion evidence:** Fixture-to-report/native-ledger reconciliation and native card/report/export evidence.
