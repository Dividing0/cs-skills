---
name: design-data-structures
description: "Design specialized data structures against workload, invariants and resource costs. Use for indexing, persistent structures, concurrent structures, amortized bounds, cache locality and model-based operation testing."
---

# Design Data Structures

## Scope and routing

Focus on data representation and operation contracts. Use general algorithm design for whole-problem selection and memory-model analysis for atomic/reclamation proofs.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify operations, key/value domains, ordering/duplicate policy, ownership, mutation and iterator validity; characterize workload and resource constraints.
2. Compare candidate representations using operation mix, locality, allocation, persistence and concurrency requirements.
3. Write representation invariants and identify the point each mutating operation restores them; define failure/rollback behavior.
4. Derive worst-case, amortized or expected bounds with stated cost models and assumptions; include resize and reclamation costs.
5. Test generated operation sequences against a simple reference model, including empty/full states, duplicates, deletion and invalid iterators.
6. Benchmark representative sizes/distributions and report memory overhead; keep correctness evidence independent from timing evidence.

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

`design-and-implement-algorithms`, `analyze-memory-models`, `analyze-memory-lifecycles`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
