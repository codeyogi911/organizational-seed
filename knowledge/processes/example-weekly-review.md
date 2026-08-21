---
id: example-weekly-review
type: process
state: example
judge: Founder
description: Adapt this worked example into an Instance's first recurring Process.
status: stable
---

> **Template note:** a worked example showing the shape every Process shares —
> one outcome, clear boundaries, evidence, human-followable steps, mechanical
> Checks, and one Judgment question. Adapt it to your first real recurring pain,
> rename it, set `state: active`, and delete this note. (New Processes after
> this one use [change Standing Knowledge](change-standing-knowledge.md).)

# Process: weekly review (example)

## Outcome

The Founder has a short, evidence-backed view of what changed, what needs a
decision, and what should happen next.

**Standing intent:** "{quote the Founder's actual words for why this Process
exists}."

## When to use

Use weekly, or when the Founder asks for the same review. The cadence lives
here; triggering is machinery — a human habit or a separately approved
scheduler Mount.

## Boundaries

- Read only the Records and Systems authorized by [AUTHORITY.md](../AUTHORITY.md).
- Recommend at most three actions, each traceable to a finding.
- Do not make an external change while performing this review unless another
  Process and approval separately authorize it.

## Evidence and approvals

Name every input and its freshness. Every claim cites a Record. The Founder
answers: **"Does this reflect reality, and would I act on these
recommendations?"** Record the ruling and rejection reasoning verbatim in the
Task.

## Steps

1. Open a Task in `work/` (id `YYYY-Www-weekly-review`), status `open`; record
   `performed-by`; quote the standing intent. Update [NOW.md](../NOW.md).
2. Gather inputs — name them explicitly, with staleness noted: which records, which
   system reads (under what grant in [AUTHORITY.md](../AUTHORITY.md)).
3. Produce the output as a Record. **Every claim cites the records that support
   it** — an uncited claim is unverified by definition.
4. Recommend actions inside the boundary above.
5. Run the done checks below by hand or with `tools/doctor`; set the Task to
   `checked` only when they pass.
6. Present the result for Founder Judgment and record the ruling.
7. Record a Lesson if anything was learned. Route Process teaching through
   [review Lessons](review-lessons.md).

## Done when

- Task frontmatter is valid (`id`, `type: Task`, `process`, `state`, `opened`,
  `requested-by`, `output`); intent quoted; output exists.
- Every claim in the output carries at least one citation; all relative links
  resolve.
- Recommendations are at most three, each citing a finding.
- No external write occurred beyond the grants in `AUTHORITY.md`.
- The Founder ruling is recorded, or the Task clearly remains `checked` and
  waiting for it.

## Failure and recovery

The Task is the checkpoint. After interruption, refresh every input whose
source may have changed, rerun the checks, and present the current result. Never
reuse a ruling for a changed output.
