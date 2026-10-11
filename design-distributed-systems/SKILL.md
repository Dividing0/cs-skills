---
name: design-distributed-systems
description: "Design service architectures with explicit distribution and failure contracts. Use for partitioning, replication, quorums, coordination, clocks, cross-service state and consistency/availability tradeoffs."
---

# Design Distributed Systems

## Scope and routing

Choose system structure and contracts. Delegate consensus internals, consistency verification, fault-tolerance mechanisms and live fault tests to dedicated skills.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define operations, scale, latency, geography, tenancy, durability and consistency required by users; capture workload and failure assumptions.
2. Map state ownership, shard keys, replication, trust boundaries and the component dependency graph.
3. Specify behavior for network partitions, crashes, recovery, delayed messages and clock skew; identify authority for each write.
4. Compare coordination/quorum and availability choices per operation, avoiding blanket CAP claims outside partition scenarios.
5. Specify API retry/idempotency, schema evolution, observability and rollout/recovery plans with bounded queues and capacities.
6. Produce decision records, concrete failure sequences and a validation plan; mark unverified throughput and availability targets as targets.

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

`analyze-consensus-protocols`, `design-fault-tolerant-systems`, `verify-distributed-consistency`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
