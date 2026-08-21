---
id: _kind
kind: kind-definition
of: lesson
status: active
---

# Kind: Lesson

A Lesson preserves what performed work taught. It changes no behavior by
itself. Each Lesson is one Markdown file named
`YYYY-MM-DD-what-it-teaches.md`.

This lifecycle becomes live in an Instance. The Seed source ships this
definition but carries no live Lesson members; Seed-maintenance evidence stays
in reviewed PRs, Git history, and ADRs.

**Required frontmatter:** `id`, `kind`, `date`, `process`, and `status`. `kind`
is **lesson**; `process` names one active Process. `status` is **pending**,
**absorbed**, or **retired**.

The body records what happened, what it teaches, the evidence, and where the
teaching should be applied. A Lesson that cannot name a Process is not ready
for the Process-improvement queue.

## Outcomes

Run [improve a Process](../processes/improve-a-process.md) for all pending
Lessons routed to one Process. Each Lesson receives one outcome:

- **Absorb:** move the teaching into its current home. Set `status: absorbed`,
  add root-relative `absorbed-into:` and `decided-by:` paths, and reduce the body
  to a short link to both files. Git keeps the original detail. The approval
  receipt records `lesson-outcome: absorb` and links the exact Lesson and
  receiver.
- **Keep:** leave `status: pending` and record why more evidence or time is
  needed.
- **Reroute:** change `process:` to the Process that owns the teaching and keep
  `status: pending`.
- **Close:** set `status: retired`, add a root-relative `closed-by:` path, and
  preserve a non-placeholder `## Closure reason`. The approval receipt records
  `lesson-outcome: close` and links that exact heading as
  `lesson-file.md#closure-reason`.

For absorption, the receipt is either an applied Proposal with a Founder-ruled
approved Ruling or the exact row in the fast-track ledger. Closure may also use
a standalone Founder-ruled Decision. Absorption and closure are valid only when
the receipt approves the exact Lesson outcome. Age, a filename mention, or an
unapproved field never removes a Lesson from the queue.
