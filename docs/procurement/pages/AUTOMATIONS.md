# Automations

Native destination: `PROC Automation Rule`. Audience: Procurement administrators and scoped operational owners.

[Screen contract](README.md) · [Policy owner](../AUTOMATION_AND_RELIABILITY.md).

## Components and layout

Native rule Form/List with Trigger, Conditions, Ordered actions, Run-as, Simulation, Versions and Run history. Operational errors link to persisted runs/outbox.

## Displayed fields and context

Allowlisted event/context, company scope, forward steps, template/purpose, wait time, service principal, published hash and safe simulated recipients/exclusions.

## Actions by state

Save draft; simulate without mutations; publish/retire; pause new starts; inspect/cancel active runs; retry only proven safe failed work with a recorded reason.

## Permission boundaries

Run-as privileges are bounded and rechecked. No action grants approval, opens bids, changes bank approval, posts financial documents or executes payments.

## Validation, loading and exception states

Unknown steps/cycles/overlong definitions fail publication. Unknown mail is not retried blindly. Existing runs retain their old version on a new publication.

## Responsive and keyboard behaviour

Ordered steps become stacked groups; no drag-and-drop requirement. Show step number/state and preserve typed draft data on validation errors.

## Acceptance links

[PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).
