"""Paired cluster bootstrap for error-rate differences on independent groups."""

import argparse
import json
import math
import random
from pathlib import Path


def compare(groups, trials=2000, seed=0):
    if not groups or trials < 100:
        raise ValueError("nonempty groups and at least 100 trials required")
    ids = [g["id"] for g in groups]
    if any(not isinstance(i, str) for i in ids) or len(set(ids)) != len(ids):
        raise ValueError("group IDs must be unique strings")
    for g in groups:
        for field in ("errors_a", "errors_b", "units"):
            value = g[field]
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError("counts must be nonnegative integers")
        if g["units"] == 0:
            raise ValueError("each group must have positive denominator")

    def delta(selected):
        units = sum(g["units"] for g in selected)
        return (
            sum(g["errors_b"] for g in selected) - sum(g["errors_a"] for g in selected)
        ) / units

    rng = random.Random(seed)
    samples = sorted(delta([rng.choice(groups) for _ in groups]) for _ in range(trials))

    def quantile(p):
        position = p * (len(samples) - 1)
        lo = math.floor(position)
        hi = math.ceil(position)
        return samples[lo] + (samples[hi] - samples[lo]) * (position - lo)

    return {
        "delta_b_minus_a": delta(groups),
        "percentile_95_interval": [quantile(0.025), quantile(0.975)],
        "groups": len(groups),
        "trials": trials,
        "seed": seed,
        "scope": "resample independent groups, paired A/B; pooled count ratios; percentile interval is empirical and unreliable with few/nonrepresentative groups; no significance or generalization certification",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="JSON [{id,errors_a,errors_b,units},...]")
    p.add_argument("--trials", type=int, default=2000)
    p.add_argument("--seed", type=int, default=0)
    a = p.parse_args()
    try:
        r = compare(json.loads(a.input.read_text()), a.trials, a.seed)
    except (ValueError, TypeError, KeyError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
