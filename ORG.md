# {Organization Name} — the Organization

> **Template note:** this file is your organization's front door. Replace every
> `{placeholder}`, then delete this note. Rule of thumb: anything live is either
> stated here once or linked from here — never mirrored.

This file is the canonical entry point. If you are new here — human or agent — read
this file top to bottom, then obey [AUTHORITY.md](AUTHORITY.md). Everything else
links from here. The glossary of terms is [CONTEXT.md](CONTEXT.md).

## Purpose

{What this organization exists to do, in 2–4 sentences. Real, not aspirational.}

**Current goal:** {the one thing the organization is trying to prove or achieve
right now}

## Roles

Authority attaches to Roles, never to named people. Occupancy today:

| Role | Holds | Occupied by |
|---|---|---|
| **Founder** | Judgment on all Processes; the six reserved powers ([AUTHORITY.md](AUTHORITY.md)) | {name} |
| **Operator** | Performs Tasks within granted authority | any human or agent working this repo |

Chartered roles (created via Proposal) live in `roles/`, one file each; this table
is the occupancy index.

## Now

- **Active work:** {none yet — or link the open Task}
- **Founder decision queue:** {empty — or the rulings waiting}
- **Next action:** {the single next thing; updating this line is part of every Task}

## How work happens

1. The Founder expresses intent — ephemeral, spoken or typed, quoted verbatim into
   the Task.
2. The Operator instantiates a **Task** in `work/` from a **Process** in
   `processes/`. Intent with no matching Process → the Operator drafts a
   **Proposal** for a new one and awaits ruling. Growth, not error.
3. The Task is performed. Every claim in the output cites **Records** — that is
   what evidence means here.
4. Mechanical **Checks** run (defined in the Process; no LLM required). Then the
   Founder rules the **Judgment**, recorded verbatim in the Task.
5. **Lessons** go to `lessons/`. A friction that would change a governed file
   becomes a **Proposal** — never applied without a Founder ruling.

## What is conserved / what is free

Like an organism: a small conserved genome, everything else free to vary.

**Conserved** — change requires an approved Proposal:

- this file's Purpose and Roles sections, and this section itself
- [AUTHORITY.md](AUTHORITY.md)
- everything in `processes/` and `roles/`

**Free** — changes through ordinary work:

- `work/`, `records/`, `lessons/`; writing new entries in `proposals/` and
  `decisions/`
- the Now section of this file

## Map

| Path | What lives there |
|---|---|
| `ORG.md` | this file — canonical entry |
| `AUTHORITY.md` | the rulebook |
| `CONTEXT.md` | glossary of seed terms |
| `processes/` | how kinds of work are done (conserved) |
| `roles/` | chartered Roles (conserved) |
| `work/` | Tasks — one file per performance |
| `records/` | the Ontology — each Kind carries a `_kind.md` |
| `decisions/` | Decisions that rule on the organization itself |
| `lessons/` | preserved knowledge, tagged by process |
| `proposals/` | the mutation queue |
| `docs/adr/` | design decisions about the pattern itself |
| `tools/` | machinery — replaceable check scripts |
| `AGENTS.md`, `CLAUDE.md`, `.claude/` | Mounts — harness bindings, disposable |

## For harnesses

`AGENTS.md`, `CLAUDE.md`, and any agent config are Mounts: thin pointers into this
file. Deleting every Mount leaves the organization fully operable by a human with a
text editor. Never put organizational state in a Mount.
