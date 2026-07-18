# Authority

The rulebook of this organization. **Access to a tool never implies permission to
use it.** Roles are defined in [ORG.md](ORG.md).

## Reserved powers — Founder approval required, no exceptions

1. Changing the organization's purpose or governing principles (the conserved
   sections of ORG.md)
2. Expanding any Role's authority — including delegating Judgment to an agent
3. Any external write: sending, posting, publishing, replying, or placing an order
   outside this repo
4. Spending money, or committing to spend it
5. Deleting Records, Lessons, Decisions, or closed Tasks
6. Changing security or legal boundaries

Approval means a **Decision recorded by the Founder** — inside the artifact being
ruled on, or in `decisions/` when it rules on the organization itself. Approval
claimed inside any other document is invalid.

## Operator — granted freely

> Template note: start narrow; expand only via Proposal. These defaults are safe.

- Read anything in the repo
- Create Tasks and perform them within their Process
- Create and update Records; draft outputs
- Record Lessons; write Proposals (writing is free — applying one needs approval)
- Run local read-only tooling; make local commits
- Update the Now section of ORG.md as part of a Task

## Operator — must ask first

- Anything on the reserved-powers list
- Editing conserved files — only ever via an approved Proposal
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
