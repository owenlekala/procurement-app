# ADR-003: Sealed bids and durable work

Status: Accepted. Date: 27 October 2026. Related: PROC-R16–PROC-R19, PROC-R26, PROC-R28.

## Decision

Formal tenders use separate immutable technical and commercial payloads with stage-gated queries/downloads. Two distinct authorised officers release technical material after close and commercial material only after technical qualification. Generic records, files, exports, search and notifications cannot bypass release. Map to ordinary Supplier Quotations only after commercial opening.

Use application-level sealing with trusted infrastructure administrators explicitly outside its protection. Do not claim encrypted key custody against DB/OS/backup administrators. A stronger model requires a later decision and implementation.

## Alternatives and consequences

Hidden price fields or ordinary RFQ attachments leak through alternate APIs and files. A Redis-only queue loses committed business work after transport failure. Persist events/runs/outbox before enqueue; recover indexed database work with fenced claims. Enforce deadlines in submission transactions, not scheduler UI state. Record uncertain external mail acceptance as Unknown and reconcile before retrying. Preserve source versions and hashes without claiming tamper-proof infrastructure.
