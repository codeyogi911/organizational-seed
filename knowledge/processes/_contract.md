---
id: _contract
type: process-contract
state: active
judge: Founder
status: stable
---

# Process contract

A Process is a durable way of working that a capable human can follow. It owns
one outcome, its boundaries, the evidence and approvals it needs, practical
steps, and a visible done condition. A tool may check it but may not define it.

## Name the outcome

The filename, frontmatter `id`, `# Process: …` title, and **Outcome** must name
the same result. Name what becomes true, not the cadence, trigger, tool, system,
or temporary project. Review all four together before approval; `tools/doctor`
only catches obvious drift.

The Seed does not define a safe rename mechanism. Do not rename an active
Process unless the Instance first adds a migration that preserves historical
ids and current links. Never change only the filename or `id`, and never
rewrite historical Tasks or Decisions to pretend they used a new name.

Creating, materially changing, renaming, merging, or retiring an active
Process uses [change Standing Knowledge](change-standing-knowledge.md). Work
for which no active Process exists begins with
[handle uncovered work](handle-uncovered-work.md); its draft is not active
until that governed change is approved.

## Use this shape

Every active, draft, or example Process has seven short sections:

1. **Outcome** — what must be true at the end and why it matters.
2. **When to use** — the request or condition that selects it.
3. **Boundaries** — what is allowed, approval-required, and prohibited.
4. **Evidence and approvals** — what must be read and who must rule.
5. **Steps** — the smallest useful sequence.
6. **Done when** — observable success, including a valid no-op.
7. **Failure and recovery** — what survives interruption and how to retry.

Keep order mandatory only where safety or an irreversible effect depends on it.
Do not restate a rule already owned by another file; link to it.

## Lifecycle

- **Draft:** `state: draft`; Working State under `work/process-drafts/`, absent
  from the active index, and grants no reusable Authority. Use the same seven
  sections so review compares the candidate directly with the active shape.
- **Active:** `state: active`; Standing Knowledge, discoverable through the
  Process index, and performable within its approved Authority.
- **Example:** `state: example`; Seed teaching material, not performable until
  an Instance adapts, renames, and approves it as active.
- **Retired:** `state: retired` with `retired-on: YYYY-MM-DD`; Organizational
  Memory kept at its stable path so historical Tasks, Lessons, and Decisions
  remain truthful. A Lesson absorption receipt must predate retirement to keep
  this Process as its historical receiver.

Draft creation is free. Creating an active Process moves an approved draft into
`processes/`; changing or retiring an active Process edits it there. All three
use [change Standing Knowledge](change-standing-knowledge.md).
