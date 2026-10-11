---
name: analyze-memory-lifecycles
description: "Diagnose object retention, leaks, ownership and resource release across garbage-collected runtimes, native code and FFI. Use for retained callbacks, timer cancellation, reference cycles, allocator growth or incomplete teardown."
---

# Analyze Memory Lifecycles

## Scope and routing

Trace concrete ownership paths and release events. Use language-specific unsafe auditing for pointer validity and performance skills for allocator throughput.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Capture the reproducer, interpreter/build versions, allocation sizes, object counts and exact lifecycle event expected to release each resource.
2. Draw the ownership graph across callbacks, arguments, contexts, queues, handles, FFI wrappers and native buffers; distinguish strong, weak and borrowed edges.
3. Measure live-object survival with weak references or finalizers after deleting external references; compare before cancellation, after cancellation, after queue processing and after close.
4. Separate reachable retention, unreachable cycles, native allocations and allocator-reserved memory; compare heap evidence with RSS rather than treating RSS alone as a leak detector.
5. Check teardown order, repeated cancel/close calls, exceptions and destructor reentrancy; release payloads without exposing invalid handle state to reentrant Python code.
6. Produce a minimal failing regression; validate that the fix releases payloads at the required event while preserving identity, scheduling and cancellation semantics.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/retention_probe.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`audit-python-native-boundary`, `optimize-pyo3-boundary`, `test-python-correctness`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
