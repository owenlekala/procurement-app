# Desk page index

The destinations below comprise the owned TAG Procurement Sidebar. Use native forms/lists/reports except the bounded evaluation Page and native Workspace. Generate form/list/report routes through the installed framework; do not invent legacy routes. Only menu visibility is role-based; all resource access is enforced independently.

Shared requirements live in [UI design](../UI_DESIGN_SYSTEM.md), [permissions](../PERMISSIONS_AND_PRIVACY.md) and [API contracts](../API_CONTRACTS.md). Page documents own layout, context, state actions, validation/recovery and responsive details. They must not redefine schema or lifecycle rules.

## Navigation

- [Overview](OVERVIEW.md): `Workspace`.
- [Procurement Requests](PROCUREMENT_REQUESTS.md): `PROC Procurement Request`.
- [Vendor Applications](VENDOR_APPLICATIONS.md): `PROC Vendor Application`.
- [Vendor Database](VENDOR_DATABASE.md): `PROC Company Approval`.
- [Compliance Reviews](COMPLIANCE_REVIEWS.md): `PROC Review Task`.
- [Tenders](TENDERS.md): `PROC Tender`.
- [Evaluation](EVALUATION.md): `Page proc-evaluation`.
- [Awards](AWARDS.md): `PROC Award`.
- [Contracts](CONTRACTS.md): `PROC Contract Control`.
- [Orders and Fulfilment](ORDERS_AND_FULFILMENT.md): `Report Procurement Fulfilment`.
- [Invoice Claims](INVOICE_CLAIMS.md): `PROC Invoice Claim`.
- [Reports](REPORTS.md): `Native Script Reports`.
- [Automations](AUTOMATIONS.md): `PROC Automation Rule`.
- [Settings](SETTINGS.md): `PROC Settings`.

## Shared screen acceptance

Schema and transport are owned by [data model](../DATA_MODEL.md) and [API contracts](../API_CONTRACTS.md); individual pages own presentation only. Each feature records actual screenshot evidence in its implementation task. Screen specifications are not runtime screenshots.

Every destination must include loading, empty, denied, stale-revision, network failure and successful-action behaviour. Preserve entered drafts, expose actionable blockers and use idempotent commands. Reference comparisons use actual ERPNext and active-theme screenshots, keyboard navigation and 1440/1024/390px viewports. Runtime evidence belongs to the implementing task, not this index.
