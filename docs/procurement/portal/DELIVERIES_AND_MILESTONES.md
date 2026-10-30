# Deliveries and Milestones

Website route: `/procurement/fulfilment`. Audience: Own organisation delivery/service contributors and contract contacts.

[Screen contract](README.md) · [Policy owner](../CONTRACTS_AND_FULFILMENT.md).

## Components and layout

Themed order/milestone progress list and evidence-submission form, with reported and internally accepted quantities shown separately.

## Displayed fields and context

PO/contract line, planned date, dispatch/delivery details, completion quantity/value, private supporting files, internal acceptance/correction reasons and outstanding amount.

## Actions by state

Save/submit dispatch or completion; respond to correction; propose partial completion or return. Only internal receiving can accept/post stock or service entitlement.

## Permission boundaries

Only own contract lines and explicitly permitted evidence appear. Contributor submission cannot approve their own work or exceed an allocation.

## Validation, loading and exception states

Validate source/remaining quantity, clean files and milestone scope. Pending inspection is not accepted. Downstream invoicing constrains reversal and creates a visible dispute route.

## Responsive and keyboard behaviour

Use step/status text for delivery→inspection→acceptance; line editing is single-column with labelled quantity/UOM and evidence controls.

## Acceptance links

[PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21), [PROC-A22](../TESTING_AND_ACCEPTANCE.md#proc-a22), [PROC-A23](../TESTING_AND_ACCEPTANCE.md#proc-a23).
