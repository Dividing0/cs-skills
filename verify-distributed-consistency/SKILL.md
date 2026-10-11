---
name: verify-distributed-consistency
description: "Check stated consistency and transaction isolation guarantees against formal specifications and operation histories. Use for linearizability, serializability, strict serializability, session guarantees and stale-read counterexamples."
---

# Verify Distributed Consistency

## Scope and routing

Verify a named property for a specific object or transaction model. Use distributed-system design for architecture and distributed testing for fault scheduling.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. State the exact property, object semantics, initial state and observation model; distinguish real-time order from per-client order and transaction dependencies.
2. Normalize histories into invocation, completion, arguments, results, operation IDs and clock assumptions; retain pending and failed operations rather than silently removing them.
3. For linearizability search legal sequential executions that preserve non-overlap real-time precedence; for serializability analyze transaction semantics/dependencies instead.
4. Treat timeouts as uncertain completion unless the API proves abort; choose and document permitted completions/extensions of partial histories.
5. Produce a witness order for an accepted history or a minimal conflicting history for a violation; bound search and return unknown on exhaustion.
6. Explain coverage: a passing finite history is compatible with the property, not proof of the implementation under every execution.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/check_register.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`test-distributed-systems`, `model-check-state-machines`, `solve-with-z3`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
