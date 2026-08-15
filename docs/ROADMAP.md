# Seed roadmap

The pattern evolves only by folding back what live instances prove. Versions are
themes, not dates.

This edition is written after a full generation of live operation, so it records
what was **abandoned** and what **reversed** as plainly as what shipped. A
roadmap that shows only green is the same failure as a status report that shows
only green, and this pattern exists to prevent that one.

Two words are used precisely below. **Shipped** means the mechanism is in this
seed. **Proved** means a live instance ran it — the *proving ground* — and where
something exists only there, the row says so.

| Version | Theme | State |
|---|---|---|
| **v0.3 — Verify** | checks become universal | shipped, one line abandoned, one arriving in a different shape |
| **v0.4 — Subtraction** ✅ | git does the work three mechanisms were imitating | **this release** |
| **v0.5 — Hiring library** | forkable stewards | proved early; the forking itself unproven |
| **v0.6 — Always on** | headless operation | partial; one item reversed |
| **v1.0 — The network** | many instances | one piece shipped, the rest open |

## v0.3 — Verify: what actually happened

| Promised | Reality |
|---|---|
| `tools/doctor` — immune surveillance over an instance | **Shipped, then hugely surpassed.** Validation in the proving ground went far past the checks the seed shipped with. A mechanical pass over an instance is now an assumption, not an aspiration. |
| the mechanical conserved-file gate (CODEOWNERS + branch protection) | **Shipped and hardened**, plus CI. It also gained the correction that matters: the merge button is not the ruling ([enforcement.md](enforcement.md)). |
| the design vocabulary made explicit ([biomimicry.md](biomimicry.md)) | **Abandoned as a working vocabulary.** The proving ground uses none of it in daily operation. The page stays as design history — it is honest about the two mechanisms the metaphor talked us into — but no instance is asked to learn it. |
| per-process check generalization | **Shipped in a different shape.** Rather than generalizing check lists, every Process now carries a **done condition**: what makes one performance finished, written so a human or a script can settle it without judgment. One ceremony fewer, same guarantee. |
| kind→JSON-schema compilation (slated v0.5) | **Destination reached, mechanism rejected.** Required fields are declared in prose in each `_kind.md` and validated mechanically from there. Compiling schemas would have created a second home for a fact the `_kind.md` already owns — and the only JSON schemas the design ever needed belonged to a layer that has since been retired. |

## v0.4 — Subtraction: what shipped

The theme is removal. Three mechanisms left the design because live operation
showed the substrate was already doing their job, or that the ceremony was not
doing its own.

**Removed**

- **Session leases** → git owns repository concurrency: worktrees, merge
  conflicts, non-fast-forward rejection
  ([ADR 0003](adr/0003-git-owns-repository-concurrency.md)). The write
  discipline stays, in full, for external systems.
- **Two-tier governance** (Proposals + a fast-track ledger) → one route: branch,
  reviewed diff, Decision file with the Founder's verbatim ruling
  ([ADR 0004](adr/0004-one-governance-route.md)).
- **The `## Now` section in `ORG.md`** → routine work never writes to the
  organization's most sacred file.
- **The mandatory task file** → a work note is optional, for work that is
  long-running, resumable or externally effectful.

**Added — contract, not machinery**

`EXECUTION.md`, `AUTHORING.md`, `MOUNTING.md` and `voice.md`; `records/gaps/`
(the Kind for what was missing); `processes/index.md` and `processes/draft/`
with graduation only by ruling; boot-path line caps; claim precedence; the three
authorization layers with one-time Decisions and outcome receipts; a secrets
discipline binding every Role and transport; and *one fact, one home* as a named
rule.

**Arrived early, from later versions**

| Planned | What landed |
|---|---|
| v0.4 — weekly review as a core process | **Shipped**, but three of its four named duties changed: Now compaction went with the Now section, ledger batch-review went with the ledger, and the pattern-sync duty is the one that failed (below). The deadman grid is the duty that survived intact. |
| v0.4 — deadman grid | **Shipped with real numbers.** Overdue at **36h** for a daily process, **8 days** weekly, **32 days** monthly. Silence is never success. |
| v0.4 — per-operator-class credential doctrine | **Shipped in a different shape:** a secrets discipline that binds every Role and every transport (never commit a credential, never echo one even truncated, never print a token-refresh body; to confirm a secret exists, name it and state that it is set), plus a per-system connector strategy. |
| v0.5 — reference charters (books, support, audit) | **Two of three proved**, plus an unplanned third the work demanded. "Audit" turned out to be a **Process, not a Role** — something the organization does on a cadence, not someone it hires. |
| v0.5 — domain canon packs | **Proved**, including doctrine files that **outrank the Processes citing them**. The doctrine mechanism is in the seed; the packs are instance-side by nature. |
| v1.0 — cross-instance lesson flow | **Shipped one-way and governed:** a single outbound Process with a generalize-or-drop gate, a blocking tenant scrub, and a verbatim publish ruling. Nothing flows inbound automatically, and instance data never flows at all. |

**Abandoned**

- **v0.4 — lease heartbeat helper.** It would have automated a mechanism that no
  longer exists.
- **v0.5 — "hiring by forking a file".** **Unproven, not shipped.** The stewards
  that exist were grown in place, one charter at a time, against real work.
  Nothing has yet been hired by forking a charter out of a library, so the claim
  stays unproven rather than quietly upgraded.

**Reversed**

- **v0.6 — CLI→MCP transport evolution.** The doctrine is now the opposite.
  **CLIs are the spine; MCP servers are interactive sugar.** Every
  authority-granted write the live processes need is CLI-only or CLI-safer:
  scriptable, loggable, diffable, runnable without a chat session, and
  narrowable to a single effect. MCP earns its place at the interactive edge,
  not under a scheduled process that spends money.

## The rule that failed

The last edition carried one standing rule: *"pattern-level lessons flow here
from live instances at their weekly reviews; instance data never does."*

The second half held — no instance data has ever flowed here. The first half did
not run at all.

| | |
|---|---|
| Promised | pattern lessons published at every weekly review |
| Published | none |
| Elapsed since the last edition | **24 days** |
| Rulings made in the proving ground in that window | **27** |

It failed the way rules do. It named a duty inside somebody else's process and
made nothing visibly missing when the duty was skipped — nothing was overdue,
because nothing was owed by name. That is precisely the failure the deadman grid
catches for scheduled processes, reproduced in a process that had no expected
output of its own to be missing.

What changes: the sync becomes a Process with its own name, its own dated
expected output, and the same deadman treatment as every other cadenced Process
— a file that is either there or conspicuously absent. This edition, 24 days
late, is that output's first instance. Whether the fix works is a claim for the
next edition, not this one.

## Open questions, answered

[biomimicry.md](biomimicry.md) closes on three open questions. Two are now
answered by live operation.

- **Senescence** — when does a process retire on purpose, rather than because
  someone noticed? **Answered: retirement is a move, not a deletion.** A
  superseded file leaves the live path once its unique knowledge has a verified
  home, the successor is named at the moment of retirement, and git keeps the
  bytes. Removing the last current home of unique evidence is a reserved power;
  removing a verified superseded copy is ordinary work.
- **Caste differentiation** — one Operator role, or specialized stewards?
  **Answered: three chartered stewards, and a rule for when a fourth is
  justified.** A new steward earns a charter when a body of work has its own
  standing evidence base *and* its own never-boundaries. Volume alone does not
  justify one: work that recurs on a cadence but shares the Operator's
  boundaries stays a Process.
- **Symbiosis** — two instances trading services under each other's Authority —
  is still open. The one-way, gated publish route above is the only leg of it
  that exists.

## What's next

| Version | Theme | Still open |
|---|---|---|
| **v0.5 — Hiring library** | forkable stewards | prove the fork: a charter lifted from a library into a second instance and occupied without being rewritten. Until then the library is a hypothesis. |
| **v0.6 — Always on** | headless operation | **partial.** CI covers repository checks; the business runs still ride a harness-bound scheduler. Deadman escalation to the Founder's phone is **not shipped** — a missed run is currently caught by a missing file at the next review, which is slower than the failure deserves. |
| **v1.0 — The network** | many instances | `seed init`, the holding-org pattern for several businesses under one owner, a docs site, and symbiosis. |

Standing rule, rewritten: pattern-level lessons flow here through **one named
outbound Process with its own dated output**, a generalize-or-drop gate, and a
tenant scrub that blocks publication. Instance data never flows. The missing
dated output is the signal — the previous version of this rule had none, and
went unnoticed for 24 days.
