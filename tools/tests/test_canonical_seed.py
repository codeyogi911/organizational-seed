"""Public-boundary checks for the canonical Seed bundle."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COMMAND = ROOT / "tools" / "knowledge-bundle"
sys.path.insert(0, str(ROOT / "tools"))
from knowledge_bundle import parse_concept  # noqa: E402


class CanonicalSeedTest(unittest.TestCase):
    def test_mainmind_deposit_is_valid_inside_a_real_instance(self):
        with tempfile.TemporaryDirectory() as directory:
            instance = Path(directory)
            shutil.copytree(ROOT / "knowledge", instance / "knowledge")
            shutil.copytree(ROOT / ".github", instance / ".github")
            shutil.copy2(ROOT / ".mainmind.json", instance / ".mainmind.json")

            org = instance / "knowledge" / "ORG.md"
            org.write_text(
                org.read_text(encoding="utf-8").replace(
                    "# {Organization Name} — the Organization",
                    "# Example Company — the Organization",
                ),
                encoding="utf-8",
            )
            process = instance / "knowledge" / "processes" / "returns-review.md"
            process.write_text(
                textwrap.dedent(
                    """
                    ---
                    id: returns-review
                    type: process
                    state: active
                    description: Returns receive an evidence-backed review.
                    status: stable
                    access-scope: core
                    write-class: conserved
                    ---

                    # Process: returns review

                    ## Outcome

                    Returns receive an evidence-backed review.

                    ## When to use

                    Use when reviewing a return.

                    ## Boundaries

                    Stay within Authority.

                    ## Evidence and approvals

                    Read the return evidence.

                    ## Steps

                    1. Review the return.

                    ## Done when

                    The result and evidence are visible.

                    ## Failure and recovery

                    Retry from the preserved evidence.
                    """
                ).lstrip(),
                encoding="utf-8",
            )
            process_index = instance / "knowledge" / "processes" / "index.md"
            process_index.write_text(
                process_index.read_text(encoding="utf-8")
                + "\n| [returns review](returns-review.md) | Returns receive an evidence-backed review. |\n",
                encoding="utf-8",
            )
            fixture = (
                instance
                / "knowledge"
                / "lessons"
                / "2026-08-22-returns-need-a-visible-receipt.md"
            )
            fixture.write_text(
                textwrap.dedent(
                    """
                    ---
                    id: lesson-2026-08-22-returns-need-a-visible-receipt
                    type: Lesson
                    date: 2026-08-22
                    source-process: returns-review
                    state: pending
                    status: stable
                    access-scope: core
                    write-class: ledger
                    applies-to: processes/returns-review.md
                    ---

                    # Returns need a visible receipt

                    ## What happened

                    A return could not be reconciled without its receipt.

                    ## What it teaches

                    Require the receipt before reconciliation.

                    ## Where it applies

                    processes/returns-review.md

                    ## Evidence

                    - Synthetic acceptance evidence only.
                    """
                ).lstrip(),
                encoding="utf-8",
            )
            parsed = parse_concept(fixture.read_text(encoding="utf-8"))
            result = subprocess.run(
                [str(ROOT / "tools" / "doctor"), str(instance)],
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(parsed.fields["source-process"], "returns-review")
            self.assertEqual(parsed.fields["applies-to"], "processes/returns-review.md")
            self.assertFalse(parsed.raw_fields["source-process"].lstrip().startswith("["))
            self.assertFalse(parsed.raw_fields["applies-to"].lstrip().startswith("["))

    def test_optional_mainmind_mount_projects_every_policy_bearing_node(self):
        manifest = json.loads((ROOT / ".mainmind.json").read_text(encoding="utf-8"))
        projection = manifest["projection"]

        self.assertTrue(projection["replace"])
        self.assertEqual(projection["prefix"], "knowledge")
        self.assertIn("processes", projection["dirs"])
        projected = {
            path.relative_to(ROOT / "knowledge").as_posix()
            for path in (ROOT / "knowledge").rglob("*.md")
            if (
                path.relative_to(ROOT / "knowledge").as_posix()
                in projection["root"]
                or path.relative_to(ROOT / "knowledge").parts[0]
                in projection["dirs"]
            )
        }
        canonical = {
            path.relative_to(ROOT / "knowledge").as_posix()
            for path in (ROOT / "knowledge").rglob("*.md")
            if path.relative_to(ROOT / "knowledge").as_posix() != "index.md"
        }
        self.assertEqual(projected, canonical)

        # The directory declaration is the future-proof contract: a new
        # Instance Process is projected without editing this Mount. The
        # generated index is included too, but remains fail-closed because it
        # carries no discovery classification; the Process contract is an
        # explicitly classified conserved node.
        def is_projected(path):
            return path in projection["root"] or any(
                path.startswith(f"{directory}/")
                for directory in projection["dirs"]
            )

        for path in (
            "processes/future-instance-process.md",
            "processes/retired-instance-process.md",
            "processes/index.md",
            "processes/_contract.md",
            "work/process-drafts/future-process.md",
        ):
            with self.subTest(path=path):
                self.assertTrue(is_projected(path))
        index = parse_concept(
            (ROOT / "knowledge" / "processes" / "index.md").read_text(encoding="utf-8")
        )
        contract = parse_concept(
            (ROOT / "knowledge" / "processes" / "_contract.md").read_text(encoding="utf-8")
        )
        self.assertIsNone(index.fields)
        self.assertEqual(contract.fields["write-class"], "conserved")

    def test_every_canonical_node_declares_access_and_write_policy(self):
        access = parse_concept(
            (ROOT / "knowledge" / "ACCESS.md").read_text(encoding="utf-8")
        ).fields
        allowed_scopes = {
            value.strip() for value in access["access-scopes"].split(",")
        }
        allowed_write_classes = {
            value.strip() for value in access["write-classes"].split(",")
        }

        for path in (ROOT / "knowledge").rglob("*.md"):
            relative = path.relative_to(ROOT / "knowledge").as_posix()
            if relative in {"index.md", "processes/index.md"}:
                continue
            with self.subTest(path=path.relative_to(ROOT)):
                fields = parse_concept(path.read_text(encoding="utf-8")).fields
                self.assertIsNotNone(fields)
                self.assertIn(fields.get("access-scope"), allowed_scopes)
                self.assertIn(fields.get("write-class"), allowed_write_classes)
                self.assertEqual(fields["access-scope"], "core")

        self.assertEqual(access["access-scope"], "core")
        self.assertEqual(access["write-class"], "ruled")

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
