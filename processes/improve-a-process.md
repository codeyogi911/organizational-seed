---
id: improve-a-process
kind: process
status: active
judge: Founder
description: Improve one Process by deciding what to do with every Lesson waiting for it.
---

# Process: improve a Process

## Outcome

One Process has a safe improvement outcome. Approved teaching now lives in the
exact step, boundary, check, or definition that future work will read; teaching
that is not ready remains visible with a reason. Every Lesson considered has a
visible outcome. The queue shrinks when absorption or closure is justified and
may stay unchanged when keep or reroute is the honest result.

## When to use

Use when the doctor reports Lessons waiting for a Process, a review finds a
Lesson backlog, or the Founder asks to improve a Process from experience.

## Boundaries

- Review one target Process and all pending Lessons routed to it.
- Give every Lesson one outcome: **absorb**, **keep**, **reroute**, or **close**.
- A Lesson is evidence, not a rule. It changes future work only through an
  approved edit to the Process or other current home that owns the behavior.
- Absorb by moving the teaching, not copying it. Keep weak teaching pending;
  reroute it to the Process that owns it; close only when it is no longer
  useful, with the reason preserved and an approval receipt.
- In an Instance, only the Founder may approve a conserved Process change. This
  Process makes no external business-system change.

## Evidence and approvals

Read the current target Process, every pending Lesson routed to it, and the
Tasks, Records, Decisions, or Git history needed to verify the teaching. In an
Instance, the Founder approves the exact Process diff and Lesson outcomes. An
independent reviewer checks the exact diff before integration. The approval
receipt records the exact `absorb` or `close` outcome and links the Lesson and,
for absorption, its receiving file.

## Steps

1. Choose one target Process. Collect every Lesson whose `process:` names it
   and whose `status:` is `pending`.
2. Read the evidence behind each Lesson. Record **absorb**, **keep**,
   **reroute**, or **close**, with a short reason.
3. Put absorbed teaching in the smallest correct current home. A link alone is
   not absorption.
4. Prepare one coherent diff covering the Process change and every Lesson
   outcome. An absorption or other conserved edit uses the Instance's full
   Proposal or fast-track path. A closure-only outcome may instead use a
   standalone Founder Decision. Keep and reroute stay pending and need no
   completion receipt.
5. Apply only the approved change. For absorption, leave a short Lesson
   tombstone linking `absorbed-into:` and `decided-by:`. For closure, record
   `status: retired`, `closed-by:`, and a non-placeholder `## Closure reason`.
   Rerouted or kept Lessons remain pending.
6. Run the repository checks and report the queue before and after.

## Done when

- Every selected Lesson has one recorded outcome.
- Approved teaching has one current home; the full teaching is not copied in
  both the Process and Lesson.
- Each absorption or closure carries its required approval receipt.
- Checks pass, the exact diff is reviewed, and anything still pending remains
  visible with its reason.
- A no-change result is valid when the evidence supports only keep or reroute;
  never absorb or close merely to reduce the count.

## Failure and recovery

The branch diff is the recovery point. After interruption, refresh the target
Process and its pending Lessons, then recheck any earlier ruling against the
exact diff. A changed diff needs fresh review. Weak evidence stays pending;
never lower the queue with a filename mention, a false completion field, or a
silent deletion.
