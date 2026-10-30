# P0 — Environment and bootstrap

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P0-001

- [x] **Verify source and deployment baseline**

**Depends on:** None; first implementation task.

**Requirements:** PROC-R01, PROC-R29. **Acceptance:** [PROC-A01](../TESTING_AND_ACCEPTANCE.md#proc-a01), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).

**Read first:** [Framework And Setup](../FRAMEWORK_AND_SETUP.md) · [References](../REFERENCES.md).

**Implementation and boundaries:** Record inspected forks/revisions, runtime manifests and actual available container/site inventory without printing secrets. Separate source facts from unverified deployment assumptions.

**Failure cases and verification:** Check missing dependencies and unsupported runtime versions; do not substitute upstream releases silently.

**Completion evidence:** Exact version/commit inventory, runtime findings and remaining setup blockers.

**Execution evidence (2026-10-30):** Source checkouts inspected locally: Frappe 16.53.0 at `e8d41dd006` (2026-10-22), ERPNext 16.52.1 at `ade850bbd6` (2026-10-22), and `frappe_za_core` at `a6128f1` (2026-10-08). `frappe/pyproject.toml` requires Python `>=3.14,<3.15`; ERPNext requires Python `>=3.14`; Node is `v24.15.0`. Host `python3` is 3.9.6 and has no `bench` executable. Docker CLI/Compose are 29.4.1/5.1.3; the default sandbox could not access the Docker Desktop socket, but a read-only check outside that sandbox confirmed Docker Desktop 29.4.1 is running. Its existing WhatsApp stack uses Python 3.14.8, the pinned Frappe/ERPNext revisions above, MariaDB/Redis health checks, and site `wa-marketing.localhost`; that site is not a procurement test site and will not be modified. No secrets were read or printed. `tag_marketing` has 43 pre-existing changed/untracked paths and was left untouched.

## PROC-P0-002

- [ ] **Establish disposable reproducible runtime**

**Depends on:** `PROC-P0-001`, `PROC-P0-003`

**Requirements:** PROC-R01, PROC-R29. **Acceptance:** [PROC-A01](../TESTING_AND_ACCEPTANCE.md#proc-a01), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).

**Read first:** [Framework And Setup](../FRAMEWORK_AND_SETUP.md) · [Operations And Release](../OPERATIONS_AND_RELEASE.md).

**Implementation and boundaries:** Prepare pinned app-owned development configuration, disposable Bench/site, ERPNext installation, private storage/scanner fakes and dedicated queues. Verify DB/Redis/scheduler/realtime with synthetic diagnostics.

**Failure cases and verification:** Prove repeated startup, asset build and worker recovery; no production mutations or external notifications.

**Completion evidence:** Image digests, commands, disposable site details and diagnostic results.

## PROC-P0-003

- [x] **Create app repository and instruction bridge**

**Depends on:** `PROC-P0-001`

**Requirements:** PROC-R01, PROC-R30. **Acceptance:** [PROC-A01](../TESTING_AND_ACCEPTANCE.md#proc-a01), [PROC-A30](../TESTING_AND_ACCEPTANCE.md#proc-a30).

**Read first:** [Implementation Kickoff](../IMPLEMENTATION_KICKOFF.md) · [Architecture](../ARCHITECTURE.md).

**Implementation and boundaries:** Scaffold independent tag_procurement app, version this canonical handbook and create app-level AGENTS.md bridge. Declare tested dependencies and owned packaging without framework/payroll edits.

**Failure cases and verification:** Verify ownership, repeatable installation and source-link validation after any documentation move; leave no editable second handbook.

**Completion evidence:** Repository commit, app inventory, instruction bridge and structural-check result.

**Execution evidence (2026-10-30):** Created the independent `tag_procurement` Git repository at commit `295921a` with app packaging metadata, the Frappe module package, the app-level `AGENTS.md` bridge and the handbook as its only canonical copy. Built `tag_procurement-0.1.0-py3-none-any.whl` (SHA-256 `993aa63dc27d249c5ada3af2cbfba2c17b9197983299e97af188d06460bd990a`) using Python 3.14.8 and the pinned `frappe/bench` image; source was mounted read-only. `python3 tag_procurement/docs/procurement/validate_docs.py --self-test` passed with 82 Markdown files, 865 local links, 27 source references, all 30 requirement/acceptance mappings, all 40 tasks and all nine negative self-tests. This establishes package metadata and handbook ownership; it does not qualify site installation or app runtime behaviour.

## PROC-P0-004

- [ ] **Establish deterministic test and adapter harness**

**Depends on:** `PROC-P0-003`

**Requirements:** PROC-R01, PROC-R03, PROC-R29. **Acceptance:** [PROC-A01](../TESTING_AND_ACCEPTANCE.md#proc-a01), [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).

**Read first:** [Testing And Acceptance](../TESTING_AND_ACCEPTANCE.md) · [Architecture](../ARCHITECTURE.md).

**Implementation and boundaries:** Configure domain/integration/browser scripts, fake clock/mail/scanner, two-company/two-vendor fixtures and disabled unexpected network traffic. Exercise actual DB uniqueness/locking.

**Failure cases and verification:** Verify one passing and intentionally failing harness case, source rollback and controlled adapter failure.

**Completion evidence:** Exact supported commands, fixtures and harness results; no runtime test claims from mocks alone.
