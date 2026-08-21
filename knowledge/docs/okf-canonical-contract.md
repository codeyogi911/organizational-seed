---
type: Reference
state: stable
title: Organizational Seed OKF canonical contract
description: The shared, service-independent bundle contract instantiated by an organization grown from this Seed.
status: stable
---

# Organizational Seed OKF canonical contract

## Boundary

Durable organizational knowledge is one self-contained Open Knowledge Format
v0.2 bundle under `knowledge/`. Repository tooling and harness Mounts remain
outside that bundle and point into it. A generated index, search store, graph,
database or prompt bundle is a projection and never outranks the Markdown at an
exact Git commit.

The contract pins the upstream format specification at commit
`62432a095456147ee71e70ac6e4dc0d2dea3ac30`. It adopts no Google Cloud service,
repository, SDK, runtime, schema registry or daemon. An Instance owns its local
copy of the validator and may extend the profile without depending on the Seed
repository at runtime.

## Shared structure

- `knowledge/ORG.md` is the canonical entry point.
- `knowledge/AUTHORITY.md` is the constitutional ceiling.
- Organizational directories retain their relative paths inside `knowledge/`.
- Root `AGENTS.md` and other Mounts route into the canonical bundle but own no
  organizational fact.
- `KnowledgeBundle.inventory`, `compile` and `validate` are the public format
  seams. Consumers do not implement parallel frontmatter parsers.

## Profile

```json okf-profile
{
  "profile": "organizational-seed-okf-canonical-v1",
  "okf_version": "0.2",
  "upstream_commit": "62432a095456147ee71e70ac6e4dc0d2dea3ac30",
  "bundle_root": "knowledge",
  "bundle_title": "Organizational Seed",
  "source": {
    "root": "knowledge",
    "files": [
      "AUTHORING.md",
      "AUTHORITY.md",
      "CONTEXT.md",
      "KNOWLEDGE.md",
      "ORG.md"
    ],
    "directories": [
      "decisions",
      "docs",
      "goals",
      "lessons",
      "processes",
      "proposals",
      "records",
      "roles",
      "work"
    ]
  },
  "type_rules": [
    {"glob": "AUTHORING.md", "type": "Authoring Rules"},
    {"glob": "AUTHORITY.md", "type": "Authority"},
    {"glob": "CONTEXT.md", "type": "Glossary"},
    {"glob": "KNOWLEDGE.md", "type": "Knowledge Model"},
    {"glob": "ORG.md", "type": "Organization"},
    {"glob": "decisions/fast-track.md", "type": "Decision Ledger"},
    {"glob": "docs/adr/**", "type": "Architecture Decision"},
    {"glob": "docs/**", "type": "Reference"},
    {"glob": "goals/_kind.md", "type": "kind-definition"},
    {"glob": "goals/**", "type": "Goal"},
    {"glob": "lessons/**", "type": "Lesson"},
    {"glob": "processes/**", "type": "Process"},
    {"glob": "proposals/0000-proposal-template.md", "type": "Proposal Template"},
    {"glob": "proposals/**", "type": "Proposal"},
    {"glob": "roles/**", "type": "Role Template"},
    {"glob": "work/_active/**", "type": "Session Lease"},
    {"glob": "work/_kind.md", "type": "kind-definition"},
    {"glob": "work/**", "type": "Task"}
  ],
  "identity_overrides": {},
  "incompatible_field_overrides": {},
  "lifecycle": {
    "draft_types": ["proposal"],
    "draft_state_prefixes": ["draft", "proposed"],
    "deprecated_state_prefixes": ["retired", "superseded", "withdrawn"],
    "default": "stable"
  }
}
```

The profile declares `source.root` as `knowledge` and keeps every source path
relative to that root. Recompiling to an external bundle must reproduce the
canonical values and bodies without an extra directory prefix.

## Failure and rollback

Missing YAML support, malformed or duplicate frontmatter keys, ambiguous type
or lifecycle mapping, lossy projection, invalid reserved files, escaped paths
or duplicate emitted identities stop compilation. A migration is recovered by
reverting its named Git commit; a changed candidate invalidates its receipts.
