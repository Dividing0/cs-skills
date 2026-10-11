---
name: design-human-computer-interaction
description: "Design and evaluate task-focused interfaces and interaction flows. Use for user journeys, information architecture, responsive layouts, accessibility, error recovery and usability studies."
---

# Design Human Computer Interaction

## Scope and routing

Specify and validate interaction outcomes. Use framework/UI skills for implementation and threat modeling for sensitive actions or trust boundaries.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Identify users, tasks, environment, device constraints, accessibility needs and the existing evidence about usability failures.
2. Map task flows, information hierarchy and states including loading, empty, error, offline and destructive/undoable actions.
3. Design responsive behavior by available space and input modality; preserve focus, reading order and state across layout changes.
4. Check keyboard/screen-reader operation, contrast, labels and target sizes against applicable WCAG criteria; include platform-specific requirements.
5. Define concrete usability tasks and success/error/time measures; distinguish expert inspection, automated checks and observed user sessions.
6. Deliver annotated flows/prototypes and prioritized findings with validation evidence, unresolved assumptions and implementation acceptance criteria.

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

`threat-model-systems`, `evaluate-practical-feasibility`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
