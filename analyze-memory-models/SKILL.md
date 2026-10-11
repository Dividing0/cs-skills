---
name: analyze-memory-models
description: "Analyze shared-memory concurrency under an explicit language or hardware memory model. Use for happens-before, atomics, acquire/release publication, fences, ABA, lock-free reclamation and weak-memory litmus tests."
---

# Analyze Memory Models

## Scope and routing

Reason about allowed executions and lifetime separately. Use concurrency validation for broader task/lock lifecycles and architecture analysis for measured cache behavior.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Identify the language standard, compiler, architecture, atomic widths and data-race rules; do not transfer LKMM guarantees directly into Rust or C++.
2. List reads, writes, read-modify-write operations and synchronization edges; distinguish sequenced-before, modification order, reads-from and happens-before.
3. Encode the disputed outcome as a litmus test and check whether synchronization actually exists for that reads-from case.
4. Audit ownership publication, aliasing and reclamation; an atomic pointer or stronger ordering alone does not keep the referenced object alive.
5. For CAS loops examine success and failure ordering, spurious failure, ABA, progress guarantees and reclamation via epochs or hazards.
6. Use an appropriate model checker if available; report the explored model/bounds and produce a proof sketch or counterexample without equating stress tests with proof.

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

`validate-rust-concurrency`, `audit-rust-unsafe`, `analyze-computer-architecture`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
