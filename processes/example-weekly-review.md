---
id: example-weekly-review
kind: process
status: example
judge: Founder
---

> **Template note:** a worked example showing the shape every process shares —
> standing intent, lessons-first, human-followable steps, mechanical Checks, one
> Judgment question. Adapt it to your first real recurring pain, rename it, set
> `status: active`, and delete this note. (New processes after this one arrive via
> Proposal — see `proposals/0000-proposal-template.md`.)

# Process: weekly review (example)

**Standing intent:** "{quote the founder's actual words for why this process
exists}". Cadence: weekly. The cadence lives here; *triggering* is machinery — a
human habit or a separately-approved scheduler Mount.

## Steps

1. Read the lessons tagged `example-weekly-review`. They are inherited experience;
   ignoring them repeats paid-for mistakes.
2. Open a Task in `work/` (id `YYYY-Www-weekly-review`), status `open`; record
   `performed-by`; quote the standing intent. Update the Now section of
   [ORG.md](../ORG.md).
3. Gather inputs — name them explicitly, with staleness noted: which records, which
   system reads (under what grant in [AUTHORITY.md](../AUTHORITY.md)).
4. Produce the output as a Record. **Every claim cites the records that support
   it** — an uncited claim is unverified by definition.
5. Recommend at most three actions, each traceable to a finding.
6. Run the Checks below (by hand, or with a script in `tools/` — the script
   automates the Checks, it never defines them). Set status `checked`.
7. Present to the Founder for Judgment; record the ruling verbatim in the Task.
8. Record at least one Lesson if anything was learned; open a Proposal for any
   friction whose fix would change a governed file.

## Checks (mechanical — no judgment involved)

- E1 Task frontmatter valid (`id`, `kind: task`, `process`, `status`, `opened`,
  `requested-by`, `output`); intent quoted; output exists.
- E2 Every claim in the output carries at least one citation; all relative links
  resolve.
- E3 Recommendations ≤ 3, each citing a finding.
- E4 No external write occurred beyond the grants in AUTHORITY.md.

## Judgment (the Founder's ruling)

**"Does this reflect reality, and would I act on these recommendations?"**
Rejection reasoning is recorded verbatim; it is the seed of the next Lesson.
