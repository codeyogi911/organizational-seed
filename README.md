# Organizational Seed

Run an organization as a folder of plain files — operable by a human with a text
editor, accelerated by any AI coding agent, owned by neither.

Traditional software freezes an organization's workflows into applications. Now
that software can be generated and modified by agents, the durable asset is no
longer the app — it is the organization's own state: purpose, authority,
processes, evidence, decisions, and lessons. This seed keeps all of that as
plain Markdown in a git repo, and treats every agent, model, script and
scheduler as replaceable machinery.

## The pitch

**Your business, as a folder any AI agent can run — and none can run away
with.** Software used to freeze your workflows into apps; now agents can
generate software, so the durable asset is your organization itself: purpose,
authority, processes, evidence, decisions. The seed keeps all of it in plain
files under git. Agents are hired like staff — chartered roles with narrow
grants, hard boundaries, probation — and fired by deleting a file. You stay the
judge: nothing spends, sends, signs, or files without you. Start with one
painful recurring process, not a migration; your existing tools keep running.

It is proven, not theoretical. A real eight-figure (INR) e-commerce business
runs on this daily: books reconciled to the paisa, every marketplace refund
provably credit-noted from the right account, support drafted every morning
before the owner wakes up.

One caveat the seed will not sell past. *Before the owner wakes up* is a promise
made by a harness-bound scheduler, not by this repository. On three occasions a
scheduled run deposited nothing and no check caught it. That is why every
scheduled process here owes a date-stamped expected output — so a run that never
happened surfaces as a missing file instead of as silence. Treat autonomy as a
thing you keep verifying, not a thing you switch on.

Fork the seed. Keep the judgment. Delegate the rest.

**The thesis:** the seed is the genotype; everything else is phenotype.
Harnesses, models, and SaaS systems are expression machinery — they improve
every quarter, and because the organization's identity lives in files and not in
any of them, every improvement anywhere in the stack is captured as a free
upgrade. The org rides every curve and is owned by none.

**Origin:** extracted from a living instance that runs a real e-commerce
business — its purchase orders, support desk, books reconciliation, and
governance all flow through this exact structure daily. The pattern is
published; the business stays private.

## v0.4 — Subtraction

This release folds back a full generation of live operation, and most of it is
removal. Three v0.2 mechanisms are gone:

- **Session leases** (`work/_active/`, heartbeats, fencing epochs). Git already
  serializes repository writes: a change-specific worktree prevents dirty-tree
  collisions, a merge conflict prevents silent integration over a changed base,
  a non-fast-forward rejection prevents overwriting a branch that moved. Those
  signals are mechanical, unfakeable and free — the leases were Markdown
  imitating them ([ADR 0003](docs/adr/0003-git-owns-repository-concurrency.md)).
  The write discipline stays in full for **external** systems: git can serialize
  a file describing a payment, never the payment
  ([docs/write-discipline.md](docs/write-discipline.md)).
- **Two-tier governance** (full Proposals where power grew, a fast-track ledger
  for everything else). Both halves failed, in opposite directions. The ledger
  recorded *that* something was ruled and never *why*, so it stopped being read
  and the batch review had nothing to review. Proposals duplicated what a branch
  already is, and the duplicate was always the stale one. One route now: branch
  → reviewed diff → a Decision file carrying the Founder's verbatim ruling, with
  no lighter tier ([ADR 0004](docs/adr/0004-one-governance-route.md)).
- **The `## Now` section in `ORG.md`.** Routine work must never have to write to
  the organization's most sacred file. Current state lives in Records, work
  notes and git history; `ORG.md` is identity, not a status page.

What arrived in their place is contract, not machinery: `EXECUTION.md` (the git
path and the external-effect path), `AUTHORING.md` (how durable knowledge is
written and reviewed, plus a line budget for the files every session pays for),
`MOUNTING.md` (how a harness binding is written — and why a rule copied into one
outlives the decision it depended on), `voice.md` (how an agent reports to the
Founder: answer first, and never compress a failure), `records/gaps/` (the Kind
that records what was *missing* rather than what was wrong),
`processes/index.md` (routing by task language instead of filenames), and
`processes/draft/` (an emerging process that grants no authority until a ruling
graduates it).

Roadmap — including what was abandoned, what reversed, and one standing rule
that failed: [docs/ROADMAP.md](docs/ROADMAP.md).

## What an organization is made of

An organization of any size is a quantity of seven kinds of durable thing —
scale adds files, never new kinds:

| # | Category | Lives in | What it is |
|---|---|---|---|
| 1 | **Identity** | `ORG.md` | purpose, current goal, operating model, repository map — deliberately not a status page |
| 2 | **Roles** | `roles/` | positions with responsibilities + authority; humans *or agents* occupy them |
| 3 | **Processes** | `processes/` | how a kind of work is done — outcome, boundaries, evidence, approvals, steps, done condition. A doctrine states invariants instead of steps, and outranks the processes citing it |
| 4 | **Records** | `records/` | the nouns the business touches; each Kind defined by a `_kind.md` (this *is* your ontology) — including [gaps](records/gaps/_kind.md), the Kind for what the organization needed and did not have |
| 5 | **Decisions** | `decisions/` | recorded exercises of authority, carrying the ruling verbatim |
| 6 | **Lessons** | `lessons/` | preserved experience; every process reads its lessons first |
| 7 | **Work notes** | `work/` | *optional* checkpoints for work that is long-running, resumable or externally effectful |

…governed by **`AUTHORITY.md`** (the constitutional ceiling), with **Mounts**
(`AGENTS.md`, `CLAUDE.md`, `.claude/`, schedules, connectors) as disposable
harness bindings outside the shape entirely.

One row left this table in v0.4 and one changed its nature. **Proposals** are
gone: the branch is the queue, the diff is the proposal, the revert is the
rollback. **Tasks** became optional work notes — requiring a file per
performance bought a directory of stubs nobody read and taxed exactly the
interactions that should be cheap. A work note now earns its place only by
answering something git history cannot.

## The loop

Every piece of work travels the same path:

1. A human expresses **intent** (ephemeral — never a filed artifact).
2. It is routed to a **Process** through [processes/index.md](processes/index.md),
   found by the words someone would use for the problem, not by filename.
3. A human or agent performs it inside that process's boundaries; every claim in
   the output **cites Records**.
4. The process's own **done condition** settles it — citations resolve, sections
   present, arithmetic correct, receipt verified; no LLM required — and a human
   rules the **Judgment**. Anything reaching the outside world needs the approval
   the process names, and leaves a verified receipt afterwards. A tool call is
   not a receipt.
5. What is worth keeping gets a home: a **Record**, a **Lesson**, a **gap**, a
   corrected process, a **Decision**, or a focused commit. Nothing else is filed.

Intent with no matching process is not an error — it is the growth signal. Do
only the smallest safe one-off that existing authority already permits, record
what was missing as a [gap](records/gaps/_kind.md), and write
`processes/draft/<name>.md` only when repetition looks plausible. A draft grants
no reusable authority, and no number of clean runs promotes it: it becomes
active only by a Founder Decision (*directed evolution* —
[ADR 0002](docs/adr/0002-directed-evolution.md), whose mechanism is now
[ADR 0004](docs/adr/0004-one-governance-route.md)).

Changing the organization itself is the same loop with one addition: a branch, a
reviewed diff, and a Decision file in `decisions/` carrying the Founder's exact
words. The merge is the repository receipt, the revert is the rollback, and the
pull request is transport — never the ruling.

## Principles that keep it honest

- **Bindings, not homes.** Skills, agent files, and connectors point at durable
  state; they never own it. Delete every mount and the organization still runs.
  ([ADR 0001](docs/adr/0001-bindings-not-homes.md))
- **One route for conserved change.** Identity, authority, roles, active
  processes and doctrines change on a branch, with a reviewed diff and their own
  Decision. There is no cheap tier: writing down the reason *is* the cheap part,
  and it is exactly the part the ledger lost.
- **Capability is not authority.** A connected tool shows what can be done, not
  what may be done. Authority resolves in three layers — the constitutional
  ceiling, the mandate an approved process supplies inside its scope, and a
  one-time Decision for one named effect that expires when used and creates no
  future authority. Spending, sending, signing and filing stop at a human.
- **Evidence is a citation discipline.** A claim without a citation is
  unverified by definition; done conditions are runnable by hand.
- **One fact, one home.** Every durable fact is stated in exactly one file and
  cited everywhere else. A second statement is not redundancy — it is a fork
  with a delay fuse, and nothing says which copy is true.
- **Absence gets recorded, not just noticed.** Every other check finds something
  wrongly present; a missing rule has no file to inspect. So the moment a
  performance comes up empty is itself a record — the only series an
  organization ever has about its own blind spots.
- **Systems are federated, not migrated.** Gmail, your ERP, your helpdesk keep
  owning their data; the seed records who owns which truth
  ([records/systems/](records/systems/_kind.md)) and governs how it may be
  touched.
- **Lessons weigh what their evidence weighs.** Recurring evidence upgrades a
  lesson; a closed one-off decays. Scar tissue is audited, not accumulated.
- **The boot path is a budget.** The files every session reads before doing
  anything are paid for by every session, forever. They are line-capped, and the
  cap is never raised to fit new prose.

## Quick start — grow a new organization

1. **Use this template** (GitHub → "Use this template", or clone).
2. **Write your `ORG.md`** — fill every `{placeholder}`: purpose, current goal, a
   Founder and an Operator role. Resist adding a status section; that is what
   Records and git history are for.
3. **Keep `AUTHORITY.md`'s reserved powers** (they travel well verbatim), then
   name your own invariants — the hard ceilings specific to you, each stating
   the default denial and the only shape that lifts it.
4. **Enumerate your external systems** as `records/systems/` entries — what each
   is the source of truth for, what access exists. This moves no data; adoption
   is acknowledgment, not migration.
5. **Write one process** for one real recurring pain, to the shape in
   `processes/_contract.md` and with
   [processes/example-weekly-review.md](processes/example-weekly-review.md) as
   the worked example. Give it a row in
   [processes/index.md](processes/index.md), written in the words someone would
   use for the problem.
6. **Run the loop once** — intent → process → evidence-cited output → done
   condition → your judgment → a lesson or a gap → a Decision or a focused
   commit. Then keep running it.
7. **Turn on the gate.** Copy `CODEOWNERS.example` to `.github/CODEOWNERS`,
   protect `main`, require code-owner review on the conserved paths
   ([docs/enforcement.md](docs/enforcement.md)). Branch protection proves a diff
   was *seen*; only the Decision file proves it was reasoned about.
8. **Point your agent at it.** Any coding agent that reads `AGENTS.md` (or
   `CLAUDE.md`) lands in `ORG.md` and knows the org, its authority, and how work
   happens here. Switch harnesses any time — the folder is the organization.

## Migrating an existing business

Don't migrate. **Federate.** Your systems keep running; the seed starts as the
governance layer: enumerate the systems, run one process against them, and let
records migrate inward only when a process earns it. A business is "on the seed"
the day one real decision flows through the loop — not the day its data moves.

When you find doctrine trapped in old tooling (playbooks, prompts, skills),
migrate it *curated*: read everything, take what earns its place, leave the
wrapper, and record what was missing as a [gap](records/gaps/_kind.md). The
conserved home outlives every tool that visits it.

## What's in the box

```
ORG.md                      ← your canonical entry (template)
AUTHORITY.md                ← the ceiling: reserved powers, the three
                              authorization layers, claim precedence, secrets
AGENTS.md / CLAUDE.md       ← thin mounts for any coding agent
EXECUTION.md                ← the git path and the external-effect path
AUTHORING.md                ← how durable knowledge is written and reviewed
MOUNTING.md                 ← how a harness binding is written and changed
voice.md                    ← how an agent reports to the Founder
CONTEXT.md                  ← the glossary of seed terms (keep it)
processes/index.md          ← the task-language routing surface
processes/_contract.md      ← the shape every process must have
processes/draft/_kind.md    ← an emerging process grants no authority
processes/example-weekly-review.md   ← a worked example process
records/systems/_kind.md    ← the Kind that makes adoption = acknowledgment
records/gaps/_kind.md       ← the Kind that records what was missing
work/_kind.md               ← work notes, and why they are optional
decisions/_template.md      ← the ruling form (what changes, why, evidence,
                              the verbatim ruling, result, rollback)
roles/_charter-template.md  ← hiring an agent: narrow grants, hard
                              boundaries, probation
docs/enforcement.md         ← the mechanical gate (with CODEOWNERS.example)
docs/adr/                   ← why the pattern is shaped this way
```

`lessons/` appears when your first lesson does. Every directory that *is* here
ships with the file that defines it — a `_kind.md`, a contract, a template, or a
worked example. No empty folders, no `.gitkeep`, and no scaffolding left
standing for a mechanism that is gone.

## License

Apache-2.0. Fork it, run a company on it, build products above it.
