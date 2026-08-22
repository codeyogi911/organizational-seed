---
id: _kind
type: kind-definition
of: decision
state: active
status: stable
access-scope: core
write-class: conserved
---

# Kind: repository-native Decision

A Decision is the durable Founder receipt for one exact governed candidate.
It is Organizational Memory, written as one Markdown file under `decisions/`.
The candidate branch is Working State and the pull request is Machinery that
presents it; the Decision is the ruling that survives when Mainmind, GitHub's
UI, or any agent harness is removed.

Mainmind Decision members are named
`mainmind-<first-12-candidate-sha>.md`. **Required frontmatter:** `id`, `type`,
`date`, `ruled-by`, `ruling`, `ruled-at`, `state`, `outcome`, `base-sha`,
`candidate-sha`, `target-diff-sha256`, `targets`, `status`, `access-scope`, and
`write-class`.

- `type` is `decision`, `state` is `ruled`, `status` is `stable`, and
  `write-class` is `ledger`.
- `ruled-by` names the Founder and the authenticated Mainmind session identity.
  `ruling` is exactly `yes` or `no`; `outcome` is respectively `approved` or
  `rejected`. The body preserves the ruling and any optional Founder words.
- `base-sha` and `candidate-sha` are complete lowercase Git commit IDs.
  `targets` is the complete non-empty set of governed paths shown to the
  Founder.
- `target-diff-sha256` binds the exact bytes of that set. For each target, hash
  the complete before and after UTF-8 bytes, form objects in the field order
  `operation`, `path`, `before_sha256`, `after_sha256`, sort paths by Unicode
  code point, encode the array as compact UTF-8 JSON with no trailing newline,
  and SHA-256 that envelope. A creation has a null before hash.

## Approval history

Let `A` be the target-only candidate: one direct child of `base-sha`, changing
exactly `targets`. After the authenticated Founder says yes, Mainmind appends
one deterministic Decision-only child `B` to `A`. It then uses an ordinary
merge that retains `A` and `B` in ancestry. Squash, rebase, changed targets, or
changed bytes require a fresh ruling.

The Decision does not contain `B`'s own commit ID. The candidate SHA and target
digest determine its path and bytes before `B` exists, avoiding a circular
self-hash.

## Rejection history

After the authenticated Founder says no, `A` never enters canonical history.
Mainmind closes the candidate pull request unmerged and appends only the
deterministic Decision to the canonical branch. The receipt still names
`base-sha`, `candidate-sha`, the exact target digest, and every refused target.

A plain clone can validate the durable ruling schema and binding identifiers.
When candidate objects are available, an independent verifier can also
recompute the digest and verify ancestry. The repository receipt never claims
that a digest alone proves bytes an auditor has not obtained.
