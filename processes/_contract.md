---
id: _contract
kind: process-contract
status: active
judge: Founder
contract-version: simple-v1
description: The shape every Process file must have — seven sections, what each is for, what makes each wrong, and how a draft graduates without earning Authority by repetition.
---

# The Process contract

> **Template note:** this file is generic. Keep it as-is when you fork; the
> only things worth changing are thresholds you decide differently, and they
> are marked `{like this}`. Delete this note.

This is the authoring shape for a new Process, and for an existing Process the
next time it is substantively amended. It is not itself performable — there is
nothing here to run.

A **Process** is a durable way of working that a capable human could follow
with no agent present. It owns the outcome, the boundaries, the evidence, the
approvals and the done condition. Git owns its versions, review and rollback. A
harness may point at a Process; it may never restate or rewrite one
([MOUNTING.md](../MOUNTING.md)).

**A Process is changed only through a reviewed Git change and a Founder
Decision.** It is conserved
([ORG.md](../ORG.md#what-is-conserved--what-is-free)), and it stays conserved
when the edit is described as a correction. No performance amends the file it
ran from, however well that performance went.

## Frontmatter

| Field | Value |
|---|---|
| `id` | the filename slug |
| `kind` | `process`, or `doctrine` for a file that states invariants |
| `status` | `active`, `example` or `retired` |
| `judge` | the Role that rules its Judgment question — `Founder` by default |
| `contract-version` | `simple-v1` |
| `description` | one line of task language; the routing index shows this |

## The seven sections

Use them in this order. Keep them short. Add a numbered algorithm only where
order itself is the invariant — safety, accounting, legal, or an effect that
cannot be undone. Everywhere else use bullets and leave strategy free.

### Outcome

What must be true when a performance is finished, and why that matters to the
organization.

*Wrong when* it describes activity rather than a result ("review the numbers"),
or when it is drawn so wide that no performance could fail it.

### When to use

The request, observation, schedule or condition that selects this Process —
written in the task language a reader would actually search, not in the file's
own vocabulary.

*Wrong when* it reads "run the {reconciliation}" instead of "{the bank balance
does not match the books}". Also wrong when two Processes claim the same
trigger and neither says which one wins.

### Boundaries

The negative space. What this Process permits directly, what needs a one-time
Decision, and what it prohibits outright. Name the eligible Role where it
matters. Tool access is never permission.

*Wrong when* it lists only permissions. A Process with no prohibitions has no
boundaries, only a wish. Also wrong when it grants something `AUTHORITY.md`
reserves — the ceiling is not the Process's to raise.

### Evidence and approvals

Which current Records or external systems must be read, how fresh they must be,
what must be cited, which human approval is required before which effect, and
what receipt proves the effect landed. Link to changing facts; never copy them.

*Wrong when* it says "gather the relevant information" — that names no source
and no reader can settle it. Also wrong when it copies a figure or threshold
that already lives in another file.

### Steps

The smallest useful sequence, followable by a capable human with no agent and
no tooling of yours. Bullets where order does not matter.

*Wrong when* it encodes one operator's tools as the method, or when it
restates the Boundaries as steps — the boundary holds whether or not the step
is reached.

### Done when

Observable success and no-op conditions, settleable without judgment.

*Wrong when* a line needs judgment to settle ("the report is good"), or when
the performer can satisfy it by asserting it. A claimed success is not proof:
name the readback, artifact, receipt or check that proves it.

### Failure and recovery

The stable recovery key, what a resumed performance must re-read before acting,
how a partial effect is recovered, and the failure that must be reported
without compression.

*Wrong when* it is absent, which is the commonest defect in a Process that has
never failed yet. Also wrong when it ends at "retry" without naming the key
that makes a retry safe rather than a second effect.

## Drafts grant no Authority

A draft under `processes/draft/` is free to create and edit, absent from the
active index, and **grants no reusable Authority**. It uses five short
sections — **Outcome, Why, Do, Don't, Done-when** — and every external effect
during a draft performance therefore needs the one-time Decision its evidence
and the active Processes require.

**A draft becomes active when the Founder rules it real.** Branch, reviewed
diff, Decision file — the ordinary conserved path in
[EXECUTION.md](../EXECUTION.md#repository-changes). Rewrite it into the seven
sections, move it out of `draft/`, add its index row.

**Never a count.** No number of clean performances graduates a draft, and no
file should record such a number as if it would. Repetition is evidence that a
way of working is useful; it is not evidence that anyone approved it, and a bar
made of counts hands Authority to the least surprising thing in the world — a
routine that has not broken yet. The Founder may ask for more evidence before
ruling. That is Judgment, not a gate any file enforces.

Any operator may retire a draft after a strike and record the Lesson.

## Where the contract is silent

Anything the seven sections do not cover is strategy, and strategy is free
inside them. If a Process needs a rule that would bind other Processes too, it
belongs in a doctrine or in `AUTHORITY.md`, not in one Process's prose —
[AUTHORING.md](../AUTHORING.md) governs how it is written and reviewed.
