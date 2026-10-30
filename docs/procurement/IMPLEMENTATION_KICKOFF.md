# Implementation kickoff

This handbook is the authorised documentation deliverable. Application code is future work and must begin through the [task index](tasks/README.md). Do not scaffold an app merely to make documentation progress look complete.

## First implementation session

Read [product requirements](PRODUCT_REQUIREMENTS.md), [rules](IMPLEMENTATION_RULES.md), [architecture](ARCHITECTURE.md), [setup](FRAMEWORK_AND_SETUP.md), [policy](PROCUREMENT_POLICY.md) and [progress](PROGRESS.md). Identify the first unblocked task and its linked acceptance checks. Reconfirm exact local revisions and a disposable runtime before issuing Bench commands.

Create the independent `tag_procurement` repository during P0, establish versioned handbook ownership and an app-level AGENTS.md bridge, and retain this documentation at one canonical location. Do not initialise Git at the workspace root or modify framework/payroll repositories as an incidental bootstrap step.

## Task execution contract

Implement one coherent vertical slice, including negative paths and operator recovery. Inspect this fork's supported APIs before choosing hooks. Update the owning spec if verified runtime behaviour requires a design correction; architectural changes get an ADR. Preserve stable IDs and actor/company/envelope boundaries.

Run the relevant domain/integration/browser/operational checks, capture actual commands/results and safe screenshots, and append evidence. Check only that task's phase checkbox when all required evidence passes. Missing credentials, runtime or external authorisation leaves the affected task open; complete independent work and report the specific limitation.

P0 establishes exact app lint/type/browser commands. Initial planning does not assert those scripts or a working site already exist. All synthetic data must remain separate from real vendor, bank, tax and tender records.
