---
id: index
kind: index
of: process
status: active
description: Routing index over processes/ — one line per Process, so a reader can choose without opening the body.
---

# Processes — find the right way of working

> **Template note:** this is the routing surface every session hits after
> `ORG.md`. Keep one row per Process, and write the "What it is for" column in
> **task language** — the words someone would use to describe the problem, not
> the name of the file. Replace the example rows with your own. Generating this
> file from Process frontmatter is a good idea once you have more than a
> handful; the Markdown Processes stay canonical either way.

## Discover

Start with the task-language descriptions below, then use `rg -i` over
`processes/` if the wording is uncertain. Open only plausible matches. The
canonical unmatched-intent and reinforcement loop is
[ORG.md § Process discovery and reinforcement](../ORG.md#process-discovery-and-reinforcement).

## Active

| Process | Kind | What it is for |
|---|---|---|
| [example-weekly-review](example-weekly-review.md) | process | Weekly: prove every cadenced Process actually ran, and that the conserved core changed only by a recorded ruling. |
| {your-process} | process | {The problem in the words someone would use to describe it — "a customer is asking for a refund", not "refund handling".} |
| {your-doctrine} | doctrine | {The invariants this file owns. A doctrine states what must be true, not what to do; when a Process disagrees with it, this file wins.} |

## Drafts

Drafts live in [`draft/`](draft/) and are **not** listed above. A draft grants
no reusable Authority and is not promoted by successful use — only by a Founder
ruling.

## Retired

Follow the successor. A retired file remains in the current tree only while an
active Process still cites unique live knowledge inside it.

| Process | Status | Superseded by | What it was for |
|---|---|---|---|
| — | — | — | — |
