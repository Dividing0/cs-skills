---
name: design-real-time-systems
description: "Design timing-constrained systems with explicit deadline assumptions. Use for periodic/sporadic tasks, WCET, jitter, response-time analysis, scheduling, priority inversion and deadline-miss handling."
---

# Design Real Time Systems

## Scope and routing

Analyze deadlines under a stated scheduler and workload model. Use performance analysis for measurements that do not establish hard worst-case guarantees.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Classify hard/firm/soft deadlines and specify task periods, arrivals, deadlines, execution bounds, blocking and allowed misses.
2. Identify scheduler, preemption, cores, priorities and resource sharing; separate execution, release jitter and interference.
3. Choose a schedulability test valid for those assumptions; account for blocking, context-switch overhead and interrupt interference.
4. Derive response-time or demand bounds and check convergence/feasibility; label measured execution maxima as measurements unless WCET is justified.
5. Design overrun, watchdog, degraded-mode and priority-inversion handling with explicit safety and recovery behavior.
6. Validate traces under representative/adversarial load while reporting the gap between empirical latency and analytic deadline guarantees.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/implicit_deadlines.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`research-queueing-theory`, `analyze-operating-systems`, `analyze-system-performance`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
