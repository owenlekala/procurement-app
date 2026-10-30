# Settings

Native destination: `PROC Settings`. Audience: System managers plus authorised company policy owners.

[Screen contract](README.md) · [Policy owner](../OPERATIONS_AND_RELEASE.md).

## Components and layout

Native settings Form with Company policies, Requirements, Roles/delegations, Notifications, Storage/scanning, Retention, Readiness and Diagnostics tabs. Protect secrets with native password controls.

## Displayed fields and context

Company selectors, complete threshold bands, approval stages, requirement versions, sender/scanner health, pilot allowlists, retention owners, feature switches and evidence links.

## Actions by state

Preview/publish policy or requirements; run synthetic diagnostics; rotate secrets; manage pilot scope; enable only after gates; emergency-disable with reason. No bulk business approval control.

## Permission boundaries

Technical administration is separate from business sign-off. Company policies require the relevant policy owner; read-only diagnostics redact credentials and sensitive vendor data.

## Validation, loading and exception states

Incomplete policy, missing retention, unhealthy scanner/worker or absent pilot evidence produces explicit readiness blockers. Changing a global setting must not reset company policies/customisations.

## Responsive and keyboard behaviour

Tabs collapse into accessible sections; dangerous switches use native review dialogs naming their scope and preserving current operational state.

## Acceptance links

[PROC-A01](../TESTING_AND_ACCEPTANCE.md#proc-a01), [PROC-A05](../TESTING_AND_ACCEPTANCE.md#proc-a05), [PROC-A12](../TESTING_AND_ACCEPTANCE.md#proc-a12), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).
