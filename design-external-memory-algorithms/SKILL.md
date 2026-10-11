---
name: design-external-memory-algorithms
description: "Design algorithms for data exceeding RAM. Use for external sorting, block I/O complexity, merge fan-in, partitioning, streaming joins, disk spill and memory/file-descriptor bounds."
---

# Design External Memory Algorithms

## Scope and routing

Model algorithmic I/O and resource use. Use storage-engine design for durable indexing and system-performance analysis for actual device behavior.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify dataset size N, available memory M, block size B, record sizes, storage topology, descriptor limits and output durability needs.
2. Choose sequential scanning, external merge sorting, partitioned hashing or indexed access based on required operations and skew.
3. Derive I/O passes and fan-in accounting for input buffers, output buffers, metadata and open files; include variable-size records.
4. Design spill naming, temporary-space bounds, cleanup and restart behavior without overwriting input data.
5. Validate correctness against an in-memory oracle on small data and verify behavior under duplicates, skew, malformed records and disk-full errors.
6. Measure large-data throughput, bytes read/written and memory high-water marks; distinguish the ideal block-I/O model from measured device costs.

## Executable helper

Read [external-sort contract](references/command-line.md) before using `scripts/external_sort.py`; its text ordering, byte-budget limits and failure semantics are intentionally narrow.

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

`design-and-implement-algorithms`, `design-storage-engines`, `analyze-system-performance`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
