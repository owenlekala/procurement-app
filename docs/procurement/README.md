# TAG Procurement implementation handbook

Accepted planning baseline: 27 October 2026. This is the canonical procurement specification. Application implementation is **Not started**; production readiness is **Not qualified**. See [progress](PROGRESS.md) for evidence rather than inferring completion from document existence.

Build `tag_procurement`, a separate Frappe app containing the **TAG Procurement** module, with native ERPNext Desk and a Frappe vendor portal. Cover multi-company vendor onboarding, configurable compliance, goods/services/works sourcing, sealed tenders, evaluation, award, contracts, fulfilment, invoice claims and accounting-derived payment status.

## Start here

1. Read [product requirements](PRODUCT_REQUIREMENTS.md), [implementation rules](IMPLEMENTATION_RULES.md), [policy](PROCUREMENT_POLICY.md) and [setup](FRAMEWORK_AND_SETUP.md).
2. Read [architecture](ARCHITECTURE.md), [data model](DATA_MODEL.md), [API contracts](API_CONTRACTS.md), [permissions](PERMISSIONS_AND_PRIVACY.md) and [UI design](UI_DESIGN_SYSTEM.md).
3. Follow the applicable [Desk page](pages/README.md), [portal page](portal/README.md) and [flow](flows/README.md).
4. Select a dependency-ready [task](tasks/README.md), follow [kickoff](IMPLEMENTATION_KICKOFF.md), verify [acceptance](TESTING_AND_ACCEPTANCE.md) and record evidence.

## Specification owners

- [Registration and compliance](REGISTRATION_AND_COMPLIANCE.md): requirement builder, registration, review, expiry and renewal.
- [Procurement policy](PROCUREMENT_POLICY.md): approval authority, budgets and sourcing routes.
- [Tendering and evaluation](TENDERING_AND_EVALUATION.md): publication, bidding, opening, scoring and award.
- [Contracts and fulfilment](CONTRACTS_AND_FULFILMENT.md): commercial obligations, execution, claims and closeout.
- [ERPNext integration](ERPNext_INTEGRATION.md): native record ownership, mappings and lifecycle guards.
- [Automation and reliability](AUTOMATION_AND_RELIABILITY.md): durable triggers, notifications and recovery.
- [Reporting](REPORTING.md): metric definitions, currencies, safe drill-down and exports.
- [Operations and release](OPERATIONS_AND_RELEASE.md): readiness, monitoring, backup and production gates.
- [Implementation plan](IMPLEMENTATION_PLAN.md): phases; [traceability](TRACEABILITY.md): coverage; [decisions](decisions/README.md): accepted architecture; [references](REFERENCES.md): inspected sources.

## Handbook ownership

Fields and persisted state names belong to the data model; endpoint shapes to API contracts; transition policy to its subject owner; layout to page specifications. Other files link instead of copying those definitions. Task completion checkboxes belong only in phase files; evidence belongs in progress. Requirement, task and acceptance IDs are stable.

The workspace root is not a Git repository. During P0 place this handbook under the future app's versioned ownership, update source references, and leave only a pointer at an old location if moved. Do not maintain editable duplicate handbooks. The existing WhatsApp handbook remains independent.
