"""Release archives validate skills and exclude repository artifacts."""

import subprocess
import tempfile
import unittest
from pathlib import Path
from urllib.parse import quote
from zipfile import ZipFile

from scripts.release_skills import package


class ReleaseMetadata(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "repo з пробілом & дані"
        self.root.mkdir()
        self.write("LICENSE", "Test license notice.\n")
        self.write(
            "sample-skill/SKILL.md",
            '---\nname: sample-skill\ndescription: "A sample skill."\n---\n\n'
            "# Sample\n\nRead [the reference](references/example.md).\n",
        )
        self.write(
            "sample-skill/agents/openai.yaml",
            'interface:\n  display_name: "Sample Skill"\n'
            '  short_description: "A skill for checking release metadata"\n'
            '  default_prompt: "Use $sample-skill for this task."\n',
        )
        self.write("sample-skill/references/example.md", "Sample reference.\n")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.track()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")

    def track(self):
        subprocess.run(["git", "add", "--all"], cwd=self.root, check=True)

    def test_archive_includes_metadata_and_excludes_service_files(self):
        excluded = [
            "tests/test_example.py",
            "scripts/tool.py",
            ".claude-plugin/private.json",
            ".venv/example.py",
            "sample-skill/.DS_Store",
            "sample-skill/__pycache__/example.pyc",
            "sample-skill/venv/example.py",
        ]
        for name in excluded:
            self.write(name, "not a release resource\n")
        self.track()
        output = self.root / "release.zip"
        package(self.root, output)
        with ZipFile(output) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(
                set(archive.namelist()),
                {
                    "LICENSE",
                    "sample-skill/SKILL.md",
                    "sample-skill/agents/openai.yaml",
                    "sample-skill/references/example.md",
                },
            )
            self.assertEqual(archive.read("LICENSE"), b"Test license notice.\n")

    def test_rejects_untracked_ui_metadata(self):
        subprocess.run(
            ["git", "rm", "--cached", "-q", "sample-skill/agents/openai.yaml"],
            cwd=self.root,
            check=True,
        )
        with self.assertRaisesRegex(ValueError, "missing tracked UI metadata"):
            package(self.root, self.root / "release.zip")

    def test_rejects_missing_and_escaping_links(self):
        for target in ("references/missing.md", "../../outside.md"):
            with self.subTest(target=target):
                self.write(
                    "sample-skill/references/example.md",
                    f"Read [reference]({target}).\\n",
                )
                with self.assertRaisesRegex(ValueError, "link"):
                    package(self.root, self.root / "release.zip")

    def test_rejects_wrong_skill_name(self):
        path = self.root / "sample-skill/SKILL.md"
        source = path.read_text(encoding="utf-8")
        self.write("sample-skill/SKILL.md", source.replace("name: sample-skill", "name: wrong"))
        with self.assertRaisesRegex(ValueError, "name must match"):
            package(self.root, self.root / "release.zip")

    def test_license_is_optional(self):
        subprocess.run(["git", "rm", "--cached", "-q", "LICENSE"], cwd=self.root, check=True)
        output = self.root / "release.zip"
        package(self.root, output)
        with ZipFile(output) as archive:
            self.assertNotIn("LICENSE", archive.namelist())

    def test_crlf_unicode_git_paths_and_zip_round_trip(self):
        name = "sample-skill/references/дані з пробілом.md"
        content = "Є Ё ∀ — preserved UTF-8\r\n".encode()
        (self.root / name).write_bytes(content)
        skill = self.root / "sample-skill/SKILL.md"
        source = skill.read_text(encoding="utf-8")
        source += f"\nRead [Unicode data]({quote('references/дані з пробілом.md')}).\n"
        skill.write_bytes(source.replace("\n", "\r\n").encode("utf-8"))
        self.track()
        output = self.root / "nested" / "архів з пробілом.zip"
        package(self.root, output)
        with ZipFile(output) as archive:
            self.assertIsNone(archive.testzip())
            self.assertIn(name, archive.namelist())
            self.assertTrue(all("\\" not in path for path in archive.namelist()))
            self.assertEqual(archive.read(name), content)
            self.assertEqual(archive.read("sample-skill/SKILL.md"), skill.read_bytes())
            extracted = self.root / "unpacked"
            archive.extractall(extracted)
        self.assertEqual((extracted / name).read_bytes(), content)


if __name__ == "__main__":
    unittest.main()

