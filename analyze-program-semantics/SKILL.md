---
name: analyze-program-semantics
description: "Define and reason about program meaning and behavior preservation. Use for small/big-step semantics, evaluation order, substitution, exceptions, effects, divergence and observational equivalence."
---

# Analyze Program Semantics

## Scope and routing

Specify program meaning before transformations. Use compiler construction for implementation and type-system design for static typing guarantees.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define syntax, values, environments/stores, evaluation strategy and observable effects, including exceptions, I/O and termination.
2. Write inference/transition rules with side conditions; handle binding and capture-avoiding substitution explicitly.
3. Trace disputed programs under those rules; distinguish stuck states, normal termination, exceptions and divergence.
4. State the intended equivalence or refinement and admissible contexts; value equality alone is insufficient when effects differ.
5. Check a transformation through simulation or an equivalent semantic argument; preserve evaluation order and defined/undefined behavior assumptions.
6. Use executable interpreters or differential checks for counterexamples, keeping experimental evidence separate from universal equivalence proofs.

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

`design-type-systems`, `build-compilers-and-interpreters`, `check-math-equivalence`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
