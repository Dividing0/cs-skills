---
name: design-fault-tolerant-systems
description: "Design recovery mechanisms with measurable failure behavior. Use for retries, idempotency, failover, fencing, circuit breakers, checkpoints, sagas, backup/restore and RPO/RTO requirements."
---

# Design Fault Tolerant Systems

## Scope and routing

Specify practical survival and recovery mechanisms. Use distributed-system design for topology and distributed tests to validate scenarios.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define failure modes, blast radius, acceptable loss/duplication, RPO/RTO and user-visible degraded behavior.
2. Map state changes to acknowledgement and durable records; identify ambiguous outcomes and non-idempotent external effects.
3. Design bounded retries with deadlines/jitter, stable idempotency keys and atomic effect/deduplication handling where needed.
4. Specify failover authority, fencing tokens and recovery ordering so stale actors cannot continue mutating shared state.
5. Plan backups, restore drills, checkpoints and compensations; distinguish compensation from true rollback of external effects.
6. Validate crash windows, dependency outages and recovery under load; measure restored correctness, resource bounds and actual RPO/RTO.

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

`design-backpressure`, `test-distributed-systems`, `verify-distributed-consistency`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
