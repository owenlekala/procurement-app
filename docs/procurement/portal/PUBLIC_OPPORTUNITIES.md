# Public Opportunities

Website route: `/procurement/opportunities`. Audience: Guests and vendor users.

[Screen contract](README.md) · [Policy owner](../TENDERING_AND_EVALUATION.md).

## Components and layout

Active website navbar/footer, public company/category/location/search filters and paginated native-style opportunity cards. Use a factual heading, not internal dashboard widgets.

## Displayed fields and context

Published title/reference, buying company, category/location, work type, closing date/offset and public summary. No estimates, bidder identities or internal panel data.

## Actions by state

View detail/public documents; sign in/register; eligible members may follow a tender. Guests cannot create participation or submit a bid.

## Permission boundaries

Only current published Public versions appear; invited-only identifiers return generic Not found. Private records never enter page cache or search feed.

## Validation, loading and exception states

No opportunities offers filter reset; unavailable service shows retry without fabricated entries. Validate allowed filters/page bounds and escape all published summaries.

## Responsive and keyboard behaviour

Cards become one column with readable deadline; filters stack and retain selections on back navigation.

## Acceptance links

[PROC-A02](../TESTING_AND_ACCEPTANCE.md#proc-a02), [PROC-A13](../TESTING_AND_ACCEPTANCE.md#proc-a13), [PROC-A14](../TESTING_AND_ACCEPTANCE.md#proc-a14), [PROC-A28](../TESTING_AND_ACCEPTANCE.md#proc-a28).
