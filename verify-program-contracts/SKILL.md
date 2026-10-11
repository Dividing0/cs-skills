---
name: verify-program-contracts
description: "Specify and verify code contracts and invariants with explicit assumptions. Use for pre/postconditions, frame conditions, loop invariants, termination measures, Hoare-style obligations and counterexamples."
---

# Verify Program Contracts

## Scope and routing

Translate a code claim into proof obligations. Delegate SMT execution, bounded Rust/C verification and proof-assistant implementation to existing tool-specific skills.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Identify function behavior, legal inputs, state footprint, exceptional behavior, arithmetic model and partial versus total correctness goals.
2. Write preconditions, postconditions and frame conditions; check they express the user's intended behavior rather than a weaker surrogate.
3. Derive loop/recursive invariants and a decreasing well-founded variant if termination is claimed; separate initialization, preservation and exit obligations.
4. Encode obligations in an appropriate verifier with explicit heap/alias/environment assumptions and tool versions.
5. Inspect counterexamples for genuine defects, specification gaps or abstraction artifacts; avoid resolving failures by silently strengthening preconditions.
6. Report proved obligations, assumed axioms, bounded checks and unknown/timeouts separately; add executable regressions for concrete counterexamples.

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

`solve-with-z3`, `verify-rust-kani`, `verify-c-formal`, `prove-with-lean4`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
