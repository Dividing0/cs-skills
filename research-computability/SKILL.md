---
name: research-computability
description: "Investigate decidability, recognizability and computability with precise models and reductions. Use for halting-style claims, semidecision procedures, Rice theorem applicability and limits of static analysis."
---

# Research Computability

## Scope and routing

Study whether a problem can be solved at all. Use research-mathematical-complexity for resource bounds and hardness of decidable problems.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define finite encodings, legal inputs, output and whether the claim concerns a decider, recognizer, search procedure or partial function.
2. State the computation model and effective access to inputs; separate arbitrary programs from bounded finite-state restrictions.
3. Choose constructive algorithms, diagonalization or a reduction from an established undecidable problem; state the source theorem precisely.
4. Make the transformation effective and total; prove the yes/no equivalence in the correct direction and check malformed-input handling.
5. Check semantic-property hypotheses before invoking Rice's theorem; syntactic properties and trivial properties need separate reasoning.
6. Record the conclusion with scope, recognizability/co-recognizability where established and practical consequences for bounded approximations.

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

`research-mathematical-complexity`, `research-mathematical-logic`, `analyze-programs-statically`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
