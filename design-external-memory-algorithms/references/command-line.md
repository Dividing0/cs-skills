# External sorting helper

Requires Python 3.10+ and standard library only. Run from the skill directory:

```bash
python scripts/external_sort.py assets/example-input.txt /tmp/cs-sort-new-output.txt --chunk-bytes 4 --fan-in 2 --max-record-bytes 64
```

The output path must not exist; choose a fresh path per run. Input is UTF-8 newline-delimited text. Sort key is the complete record after removing its LF delimiter, with lexicographic Python string order. Carriage returns remain part of the record. Duplicates remain. Missing final LF is normalized to LF in output. This does not sort JSON fields, numeric values or locale collation.

`--chunk-bytes` bounds encoded input in a sort chunk except one permitted oversized record; `--max-record-bytes` bounds a single encoded record including LF. Python decoded-string/list overhead means this is not a precise RSS cap. Each merge opens at most fan-in readers plus one output. Temporary runs are automatically cleaned on normal errors; process/power loss may leave temporary files. Final output is newly created; an interrupted write may leave partial data after process termination. No fsync, atomic durable publication or recovery protocol is claimed. Use the storage-engine workflow for those requirements.

Never overwrite the input or an existing output. Preserve output/data hashes and report record count, spill passes, memory observations and device conditions when using this on real data.
