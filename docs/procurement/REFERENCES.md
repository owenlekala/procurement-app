# Source and reference register

Reviewed 27 October 2026. Local source is the implementation baseline; official documentation supplies conceptual guidance and must not override the inspected fork's behaviour. Future app paths elsewhere in this handbook are proposed, not evidence of implemented files.

## Inspected local sources

- [Frappe version](../../../frappe/frappe/__init__.py), [manifest](../../../frappe/pyproject.toml), [Node manifest](../../../frappe/package.json).
- [ERPNext version](../../../erpnext/erpnext/__init__.py), [dependency manifest](../../../erpnext/pyproject.toml).
- [Buying navigation](../../../erpnext/erpnext/workspace_sidebar/buying.json), [Desktop Icon](../../../erpnext/erpnext/desktop_icon/buying.json), [workspace](../../../erpnext/erpnext/buying/workspace/buying/buying.json).
- [Supplier schema](../../../erpnext/erpnext/buying/doctype/supplier/supplier.json), [controller](../../../erpnext/erpnext/buying/doctype/supplier/supplier.py): existing companies, portal users and global hold flags require careful adapter behaviour.
- [RFQ controller](../../../erpnext/erpnext/buying/doctype/request_for_quotation/request_for_quotation.py), [RFQ portal](../../../erpnext/erpnext/templates/pages/rfq.py): ordinary RFQ can send mail, link users and create quotations; do not reuse it as a sealed-envelope store.
- [Portal transaction access](../../../erpnext/erpnext/controllers/website_list_for_contact.py): native Supplier membership is a distinct access path requiring qualification.
- [Purchase Order](../../../erpnext/erpnext/buying/doctype/purchase_order/purchase_order.py), [Purchase Receipt](../../../erpnext/erpnext/stock/doctype/purchase_receipt/purchase_receipt.py), [Purchase Invoice](../../../erpnext/erpnext/accounts/doctype/purchase_invoice/purchase_invoice.py), [Payment Entry](../../../erpnext/erpnext/accounts/doctype/payment_entry/payment_entry.py): preserve native accounting/quantity validation.
- [Budget schema](../../../erpnext/erpnext/accounts/doctype/budget/budget.json), [controller](../../../erpnext/erpnext/accounts/doctype/budget/budget.py): supports company, project/cost centre and configurable exceedance actions; pre-award planning is not an accounting commitment.
- [Contract schema](../../../erpnext/erpnext/crm/doctype/contract/contract.json), [controller](../../../erpnext/erpnext/crm/doctype/contract/contract.py): supports Supplier party and linked documents but lacks the full company-specific procurement envelope.
- [Blanket Order](../../../erpnext/erpnext/manufacturing/doctype/blanket_order/blanket_order.py): candidate for purchasing frameworks with owned balance controls.
- [Website base](../../../frappe/frappe/templates/base.html), [Website Theme](../../../frappe/frappe/website/doctype/website_theme/website_theme.py), [framework hooks](../../../frappe/frappe/hooks.py), [ERPNext hooks](../../../erpnext/erpnext/hooks.py).
- [Existing handbook](../../../tag_marketing/docs/whatsapp_marketing/README.md): documentation ownership, evidence discipline and native UI precedent; its single-company marketing assumptions do not apply here.

## Official sources checked

- [ERPNext Buying](https://docs.frappe.io/erpnext/buying): purchasing lifecycle and goods/service handling.
- [Request for Quotation](https://docs.frappe.io/erpnext/request-for-quotation): ordinary supplier invitations and quotation workflow; formal sealed tender policy is an owned design.
- [Frappe hooks](https://docs.frappe.io/framework/user/en/python-api/hooks): supported application extension mechanisms; qualify exact hooks against this checkout.
- [SARS TCS guidance](https://www.sars.gov.za/guide-to-the-tax-compliance-status-functionality-on-efiling/): distinguishes TCS PIN verification from merely possessing an upload. This design does not assume a public verification API.

The broad portal-development documentation URL was inaccessible during review. Portal design therefore uses inspected local website/portal source and must be runtime-qualified in P0/P1. SA registration/B-BBEE/insurance examples are administrator-editable placeholders for business policy; no claim of universally mandatory documents, legal retention duration or statutory scoring formula is made.
