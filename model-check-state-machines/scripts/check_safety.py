"""Explore an explicit finite graph for forbidden states; no temporal liveness proof."""

import argparse
import json
from collections import deque
from pathlib import Path


def check(model, limit=100000):
    states = model["states"]
    if (
        not isinstance(states, list)
        or any(not isinstance(s, str) for s in states)
        or len(set(states)) != len(states)
    ):
        raise ValueError("states must be unique strings")
    states = set(states)
    initial, forbidden = model["initial"], set(model["forbidden"])
    if not initial or not set(initial) <= states or not forbidden <= states:
        raise ValueError(
            "initial/forbidden states must be declared, and initial must not be empty"
        )
    if limit <= 0:
        raise ValueError("limit must be positive")
    edges = {s: [] for s in states}
    for edge in model["transitions"]:
        source, target = edge["from"], edge["to"]
        if source not in states or target not in states:
            raise ValueError("transition mentions undeclared state")
        edges[source].append((target, edge.get("label", "step")))
    queue = deque((s, [{"state": s}]) for s in initial)
    seen, terminals = set(), []
    while queue:
        current, path = queue.popleft()
        if current in seen:
            continue
        if len(seen) >= limit:
            return {"status": "unknown", "reason": "state limit", "visited": len(seen)}
        seen.add(current)
        if current in forbidden:
            return {"status": "violated", "trace": path, "visited": len(seen)}
        if not edges[current]:
            terminals.append(current)
        for target, label in edges[current]:
            if target not in seen:
                queue.append((target, path + [{"label": label, "state": target}]))
    return {
        "status": "holds_in_supplied_finite_graph",
        "visited": len(seen),
        "terminal_states": sorted(terminals),
        "liveness": "not checked",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("model", type=Path)
    p.add_argument("--limit", type=int, default=100000)
    a = p.parse_args()
    try:
        result = check(json.loads(a.model.read_text()), a.limit)
    except (ValueError, KeyError, TypeError) as e:
        p.error(str(e))
    print(json.dumps(result, indent=2))
    return {"holds_in_supplied_finite_graph": 0, "violated": 1, "unknown": 2}[
        result["status"]
    ]


if __name__ == "__main__":
    raise SystemExit(main())
