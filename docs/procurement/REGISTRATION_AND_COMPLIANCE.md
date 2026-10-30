# Registration and continuous compliance

Owners: PROC-R04–PROC-R10. Field definitions: [data model](DATA_MODEL.md); access: [permissions](PERMISSIONS_AND_PRIVACY.md); commands: [API](API_CONTRACTS.md). This file owns registration policy, not page layout.

## Requirement builder

A Procurement Administrator creates a draft `PROC Requirement Pack` for a buying company and purpose (Registration, Renewal or Tender), with optional country, category and work-type selectors. Publishing validates references, builds an immutable numbered version and hash, and records effective dates. Company onboarding requires an active company-wide base pack. Matching category/work-type/country packs add requirements; they cannot weaken base requirements. Tender packs add submission conditions for that tender only.

Resolve all applicable versions when an application starts; require the applicant to select categories, work types and coverage first. Use stable requirement keys. If packs repeat a key, type/options/verification must agree and the stricter requiredness/expiry bound wins; incompatible definitions block publication. Show the resolved checklist and its version list before starting the application. Category changes recalculate only an editable draft; submitted revisions retain their original resolution.

A requirement defines label, translated help, section, field type, allowed selections, conditional expression, validation, applicant visibility, sensitivity, evidence instructions, expiry requirement, verification method and review stage. Types are text, long text, date, integer, decimal, boolean declaration, select, multiselect and attachment. Repeatable business data uses supported child tables with fixed column definitions; do not execute arbitrary JSON schema or dynamic Python.

Conditions support `all`/`any` groups of `equals`, `in`, `is_set` and numeric/date comparisons against earlier answer keys and context (company, country, category, work type). A depth limit of five and 50 clauses per version bounds evaluation. Reject cycles, unknown keys, incompatible comparisons, hidden-required traps and script/SQL input. The server uses the same published definition as the preview. A field cannot depend on a later field. Inactive answers stay in draft history but do not satisfy active requirements or appear in submitted snapshots unless applicable.

Document requirements specify allowed types, bounded size, required issue/expiry dates, verification checklist, restricted reviewer group, acceptance criterion and whether sharing is permitted. Files must be clean before submission. `expires_on` is interpreted through end-of-day in the buying company's configured timezone; live comparisons use the converted instant. No-expiry evidence requires an explicit permitted reason rather than an invented future date.

## Editable South African starter packs

Ship these as disabled sample definitions for an administrator to adapt, preview and publish. None is universally mandatory simply because it appears in a sample:

- **Legal identity:** legal/trading name, country, registration identifier and registration evidence; manual comparison of entity names/identifiers with the uploaded record and approved verification source.
- **Tax:** tax reference, restricted TCS PIN and manual verification result/time. A PIN upload does not itself establish a current compliant result. PINs use protected secret storage, not ordinary answer text.
- **VAT:** “Are you VAT registered?” declaration; require VAT reference/evidence only when Yes. Validate presentation and identity consistency without inventing a VAT-registration obligation.
- **B-BBEE:** administrator-selected certificate/declaration evidence type, issue/expiry details where appropriate, and manual reviewer checklist. No statutory preference formula is seeded into tender scoring.
- **Banking:** separate restricted account-maintenance flow with proof, masked account display and independent trusted-contact verification; never expose full banking answers to general reviewers.
- **Goods categories:** product/service capabilities, delivery regions, lead times and any category-specific quality evidence the company chooses to require.
- **Services categories:** experience/references, professional credentials and relevant insurance with expiry only where the selected category/policy requires them.
- **Works categories:** relevant contractor credentials, insurance, safety-plan evidence and site-specific obligations configured by the buying company. Tender-specific additions remain in the published tender pack.

Provide a synthetic preview demonstrating conditional VAT evidence, category-dependent insurance, a rejected document correction, an expiring requirement, and differing checklists for two buying companies. Each published pack names its accountable policy owner and verification instructions.

## Approval chains and waivers

Configure ordered stages with reviewer role, minimum distinct decisions, SLA in calendar hours, escalation recipient, evidence checklist and a final approver. A reviewer cannot approve their own uploaded/internal-created evidence or self-approve activation, bank verification or awards. No assigned reviewer means blocked routing, not automatic approval. Reassignment/delegation is explicit, time-bounded and audited; self-approval and conflicts remain prohibited.

A waiver names one requirement, application/company/category, reason, approving actor and expiry. It never bypasses identity ownership, file scanning, independent final approval or tender sealing. Waiver proposal and approval are separate actions. Eligibility evaluates valid waivers explicitly and displays them to award approvers. No blanket permanent exemptions.

## Registration and progress

Verify the user's email through Frappe's supported account flow before accepting uploads. Do not build password storage. Create an organisation claim with country and registration identifier. Canonicalise identifiers per country without stripping meaningful characters; exact known identity conflicts go to duplicate review. A claimant cannot inspect the existing organisation or become its owner without verified evidence and independent internal adjudication.

The owner selects one or more buying companies, services/categories, work types and geographic coverage. Each selected company creates a separate application pinned to its resolved requirement versions. Shared profile basics are proposed centrally; company-sensitive responses remain in the company application. Present notice/terms versions and capture acceptance evidence. Job subscriptions are separate optional choices.

Drafts autosave explicitly with revision checks and last-saved time. Validation lists missing/invalid active requirements. Submission freezes answers, clean-file hashes, declarations, version hashes and timestamp. Submission cannot itself activate a Supplier. Review creates visible correction requests and separate confidential internal notes.

Progress is `completed applicable required items / applicable required items`, with optional items excluded; zero required items displays “No outstanding required items”. Answer completeness and document review status are shown separately. Never label 100% complete as approved. Display current review stage, elapsed/target time, next actor and corrections. No guaranteed approval date from an SLA.

Corrections create a new response revision. The prior submission stays immutable; only affected decisions reset unless a material identity/category change requires all stages. Rejection requires an applicant-safe reason; a new application references the rejected one. Withdrawal is allowed before activation and closes open tasks. Approved organisations edit profile proposals rather than rewriting approved snapshots.

## Evidence and verification

Reviewers record result (Accepted, Rejected or More information), reason, checked-at time, evidence revision, source/method and validity. An upload and a verification are distinct records. A tax PIN is a restricted secret, never ordinary text exposed in list/export. Manual SARS verification records the reviewer and observed result; do not automatically treat a document date as current tax compliance.

Sharing evidence across buying companies requires a vendor-authorised grant identifying the receiving company, evidence revision and purpose. The recipient still performs its own verification. Revocation stops new reuse; already relied-on evidence remains under the receiving company's recorded retention/hold policy with a visible revocation marker.

## Activation, expiry and remediation

After every stage succeeds, an independent approver activates company/category approval and creates or links the ERPNext Supplier in one transaction. Supplier identity is global; membership approval is local. Initial company-approval status is Unverified. Effective eligibility requires Active status, approved category, current required evidence/waivers, no company suspension and a non-disabled/non-frozen ERPNext Supplier with no relevant purchasing block.

Scheduled scans create renewal tasks and reminders at configured intervals (initial suggestion 30, 14 and 7 days). Missing policies block activation. Expiry immediately affects eligibility checks even if the scanner is late. Expired mandatory evidence puts the affected categories on Compliance Hold. It blocks new bids, awards and orders; historical bids, executed contracts and lawful invoice settlement remain visible. Suspend ongoing fulfilment only by an explicit authorised contract decision.

Renewal uses a new application pinned to the selected versions. Current approval remains effective until its evidence expires or a decision suspends it; renewal approval updates eligibility atomically. Suspension requires scope/reason and applicant-safe notification; reinstatement requires remediation and independent approval. Offboarding revokes future invitations/transaction eligibility and team access as appropriate while retaining required history.

## Requirement changes and profile changes

A new requirement version affects new applications after its effective date. For active vendors, publish a remediation campaign specifying affected company/categories, deadline, notices and whether a compliance hold applies at that deadline. Never silently rewrite existing approvals. Existing submitted applications remain pinned unless an administrator starts an explicit migration requiring applicant acknowledgement and renewed affected review.

Legal name, country, registration identifier and bank changes are material. A registration identifier change is a legal-identity review, not an unrestricted rename. Approved address/contact changes use a logged proposal and risk-based review; ownership changes always require the membership recovery process.

## Bank changes and legacy suppliers

Bank details use a restricted proposal with account fingerprint, masked display, proof and verification evidence. An independent finance verifier must use a trusted contact method not supplied solely by the change request. Keep the old verified account active until approval; freeze new payment preparation for the affected supplier/company while a change is under review. Never alter submitted financial documents silently. Finance must reapprove affected pending payment instructions after activation.

Import is a persisted preview/confirm/resume operation: validate company mapping, normalise identity, detect duplicates, explain conflicts, and map Supplier links. Imported organisations and company approvals start Unverified. Existing submitted financial documents remain intact. No bulk import creates live portal memberships, verified bank data or approved eligibility. Existing native Supplier portal access must be audited and explicitly reconciled before portal launch.
