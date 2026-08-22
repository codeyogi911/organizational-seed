---
id: change-standing-knowledge
type: process
state: active
judge: Founder
description: Create, correct, improve, merge, rename, or retire knowledge that future work must follow.
status: stable
access-scope: core
write-class: conserved
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
- Every mutation uses the same exact-candidate contract. Creating or widening
  power changes who must read the diff; it never weakens the receipt.
- In the Seed source, maintainer branch and pull-request review replaces a live
  Instance Decision artifact.
- This Process changes repository knowledge, not external business systems.

## Evidence and approvals

Read [the knowledge model](../KNOWLEDGE.md), the current canonical home, its
authoring contract, cited evidence, and relevant history. In an Instance, the
Founder rules on one immutable candidate commit, complete target set, and
target-diff digest; an independent reviewer checks the exact before/after bytes.
In the Seed source, the reviewed pull request is the approval receipt.

## Steps

1. Name the target and operation: create, correct, improve, merge, rename, or
   retire.
2. Confirm the target is Standing Knowledge and identify its one current home.
3. State why it should change using direct evidence, Founder intent, a reviewed
   Lesson, or an evidenced draft.
4. In an Instance, prepare target-only candidate `A` as one direct child of the
   recorded base on the recorded repository and fully qualified base ref.
   Preallocate its stable Decision path before constructing any terminal Lesson
   target. Record the complete target set and target-diff SHA-256. Deletion binds
   complete before bytes to a null after hash; rename binds one create and one
   delete. In the Seed source, use a change-specific branch and maintainer pull
   request instead.
5. Review the diff through [AUTHORING.md](../AUTHORING.md), including the
   target Kind's contract. Run mechanical checks.
6. Obtain the required Instance ruling or Seed maintainer review for those exact
   bytes. On approval append deterministic Decision child `B` to `A`, then use
   an ordinary merge retaining both commits. On rejection close the candidate
   unmerged and append only its Decision to the canonical branch. Record the
   reason and rollback. Only an integrated change completes linked Lesson
   absorptions. A lifecycle candidate includes the terminal Lesson and receiver
   targets required by the Decision contract; `B` still adds only its Decision.

## Done when

- The exact candidate, complete target set, and target-diff digest have the
  required ruling or maintainer review and a recorded integrated or rejected
  outcome.
- If integrated, the new Standing Knowledge has one current home, replaced live
  copies are removed, linked Lessons and drafts show their resulting state, and
  rollback names the integrating commit plus any irreversible effect.
- If rejected, the prior Standing Knowledge remains in force, linked Lessons
  stay pending, and the rejection reason is preserved.
- In either outcome, history remains truthful and the checks report no hidden
  partial application.

## Failure and recovery

The immutable candidate and repository-native Decision are the recovery point.
If any target byte changes after review or ruling, obtain fresh review and
approval. Recover approval only when Git proves `base → A → B` and the ordinary
merge retains `B`. Recover rejection only when the candidate is unmerged and
the canonical Decision-only commit matches its deterministic bytes. Otherwise
stop. Rejection leaves the prior Standing Knowledge in force and records why
the candidate did not replace it.
