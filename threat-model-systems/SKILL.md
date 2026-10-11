---
name: threat-model-systems
description: "Create evidence-based system threat models within authorized scope. Use for assets, data flows, trust boundaries, attacker capabilities, abuse cases, mitigation priorities and security acceptance tests."
---

# Threat Model Systems

## Scope and routing

Model threats at system boundaries. Use language security audits for concrete code defects and cryptography research for mathematical claims.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define scope, protected assets, business invariants, deployment, actors and existing security controls; separate facts from architecture assumptions.
2. Draw data flows and trust boundaries including dependencies, identity providers, uploads, admin paths and storage.
3. Enumerate attacker capabilities and abuse cases with prerequisites, affected assets and plausible impact; use STRIDE or another method as a prompt, not as proof.
4. Rank threats using evidence and transparent likelihood/impact assumptions; avoid invented precise probabilities and generic unprioritized lists.
5. Specify mitigations and verification tasks tied to each threat, including authentication/authorization, tenant isolation, input limits and recovery.
6. Produce residual-risk decisions and testable acceptance criteria; keep testing inside authorized environments and preserve sensitive-data boundaries.

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

`audit-python-security`, `audit-rust-security`, `design-network-protocols`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
