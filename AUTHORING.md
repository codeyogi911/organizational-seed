# Authoring durable knowledge

Read this before changing reusable repository knowledge.

## Universal node rules

1. **Write for a cold reader.** The file must make sense without transcript
   history.
2. **One fact, one home.** Link to the canonical statement instead of copying
   it.
3. **One capability, one owner.** Before adding a *doing* — a check, a read, a
   computation, an effect — search for the node that already performs it and
   extend or call that one. Rule 2 governs facts and catches copied prose; this
   catches a second implementation of the same capability, which review of a
   diff will not, because nothing in the diff is a copy.
4. **Cite claims.** Name provenance, applicability, freshness and uncertainty
   when they can vary.
5. **Keep one purpose per file.** A reader should know why the file exists.
6. **Prefer plain Markdown.** Add frontmatter only when the directory's Kind or
   a useful tool actually consumes it.
7. **Write links for readers.** A generated graph may derive edges from those
   links, but graph structure never dictates prose.
8. **Delete superseded live-path copies.** Verify the surviving home first; Git
   already preserves history.
9. **Keep machinery replaceable.** A tool, Mount, generated index or projection
   owns no fact and no Authority.

## By knowledge type

- **Rule** — state the rule before its rationale; name the governed population,
  failure condition and one to three useful edge cases. Keep Authority distinct
  from advice.
- **Process** — outcome, when to use it, boundaries, evidence, approvals,
  practical steps and done condition.
- **Record** — source, timestamp, observed fact and uncertainty. Separate
  observation from inference.
- **Decision** — what changes, who ruled, why, evidence, resulting commit and
  rollback.
- **Lesson** — what happened, what it teaches, evidence and where it should be
  applied.
- **Reference** — stable scope, canonical source and `as-of` when facts drift.
- **Work note** — bounded intent, current state, recovery and outcome; never a
  copy of its Process.
- **Mechanism** — contract, inputs, outputs, failure modes and recovery. Test
  boundary cases, and keep Capability distinct from Authority.

## One file, one question

Every file answers exactly one question. Content that answers a different
question is misfiled — and misfiled content forks the moment anyone else needs
it, because the next reader looks in the right place, does not find it, and
writes it again.

Four questions, four homes:

| The question | Its home |
|---|---|
| *What is this, and when is it well-formed?* | the Kind definition |
| *What must always be true?* | a constraint record with a named guardian |
| *How is this work done?* | a Process |
| *What does this word mean?* | the glossary |

Three corollaries, each paid for:

- **A cadence, trigger or tool must never appear in a file's identity.** How
  often a rule needs checking is a property of the rule, not of whoever checks
  it. Name a check for what it checks.
- **A consumer cites a definition and never restates it.** A restated
  definition is a forked definition.
- **State the precedence inside the definition, before the conflict happens.**
  Without that line, a fork is a standoff. With it, a fork is a repair with a
  known direction.

A file nobody ever performs or reads is evidence of a homing error, not of low
priority.

## Subtraction is a required question

Every proposed change states what it **removes**. "Nothing" is an allowed
answer, but it must be argued rather than assumed.

A file kept alive just in case is not free: it is a cost paid by every future
session that traverses past it, forever. And read a change's own
*what-this-removes* section as a claim to verify, not a virtue to display.

This rule exists to correct a structural incentive. Removing a Record is a
reserved power; adding one is free. Left alone, that makes the cheapest
compliant action always *addition*, and the repository silently fills with
knowledge nobody dares delete.

## Retirement is a move, not a label

The current tree holds what is true **now**. History lives in Git and in the
Decision that changed it.

A category directory contains only live members. A file marked "retired"
sitting inside one is a defect, not an archive — one instance found withdrawn
doctrine still sitting in a directory a live Process instructed agents to read
*in full*, each file preserving its original claim under a retirement banner.
Any partial read could surface a retracted rule as current with nothing in view
to contradict it.

Retiring is three steps:

1. Remove the file from the live path.
2. Add a row to the category's retired roster, naming the **successor**.
3. Repoint live citations at that roster.

Repointing a citation repairs a *pointer*, never a *claim* — check that what
cited the old file still says something true.

Because Git is the audit trail, the reserved power guarding evidence is
satisfied by the commit: the ruling authorizes a **move**, not a loss. The one
counter-signal is dependency — keep a retired file while live content still
needs something only it says. The test is dependency, not comfort.

## A performance can destroy the state its own writeup cites

When one piece of work both writes standing context *and* takes an action, list
every claim the action would falsify before proposing it.

Prefer a dated past event with a citation over a present-tense assertion about
mutable state. *"As of {date}, six items were outstanding — {source}"* survives
the change. *"Six items are outstanding"* does not.

The tell that separates this from ordinary staleness: one performance, or two.
Ordinary staleness needs someone else to change the world. This one falsifies
its own sentence, in the same session, before anyone reads it.

## Name the residue, or say there was none

A finished piece of work names the durable knowledge it deposited — a Record, a
Lesson, a gap, a corrected Process, a Decision, or an explicit **none**.

Unchecked, this obligation is skipped silently and uniformly. One instance had
carried the rule since founding; the first time anything actually looked, every
completed performance had failed it.

## Changing standing context

Review the exact Git diff before integration:

1. **Correct** — material claims match their cited sources.
2. **Nothing lost** — every prior rule, fact and exception survives or its
   removal is explicit.
3. **Nothing left behind** — superseded copies leave the current path.
4. **No second owner** — the change does not add a capability some other node
   already performs. Ask what already does this, not just whether the prose is
   new; a duplicate capability reads as clean in a diff.
5. **Navigable** — links resolve and a cold reader can find the next file.
6. **Authorized** — a conserved change carries the required Founder Decision.

For conserved reusable knowledge, the reviewer is independent of the author.
The reviewer reports findings; the Founder rules where Authority requires it.
The diff, review discussion, Decision and resulting commit are sufficient.
Separate node-review records, role classifiers and digest ceremonies are not
required.

Generated views are reviewed only for faithful rebuildability. When a generated
view disagrees with the Markdown, rebuild or delete the view.

## The boot path is size-capped

The files every session reads before doing anything are paid for by every
session, forever. Cap them, and hold the cap:

| Always-read file | Suggested maximum lines |
|---|---:|
| `CLAUDE.md` | 5 |
| `AGENTS.md` | 40 |
| `ORG.md` | 190 |
| `AUTHORITY.md` | 120 |
| Combined | 345 |

Never raise a cap to fit new prose. Move conditional detail to its owning file,
and do not add another always-read file. Tune the numbers to your organization
once; then treat them as a budget, not a target.
