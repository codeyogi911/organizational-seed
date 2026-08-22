---
type: Organization
status: stable
access-scope: core
write-class: ruled
---
# {Organization Name} — the Organization

> **Template note:** this file is your organization's front door. Replace every
> `{placeholder}`, then delete this note. Rule of thumb: anything live is either
> stated here once or linked from here — never mirrored.

This file is the canonical entry point. If you are new here — human or agent — read
this file top to bottom, then obey [AUTHORITY.md](AUTHORITY.md). When a scoped
Mount is in use, [ACCESS.md](ACCESS.md) limits what the current Role may
discover; it never grants Authority. Everything else links from here. The
glossary of terms is [CONTEXT.md](CONTEXT.md).

## Purpose

{What this organization exists to do, in 2–4 sentences. Real, not aspirational.}

Optional [Goals](goals/_kind.md) make durable organizational direction explicit
when Purpose alone is too broad to coordinate current work.

## Roles

Authority attaches to Roles, never to named people. Occupancy today:

| Role | Holds | Occupied by |
|---|---|---|
| **Founder** | Judgment on all Processes; the reserved powers ([AUTHORITY.md](AUTHORITY.md)) | {name} |
| **Operator** | Performs Tasks within granted authority | any human or agent working this repo |

Chartered roles (created through an approved governed candidate) live in
`roles/`, one file each; this table is the occupancy index.

## How work happens

1. A human expresses bounded intent — ephemeral, spoken or typed, quoted
   verbatim into the Task.
2. The Operator instantiates a **Task** in `work/` under one **Process** from
   [the Process index](processes/index.md). If no Process fits, use
   [handle uncovered work](processes/handle-uncovered-work.md); absence is a
   growth signal, not permission to invent standing Authority. Link one Goal
   only when the Task advances durable organizational direction.
3. The Task is performed. Every claim in the output cites **Records** — that is
   what evidence means here.
4. Mechanical **Checks** run (defined in the Process; no LLM required). Then the
   Founder rules the **Judgment**, recorded verbatim in the Task.
5. **Lessons** go to `lessons/` and are handled through
   [review Lessons](processes/review-lessons.md): absorb, keep, reroute, or
   close. Creating, correcting, improving, merging, renaming, or retiring what
   future work follows uses
   [change Standing Knowledge](processes/change-standing-knowledge.md). A
   governed change is never applied without the required Founder ruling.

**Concurrent operators.** Before mutating, a session takes a lease in
`work/_active/` (see its `_kind.md`): operator, task, claimed scopes (e.g.
`{system}:mutate`, `repo:knowledge/goals/<id>.md`), heartbeat ≤15 min. Stale at
30 min — breakable with a record. Re-read your own lease before every mutation
batch; gone means halt. One mutator per external system at a time;
scheduled runs check leases first and defer once. Every scheduled process has a
date-stamped expected report — a missing one is a flag, never silence. Leases
are advisory: crash-safety comes from the write discipline
([docs/write-discipline.md](docs/write-discipline.md)), which makes recovery
"just run the process again".

## How Knowledge and Machinery change

[KNOWLEDGE.md](KNOWLEDGE.md) separates Knowledge from Machinery. Knowledge has
three classes: Standing Knowledge, Organizational Memory, and Working State.
**Conserved** is the change rule applied to Standing Knowledge, not a fourth
class or a folder name.

**Standing Knowledge** changes only with a Founder ruling under one exact
candidate contract. It includes:

- this file's Purpose, Roles, knowledge-change rules, and map;
- [KNOWLEDGE.md](KNOWLEDGE.md), [CONTEXT.md](CONTEXT.md),
  [AUTHORITY.md](AUTHORITY.md), [ACCESS.md](ACCESS.md), and
  [AUTHORING.md](AUTHORING.md);
- active Processes, Process contracts, Role charters, and every `_kind.md`
  definition;
- the repository-native Decision definition that shapes governed change.

Every Standing Knowledge change uses one contract, whether it expands power or
only corrects wording: prepare one exact target-only candidate `A`, display its
complete before/after bytes and target-diff digest, and obtain an authenticated
Founder yes or no for that immutable candidate. Approval appends a deterministic
Decision-only child `B` and uses an ordinary merge retaining `A` and `B`.
Rejection keeps `A` out of canonical history and appends only the refusal
Decision to the canonical branch. A changed byte, target, branch, repository,
or candidate requires a fresh ruling. See [the Decision Kind](decisions/_kind.md).

**Organizational Memory** grows through ordinary work and is not rewritten to
change history: Records, resolved Decisions, Lessons, terminal Tasks, and Git
history. Corrections supersede earlier claims; deletion requires Founder
approval.

**Working State** changes through the deciding Role or Process that owns it:
active Goals, open Tasks, draft Processes, and governed candidate branches. A
Goal, draft, or candidate grants no standing Authority.

**Machinery is not Knowledge.** It is replaceable through repository
maintenance: tools, generated indexes, and Mounts. It may read, check, project,
or present Knowledge but cannot own organizational meaning or Authority.

Ordinary work may therefore:

- update Working State through its Process; append new Records, Lessons, and
  Decisions; refresh current Record fields only as their Kind
  allows with new source and `as-of`;
- append lifecycle receipts or superseding corrections to Organizational
  Memory, never rewrite an established historical claim;
- create and revise draft Processes that grant no Authority;
- record authorized Goals and append linked progress without changing their
  outcome or lifecycle ruling.

## Map

| Path | What lives there |
|---|---|
| `ORG.md` | this file — canonical entry |
| `KNOWLEDGE.md` | Knowledge classes, Machinery boundary, ownership, and evolution map |
| `AUTHORITY.md` | the rulebook |
| `ACCESS.md` | repository-native discovery scopes and write ceremonies; never an Authority grant |
| `CONTEXT.md` | glossary of seed terms |
| `goals/` | Founder-set outcomes; active Goals are Working State, terminal Goals are Organizational Memory |
| `processes/` | how kinds of work are done; active definitions are Standing Knowledge |
| `processes/index.md` | replaceable Process discovery projection, verified against each Process definition |
| `processes/_contract.md` | how Processes are named and written |
| `roles/` | chartered Roles — Standing Knowledge |
| `work/` | Tasks use one Process and may link one Goal; open Tasks are Working State, terminal Tasks are Organizational Memory |
| `records/` | Organizational Memory; each Kind's `_kind.md` is Standing Knowledge |
| `decisions/` | Organizational Memory of rulings on the organization itself |
| `lessons/` | Organizational Memory naming its source Process and proposed Standing Knowledge home |
| `docs/adr/` | design decisions about the pattern itself |
| `tools/` | machinery — replaceable check scripts |
| `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.mainmind.json` | Mounts — harness bindings, disposable |

## For harnesses

`AGENTS.md`, `CLAUDE.md`, and any agent config are Mounts: thin pointers into this
file. Deleting every Mount leaves the organization fully operable by a human with a
text editor. Never put organizational state in a Mount.
