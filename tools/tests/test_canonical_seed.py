"""Public-boundary checks for the canonical Seed bundle."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COMMAND = ROOT / "tools" / "knowledge-bundle"
sys.path.insert(0, str(ROOT / "tools"))
from knowledge_bundle import parse_concept  # noqa: E402


class CanonicalSeedTest(unittest.TestCase):
    def test_shared_parser_resolves_canonical_yaml_for_consumers(self):
        parsed = parse_concept(
            "---\n"
            'type: "Process"\n'
            'state: "active"\n'
            "tags: [seed, okf]\n"
            "---\n\n# Process\n"
        )

        self.assertEqual(parsed.fields["type"], "Process")
        self.assertEqual(parsed.fields["state"], "active")
        self.assertEqual(parsed.fields["tags"], "seed, okf")
        self.assertEqual(parsed.raw_fields["tags"], "[seed, okf]")
        self.assertEqual(parsed.body, "\n# Process\n")

    def test_mount_routes_to_the_canonical_bundle(self):
        mount = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("knowledge/ORG.md", mount)
        self.assertIn("knowledge/KNOWLEDGE.md", mount)
        self.assertIn("knowledge/AUTHORITY.md", mount)

    def test_root_has_no_second_canonical_entry(self):
        self.assertFalse((ROOT / "ORG.md").exists())
        self.assertFalse((ROOT / "KNOWLEDGE.md").exists())
        self.assertFalse((ROOT / "AUTHORITY.md").exists())
        self.assertTrue((ROOT / "knowledge" / "ORG.md").is_file())
        self.assertTrue((ROOT / "knowledge" / "KNOWLEDGE.md").is_file())
        self.assertTrue((ROOT / "knowledge" / "AUTHORITY.md").is_file())

    def test_pr1_knowledge_model_and_processes_live_in_the_bundle(self):
        for relative in (
            "AUTHORING.md",
            "CONTEXT.md",
            "processes/_contract.md",
            "processes/change-standing-knowledge.md",
            "processes/handle-uncovered-work.md",
            "processes/review-lessons.md",
            "goals/_kind.md",
            "lessons/_kind.md",
            "work/_kind.md",
        ):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / "knowledge" / relative).is_file())
                self.assertFalse((ROOT / relative).exists())

    def test_seed_doctor_accepts_the_canonical_boundary(self):
        result = subprocess.run(
            [str(ROOT / "tools" / "doctor"), str(ROOT)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_canonical_bundle_validates_through_the_public_cli(self):
        result = subprocess.run(
            [
                str(COMMAND),
                "--root",
                str(ROOT),
                "validate",
                "--bundle",
                str(ROOT / "knowledge"),
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["findings"], [])

    def test_canonical_profile_inventories_the_bundle_without_an_extra_prefix(self):
        result = subprocess.run(
            [
                str(COMMAND),
                "--root",
                str(ROOT),
                "inventory",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["unmapped"], [])


if __name__ == "__main__":
    unittest.main()
