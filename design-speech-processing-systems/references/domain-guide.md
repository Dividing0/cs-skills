# Domain guide: Design Speech Processing Systems

## Pitfalls and boundaries

- Upsampling 8 kHz to 16 kHz does not restore lost high-frequency information.
- Cleaner-sounding enhancement can increase WER or erase speech.
- Model lookahead and endpoint delay can dominate compute latency.

## Worked task

Design an 8 kHz Ukrainian telephone pipeline with denoising, VAD and streaming ASR under a 300 ms partial-result budget.

### Required reasoning and evidence

1. Account for lookahead, framing and queue delays.
2. Keep timestamps through resampling.
3. Evaluate WER and latency on telephone recordings.

## Claim to challenge

Convert 8 kHz audio to 48 kHz and call it maximum-quality restored audio.

- Distinguish representation conversion from recovered information.
- Preserve provenance and evaluate downstream quality.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
