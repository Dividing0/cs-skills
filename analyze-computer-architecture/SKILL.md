---
name: analyze-computer-architecture
description: "Analyze how hardware organization affects measured code behavior. Use for caches, TLBs, NUMA, memory bandwidth, SIMD, branch prediction, false sharing and instruction/data locality."
---

# Analyze Computer Architecture

## Scope and routing

Tie hardware hypotheses to measurements. Use assembly skills for instruction-level inspection and memory-model analysis for correctness/order guarantees.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Record CPU/SoC, topology, cache/TLB organization, ISA features, memory channels, compiler flags and process affinity.
2. Map the workload to compute, bandwidth, latency, branches and data movement; estimate working-set and arithmetic-intensity regimes.
3. Use supported counters/profiles and controlled size/stride sweeps; separate cache misses, page faults and allocator placement effects.
4. Investigate false sharing, NUMA placement and cross-core traffic with explicit data-layout hypotheses.
5. Check vectorization, alignment, alias assumptions and tail handling against correctness requirements before changing layout or ISA paths.
6. Report measured effects across relevant sizes and core counts; avoid porting one-machine conclusions without hardware-specific validation.

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

`analyze-rust-assembly`, `analyze-c-assembly`, `analyze-memory-models`, `analyze-system-performance`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
