"""Compute work/span for a weighted finite DAG under an ideal scheduler model."""

import argparse
import json
import math
from pathlib import Path


def analyze(tasks, processors=1):
    if processors <= 0:
        raise ValueError("processors must be positive")
    by_id = {t["id"]: t for t in tasks}
    if len(by_id) != len(tasks) or any(not isinstance(i, str) for i in by_id):
        raise ValueError("task IDs must be unique strings")
    for t in tasks:
        c = t["cost"]
        if (
            isinstance(c, bool)
            or not isinstance(c, (int, float))
            or not math.isfinite(c)
            or c < 0
        ):
            raise ValueError("costs must be finite nonnegative numbers")
        if not set(t.get("deps", [])) <= set(by_id):
            raise ValueError("unknown dependency")
    finish = {}
    pending = set(by_id)
    while pending:
        ready = sorted(
            i for i in pending if set(by_id[i].get("deps", [])) <= set(finish)
        )
        if not ready:
            raise ValueError("dependency cycle")
        for i in ready:
            t = by_id[i]
            finish[i] = t["cost"] + max(
                (finish[d] for d in t.get("deps", [])), default=0
            )
        pending.difference_update(ready)
    work = sum(t["cost"] for t in tasks)
    span = max(finish.values(), default=0)
    return {
        "work": work,
        "span": span,
        "processors": processors,
        "ideal_time_lower_bound": max(work / processors, span),
        "ideal_greedy_time_upper_bound": work / processors + span,
        "average_parallelism": work / span if span else None,
        "assumptions": "independent processor costs, dependency DAG, zero overhead/communication; not a measured runtime prediction",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--processors", type=int, default=1)
    a = p.parse_args()
    try:
        r = analyze(json.loads(a.input.read_text()), a.processors)
    except (ValueError, TypeError, KeyError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
