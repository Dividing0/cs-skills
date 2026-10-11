---
name: analyze-consensus-protocols
description: "Analyze consensus and replicated-log protocols against explicit safety and liveness assumptions. Use for Raft/Paxos, quorum intersection, leader election, commit rules, membership changes and stale-leader reads."
---

# Analyze Consensus Protocols

## Scope and routing

Verify protocol mechanics and assumptions. Use distributed-system design for service architecture and model checking for executable abstractions.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Identify the exact protocol/version, crash versus Byzantine model, persistence guarantees, network timing and membership rules.
2. Define ballots/terms, votes, log positions, quorum sets and invariants preventing conflicting committed decisions.
3. Trace election, append/accept and commit paths including stale messages, leader changes and recovery of durable metadata.
4. Audit current-term commit constraints, read protocols, snapshots and joint/reconfigured membership against the chosen protocol.
5. Check liveness separately under stated eventual synchrony/failure-detector assumptions; timeouts alone do not prove safety.
6. Build small adversarial histories or a model; report counterexamples and distinguish informal proof, bounded model checks and implementation tests.

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

`model-check-state-machines`, `verify-distributed-consistency`, `design-distributed-systems`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
