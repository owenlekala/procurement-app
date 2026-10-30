# ADR-001: App and design baseline

Status: Accepted. Date: 27 October 2026. Source: user-approved handbook plan and selected procurement scope.

## Decision

Create `tag_procurement` as a separate Frappe app requiring compatible Frappe/ERPNext v16. Provide the TAG Procurement Desk module and a native Frappe website vendor portal. Support multiple TAG buying companies, goods/services/works and the full procurement lifecycle. Use native widgets, forms, lists, reports, theme tokens and website templates; no independent SPA or CSS framework.

## Alternatives and consequences

Adding procurement to payroll or marketing couples unrelated release and access concerns; modifying Buying core makes upgrades fragile. A standalone frontend duplicates the user's requested native UI. Own app metadata/hooks, layered services and versioned migrations instead. Company policies, legal retention and financial thresholds require explicit operational configuration. The planning pack is implemented separately from future application tasks, which remain unstarted until evidence exists.

The [product baseline](../PRODUCT_REQUIREMENTS.md), [UI design](../UI_DESIGN_SYSTEM.md) and [release gates](../OPERATIONS_AND_RELEASE.md) carry the detailed consequences.
