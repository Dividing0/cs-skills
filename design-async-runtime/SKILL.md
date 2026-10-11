---
name: design-async-runtime
description: "Design or review asynchronous runtimes and event loops. Use for runnable queues, timer heaps, readiness polling, wakeups, cancellation, fairness, shutdown and compatibility with asyncio or native task contracts."
---

# Design Async Runtime

## Scope and routing

Specify scheduler and lifecycle semantics across components. Delegate language-level race diagnosis to validate-rust-concurrency and object release diagnosis to analyze-memory-lifecycles.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify task, callback, timer and I/O-handle states, queue membership invariants, thread-affinity rules and the public compatibility contract.
2. Define enqueue/dequeue linearization points, wakeup coalescing and the poll timeout; handle newly queued work arriving between idle checks and blocking.
3. Use monotonic deadlines, deterministic tie handling where required and explicit timer tombstone/payload policies; test zero-delay and callback-created timers.
4. Specify cancellation at each await boundary, result delivery, exactly-once completion and ownership cleanup when exceptions or cancellation race readiness.
5. Bound per-tick work to prevent ready-queue starvation of I/O and timers; define draining, shutdown and executor/task cleanup separately.
6. Validate with deterministic schedules and real socket/timer workloads; measure throughput, tail latency and starvation under the same load and reference implementation.

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

`validate-rust-concurrency`, `analyze-memory-lifecycles`, `analyze-system-performance`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
