# Domain guide: Analyze Computer Architecture

## Pitfalls and boundaries

- Counter events may be multiplexed, unavailable or architecture-specific.
- Cache-line padding can increase footprint enough to reverse a local win.
- Theoretical peak FLOPS do not predict memory-bound service throughput.

## Worked task

A per-thread counter array slows down as cores increase. Investigate false sharing versus bandwidth saturation.

### Required reasoning and evidence

1. Specify layout/cache-line hypotheses.
2. Compare padding and privatized reduction.
3. Measure footprint and coherence evidence.

## Claim to challenge

An SoC has twice the peak FLOPS, so an irregular graph workload must run twice as fast.

- Examine bandwidth, latency and parallelism.
- Reject an unsupported peak-to-workload extrapolation.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
