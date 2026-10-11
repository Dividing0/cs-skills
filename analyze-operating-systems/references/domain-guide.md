# Domain guide: Analyze Operating Systems

## Pitfalls and boundaries

- RSS, virtual address size and page-cache usage describe different resources.
- Increasing descriptor/thread limits can hide a lifecycle bug.
- Linux findings do not establish Windows IOCP or macOS kqueue behavior.

## Worked task

A server fails with cannot start new thread at high load although CPU is moderate. Diagnose limits and lifecycle.

### Required reasoning and evidence

1. Inspect process/cgroup thread limits and stack memory.
2. Trace thread ownership and growth.
3. Test recovery and bounded spawning.

## Claim to challenge

Raise every OS limit and call the resource problem fixed.

- Identify root cause and resource budget.
- Measure bounded steady-state behavior.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
