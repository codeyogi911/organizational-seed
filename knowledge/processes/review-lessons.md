---
id: review-lessons
type: process
state: active
judge: Founder
description: Decide whether pending Lessons should be absorbed, kept, rerouted, or closed.
status: stable
access-scope: core
write-class: conserved
---

# Process: review Lessons

## Outcome

Every selected Lesson has an honest visible outcome. Useful teaching is either
queued for its exact Standing Knowledge home or remains pending with a reason;
weak teaching is never forced into future behavior merely to shrink a queue.

## When to use

Use when the doctor reports pending Lessons, a review finds accumulated
teaching, or the Founder asks what the organization should learn from previous
work.

## Boundaries

- Give every selected Lesson one outcome: **absorb**, **keep**, **reroute**, or
  **close**.
- A Lesson is Organizational Memory, not Standing Knowledge. It changes no
  behavior by itself.
- Absorption moves teaching into one current home; it does not copy the full
  teaching into multiple files.
- Keep uncertain teaching pending. Reroute it to the correct proposed home.
  Close only when it is no longer useful, with a preserved reason.
- This Process decides Lesson disposition. The governed mutation itself uses
  [change Standing Knowledge](change-standing-knowledge.md).

## Evidence and approvals

Read each Lesson, the Task and Records behind it, its proposed receiving home,
and contrary evidence. Keep and reroute need no completion ruling because they
remain pending. Absorption requires the exact approved Standing Knowledge diff.
Closure requires a Founder-approved receipt linking the Lesson's preserved
reason.

## Steps

1. Select a coherent group of pending Lessons, normally those naming the same
   proposed home.
2. Verify the evidence behind each Lesson and whether the proposed home is the
   smallest correct owner.
3. Record absorb, keep, reroute, or close with a short reason.
4. For absorb, preallocate the stable Decision path, then prepare one Change
   Standing Knowledge candidate containing the receiver mutation and the exact
   Lesson terminal bytes: `state: absorbed`, matching `applies-to:` and
   `absorbed-into:`, `decided-by:` that Decision, and short links to both files.
5. For close, prepare one candidate containing `state: retired`, `closed-by:`
   the preallocated Decision, and a non-placeholder `## Closure reason`. The
   receipt links that exact heading. Keep and reroute stay pending.
6. Run the repository checks and report what remains pending.

## Done when

- Every selected Lesson has one visible outcome.
- Absorbed teaching has one current Standing Knowledge home and an exact
  approval receipt.
- Closed teaching preserves why it was closed and who approved closure.
- Anything uncertain remains visible as pending.
- A no-change result is valid; the queue may remain unchanged.

## Failure and recovery

Pending Lessons and the branch diff are the recovery point. On resume, re-read
their evidence and current proposed homes. A changed receiving diff requires
fresh review and approval. Never lower the queue with a filename mention,
completion field, hidden file, or silent deletion.
