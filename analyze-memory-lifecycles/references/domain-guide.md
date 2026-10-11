# Domain guide: Analyze Memory Lifecycles

## Pitfalls and boundaries

- Keep active timers ahead of cancelled timers so queue-head cleanup cannot hide retention.
- Use several garbage-collection phases only when cycles require them; document whether release is immediate or eventual.
- Do not log entire referrer graphs containing application secrets; reduce evidence to relevant types and ownership edges.

## Worked task

A timer heap retains 20000 cancelled callbacks behind an earlier active timer. Each callback owns a payload and a context variable references another object. Diagnose release semantics.

### Required reasoning and evidence

1. Construct weak-reference observations for callback, args and context payloads.
2. Distinguish queue bookkeeping from Python payload ownership.
3. Test repeated cancellation and reentrant finalization.

## Claim to challenge

After all weak references die, RSS remains high. Declare the library has a leak and force allocator replacement.

- Reject the unsupported leak conclusion.
- Investigate allocator residency/native allocations and repeat workload measurements.

## Review rubric

For an immediate cancellation-release contract, keep old callback/argument/context references alive locally while publishing the cancelled state, clearing all owned payload slots and updating cancellation accounting once. Only then drop the old references: decref may execute a finalizer that calls cancel, closes the loop or schedules work. Test what that finalizer observes, not only the eventual garbage-collection count. Retain handles and heap bookkeeping during the test so pruning cannot make it pass accidentally. Distinguish the requested contract from each reference runtime's observed context-release behavior; do not assume all asyncio-shaped implementations clear context on cancel.

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
