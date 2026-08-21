---
type: Reference
status: stable
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
/ORG.md            @founder-handle
/KNOWLEDGE.md      @founder-handle
/CONTEXT.md        @founder-handle
/AUTHORITY.md      @founder-handle
/AUTHORING.md      @founder-handle
/processes/        @founder-handle
/roles/            @founder-handle
/**/_kind.md       @founder-handle
/proposals/0000-proposal-template.md @founder-handle
/decisions/fast-track.md @founder-handle
/docs/write-discipline.md @founder-handle
/.github/CODEOWNERS @founder-handle
```

## Branch protection

On the hosted repo: protect `main`, require code-owner review for the paths
above. Agents then work Standing Knowledge changes on branches; the merge button *is*
the Founder's ruling (record the verbatim in the PR — the PR becomes the
fast-track ledger entry or the proposal's Ruling).

## What this does and doesn't do

- Does: make the Standing Knowledge boundary physical. A crashed, confused, or
  malicious operator cannot land a governed change without the Founder.
- Doesn't: replace AUTHORITY.md (external systems don't read CODEOWNERS),
  or the leases (concurrency is a different failure), or Judgment (a merge
  without reading is still a ruling — just a bad one).
- Trade-off: direct-to-main workflows (a Founder ruling in-chat, applied
  same-session) need either the Founder's own push, an admin bypass, or a
  short-lived PR. Choose per instance; record the choice in ORG.md.

The doctor's D6 check flags a missing CODEOWNERS file or a Standing Knowledge path that
the file does not cover.
