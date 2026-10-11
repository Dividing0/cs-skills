---
name: test-distributed-systems
description: "Test distributed behavior using operation histories and controlled faults. Use for deterministic scheduling, crashes, partitions, message delay/duplication, recovery, consistency checks and minimized failing traces."
---

# Test Distributed Systems

## Scope and routing

Generate and execute experiments in isolated systems. Use consistency verification to interpret histories and fault-tolerant design to choose fixes.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Identify the deployment topology, operation model, fault permissions, isolation and property oracle before executing a test.
2. Build a deterministic workload with operation IDs, monotonic client timings, recorded results and pending/failed outcome semantics.
3. Schedule faults at specific protocol/durability boundaries; include asymmetric partitions, restarts and correlated dependencies when relevant.
4. Check safety during/after faults and liveness only under documented recovery/fairness conditions and observation windows.
5. Minimize failures while preserving the causal schedule; save seed, build, configuration, fault timeline and history for replay.
6. Report tested scenarios and uncovered regions; do not promote passing fault runs into universal correctness or availability claims.

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

`verify-distributed-consistency`, `model-check-state-machines`, `design-fault-tolerant-systems`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
