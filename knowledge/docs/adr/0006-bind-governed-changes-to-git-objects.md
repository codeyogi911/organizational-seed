---
state: accepted
type: Architecture Decision
status: stable
access-scope: core
write-class: ruled
---

# Bind governed changes to Git objects

## Decision

Every Instance Standing Knowledge mutation uses one exact-candidate Founder
Decision contract. The candidate is a target-only commit `A` whose parent,
complete path set, and before/after bytes are preserved in Git. The Founder surface
shows that immutable candidate and rules yes or no. The repository-native
Decision binds the immutable repository identity, fully qualified base ref,
base SHA, candidate SHA, target set, and canonical target-diff SHA-256.
It declares `governance-protocol: mainmind-exact-v1`, separating this exact
mutation receipt from generic organizational Decisions that record rulings but
do not claim governed bytes or Lesson lifecycle outcomes.

Approval appends deterministic Decision-only child `B` to `A` and uses an
ordinary merge retaining both. Rejection never integrates `A`; it closes the
candidate unmerged and appends only the refusal Decision to the canonical
branch. Mainmind allocates the stable Decision path before `A`, allowing a
terminal Lesson in `A` to point to it while `B` still changes only the Decision
file. The receipt contains no hash of `B` or the later merge, so its own bytes
do not depend on a Git object that cannot exist yet. Governed deletion uses
complete before bytes and a null after hash; rename is a create plus delete.

## Why

The previous Proposal file and fast-track ledger bound Judgment to mutable text
and two different ceremonies. That works when one owner operates a checkout but
does not safely serve a team whose agents have only scoped MCP access. One Git
contract makes approval portable, rejection durable, crash recovery
deterministic, and independent verification possible without granting working
agents GitHub credentials.

## Consequences

- Mainmind or equivalent Machinery may prepare candidates and carry rulings,
  but Git and the repository Decision remain canonical.
- Power-expanding and non-expanding changes use the same byte-binding standard.
- Direct Lessons and Records remain typed `ledger` deposits and need no Founder
  ruling unless their active Process or Authority says otherwise.
- A shallow plain clone verifies the durable receipt schema and binding
  identifiers. An auditor with the candidate objects can additionally
  recompute the target digest and prove ancestry.
