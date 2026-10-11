---
name: design-computer-graphics
description: "Design graphics pipelines and geometric representations with explicit conventions. Use for transforms, camera projection, clipping, rendering, lighting, precision, GPU resources and visual correctness tests."
---

# Design Computer Graphics

## Scope and routing

Specify rendering and geometric computation. Use computational-geometry research for geometric proofs and framework skills for engine-specific implementation.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define geometry, coordinate handedness, units, row/column-vector convention, transform order, camera and clip/depth ranges.
2. Specify model/view/projection stages and homogeneous division; check inverse/transposed transforms for normals under nonuniform scale.
3. Design clipping, depth testing, blending and color-space conversion; distinguish linear-light computations from encoded display values.
4. Budget geometry/textures, draw calls, shader work and resource lifetimes; identify CPU/GPU synchronization costs.
5. Validate known points, transform round trips, occlusion and edge cases before judging screenshots; use tolerance matched to precision.
6. Report correctness and performance with renderer/API/hardware conditions; preserve deterministic test scenes and disclose approximation/artifact limits.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/transform_points.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`research-computational-geometry`, `research-linear-algebra`, `analyze-computer-architecture`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
