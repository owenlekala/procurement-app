# Submitted Bids and Results

Website route: `/procurement/bids`. Audience: Own organisation members with relevant bid access.

[Screen contract](README.md) · [Policy owner](../TENDERING_AND_EVALUATION.md).

## Components and layout

Paginated own-bid list and receipt detail, showing immutable version history, submitted/superseded/withdrawn states and safe result communications.

## Displayed fields and context

Receipt ID/time/hash, tender version, acknowledgement/compliance hold, effective submission, own permitted envelope copy, award feedback and complaint deadline.

## Actions by state

Before close: replace/withdraw through controlled commands or reaffirm under a new receipt after acknowledging changed terms. After close: inspect own receipt, respond to permitted offer-clarification/validity-extension requests, accept/decline own award or submit complaint within policy.

## Permission boundaries

No competitor bid, ranking detail or internal evaluator notes. Download still checks own membership/capability and evidence policy; former members lose access.

## Validation, loading and exception states

Distinguish received bid from qualified/awarded. Old versions remain historical. Closed or superseded receipts never offer an edit link that mutates the original.

## Responsive and keyboard behaviour

Receipt facts stack with copyable safe reference; version history is an ordered accessible list and next action precedes older events.

## Acceptance links

[PROC-A16](../TESTING_AND_ACCEPTANCE.md#proc-a16), [PROC-A18](../TESTING_AND_ACCEPTANCE.md#proc-a18), [PROC-A19](../TESTING_AND_ACCEPTANCE.md#proc-a19), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
