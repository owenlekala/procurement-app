# Team and Preferences

Website route: `/procurement/team`. Audience: Organisation Owners managing teams; all members managing their own preferences.

[Screen contract](README.md) · [Policy owner](../PERMISSIONS_AND_PRIVACY.md).

## Components and layout

Themed membership list and native dialogs for invite/capabilities/ownership, followed by language and optional job-alert preferences.

## Displayed fields and context

Member identity, Owner/Contributor state, Bid Submitter/Billing/Bank Maintainer capabilities, invite expiry, active company subscriptions and verified contact state.

## Actions by state

Owner invites/revokes/changes capabilities or requests verified ownership transfer. Members choose language/digest/immediate/opt-out for optional jobs; essential notices are explained.

## Permission boundaries

No self-granted capabilities, email-domain takeover or removal of the last Owner. Invitation acceptance binds to intended verified user/organisation and cannot expand its grant.

## Validation, loading and exception states

Expired/replayed invitations fail safely. Stale membership edits show current access before applying. Ownership recovery needs independent verification rather than a support bypass.

## Responsive and keyboard behaviour

Member rows show role/capabilities in readable text; destructive revocation dialog names the user/organisation and returns focus after completion.

## Acceptance links

[PROC-A04](../TESTING_AND_ACCEPTANCE.md#proc-a04), [PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A26](../TESTING_AND_ACCEPTANCE.md#proc-a26), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
