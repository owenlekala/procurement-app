# ADR-002: Shared identity and ERPNext ownership

Status: Accepted. Date: 27 October 2026. Related: PROC-R03, PROC-R04, PROC-R07, PROC-R20–PROC-R24.

## Decision

One vendor organisation represents legal identity and has a reviewed Supplier link. Explicit memberships authorise people. Separate company/category approval and evidence-sharing grants determine eligibility. Shared identity never shares confidential applications automatically. ERPNext owns purchasing, stock and accounting records; owned procurement records govern approval, sealed sourcing, service acceptance and portal claims.

## Alternatives and consequences

A separate Supplier per buying company creates identity duplicates and fragmented accounting. A single approved flag on Supplier grants too much cross-company authority. Using native Supplier portal membership alone loses contributor/finance separation. Use company-scoped predicates across native and owned routes and audit existing portal grants before launch.

Keep company suspensions separate from global Supplier disablement. Preserve native accounting validation, use idempotent source mappings, and treat invoice claims as review input rather than posted invoices. The [integration contract](../ERPNext_INTEGRATION.md) owns concrete mappings and cancellation behaviour.
