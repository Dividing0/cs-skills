---
name: design-robotics-software
description: "Design robotics and navigation software with explicit time and frame semantics. Use for sensor interfaces, transforms, synchronization, calibration, estimator integration, replay and simulation/real-device validation."
---

# Design Robotics Software

## Scope and routing

Specify robotics software contracts and reproducibility. Use control/state-estimation skills for estimator mathematics and real-time skills for scheduling.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define sensor rates, units, coordinate frames, handedness, transform direction, clock domains and calibration provenance.
2. Specify timestamp semantics, synchronization, interpolation and bounded latency; distinguish measurement time from receipt time.
3. Define estimator inputs, covariance/noise assumptions, initialization, invalid-data handling and reset behavior without silently changing mathematical models.
4. Design recording/replay with schema versions, calibration and clock metadata so the same input yields explainable outputs.
5. Test known transforms, stationary/moving trajectories, dropped/reordered sensors and restart; compare residuals and reference trajectories with aligned time.
6. Report simulation, replay and hardware results separately; retain coordinate/time conventions and unresolved observability or calibration limitations.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/enu_ned.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`develop-control-state-estimation`, `design-real-time-systems`, `design-stream-processing`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
