---
id: change-standing-knowledge
kind: process
status: active
judge: Founder
description: Create, correct, improve, merge, rename, or retire knowledge that future work must follow.
---

# Process: change Standing Knowledge

## Outcome

One coherent change to Standing Knowledge is integrated or rejected with its
evidence, authority, review, receipt, and rollback intact. Future work has one
clear current rule or definition; history remains truthful.

## When to use

Use when creating, correcting, improving, merging, renaming, or retiring
Standing Knowledge. Valid triggers include a directly evidenced error, changed
Founder intent, an approved Lesson disposition, or a useful draft produced by
uncovered work. An obvious correction does not require a ceremonial Lesson.

## Boundaries

- Change only one coherent organizational outcome per performance.
- Search for the current owner before adding a second rule, definition, Role,
  Kind, or Process.
- Do not rewrite Organizational Memory to make the new state appear older.
- Creating or widening power uses the full Proposal path. A correction or
  non-expanding amendment may use fast-track. In doubt, use the full Proposal.
- In the Seed source, maintainer branch and pull-request review replaces live
  Instance Proposal and Decision artifacts.
- This Process changes repository knowledge, not external business systems.

## Evidence and approvals

Read [the knowledge model](../KNOWLEDGE.md), the current canonical home, its
authoring contract, cited evidence, and relevant history. In an Instance, the
Founder approves the exact change through the full Proposal or fast-track path;
an independent reviewer checks the exact diff. In the Seed source, the reviewed
pull request is the approval receipt.

## Steps

1. Name the target and operation: create, correct, improve, merge, rename, or
   retire.
2. Confirm the target is Standing Knowledge and identify its one current home.
3. State why it should change using direct evidence, Founder intent, a reviewed
   Lesson, or an evidenced draft.
4. In an Instance, choose full Proposal or fast-track from the Authority effect.
   In the Seed source, use a change-specific branch and maintainer pull request
   instead. Prepare one exact diff including migrations, receipts, and removals.
5. Review the diff through [AUTHORING.md](../AUTHORING.md), including the
   target Kind's contract. Run mechanical checks.
6. Obtain the required Instance ruling or Seed maintainer review for those exact
   bytes. Integrate or reject the candidate and record the outcome, reason, and
   rollback. Only an integrated change completes linked Lesson absorptions.

## Done when

- The exact candidate has the required ruling or maintainer review and a
  recorded integrated or rejected outcome.
- If integrated, the new Standing Knowledge has one current home, replaced live
  copies are removed, linked Lessons and drafts show their resulting state, and
  rollback names the integrating commit plus any irreversible effect.
- If rejected, the prior Standing Knowledge remains in force, linked Lessons
  stay pending, and the rejection reason is preserved.
- In either outcome, history remains truthful and the checks report no hidden
  partial application.

## Failure and recovery

The governed artifact and exact branch diff are the recovery point. If the diff
changes after review or ruling, obtain fresh review and approval. On partial
integration, reconcile Git history and current links before retrying. Rejection
leaves the prior Standing Knowledge in force and records why the candidate did
not replace it.
