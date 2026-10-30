# Task index and completion contract

Select the first dependency-ready task. Forty implementation tasks are sequenced through ten phases; dependencies intentionally form one serial readiness chain so a later feature cannot skip its access/reliability prerequisites. Feature events may be persisted before P8, but external dispatch waits for the qualified transport.

Read [implementation rules](../IMPLEMENTATION_RULES.md), [kickoff](../IMPLEMENTATION_KICKOFF.md), [phase gates](../IMPLEMENTATION_PLAN.md) and [progress](../PROGRESS.md). This index owns navigation, not a second task status tracker.

## Ordered backlog

### P0 — Environment and bootstrap

- [PROC-P0-001: Verify source and deployment baseline](P0-ENVIRONMENT-AND-BOOTSTRAP.md#proc-p0-001).
- [PROC-P0-003: Create app repository and instruction bridge](P0-ENVIRONMENT-AND-BOOTSTRAP.md#proc-p0-003).
- [PROC-P0-002: Establish disposable reproducible runtime](P0-ENVIRONMENT-AND-BOOTSTRAP.md#proc-p0-002).
- [PROC-P0-004: Establish deterministic test and adapter harness](P0-ENVIRONMENT-AND-BOOTSTRAP.md#proc-p0-004).

### P1 — App foundation and native UI

- [PROC-P1-001: Implement owned schema, company boundaries and roles](P1-APP-AND-NATIVE-UI.md#proc-p1-001).
- [PROC-P1-002: Register navigation and native visual foundations](P1-APP-AND-NATIVE-UI.md#proc-p1-002).
- [PROC-P1-003: Implement themed portal shell and alternate-route guards](P1-APP-AND-NATIVE-UI.md#proc-p1-003).
- [PROC-P1-004: Qualify foundation and full UI contract](P1-APP-AND-NATIVE-UI.md#proc-p1-004).

### P2 — Requirements, identity and registration

- [PROC-P2-001: Implement versioned requirement and policy builders](P2-REGISTRATION-AND-PORTAL.md#proc-p2-001).
- [PROC-P2-002: Implement organisation claims and verified memberships](P2-REGISTRATION-AND-PORTAL.md#proc-p2-002).
- [PROC-P2-003: Implement resumable applications and quarantined uploads](P2-REGISTRATION-AND-PORTAL.md#proc-p2-003).
- [PROC-P2-004: Implement progress, correction and applicant communications](P2-REGISTRATION-AND-PORTAL.md#proc-p2-004).

### P3 — Approval, renewal and legacy migration

- [PROC-P3-001: Implement review stages and independent activation](P3-APPROVAL-AND-COMPLIANCE.md#proc-p3-001).
- [PROC-P3-002: Implement expiry, renewal, sharing and remediation](P3-APPROVAL-AND-COMPLIANCE.md#proc-p3-002).
- [PROC-P3-003: Implement bank-change and native payment protection](P3-APPROVAL-AND-COMPLIANCE.md#proc-p3-003).
- [PROC-P3-004: Implement legacy import and duplicate reconciliation](P3-APPROVAL-AND-COMPLIANCE.md#proc-p3-004).

### P4 — Requests, authority and publication

- [PROC-P4-001: Implement requests and native budget approval](P4-REQUESTS-AND-TENDERS.md#proc-p4-001).
- [PROC-P4-002: Implement sourcing routes and controlled exceptions](P4-REQUESTS-AND-TENDERS.md#proc-p4-002).
- [PROC-P4-003: Implement immutable tender publication and public discovery](P4-REQUESTS-AND-TENDERS.md#proc-p4-003).
- [PROC-P4-004: Implement matching, clarifications and addenda](P4-REQUESTS-AND-TENDERS.md#proc-p4-004).

### P5 — Sealed submissions and opening

- [PROC-P5-001: Implement separate envelope drafts and protected evidence](P5-BIDS-AND-OPENING.md#proc-p5-001).
- [PROC-P5-002: Implement atomic submit, receipt, replacement and withdrawal](P5-BIDS-AND-OPENING.md#proc-p5-002).
- [PROC-P5-003: Implement staged two-actor opening](P5-BIDS-AND-OPENING.md#proc-p5-003).
- [PROC-P5-004: Qualify bid fairness and sealed-content boundaries](P5-BIDS-AND-OPENING.md#proc-p5-004).

### P6 — Evaluation, awards and complaints

- [PROC-P6-001: Implement assignments, conflicts and immutable scoring](P6-EVALUATION-AND-AWARDS.md#proc-p6-001).
- [PROC-P6-002: Implement moderation and commercial comparison](P6-EVALUATION-AND-AWARDS.md#proc-p6-002).
- [PROC-P6-003: Implement independent awards and vendor response](P6-EVALUATION-AND-AWARDS.md#proc-p6-003).
- [PROC-P6-004: Implement complaints, withdrawal and sourcing outcomes](P6-EVALUATION-AND-AWARDS.md#proc-p6-004).

### P7 — Contracts, execution and financial handoff

- [PROC-P7-001: Implement contract control, obligations and variations](P7-CONTRACTS-AND-FULFILMENT.md#proc-p7-001).
- [PROC-P7-002: Implement idempotent orders and goods/service acceptance](P7-CONTRACTS-AND-FULFILMENT.md#proc-p7-002).
- [PROC-P7-003: Implement claims, invoice matching and credit review](P7-CONTRACTS-AND-FULFILMENT.md#proc-p7-003).
- [PROC-P7-004: Qualify financial schedules, payment visibility and closeout](P7-CONTRACTS-AND-FULFILMENT.md#proc-p7-004).

### P8 — Durable automation, notifications and reports

- [PROC-P8-001: Implement shared durable transport and recovery workers](P8-AUTOMATION-AND-REPORTING.md#proc-p8-001).
- [PROC-P8-002: Implement native automation editor and initial journeys](P8-AUTOMATION-AND-REPORTING.md#proc-p8-002).
- [PROC-P8-003: Complete email, portal notices and preferences](P8-AUTOMATION-AND-REPORTING.md#proc-p8-003).
- [PROC-P8-004: Implement reconciled reports and private exports](P8-AUTOMATION-AND-REPORTING.md#proc-p8-004).

### P9 — Production qualification and release

- [PROC-P9-001: Implement readiness, observability and privacy operations](P9-QUALIFICATION-AND-RELEASE.md#proc-p9-001).
- [PROC-P9-002: Run security, capacity, upgrade and restore qualification](P9-QUALIFICATION-AND-RELEASE.md#proc-p9-002).
- [PROC-P9-003: Validate handbook traceability and rendered journeys](P9-QUALIFICATION-AND-RELEASE.md#proc-p9-003).
- [PROC-P9-004: Complete authorised pilot and release decision](P9-QUALIFICATION-AND-RELEASE.md#proc-p9-004).

## Shared completion rules

1. Read the owning specifications and source register. Implement complete data/service/permission/UI/recovery vertical slices, not placeholder screens or success-only paths.
2. Run all linked acceptance checks appropriate to the slice, including denial/concurrency/failure cases. Broad scenarios such as PROC-A29 are staged: early tasks verify their setup/adapter portion, and P9 runs the complete capacity/restore/pilot scenario. State the exercised portion and deferred checks explicitly; an early partial result does not complete the global release gate. Capture actual native/portal screen comparisons where applicable; common visual rules are not copied into every task.
3. Record commit/image/site type, exact commands/results, acceptance IDs, safe screenshots/artifacts, unresolved failures and next action using [progress evidence](../PROGRESS.md#implementation-evidence-format).
4. Update affected owning contracts, diagrams and traceability; run the read-only documentation validator. Architecture changes require an ADR.
5. Check only this task's single phase checkbox after all required evidence passes. Partial offline success or unavailable required live verification leaves the task open and evidence marked In progress/Blocked.

Phase readiness comes from the gates, not another checkbox list. External notifications and production activation require explicit scope/configuration and the operational gates; no task title implies a live authorisation.
