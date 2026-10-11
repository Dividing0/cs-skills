# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/transform_points.py assets/example-input.json
```

matrices are 4x4 finite entries, listed first-applied to last-applied; column vectors. Composite=last*...*first. points are finite [x,y,z]; homogeneous w=1 then divide by output w. Near-zero/nonfinite w is rejected. No clipping/viewport convention, normal transform or coordinate-frame identity is implied. Use known points and composition tests before rendering.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
