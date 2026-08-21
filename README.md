# Organizational Seed

Run an organization as a folder of plain files — operable by a human with a text
editor, accelerated by any AI coding agent, owned by neither.

Traditional software freezes an organization's workflows into applications. Now that
software can be generated and modified by agents, the durable asset is no longer the
app — it is the organization's own state: purpose, authority, processes, work,
evidence, decisions, and lessons. This seed keeps all of that as Markdown + YAML in a
git repo, and treats every agent, model, script, and scheduler as replaceable
machinery.

## The pitch

**Your business, as a folder any AI agent can run — and none can run away
with.** Software used to freeze your workflows into apps; now agents can
generate software, so the durable asset is your organization itself: purpose,
authority, processes, evidence, decisions. The seed keeps all of it in plain
files under git. Agents are hired like staff — chartered roles with narrow
grants, hard boundaries, probation — and fired by deleting a file. You stay
the judge: nothing spends, sends, signs, or files without you. Start with one
painful recurring process, not a migration; your existing tools keep running.
It's proven, not theoretical: a real eight-figure (INR) business runs on it
today — books reconciled to the paisa, every marketplace refund provably
credit-noted from the right account, support drafted every morning before the
owner wakes up. Fork the seed. Keep the judgment. Delegate the rest.

**The thesis:** the seed is the genotype; everything else is phenotype.
Harnesses, models, and SaaS systems are expression machinery — they improve
every quarter, and because the organization's identity lives in files and not
in any of them, every improvement anywhere in the stack is captured as a free
upgrade. The org rides every curve and is owned by none. Roadmap:
[knowledge/docs/ROADMAP.md](knowledge/docs/ROADMAP.md).

**Origin:** extracted from a living instance that runs a real e-commerce business —
its purchase orders, support desk, books reconciliation, and governance all flow
through this exact structure daily. The pattern is published; the business stays
private.

**v0.2** folds back what sustained live operation taught: chartered agent Roles
(`knowledge/roles/_charter-template.md` — narrow grants, hard boundaries, probation), the
concurrency convention (session leases + fencing + deadman checks; `knowledge/work/_active/`),
two-tier governance (full Proposals only where power grows; `knowledge/decisions/fast-track.md`
for everything else), and the write discipline that makes crashed or colliding agents
recoverable by design ([knowledge/docs/write-discipline.md](knowledge/docs/write-discipline.md)). All of
it was forced by real failures — concurrent agents in one ledger, mid-write crashes,
silent schedule deaths — not designed in advance.

## The knowledge model

Every artifact answers where it came from and whether it is Knowledge or
Machinery. The Seed supplies a reusable baseline; an Instance owns its current
copy and may add business-specific Knowledge. Origin never creates continuing
upstream Authority. Knowledge is Standing Knowledge, Organizational Memory, or
Working State. Machinery sits outside Knowledge and may only read, check,
project, or present it. See the
[architecture at a glance](knowledge/KNOWLEDGE.md#architecture-at-a-glance);
[knowledge/KNOWLEDGE.md](knowledge/KNOWLEDGE.md) is the canonical map.
For the delivery view, see how
[intent and sessions route through the architecture](knowledge/docs/context-routing-and-role-scale.md)
and how one substrate produces bounded views for different Roles.

## The loop

Every piece of work travels the same path:

1. A human expresses bounded **intent** (ephemeral — never a filed artifact).
2. The intent becomes a **Task** under one **Process**. It links a **Goal** only
   when it advances durable organizational direction.
3. A human or agent performs it; every claim in the output **cites Records**.
4. Mechanical **Checks** verify coherence (no LLM required); a human rules the
   **Judgment**.
5. **Lessons** are recorded and handled through
   [review Lessons](knowledge/processes/review-lessons.md): absorb, keep, reroute, or
   close. Any resulting governed mutation uses
   [change Standing Knowledge](knowledge/processes/change-standing-knowledge.md).

Intent with no matching Process is not an error. Use
[handle uncovered work](knowledge/processes/handle-uncovered-work.md) for the smallest
safe result; leave a draft only when recurrence is plausible. Making that draft
active is one operation of Change Standing Knowledge.

## Seed and Instance knowledge

The Seed ships **Seed Processes** that maintain the knowledge system itself:
handle uncovered work, review Lessons, and change Standing Knowledge. These are
baseline habits, not continuing upstream control.

Each organization adds **Instance Processes** for its own work: handling
support, buying stock, closing books, or anything else specific to it. An
Instance may also change a Seed Process through its own approval rules. Once
the Instance exists, its copy is sovereign: a later Seed update is only a
candidate for review and is never applied automatically.

This repository is the source of the Seed, not a live Instance. Seed
maintainers change the template through branches and reviewed pull requests;
they do not create an in-template Proposal to authorize editing the template.
Seed-maintenance evidence stays in issues, PRs, Git history, and ADRs rather
than live Task, Lesson, Proposal, or organizational Decision entries. Those
runtime rules become live when the Seed is instantiated.

## Principles that keep it honest

- **Bindings, not homes.** Skills, agent files, and connectors point at durable
  state; they never own it. Delete every mount and the organization still runs.
  ([ADR 0001](knowledge/docs/adr/0001-bindings-not-homes.md))
- **Standing Knowledge is governed.** In an Instance, anything future work must
  obey or interpret consistently changes only through its approved Proposal or
  fast-track path. Seed source changes use maintainer PR review.
- **Access is not permission.** A connected tool grants nothing; only `knowledge/AUTHORITY.md`
  does. External writes and spending always stop at a human boundary.
- **Evidence is a citation discipline.** A claim without a citation is unverified by
  definition; checks are runnable by hand.
- **Systems are federated, not migrated.** Gmail, your ERP, your helpdesk keep
  owning their data; the seed records who owns which truth
  ([knowledge/records/systems/](knowledge/records/systems/_kind.md)) and governs how it may be touched.
- **Lessons weigh what their evidence weighs.** Recurring evidence upgrades a
  lesson; a closed one-off decays. Scar tissue is audited, not accumulated.

## Quick start — grow a new organization

1. **Use this template** (GitHub → "Use this template", or clone).
2. **Write your `knowledge/ORG.md`** — fill every `{placeholder}`: purpose, a
   Founder and an Operator role. If the organization needs a durable Goal,
   create it under `knowledge/goals/` using its `_kind.md` definition.
3. **Keep `knowledge/AUTHORITY.md`'s reserved powers** (they travel well verbatim); write your
   Operator grants.
4. **Enumerate your external systems** as `knowledge/records/systems/` entries — what each is
   the source of truth for, what access exists. This moves no data; adoption is
   acknowledgment, not migration.
5. **Write one process** for one real recurring pain, using
   [knowledge/processes/example-weekly-review.md](knowledge/processes/example-weekly-review.md) as the
   shape. Put the candidate under `knowledge/work/process-drafts/`, then use
   [change Standing Knowledge](knowledge/processes/change-standing-knowledge.md) with a
   full Proposal and Founder ruling to make it active under `knowledge/processes/`.
6. **Run the loop once** — intent → Task under one Process → evidence-cited
   output → Checks → your Judgment → Lesson. Link a Goal only when relevant.
   Review the Lesson when its evidence warrants it; do not create a Proposal
   merely because a Lesson exists.
7. **Point your agent at it.** Any coding agent that reads `AGENTS.md` (or
   `CLAUDE.md`) lands in `knowledge/ORG.md` and can find the organization, its
   Authority, Goals, Tasks, and Processes. Switch harnesses any time — the
   folder is the organization.

## Migrating an existing business

Don't migrate. **Federate.** Your systems keep running; the seed starts as the
governance layer: enumerate the systems, run one process against them, and let
records migrate inward only when a process earns it. A business is "on the seed" the
day one real decision flows through the loop — not the day its data moves.

When you find doctrine trapped in old tooling (playbooks, prompts, skills), migrate
it *curated*: read everything, take what earns its place, leave the wrapper, record
the gaps you find. The conserved home outlives every tool that visits it.

## What's in the box

```
knowledge/ORG.md                      ← your canonical entry (template)
knowledge/KNOWLEDGE.md                ← three Knowledge classes, Machinery boundary, evolution map
knowledge/AUTHORITY.md                ← the rulebook (template; reserved powers ready)
knowledge/CONTEXT.md                  ← the glossary of seed terms (keep it)
knowledge/goals/_kind.md              ← Goal definition; Instances create their own Goals
AGENTS.md / CLAUDE.md       ← thin mounts for any coding agent
knowledge/processes/example-weekly-review.md   ← a worked example process
knowledge/processes/handle-uncovered-work.md    ← safe route when no Process fits
knowledge/processes/review-lessons.md           ← Lesson disposition without queue pressure
knowledge/processes/change-standing-knowledge.md ← one route for governed knowledge changes
knowledge/processes/_contract.md                ← the small Process authoring contract
knowledge/processes/index.md                    ← Process discovery
knowledge/lessons/_kind.md                      ← Lesson routing and completion rules
knowledge/work/_kind.md                         ← Task definition and optional Goal link
knowledge/AUTHORING.md                          ← rules for durable knowledge changes
knowledge/records/systems/_kind.md    ← the Kind that makes adoption = acknowledgment
knowledge/proposals/0000-proposal-template.md  ← the mutation form (reason, evidence,
                              benefit, validation, rollback, ruling)
knowledge/docs/adr/                   ← why the pattern is shaped this way
```

Directories like `knowledge/work/` and `knowledge/decisions/` gain entries when
your first Task or Decision happens; the Seed ships only definitions and
examples that every Instance needs.

## License

Apache-2.0. Fork it, run a company on it, build products above it.
