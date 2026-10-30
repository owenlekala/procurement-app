# Notifications

Website route: `/procurement/notifications`. Audience: Authenticated members viewing their own company/organisation notices.

[Screen contract](README.md) · [Policy owner](../AUTOMATION_AND_RELIABILITY.md).

## Components and layout

Paginated native-style notification centre with unread/purpose/company filters, safe text summaries and authenticated resource links.

## Displayed fields and context

Title, purpose, essential/optional label, source reference, timestamp, read state and permitted next action. No envelope or bank content is embedded.

## Actions by state

Open resource, mark own notices read, adjust optional job subscriptions and inspect delivery-independent portal history. Essential notices cannot be disabled in preferences.

## Permission boundaries

Resource access is checked again on click, not conferred by possession of an old notice. Revoked memberships do not retain sensitive cached content.

## Validation, loading and exception states

Empty unread list offers all notices; stale/inaccessible links display a safe unavailable state. Read marking is idempotent and does not change workflow completion.

## Responsive and keyboard behaviour

One-column rows support keyboard focus and text/icon status; do not announce every background update through live regions.

## Acceptance links

[PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
