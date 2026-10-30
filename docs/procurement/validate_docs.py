#!/usr/bin/env python3
"""Read-only structural checks for the canonical procurement handbook."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent
ROOT_NAMES = """AGENTS API_CONTRACTS ARCHITECTURE AUTOMATION_AND_RELIABILITY
CONTRACTS_AND_FULFILMENT DATA_MODEL ERPNext_INTEGRATION FRAMEWORK_AND_SETUP
IMPLEMENTATION_KICKOFF IMPLEMENTATION_PLAN IMPLEMENTATION_RULES OPERATIONS_AND_RELEASE
PERMISSIONS_AND_PRIVACY PROCUREMENT_POLICY PRODUCT_REQUIREMENTS PROGRESS README
REFERENCES REGISTRATION_AND_COMPLIANCE REPORTING TENDERING_AND_EVALUATION
TESTING_AND_ACCEPTANCE TRACEABILITY UI_DESIGN_SYSTEM""".split()
SCREEN_NAMES = """OVERVIEW PROCUREMENT_REQUESTS VENDOR_APPLICATIONS VENDOR_DATABASE
COMPLIANCE_REVIEWS TENDERS EVALUATION AWARDS CONTRACTS ORDERS_AND_FULFILMENT
INVOICE_CLAIMS REPORTS AUTOMATIONS SETTINGS""".split()
PORTAL_NAMES = """PUBLIC_OPPORTUNITIES TENDER_DETAIL REGISTRATION APPLICATION_PROGRESS
COMPANY_PROFILE COMPLIANCE_DOCUMENTS INVITATIONS BID_WORKSPACE SUBMITTED_BIDS_AND_RESULTS
CONTRACTS_AND_ORDERS DELIVERIES_AND_MILESTONES INVOICE_CLAIMS_AND_PAYMENTS
NOTIFICATIONS TEAM_AND_PREFERENCES""".split()
FLOW_NAMES = """IDENTITY_AND_ONBOARDING REGISTRATION_AND_REVIEW RENEWAL_AND_REMEDIATION
REQUEST_AND_SOURCING PUBLICATION_AND_MATCHING BID_SUBMISSION_AND_REVISION
OPENING_AND_EVALUATION AWARD_ACCEPTANCE_AND_COMPLAINT CONTRACTS_AND_ORDERS
FULFILMENT_CLAIMS_AND_PAYMENT AUTOMATION_AND_RECOVERY MIGRATION_AND_OFFBOARDING""".split()
PHASE_NAMES = """P0-ENVIRONMENT-AND-BOOTSTRAP P1-APP-AND-NATIVE-UI
P2-REGISTRATION-AND-PORTAL P3-APPROVAL-AND-COMPLIANCE P4-REQUESTS-AND-TENDERS
P5-BIDS-AND-OPENING P6-EVALUATION-AND-AWARDS P7-CONTRACTS-AND-FULFILMENT
P8-AUTOMATION-AND-REPORTING P9-QUALIFICATION-AND-RELEASE""".split()
DECISION_NAMES = """README ADR-001-APP-AND-DESIGN-BASELINE
ADR-002-IDENTITY-AND-ERPNext-OWNERSHIP ADR-003-SEALED-BIDS-AND-DURABLE-WORK""".split()


def expected_files() -> set[str]:
    result = {f"{name}.md" for name in ROOT_NAMES}
    for folder, names in (
        ("pages", ["README", *SCREEN_NAMES]),
        ("portal", ["README", *PORTAL_NAMES]),
        ("flows", ["README", *FLOW_NAMES]),
        ("tasks", ["README", *PHASE_NAMES]),
        ("decisions", DECISION_NAMES),
    ):
        result.update(f"{folder}/{name}.md" for name in names)
    return result


def prose(body: str) -> str:
    return re.sub(r"^```[^\n]*\n.*?^```\s*$", "", body, flags=re.M | re.S)


def anchors(body: str) -> set[str]:
    counts: Counter[str] = Counter()
    result = set()
    for title in re.findall(r"^#{1,6}\s+(.+)$", prose(body), re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        number = counts[slug]
        counts[slug] += 1
        result.add(slug + (f"-{number}" if number else ""))
    return result


def substantive_paragraphs(body: str) -> list[str]:
    """Ignore navigation-only fragments; compare copied prose independent of links."""
    result = []
    for paragraph in re.split(r"\n\s*\n", prose(body)):
        paragraph = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", paragraph)
        paragraph = re.sub(r"\s+", " ", paragraph).strip()
        if len(paragraph.split()) >= 35 and not paragraph.startswith("#"):
            result.append(paragraph)
    return result


def validate(contents: dict[str, str]) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    expected = expected_files()
    if set(contents) != expected:
        errors.append(
            f"Inventory: missing={sorted(expected - set(contents))}, "
            f"extra={sorted(set(contents) - expected)}"
        )
    links = 0
    source_paths = set()
    mermaid = 0
    seen_bodies: dict[str, str] = {}
    paragraph_owners: defaultdict[str, list[str]] = defaultdict(list)
    for name, body in contents.items():
        if len(body.split()) < 70:
            errors.append(f"Short specification: {name}")
        if body in seen_bodies:
            errors.append(f"Duplicate files: {name}, {seen_bodies[body]}")
        seen_bodies[body] = name
        for paragraph in substantive_paragraphs(body):
            paragraph_owners[paragraph].append(name)
        if len(re.findall(r"^```", body, re.M)) % 2:
            errors.append(f"Unbalanced code fences: {name}")
        diagrams = re.findall(r"^```mermaid\s*\n(.*?)^```", body, re.M | re.S)
        mermaid += len(diagrams)
        for diagram in diagrams:
            if not re.match(r"flowchart\s+(TD|LR)\s*\n", diagram):
                errors.append(f"Unsupported Mermaid header: {name}")
            if "-->" not in diagram:
                errors.append(f"Missing Mermaid flow edges: {name}")
        if not name.startswith("tasks/P") and re.search(r"^- \[[ xX]\]", body, re.M):
            errors.append(f"Misplaced completion checkbox: {name}")
        if "docs/TAG_WAmarketing" in body:
            errors.append(f"Stale reference: {name}")
        for href in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", prose(body)):
            href = href.strip("<>")
            parsed = urlsplit(href)
            if parsed.scheme or href.startswith("//"):
                continue
            target = unquote(parsed.path)
            dest = ((ROOT / name).parent / target).resolve() if target else ROOT / name
            links += 1
            if dest.is_relative_to(ROOT):
                relative = dest.relative_to(ROOT).as_posix()
                exists = relative in contents or (dest.is_file() and dest.suffix != ".md")
                destination_body = contents.get(relative, "")
            else:
                source_paths.add(str(dest))
                exists = dest.exists()
                destination_body = dest.read_text() if exists and dest.suffix == ".md" else ""
            if not exists:
                errors.append(f"Broken link: {name} -> {href}")
            elif parsed.fragment and dest.suffix == ".md":
                if unquote(parsed.fragment) not in anchors(destination_body):
                    errors.append(f"Broken anchor: {name} -> {href}")

    repeated_paragraphs = 0
    for paragraph, owners in paragraph_owners.items():
        if len(owners) > 1:
            repeated_paragraphs += 1
            errors.append(f"Repeated shared paragraph: {sorted(owners)}: {paragraph[:90]}")

    requirement_defs = re.findall(
        r"^- \*\*(PROC-R\d{2}) —", contents.get("PRODUCT_REQUIREMENTS.md", ""), re.M
    )
    acceptance_defs = re.findall(
        r"^### (PROC-A\d{2})\s*$", contents.get("TESTING_AND_ACCEPTANCE.md", ""), re.M
    )
    requirements, acceptance = set(requirement_defs), set(acceptance_defs)
    if len(requirement_defs) != 30 or len(requirements) != 30:
        errors.append("Expected 30 unique requirement definitions")
    if len(acceptance_defs) != 30 or len(acceptance) != 30:
        errors.append("Expected 30 unique acceptance definitions")
    for name, body in contents.items():
        for rid in re.findall(r"\bPROC-R\d{2}\b", body):
            if rid not in requirements:
                errors.append(f"Unknown requirement: {rid} in {name}")
        for aid in re.findall(r"\bPROC-A\d{2}\b", body):
            if aid not in acceptance:
                errors.append(f"Unknown acceptance: {aid} in {name}")

    tasks: dict[str, list[str]] = {}
    requirement_tasks: defaultdict[str, set[str]] = defaultdict(set)
    acceptance_tasks: defaultdict[str, set[str]] = defaultdict(set)
    for name, body in contents.items():
        if not name.startswith("tasks/P"):
            continue
        parts = re.split(r"^## (PROC-P\d-\d{3})\s*$", body, flags=re.M)
        if len(parts) != 9:
            errors.append(f"Phase must define four tasks: {name}")
        for index in range(1, len(parts), 2):
            tid, section = parts[index : index + 2]
            if tid in tasks:
                errors.append(f"Duplicate task: {tid}")
            dependency = re.search(r"\*\*Depends on:\*\* (.+)", section)
            tasks[tid] = re.findall(r"PROC-P\d-\d{3}", dependency.group(1)) if dependency else []
            for label in (
                "Depends on", "Requirements", "Acceptance", "Read first",
                "Implementation and boundaries", "Failure cases and verification", "Completion evidence",
            ):
                if f"**{label}:**" not in section:
                    errors.append(f"Missing task contract: {tid} {label}")
            if len(re.findall(r"^- \[[ xX]\] ", section, re.M)) != 1:
                errors.append(f"Task must own one checkbox: {tid}")
            for rid in re.findall(r"PROC-R\d{2}", section):
                requirement_tasks[rid].add(tid)
            for aid in re.findall(r"PROC-A\d{2}", section):
                acceptance_tasks[aid].add(tid)
            if tid not in contents.get("tasks/README.md", ""):
                errors.append(f"Task absent from index: {tid}")
            if tid not in contents.get("TRACEABILITY.md", ""):
                errors.append(f"Task absent from traceability: {tid}")
    if len(tasks) != 40:
        errors.append(f"Expected 40 unique tasks, got {len(tasks)}")
    visiting, visited = set(), set()

    def visit(tid: str) -> None:
        if tid in visiting:
            errors.append(f"Dependency cycle: {tid}")
            return
        if tid in visited:
            return
        visiting.add(tid)
        for dependency in tasks[tid]:
            if dependency not in tasks:
                errors.append(f"Unknown dependency: {tid} -> {dependency}")
            else:
                visit(dependency)
        visiting.remove(tid)
        visited.add(tid)

    for tid in tasks:
        visit(tid)
    traceability = contents.get("TRACEABILITY.md", "")
    for rid in requirements:
        if not requirement_tasks[rid] or rid not in traceability:
            errors.append(f"Uncovered requirement: {rid}")
    for aid in acceptance:
        if not acceptance_tasks[aid] or aid not in traceability:
            errors.append(f"Uncovered acceptance: {aid}")
    trace_sections = re.split(r"^### (PROC-R\d{2}) .+$", traceability, flags=re.M)
    for index in range(1, len(trace_sections), 2):
        rid, section = trace_sections[index : index + 2]
        expected_acceptance = rid.replace("-R", "-A")
        if expected_acceptance not in section:
            errors.append(f"Traceability section missing acceptance: {rid}")
        referenced = set(re.findall(r"PROC-P\d-\d{3}", section))
        if referenced != requirement_tasks[rid]:
            errors.append(f"Traceability task mapping mismatch: {rid}")
    for name, body in contents.items():
        for tid in re.findall(r"\bPROC-P\d-\d{3}\b", body):
            if tid not in tasks:
                errors.append(f"Unknown task reference: {name} -> {tid}")
    for folder, names in (("pages", SCREEN_NAMES), ("portal", PORTAL_NAMES)):
        for screen in names:
            name = f"{folder}/{screen}.md"
            body = contents.get(name, "")
            for heading in (
                "Components and layout", "Displayed fields and context", "Actions by state",
                "Permission boundaries", "Validation, loading and exception states",
                "Responsive and keyboard behaviour", "Acceptance links",
            ):
                if f"## {heading}" not in body:
                    errors.append(f"Missing screen contract: {name} {heading}")
            if f"({screen}.md)" not in contents.get(f"{folder}/README.md", ""):
                errors.append(f"Screen missing from index: {name}")
            if not re.search(r"PROC-A\d{2}", body):
                errors.append(f"Screen lacks acceptance links: {name}")
    for name in FLOW_NAMES:
        body = contents.get(f"flows/{name}.md", "")
        if len(re.findall(r"^```mermaid", body, re.M)) != 1:
            errors.append(f"Flow must have one diagram: {name}")
        for heading in (
            "Entry, ownership and transaction boundary", "Decisions and durable effects",
            "Exceptions and recovery", "Required verification",
        ):
            if f"## {heading}" not in body:
                errors.append(f"Missing flow contract: {name} {heading}")
        if f"({name}.md)" not in contents.get("flows/README.md", ""):
            errors.append(f"Flow missing from index: {name}")
    if mermaid != 13:
        errors.append(f"Expected 13 Mermaid diagrams, got {mermaid}")
    return errors, {
        "markdown_files": len(contents), "relative_links": links,
        "source_paths": len(source_paths), "requirements": len(requirements),
        "acceptance_scenarios": len(acceptance), "implementation_tasks": len(tasks),
        "desk_screens": len(SCREEN_NAMES), "portal_screens": len(PORTAL_NAMES),
        "workflow_documents": len(FLOW_NAMES), "mermaid_diagrams": mermaid,
        "repeated_shared_paragraphs": repeated_paragraphs,
    }


def self_test(contents: dict[str, str]) -> list[str]:
    def changed(name: str, transform) -> dict[str, str]:
        sample = contents.copy()
        sample[name] = transform(sample[name])
        return sample

    scenarios = [
        ("broken link", changed("README.md", lambda body: body + "\n[broken](missing.md)\n"), "Broken link"),
        ("unknown ID", changed("README.md", lambda body: body + "\nPROC-R99\n"), "Unknown requirement"),
        ("cycle", changed("tasks/P0-ENVIRONMENT-AND-BOOTSTRAP.md", lambda body: body.replace(
            "**Depends on:** None; first implementation task.", "**Depends on:** `PROC-P9-004`", 1
        )), "Dependency cycle"),
        ("duplicate acceptance", changed("TESTING_AND_ACCEPTANCE.md", lambda body: body + "\n### PROC-A01\n"), "30 unique acceptance"),
        ("misplaced checkbox", changed("README.md", lambda body: body + "\n- [ ] Invalid status\n"), "Misplaced completion"),
        ("missing inventory", {name: body for name, body in contents.items() if name != "portal/REGISTRATION.md"}, "Inventory"),
        ("copied shared prose", changed("README.md", lambda body: body + "\n\n" + next(
            paragraph for paragraph in re.split(r"\n\s*\n", contents["ARCHITECTURE.md"])
            if len(paragraph.split()) >= 35 and not paragraph.startswith(("#", "```"))
        ) + "\n"), "Repeated shared paragraph"),
        ("incomplete traceability", changed("TRACEABILITY.md", lambda body: body.replace(
            "[PROC-P0-001](tasks/P0-ENVIRONMENT-AND-BOOTSTRAP.md#proc-p0-001), ", "", 1
        )), "Traceability task mapping mismatch"),
        ("repeated prose within one file", changed("ARCHITECTURE.md", lambda body: body + "\n\n" + next(
            paragraph for paragraph in re.split(r"\n\s*\n", body)
            if len(paragraph.split()) >= 35 and not paragraph.startswith(("#", "```"))
        ) + "\n"), "Repeated shared paragraph"),
    ]
    failures = []
    for label, sample, expected in scenarios:
        errors, _ = validate(sample)
        if not any(expected in error for error in errors):
            failures.append(f"Self-test failed to detect {label}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="Exercise nine in-memory negative cases")
    args = parser.parse_args()
    contents = {path.relative_to(ROOT).as_posix(): path.read_text() for path in ROOT.rglob("*.md")}
    errors, stats = validate(contents)
    if args.self_test and not errors:
        errors.extend(self_test(contents))
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    for key, value in stats.items():
        print(f"PASS: {key}={value}")
    if args.self_test:
        print("PASS: nine in-memory negative self-tests; no files changed")
    print("LIMIT: structure only; no graphical Mermaid rendering or application/runtime qualification")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
