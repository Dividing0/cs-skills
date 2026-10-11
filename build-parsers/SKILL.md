---
name: build-parsers
description: "Implement robust parsers with explicit grammar and diagnostics. Use for lexers, recursive descent, Pratt/LR/PEG parsing, ASTs, precedence, ambiguity, error recovery, incremental input and parser fuzzing."
---

# Build Parsers

## Scope and routing

Build concrete parsing behavior. Use automata/grammar design for language-theoretic properties and compiler construction for later semantic phases.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify tokenization, encoding, grammar, whitespace/comments, resource limits and the AST or event output contract.
2. Select a parsing strategy matched to ambiguity, left recursion, precedence and streaming/incremental requirements.
3. Track source spans and define precedence/associativity, full-input consumption and end-of-input behavior explicitly.
4. Implement diagnostics and bounded recovery without infinite loops; cap nesting, token length and backtracking where untrusted input can exhaust resources.
5. Test grammar-derived valid examples, invalid truncations, unicode, precedence and recovery; compare round trips or a reference parser where meaningful.
6. Fuzz input and retain minimized crashes/hangs; report accepted-language deviations and measured complexity under pathological inputs.

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

`design-automata-and-grammars`, `test-python-correctness`, `build-compilers-and-interpreters`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
