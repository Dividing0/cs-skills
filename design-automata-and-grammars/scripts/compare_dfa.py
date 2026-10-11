"""Compare two finite DFAs; return a shortest distinguishing token sequence."""

import argparse
import json
from collections import deque
from pathlib import Path


def compare(left, right, limit=100000):
    if limit <= 0:
        raise ValueError("limit must be positive")
    for d in (left, right):
        if any(not isinstance(s, str) for s in d["states"]) or len(
            set(d["states"])
        ) != len(d["states"]):
            raise ValueError("states must be unique strings")
        if d["start"] not in d["states"] or not set(d["accept"]) <= set(d["states"]):
            raise ValueError("undeclared start or accepting state")
        if any(not isinstance(t, str) for t in d["alphabet"]):
            raise ValueError("alphabet tokens must be strings")
        for s, transitions in d["transitions"].items():
            if (
                s not in d["states"]
                or not set(transitions) <= set(d["alphabet"])
                or not set(transitions.values()) <= set(d["states"])
            ):
                raise ValueError("undeclared transition")
    if set(left["alphabet"]) != set(right["alphabet"]):
        raise ValueError("alphabets must match; align them explicitly first")
    alphabet = sorted(set(left["alphabet"]))
    queue = deque([(left["start"], right["start"], [])])
    seen = set()
    while queue:
        a, b, word = queue.popleft()
        if (a, b) in seen:
            continue
        if len(seen) >= limit:
            return {
                "status": "unknown",
                "reason": "product-state limit",
                "visited": len(seen),
            }
        seen.add((a, b))
        if (a in left["accept"]) != (b in right["accept"]):
            return {
                "status": "different",
                "word": word,
                "left_accepts": a in left["accept"],
                "right_accepts": b in right["accept"],
            }
        for token in alphabet:
            na = left["transitions"].get(a, {}).get(token)
            nb = right["transitions"].get(b, {}).get(token)
            queue.append((na, nb, word + [token]))
    return {
        "status": "equivalent",
        "visited": len(seen),
        "missing_transition_policy": "rejecting sink",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("pair", type=Path)
    p.add_argument("--limit", type=int, default=100000)
    a = p.parse_args()
    try:
        pair = json.loads(a.pair.read_text())
        r = compare(pair["left"], pair["right"], a.limit)
    except (ValueError, KeyError, TypeError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))
    return {"equivalent": 0, "different": 1, "unknown": 2}[r["status"]]


if __name__ == "__main__":
    raise SystemExit(main())
