"""Exercise documented helper commands and their result/exit-code contracts."""

import json
import re
import shlex
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class HelperCommands(unittest.TestCase):
    def run_helper(self, skill, arguments):
        return subprocess.run(
            [sys.executable, *arguments],
            cwd=ROOT / skill,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=30,
        )

    def test_documented_examples(self):
        guides = sorted(ROOT.glob("*/references/command-line.md"))
        self.assertTrue(guides, "No helper command guides found")
        with tempfile.TemporaryDirectory() as temporary:
            for guide in guides:
                skill = guide.parent.parent.name
                with self.subTest(skill=skill):
                    source = guide.read_text(encoding="utf-8")
                    match = re.search(r"```bash\n(python [^\n]+)\n```", source)
                    self.assertIsNotNone(match)
                    assert match is not None
                    arguments = shlex.split(match.group(1))[1:]
                    output = Path(temporary) / "sorted.txt"
                    if skill == "design-external-memory-algorithms":
                        arguments[2] = str(output)
                    result = self.run_helper(skill, arguments)
                    expected_exit = 1 if skill in {
                        "design-automata-and-grammars", "model-check-state-machines"
                    } else 0
                    self.assertEqual(result.returncode, expected_exit, result.stderr)
                    data = json.loads(result.stdout)
                    self.assertIsInstance(data, dict)
                    self.assertTrue(data)
                    if skill == "design-external-memory-algorithms":
                        fixture = (ROOT / skill / arguments[1]).read_text(encoding="utf-8")
                        self.assertEqual(
                            output.read_text(encoding="utf-8").splitlines(),
                            sorted(fixture.splitlines()),
                        )
                    elif skill == "design-network-protocols":
                        self.assertEqual(data["frames_hex"], ["616263", ""])
                    elif skill == "design-automata-and-grammars":
                        self.assertEqual(data["status"], "different")
                        self.assertEqual(data["word"], ["a"])

    def test_capped_automata_search_reports_unknown(self):
        result = self.run_helper("design-automata-and-grammars", [
            "scripts/compare_dfa.py", "assets/example-input.json", "--limit", "1"
        ])
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "unknown")

    def test_oversized_frame_is_rejected(self):
        result = self.run_helper("design-network-protocols", [
            "scripts/frame_decoder.py", "assets/example-input.json", "--max-frame", "2"
        ])
        self.assertEqual(result.returncode, 2)
        self.assertIn("declared frame exceeds limit", result.stderr)


if __name__ == "__main__":
    unittest.main()
