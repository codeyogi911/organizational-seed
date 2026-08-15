---
status: accepted
mechanism-superseded-by: 0004-one-governance-route.md
---

# Directed evolution, not random

> The **principle** below stands unchanged. Its **mechanism** does not: the
> Proposal queue was retired in favour of a single route — a branch, a reviewed
> diff, and a Decision. See
> [ADR 0004](0004-one-governance-route.md). Read `proposals/` and `Checks`
> below as "the branch" and "the diff review".

The Instance must adapt — mutate, within the framework. Two models were considered.
Darwinian: agents freely rewrite governed files and problems are culled after the
fact — fast, and occasionally lethal (an agent silently rewriting its own
authority). Directed: a mutation is a Proposal carrying reason, evidence, expected
benefit, validation and rollback; selection (Checks + Founder Judgment) happens
*before* the mutation reaches the conserved core; Lessons make acquired traits
heritable. We chose directed. Accepted consequences: a slower mutation rate, and the
Founder as selection bottleneck until Judgment is explicitly delegated. No mutation
engines, variant machinery, or fitness scoring are built — git is the mutation log,
`proposals/` the queue, evaluation the filter.
