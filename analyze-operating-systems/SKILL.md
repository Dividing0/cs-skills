---
name: analyze-operating-systems
description: "Analyze OS resource and execution behavior. Use for process/thread scheduling, virtual memory, page faults, descriptors, IPC, file systems, readiness/completion APIs and process lifecycle failures."
---

# Analyze Operating Systems

## Scope and routing

Explain kernel/application interactions on a specific platform. Use architecture analysis for hardware effects and async-runtime design for user-space scheduling contracts.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Capture OS/kernel version, resource limits, cgroup/container settings, process topology and the exact observed symptom.
2. Map application operations to threads, descriptors, mappings, syscalls and scheduler states; distinguish per-process and system-wide limits.
3. Measure CPU/runnable time, blocking, page faults, I/O and resource growth using platform-supported traces with known overhead.
4. Analyze readiness versus completion, partial operations, EINTR/EAGAIN and descriptor reuse; document platform-specific differences.
5. Inspect exit, signal, cancellation, inheritance and cleanup paths; account for mmap/page cache separately from heap ownership.
6. Validate one causal hypothesis with an isolated reproducer and before/after resource evidence; preserve permission and production constraints.

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

`design-async-runtime`, `analyze-system-performance`, `analyze-memory-lifecycles`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
