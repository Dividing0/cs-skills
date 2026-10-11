---
name: design-parallel-algorithms
description: "Design and analyze parallel algorithms using work/span and resource constraints. Use for decomposition, dependencies, task granularity, reductions, synchronization, scaling and deterministic results."
---

# Design Parallel Algorithms

## Scope and routing

Analyze parallel algorithm structure. Use architecture analysis for NUMA/cache details and distributed-system design for failure-prone network services.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify computational task, sequential reference, dependency graph, output semantics and available processors/memory bandwidth.
2. Decompose work and identify critical-path span, total work, scheduling assumptions and communication costs.
3. Choose task granularity and reduction strategy; preserve dependencies and bound intermediate memory and synchronization.
4. Audit races, ownership, false sharing and nonassociative arithmetic; decide whether deterministic ordering or numerical tolerance is required.
5. Validate results with a sequential oracle and adversarial partition sizes; test zero/one worker and uneven workloads.
6. Measure strong/weak scaling separately and compare measured speedup with work/span, bandwidth and serial-fraction limits.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/work_span.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`design-and-implement-algorithms`, `analyze-computer-architecture`, `analyze-system-performance`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
