# P1 — App foundation and native UI

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P1-001

- [ ] **Implement owned schema, company boundaries and roles**

**Depends on:** `PROC-P0-004`

**Requirements:** PROC-R01, PROC-R03, PROC-R28. **Acceptance:** [PROC-A01](../TESTING_AND_ACCEPTANCE.md#proc-a01), [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Data Model](../DATA_MODEL.md) · [Permissions And Privacy](../PERMISSIONS_AND_PRIVACY.md).

**Implementation and boundaries:** Create foundational settings/identity/policy/audit/operation metadata, shared permission predicates, managed-field guards and default-disabled readiness. Preserve company/global record distinctions.

**Failure cases and verification:** Test generic CRUD/import/direct IDs and missing scope; seeds/migrations must preserve customisations.

**Completion evidence:** Schema/constraint/migration and two-company negative-path evidence.

## PROC-P1-002

- [ ] **Register navigation and native visual foundations**

**Depends on:** `PROC-P1-001`

**Requirements:** PROC-R02, PROC-R03. **Acceptance:** [PROC-A02](../TESTING_AND_ACCEPTANCE.md#proc-a02), [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03).

**Read first:** [Ui Design System](../UI_DESIGN_SYSTEM.md) · [Readme](../pages/README.md).

**Implementation and boundaries:** Create owned Desktop Icon/Sidebar/Workspace and role-filtered destinations, common controls/dialogs/operation progress and scoped assets. Keep Buying metadata unchanged.

**Failure cases and verification:** Check absent optional navigation adapter, asset errors, denied/empty states and theme leakage.

**Completion evidence:** Rendered reference comparisons and repeat install/navigation checks.

## PROC-P1-003

- [ ] **Implement themed portal shell and alternate-route guards**

**Depends on:** `PROC-P1-002`

**Requirements:** PROC-R02, PROC-R03, PROC-R04, PROC-R28. **Acceptance:** [PROC-A02](../TESTING_AND_ACCEPTANCE.md#proc-a02), [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A04](../TESTING_AND_ACCEPTANCE.md#proc-a04), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Readme](../portal/README.md) · [Erpnext Integration](../ERPNext_INTEGRATION.md).

**Implementation and boundaries:** Build website-theme shell, explicit organisation/company context, login-return controls, no-store private pages and shared DTO/file gates. Enforce equivalent boundaries on managed native Supplier routes.

**Failure cases and verification:** Test session expiry, cross-membership context, native Supplier role bypass, raw File and shared-cache leakage.

**Completion evidence:** Two-vendor route/download tests and active website-theme screenshots.

## PROC-P1-004

- [ ] **Qualify foundation and full UI contract**

**Depends on:** `PROC-P1-003`

**Requirements:** PROC-R01, PROC-R02, PROC-R03, PROC-R28. **Acceptance:** [PROC-A01](../TESTING_AND_ACCEPTANCE.md#proc-a01), [PROC-A02](../TESTING_AND_ACCEPTANCE.md#proc-a02), [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).

**Read first:** [Ui Design System](../UI_DESIGN_SYSTEM.md) · [Testing And Acceptance](../TESTING_AND_ACCEPTANCE.md).

**Implementation and boundaries:** Verify all destination registrations/shared layouts, keyboard/error/loading foundations, restricted payload invisibility and repeated migrations using the actual runtime.

**Failure cases and verification:** Check 1440/1024/390px supported themes, customisation preservation and unauthorised widgets/counts.

**Completion evidence:** Foundation visual/accessibility and install evidence; feature screen evidence remains with later slices.
