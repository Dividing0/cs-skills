---
name: design-information-retrieval
description: "Design and evaluate document retrieval and ranking systems. Use for inverted/vector indexes, lexical or hybrid search, query analysis, relevance judgments, Recall@k, MRR, nDCG and retrieval cost."
---

# Design Information Retrieval

## Scope and routing

Optimize retrieval against relevance judgments and deployment constraints. Use ML evaluation for training leakage and database skills for persistence mechanics.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define information needs, corpus boundaries, document granularity, freshness, language/tokenization and access-control filtering.
2. Create a reproducible lexical baseline and judged query set separated from tuning data; retain query strata and incomplete-judgment limitations.
3. Design candidate generation, filters and reranking; compare lexical, dense and hybrid options against index size, updates and latency budgets.
4. Choose metrics matched to the task, including recall for candidate generation and ranking quality for final lists; document gain and unjudged-document conventions.
5. Evaluate failures by query/document slices, duplicate documents, Ukrainian morphology, code switching and temporal drift when relevant.
6. Report paired quality/cost comparisons and examples; validate permission filters before ranking and make production freshness/index rebuild behavior explicit.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/ranking_metrics.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`evaluate-machine-learning-systems`, `analyze-database-internals`, `research-information-theory`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
