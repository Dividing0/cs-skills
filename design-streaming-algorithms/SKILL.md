---
name: design-streaming-algorithms
description: "Design bounded-memory algorithms over data streams. Use for frequency sketches, approximate distinct counts, reservoir sampling, mergeability, adversarial streams and explicit error/confidence guarantees."
---

# Design Streaming Algorithms

## Scope and routing

Choose streaming approximations and analyze their guarantees. Use stream-processing design for windows, recovery and infrastructure semantics.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define stream model, updates/deletions, query, window, memory budget, adversarial assumptions and acceptable error/probability.
2. Compare exact bounded alternatives with sketches or sampling; identify whether estimates overestimate, underestimate or have two-sided error.
3. Derive parameters from a named guarantee and its assumptions; specify hash independence, random seed behavior and merge compatibility.
4. Implement an exact oracle for tractable prefixes; test skew, duplicates, empty streams, heavy tails and reordered or merged partitions.
5. Measure empirical error across independent random seeds and realistic distributions while retaining the theoretical guarantee separately.
6. Document unsupported deletion/window operations, counter overflow and serialization/version compatibility before production use.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/count_min.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`research-probability-theory`, `design-stream-processing`, `compute-with-monte-carlo`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
