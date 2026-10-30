# Awards

Native destination: `PROC Award`. Audience: Procurement recommenders, independent award approvers and complaint reviewers.

[Screen contract](README.md) · [Policy owner](../TENDERING_AND_EVALUATION.md).

## Components and layout

Native List/Form with decision summary, lot allocation child table, eligibility/budget checks, conditions, vendor response and complaint history. A review dialog presents the exact allocation/hash.

## Displayed fields and context

Route-specific approved request/offer source, formal technical/commercial summary where applicable, value/currency, quantities, exceptions, current compliance, conditions/deadline, acceptance and unresolved holds.

## Actions by state

Propose; independently approve/return/reject; offer; record vendor response; clear independently verified conditions; resolve complaint; withdraw or create contract after all gates.

## Permission boundaries

Award approver cannot be proposer or recommendation author. Supplier response is restricted to authorised membership; complaint reviewer must be independent.

## Validation, loading and exception states

Lock aggregate allocations, enforce authority and budget, and stop contract/order handoff on conditions or complaint hold. Decline/timeout triggers a new decision, never automatic runner-up award.

## Responsive and keyboard behaviour

Allocation rows summarise by lot with detail links; confirmation identifies vendor/company/amount and any conditions.

## Acceptance links

[PROC-A18](../TESTING_AND_ACCEPTANCE.md#proc-a18), [PROC-A19](../TESTING_AND_ACCEPTANCE.md#proc-a19), [PROC-A20](../TESTING_AND_ACCEPTANCE.md#proc-a20), [PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21).
