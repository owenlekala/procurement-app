# Permissions, privacy and protected evidence

Owner: PROC-R03, PROC-R04, PROC-R09, PROC-R16–PROC-R19, PROC-R28. This is an application access design; privacy retention and organisational policy require explicit configuration, without invented legal periods.

## Role and resource boundaries

**Guest:** sanitised published public opportunities and explicitly public tender attachments only. No organisation search, application status, participant count identifying vendors, bid or compliance access.

**Vendor Owner:** own verified organisation profile proposals, company applications, evidence grants, team management and bid/claim submission. **Vendor Contributor:** own-organisation draft/profile/document preparation; cannot invite owners, change bank data or submit a bid unless granted explicit Bid Submitter capability. Separate Billing capability permits financial claim/view access; ordinary contributors cannot see invoice/payment details. Owners may see masked bank state; full bank proof requires Bank Maintainer capability and restricted finance access.

**Procurement Administrator:** company-scoped configuration of requirements, categories/regions, authority routing and safe automation. This role does not implicitly grant vendor activation, award, bank or payment approval; business publication requires the appropriate company policy authority.

**Requester:** own/department-authorised procurement requests and approved progress, no unrestricted bid prices. **Buyer:** company-scoped sourcing and published technical requirements, not sealed content. **Compliance Reviewer:** assigned applications/evidence, applicant-safe comments and internal notes. **Procurement Manager:** company policy and independent activation/award authority subject to actor separation.

**Opening Officer:** assigned stage-release command only with a second distinct confirmer; opening role alone does not grant every bid body. **Evaluator:** assigned tender/lot/criterion and released envelope only, valid conflict declaration required. **Contract Manager:** company/contract obligations and relevant vendor evidence. **Receiving Officer:** assigned goods/service acceptance. **Finance Reviewer:** claims, restricted bank verification and native financial review within company permissions. **Payment Approver:** independent native payment content approval. **Auditor:** company-scoped read-only released records/audit; no bank secrets or sealed commercial envelopes by default. **System Manager:** technical setup, not implicit business authority to approve or open.

Roles are additive only where resource predicates also pass. Internal user Company permissions, assignment, field sensitivity, envelope stage and purpose all apply. Vendor users can belong to several organisations through explicit memberships; the selected organisation is verified server-side every request. A URL parameter is never authority.

## Enforcement surfaces

Implement shared predicate functions in list/query permission hooks, `has_permission`, service commands, controllers, files, print, search/link queries, reports, dashboard cards, exports, websocket subscriptions and alternate native Supplier routes. Child records inherit the stricter parent/evidence policy. Explicit sharing grants cannot override envelope stage or give a reviewer bank rights.

Public routes return allowlisted fields with generic Not found responses for inaccessible records. No counts, filenames, exception messages or download redirect leaks. Private pages use no-store/cache controls and no CDN/shared HTML cache. Realtime emits authorised user/document invalidation IDs, never envelopes, scores, evidence or bank content into site-wide rooms. Revalidate after reassignment, membership revocation or company switch.

## Upload and retrieval

Use authenticated upload intents bound to actor, organisation, company, purpose, parent revision and purpose-specific classification. The [data model](DATA_MODEL.md#configuration-requirements-and-review) defines which company, organisation or verified claimant scope is required; a registration claimant does not need membership in an organisation that does not yet exist. Limits are owned by [product defaults](PRODUCT_REQUIREMENTS.md). Require MIME/magic-byte validation, sanitised names, quotas, rate limits and checksum; reject active HTML/SVG, executable/archived/macro content. Every uploaded input, including administrative CSV, enters private quarantine and must pass a configured malware scanner before parsing/attachment to a submission. Administrative imports use their separate typed parser and actor/scope rules; they do not weaken vendor upload restrictions.

Scanner unavailability leaves Pending scan; no reviewer or public download, no deadline backdating and no “clean” assumption. Unclaimed upload intents expire after 24 hours; cleanup respects referenced submissions and legal holds. Malware is isolated with a security event and applicant-safe failure. Store raw bytes outside public web paths; prevent thumbnails/OCR/search indexing of sealed content.

Standard File ownership alone is insufficient. Implement and test a supported File permission/download gate against the parent classification and stage, or use an owned protected storage handler if the framework cannot express it. No sealed filename/path is rendered in generic attachments. Authorised download is streamed after a fresh permission check with no-store and content-disposition attachment. Avoid reusable storage URLs; if deployment requires signed URLs, short expiry alone cannot satisfy immediate membership revocation and the proxy must reauthorise.

## Sealed-content threat model

Technical and commercial payloads are separately permissioned, not merely hidden fields in the same document. No prices in standard Version records, search indexes, logs, exception traces, approval comments, email, notification payloads or bulk exports. Generic create/read/update permissions on envelope payload DocTypes are denied to ordinary roles. Use restricted services for vendor-authorised draft read/write and assigned post-opening projections.

Active Owners and Contributors may prepare/read both envelopes of their own organisation’s bids, including commercial drafts. Only an Owner or Bid Submitter may final-submit. Billing controls invoice/claim access and does not independently authorise a non-member to view bids; buyers/evaluators cannot read unreleased envelopes. Opening gates technical access after close and commercial access after technical qualification. Disqualified envelopes remain sealed in ordinary paths. Trusted DB/OS/backup/deployment administrators are outside application-level sealing; audit their access and segregate duties. Do not claim tamper-proof or administrator-proof storage.

## Audit, secrets and business segregation

Append-only audit events record actor, membership/company, action, resource/revision, decision reason, time and correlation ID; avoid raw evidence/price/secret payloads. Business history uses immutable revisions, not editable comment trails. Record rejected privilege attempts separately with redaction. Protect tax PINs and bank secrets in restricted encrypted fields/storage; never copy secrets into ordinary JSON snapshots or hashes vulnerable to low-entropy guessing.

Reassignment and emergency technical access require recorded scope/reason and audit, cannot self-approve sensitive business actions and must not enable a generic “ignore permissions” route. Export manifests include initiating actor, scope, selected fields and audit reference. CSV escapes formula-like cells. Large outputs are private operations with permissions rechecked at generation and download.

## Retention, holds and requests

Before Live, configure purpose-specific retention for identity, applications, bid envelopes, contracts, financial claims, notices, audit and temporary uploads; approve the policy with named owners. Legal holds override cleanup. Preview deletion counts and dependencies; do not cascade-delete submitted financial history. Personal access/erasure requests verify identity and authority, distinguish organisation from individual data and record why retained evidence remains.

Membership revocation stops future access immediately but preserves authored business history. Consent withdrawal stops optional matching alerts, not required tender addenda or contract notices. Use minimal email content and authenticated portal links. Data residency/storage/backups and restore-key recovery are explicit deployment decisions recorded before production qualification.
