---
id: _kind
type: kind-definition
of: lesson
state: active
status: stable
access-scope: core
write-class: conserved
---

# Kind: Lesson

A Lesson preserves what performed work taught. It changes no behavior by
itself. Each Lesson is one Markdown file named
`YYYY-MM-DD-what-it-teaches.md`.

This lifecycle becomes live in an Instance. The Seed source ships this
definition but carries no live Lesson members; Seed-maintenance evidence stays
in reviewed PRs, Git history, and ADRs.

**Required frontmatter:** `id`, `type`, `date`, `source-process`, `applies-to`,
and `state`. `type` is **Lesson**; `source-process` names the Process whose
performance produced the teaching, even if that Process is now retired.
`applies-to` is a root-relative path
to the proposed Standing Knowledge home, or `unresolved` when review has not
found one. `state` is **pending**, **absorbed**, or **retired**. OKF `status`
records the broader stable, draft, or deprecated lifecycle.

The body records what happened, what it teaches, the evidence, and why the
proposed home may own it. A Lesson may remain unresolved; uncertainty stays
visible instead of being hidden in the wrong Process.

## Outcomes

Run [review Lessons](../processes/review-lessons.md) for pending Lessons,
normally grouped by `applies-to`. Each Lesson receives one outcome:

- **Absorb:** move the teaching into its current home. Set `state: absorbed`,
  set `applies-to:` and root-relative `absorbed-into:` to that same home, add a
  root-relative `decided-by:` path, and reduce the body to a short link to both
  files. Git keeps the original detail. The approval receipt records
  `lesson-outcome: absorb` and links the exact Lesson and receiver.
- **Keep:** leave `state: pending` and record why more evidence or time is
  needed.
- **Reroute:** change `applies-to:` to the correct proposed Standing Knowledge
  home, or to `unresolved`, and keep `state: pending`.
- **Close:** set `state: retired`, add a root-relative `closed-by:` path, and
  preserve a non-placeholder `## Closure reason`. The approval receipt records
  `lesson-outcome: close` and links that exact heading as
  `lesson-file.md#closure-reason`.

For absorption, [change Standing Knowledge](../processes/change-standing-knowledge.md)
supplies either an applied Proposal with a Founder-ruled approved Ruling or the
exact row in the fast-track ledger. Closure may also use a standalone
Founder-ruled Decision. Absorption and closure are valid only when the receipt
approves the exact Lesson outcome. Age, a filename mention, or an unapproved
field never removes a Lesson from the queue.
