"""Offline exact tumbling-window oracle; no watermark or online recovery semantics."""

import argparse
import json
import math
from collections import Counter
from pathlib import Path


def count_windows(events, width, deduplicate=False):
    if not math.isfinite(width) or width <= 0:
        raise ValueError("width must be finite and positive")
    seen, counts = {}, Counter()
    for event in events:
        stamp = event["time"]
        if (
            isinstance(stamp, bool)
            or not isinstance(stamp, (int, float))
            or not math.isfinite(stamp)
        ):
            raise ValueError("event time must be finite number")
        key = event["key"]
        if not isinstance(key, str):
            raise ValueError("keys must be strings")
        if deduplicate:
            identity = event["id"]
            if not isinstance(identity, str):
                raise ValueError("IDs must be strings")
            signature = json.dumps(event, sort_keys=True, allow_nan=False)
            if identity in seen:
                if seen[identity] != signature:
                    raise ValueError("same event ID has conflicting payloads")
                continue
            seen[identity] = signature
        start = math.floor(stamp / width) * width
        counts[(key, start)] += 1
    return {
        "windows": [
            {"key": k, "start": s, "end": s + width, "count": n}
            for (k, s), n in sorted(counts.items())
        ],
        "semantics": "[start,end), origin0; exact offline; deduplication is global over this input only",
        "deduplicate": deduplicate,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--width", type=float, required=True)
    p.add_argument("--deduplicate", action="store_true")
    a = p.parse_args()
    try:
        r = count_windows(json.loads(a.input.read_text()), a.width, a.deduplicate)
    except (ValueError, TypeError, KeyError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
