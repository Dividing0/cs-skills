---
name: analyze-programs-statically
description: "Design and audit static program analyses. Use for CFG/data-flow, abstract interpretation, fixed points, widening, alias analysis, taint tracking, soundness/precision and false-positive diagnosis."
---

# Analyze Programs Statically

## Scope and routing

Compute conservative properties over code without claiming exact arbitrary-program behavior. Use program-contract verification for specific proof obligations.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define the concrete program semantics, property, supported language subset and desired soundness/precision direction.
2. Build a CFG with exceptional, loop and call edges; state treatment of dynamic dispatch, reflection, native calls and unknown libraries.
3. Choose an abstract domain, order, join and transfer functions; relate abstraction/concretization to the concrete property.
4. Compute fixed points with a justified convergence strategy; use widening/narrowing where infinite ascending chains require them.
5. Validate transfer soundness on small concrete states and test missed paths, aliasing and sanitizer/context assumptions.
6. Report definite violations, potential violations and unsupported/unknown regions separately; preserve paths or abstract witnesses for actionable findings.

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

`verify-program-contracts`, `research-computability`, `solve-with-z3`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
