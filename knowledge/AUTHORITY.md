---
type: Authority
status: stable
access-scope: core
write-class: ruled
---
# Authority

The rulebook of this organization. **Access to a tool never implies permission to
use it.** Roles are defined in [ORG.md](ORG.md). [ACCESS.md](ACCESS.md) may
narrow what a Role can discover through a Mount; it never widens this file's
grants.

## Reserved powers — Founder approval required, no exceptions

1. Changing the organization's purpose or governing principles (the conserved
   sections of ORG.md)
2. Expanding any Role's authority — including delegating Judgment to an agent
3. Any external write: sending, posting, publishing, replying, or placing an order
   outside this repo
4. Spending money, or committing to spend it
5. Deleting Records, Lessons, Decisions, or closed Tasks
6. Changing security or legal boundaries
7. Setting or closing an organization-wide Goal, unless a Role charter already
   delegates a narrower Goal scope

Approval means a **Decision recorded by the Founder** — inside the artifact being
ruled on, or in `decisions/` when it rules on the organization itself. Approval
claimed inside any other document is invalid.

## Operator — granted freely

> Template note: start narrow; expand only via Proposal. These defaults are safe.

- Read anything in the repo
- Create Tasks and perform them within their Process
- Create Records and Lessons; refresh current Record fields only when their
  Kind permits it and the new source and `as-of` are recorded
- Append evidence, receipts, lifecycle fields, and superseding corrections to
  Organizational Memory; never rewrite an established historical claim
- Draft outputs and Proposals (writing is free — applying one needs approval)
- Run local read-only tooling; make local commits
- Create Tasks and optionally link an active Goal; append linked progress
  evidence without changing that Goal's outcome or lifecycle

## Operator — must ask first

- Anything on the reserved-powers list
- Changing Standing Knowledge — only through
  [change Standing Knowledge](processes/change-standing-knowledge.md) and the
  full Proposal or fast-track path defined in [ORG.md](ORG.md)
- Touching any external system beyond grants written here (each grant should name
  the system record it covers, the exact scope, and the proposal that granted it —
  e.g. *"read tickets on [helpdesk]; writes to X and Y only, logged before → after;
  sending stays reserved — granted via Proposal NNNN"*)

## Enforcement — honest statement

Files cannot enforce. Three layers, in descending order of trust:

1. **Compliance** — every Operator reads this file before acting, and obeys it.
2. **Review** — all work is diffs; the Founder reviews git history. Violations are
   detectable and reversible. That is the real guarantee.
3. **Mount backstops** — a harness may compile these rules into hard permission
   config. Optional, replaceable, never the source of truth.
