# Procurement flow index

These flows connect the authoritative policies to the user-facing screens and durable work. Each includes a Mermaid diagram, entry/transaction ownership, decisions, failure recovery and linked acceptance scenarios. Read [architecture](../ARCHITECTURE.md) for shared locking/commit rules and [permissions](../PERMISSIONS_AND_PRIVACY.md) for access boundaries.

## End-to-end journeys

- [Identity, membership and onboarding](IDENTITY_AND_ONBOARDING.md).
- [Configurable registration and review](REGISTRATION_AND_REVIEW.md).
- [Expiry, renewal and policy remediation](RENEWAL_AND_REMEDIATION.md).
- [Request, budget authority and sourcing route](REQUEST_AND_SOURCING.md).
- [Tender publication, matching and shared changes](PUBLICATION_AND_MATCHING.md).
- [Sealed bid submission and replacement](BID_SUBMISSION_AND_REVISION.md).
- [Opening, scoring and commercial release](OPENING_AND_EVALUATION.md).
- [Award, vendor response and complaint](AWARD_ACCEPTANCE_AND_COMPLAINT.md).
- [Contracts, variations and order allocation](CONTRACTS_AND_ORDERS.md).
- [Delivery, acceptance, claims and settlement visibility](FULFILMENT_CLAIMS_AND_PAYMENT.md).
- [Durable rules, notices and worker recovery](AUTOMATION_AND_RECOVERY.md).
- [Legacy migration, retention and offboarding](MIGRATION_AND_OFFBOARDING.md).

All routes start from an authorised actor and preserve source versions/audit. A portal action cannot bypass review, a scheduled timer cannot backdate a submission, and a background retry cannot duplicate a financial commitment. Flow diagrams summarise orchestration; resolve field/state details through [data model](../DATA_MODEL.md) and transport through [API contracts](../API_CONTRACTS.md). Exercise normal and rejected paths with synthetic actors and real database constraints; a diagram is not execution evidence.
