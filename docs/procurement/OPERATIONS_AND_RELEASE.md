# Operations, readiness and release

Owner: PROC-R29. Application implementation has not started. The release gates below are future qualification requirements, not claims of deployment.

## Runtime and ownership

Use an immutable image containing the inspected compatible apps and built assets, supported database/Redis, dedicated `procurement` and `procurement_io` workers, scheduler, realtime, private storage, malware scanner, configured SMTP/mail adapter and TLS. Pin image digests/runtime patch versions and record actual resource allocation. No developer mode, `bench start`, exposed database or public private-file bucket in production.

Before activation record named procurement, compliance, finance, security and platform owners; DNS/mail sender configuration; storage residency/access; secret rotation and backup-key custody; support escalation; maintenance/incident communications; and approved company policies. Business thresholds and legal retention periods require accountable configuration, not invented defaults.

## Readiness and staged activation

Independent switches control publication, bid submissions and outbound notifications, scoped by company. Default all Disabled. Pilot uses explicit company, staff/vendor users and tender allowlists; a guest public listing pilot uses invitation-only visibility unless separately authorised. Vendor registration may be piloted with synthetic/private invited users before public launch.

Readiness requires compatible runtime, successful migrations/build, native access-route isolation, clean scanner/storage health, healthy durable queues, configured authority/requirements/retention, valid sender, tested backup restore and required acceptance evidence. If readiness fails, show specific safe reasons and preserve draft/read-only access. Late detection of an outage does not change server deadline rules.

Live activation requires reviewed pilot evidence and named business/platform release decisions. Re-enabling after restore requires reconciliation and deliberate approval; source code or handbook approval alone does not authorise external notifications.

## Monitoring and initial service targets

Monitor worker/scheduler heartbeats, oldest pending event/outbox/scan, claim lease expiry, failed/Unknown mail, essential notice delivery failures, submission error rate, blocked policy, compliance hold backlog, native mapping conflicts, unauthorised access and private-storage errors. Initial alert thresholds: missing heartbeat for 3 minutes, oldest due event/essential outbox over 5 minutes, scan pending over 5 minutes, any Unknown submission/send, any confirmed sealed-content exposure. Route to named operators and tune only with recorded evidence.

Qualify initial synthetic load at 10,000 vendor organisations, two buying companies, 100 active tenders with 500 bid versions each, 100 concurrent portal sessions and 25 concurrent submissions near close. This is a test target, not a new business limit. On recorded 4-vCPU/8-GB application/worker staging allocation and separately recorded database/storage allocation, target p95 ordinary scoped queries <2 seconds and atomic bid submission <3 seconds excluding uploads/scanning. Require zero deadline bypasses, duplicate commitments or envelope leaks. Measure query counts, peak memory, queue lag and contention; change design or capacity rather than silently lowering targets.

## Incident runbooks

**Submission outage:** stop publication if needed, show service status, retain verified receipts and audit failed requests. No backdated manual bids. Procurement may publish an authorised extension/addendum before close; after close use cancellation/reissue. Publish essential notices through recovered channels and keep portal evidence.

**Scanner/storage outage:** quarantine remains closed; no clean override. Restore service, replay safe scan jobs, verify checksums and alert affected application/bid owners without promising deadline exceptions.

**Queue/email outage:** business submission commits survive. Recover indexed database work after service restoration. Reconcile possible mail acceptance before retrying Unknown items; portal notices remain authoritative internal records.

**Data exposure:** revoke affected access/links, suspend risky download/export surfaces, preserve audit, identify scope, notify organisational owners under their approved incident policy and rotate compromised credentials. Do not erase bid history to conceal the incident.

**Mapping/financial discrepancy:** stop affected new document generation, inspect native source/cancellation chains, reconcile mappings and escalate to finance. Never repair GL data by updating procurement projections alone.

## Upgrade, backup and restore

Back up DB, private files, app versions/assets and required encryption/secret recovery material. Restore into an isolated site with publication/submissions/outbound disabled and production credentials inaccessible. Reconcile open submissions, envelopes/hashes, evidence/scan state, pending events/outbox, bank versions, native mappings and accounting projections before enablement. Old Submitting mail becomes Unknown pending disposition; no automatic restored resend.

Migrate twice on populated staging, preserve site customisations and run affected native app regression tests. Destructive schema rollback is not assumed safe; prefer compatible forward fixes. If rollback needs restore, document the recovery point, intervening transactions and reconciliation. Initial backup objective is RPO ≤24 hours and tested RTO ≤4 hours; production owners must approve stricter targets when operational needs require them.

## Release gates

1. Reproducible runtime, app repository and test harness (P0).
2. Native UI/access isolation across every route, file and company (P1–P3).
3. Complete request→tender→bid→evaluation→award slices with deadline/concurrency/sealing evidence (P4–P6).
4. Contract→fulfilment→claim→accounting handoff, bank/payment controls and enabled financial templates qualified (P7).
5. Durable automation/report reconciliation and failure recovery (P8).
6. Full security/load/migration/restore tests, rendered UI/diagram review, linked documentation and authorised limited pilot (P9).

An unmet required gate keeps Live disabled. Record actual results in [progress](PROGRESS.md); document checks alone never satisfy application gates.
