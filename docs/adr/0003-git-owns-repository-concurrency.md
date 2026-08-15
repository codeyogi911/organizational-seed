---
status: accepted
supersedes: the lease half of the concurrency convention (v0.2)
---

# Git owns repository concurrency

v0.2 gave concurrent operators an advisory lease: a file in `work/_active/`
naming the operator, the task and the claimed scopes, kept alive by a
heartbeat, breakable when stale. It was always described as collision
*avoidance* rather than collision *safety* — the write discipline was the real
guarantee — and live operation confirmed the weaker half was not earning its
cost.

Two things went wrong. Leases needed their own machinery to stay honest: stale
detection, break-with-a-record, self-re-read before every mutation batch, a
release path for a lease whose worktree no longer existed. And they duplicated,
in Markdown that nothing enforces, a job Git already does properly. A
change-specific worktree prevents dirty-tree and index collisions. A merge
conflict prevents silent integration over a changed base. A non-fast-forward
rejection prevents overwriting a branch that moved. Those signals are
mechanical, unfakeable, and free.

Decided: **for repository state, Git is the concurrency layer.** Every writer
uses a change-specific worktree and branch, refreshes from current `main`,
resolves conflicts explicitly, reruns checks, and never force-pushes. Path
leases, fencing epochs and Markdown lease receipts leave the default design.

This is scoped to the repository. **External systems still need the write
discipline** ([docs/write-discipline.md](../write-discipline.md)) in full:
deterministic references, the external system as the write-ahead log, fresh
pre-write reads, and one mutator per external system at a time. Git can
serialize edits to a file describing a payment. It cannot serialize the
payment.

Accepted consequence: two operators can still both be *right* about a file and
meet at a conflict a human must resolve. That is the intended failure mode — a
loud, local, recoverable stop, instead of a quiet overwrite that a lease would
only have made less likely.
