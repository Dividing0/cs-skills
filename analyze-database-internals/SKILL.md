---
name: analyze-database-internals
description: "Diagnose database behavior from engine internals and concrete workloads. Use for query plans, indexes, MVCC, locks, transaction isolation, WAL, vacuum, connection contention and crash recovery."
---

# Analyze Database Internals

## Scope and routing

Analyze the selected database version. Use storage-engine design to implement engines and consistency verification to assess abstract transaction guarantees.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Capture database engine/version, schema, cardinalities, statistics, query parameters, transaction boundaries, isolation and representative plans.
2. Read estimated and actual rows, scan/join methods, loops, spills and buffers; identify cardinality mistakes before recommending indexes.
3. Trace lock waits, transaction age, snapshots, row versions and connection occupancy; relate MVCC cleanup to long-lived transactions.
4. Compare candidate indexes or query rewrites against read/write costs, storage, selectivity and realistic parameter distributions.
5. Separate commit acknowledgement, WAL flush, replication acknowledgement and durability settings; check restart/recovery expectations explicitly.
6. Validate in an isolated representative database with result equivalence, concurrent transactions and measured plan/resource changes.

## Evidence and completion

- Inspect actual code, configuration, schemas or traces before diagnosing a concrete system; give artifact/function references for findings.
- Read [domain guide](references/domain-guide.md) for domain pitfalls and a worked task; consult it before making a guarantee.
- Read [primary sources](references/sources.md) for authoritative starting points. Check current version-specific documentation when APIs, standards or tool behavior matter. Never fabricate tool availability, source citations or measurements.
- Run the relevant available checks after changes and preserve the command, versions, input, outcome and reproducibility conditions. If execution is unavailable, say which validation remains unperformed and give the runnable check.
- Distinguish a mathematical proof, tool proof under assumptions, finite/bounded exploration, passing tests, simulation and measured observations. Report timeouts, unsupported models and incomplete data as unknown, not success.
- Complete the requested artifact or fix within the authorized scope; use the smallest change supported by evidence. Validate the user's acceptance criteria as well as the model's internal properties.

## Deliverable

Use [report template](assets/report-template.md) as a checklist, adapting length to the task. Lead with the result, then give assumptions, the concrete model/design/change, evidence, limitations and remaining checks. Include a minimal counterexample for a refuted claim. For a design, include implementation-ready contracts and acceptance criteria.

## Related skills

`design-storage-engines`, `verify-distributed-consistency`, `analyze-system-performance`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
