---
type: Reference
status: stable
access-scope: core
write-class: conserved
---
# Mechanical enforcement of Standing Knowledge

The seed's honest enforcement statement has three layers: compliance,
review, backstops. This recipe (learned from the Agentic Enterprise
project's homework) upgrades layer 3 from optional to nearly free: **let
git itself refuse unapproved changes to Standing Knowledge.**

## CODEOWNERS

Copy `CODEOWNERS.example` to `.github/CODEOWNERS` and set the Founder's
handle:

```
# Standing Knowledge — changes require the Founder's review
/knowledge/ACCESS.md         @founder-handle
/knowledge/ORG.md            @founder-handle
/knowledge/KNOWLEDGE.md      @founder-handle
/knowledge/CONTEXT.md        @founder-handle
/knowledge/AUTHORITY.md      @founder-handle
/knowledge/AUTHORING.md      @founder-handle
/knowledge/processes/        @founder-handle
/knowledge/roles/            @founder-handle
/knowledge/**/_kind.md       @founder-handle
/knowledge/docs/write-discipline.md @founder-handle
/.mainmind.json @founder-handle
/.github/CODEOWNERS @founder-handle
```

## Branch protection

On the hosted repo: protect `main` and require code-owner review for the paths
above. Agents prepare exact target-only candidates on branches. The Founder
rules through an authenticated surface that displays the immutable repository
and base ref, complete before/after bytes, and candidate SHA. The durable ruling
is the repository-native Decision,
not the merge button or mutable pull-request metadata.

## What this does and doesn't do

- Does: make the Standing Knowledge boundary physical. A crashed, confused, or
  malicious operator cannot land a governed change without the Founder.
- Does: keep an optional Mainmind projection change behind the same review,
  because changing what is served changes an enforcement boundary even though
  the manifest remains replaceable Machinery.
- Doesn't: replace AUTHORITY.md (external systems don't read CODEOWNERS),
  or the leases (concurrency is a different failure), or Judgment (a merge
  without reading is still a ruling — just a bad one).
- Trade-off: the write path needs a GitHub App or equivalent service that can
  append the deterministic receipt and perform an ordinary merge without
  giving working agents repository credentials.

The doctor's D6 check flags a missing CODEOWNERS file or a Standing Knowledge path that
the file does not cover.

## A rule with no checker decays

CODEOWNERS is one instance of a general finding, and the general finding is
the reason to bother with any of layer 3.

An Instance ran the experiment by accident. A four-dimension audit of its own
repository — duplication, staleness, contradiction, graph structure — sorted
every rule the organization held by one question: *is there a script that
checks it?*

| Rule | Mechanically checked? | Outcome |
|---|---|---|
| Links must resolve | yes | zero dangling, across 749 files |
| Snapshots must be under 30 days old | yes | held — hard-stopped a stale purchase order |
| No concurrent overwrite | yes | held — no lost write |
| One fact, one home | no | the same rule found living in six places |
| A cadence actually runs | no | three processes had never run once |
| A control gets checked | no | every control's `last-checked` field empty |
| A ruling propagates | no | a withdrawn fix still live in two governed files |

**Every rule with a checker held. Every rule without one decayed — several
within a day of being written.** The doctrine was not wrong and the operators
were not careless; the rules with checkers and the rules without were written
by the same people in the same week.

Three consequences worth designing for:

1. **Writing more doctrine does not fix a decay problem.** The decayed rules
   were already written down, clearly, in Standing Knowledge. Restating them
   adds a copy, which is itself the failure mode in row 4.
2. **A field nothing writes is worse than no field.** An always-empty
   `last-checked` reads as *not yet stale* to every consumer, so adding the
   field without adding the writer made the gap harder to see, not easier.
3. **The checker has to key on the thing that is true, not on a proxy for
   it.** A governance route that ends "…and one recorded ruling" needs the
   check to be *ruling artifact present*, not *commit message mentions a
   ruling* — the route was followed three steps out of four several times, and
   only the fourth step was the one that made the change findable later.

So the practical test when adding any rule — asked by
[AUTHORING.md's Standing Knowledge review](../AUTHORING.md#standing-knowledge-review):
**name the script that will fail if it stops being true.** If there is none,
either write one, or write the rule knowing it is guidance rather than an
invariant — and say which it is, in the rule itself. A checker whose failures
are routinely ignored has stopped being a checker; a red check nobody reads
decays exactly like a rule nobody checks.
