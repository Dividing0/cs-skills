# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/enu_ned.py assets/example-input.json
```

Only ENU->NED and NED->ENU, same physical origin and units. vector is length3. Optional covariance is finite 3x3 and is transformed by R C R^T. The helper does not establish positive-semidefiniteness or sensor calibration. It does not convert geodetic coordinates, transform between moving frames, shift origins or synchronize clocks. Round trip is an identity under this convention.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
