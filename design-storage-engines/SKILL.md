---
name: design-storage-engines
description: "Design durable storage and indexing engines. Use for B-tree/LSM layouts, WAL, compaction, checksums, manifests, snapshots, write amplification and crash-safe recovery."
---

# Design Storage Engines

## Scope and routing

Build engine persistence mechanics. Use database-internals analysis for an existing DB and external-memory algorithms for bulk data processing.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify key/value format, operations, transaction scope, consistency, durability acknowledgement and storage-device assumptions.
2. Choose index/page/run layout with versioned encoding, checksums and explicit memory/I/O budgets.
3. Design WAL ordering, flush barriers, checkpoint/manifest publication and recovery so acknowledged work survives the claimed failure model.
4. Model compaction, tombstones, snapshot retention and file reclamation; prevent deletion of data still visible to readers.
5. Enumerate crash points around writes, syncs, renames and metadata publication; document filesystem/device semantics instead of assuming rename implies durability.
6. Validate recovery with fault-injected write/sync failures and a reference map; measure read/write/space amplification under representative workloads.

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

`design-external-memory-algorithms`, `analyze-memory-lifecycles`, `verify-distributed-consistency`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
