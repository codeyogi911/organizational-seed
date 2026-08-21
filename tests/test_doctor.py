import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


DOCTOR = Path(__file__).resolve().parents[1] / "tools" / "doctor"


class DoctorTests(unittest.TestCase):
    def make_instance(self):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        (root / ".github").mkdir()
        (root / ".github" / "CODEOWNERS").write_text(
            "/ORG.md @founder\n"
            "/AUTHORITY.md @founder\n"
            "/AUTHORING.md @founder\n"
            "/processes/ @founder\n"
            "/roles/ @founder\n"
        )
        (root / "processes").mkdir()
        (root / "lessons").mkdir()
        (root / "decisions").mkdir()
        (root / "proposals").mkdir()
        self.write(
            root,
            "lessons/_kind.md",
            """
            # Kind: Lesson

            **Required frontmatter:** `id`, `kind`, `date`, `process`, and `status`.
            """,
        )
        return tmp, root

    def write(self, root, relative, body):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(body).lstrip())
        return path

    def run_doctor(self, root):
        return subprocess.run(
            [sys.executable, str(DOCTOR), str(root)],
            text=True,
            capture_output=True,
            check=False,
        )

    def add_process(self, root, filename="improve-a-process.md", process_id="improve-a-process", title="improve a Process"):
        self.write(
            root,
            f"processes/{filename}",
            f"""
            ---
            id: {process_id}
            kind: process
            status: active
            ---

            # Process: {title}

            ## Outcome

            One Process improves from experience.

            ## When to use

            Use when needed.

            ## Boundaries

            Stay within Authority.

            ## Evidence and approvals

            Read the evidence and obtain approval.

            ## Steps

            1. Improve it.

            ## Done when

            The outcome is visible.

            ## Failure and recovery

            Retry from the branch diff.
            """,
        )

    def add_lesson(self, root, frontmatter, body="Teaching remains visible."):
        content = (
            "---\n"
            "id: 2026-08-21-visible-teaching\n"
            "kind: lesson\n"
            "date: 2026-08-21\n"
            f"{frontmatter}\n"
            "---\n\n"
            "# Visible teaching\n\n"
            f"{body}\n"
        )
        self.write(root, "lessons/2026-08-21-visible-teaching.md", content)

    def test_pending_lesson_is_reported_without_failing(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.add_lesson(root, "process: improve-a-process\nstatus: pending")

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("lesson queue: 1 pending", result.stdout)

    def test_process_filename_must_match_id(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root, filename="old-name.md")

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[process-name]", result.stdout)

    def test_process_title_must_share_the_outcome_name(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root, title="weekly audit")

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[process-name]", result.stdout)

    def test_active_process_requires_the_shared_shape(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.write(
            root,
            "processes/incomplete.md",
            """
            ---
            id: incomplete
            kind: process
            status: active
            ---

            # Process: incomplete

            ## Outcome

            Something becomes complete.
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[process-shape]", result.stdout)

    def test_codeowners_must_cover_authoring(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        (root / ".github" / "CODEOWNERS").write_text(
            "/ORG.md @founder\n/AUTHORITY.md @founder\n/processes/ @founder\n/roles/ @founder\n"
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[enforce]", result.stdout)
        self.assertIn("/AUTHORING.md", result.stdout)

    def test_lesson_must_route_to_an_active_process(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_lesson(root, "process: missing-process\nstatus: pending")

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-route]", result.stdout)

    def test_absorption_requires_receipts(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.add_lesson(root, "process: improve-a-process\nstatus: absorbed")

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_standalone_decision_cannot_authorize_process_absorption(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/0001-absorb.md",
            """
            ---
            kind: decision
            date: 2026-08-21
            status: ruled
            ruled-by: Founder
            outcome: approved
            lesson-outcome: absorb
            ---

            # Decision

            Approve [this Lesson](../lessons/2026-08-21-visible-teaching.md)
            into [the Process](../processes/improve-a-process.md).
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: processes/improve-a-process.md\ndecided-by: decisions/0001-absorb.md",
            "Absorbed into [the Process](../processes/improve-a-process.md) by [Decision 0001](../decisions/0001-absorb.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_retirement_requires_a_live_decision(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: retired\nclosed-by: decisions/missing.md",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_applied_proposal_ruling_can_be_the_approval_receipt(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "proposals/0001-absorb.md",
            """
            ---
            status: applied
            ---

            # Proposal

            Absorb [this Lesson](../lessons/2026-08-21-visible-teaching.md)
            into [the Process](../processes/improve-a-process.md).

            ## Ruling

            **Outcome:** approved

            **Ruled by:** Founder

            **Date:** 2026-08-21

            **Lesson outcome:** absorb

            **Reason:** The teaching belongs in the Process.
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: processes/improve-a-process.md\ndecided-by: proposals/0001-absorb.md",
            "Absorbed into [the Process](../processes/improve-a-process.md) by [Proposal 0001](../proposals/0001-absorb.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_not_approved_words_do_not_count_as_approval(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "proposals/0001-not-approved.md",
            """
            ---
            status: applied
            ---

            # Proposal

            [Lesson](../lessons/2026-08-21-visible-teaching.md) and
            [Process](../processes/improve-a-process.md).

            ## Ruling

            This was not approved.
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: processes/improve-a-process.md\ndecided-by: proposals/0001-not-approved.md",
            "Claimed by [the Process](../processes/improve-a-process.md) and [Proposal](../proposals/0001-not-approved.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_rejected_decision_cannot_absorb_a_lesson(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/0001-reject.md",
            """
            ---
            outcome: rejected
            ---

            # Decision

            Reject [this Lesson](../lessons/2026-08-21-visible-teaching.md)
            for [the Process](../processes/improve-a-process.md).
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: processes/improve-a-process.md\ndecided-by: decisions/0001-reject.md",
            "Claimed by [the Process](../processes/improve-a-process.md) and [Decision](../decisions/0001-reject.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_absorption_proposal_must_link_the_receiver(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "proposals/0001-incomplete.md",
            """
            ---
            status: applied
            ---

            # Proposal

            Approve [this Lesson](../lessons/2026-08-21-visible-teaching.md).

            ## Ruling

            **Outcome:** approved

            **Ruled by:** Founder

            **Date:** 2026-08-21

            **Lesson outcome:** absorb

            **Reason:** The teaching belongs in the Process.
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: processes/improve-a-process.md\ndecided-by: proposals/0001-incomplete.md",
            "Claimed by [the Process](../processes/improve-a-process.md) and [Proposal](../proposals/0001-incomplete.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_approved_closure_is_valid(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/0002-close.md",
            """
            ---
            kind: decision
            date: 2026-08-21
            status: ruled
            ruled-by: Founder
            outcome: approved
            lesson-outcome: close
            ---

            # Decision

            Close [this Lesson](../lessons/2026-08-21-visible-teaching.md#closure-reason).
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: retired\nclosed-by: decisions/0002-close.md",
            "See [Decision](../decisions/0002-close.md).\n\n## Closure reason\n\nThe teaching no longer applies.",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_decision_must_link_the_closure_reason(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/0005-no-reason.md",
            """
            ---
            kind: decision
            date: 2026-08-21
            status: ruled
            ruled-by: Founder
            outcome: approved
            lesson-outcome: close
            ---

            # Decision

            Close [this Lesson](../lessons/2026-08-21-visible-teaching.md).
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: retired\nclosed-by: decisions/0005-no-reason.md",
            "See [Decision](../decisions/0005-no-reason.md).\n\n## Closure reason\n\nThe teaching no longer applies.",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_unruled_decision_cannot_close_a_lesson(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/0003-unruled.md",
            """
            ---
            outcome: approved
            lesson-outcome: close
            ---

            # Decision

            Close [this Lesson](../lessons/2026-08-21-visible-teaching.md).
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: retired\nclosed-by: decisions/0003-unruled.md",
            "See [Decision](../decisions/0003-unruled.md).\n\n## Closure reason\n\nThe teaching no longer applies.",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_keep_decision_cannot_close_a_lesson(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/0004-keep.md",
            """
            ---
            kind: decision
            date: 2026-08-21
            status: ruled
            ruled-by: Founder
            outcome: approved
            lesson-outcome: keep
            ---

            # Decision

            Keep [this Lesson](../lessons/2026-08-21-visible-teaching.md#closure-reason).
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: retired\nclosed-by: decisions/0004-keep.md",
            "See [Decision](../decisions/0004-keep.md).\n\n## Closure reason\n\nThe teaching no longer applies.",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_reroute_proposal_cannot_absorb_a_lesson(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "proposals/0002-reroute.md",
            """
            ---
            status: applied
            ---

            # Proposal

            [Lesson](../lessons/2026-08-21-visible-teaching.md) and
            [Process](../processes/improve-a-process.md).

            ## Ruling

            **Outcome:** approved

            **Ruled by:** Founder

            **Date:** 2026-08-21

            **Lesson outcome:** reroute

            **Reason:** Another Process owns the teaching.
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: processes/improve-a-process.md\ndecided-by: proposals/0002-reroute.md",
            "Claimed by [the Process](../processes/improve-a-process.md) and [Proposal](../proposals/0002-reroute.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_fast_track_row_can_authorize_absorption(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/fast-track.md",
            """
            # Fast-track ledger

            | Date | File(s) | Change | Outcome | Ruling |
            |---|---|---|---|---|
            | 2026-08-21 | [Process](../processes/improve-a-process.md) | Lesson outcome: absorb [Lesson](../lessons/2026-08-21-visible-teaching.md) into [Process](../processes/improve-a-process.md) | approved | "yes" |
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: processes/improve-a-process.md\ndecided-by: decisions/fast-track.md",
            "Absorbed into [the Process](../processes/improve-a-process.md) by the [fast-track ruling](../decisions/fast-track.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_fast_track_no_cannot_authorize_absorption(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/fast-track.md",
            """
            # Fast-track ledger

            | Date | File(s) | Change | Outcome | Ruling |
            |---|---|---|---|---|
            | 2026-08-21 | [Process](../processes/improve-a-process.md) | Lesson outcome: absorb [Lesson](../lessons/2026-08-21-visible-teaching.md) into [Process](../processes/improve-a-process.md) | approved | "no" |
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: processes/improve-a-process.md\ndecided-by: decisions/fast-track.md",
            "Claimed by [the Process](../processes/improve-a-process.md) and [fast-track](../decisions/fast-track.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_fast_track_receipt_requires_a_real_date(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/fast-track.md",
            """
            # Fast-track ledger

            | Date | File(s) | Change | Outcome | Ruling |
            |---|---|---|---|---|
            | {YYYY-MM-DD} | [Process](../processes/improve-a-process.md) | Lesson outcome: absorb [Lesson](../lessons/2026-08-21-visible-teaching.md) into [Process](../processes/improve-a-process.md) | approved | "yes" |
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: processes/improve-a-process.md\ndecided-by: decisions/fast-track.md",
            "Claimed by [the Process](../processes/improve-a-process.md) and [fast-track](../decisions/fast-track.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[ledger]", result.stdout)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_fast_track_closure_requires_a_lesson_reason(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/fast-track.md",
            """
            # Fast-track ledger

            | Date | File(s) | Change | Outcome | Ruling |
            |---|---|---|---|---|
            | 2026-08-21 | [Lesson](../lessons/2026-08-21-visible-teaching.md#closure-reason) | Lesson outcome: close [Lesson](../lessons/2026-08-21-visible-teaching.md#closure-reason) | approved | "yes" |
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: retired\nclosed-by: decisions/fast-track.md",
            "Claimed closed by [fast-track](../decisions/fast-track.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("Closure reason", result.stdout)

    def test_standalone_closure_requires_a_real_date(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "decisions/0006-placeholder-date.md",
            """
            ---
            kind: decision
            date: {YYYY-MM-DD}
            status: ruled
            ruled-by: Founder
            outcome: approved
            lesson-outcome: close
            ---

            # Decision

            Close [this Lesson](../lessons/2026-08-21-visible-teaching.md#closure-reason).
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: retired\nclosed-by: decisions/0006-placeholder-date.md",
            "See [Decision](../decisions/0006-placeholder-date.md).\n\n## Closure reason\n\nThe teaching no longer applies.",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

    def test_closure_rejects_placeholder_lesson_reasons(self):
        for placeholder in ("TBD", "N/A"):
            with self.subTest(placeholder=placeholder):
                tmp, root = self.make_instance()
                self.addCleanup(tmp.cleanup)
                self.add_process(root)
                self.write(
                    root,
                    "decisions/0007-placeholder-reason.md",
                    f"""
                    ---
                    kind: decision
                    date: 2026-08-21
                    status: ruled
                    ruled-by: Founder
                    outcome: approved
                    lesson-outcome: close
                    ---

                    # Decision

                    Close [this Lesson](../lessons/2026-08-21-visible-teaching.md#closure-reason).
                    """,
                )
                self.add_lesson(
                    root,
                    "process: improve-a-process\nstatus: retired\nclosed-by: decisions/0007-placeholder-reason.md",
                    f"See [Decision](../decisions/0007-placeholder-reason.md).\n\n## Closure reason\n\n{placeholder}",
                )

                result = self.run_doctor(root)

                self.assertEqual(1, result.returncode)
                self.assertIn("[lesson-outcome]", result.stdout)

    def test_seed_source_rejects_live_lesson_residue(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.write(root, "ORG.md", "# {Organization Name} — the Organization\n")
        self.add_process(root)
        self.add_lesson(root, "process: improve-a-process\nstatus: pending")

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[seed-boundary]", result.stdout)
        self.assertNotIn("[lesson-outcome]", result.stdout)

    def test_seed_source_rejects_every_runtime_residue_class(self):
        cases = {
            "work/2026-08-21-task.md": "# Task\n",
            "lessons/archive/2026-08-21-lesson.md": "# Lesson\n",
            "proposals/0001-change.md": "# Proposal\n",
            "decisions/0001-ruling.md": "# Decision\n",
        }
        for relative, body in cases.items():
            with self.subTest(relative=relative):
                tmp, root = self.make_instance()
                self.addCleanup(tmp.cleanup)
                self.write(root, "ORG.md", "# {Organization Name} — the Organization\n")
                self.write(root, relative, body)

                result = self.run_doctor(root)

                self.assertEqual(1, result.returncode)
                self.assertIn("[seed-boundary]", result.stdout)

    def test_seed_source_rejects_a_populated_fast_track_ledger(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.write(root, "ORG.md", "# {Organization Name} — the Organization\n")
        self.write(
            root,
            "decisions/fast-track.md",
            """
            # Fast-track ledger

            | Date | File(s) | Change | Outcome | Ruling |
            |---|---|---|---|---|
            | 2026-08-21 | file.md | wording | approved | "yes" |
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[seed-boundary]", result.stdout)

    def test_process_file_cannot_evade_shape_with_wrong_kind(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.write(
            root,
            "processes/evade.md",
            """
            ---
            id: evade
            kind: note
            status: active
            ---

            # Process: evade
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[process-shape]", result.stdout)

    def test_process_sections_must_be_exact_and_ordered(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        process = root / "processes/improve-a-process.md"
        process.write_text(process.read_text().replace(
            "## Steps\n", "## Extra ceremony\n\nNone.\n\n## Steps\n"
        ))

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[process-shape]", result.stdout)

    def test_nested_and_hidden_lessons_stay_visible_to_the_queue(self):
        for target_relative in (
            "lessons/archive/2026-08-21-visible-teaching.md",
            "lessons/_hidden.md",
        ):
            with self.subTest(target=target_relative):
                tmp, root = self.make_instance()
                self.addCleanup(tmp.cleanup)
                self.add_process(root)
                self.add_lesson(root, "process: improve-a-process\nstatus: pending")
                source = root / "lessons/2026-08-21-visible-teaching.md"
                target = root / target_relative
                target.parent.mkdir(parents=True, exist_ok=True)
                source.rename(target)

                result = self.run_doctor(root)

                self.assertEqual(1, result.returncode)
                self.assertIn("[lesson-identity]", result.stdout)
                self.assertIn("lesson queue: 1 pending", result.stdout)

    def test_absorption_receiver_cannot_be_its_own_proposal(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "proposals/0008-self.md",
            """
            ---
            status: applied
            ---

            # Proposal

            [Lesson](../lessons/2026-08-21-visible-teaching.md) and
            [this Proposal](0008-self.md).

            ## Ruling

            **Outcome:** approved

            **Ruled by:** Founder

            **Date:** 2026-08-21

            **Lesson outcome:** absorb

            **Reason:** The teaching needs a current home.
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: proposals/0008-self.md\ndecided-by: proposals/0008-self.md",
            "Claimed by [Proposal](../proposals/0008-self.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("behavioral home", result.stdout)

    def test_lesson_kind_can_receive_lifecycle_teaching(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "proposals/0009-lesson-kind.md",
            """
            ---
            status: applied
            ---

            # Proposal

            Move [this Lesson](../lessons/2026-08-21-visible-teaching.md) into
            [the Lesson definition](../lessons/_kind.md).

            ## Ruling

            **Outcome:** approved

            **Ruled by:** Founder

            **Date:** 2026-08-21

            **Lesson outcome:** absorb

            **Reason:** The teaching defines Lesson lifecycle behavior.
            """,
        )
        self.add_lesson(
            root,
            "process: improve-a-process\nstatus: absorbed\nabsorbed-into: lessons/_kind.md\ndecided-by: proposals/0009-lesson-kind.md",
            "Absorbed into [the Lesson definition](_kind.md) by [Proposal](../proposals/0009-lesson-kind.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_machinery_and_mounts_cannot_receive_teaching(self):
        for receiver, proposal_link, lesson_link in (
            ("tools/doctor", "../tools/doctor", "../tools/doctor"),
            ("AGENTS.md", "../AGENTS.md", "../AGENTS.md"),
        ):
            with self.subTest(receiver=receiver):
                tmp, root = self.make_instance()
                self.addCleanup(tmp.cleanup)
                self.add_process(root)
                self.write(root, receiver, "replaceable machinery\n")
                self.write(
                    root,
                    "proposals/0010-machinery.md",
                    f"""
                    ---
                    status: applied
                    ---

                    # Proposal

                    Move [this Lesson](../lessons/2026-08-21-visible-teaching.md)
                    into [the receiver]({proposal_link}).

                    ## Ruling

                    **Outcome:** approved

                    **Ruled by:** Founder

                    **Date:** 2026-08-21

                    **Lesson outcome:** absorb

                    **Reason:** The teaching needs a current home.
                    """,
                )
                self.add_lesson(
                    root,
                    f"process: improve-a-process\nstatus: absorbed\nabsorbed-into: {receiver}\ndecided-by: proposals/0010-machinery.md",
                    f"Claimed by [receiver]({lesson_link}) and [Proposal](../proposals/0010-machinery.md).",
                )

                result = self.run_doctor(root)

                self.assertEqual(1, result.returncode)
                self.assertIn("durable behavioral home", result.stdout)


if __name__ == "__main__":
    unittest.main()
