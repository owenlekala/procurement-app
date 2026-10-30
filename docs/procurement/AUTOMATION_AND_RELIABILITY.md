# Automation, notifications and recovery

Owner: PROC-R14, PROC-R26, PROC-R29. Use the [data model](DATA_MODEL.md) for storage and [API contracts](API_CONTRACTS.md) for command interfaces.

## Native rule editor

Use a standard Automation Rule form with trigger selector, ordered condition/action rows, run-as principal, simulation and publish actions. Versions are immutable after publication. An existing run keeps its published version; retirement stops new runs, while an explicit cancellation handles old waiting runs. There is no arbitrary Python/JavaScript/SQL, external workflow engine or recursive rule graph.

Triggers: application submitted/correction requested/stage overdue/approved; evidence expiring/expired; bank change requested; tender published/addendum/closing soon/closed; evaluation assigned/overdue; award offered/accepted/declined; fulfilment overdue/submitted; claim exception; contract expiring; native order/receipt/invoice/payment state changed. Source events are deduplicated by source identity/revision/action. Timer events use a unique target/version/due-time key and check current state before effect.

Conditions use allowlisted company, category, work type, region, state, amount band, due-time and assignment predicates. Maximum 50 steps, five nested condition levels; no backward targets or cycles. Actions: create/reassign a review task within authorised pools, send approved portal/email template, schedule bounded wait, add an internal reminder, propose a compliance hold, and request reconciliation. Sensitive business approval, bid opening, score editing, bank activation, award approval, financial posting and payment execution are never automation actions. Compliance hold effects remain governed by live expiry policy, not an AI/rule approval.

Simulation uses synthetic/authorised source snapshots, displays matched/excluded reasons and proposed recipients, and makes no production writes or sends. Run-as is an explicit scoped service principal with least privilege; retain initiating actor and policy context. Re-evaluate authority and current source state on each resumed step.

## Notification catalogue

**Essential workflow:** account/membership messages; application receipt, corrections and decisions; expiry affecting an existing approval; invitations to explicitly invited tenders; addenda/cancellation for participants; submission receipts; evaluator assignments; award/complaint outcomes; contract, delivery and invoice updates. Portal delivery persists even if email fails. Business users cannot unsubscribe from notices necessary for their active participation; they can revoke their membership through an orderly transfer process.

**Optional opportunity alerts:** matching public jobs and digests. Require active membership, approved target-company/category eligibility and a current subscription at worker dispatch, not just initial selection. Withdrawing a subscription immediately suppresses queued optional alerts. Required addenda still reach relevant participants even if compliance later expires or subscriptions are disabled.

Templates contain minimal safe summaries and authenticated links; no bank/tax secrets, bid prices, reviewer-private notes or attachments. Record template version, language fallback and purpose. Default portal/email immediate delivery for essential notices; optional job alerts support immediate or daily digest at 09:00 company time. A tender closing before digest time remains available in the portal; digest scheduling must not delay essential invitations/addenda.

## Durable execution

Persist Event, Run, Notification and Outbox rows in the originating transaction. Enqueue only after commit. Recovery scans due persisted records in indexed batches (initial 100) and safely re-enqueues missing RQ work. Do not rely on Redis as the only state store. Unique source keys, run/version keys and notification purpose/recipient/channel keys prevent duplicate logical effects.

Workers claim a row in a short transaction using a fencing lease token and 60-second initial lease; perform external I/O outside database locks. Heartbeat long operations; updates require the current lease token so a stale worker cannot overwrite a newer claim. Expired pre-I/O claims can be reclaimed. Before mail I/O persist Submitting; a crash after that boundary may mean mail was accepted and becomes Unknown, not automatically Pending.

Database tasks and native record mappings can be retried idempotently. Mail retries only proven not accepted failures, with at most five attempts total: the initial attempt and four proven-safe retries after 1, 5, 15 and 60 minutes. Use an adapter/provider that classifies acceptance; plain SMTP acceptance means accepted by the next mail server, not delivered to the person. Network timeout after possible acceptance is Unknown. Operator disposition records acceptance evidence, proven non-acceptance or an unresolved outcome; only proven non-acceptance permits ordinary retry. If the business authorises a potentially duplicate replacement notice, create a distinct audited replacement acknowledging that risk and preserve the original Unknown attempt. Never promise exactly-once external delivery.

Portal notifications are deduplicated and durable, with independent read state. Email bounce/rejection records update delivery diagnostics and create a contact-correction task for essential notices. No absence of email read/delivery evidence changes a bid receipt or extends a deadline automatically.

## Scheduled controls and incident behaviour

Expiry/closing/overdue scans run at least each minute under healthy scheduler conditions. Commands enforce deadlines/evidence expiry live even during an outage. Scheduled “closed” indicators are projections, never submission authority. Durably schedule waits with due_at and recheck cancellation/version/current state on wake.

Readiness switches separately control publication, submissions and outbound notifications. A submission outage is visible to vendors and alerts procurement; no offline/backdated submission endpoint. An independently authorised tender extension/addendum before close or cancellation/reissue after close is the recovery route. If a switch closes submissions while a command is in flight, serialise it with the shared submission gate.

Metrics include oldest pending event/outbox/scan, lease expiry, Unknown mail, failed essential notice, overdue task, scheduler/worker heartbeat and policy readiness. Operator views expose safe context, next action and audit, with no envelope content. Reprocessing must not replay historical approvals or send obsolete tender alerts after cancellation.
