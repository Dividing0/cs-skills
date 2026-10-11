# Domain guide: Analyze Consensus Protocols

## Pitfalls and boundaries

- FLP addresses deterministic consensus under particular asynchronous assumptions; it does not make practical protocols universally unusable.
- Raft majority replication alone is insufficient to commit arbitrary older-term entries by counting replicas.
- Lease-based reads require explicit timing/clock assumptions.

## Worked task

Review a Raft implementation that commits an older-term entry solely because it appears on a majority after a new election.

### Required reasoning and evidence

1. Apply the exact current-term commit rule.
2. Trace a leader-change counterexample if applicable.
3. Distinguish commit safety from eventual progress.

## Claim to challenge

A timeout has expired, so the old leader is certainly dead and cannot serve stale reads.

- Reject failure certainty from timeout.
- Specify read authority/quorum or justified lease conditions.

## Review rubric

Distinguish intact-disk process crashes from permanent replica storage loss. In a three-voter majority protocol, leader plus one durable follower can provide a commit quorum only under the actual election/commit rules. It neither provides progress with one surviving voter nor preserves data after destruction of both write-bearing copies before the third copy exists. A stronger durability target needs a stronger acknowledgement/storage contract; a stronger availability target needs a sufficient communicating quorum.

For linearizable reads prefer the selected protocol's quorum authority/read barrier and applied-index condition unless a specific proved lease construction is available. A heartbeat timestamp is not a lease proof. For leases identify grant duration measured at grantors, requester validity interval, bounded drift/clock behavior, delayed renewals, process pauses/restarts, election exclusion and membership transitions. Derive conservative timing inequalities from that construction; do not invent a universal 30-second rule. Test both clock-bound edges and behavior outside supported bounds.

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
