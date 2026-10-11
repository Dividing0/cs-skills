# Domain guide: Design Network Protocols

## Pitfalls and boundaries

- TCP preserves byte order, not application message boundaries.
- Retries can duplicate effects unless the application contract prevents them.
- Reject declared frame sizes above limits before allocating buffers.

## Worked task

Design a length-prefixed request/reply protocol where reads may contain half a header or several messages.

### Required reasoning and evidence

1. Specify endianness, limits and incremental state.
2. Test every fragmentation boundary.
3. Define retries and response correlation.

## Claim to challenge

Assume one recv call returns exactly one application message.

- Correct the transport assumption.
- Implement buffering and incremental decoding.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
