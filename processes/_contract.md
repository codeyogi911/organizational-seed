---
id: _contract
kind: process-contract
status: active
judge: Founder
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

## Use this shape

Every active Process has seven short sections:

1. **Outcome** — what must be true at the end and why it matters.
2. **When to use** — the request or condition that selects it.
3. **Boundaries** — what is allowed, approval-required, and prohibited.
4. **Evidence and approvals** — what must be read and who must rule.
5. **Steps** — the smallest useful sequence.
6. **Done when** — observable success, including a valid no-op.
7. **Failure and recovery** — what survives interruption and how to retry.

Keep order mandatory only where safety or an irreversible effect depends on it.
Do not restate a rule already owned by another file; link to it.
