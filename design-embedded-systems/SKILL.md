---
name: design-embedded-systems
description: "Design resource-constrained embedded software and hardware interfaces. Use for RAM/flash/energy budgets, interrupts, DMA, peripheral timing, watchdogs, boot/update paths and hardware-in-the-loop validation."
---

# Design Embedded Systems

## Scope and routing

Specify device constraints and peripheral contracts. Use real-time analysis for schedulability and threat modeling for firmware security boundaries.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Record MCU/SoC, clock, memory map, peripherals, power modes, toolchain and environmental constraints from the actual device documentation.
2. Budget static/dynamic memory, stack per context, buffers, code size and worst-case work; include ISR and DMA ownership.
3. Define interrupt/task communication, critical sections and ring-buffer overflow behavior; use platform memory/cache ordering for DMA coherency.
4. Specify startup, watchdog, brownout and power-fail behavior; design updates with version validation and recoverable interruption states.
5. Prototype against mocked registers where useful but validate timing and peripheral behavior on hardware or an explicitly limited simulator.
6. Measure high-water memory, energy and timing under stress; report device evidence separately from host tests and simulation.

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

`design-real-time-systems`, `analyze-memory-models`, `threat-model-systems`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
