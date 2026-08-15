---
id: NNNN-short-slug
kind: decision
date: YYYY-MM-DD
ruled-by: Founder ({name}), {where}, verbatim "{the Founder's exact words}"
---

# Decision NNNN: {what was ruled, in one line}

> **Template note:** copy this file to `decisions/NNNN-short-slug.md` for every
> conserved change. Delete this note. There is no lighter tier — see
> [ADR 0004](../docs/adr/0004-one-governance-route.md).

## What changes

{The change in behavioural terms — what may or must happen in a future
performance that could not, or had to, before. Name the files the diff
touches.}

## Why

{The reason this is right. This is the part a ledger row cannot carry and the
whole reason the file exists. A reader in a year must be able to tell whether
the reason still holds.}

## Evidence

{What made the case — the Lesson, gap, Record, review finding or external fact.
Cite by repo-relative path. If the ruling went against some of the evidence,
say so here rather than omitting it.}

## The ruling

{The Founder's words, verbatim. If the ruling was narrower than what was asked,
record the narrowing explicitly — a Decision that quietly grants more than was
said is the failure this file exists to prevent.}

## Result

- **Commit:** {hash, filled in after the change lands}
- **Rollback:** {what reverting looks like, and anything a plain `git revert`
  would not undo — an external effect already performed, a schedule already
  registered}

## Scope limit

This Decision changes future behavior only as stated above. It grants no
Authority beyond its named scope, and no amount of successful use widens it.
