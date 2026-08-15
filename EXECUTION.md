# Working with this repository

This file defines the two practical paths: changing repository knowledge with
Git, and performing an external effect through a Process. It is not a runtime
or a permission engine.

## Repository changes

1. Start from current `main` in a change-specific worktree and branch.
2. Read `ORG.md`, `AUTHORITY.md`, the relevant Process or knowledge file, and
   the evidence the change needs.
3. Make the smallest coherent change. Preserve unrelated work and stage
   explicit paths.
4. Run focused checks, inspect the exact diff and commit a meaningful
   checkpoint.
5. Refresh from current `main`. Resolve a merge conflict explicitly and rerun
   the checks; never overwrite another branch's work.
6. Review the exact candidate diff. A conserved change also needs the required
   Founder Decision.
7. Integrate without force. The merge commit or fast-forwarded commit is the
   repository receipt; a revert is rollback.

Git owns repository concurrency. Separate worktrees prevent dirty-tree and
index collisions. Merge conflicts and non-fast-forward rejection prevent silent
integration over a changed base. Repository path leases, fencing epochs and
Markdown lease receipts are not part of this design — see
[docs/adr/0003-git-owns-repository-concurrency.md](docs/adr/0003-git-owns-repository-concurrency.md).

| Git artifact | Meaning here |
|---|---|
| Worktree and branch | isolated proposed change |
| Commit | checkpoint, evidence-bearing diff and durable receipt |
| Pull request | optional review and discussion transport |
| Decision file | ruling whose reason must survive independently |
| Merge or tag | integrated or named repository state |
| Revert | explicit rollback |

Git review is not business Authority. It governs repository integration only.
For a conserved change without a retained pull request, its durable Decision
names the independent reviewer, verdict, exact reviewed commit or diff, and
resulting commit. This is review evidence, not a separate approval ceremony.

## External effects

Git cannot authorize a payment, send an email or verify an external fact. For
an effect outside this repository:

1. Find and read the applicable Process.
2. Read fresh facts from the external system named by that Process.
3. Check `AUTHORITY.md` and the Process's permitted, approval-required and
   prohibited effects.
4. When required, obtain and record the explicit one-time human Decision in
   [AUTHORITY.md's bounded shape](AUTHORITY.md#one-time-decision-record).
5. Perform the effect through the relevant capability adapter, using a stable
   target and idempotency reference where the platform supports one.
6. Re-read the external system to verify the outcome.
7. Record the result, source, timestamp, uncertainty, Decision status and
   consumption evidence in the Process's normal output.

A tool result is evidence only after its target and outcome are verified. A
draft or proposed effect is not a completed effect.

## Optional work notes

Use `work/<date>-<slug>.md` when work is long-running, resumable, externally
effectful or otherwise needs a durable checkpoint outside Git commits. A short
read-only answer or focused repository change does not require one.

A useful work note records intent, current state, evidence, decisions, recovery
and outcome. It does not duplicate the Process.

## Completion

Work is complete when its promised result exists, cited evidence supports its
claims, relevant checks pass, external effects have verified receipts, and
useful new knowledge has a current home.

Possible durable residue:

- a Record for a fact or outcome;
- a Lesson for reusable learning;
- a corrected Process;
- a draft Process for a likely repeated pattern;
- a Decision for changed future behavior; or
- a focused commit when Git history is sufficient.

## Process lifecycle

Process discovery, drafting, graduation, evidence of use, correction and
retirement are defined once in
[ORG.md § Process discovery and reinforcement](ORG.md#process-discovery-and-reinforcement).
Any generated process index is a routing view over the Markdown, never a
second source of truth.

## A recurring effect must name the Process that will hold it

A proposed change that asks for a schedule, a harness binding, or any effect
that repeats must name the Process whose permissions will hold it — one it
widens, or one it creates in the same change.

Recurring operational Authority lives in an approved Process and nowhere else.
A one-time Decision cannot carry it, and a scheduled binding that names no
Process would end up carrying policy of its own — which is precisely what a
Mount may not do.

*"This adds no Process"* and *"this adds a recurring job"* cannot both be true.
When a change declares the first while requesting the second, the declaration
is the defect.

## Adapter seam

Harnesses and generated graphs are replaceable navigation adapters. Capability
adapters perform external reads and effects but supply no Authority.

## Delegation

Helpers receive the smallest question and context they need. Delegation changes
neither Authority nor the human approval boundary, and the primary operator
remains responsible for verifying the integrated result.
