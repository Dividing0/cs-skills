---
name: model-check-state-machines
description: "Build and check explicit transition-system models. Use for protocol states, lifecycle races, safety invariants, deadlock, temporal liveness, fairness assumptions and reproducible counterexample traces."
---

# Model Check State Machines

## Scope and routing

Check the abstraction supplied, not the entire implementation. Use program-contract verification for code obligations and distributed testing for faults on actual services.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define state variables, initial states, actions, domains and environment assumptions; map each action to concrete implementation events.
2. Write safety invariants and liveness properties separately; define terminal states, stuttering and the exact weak/strong fairness assumptions.
3. Start with a small finite model and executable safety checks; account for every enabled transition including cancellation, timeout and failures.
4. Check reachability, unexpected deadlocks and property violations; preserve the shortest useful counterexample as labelled state transitions.
5. For liveness use temporal tooling such as TLC with explicit fairness, or label the result unverified; reachability alone does not prove eventual progress.
6. Increase bounds and compare traces to the code; document symmetry/abstraction choices and replay implementation regressions derived from the model.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/check_safety.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`solve-with-z3`, `verify-rust-kani`, `verify-program-contracts`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
