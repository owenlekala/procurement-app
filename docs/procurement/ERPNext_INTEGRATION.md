# ERPNext integration and record ownership

Owners: PROC-R03, PROC-R10–PROC-R12, PROC-R20–PROC-R25. Inspect the [local source register](REFERENCES.md) before implementing adapters. Use supported app hooks and native mapping/controller methods; do not patch ERPNext core.

## Authoritative records

- **Vendor identity → Supplier:** one reviewed Supplier link per vendor organisation. Supplier is global; `PROC Company Approval` carries company/category status. Add owned custom link fields using idempotent fixtures/patches only where reverse navigation is needed.
- **Organisation people → User/Contact/Address:** explicit verified membership authorises the owned portal. Do not automatically populate Supplier `portal_users`; that can grant broader native transaction access than contributor permissions intend.
- **Request → Material Request:** create/link approved native purchase demand where supported; maintain line mapping. Services/works use approved non-stock Items; procurement scope remains in the owned request.
- **Budget → native Budget:** company/account/project/cost-centre validation remains native. Record pre-award observations, not a second financial ledger or claimed reservation.
- **Simplified sourcing → RFQ:** send flags disabled; owned outbox supplies invitations. Existing native RFQ routes must pass the same company/vendor approval guard for managed sourcing.
- **Opened commercial offer → Supplier Quotation:** map only after commercial opening and permitted review. Source envelope remains immutable. No quotation exists for a still-sealed commercial bid.
- **Award/contract → Purchase Order:** create a draft from the approved quotation/request, preserving quantities, taxes, UOM, schedule and source references. Draft creation is not financial commitment.
- **Signed terms → native Contract:** Supplier party plus owned company/award control record. Verify native party access; the native record lacks the complete company-specific procurement policy.
- **Framework → Purchasing Blanket Order:** use where native semantics fit, with owned locked call-off reservations and aggregate checks.
- **Goods → Purchase Receipt/Quality Inspection:** internal receiving records stock and inspection; portal dispatch advice is supporting evidence only.
- **Service/works → owned Service Acceptance:** link native non-stock receipt only where configured; preserve native invoicing requirements.
- **Claim → Purchase Invoice draft:** finance submits; matching/duplicates are rechecked at submit, not only at portal approval.
- **Payment → Payment Entry and allocations:** portal is read-only; native reversals update projections. No external payment provider is introduced.
- **Performance → Supplier Scorecard:** reuse qualified criteria/periods where compatible; owned review evidence supplies company/contract scope.

## Managed purchasing perimeter

A company setting declares the procurement-managed perimeter: initially all new purchasing transactions for enabled companies. Existing historical submitted transactions remain readable and are not silently revalidated or cancelled. New RFQ/quotation/PO/invoice/payment paths inside the perimeter must use procurement source authority or an approved direct/legacy-settlement exception.

Use `doc_events`, supported permission hooks and service-managed custom links to enforce Supplier company/category approval, bank/payment authority, source mapping, limits and managed field integrity on insert/save/submit/cancel/amend. Test native Desk, generic REST, Data Import, bulk updates, native portal routes and background integrations. A caller cannot escape by omitting procurement link fields: company perimeter determines enforcement.

Do not globally disable a Supplier when one company suspends it. Respect existing Supplier `disabled`, `is_frozen`, purchasing prevention and hold settings in addition to company approval. Invoice/payment holds differ from new-purchase eligibility; allow legitimate existing liability settlement only through documented finance authority. Native financial Stop validation always wins.

Verified bank-account approval is company-specific even when the native Bank Account is Supplier-linked. Do not automatically change the Supplier's global default account from a single company's proposal. Payment preparation selects an account whose current verification is valid for that company; explicit cross-company verification is required before another entity uses it. Native defaults never override this gate.

Audit existing Supplier portal users before enabling the owned portal. Do not remove unrelated app access blindly. For procurement-managed records enforce owned membership/company filters even when a native Supplier role would ordinarily reveal all Supplier documents; if hooks cannot enforce equivalent scope, block that alternate route for managed documents and use owned DTO pages. This is a P1/P3 release gate, not a documented assumption of safety.

## Mapping, idempotency and reconciliation

`PROC Source Mapping` uniquely binds source type/id/revision/action to native doctype/name and relevant line keys. Same-site creation and mapping commit together. On retry return the existing authorised draft instead of creating another. If an operator deleted/cancelled the native draft, require an explicit replacement action with reason/new mapping generation.

Never rebuild taxes or ledger amounts in browser code. Use native document calculations, precision and configured templates. Validate company consistency on every linked Company, Project, Cost Center, Warehouse, Account, Supplier and Item mapping. Source quantity/value consumption includes active drafts/reservations and submitted downstream documents, with cancellation/amendment reconciliation.

Source hooks write small durable events in the native transaction, enqueue after commit and roll back with source failure. Reconciliation recalculates projections from authoritative records, identifies missing/broken mappings and creates operator tasks; it does not silently post or cancel financial documents.

## Cancellation and compatibility

Cancellation requests identify affected orders, receipts, invoices, payments and claims; native dependency rules decide allowable cancellations. Preserve cancelled mappings and amendment chains. After native cancellation, source allocations reopen only after the reconciliation transaction confirms the authoritative result. Returning a receipt/crediting an invoice is not equivalent to deleting its history.

Qualify install with only Frappe/ERPNext, then with optional installed neighbours. Migrate twice and verify fixtures/custom fields do not overwrite site customisations. Any change requiring a core edit or incompatible native financial behaviour needs an ADR and explicit updated scope before implementation.
