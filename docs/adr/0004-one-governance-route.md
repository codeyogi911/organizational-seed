---
status: accepted
supersedes: the two-tier governance mechanism in ADR 0002 (its principle stands)
---

# One governance route, not two

v0.2 shipped two tracks for changing a conserved file. A **full Proposal** —
reason, evidence, expected benefit, validation, rollback — for anything that
expanded power. A **fast-track** for conserved changes that expanded nothing:
state the diff, get the Founder's verbatim yes, one commit, and one line in
`decisions/fast-track.md`, batch-reviewed at the weekly review.

Both halves failed, in opposite directions.

The fast-track ledger was the load-bearing part of the light tier: it was what
made an unproposed conserved change reviewable after the fact. In live
operation the ledger stopped being read. A row in a table is not a reason — it
records *that* something was ruled, never *why* — so the weekly batch review had
nothing to review, and a growing set of conserved changes had no surviving
rationale. The tier that was supposed to be cheap-but-accountable turned out to
be cheap-and-unaccountable.

Proposals failed the other way. As a separate artifact class they duplicated
what a branch already is. A Proposal file described a change; the branch *was*
the change. Two representations of one thing drift, and the Proposal — written
first, merged later, rarely updated — was reliably the stale one. Worse, the
proposal queue accumulated: written freely, ruled rarely, and read as a backlog
of organizational intent that nobody had actually agreed to.

Decided: **one route.** A conserved change is a branch with a reviewed diff and
its own Decision file in `decisions/` carrying the Founder's verbatim ruling.
There is no lighter tier — a "small" conserved change still gets a Decision,
because writing down the reason is the cheap part and it is exactly the part
the ledger lost.

Consequences accepted:

- More Decision files. This is the point; each one is a paragraph explaining
  why, which is what the ledger row never was.
- The proposal-shaped questions (what is the evidence, what would we roll back
  to) do not disappear — they move into the Decision and the diff review in
  [AUTHORING.md](../../AUTHORING.md#changing-standing-context).
- **The pull request is transport, not the ruling.** A merge button is a
  repository event on someone else's server; the reason must live in the
  repository. A PR body may carry the discussion, but the Decision file is what
  survives.
- ADR 0002's principle — directed evolution, selection *before* a mutation
  reaches the conserved core — is unchanged. Only its mechanism moves: Git is
  still the mutation log, the branch is now the queue, and the Decision plus
  diff review is the filter.
