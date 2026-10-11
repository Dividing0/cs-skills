---
name: build-compilers-and-interpreters
description: "Build language execution pipelines with preserved semantics. Use for AST/IR design, binding, lowering, interpreters, optimization passes, code generation, runtime interfaces and differential validation."
---

# Build Compilers And Interpreters

## Scope and routing

Coordinate executable language implementation. Use parser construction for front ends and program semantics/type systems for language definitions.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define language semantics, integer/float rules, evaluation order, exceptions, target ABI and intended supported subset.
2. Separate parsing, name resolution, typing and lowering; retain source locations and explicit invariants for every IR stage.
3. Implement a small reference interpreter before optimizations, including scope, closures, lifetime and runtime error behavior.
4. Specify each pass's preconditions and preservation obligation; account for overflow, aliasing, exceptions and undefined behavior.
5. Validate IR after each pass and compare optimized/unoptimized/reference executions on generated well-defined programs.
6. Test target calling convention, layout and runtime interfaces; measure performance only after semantic equivalence checks and record unsupported features.

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

`build-parsers`, `analyze-program-semantics`, `design-type-systems`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
