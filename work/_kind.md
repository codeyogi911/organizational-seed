---
id: _kind
kind: kind-definition
of: work-note
status: active
description: An optional durable checkpoint for work that outlives one sitting — not a mandatory record of every performance.
node-role: work
context-scope: episodic
---

# Kind: work note

A **work note** is `work/<YYYY-MM-DD>-<slug>.md`, and it is **optional**.

Write one when work is long-running, resumable, externally effectful, or
otherwise needs a durable checkpoint outside Git commits. A short read-only
answer or a focused repository change does not need one — the commit is already
the record, and a note that only restates the commit is a second home for the
same fact.

This is a deliberate reversal. An earlier version of this pattern required a
file per performance, on the theory that the organization should be able to
replay any piece of work. What it produced instead was a directory of
low-signal stubs that nobody read, and a tax on exactly the small interactions
that should be cheap. Git history already answers "what happened"; a work note
earns its place only when it answers something Git cannot.

## What a useful note records

- **Intent** — bounded, in the requester's own words.
- **Current state** — enough that a different operator could resume cold.
- **Evidence** — what was read, from where, and as of when.
- **Decisions** — including any one-time approval and its
  [record shape](../AUTHORITY.md#one-time-decision-record).
- **Recovery** — what a retry must re-read before acting, and what must not be
  repeated.
- **Outcome** — what landed, verified from the owning system.

It does **not** duplicate its Process. Link to the Process; do not copy its
steps.

## Identity and liveness

`<YYYY-MM-DD>-<slug>`, named for the work, not the Process. A note is finished
when its outcome is recorded; it is not deleted afterwards, because a completed
note is the cheapest evidence that an external effect was performed and
verified.

## Not a lease

A work note claims nothing and locks nothing. Repository concurrency is Git's
job — a change-specific worktree and branch, merge conflicts, and
non-fast-forward rejection
([ADR 0003](../docs/adr/0003-git-owns-repository-concurrency.md)). External
systems are protected by the
[write discipline](../docs/write-discipline.md), not by a file in this
directory.
