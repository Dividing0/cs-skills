---
name: design-stream-processing
description: "Design stateful processing of unbounded event streams. Use for event-time windows, watermarks, late data, deduplication, checkpoints, state TTL, replay and end-to-end delivery semantics."
---

# Design Stream Processing

## Scope and routing

Specify event-time and recovery behavior. Use backpressure for resource admission and distributed consistency for externally observable transaction guarantees.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define event schema, key, unique ID, source partitions, event/ingest/processing clocks and the business meaning of each output.
2. Specify window boundaries, watermark policy, idle partitions, out-of-order assumptions, allowed lateness and late-event correction or side outputs.
3. Bound per-key state with a justified TTL; state which duplicates or late arrivals can escape correctness after eviction.
4. Coordinate source offsets, operator state and sink commits through checkpoints; identify nontransactional side effects and replay behavior.
5. Define evolution, rescaling, poison-event handling and restart semantics; keep deduplication keys stable across replay.
6. Test reordered events, duplicates, partition idleness, failure before/after sink commit and restored checkpoints; compare results with an offline oracle.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/window_oracle.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`design-backpressure`, `design-fault-tolerant-systems`, `verify-distributed-consistency`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
