---
id: example-weekly-review
kind: process
status: example
judge: Founder
contract-version: simple-v1
description: "Weekly: prove every cadenced Process actually ran, and that the conserved core changed only by a recorded ruling."
---

> **Template note:** a worked example of the shape in
> [`_contract.md`](_contract.md) — seven sections, lessons first, steps a
> human could follow with no agent, one Judgment question ruled by the
> Founder. Adapt it to your first real recurring pain, rename it, set
> `status: active`, and delete this note. A new Process arrives the same way
> any conserved change does: a branch, a reviewed diff, and its own Decision
> file in `decisions/`.

# Process: weekly review (example)

**Standing intent:** "{quote the founder's actual words for why this process
exists}". Cadence: weekly. The cadence lives here; *triggering* is machinery —
a human habit or a separately-approved scheduler Mount. **Never infer that this
sentence proves a scheduler ran.** Read the scheduler's own registration
([MOUNTING.md](../MOUNTING.md#a-schedule-is-not-proof-of-a-schedule)).

## Outcome

The Founder receives one repository-backed report for the ISO week showing
which cadenced Processes actually ran, whether every conserved change traces to
a recorded ruling, what durable work is still unresolved, and the few
improvements that deserve attention. The review observes the organization; it
never performs the work it finds missing.

## When to use

Once at the end of each ISO week, after the other weekly operating Processes
have finished, so their Records exist to be read. Also on demand when someone
asks whether something actually ran — that question is this Process, not a
lookup.

## Boundaries

- **Read** repository and Git state, plus the harness Mount files and scheduler
  registrations needed to verify what they point at.
- **Write** only `records/weekly-reviews/YYYY-Www.md` (add its `_kind.md` when
  you fork) and, for a run that spans sittings, an optional work note —
  through the normal Git path in
  [EXECUTION.md](../EXECUTION.md#repository-changes).
- **Never** read or mutate a business platform, run a missed Process on the
  spot, edit a Mount, merge a branch, or perform a remediation this review
  recommends. Recommending and doing are different jobs: a review that repairs
  what it finds can no longer be trusted to report what it found.
- **Never** infer that cadence prose proves a scheduler ran.
- Any recommendation touching a Role, an active Process, a doctrine, a
  schedule, Authority, or a security or legal boundary needs its own reviewed
  Founder Decision. This Process supplies none of that.

## Evidence and approvals

Read the Lessons tagged `example-weekly-review`; the previous review and the
cutoff it stopped at; Git history since that cutoff; every active Process that
declares a cadence, together with the output it is expected to leave; this
week's outcome Records, Decisions, gaps and draft Processes; and the current
Mount and scheduler registrations. Run whatever validation lives in `tools/`.

**Record exact results and inherited failures rather than converting them into
a green summary.** A check that was failing before this week is still failing
this week and says so. A number nobody could verify is reported as unverified,
in those words ([voice.md](../voice.md)).

A claim about an external system with no repository receipt stays unverified.
It becomes a recommendation for the Process that owns that system — never a
live lookup from here.

The Founder judges the finished report:

**"Does this reflect reality, and would I act on these recommendations?"**

The ruling is recorded verbatim, a rejection included — rejection reasoning is
the seed of the next Lesson. Any conserved change the report proposes is ruled
separately, on its own diff.

## Steps

1. Read the Lessons tagged `example-weekly-review` first. They are inherited
   experience; skipping them repeats mistakes already paid for.
2. Pin the recovery key — the ISO week, the previous review's cutoff, and the
   exact commit being inspected. Everything below is read at that commit.
3. Build the health grid: one row per cadence-declaring active Process, with
   its expected dated output, the file that proves the output landed, the
   result, and the named miss where it did not. **A missing expected output is
   a finding, never silence.** Mark a run missed when its newest dated proof is
   older than `{36 hours}` for a daily cadence, `{8 days}` for weekly,
   `{32 days}` for monthly.
4. List the conserved-path commits since the cutoff. Link each to its reviewed
   diff, its Founder Decision and the resulting commit. Flag any conserved
   change that traces to no Decision — that is the finding this review exists
   to catch.
5. Run the repository checks and quote their exact output, including failures
   inherited from earlier weeks and anything the checks do not cover.
6. Review open work notes, gaps, Lessons and draft Processes. Link repeated
   use, failures and corrections to the Process they inform. Name any draft
   carrying real use or a strike and say what the Founder would be ruling on —
   the review recommends, it never promotes, and there is no count to reach.
7. Check each Mount named by [MOUNTING.md](../MOUNTING.md) against the thing it
   claims: entry files, scheduled tasks, skills, connector configurations, and
   any Mount-like file missing from its registry. Report drift and copied
   policy; do not repair it here.
8. Write the report as a Record. **Every claim cites the records that support
   it** — an uncited claim is unverified by definition.
9. Recommend **at most three** actions, each traceable to a finding.
10. Present it to the Founder and record the ruling verbatim. Record at least
    one Lesson if anything was learned. For friction whose fix would change a
    governed file, the route is a branch, a reviewed diff and a Decision file
    in `decisions/` — opened as separate work, never inside this review.

## Done when

- The report id and frontmatter carry the ISO week and the pinned commit.
- Every cadence-declaring active Process has dated proof or a named miss. No
  row in the grid is blank.
- Every conserved-path change since the cutoff traces to a reviewed diff and a
  Founder Decision, or is flagged.
- Check output is quoted as it ran, with its limits and inherited failures
  intact.
- Open work, gaps, Lessons, drafts and Mount drift each have a current owner or
  are named as orphaned.
- Every claim carries at least one citation and every relative link resolves.
- Recommendations number three or fewer, each citing a finding, and none of
  them was executed.
- No external write occurred beyond the grants in
  [AUTHORITY.md](../AUTHORITY.md).
- The Founder's ruling is recorded verbatim.

## Failure and recovery

The recovery key is the ISO week plus the pinned commit. A resumed run reuses
both rather than starting a fresh week.

- Preserve the partial health grid and the last completed Git range in the
  report or work note before stopping.
- On resume, re-read Git state and the scheduler registrations — both move
  while you are away — and keep the original cutoff. **Never silently extend
  the cutoff.** A widened window hides exactly the missed run this review is
  looking for.
- **Never replace a missing operational receipt with inference.** No receipt
  means no proof, and no proof is a finding.
- Report `checked`, `blocked` or `failed`, naming the exact missing evidence:
  which file, which week, which system. "Partly done" names nothing and is not
  one of the three.

A finished review is allowed to be ugly. One real one ended:

> *Nothing here was fixed mid-run. The numbers are the numbers.*

That is the posture. This report is worth having precisely because nothing
improved on its way past.
