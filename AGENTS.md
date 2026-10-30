# TAG Procurement app instructions

Read the [canonical handbook](docs/procurement/README.md), its [kickoff contract](docs/procurement/IMPLEMENTATION_KICKOFF.md), [implementation rules](docs/procurement/IMPLEMENTATION_RULES.md), and [progress evidence](docs/procurement/PROGRESS.md) before changing app code.

Implement the first dependency-ready task in the [task index](docs/procurement/tasks/README.md). Read its owning specifications before editing. Keep domain decisions independent of Frappe, orchestration and transaction ownership in application services, and persistence/external services in infrastructure adapters. Controllers remain thin and validate ordinary saves.

Keep each policy, state machine, API contract, screen contract, and completion evidence in its owning handbook document. Link to it rather than duplicating it. Preserve stable `PROC-R`, `PROC-A`, and `PROC-P` identifiers. Record architectural changes as ADRs, add tests for negative paths, and record actual commands/results. Do not mark work production-ready or complete without the task's required evidence.

Use native Frappe/ERPNext components and the active website theme. Do not modify sibling Frappe, ERPNext, payroll, or marketing repositories as part of procurement work. Keep secrets and disposable runtime data in ignored `.local` paths.
