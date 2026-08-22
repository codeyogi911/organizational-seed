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
