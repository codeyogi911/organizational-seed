---
id: _kind
kind: kind-definition
of: gap
status: active
max-age-days: 14
freshness-applies-to: open
description: A recorded instance of the repository failing to supply something a performance needed — the organization's only evidence of what is missing rather than wrong.
node-role: observation
context-scope: episodic
---

# Kind: gap

A **gap** is one recorded instance of the organization failing to supply
something a performance needed. It is the counterpart to a Lesson: a Lesson
records what was *learned*; a gap records something that **was needed and was
not there**.

Every other check in a repository like this one is shaped *"something is
present that shouldn't be"* — a citation to a retired file, a retracted claim
still asserted, a stale projection. **Nothing detects "something should be
present and isn't,"** and the failures that cost the most are of that kind: an
escalation obligation that lived in no file, a withdrawn premise whose
dependents never quoted it.

Absence cannot be found by inspecting the files, because a missing rule has no
file to inspect. It is observable only at the moment a performance needs it and
comes up empty. **That moment is this Kind.**

## Identity

**Identity rule:** `<YYYY-MM-DD>-<what-was-needed>` — named for the *need*, in
the words the performance used, not for the fix.
`2026-01-24-escalation-threshold-for-large-exposure`, not
`add-check-7-to-controls`.

**Required frontmatter:**

- `id` · `kind` (`gap`) · `date`
- `needed` — what the performance needed, one line, in its own words
- `found-by` — how it surfaced: `impasse` (a human had to be asked),
  `unrouted` (traversal and search found nothing), `dark-match` (search found
  content that traversal could not reach), or `external` (a system of record
  named something the repository does not)
- `work` — the performance that hit it
- `status` — `open`, `codified`, or `declined`
- `disposition` — required once status leaves `open`: the path that now covers
  it, or the reason it should not be covered

## When to read this Kind

Read it when asking *"what does the organization not know yet?"* — when
planning a governance round, or when a performance is about to depend on
something nobody has written down. Never read it to perform ordinary work: a
gap is a statement about the repository, never evidence about the business.

## Liveness

**A gap is never deleted and its `status` never returns to `open`.** Codified
and declined are both terminal, and both are useful: a declined gap is a
standing record that the organization considered covering something and chose
not to, which is exactly the knowledge a later performance needs to avoid
re-opening it.

An `open` gap older than this Kind's `max-age-days` should be reported by your
validation tool. That is the whole enforcement mechanism: **the organization is
not allowed to notice a gap and forget it.**

## Exclusion

- **Never cited as evidence about the business.** That a gap exists says the
  repository was incomplete, not that any external fact is true.
- **Not a Lesson.** A Lesson is what was learned; a gap is what was missing.
  The two are frequently a pair — the Lesson goes to `lessons/`, the gap
  records that the organization had to learn it the expensive way.

## Why the record is worth more than the fix

The fix is one file. The gap is a data point in the only series the
organization has about its own blind spots — and the series is what tells you
whether the repository is getting better, which the fix alone never can.
