---
id: _kind
kind: kind-definition
of: draft-process
status: active
description: Emerging ways of working that have not earned reusable Authority — and cannot earn it by succeeding.
node-role: rule
context-scope: standing
---

# Kind: draft Process

A **draft Process** is a file in `processes/draft/` describing a way of working
that looks likely to repeat but has not been ruled into the organization.

## The one rule that matters

**A draft grants no reusable Authority.**

Performing a draft does not authorize anything a Process would authorize.
Whatever permission the performance had, it had already — from the
constitutional ceiling, from an existing Process, or from a one-time Decision.
The draft records *shape*, never *permission*.

## How a draft is born

Not by planning. A draft is the residue of work that had nowhere to go: someone
hit a request no active Process covered, did the smallest safe version of it
that existing Authority permitted, recorded what was missing, and then — only
if repetition looked plausible — wrote down the shape so the next person starts
further along. See
[ORG.md § Process discovery and reinforcement](../../ORG.md#process-discovery-and-reinforcement).

If repetition does not look plausible, the right residue is a Lesson or a
[gap](../../records/gaps/_kind.md), and no draft at all. A draft written for a
thing that happens once is a file that will be read, trusted, and wrong.

## How a draft graduates

**By a Founder ruling. Only.**

There is no count of clean performances that promotes a draft by itself, and
the organization should resist inventing one. A threshold ("three successful
runs and it goes active") looks like evidence-based governance and is not:
it measures that nothing went wrong yet, which is exactly what a young Process
looks like right up until the first time it does. Repetition shows a draft is
*useful*; only Judgment decides it is *safe to make reusable*.

When the Founder rules it active: move the file out of `draft/`, add it to
[`processes/index.md`](../index.md), and record the ruling in `decisions/`.

## Drafts are free, and stay reviewed

Writing and editing a draft is ordinary work — no Decision required, which is
why `processes/draft/` is deliberately left out of the conserved paths in
`CODEOWNERS.example`. That freedom is the point: the cost of writing one down
should be lower than the cost of improvising it again.

The counterweight is that a draft says so, in its own frontmatter
(`status: draft`), so no reader mistakes it for law.

## Liveness

A draft that has not been performed in a long time is evidence about the
organization, not about the draft: either the work stopped happening, or it is
happening under some other name. Review drafts periodically and let them go.
Deleting an unused draft removes no unique evidence — the Lesson or gap that
produced it survives on its own.
