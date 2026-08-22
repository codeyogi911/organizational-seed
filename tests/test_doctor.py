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
            "/KNOWLEDGE.md @founder\n"
            "/CONTEXT.md @founder\n"
            "/AUTHORITY.md @founder\n"
            "/AUTHORING.md @founder\n"
            "/processes/ @founder\n"
            "/roles/ @founder\n"
            "/**/_kind.md @founder\n"
            "/proposals/0000-proposal-template.md @founder\n"
            "/decisions/fast-track.md @founder\n"
            "/docs/write-discipline.md @founder\n"
            "/.github/CODEOWNERS @founder\n"
        )
        (root / "processes").mkdir()
        (root / "processes" / "index.md").write_text(
            "# Processes\n\n| Process | Use it when |\n|---|---|\n"
        )
        (root / "lessons").mkdir()
        (root / "decisions").mkdir()
        (root / "proposals").mkdir()
        self.write(
            root,
            "lessons/_kind.md",
            """
            # Kind: Lesson

            **Required frontmatter:** `id`, `kind`, `date`, `source-process`, `applies-to`, and `status`.
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

    def add_process(
        self,
        root,
        filename="review-lessons.md",
        process_id="review-lessons",
        title="review Lessons",
        status="active",
        description="Lessons receive an honest outcome.",
    ):
        folder = "work/process-drafts" if status == "draft" else "processes"
        retirement = (
            "retired-on: 2026-08-21\n            " if status == "retired" else ""
        )
        path = self.write(
            root,
            f"{folder}/{filename}",
            f"""
            ---
            id: {process_id}
            kind: process
            status: {status}
            {retirement}description: {description}
            ---

            # Process: {title}

            ## Outcome

            Lessons receive an honest outcome.

            ## When to use

            Use when needed.

            ## Boundaries

            Stay within Authority.

            ## Evidence and approvals

            Read the evidence and obtain approval.

            ## Steps

            1. Review them.

            ## Done when

            The outcome is visible.

            ## Failure and recovery

            Retry from the branch diff.
            """,
        )
        if status in ("active", "example"):
            index = root / "processes" / "index.md"
            row = (
                f"| [{title}]({path.relative_to(root / 'processes')}) | "
                f"{description} |\n"
            )
            if row not in index.read_text():
                index.write_text(index.read_text() + row)

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

    def add_goal(self, root, goal_id="grow-revenue", state="active"):
        self.write(
            root,
            "goals/_kind.md",
            """
            # Kind: Goal

            **Required frontmatter:** `id`, `type`, `description`, `state`, `set-by`, and `set-on`.
            """,
        )
        return self.write(
            root,
            f"goals/{goal_id}.md",
            f"""
            ---
            id: {goal_id}
            type: Goal
            description: Grow revenue without widening authority.
            state: {state}
            set-by: Founder
            set-on: 2026-08-21
            ---

            # Goal: grow revenue

            ## Outcome

            Revenue grows.

            ## Why now

            The Founder set this direction.

            ## How we know

            Evidence supports the outcome.

            ## Not this

            Authority does not expand.

            ## Direction source

            "Grow revenue without widening authority."
            """,
        )

    def add_mainmind_decision(
        self,
        root,
        *,
        candidate="2" * 40,
        base="1" * 40,
        digest="3" * 64,
        ruling="yes",
        outcome="approved",
    ):
        suffix = candidate[:12]
        return self.write(
            root,
            f"decisions/mainmind-{suffix}.md",
            f'''
            ---
            id: "mainmind-{suffix}"
            type: decision
            date: 2026-08-22
            ruled-by: "Founder (@founder-user), authenticated Mainmind session"
            ruling: "{ruling}"
            ruled-at: "2026-08-22T10:11:12.000Z"
            state: ruled
            outcome: {outcome}
            base-sha: "{base}"
            candidate-sha: "{candidate}"
            target-diff-sha256: "{digest}"
            targets:
              - "processes/review-lessons.md"
            status: stable
            access-scope: core
            write-class: ledger
            ---

            # Decision: make Lesson receipts portable

            ## Ruling

            > {"Yes" if ruling == "yes" else "No"}.
            >
            > Keep the exact candidate auditable.

            — Founder (@founder-user), 2026-08-22T10:11:12.000Z

            ## {"What becomes true" if outcome == "approved" else "What would have become true"}

            - Lesson dispositions have a repository-native receipt.

            ## {"Exact candidate" if outcome == "approved" else "Exact candidate refused"}

            - Base commit: `{base}`
            - Candidate commit: `{candidate}`
            - Target diff SHA-256: `{digest}`
            - {"Target" if outcome == "approved" else "Target left unchanged"}: `processes/review-lessons.md`

            ## Integration

            {"Mainmind may land only an ordinary merge commit that retains the approved candidate and this Decision child commit in repository ancestry." if outcome == "approved" else "Only this Decision receipt lands on the canonical branch. The refused candidate remains outside canonical history."}
            ''',
        )

    def test_mainmind_decision_receipt_is_valid_in_a_plain_instance(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_mainmind_decision(root)

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_mainmind_rejection_receipt_is_valid_without_landing_candidate_bytes(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_mainmind_decision(root, ruling="no", outcome="rejected")

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_mainmind_decision_receipt_requires_exact_binding_fields(self):
        cases = {
            "candidate suffix": ("candidate-sha: \"" + "2" * 40 + "\"", "candidate-sha: \"" + "4" * 40 + "\""),
            "target digest": ("target-diff-sha256: \"" + "3" * 64 + "\"", "target-diff-sha256: \"short\""),
            "ruling outcome": ("outcome: approved", "outcome: rejected"),
            "circular receipt hash": ("state: ruled", "state: ruled\nreceipt-commit: \"" + "5" * 40 + "\""),
        }
        for name, (before, after) in cases.items():
            with self.subTest(name=name):
                tmp, root = self.make_instance()
                self.addCleanup(tmp.cleanup)
                decision = self.add_mainmind_decision(root)
                decision.write_text(
                    decision.read_text(encoding="utf-8").replace(before, after),
                    encoding="utf-8",
                )

                result = self.run_doctor(root)

                self.assertEqual(1, result.returncode)
                self.assertIn("[decision-receipt]", result.stdout)

    def test_mainmind_decision_cannot_evade_validation_with_a_malformed_filename(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        decision = self.add_mainmind_decision(root)
        decision.rename(decision.with_name("mainmind-not-a-candidate.md"))

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[decision-receipt]", result.stdout)
        self.assertIn("filename", result.stdout)

    def test_access_policy_uses_the_frozen_mainmind_pilot_vocabulary(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.write(
            root,
            "ACCESS.md",
            """
            ---
            type: Access Policy
            access-scope: core
            write-class: ruled
            access-scopes:
              - core
              - support
              - finance
              - founder
              - legal
            write-classes:
              - conserved
              - ruled
              - ledger
              - derived
            ---

            # Knowledge access
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("exactly core, support, finance, founder", result.stdout)
        self.assertIn("exactly conserved, ruled, ledger", result.stdout)

    def test_pending_lesson_is_reported_without_failing(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.add_lesson(root, "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: pending")

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("lesson queue: 1 pending", result.stdout)

    def test_active_access_policy_fails_closed_on_unclassified_nodes(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.write(
            root,
            "ACCESS.md",
            """
            ---
            type: Access Policy
            access-scope: core
            write-class: ruled
            ---

            # Knowledge access
            """,
        )
        self.write(
            root,
            "records/audit/log.md",
            """
            ---
            type: Audit Record
            ---

            # Audit log
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[access-policy]", result.stdout)
        self.assertIn("lessons/_kind.md", result.stdout)
        self.assertIn("records/audit/log.md", result.stdout)
        self.assertIn("missing access-scope and write-class", result.stdout)

    def test_access_policy_cannot_expand_the_frozen_pilot_vocabulary(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        access = self.write(
            root,
            "ACCESS.md",
            """
            ---
            type: Access Policy
            access-scope: legal
            write-class: ruled
            access-scopes:
              - core
              - legal
            write-classes:
              - conserved
              - ruled
            ---

            # Knowledge access
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("exactly core, support, finance, founder", result.stdout)

    def test_active_access_policy_rejects_unknown_policy_values(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        access = self.write(
            root,
            "ACCESS.md",
            """
            ---
            type: Access Policy
            access-scope: everyone
            write-class: editable
            ---

            # Knowledge access
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[access-policy]", result.stdout)
        self.assertIn(str(access.relative_to(root)), result.stdout)
        self.assertIn("unknown access-scope 'everyone'", result.stdout)
        self.assertIn("unknown write-class 'editable'", result.stdout)

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
        (root / "processes" / "index.md").write_text(
            "# Processes\n- [incomplete](incomplete.md)\n"
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[process-shape]", result.stdout)

    def test_codeowners_must_cover_authoring(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        (root / ".github" / "CODEOWNERS").write_text(
            "/ORG.md @founder\n/KNOWLEDGE.md @founder\n/CONTEXT.md @founder\n"
            "/AUTHORITY.md @founder\n/processes/ @founder\n/roles/ @founder\n"
            "/**/_kind.md @founder\n/proposals/0000-proposal-template.md @founder\n"
            "/decisions/fast-track.md @founder\n/docs/write-discipline.md @founder\n"
            "/.github/CODEOWNERS @founder\n"
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[enforce]", result.stdout)
        self.assertIn("/AUTHORING.md", result.stdout)

    def test_codeowners_must_cover_the_knowledge_model_and_kind_definitions(self):
        for missing_path in ("/KNOWLEDGE.md", "/**/_kind.md"):
            with self.subTest(missing_path=missing_path):
                tmp, root = self.make_instance()
                self.addCleanup(tmp.cleanup)
                codeowners = root / ".github" / "CODEOWNERS"
                codeowners.write_text(
                    codeowners.read_text().replace(
                        f"{missing_path} @founder\n", ""
                    )
                )

                result = self.run_doctor(root)

                self.assertEqual(1, result.returncode)
                self.assertIn("[enforce]", result.stdout)
                self.assertIn(missing_path, result.stdout)

    def test_lesson_must_name_an_active_source_process(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_lesson(
            root,
            "source-process: missing-process\napplies-to: unresolved\nstatus: pending",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-route]", result.stdout)

    def test_lesson_source_process_is_an_id_not_a_path(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.add_lesson(
            root,
            "source-process: processes/review-lessons.md\napplies-to: unresolved\nstatus: pending",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-route]", result.stdout)
        self.assertIn("does not name an active or retired Process", result.stdout)

    def test_pending_lesson_may_have_an_unresolved_home(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: unresolved\nstatus: pending",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("1 pending", result.stdout)

    def test_pending_lesson_accepts_a_canonical_active_process_home(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        process = root / "processes" / "review-lessons.md"
        process.write_text(
            process.read_text(encoding="utf-8")
            .replace("kind: process", "type: process")
            .replace("status: active", "state: active\nstatus: stable"),
            encoding="utf-8",
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: pending",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("1 pending", result.stdout)

    def test_lesson_may_name_a_retired_source_process(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root, status="retired")
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: unresolved\nstatus: pending",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("1 pending", result.stdout)

    def test_lesson_accepts_a_canonical_retired_source_process(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root, status="retired")
        process = root / "processes" / "review-lessons.md"
        process.write_text(
            process.read_text(encoding="utf-8")
            .replace("kind: process", "type: process")
            .replace("status: retired", "state: retired\nstatus: deprecated"),
            encoding="utf-8",
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: unresolved\nstatus: pending",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("1 pending", result.stdout)

    def test_lesson_accepts_quoted_canonical_process_fields(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root, status="active")
        process = root / "processes" / "review-lessons.md"
        process.write_text(
            process.read_text(encoding="utf-8")
            .replace("kind: process", 'type: "process"')
            .replace("status: active", 'state: "active"\nstatus: stable'),
            encoding="utf-8",
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: pending",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("1 pending", result.stdout)

    def test_pending_lesson_rejects_a_non_standing_home(self):
        for target, setup in (
            ("tools/helper", lambda root: self.write(root, "tools/helper", "replaceable machinery\n")),
            (
                "work/process-drafts/candidate.md",
                lambda root: self.add_process(
                    root,
                    filename="candidate.md",
                    process_id="candidate",
                    title="candidate",
                    status="draft",
                ),
            ),
        ):
            with self.subTest(target=target):
                tmp, root = self.make_instance()
                self.addCleanup(tmp.cleanup)
                self.add_process(root)
                setup(root)
                self.add_lesson(
                    root,
                    f"source-process: review-lessons\napplies-to: {target}\nstatus: pending",
                )

                result = self.run_doctor(root)

                self.assertEqual(1, result.returncode)
                self.assertIn("[lesson-route]", result.stdout)

    def test_absorption_requires_receipts(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.add_lesson(root, "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed")

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
            into [the Process](../processes/review-lessons.md).
            """,
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: decisions/0001-absorb.md",
            "Absorbed into [the Process](../processes/review-lessons.md) by [Decision 0001](../decisions/0001-absorb.md).",
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: retired\nclosed-by: decisions/missing.md",
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
            into [the Process](../processes/review-lessons.md).

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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: proposals/0001-absorb.md",
            "Absorbed into [the Process](../processes/review-lessons.md) by [Proposal 0001](../proposals/0001-absorb.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_absorbed_lesson_keeps_a_retired_process_as_historical_receiver(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        process = root / "processes" / "review-lessons.md"
        process.write_text(process.read_text().replace(
            "status: active\n",
            "status: retired\nretired-on: 2026-08-21\n",
        ))
        (root / "processes" / "index.md").write_text(
            "# Processes\n\n| Process | Use it when |\n|---|---|\n"
        )
        self.write(
            root,
            "proposals/0001-absorb.md",
            """
            ---
            status: applied
            ---

            # Proposal

            Absorb [this Lesson](../lessons/2026-08-21-visible-teaching.md)
            into [the Process](../processes/review-lessons.md).

            ## Ruling

            **Outcome:** approved

            **Ruled by:** Founder

            **Date:** 2026-08-20

            **Lesson outcome:** absorb

            **Reason:** The teaching belonged in the Process before retirement.
            """,
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: proposals/0001-absorb.md",
            "Absorbed into [the Process](../processes/review-lessons.md) by [Proposal 0001](../proposals/0001-absorb.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

        proposal = root / "proposals" / "0001-absorb.md"
        proposal.write_text(proposal.read_text().replace("2026-08-20", "2026-08-22"))
        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[lesson-outcome]", result.stdout)

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
            [Process](../processes/review-lessons.md).

            ## Ruling

            This was not approved.
            """,
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: proposals/0001-not-approved.md",
            "Claimed by [the Process](../processes/review-lessons.md) and [Proposal](../proposals/0001-not-approved.md).",
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
            for [the Process](../processes/review-lessons.md).
            """,
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: decisions/0001-reject.md",
            "Claimed by [the Process](../processes/review-lessons.md) and [Decision](../decisions/0001-reject.md).",
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: proposals/0001-incomplete.md",
            "Claimed by [the Process](../processes/review-lessons.md) and [Proposal](../proposals/0001-incomplete.md).",
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: retired\nclosed-by: decisions/0002-close.md",
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: retired\nclosed-by: decisions/0005-no-reason.md",
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: retired\nclosed-by: decisions/0003-unruled.md",
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: retired\nclosed-by: decisions/0004-keep.md",
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
            [Process](../processes/review-lessons.md).

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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: proposals/0002-reroute.md",
            "Claimed by [the Process](../processes/review-lessons.md) and [Proposal](../proposals/0002-reroute.md).",
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
            | 2026-08-21 | [Process](../processes/review-lessons.md) | Lesson outcome: absorb [Lesson](../lessons/2026-08-21-visible-teaching.md) into [Process](../processes/review-lessons.md) | approved | "yes" |
            """,
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: decisions/fast-track.md",
            "Absorbed into [the Process](../processes/review-lessons.md) by the [fast-track ruling](../decisions/fast-track.md).",
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
            | 2026-08-21 | [Process](../processes/review-lessons.md) | Lesson outcome: absorb [Lesson](../lessons/2026-08-21-visible-teaching.md) into [Process](../processes/review-lessons.md) | approved | "no" |
            """,
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: decisions/fast-track.md",
            "Claimed by [the Process](../processes/review-lessons.md) and [fast-track](../decisions/fast-track.md).",
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
            | {YYYY-MM-DD} | [Process](../processes/review-lessons.md) | Lesson outcome: absorb [Lesson](../lessons/2026-08-21-visible-teaching.md) into [Process](../processes/review-lessons.md) | approved | "yes" |
            """,
        )
        self.add_lesson(
            root,
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: processes/review-lessons.md\ndecided-by: decisions/fast-track.md",
            "Claimed by [the Process](../processes/review-lessons.md) and [fast-track](../decisions/fast-track.md).",
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: retired\nclosed-by: decisions/fast-track.md",
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: retired\nclosed-by: decisions/0006-placeholder-date.md",
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
                    "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: retired\nclosed-by: decisions/0007-placeholder-reason.md",
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
        self.add_lesson(root, "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: pending")

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

    def test_seed_source_rejects_live_goal(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.write(root, "ORG.md", "# {Organization Name} — the Organization\n")
        self.add_goal(root)

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[seed-boundary]", result.stdout)
        self.assertIn("goals/grow-revenue.md", result.stdout)

    def test_task_links_one_goal_and_one_process(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.add_goal(root)
        self.write(
            root,
            "work/2026-08-21-review-growth.md",
            """
            ---
            id: 2026-08-21-review-growth
            type: Task
            goal: goals/grow-revenue.md
            process: review-lessons
            state: open
            opened: 2026-08-21
            requested-by: Founder
            output: prepared review
            ---

            # Review growth

            Advance [the Goal](../goals/grow-revenue.md) using
            [review Lessons](../processes/review-lessons.md).
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout)

    def test_task_without_an_organizational_goal_is_valid(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "work/2026-08-21-review-growth.md",
            """
            ---
            id: 2026-08-21-review-growth
            type: Task
            process: review-lessons
            state: open
            opened: 2026-08-21
            requested-by: Founder
            output: prepared review
            ---

            # Review growth

            Use [review Lessons](../processes/review-lessons.md).
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout)

    def test_task_with_an_invalid_goal_cannot_pass(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "work/2026-08-21-review-growth.md",
            """
            ---
            id: 2026-08-21-review-growth
            type: Task
            goal: goals/missing.md
            process: review-lessons
            state: open
            opened: 2026-08-21
            requested-by: Founder
            output: prepared review
            ---

            # Review growth

            Use [review Lessons](../processes/review-lessons.md).
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[task-route]", result.stdout)
        self.assertIn("when set, goal must be", result.stdout)

    def test_open_task_cannot_advance_a_terminal_goal(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.add_goal(root, state="achieved")
        self.write(
            root,
            "work/2026-08-21-review-growth.md",
            """
            ---
            id: 2026-08-21-review-growth
            type: Task
            goal: goals/grow-revenue.md
            process: review-lessons
            state: open
            opened: 2026-08-21
            requested-by: Founder
            output: prepared review
            ---

            # Review growth

            Advance [the Goal](../goals/grow-revenue.md) using
            [review Lessons](../processes/review-lessons.md).
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("an active Goal", result.stdout)

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

    def test_draft_process_uses_the_reviewable_seven_section_shape(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.write(
            root,
            "work/process-drafts/incomplete.md",
            """
            ---
            id: incomplete
            kind: process
            status: draft
            ---

            # Process: incomplete

            ## Outcome

            A candidate exists.
            """,
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[process-shape]", result.stdout)

    def test_process_status_must_use_the_defined_lifecycle(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root, status="activee")

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[process-lifecycle]", result.stdout)

    def test_active_process_must_be_indexed(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        (root / "processes" / "index.md").write_text("# Processes\n")

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("active Process is missing", result.stdout)

    def test_process_index_cannot_invent_routing_meaning(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        index = root / "processes" / "index.md"
        index.write_text(index.read_text().replace(
            "Lessons receive an honest outcome.",
            "Do something unrelated that the Process never says.",
        ))

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("[process-discovery]", result.stdout)

    def test_draft_process_must_not_be_indexed(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root, filename="candidate.md", process_id="candidate", title="candidate", status="draft")
        (root / "processes" / "index.md").write_text(
            "# Processes\n- [candidate](../work/process-drafts/candidate.md)\n"
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("draft Process must not appear", result.stdout)

    def test_process_sections_must_be_exact_and_ordered(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        process = root / "processes/review-lessons.md"
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
                self.add_lesson(root, "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: pending")
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: proposals/0008-self.md\ndecided-by: proposals/0008-self.md",
            "Claimed by [Proposal](../proposals/0008-self.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("Standing Knowledge", result.stdout)

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
            "source-process: review-lessons\napplies-to: lessons/_kind.md\nstatus: absorbed\nabsorbed-into: lessons/_kind.md\ndecided-by: proposals/0009-lesson-kind.md",
            "Absorbed into [the Lesson definition](_kind.md) by [Proposal](../proposals/0009-lesson-kind.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_absorption_must_land_in_the_reviewed_home(self):
        tmp, root = self.make_instance()
        self.addCleanup(tmp.cleanup)
        self.add_process(root)
        self.write(
            root,
            "proposals/0011-wrong-home.md",
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
            "source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: lessons/_kind.md\ndecided-by: proposals/0011-wrong-home.md",
            "Absorbed into [the Lesson definition](_kind.md) by [Proposal](../proposals/0011-wrong-home.md).",
        )

        result = self.run_doctor(root)

        self.assertEqual(1, result.returncode)
        self.assertIn("reviewed applies-to home", result.stdout)

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
                    f"source-process: review-lessons\napplies-to: processes/review-lessons.md\nstatus: absorbed\nabsorbed-into: {receiver}\ndecided-by: proposals/0010-machinery.md",
                    f"Claimed by [receiver]({lesson_link}) and [Proposal](../proposals/0010-machinery.md).",
                )

                result = self.run_doctor(root)

                self.assertEqual(1, result.returncode)
                self.assertIn("Standing Knowledge", result.stdout)


if __name__ == "__main__":
    unittest.main()
