---
name: design-automata-and-grammars
description: "Construct and analyze finite automata and formal grammars. Use for DFA/NFA conversion, epsilon closure, regular-language equivalence, minimization, context-free grammars, ambiguity and recognizers."
---

# Design Automata And Grammars

## Scope and routing

Work on language models and recognition properties. Use build-parsers for parser implementation, diagnostics and concrete token streams.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify alphabet, token versus character interpretation, accepted language, empty word behavior and the required automaton/grammar class.
2. Construct transitions or production rules with explicit initial/accepting states; make missing transitions and epsilon handling unambiguous.
3. For NFA conversion compute epsilon closure before/after symbol moves; distinguish subset construction from DFA minimization.
4. Prove the recognized-language correspondence through state meanings or derivations; check representative positive and negative boundary strings.
5. Compare DFAs via product reachability, retaining a shortest distinguishing word; complete partial DFAs with rejecting sink behavior.
6. For grammars inspect ambiguity, left recursion and precedence; bounded enumeration gives counterexamples but cannot prove arbitrary grammar unambiguity.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/compare_dfa.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`build-parsers`, `research-computability`, `model-check-state-machines`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
