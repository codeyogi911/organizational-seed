---
type: Access Policy
state: active
status: stable
access-scope: core
write-class: ruled
access-scopes:
  - core
  - support
  - finance
  - founder
write-classes:
  - conserved
  - ruled
  - ledger
---
# Knowledge access and write policy

This file is the organization's current classification vocabulary. Its presence
activates explicit access classification for every Knowledge node. A Mount that
enforces this policy must fail closed for a non-Founder when a projected node
has missing or unknown classification; it must never guess from a path or title.

Classification controls what a Role may discover. It does not grant Authority.
[AUTHORITY.md](AUTHORITY.md), the active Process, and recorded rulings still
govern what the Role may do with anything it can read.

## Access scopes

The `access-scopes` frontmatter list is the mechanically readable vocabulary
owned by this Instance. `core` and `founder` are reserved and required. An
Instance may add scopes such as `sales`, `legal`, or `warehouse` through a
ruled change to this file; the Seed does not own those names.

Each name is a unique lowercase slug beginning with a letter, containing only
letters, digits, and hyphens, and no longer than 40 characters. One Instance
may declare at most 40 access scopes. A Mount must compile this exact list and
must reject an invalid replacement before it changes the last valid serving
projection.

- `core` — shared purpose, vocabulary, Roles, Processes, and non-sensitive
  operating knowledge.
- `support` — customer conversations, cases, and support operations.
- `finance` — pricing, margins, banking, books, tax, payroll, and financial
  records.
- `founder` — strategy, people matters, credentials, and knowledge reserved to
  the Founder.

Every Knowledge node declares exactly one `access-scope` from this Instance's
list. The Founder may grant one or more scopes to a Role through a trusted
Mount, but that grant remains a discovery boundary only. New scopes or changed
scope meanings are changes to this ruled policy.

## Write classes

The `write-classes` frontmatter list is the mechanically readable vocabulary.

- `ledger` — append a new evidence-backed member through a typed deposit; do
  not silently rewrite established history.
- `conserved` — propose an exact diff and integrate it only after the ruling
  required by [ORG.md](ORG.md) and [AUTHORITY.md](AUTHORITY.md).
- `ruled` — change only through the dedicated ruling path owned by the Founder.
Every Knowledge node declares exactly one `write-class`. A write class selects
the mutation ceremony; it never widens who may perform that ceremony.

## Starter classification

The Seed deliberately starts every shipped node in `core`; an Instance must
reclassify sensitive additions before granting teammates access. Constitutional
files are `ruled`, Standing Knowledge definitions are `conserved`, and
append-only organizational receipts are `ledger`. Mechanical indexes are
Machinery and therefore carry no Knowledge write class. Runtime members use the
class required by their Kind and Process rather than inheriting from a
directory name.

`tools/doctor` checks this policy mechanically. Any Mount may compile these
fields into enforcement backstops, but no Mount owns their meaning.
