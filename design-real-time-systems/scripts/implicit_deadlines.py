"""Analytic sufficient conditions for classic independent implicit-deadline tasks."""

import argparse
import json
from fractions import Fraction
from pathlib import Path


def analyze(tasks):
    if not tasks:
        raise ValueError("at least one task required")
    ratios = []
    for t in tasks:
        c, p = Fraction(str(t["execution"])), Fraction(str(t["period"]))
        if c < 0 or p <= 0:
            raise ValueError("execution nonnegative and period positive required")
        if "deadline" in t and Fraction(str(t["deadline"])) != p:
            raise ValueError("only implicit deadlines (deadline=period) supported")
        if t.get("blocking", 0) != 0 or t.get("jitter", 0) != 0:
            raise ValueError("nonzero blocking/jitter outside this model")
        ratios.append(c / p)
    utilization = sum(ratios, Fraction(0))
    bound = len(tasks) * (2 ** (1 / len(tasks)) - 1)
    u = float(utilization)
    return {
        "utilization": u,
        "utilization_exact": str(utilization),
        "edf_schedulable_in_model": utilization <= 1,
        "rm_liu_layland_sufficient_bound": bound,
        "rm_result": "sufficient_condition_met"
        if u <= bound
        else "not_decided_by_this_sufficient_test",
        "assumptions": "single core, preemptive, independent periodic/sporadic tasks; D=T; justified execution bounds; no blocking/jitter/overhead; not an OS timing certification",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    a = p.parse_args()
    try:
        r = analyze(json.loads(a.input.read_text()))
    except (ValueError, TypeError, KeyError, ZeroDivisionError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
