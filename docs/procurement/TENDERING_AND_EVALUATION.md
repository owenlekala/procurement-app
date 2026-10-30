# Tendering, evaluation and award

Owners: PROC-R13–PROC-R19. Fields: [data model](DATA_MODEL.md); commands: [API](API_CONTRACTS.md); authority: [policy](PROCUREMENT_POLICY.md).

## Tender definition and publication

Create from an approved procurement request; record one buying company, title, scope, categories/coverage, work type, bidding currency, lots/line allocations, minimum responses, eligibility, requirement versions, price schedule, milestones, terms, briefing rules, clarification cutoff, closing instant, evaluation criteria/weights and panel/opening assignments. Publication mode is Public or Invitation only. Public payloads exclude internal estimates/budgets, panel identities, vendor lists and confidential attachments.

Publish only after authority approval, valid company setup and notification/storage readiness. Require clarification cutoff < close, all mandatory briefings before close, positive lot quantities/limits, published requirements, allocated panel, finite scoring scales and weights summing to 100 within each published scoring stage. The combined technical/price weights also sum to 100. The technical pass threshold and any per-criterion gate are fixed before publication.

The published version freezes source terms and hashes; ordinary edits cannot change it. Public discovery is available to guests; downloading explicitly public tender documents is allowed through a published-file projection. Vendor compliance and bid files are never public. An unapproved vendor sees registration guidance and time remaining, not a promise that onboarding will finish before close. An invitation does not confer approval.

## Matching, briefing, clarifications and addenda

Matching requires company Active approval, intersecting required category, coverage/work type and no relevant suspension. A tender may explicitly require all categories; store that published choice. For job alerts also require a valid recipient membership and optional subscription; invited notices and essential addenda have their own purpose basis. Save explainable match/exclusion reasons and deduplicate by vendor/version/purpose/channel.

Invited tenders permit only explicitly invited organisations. Public tenders permit all otherwise eligible organisations. A revoked invitation prevents new submission, preserving received versions and a recorded reason. Cancellation or an essential addendum is still notified to existing participants.

Clarification questions are private to the asking vendor and buyer until answered. General answers are sanitised and published to all participants without the asker's identity or commercial content. Buyer must request redaction/resubmission if a vendor puts a price in technical Q&A; restricted review evidence preserves the incident. Private account-specific answers cannot modify tender terms.

Material scope, eligibility, schedule or pricing changes create an independently approved addendum and new published version. Criteria/currency/lot structure changes after any submission require cancellation/reissue; do not introduce new scoring rules into received bids. Other permitted changes require deadline-impact review and enough configured response time. Addenda after close require re-tendering, not silent reopening.

Participants receive mandatory notices and must acknowledge the current material addenda before final submission. A previously submitted bid becomes Needs acknowledgement; the vendor may use `reaffirm_bid` to create a new bid version reusing unchanged envelope content, or submit a replacement, before the revised close. Acknowledging an addendum alone never changes a frozen bid’s tender-version binding. Reaffirmation uses the same live eligibility, current requirements, clean evidence, locking and deadline checks as submission, records the new tender version and receipt, and atomically supersedes the previous version only on success. Unacknowledged material changes at close put that bid into Nonresponsive review with an explicit outcome. Briefing attendance is recorded by an authorised officer with evidence; if published as mandatory, enforce it at submission.

## Bid preparation and atomic submission

One bid head per tender/vendor holds metadata and immutable bid versions. A vendor contributor prepares drafts; an organisation Owner or explicitly delegated Bid Submitter submits. Technical answers/files and commercial prices/files use different storage records and permissions. Technical upload instructions prohibit price content; manual screening can flag accidental disclosure without silently editing the bid.

A submission command locks the tender gate and vendor bid head, checks current server time strictly before `closes_at`, current tender/addenda version, membership, company/category approval, required evidence, briefing and clean uploads. At exactly the closing instant the command fails Closed. A late scheduler cannot reopen the gate. The transaction creates both envelope snapshots, hashes and receipt; either all commit or no bid exists.

Receipt contains opaque bid/version ID, submitted time, tender version and content hash, not prices. Retry with the same idempotency key returns the same receipt. On network uncertainty, query the receipt instead of asking the user to submit blindly.

A revision is a new complete version; it atomically supersedes the previous eligible version only when successfully submitted. Failed replacements leave the previous submission effective. Withdrawal before close records a terminal decision for that version and permits a new complete submission before close. No vendor replacement/withdrawal after close; post-close requests are audited communications for committee disposition. The effective bid is the latest successfully submitted, non-withdrawn version satisfying addendum requirements at close.

## Opening and sealing boundary

After close, an assigned Opening Officer proposes technical opening and a distinct authorised officer confirms it; both have valid conflict declarations. Lock the tender, record the accepted version manifest/hash and freeze receipt inclusion. Only technical envelopes become available to assigned compliance/evaluation users. Invitation-only participant lists remain restricted.

Commercial opening is a separate two-actor command after required technical decisions/moderation are final. Release only technically qualified effective bids; disqualified commercial envelopes stay sealed through ordinary application paths and are retained under policy. Staff cannot use generic DocType APIs, File URLs, reports, print or exports to bypass the stage gate.

This is application-level sealing against ordinary users. Database, operating-system, backup and privileged deployment administrators are trusted infrastructure actors and can technically access stored content; do not claim cryptographic protection from them. Access is logged and operational separation is required. A future stronger key-custody design needs a separate ADR.

## Technical scoring and moderation

Each evaluator declares conflicts before assignment acceptance, scores only assigned criteria/lots, supplies evidence and reasons, and submits an immutable score sheet. Recusal revokes access and reassigns work. Evaluators cannot see others' draft or submitted scores until their own submission and moderation stage. No role can edit someone else's submitted scores; correction creates a superseding sheet with reason and reapproval.

Normalise each criterion to 0–100 using its published maximum, then calculate weighted technical total. The moderated criterion result is the arithmetic mean of valid final evaluator scores; at least the configured panel quorum must contribute. Missing scores are Incomplete, never zero. Published minimum criterion gates apply before weighted pass threshold. Ties and large score variance are flagged; moderation may request independently resubmitted sheets but cannot invent an undocumented score override.

## Commercial comparison and recommendation

Require all bid prices in the published currency and structured price schedule, with quantities/UOM/taxes, discounts, validity, delivery and qualifications. Commercial documents support the schedule but cannot replace missing mandatory lines. Alternatives must be explicitly permitted; v1 alternative offers are separate labelled schedules and only the compliant base offer is ranked automatically.

Compare tax-inclusive evaluated totals using the published quantity/option basis. Price score is `100 * lowest_valid_positive_total / bidder_total`; zero/negative or incomplete offers require disposition before ranking. Apply published technical and price weights to normalised totals. Lead time/risk may be included as published technical criteria; do not invent preference or B-BBEE scoring. Evaluate monetary totals at native currency precision; compute scores with decimal arithmetic and round only final ranking scores to four decimal places using half-up rounding. If combined scores tie at that score precision, higher technical score ranks first; a remaining tie requires recorded committee decision and independent award approval, never a random winner.

A highest score is a recommendation, not an automatic award. Qualifications, arithmetic correction or negotiated changes require an explicit vendor-confirmed revised commercial record, equal-treatment policy and renewed recommendation; sealed source evidence is preserved. Material scope/criteria changes require re-tendering. An expired commercial validity instant blocks recommendation approval and award offer; an award response deadline cannot extend beyond it without explicit vendor consent. An award accepted within validity and an activated signed contract then use the agreed contract validity/terms for subsequent orders rather than repeatedly applying the original bid expiry. Request an explicit vendor validity extension or permitted arithmetic/qualification clarification as a separate `PROC Offer Revision`; vendor consent and independent review precede a new summary/recommendation. Never edit the sealed offer, infer consent from silence or unilaterally extend validity. An extension changes validity only; other changes must satisfy the published equal-treatment policy or trigger re-sourcing.

## Award, acceptance and complaints

An award proposal records tender/lot, selected bid version, quantity/value allocation, conditions, justification, approvals, compliance/budget checks and contract basis. Aggregate split allocations cannot exceed approved lot quantities/value ceilings; reject over-allocation under concurrent approvals. A partial/no award is a recorded outcome. Independent award approver cannot be the proposer or an evaluator who authored the recommendation.

Conditional awards have explicit conditions, owner and deadline; no PO is generated until fulfilled and independently cleared. Vendor acceptance has a deadline, supports decline and preserves notices. A missed deadline escalates for extension/withdrawal; never silently awards the runner-up. Any alternate selection requires a new recommendation and independent approval.

Notify successful/unsuccessful vendors privately with permitted feedback. Public results are a separately approved publication with no bid prices unless the published policy explicitly allows release. Complaint/appeal submission opens a case with response owner and configured window. A timely unresolved award complaint puts downstream order creation on hold; independent resolution records uphold, correction or withdrawal. No application action can erase already submitted accounting records.

Cancellation requires a reason, independent authority and essential participant notices; preserve all versions. Re-tendering creates a new identifier with a link to the cancelled/failed tender and new approvals/deadlines. No-bid and insufficient-response cases use [sourcing exception policy](PROCUREMENT_POLICY.md).
