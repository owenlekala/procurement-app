# Implementation sequence and phase gates

The [product baseline](PRODUCT_REQUIREMENTS.md) owns scope/defaults; [architecture](ARCHITECTURE.md) owns boundaries. The [task index](tasks/README.md) contains 40 individually identified implementation tasks, four per phase. Application implementation is not started.

## Ordered delivery and readiness

### P0 — Environment and bootstrap

[P0 — Environment and bootstrap tasks](tasks/P0-ENVIRONMENT-AND-BOOTSTRAP.md). Reproducible disposable runtime, independent app repository, versioned canonical handbook/instruction bridge and a deterministic test harness. No production traffic.

### P1 — App foundation and native UI

[P1 — App foundation and native UI tasks](tasks/P1-APP-AND-NATIVE-UI.md). Owned native navigation and themed portal foundation, managed-field/file/native-route isolation and actual supported-theme/keyboard evidence.

### P2 — Requirements, identity and registration

[P2 — Requirements, identity and registration tasks](tasks/P2-REGISTRATION-AND-PORTAL.md). No-code published requirement resolution, verified memberships, resumable clean-file applications and safe progress/correction receipts; outbound remains disabled.

### P3 — Approval, renewal and legacy migration

[P3 — Approval, renewal and legacy migration tasks](tasks/P3-APPROVAL-AND-COMPLIANCE.md). Independent activation, live expiry/renewal/remediation, bank controls and reviewed legacy/native portal reconciliation.

### P4 — Requests, authority and publication

[P4 — Requests, authority and publication tasks](tasks/P4-REQUESTS-AND-TENDERS.md). Authorised goods/service/works demand, native budget checks, all sourcing routes, immutable publication, matching and fair addenda.

### P5 — Sealed submissions and opening

[P5 — Sealed submissions and opening tasks](tasks/P5-BIDS-AND-OPENING.md). Complete separated bid drafts, atomic deadline/receipt/replacement flow and stage opening; no normal-path sealed content leak.

### P6 — Evaluation, awards and complaints

[P6 — Evaluation, awards and complaints tasks](tasks/P6-EVALUATION-AND-AWARDS.md). Conflict-aware scoring/moderation, commercial comparison, independent bounded awards, vendor response and complaints with downstream holds.

### P7 — Contracts, execution and financial handoff

[P7 — Contracts, execution and financial handoff tasks](tasks/P7-CONTRACTS-AND-FULFILMENT.md). Contract/variation/call-off, native purchasing/acceptance, claim/credit and accounting handoff. Every enabled advance/retention template has finance-reviewed posting evidence.

### P8 — Durable automation, notifications and reports

[P8 — Durable automation, notifications and reports tasks](tasks/P8-AUTOMATION-AND-REPORTING.md). Durable transport/recovery, versioned safe automation, purpose-aware email/portal notices and reconciled native reports/private exports.

### P9 — Production qualification and release

[P9 — Production qualification and release tasks](tasks/P9-QUALIFICATION-AND-RELEASE.md). Operational/security/load/migration/restore qualification, rendered screen/diagram review, complete documentation and a limited authorised pilot with release owners.

## Delivery discipline

Complete vertical slices and verify negative paths before advancing the serial task chain. Idempotent native mappings and durable work primitives may be built earlier where needed, but do not claim complete email delivery until P8 qualifies the shared transport. Source events and portal notices are durable from their feature slice onward.

Record evidence in progress; never infer implementation from specifications. Commit future app work in its own repository, not the workspace root or a framework/payroll checkout. Missing operational configuration or external pilot authorisation keeps only the affected gates open while independent work proceeds. Live activation requires the [release decision](OPERATIONS_AND_RELEASE.md), not a proportion of completed tasks.
