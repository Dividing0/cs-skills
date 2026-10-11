# Domain guide: Design Async Runtime

## Pitfalls and boundaries

- Avoid assuming one OS poll API has the readiness semantics of another.
- Check for buffered readiness and stale registrations after descriptor reuse.
- Treat benchmark wins and API compatibility as separate acceptance criteria.

## Worked task

An event loop checks an empty ready queue then blocks in poll; another thread schedules a callback in that interval. Design the wakeup protocol.

### Required reasoning and evidence

1. Identify the lost-wakeup schedule.
2. Define ordering between queue publication and wakeup notification.
3. Test shutdown, callback reentrancy and sustained timer fairness.

## Claim to challenge

A timer callback always executes within 2 ms in ten runs. Claim a hard real-time deadline guarantee.

- Separate observed latency from worst-case guarantee.
- Specify workload and scheduler assumptions before stronger claims.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
