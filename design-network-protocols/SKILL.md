---
name: design-network-protocols
description: "Design robust application network protocols. Use for byte framing, incremental decoding, ordering, retries, idempotency, timeout semantics, version negotiation and interoperability under partial I/O."
---

# Design Network Protocols

## Scope and routing

Specify observable wire behavior and state. Use consensus analysis for replication protocols and threat modeling for attacker-oriented security design.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define transport assumptions, message schema, encoding, size limits, endianness, compatibility and authenticated peer/connection identity.
2. Design framing independent of transport packet boundaries; specify incremental parsing, partial writes, EOF and malformed-frame recovery.
3. Specify request IDs, ordering, retry/deduplication and acknowledgement semantics; treat timeout as uncertain completion where necessary.
4. Define flow control, concurrency, deadlines and resource limits; ensure reconnects cannot confuse stale replies with new requests.
5. Create golden wire vectors, independent encoder/decoder checks and state-machine examples for version negotiation.
6. Test split/coalesced reads, truncation, duplicates, reconnects and slow peers; document which guarantees rely on TCP, TLS or external storage.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/frame_decoder.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`build-parsers`, `design-backpressure`, `threat-model-systems`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
