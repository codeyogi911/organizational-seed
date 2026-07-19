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
[docs/ROADMAP.md](docs/ROADMAP.md).

**Origin:** extracted from a living instance that runs a real e-commerce business —
its purchase orders, support desk, books reconciliation, and governance all flow
through this exact structure daily. The pattern is published; the business stays
private.

**v0.2** folds back what sustained live operation taught: chartered agent Roles
(`roles/_charter-template.md` — narrow grants, hard boundaries, probation), the
concurrency convention (session leases + fencing + deadman checks; `work/_active/`),
two-tier governance (full Proposals only where power grows; `decisions/fast-track.md`
for everything else), and the write discipline that makes crashed or colliding agents
recoverable by design ([docs/write-discipline.md](docs/write-discipline.md)). All of
it was forced by real failures — concurrent agents in one ledger, mid-write crashes,
silent schedule deaths — not designed in advance.

## The stencil

An organization of any size is a quantity of eight kinds of durable thing — scale
adds files, never new kinds:

| # | Category | Lives in | What it is |
|---|---|---|---|
| 1 | **Identity** | `ORG.md` | purpose, current goal, the Now |
| 2 | **Roles** | `roles/` | positions with responsibilities + authority; humans *or agents* occupy them |
| 3 | **Processes** | `processes/` | how kinds of work are done — steps, mechanical Checks, one Judgment question |
| 4 | **Tasks** | `work/` | one bounded performance of a process |
| 5 | **Records** | `records/` | the nouns the business touches; each Kind defined by a `_kind.md` (this *is* your ontology) |
| 6 | **Decisions** | `decisions/` + inline | recorded exercises of authority |
| 7 | **Lessons** | `lessons/` | preserved experience; every process reads its lessons first |
| 8 | **Proposals** | `proposals/` | the mutation queue — reviewable, reversible changes |

…governed by **`AUTHORITY.md`** (the rulebook), with **Mounts** (`AGENTS.md`,
`CLAUDE.md`, `.claude/`, connectors) as disposable harness bindings outside the
stencil entirely.

## The loop

Every piece of work travels the same path:

1. A human expresses **intent** (ephemeral — never a filed artifact).
2. The intent becomes a bounded **Task** under a **Process**.
3. A human or agent performs it; every claim in the output **cites Records**.
4. Mechanical **Checks** verify coherence (no LLM required); a human rules the
   **Judgment**.
5. **Lessons** are recorded; frictions that would change a governed file become
   **Proposals** — applied only after a human ruling, always with a rollback.

Intent with no matching process is not an error — it is the growth signal: the
operator drafts a proposal for the new process, and the organization grows one
approved mutation at a time (*directed evolution* — see
[docs/adr/0002](docs/adr/0002-directed-evolution.md)).

## Principles that keep it honest

- **Bindings, not homes.** Skills, agent files, and connectors point at durable
  state; they never own it. Delete every mount and the organization still runs.
  ([ADR 0001](docs/adr/0001-bindings-not-homes.md))
- **A small conserved core.** Identity, authority, roles, and processes change only
  via approved Proposal. Everything else is free.
- **Access is not permission.** A connected tool grants nothing; only `AUTHORITY.md`
  does. External writes and spending always stop at a human boundary.
- **Evidence is a citation discipline.** A claim without a citation is unverified by
  definition; checks are runnable by hand.
- **Systems are federated, not migrated.** Gmail, your ERP, your helpdesk keep
  owning their data; the seed records who owns which truth
  ([records/systems/](records/systems/_kind.md)) and governs how it may be touched.
- **Lessons weigh what their evidence weighs.** Recurring evidence upgrades a
  lesson; a closed one-off decays. Scar tissue is audited, not accumulated.

## Quick start — grow a new organization

1. **Use this template** (GitHub → "Use this template", or clone).
2. **Write your `ORG.md`** — fill every `{placeholder}`: purpose, a Founder and an
   Operator role, an honest Now section.
3. **Keep `AUTHORITY.md`'s reserved powers** (they travel well verbatim); write your
   Operator grants.
4. **Enumerate your external systems** as `records/systems/` entries — what each is
   the source of truth for, what access exists. This moves no data; adoption is
   acknowledgment, not migration.
5. **Write one process** for one real recurring pain, using
   [processes/example-weekly-review.md](processes/example-weekly-review.md) as the
   shape: steps a human could follow, Checks, one Judgment question, "read the
   lessons first" as step 1.
6. **Run the loop once** — intent → task → evidence-cited output → checks → your
   judgment → lesson → proposal. Then keep running it.
7. **Point your agent at it.** Any coding agent that reads `AGENTS.md` (or
   `CLAUDE.md`) lands in `ORG.md` and knows the org, its authority, and the next
   action. Switch harnesses any time — the folder is the organization.

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
ORG.md                      ← your canonical entry (template)
AUTHORITY.md                ← the rulebook (template; reserved powers ready)
CONTEXT.md                  ← the glossary of seed terms (keep it)
AGENTS.md / CLAUDE.md       ← thin mounts for any coding agent
processes/example-weekly-review.md   ← a worked example process
records/systems/_kind.md    ← the Kind that makes adoption = acknowledgment
proposals/0000-proposal-template.md  ← the mutation form (reason, evidence,
                              benefit, validation, rollback, ruling)
docs/adr/                   ← why the pattern is shaped this way
```

Directories like `work/`, `lessons/`, `decisions/` appear when your first task,
lesson, or decision does — the seed never ships empty scaffolding.

## License

Apache-2.0. Fork it, run a company on it, build products above it.
