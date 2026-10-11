---
name: design-backpressure
description: "Design admission control and bounded resource flow for asynchronous pipelines. Use for queue sizing, overload, concurrency limits, rate limits, shedding, retries, producer blocking and cancellation propagation."
---

# Design Backpressure

## Scope and routing

Define overload behavior and resource bounds. Delegate runtime scheduling, stream event-time semantics and formal queueing results to their dedicated skills.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify accepted work, completion semantics, capacity in items and bytes, arrival/service distributions and latency or loss requirements.
2. Inventory every buffer and in-flight stage, including client libraries, retries, per-key state and transport queues; bound their aggregate ownership.
3. Choose per-stage producer blocking, rejection, drop-oldest, drop-newest or spill policies based on task semantics; distinguish admission from execution concurrency.
4. Propagate demand and cancellation upstream; prevent permit leaks and deadlocks when producers hold scarce resources while waiting for downstream capacity.
5. Specify deadlines, retry budgets, per-tenant fairness and observability; ensure retry storms cannot bypass admission limits.
6. Test bursts, sustained overload, stalled consumers, cancellation and recovery; measure accepted/completed/dropped work, queue ages and resource high-water marks.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/queue_model.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`research-queueing-theory`, `design-stream-processing`, `design-async-runtime`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
