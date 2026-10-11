"""Bounded complete-history linearizability checker for one read/write register."""

import argparse
import json
import math
from pathlib import Path


def check(history, max_ops=12, max_states=100000):
    operations = history["operations"]
    if max_ops < 0 or max_states <= 0:
        raise ValueError("invalid search limits")
    if len(operations) > max_ops:
        return {"status": "unknown", "reason": "operation limit"}
    ids = [o["id"] for o in operations]
    if any(not isinstance(i, str) for i in ids) or len(set(ids)) != len(ids):
        raise ValueError("operation IDs must be unique strings")
    for o in operations:
        if o.get("status", "ok") != "ok" or o.get("end") is None:
            return {
                "status": "unknown",
                "reason": "pending/failed operations require a richer completion model",
            }
        for key in ("start", "end"):
            v = o[key]
            if (
                isinstance(v, bool)
                or not isinstance(v, (int, float))
                or not math.isfinite(v)
            ):
                raise ValueError("timestamps must be finite numbers")
        if o["end"] < o["start"]:
            raise ValueError("completion precedes invocation")
        if o["op"] not in ("read", "write"):
            raise ValueError("only read/write operations are supported")
        if (
            o["op"] == "write"
            and "value" not in o
            or o["op"] == "read"
            and "result" not in o
        ):
            raise ValueError("missing write value/read result")
    # Strict precedence: equal timestamps do not resolve event order.
    before = [
        sum(
            1 << j for j, b in enumerate(operations) if j != i and b["end"] < a["start"]
        )
        for i, a in enumerate(operations)
    ]
    full = (1 << len(operations)) - 1
    seen, count = set(), 0

    def encode(v):
        return json.dumps(v, sort_keys=True, allow_nan=False, separators=(",", ":"))

    def search(mask, value, order):
        nonlocal count
        if mask == full:
            return order
        key = (mask, encode(value))
        if key in seen:
            return None
        count += 1
        if count > max_states:
            raise TimeoutError
        seen.add(key)
        for i, o in enumerate(operations):
            bit = 1 << i
            if mask & bit or before[i] & ~mask:
                continue
            if o["op"] == "read" and encode(o["result"]) != encode(value):
                continue
            updated = o["value"] if o["op"] == "write" else value
            found = search(mask | bit, updated, order + [o["id"]])
            if found is not None:
                return found
        return None

    try:
        witness = search(0, history["initial"], [])
    except TimeoutError:
        return {"status": "unknown", "reason": "search-state limit", "explored": count}
    if witness is not None:
        return {"status": "compatible", "witness": witness, "explored": count}
    return {
        "status": "violated",
        "explored": count,
        "scope": "this complete single-register history under supplied real-time timestamps",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("history", type=Path)
    p.add_argument("--max-ops", type=int, default=12)
    p.add_argument("--max-states", type=int, default=100000)
    a = p.parse_args()
    try:
        r = check(json.loads(a.history.read_text()), a.max_ops, a.max_states)
    except (ValueError, TypeError, KeyError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))
    return {"compatible": 0, "violated": 1, "unknown": 2}[r["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
