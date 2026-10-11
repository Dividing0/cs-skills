"""Calculate PCM sizes and additive nominal latency components; no percentile guarantee."""

import argparse
import json
import math
from pathlib import Path


def analyze(data):
    rate, channels, sample_bytes = (
        data[k] for k in ("sample_rate", "channels", "sample_bytes")
    )
    if any(
        isinstance(v, bool) or not isinstance(v, int) or v <= 0
        for v in (rate, channels, sample_bytes)
    ):
        raise ValueError("sample_rate/channels/sample_bytes must be positive integers")
    frame_ms = data["frame_ms"]
    if (
        isinstance(frame_ms, bool)
        or not isinstance(frame_ms, (int, float))
        or not math.isfinite(frame_ms)
        or frame_ms <= 0
    ):
        raise ValueError("frame_ms must be positive finite number")
    components = {"initial_frame_ms": frame_ms}
    for i, stage in enumerate(data.get("stages", [])):
        for field in (
            "buffer_ms",
            "lookahead_ms",
            "processing_ms",
            "queue_ms",
            "network_ms",
            "endpoint_ms",
        ):
            value = stage.get(field, 0)
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or value < 0
            ):
                raise ValueError("latency components must be finite and nonnegative")
            components[f"{i}:{stage['name']}:{field}"] = value
    samples = rate * frame_ms / 1000
    return {
        "frame_samples_per_channel": samples,
        "integral_frame": samples.is_integer(),
        "frame_payload_bytes": samples * channels * sample_bytes,
        "pcm_bytes_per_second": rate * channels * sample_bytes,
        "source_nyquist_hz": rate / 2,
        "nominal_additive_latency_ms": sum(components.values()),
        "components": components,
        "scope": "serial additive budget; overlapping stages may change latency; sums of p95s are not end-to-end p95; no restored bandwidth from upsampling",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    a = p.parse_args()
    try:
        r = analyze(json.loads(a.input.read_text()))
    except (ValueError, TypeError, KeyError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
