# Vendor portal page index

Use owned routes under `/procurement`, Frappe website rendering and the active Website Theme. Public opportunity list/detail are the only guest business pages. Registration first uses the supported Frappe account/email verification flow. Every private controller/query applies explicit organisation membership, buying company and capability checks.

Do not grant native Supplier portal membership automatically. The owned portal exposes narrow DTOs; alternate native routes must meet the same managed-record boundaries before release. Shared visual/access requirements are in [UI design](../UI_DESIGN_SYSTEM.md) and [permissions](../PERMISSIONS_AND_PRIVACY.md).

## Route map

- [Public Opportunities](PUBLIC_OPPORTUNITIES.md): `/procurement/opportunities`.
- [Tender Detail](TENDER_DETAIL.md): `/procurement/opportunities/<id>`.
- [Registration](REGISTRATION.md): `/procurement/register`.
- [Application Progress](APPLICATION_PROGRESS.md): `/procurement/applications/<id>`.
- [Company Profile](COMPANY_PROFILE.md): `/procurement/profile`.
- [Compliance Documents](COMPLIANCE_DOCUMENTS.md): `/procurement/documents`.
- [Invitations](INVITATIONS.md): `/procurement/invitations`.
- [Bid Workspace](BID_WORKSPACE.md): `/procurement/bids/<id>/edit`.
- [Submitted Bids and Results](SUBMITTED_BIDS_AND_RESULTS.md): `/procurement/bids`.
- [Contracts and Orders](CONTRACTS_AND_ORDERS.md): `/procurement/contracts`.
- [Deliveries and Milestones](DELIVERIES_AND_MILESTONES.md): `/procurement/fulfilment`.
- [Invoice Claims and Payment Status](INVOICE_CLAIMS_AND_PAYMENTS.md): `/procurement/invoice-claims`.
- [Notifications](NOTIFICATIONS.md): `/procurement/notifications`.
- [Team and Preferences](TEAM_AND_PREFERENCES.md): `/procurement/team`.

Detail siblings for list routes use `/<id>` within the same protected controller family, except the documented bid edit path. Applications use `/procurement/applications` as the authenticated company-scoped list and the specified detail route for progress. Invitations may deep-link to the same opportunity detail only after invitation checks. Add an authenticated `/procurement` landing redirect to the current user's application progress or opportunity dashboard; never guess another organisation from email.

## Shared portal behaviour

Portal pages own presentation; use the [data model](../DATA_MODEL.md), [API contracts](../API_CONTRACTS.md) and [shared UI contract](../UI_DESIGN_SYSTEM.md) for common definitions. Feature tasks record real screen evidence; these documents are design specifications.

Show current organisation and buying-company context, safe next actions, last-saved time and explicit deadline/currency basis. Private HTML and downloads are not shared-cacheable. Public search/SEO metadata contains only approved publication fields. Login return routes must be relative allowlisted procurement paths to prevent open redirects.

All private pages need session-expiry recovery that preserves safe local edits while requiring reauthentication before submission. Evidence, bank and commercial values must not be stored in persistent browser storage. Confirm uncertainty through command receipts and durable operation status, not optimistic success banners.
