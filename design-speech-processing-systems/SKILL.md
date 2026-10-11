---
name: design-speech-processing-systems
description: "Design and evaluate streaming speech pipelines. Use for audio framing, sample rates, resampling, VAD/ASR/diarization integration, buffering, timestamps, latency budgets and telephony robustness."
---

# Design Speech Processing Systems

## Scope and routing

Specify system integration and streaming behavior. Use signal-processing skills for filter math and ML evaluation for model-quality experiments.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Specify sample rate, channels, sample representation, codec, clock, input domain and speech-quality/latency targets; preserve original source metadata.
2. Draw stage contracts for decoding, resampling, denoising, VAD, ASR and diarization with frame sizes, lookahead and timestamp mapping.
3. Budget buffering, compute, queueing, network and endpointing separately; report real-time factor and tail latency under the intended concurrency.
4. Define partial/final hypotheses, segment boundaries, state resets, speaker labels and behavior under packet loss, silence and reconnects.
5. Evaluate 8 kHz telephony separately from wideband input; test clipping, noisy speech, Ukrainian/Russian switching and enhancement-induced recognition changes when relevant.
6. Compare end-to-end quality and cost against a reproducible baseline; retain audio-aligned outputs and distinguish resampling from recovery of missing bandwidth.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/audio_budget.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

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

`develop-signal-processing`, `evaluate-machine-learning-systems`, `design-backpressure`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
