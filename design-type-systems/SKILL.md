---
name: design-type-systems
description: "Design and evaluate type systems with explicit static and dynamic rules. Use for type inference, polymorphism, subtyping, effects, ownership, progress/preservation and soundness counterexamples."
---

# Design Type Systems

## Scope and routing

Define a language-level static discipline. Use review-language API skills for ordinary API idioms and program-semantics analysis for dynamic behavior.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify syntax, values, operational semantics, typing judgments and the safety property the type system intends to establish.
2. Write typing rules with contexts and side conditions; separate checking, inference, subtyping and definitional equality.
3. For inference define constraints, unification, occurs checks, generalization and instantiation; treat mutable references with a justified value restriction.
4. Examine variance, effect propagation, ownership/borrowing and escape rules against runtime behaviors rather than intuition alone.
5. Prove or audit progress and preservation with supporting substitution/canonical-form lemmas; state excluded runtime errors.
6. Build positive/negative programs and minimal unsoundness witnesses; compare checker results with a reference evaluator or proof assistant where available.

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

`analyze-program-semantics`, `research-mathematical-logic`, `prove-with-lean4`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
