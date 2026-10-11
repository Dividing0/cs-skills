---
name: analyze-system-performance
description: "Diagnose end-to-end system bottlenecks using reproducible workload and resource evidence. Use for CPU profiles, allocation pressure, cache/TLB misses, syscalls, I/O saturation, throughput and latency tails."
---

# Analyze System Performance

## Scope and routing

Connect component measurements to user-visible service performance. Use language benchmark skills for local microbenchmarks and queueing theory for analytic models.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define the user-visible metric, workload distribution, concurrency, warmup, data size and hardware/software versions; capture a baseline before changes.
2. Measure wall time, CPU time, queue wait, allocations, I/O and saturation; attribute delays with profiles or traces while measuring instrumentation overhead.
3. Use a bottleneck hypothesis with a falsifiable prediction; distinguish CPU work from blocking, contention, backpressure and load-generator limitations.
4. Run paired or interleaved baseline/candidate trials with identical workloads; retain raw samples, variability, tail latencies and resource use.
5. Apply the smallest justified change; account for Amdahl limits, memory costs and effects on correctness or cancellation.
6. Report effect size and uncertainty at the measured operating point; stop when the target is met or evidence shows the bottleneck moved.

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

`benchmark-rust-criterion`, `benchmark-python`, `research-queueing-theory`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
