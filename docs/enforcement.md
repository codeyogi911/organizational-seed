# Enforcement — making rules bite

The honest enforcement statement in [AUTHORITY.md](../AUTHORITY.md) puts
compliance and human Judgment first, and reviewable diffs second. This file is
about the third layer: the mechanical checks that make a rule more than a
sentence.

It has two halves. The first is a cheap recipe for gating the conserved core.
The second is harder-won: **how to build a check that actually checks**, which
is where most of the failures in this pattern have actually come from.

## Part 1 — gating the conserved core

### CODEOWNERS

Copy `CODEOWNERS.example` to `.github/CODEOWNERS` and set the Founder's handle.
It covers the constitution and standing rules (`ORG.md`, `AUTHORITY.md`,
`EXECUTION.md`, `AUTHORING.md`, `MOUNTING.md`, `voice.md`), `processes/`,
`roles/`, and `decisions/` — while deliberately leaving `processes/draft/`
unowned, since a draft grants no reusable Authority.

### Branch protection

On the hosted repo: protect `main` and require code-owner review for those
paths. Agents then work conserved changes on branches, and the Founder's review
is mechanically required before integration.

### The merge button is not the ruling

An earlier version of this recipe said the merge button *was* the Founder's
ruling, and that the pull request could serve as the ledger entry. That was
wrong, and it is worth saying why, because the mistake is an attractive one.

A merge is a repository event on someone else's server. It records *that*
something was integrated, never *why*. Migrate hosts, or lose access to the
API, and the reasoning is gone while the files remain — the exact inversion of
what this pattern is for. A ruling must survive independently of its transport.

So: **the pull request is transport; the Decision file is the ruling.** Every
conserved change carries a file in `decisions/` with the Founder's verbatim
words and the reason (see [ADR 0004](adr/0004-one-governance-route.md) and
[`decisions/_template.md`](../decisions/_template.md)). Branch protection then
enforces that the diff was *seen*, which is a different and lesser claim than
that it was *reasoned about* — and only the second one is governance.

### What this does and doesn't do

- **Does:** make the conserved/free boundary physical. A crashed, confused, or
  malicious operator cannot land a conserved change without the Founder.
- **Doesn't:** replace `AUTHORITY.md` — external systems do not read
  CODEOWNERS, and the effects that actually spend money or send mail all happen
  outside this repository. Nor does it substitute for Judgment: a merge without
  reading is still a ruling, just a bad one.
- **Doesn't:** address concurrency. That is Git's job, through worktrees,
  branches and merge conflicts
  ([ADR 0003](adr/0003-git-owns-repository-concurrency.md)).
- **Trade-off:** a direct-to-main workflow (a Founder ruling in chat, applied
  the same session) needs either the Founder's own push, an admin bypass, or a
  short-lived PR. Choose per Instance and record the choice.

## Part 2 — check discipline

### A rule without a mechanism decays

Observed across a live instance's first months: **every rule that had a
mechanism held, and every rule that did not decayed — several within a day of
being written.** Not because anyone disagreed with them. A rule with no
mechanism is a sentence competing for attention against everything else in
context, and it loses.

So when you write a rule, write the thing that will notice when it is broken.
If you cannot, say so in the rule itself, and expect it to erode.

### Match the mechanism to what the rule is about

This is the other half, and publishing the first half without it is dangerous
advice.

- A rule about **form** — a date pattern, a required field, a status
  vocabulary, a resolvable link, a line budget — takes a **script**.
- A rule about **meaning** — restating a definition instead of citing it,
  burying a failure in a summary, making a claim wider than its evidence —
  takes a **reader**, adversarially prompted.

Point a script at a meaning-rule and it does not fail loudly. It passes
confidently while the violation walks past. That is worse than no check at all:
an absent check invites a human reader, and a green check dismisses them.

One instance hardened such a checker three times, and ten violations still
escaped it — none of which its own author found. It was eventually deleted
rather than hardened a fourth time.

### A check that gates an irreversible act must prove it ran

**A validator that errors writes nothing, and nothing is indistinguishable from
a pass.**

This is not hypothetical. A tenant-data scrub gating a public, irreversible
publish used a shell pipeline whose regex the local `grep` implementation
rejected. The erroring filter produced empty output, the scrub found no
violations in it, and five separate commits printed CLEAN. Nothing had been
scanned at all.

Any check standing between the organization and something it cannot take back
must carry its own liveness proof:

1. **A control input the check must match.** A known-bad token that, if the
   matcher stops working, fails the run.
2. **A non-zero count of what it examined.** Report how many lines, files or
   records were actually scanned. Zero, against a non-empty input, is a failure
   — never a pass.
3. **An error that hard-fails.** An internal error must exit non-zero, never
   fall through to a clean verdict.

Report the proof on every run, not only on failure. A number nobody sees when
things are fine is a number nobody will notice when it goes to zero.

### A permanently-failing check carries no information

Once a checker reports failure on every run, a genuinely *new* failure has to
be found by diffing output rather than by reading it. The gate has been
converted into noise. Either fix the standing failures, narrow the check, or
retire it — leaving it red is the one option that looks responsible and is not.

The same applies to a number that is reliably wrong but stable. A count quoted
as a receipt has to be true. The damage is not the inaccuracy; it is that the
next reading — the one where the number represents a real break — looks exactly
like all the others.

### State what the tool accepts, and which way it is allowed to be wrong

A lint with an unwritten notion of its own scope does not fail loudly. It
teaches everyone to write around it, and the writing-around is invisible in
every diff.

Write down what the tool treats as in scope. Then write down **which direction
it is permitted to err**, because that asymmetry decides every future change to
it: over-reporting is visible and annoying, under-reporting is silent. For
anything protecting a boundary, prefer the annoying failure.

Related: a rule whose scope names a *class* of thing must state that class's
membership somewhere a checker can read it. Left inferable, two reasonable
readings produce opposite gates, and the question gets re-litigated every time
the tool is touched.

### A mechanical result must name the tree it is about

A tool that resolves its root from its own install path will answer correctly
about the wrong working tree. In one instance, seven review rounds read a clean
result about a tree containing none of the files under review; the break
surfaced after the merge.

Under a worktree-per-change convention this is not an edge case, it is the
normal condition. Make the tool prune nested work trees structurally — **a
directory containing a `.git` entry is another work tree, whatever it is
called** — and make it print which root it examined.

### Bind a blocking review to an immutable commit

Other operators land work continuously; a review takes minutes to read. A
review bound to a branch name is a review of whatever that name meant when
someone last looked. Pin it to a commit.

And: **a reviewer that has not run yet has no verdict to cite.** Never write
that a review passed in the same edit that produces the thing to be reviewed.
If a fix changes the reviewed bytes again — *including a fix applied after an
approval* — the earlier verdict is void and nothing may cite it. Draft the
narrative freely, but write the sentence naming the outcome last, and only once
it is already true. Where no independent reviewer was available, record the
absence as an absence rather than describing a review that did not happen.

### Ask whether the set is the set you meant

Checking a claim against its source is naturally local: you read the sentence,
you read the source, they agree. A wrongly-drawn *population* is invisible to
that operation. It becomes visible only when you enumerate the members and ask
which ones do not belong.

Those are two different questions, and the second one has to be asked for
explicitly. Add it to the review as its own step.

### A required check has exactly two outcomes

When a Process requires a read before a judgment, the finding is one of exactly
two things:

1. **A result**, with its source and date; or
2. **An evidenced "nothing found"**, proving the search was actually made.

There is no third value. **Not having looked is a check failure, never a
finding**, and an unsearched item may never be reported as "nothing there".

Passing every mechanical check proves the output did nothing **forbidden**. It
proves nothing about whether it did everything **useful** the evidence
supported. An ambiguity gate should narrow what you may safely assert — never
cap how much you bother to find out.
