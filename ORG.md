# {Organization Name} — the Organization

> **Template note:** this file is your organization's front door. Replace every
> `{placeholder}`, then delete this note. Rule of thumb: anything live is either
> stated here once or linked from here — never mirrored.

This is the canonical entry point. Read it top to bottom, then obey
[AUTHORITY.md](AUTHORITY.md). Everything else is loaded only when the work
needs it.

This organization's durable knowledge is plain Markdown in Git. Git owns
versions, diffs, review, integration and rollback. External systems remain
authoritative for their live facts. A generated index or graph is a disposable
view, never a second source of truth.

## Purpose

{What this organization exists to do, in 2–4 sentences. Real, not aspirational.}

**Current goal:** {the one thing the organization is trying to prove or achieve
right now}

## Principles

- **One fact, one home.** State durable knowledge once and link to it.
- **Markdown is canonical.** A database, graph, index or prompt bundle may
  project the files but may not outrank them.
- **Git is the repository control layer.** Branches isolate changes; commits
  preserve checkpoints; review judges diffs; merge and revert integrate or
  undo them.
- **Systems stay federated.** External platforms own their live facts. The
  repository records evidence, decisions and outcome receipts.
- **Capability is not Authority.** A connected tool shows what can be done, not
  what may be done.
- **History is not current context.** Git preserves old bytes. Superseded
  copies leave the current tree after their live knowledge has a verified home.

The glossary is [CONTEXT.md](CONTEXT.md).

## Roles

Authority attaches to Roles, not named people.

| Role | Holds |
|---|---|
| **Founder** | Judgment on Processes and the reserved powers in `AUTHORITY.md` |
| **Operator** | Performs an approved Process within its stated authority |
| **{Steward}** | {Performs its Processes within its charter in `roles/`} |

Chartered Roles live in `roles/`, one file each, written from
[`roles/_charter-template.md`](roles/_charter-template.md). Legal titles are
separate; `Founder` here names the Role holding organizational judgment.

## How work happens

1. Find the closest active Process in
   [processes/index.md](processes/index.md).
2. Read that Process and only the Records, sources and capability notes the
   work needs.
3. Follow its outcome, boundaries, approvals, evidence requirements and done
   condition. Strategy inside those limits is free.
4. For repository changes, use the Git path in
   [EXECUTION.md](EXECUTION.md#repository-changes). For external effects, obey
   the Process and [AUTHORITY.md](AUTHORITY.md), obtain any required human
   approval, verify the result and record a receipt.
5. Leave durable knowledge only where it helps a future reader: a Record,
   Lesson, corrected Process, draft Process, Decision or focused Git history.

An optional work note under `work/` is useful for long-running or resumable
work. It is not required for every interaction.

## Process discovery and reinforcement

**Discovery starts with intent, not filenames.** Read the descriptions in
`processes/index.md`, then use `rg` over `processes/` when the wording is
uncertain. Open only plausible matches.

If no Process fits:

1. Do only the smallest safe one-off that existing Authority permits.
2. Record what was missing as a Lesson or [gap](records/gaps/_kind.md).
3. Create `processes/draft/<name>.md` only when repetition is plausible.
4. A draft grants no reusable Authority.
5. Graduate it into the active index only through a reviewed Git change and a
   Founder Decision.

A Process is reinforced by evidence, not repetition alone:

- an outcome Record, business artifact or commit links the Process it used;
- success shows the Process remains useful but widens no Authority;
- a failure, correction or changed external fact produces a linked Lesson or
  edit to the same Process;
- `git log -- <process-file>` shows its evolution and `rg` shows its uses.

No amount of successful use promotes a Process, action class or Role by itself.
Reusable Authority changes only through a Founder-approved change.

## Concurrent operators

Every repository writer uses a change-specific worktree and branch. Git merge
conflicts and non-fast-forward rejection are the concurrency signal; there are
no repository path leases in the default design
([ADR 0003](docs/adr/0003-git-owns-repository-concurrency.md)). Refresh from
current `main`, resolve conflicts explicitly, rerun checks, and never
force-push.

External systems still require fresh pre-reads, deterministic references,
verified post-reads and one mutator for the same effect at a time
([docs/write-discipline.md](docs/write-discipline.md)). Every scheduled Process
has a date-stamped expected output; a missing one is a flag, never silence.

## What is conserved / what is free

**Conserved — a Founder Decision is required to change future behavior:**

- `ORG.md` and `AUTHORITY.md`;
- Roles;
- active Processes and doctrines;
- reusable Authority, approval boundaries, schedules, security or legal rules.

**One route, not two.** Conserved knowledge changes on a branch with a reviewed
diff and its own Decision file in `decisions/` carrying the Founder's verbatim
ruling. Everything else is committed freely. There is no lighter tier: a
"small" conserved change still gets a Decision, because the ledger that was
supposed to make the light tier reviewable is exactly what stopped being read.

A one-time external-effect approval changes no future behavior. Record it with
the named effect and its outcome receipt.

**Free — ordinary knowledge work:**

- Records, Lessons, gaps, draft Processes and optional work notes;
- factual corrections in those free artifacts that do not amend an active
  Process, doctrine, Role or other rule for future work;
- replaceable tools, generated indexes and graph views.

An active Process or doctrine edit remains conserved even when described as a
correction.

Removing the last current home of unique evidence is not ordinary cleanup.
Removing a verified superseded copy is.

## The boot path is size-capped

These files are paid for by every session:

| Always-read file | Maximum lines |
|---|---:|
| `CLAUDE.md` | 5 |
| `AGENTS.md` | 40 |
| `ORG.md` | 190 |
| `AUTHORITY.md` | 120 |
| Combined | 345 |

Never raise a cap to fit new prose. Move conditional detail to its owning file,
and do not add another always-read file.

## Map

| Path | What lives there |
|---|---|
| `ORG.md` | identity, operating model and repository map |
| `AUTHORITY.md` | reserved powers, red lines and claim precedence |
| `processes/index.md` | task-language routing into active Processes |
| `processes/` | reusable ways of working and doctrines |
| `processes/draft/` | emerging Processes with no reusable Authority |
| `records/` | evidence, receipts and gaps; each Kind carries a `_kind.md` |
| `decisions/` | rulings whose reason must remain explicit |
| `lessons/` | reusable knowledge learned from real work |
| `work/` | optional notes for long-running or resumable work |
| `roles/` | Role charters |
| `EXECUTION.md` | Git change path and external-effect safety path |
| `AUTHORING.md` | how durable knowledge is written and reviewed |
| `MOUNTING.md` | how a harness binding is written and changed |
| `voice.md` | how an agent reports to the Founder |
| `CONTEXT.md` | glossary |
| `tools/` | replaceable capability and validation tools |
| `docs/adr/` | design decisions about the pattern itself |

## For harnesses

`AGENTS.md`, `CLAUDE.md`, `.claude/`, schedules and connector bindings are
disposable adapters. They point to durable knowledge and own only
harness-specific routing or narrowing. They never own rules, Authority or
current organizational state. See [MOUNTING.md](MOUNTING.md).

If a harness and the repository disagree, the repository wins. If a canonical
pointer cannot be loaded, the harness stops and reports instead of acting from
memory.
