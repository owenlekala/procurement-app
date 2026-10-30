# Overview

Native destination: `Workspace`. Audience: Requesters and authorised company procurement/finance operators.

[Screen contract](README.md) · [Policy owner](../REPORTING.md).

## Components and layout

Native Workspace with company/date filters, Number Cards, Dashboard Charts and a My pending actions list. Keep the existing page header; card and chart drill-down preserve the selected company and period.

## Displayed fields and context

Open applications, expiring approvals, sourcing progress, pending evaluations, overdue fulfilment, unmatched claims and native outstanding amounts grouped by currency. Operators additionally see queue/scanner exceptions.

## Actions by state

Create request when permitted; open assigned review/evaluation; drill into a metric; open readiness diagnostics for authorised operators. No approval occurs from an aggregate card.

## Permission boundaries

Apply underlying company/assignment/financial predicates to values as well as links. Cross-company totals require explicit access to every included company.

## Validation, loading and exception states

Show empty workload with a permitted next step; show unavailable data as unavailable, never zero. Preserve filters on retry; reject unsupported date ranges.

## Responsive and keyboard behaviour

Cards wrap to one column; charts retain labelled summaries; task rows expose company and deadline without horizontal page scroll.

## Acceptance links

[PROC-A02](../TESTING_AND_ACCEPTANCE.md#proc-a02), [PROC-A03](../TESTING_AND_ACCEPTANCE.md#proc-a03), [PROC-A27](../TESTING_AND_ACCEPTANCE.md#proc-a27), [PROC-A29](../TESTING_AND_ACCEPTANCE.md#proc-a29).
