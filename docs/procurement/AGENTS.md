# Procurement specification instructions

Read [README](README.md), [product requirements](PRODUCT_REQUIREMENTS.md) and [implementation rules](IMPLEMENTATION_RULES.md) before changing this subtree. Preserve the user's clean architecture and production-readiness requirements.

- Keep one authoritative owner for fields, persisted states, interfaces, policies, screen layouts and completion evidence. Shared page/flow/task guidance belongs in their indexes; link to it rather than copying paragraphs.
- Preserve `PROC-R`, `PROC-A` and `PROC-P` IDs; add rather than repurpose identifiers.
- Update affected flows, page links, task dependencies and traceability when behaviour changes.
- Use relative links, synthetic examples, translatable labels and valid Markdown/Mermaid.
- Record architecture changes in the [decision register](decisions/README.md).
- Separate inspected facts, proposed implementation and unverified runtime assumptions.
- Never mark implementation complete on documentation evidence alone.
- Run `python3 docs/procurement/validate_docs.py` from the workspace root after changes; semantic review remains necessary.

These instructions govern only this documentation subtree. P0 creates an app-level instruction bridge so future application code discovers this handbook; no sibling repository is implicitly governed by this file.
