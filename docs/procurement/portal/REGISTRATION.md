# Registration

Website route: `/procurement/register`. Audience: Email-verified prospective vendor owners and existing organisation members adding a buying company.

[Screen contract](README.md) · [Policy owner](../REGISTRATION_AND_COMPLIANCE.md).

## Components and layout

Themed step form: identity, categories/coverage, resolved requirements, documents, review/submit. Desktop step navigation and one current section; mobile uses one labelled step at a time.

## Displayed fields and context

Legal identifiers, contact/address, selected buying companies, services/work types/regions, typed configured questions, private evidence, notices and optional job subscriptions.

## Actions by state

Claim identity; save/resume; add required files; preview resolved checklist; submit each company application independently; return from duplicate review with a safe status.

## Permission boundaries

Email domain never grants membership. Existing organisation conflicts reveal no private data. Only authorised owner/delegate can submit; contributors prepare assigned content.

## Validation, loading and exception states

Validate conditional requirements on server, clean scans, dates/types/limits, declarations and current revision. Distinguish duplicate pending review, upload pending and ordinary missing fields.

## Responsive and keyboard behaviour

Preserve entered answers on failed save; show last saved time and focus first invalid field; uploads display progress/scan status with text.

## Acceptance links

[PROC-A04](../TESTING_AND_ACCEPTANCE.md#proc-a04), [PROC-A05](../TESTING_AND_ACCEPTANCE.md#proc-a05), [PROC-A06](../TESTING_AND_ACCEPTANCE.md#proc-a06), [PROC-A07](../TESTING_AND_ACCEPTANCE.md#proc-a07), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
