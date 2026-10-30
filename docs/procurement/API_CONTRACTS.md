# Public application interfaces

Owner: PROC-R04–PROC-R27. These are future version-1 interfaces. Record fields belong to [data model](DATA_MODEL.md); state/eligibility rules to their policy owners. No endpoint is implemented by this handbook.

## Transport and common envelope

Company-owned commands require company context; organisation-owned commands require verified membership. Identity claims and invitation acceptance are scoped to the verified claimant/invited user before membership exists. Use a non-null server-derived `scope_key` (`company:<id>`, `organisation:<id>` or `global`) in command-receipt uniqueness, never a nullable company key or a client-selected authority scope. Replayed keys remain subject to current access checks and source uniqueness; pruning a receipt must not allow a repeated business effect.

Authenticated POST command facade: `/api/method/tag_procurement.api.commands.execute`; GET/POST query facade: `/api/method/tag_procurement.api.queries.execute`. Both use a fixed allowlist of names below and strict payload schemas, not caller-supplied Python methods/DocTypes/SQL. Schema version is `1`; reject unknown command/query names and unexpected fields. Frappe session authentication/CSRF is required for browser mutations; optional scoped integration tokens require the same actor/company permissions. No mutation is guest-whitelisted.

Example command body:

```json
{
  "schema_version": 1,
  "command": "submit_bid",
  "context": {"organisation": "VENDOR-DEMO", "company": "TAG Demo"},
  "resource_id": "BID-DEMO",
  "expected_revision": 4,
  "idempotency_key": "demo-request-001",
  "data": {"tender_version": 2, "acknowledged_addenda": ["ADD-DEMO"]}
}
```

Actor is always session-derived. Context is a requested scope that must be authorised, not trusted authority. Creation uses `expected_revision:0`; mutations to existing aggregates require current revision, with decision commands also providing the reviewed content hash. Idempotency keys are required for submissions, approvals, publication, opening, downstream record creation and external-work commands. The stored key includes actor/non-null scope key/command; payload mismatch returns Conflict, replay rechecks access before returning the same committed result. Save-draft commands also accept keys so a lost create response does not create another draft.

Successful Frappe JSON response wraps the application object in `message`:

```json
{"message":{"ok":true,"schema_version":1,"resource_id":"BID-DEMO","revision":5,"state":"Submitted","receipt_id":"RECEIPT-DEMO","operation_id":null}}
```

Use HTTP 200 for synchronous success and 202 for accepted persisted operations. Native auth/CSRF failures retain framework handling. Application failures return an `ok:false` application object with `error:{code,message,field_errors,correlation_id,retryable}` and suitable 400/403/404/409/413/422/429/503 status. Do not return success-state data on failure. The client normalises framework exception envelopes without exposing traces. Expected codes: Validation, PermissionDenied, NotFound, StaleRevision, PolicyNotConfigured, Ineligible, Closed, Duplicate, Conflict, ScanPending, Quarantined, BudgetStop, ApprovalRequired, StageNotReleased, CapacityExceeded and TemporarilyUnavailable. Retryable means the same idempotency key may be queried/retried safely, not permission to duplicate an uncertain external send.

Query arguments contain name, authorised context, allowed filters, sort, cursor and page_size (default 20, maximum 100). Use a stable `(modified,name)` or immutable source ordering with signed/validated scope-bound cursors. Escape search terms and allowlist fields; never accept SQL or arbitrary `get_all`. Counts use the same predicates. Detail queries return explicit DTO fields, not raw `as_dict()` from sensitive records.

## Identity, registration and review commands

- `claim_organisation`: proposed legal identity and country/identifier; returns claim ID and safe state without disclosing matches.
- `resolve_organisation_claim`: claim/reviewed hash, evidence and independent decision; returns organisation/membership or rejection.
- `invite_member`, `accept_invitation`, `change_member`, `revoke_member`, `transfer_ownership`: explicit organisation, target user/capabilities, token where relevant and reason. Verify inviter authority and last-owner invariant. Ownership recovery requires independently verified evidence.
- `start_application`: buying company, kind, categories, coverage and work types; returns application ID, resolved version manifest and initial revision.
- `save_application`: typed answer changes and owned clean/pending evidence IDs; returns revision/completeness. Cannot edit a submitted snapshot.
- `submit_application`: current draft/version hash, notice/declaration acknowledgements and evidence references; returns immutable submission receipt and review stage.
- `start_application_revision`: own returned/Needs correction submission and current revision; create an editable response revision with the affected review-reset manifest, preserving the prior receipt.
- `reassign_review_task`: task revision, authorised assignee/delegation and reason; no expansion of scope or self-review exception.
- `withdraw_application`: reason; closes pending tasks without deleting history.
- `record_review`: task/submission/evidence revision, outcome, verification method/source, safe reason and separate internal note; creates an immutable decision.
- `approve_vendor`: submission/decision-manifest hash; verifies all stages and independent actor, returns company/category approval and Supplier link atomically.
- `reject_application`, `suspend_vendor`, `reinstate_vendor`, `close_vendor`: explicit scope/reason/evidence; require appropriate independent authority and do not globally disable a shared Supplier.
- `publish_requirements`: draft definition hash/effective dates; returns immutable pack version or structured condition/conflict errors.
- `propose_waiver`, `decide_waiver`: exact requirement/scope, reason, expiry and evidence; separate proposer/decision actor.
- `start_remediation`: published version IDs, selection-preview hash, deadline and hold policy; returns operation ID. `confirm_application_migration` requires applicant acknowledgement and resets affected reviews.
- `grant_evidence_reuse`, `revoke_evidence_reuse`: evidence revision, receiving company and purpose; no transfer of verification.
- `request_bank_change`, `decide_bank_change`: protected account data/evidence, verification details and reviewed hash; return masked proposal and version, never echo full secrets.
- `preview_supplier_import`, `confirm_supplier_import`, `resolve_duplicate`: private input evidence, mapping and preview hash; return persisted operation/conflict references. Confirm never grants approval/membership. Import accepts only the administrative CSV format/limits in [product defaults](PRODUCT_REQUIREMENTS.md); it is not an ordinary vendor-evidence upload.

## Procurement, tender and bid commands

- `save_request`, `submit_request`, `decide_request`: typed demand lines/dimensions or reviewed hash/decision; return request state, approved sourcing route and actionable budget/authority reasons.
- `cancel_request`: current request revision, reason and downstream impact preview; approved/committed demand needs the relevant authority and native cancellation handling.
- `publish_company_policy`: validated complete bands/stages/config hash; no live default for missing limits.
- `propose_sourcing_exception`, `decide_sourcing_exception`: type, scope/value/expiry/evidence and independent decision.
- `save_tender`, `request_tender_approval`, `publish_tender`: terms, version/approval hash, assignments and schedule; return published version and safe public route.
- `invite_vendors`, `revoke_invitation`: selection preview/hash, organisations or explicit invitation/reason; return operation/recipient results, not unconditional sends.
- `ask_clarification`, `answer_clarification`: tender version and safe question/answer, visibility and evidence IDs. Shared answers require sanitised content.
- `publish_addendum`: proposed version/diff hash, independent approval, deadline review and notice purpose; preserves old version.
- `acknowledge_addendum`, `record_briefing`: target version/attendance evidence; store explicit vendor/officer actor.
- `start_bid`, `start_bid_revision`: tender/current version or own effective receipt; return the unique bid head and an editable draft, preserving any existing effective submission. A replacement copies permitted own source content into a new draft under revision checks.
- `save_bid_technical`, `save_bid_commercial`: owned draft head/revision, permitted answers or typed price lines and clean/pending evidence IDs. Responses expose only the caller's authorised envelope projection.
- `submit_bid`: draft revision, published tender version, declarations and current addenda acknowledgements. No client timestamp, price total or eligibility flag is authoritative. Return atomic receipt/version/hash or Closed/Ineligible/ScanPending without partial submission.
- `reaffirm_bid`: current own bid receipt, new tender version and acknowledged addenda; validate unchanged content against the new requirements through the submission gate and issue a new immutable receipt. Failure preserves the old version.
- `withdraw_bid`: effective version and reason before close; return withdrawal receipt. Replacement uses a new complete draft and `submit_bid`.
- `propose_opening`, `confirm_opening`: tender, stage, expected manifest hash and qualification revision for commercial stage; distinct authorised actors. Return opening ID and stage, never a bulk envelope payload.
- `declare_conflict`, `accept_evaluation_assignment`, `recuse_assignment`: assignment and declaration/reason; revoke access immediately on recusal.
- `save_score_sheet`, `submit_score_sheet`: assignment/bid version, criterion scores and evidence/reasons; submitted corrections create superseding revisions.
- `request_offer_revision`, `submit_offer_revision`, `decide_offer_revision`: original bid version/hash, permitted change type/diff or validity, vendor consent and independent disposition. Return a separate revision; renewed summary/award gates apply.
- `build_evaluation_summary`, `submit_recommendation`: source score manifest/hash, published comparison basis and rationale; derived totals are server calculated.
- `propose_award`, `decide_award`: sourcing route, approved request and route-specific tender/bid, RFQ/quotation or exception references, source-version hash, allocations/conditions and amount/budget basis; concurrent over-allocation fails atomically.
- `clear_award_conditions`, `extend_award_deadline`: condition evidence or proposed new response deadline, reviewed award hash and independent decision. Vendor is notified; neither command silently changes allocations or an expired offer’s validity.
- `publish_award_result`: approved result projection/hash and field allowlist; excludes private feedback, competitor documents and unpublished prices.
- `respond_award`: accept/decline and authorised vendor acknowledgement; conditions and deadline enforced.
- `submit_complaint`, `resolve_complaint`: grounds/evidence or independent resolution and hold disposition.
- `cancel_tender`, `withdraw_award`, `reissue_tender`: reason, impact preview and authority; no financial document deletion or silent deadline reopening.

## Contracts, execution, finance and operations commands

- `prepare_contract`, `record_signed_contract`, `activate_contract`: approved award references, obligations/milestones/terms, signed evidence and verified approval hash.
- `propose_variation`, `decide_variation`, `apply_variation`: scope/value/schedule diff and vendor acceptance; return controlled amendments and allocation effects.
- `create_quotation`, `create_purchase_order`, `create_call_off`: approved opened offer/award/control revision, permitted lines/quantities; return existing or newly mapped native draft ID. Native submission is separately authorised and guarded.
- `respond_purchase_order`: own native PO/revision and Acknowledge/Propose change response, proposed delivery/quantity details and reason; creates a reviewable response, not a native PO amendment. `decide_order_response` records internal disposition and maps an authorised amendment when required.
- `save_fulfilment`, `submit_fulfilment`: own PO/contract and dispatch/delivery/milestone evidence; no stock posting.
- `decide_fulfilment`, `reverse_acceptance`: quantities/value, evidence and reason; internal actor only, downstream impact reviewed.
- `save_invoice_claim`, `submit_invoice_claim`: structured invoice data, source line links and private evidence; returns duplicate/matching state.
- `decide_invoice_claim`, `create_purchase_invoice_draft`: reviewed claim hash, discrepancy exception if applicable; finance-only, idempotent native draft mapping.
- `request_credit`, `decide_credit`: original invoice/claim and proposed reason/lines; routes to native credit workflow.
- `approve_payment_content`: native payment revision/hash, verified bank revision and independent decision. No execute-payment command exists.
- `submit_performance_review`, `respond_performance_review`, `close_contract`, `terminate_contract`: evidence, outstanding-obligation preview and appropriate authority.
- `save_automation`, `simulate_automation`, `publish_automation`, `pause_automation`: validated allowlisted definition/hash. Simulation returns predicted actions with no business/outbound mutations.
- `set_job_subscription`, `mark_notifications_read`: own membership/preferences or owned notice cursor; cannot suppress essential notices.
- `request_export`, `start_reconciliation`, `preview_retention`, `execute_retention`, `cancel_operation`, `retry_operation`: authorised bounded manifest/preview hash. Retry is limited to proven safe states; Unknown mail has a separate operator disposition.
- `resolve_unknown_mail`: outbox/attempt revision, provider evidence, operator reason and disposition Accepted/Proven not accepted/Leave unresolved. Only proven non-acceptance permits ordinary retry; a possible duplicate send requires a distinct explicit authorised replacement, preserving the old Unknown attempt and risk acknowledgement.
- `set_readiness`: scoped switch, reviewed gate evidence and reason; privilege never substitutes for missing release evidence.

## Query DTOs and routes

Authenticated query names: `application_checklist`, `application_detail`, `application_progress`, `review_queue`, `vendor_detail`, `vendor_eligibility`, `bank_change_detail` (masked except restricted verifier), `request_detail`, `tender_detail`, `invitations`, `bid_draft`, `bid_receipt`, `evaluation_queue`, `released_envelope`, `score_sheet`, `award_detail`, `contract_detail`, `fulfilment_detail`, `claim_detail`, `payment_status`, `notifications`, `overview_metrics`, `report_rows`, `operation_status`, `audit_timeline`, `settings_readiness`, `matching_preview`, `evidence_status`, `command_receipt` and permission-scoped list variants.

`application_progress` returns required item totals/completed counts, review outcomes, stage, applicant-safe events and next action; not internal notes. `bid_receipt` returns own immutable submission references only. `released_envelope` authorises assignment, stage and bid version per request. `payment_status` returns posted amount/credits/allocations/outstanding/currency/due date/as-of, not GL rows or bank balance. `operation_status` returns state, bounded counts/errors and private result handle, never unfiltered imported rows. `command_receipt` looks up the authorised actor/scope/command/key and safe committed outcome so lost non-bid responses can be resolved without repeating effects.

Guest GET methods are only `tag_procurement.api.public.list_opportunities`, `get_opportunity` and `get_public_document`. Discovery uses allowlisted company/category/location/search filters and safe published content; public-document retrieval serves only evidence explicitly attached to a current public publication. Public identifier existence does not grant raw record access.

Portal routes under `/procurement` are owned website routes. Detail identifiers are opaque names resolved through predicates. Route/endpoint availability is not authorisation; the [portal index](portal/README.md) owns page routing.

## Upload, downloads and asynchronous results

`reserve_upload` command declares parent context/classification, filename, MIME and bytes; returns intent ID, expiry and owned upload URL. POST `/api/method/tag_procurement.api.files.upload` accepts multipart intent/file, checks session/CSRF, quotas and actual bytes, and stores private quarantine. Response gives evidence ID/scan state only. Hash/scan completion is server-owned; `evidence_status` is a scoped query. Pending files may remain in draft but cannot enter submitted envelopes/applications.

GET `/api/method/tag_procurement.api.files.download?evidence_id=...` streams after fresh parent/stage authorisation; use no-store, safe disposition and no raw storage URL. Sealed/public classification is not caller-selectable after attachment. Export download uses the same gate and current permissions.

Persisted operations return `operation_id` and safe polling query. Realtime is optional invalidation/progress; reload/poll can recover state without socket delivery. Network failure after submission uses idempotency receipt lookup. Polling must never trigger the underlying mutation.
