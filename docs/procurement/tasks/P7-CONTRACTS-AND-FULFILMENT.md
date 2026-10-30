# P7 — Contracts, execution and financial handoff

[Completion contract](README.md) · [Phase gates](../IMPLEMENTATION_PLAN.md).

## PROC-P7-001

- [ ] **Implement contract control, obligations and variations**

**Depends on:** `PROC-P6-004`

**Requirements:** PROC-R20, PROC-R21. **Acceptance:** [PROC-A20](../TESTING_AND_ACCEPTANCE.md#proc-a20), [PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21).

**Read first:** [Contracts And Fulfilment](../CONTRACTS_AND_FULFILMENT.md) · [Contracts](../pages/CONTRACTS.md).

**Implementation and boundaries:** Link native Contract/Blanket Order with company/award controls, signed evidence, milestones, guarantees, framework balances, cumulative independent variations and termination.

**Failure cases and verification:** Test missing signatures/guarantees, expired frameworks, over-ceiling concurrent drafts and unsafe closed states.

**Completion evidence:** Contract/variation/call-off integration and UI evidence.

## PROC-P7-002

- [ ] **Implement idempotent orders and goods/service acceptance**

**Depends on:** `PROC-P7-001`

**Requirements:** PROC-R21, PROC-R22. **Acceptance:** [PROC-A21](../TESTING_AND_ACCEPTANCE.md#proc-a21), [PROC-A22](../TESTING_AND_ACCEPTANCE.md#proc-a22).

**Read first:** [Erpnext Integration](../ERPNext_INTEGRATION.md) · [Orders And Fulfilment](../pages/ORDERS_AND_FULFILMENT.md).

**Implementation and boundaries:** Map opened approved offers to native quotation/order drafts; enforce current authority/compliance/budget. Complete vendor PO acknowledgements/change responses with internal amendment review, and dispatch/work evidence and internal partial receipt/inspection/service acceptance/returns.

**Failure cases and verification:** Crash around mappings, race allocations, exceed quantities, attempt vendor stock posting and reverse invoiced acceptance.

**Completion evidence:** Native order/receipt/amendment and service/works acceptance fixtures.

## PROC-P7-003

- [ ] **Implement claims, invoice matching and credit review**

**Depends on:** `PROC-P7-002`

**Requirements:** PROC-R23, PROC-R22, PROC-R09. **Acceptance:** [PROC-A23](../TESTING_AND_ACCEPTANCE.md#proc-a23), [PROC-A22](../TESTING_AND_ACCEPTANCE.md#proc-a22), [PROC-A09](../TESTING_AND_ACCEPTANCE.md#proc-a09).

**Read first:** [Contracts And Fulfilment](../CONTRACTS_AND_FULFILMENT.md) · [Invoice Claims](../pages/INVOICE_CLAIMS.md).

**Implementation and boundaries:** Complete structured claims, native/portal number registry, source matching/tolerances, independent exceptions, disputes/corrections/credits and one mapped invoice draft per approved revision.

**Failure cases and verification:** Test concurrent duplicate/overclaims, wrong company/currency, unaccepted work, lost mapping response and native financial rejection.

**Completion evidence:** Goods/service invoice/credit fixtures with draft/post boundary and billing portal screenshots.

## PROC-P7-004

- [ ] **Qualify financial schedules, payment visibility and closeout**

**Depends on:** `PROC-P7-003`

**Requirements:** PROC-R24, PROC-R25, PROC-R20, PROC-R29. **Acceptance:** [PROC-A24](../TESTING_AND_ACCEPTANCE.md#proc-a24), [PROC-A25](../TESTING_AND_ACCEPTANCE.md#proc-a25), [PROC-A20](../TESTING_AND_ACCEPTANCE.md#proc-a20), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).

**Read first:** [Contracts And Fulfilment](../CONTRACTS_AND_FULFILMENT.md) · [Erpnext Integration](../ERPNext_INTEGRATION.md).

**Implementation and boundaries:** Qualify each enabled advance/retention/recovery template with native ledger examples; implement reversal-aware payment projection, independent payment gates, scorecard evidence and operational/financial closeout.

**Failure cases and verification:** Disable unsupported templates; test bank changes, stale payment approval, credits/reversals, open retention/disputes and offboarding access.

**Completion evidence:** Finance-reviewed ledger/reconciliation cases, performance/closeout and portal settlement-state evidence.
