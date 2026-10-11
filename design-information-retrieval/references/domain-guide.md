# Domain guide: Design Information Retrieval

## Pitfalls and boundaries

- Vector similarity is not a substitute for a relevance judgment.
- Keep tuning queries separate from final evaluation and group near-duplicate queries/documents.
- Do not interpret unjudged documents as proven irrelevant without documenting that convention.

## Worked task

Build search over Ukrainian court decisions with date filters, access rules and a 200 ms budget. Compare BM25 and hybrid retrieval.

### Required reasoning and evidence

1. Establish judged queries and a baseline.
2. Evaluate recall and final ranking separately.
3. Measure freshness, ACL correctness and latency.

## Claim to challenge

A dense retriever scores better on the same queries used to tune weights. Declare a production improvement.

- Flag evaluation contamination.
- Require held-out queries and cost/latency measurements.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
