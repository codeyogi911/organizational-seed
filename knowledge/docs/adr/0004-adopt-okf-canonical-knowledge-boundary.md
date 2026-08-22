---
id: 0004-adopt-okf-canonical-knowledge-boundary
type: Architecture Decision
status: stable
access-scope: core
write-class: ruled
title: Adopt an OKF-canonical knowledge boundary
description: Keep organizational Knowledge under one portable bundle while repository Machinery remains replaceable.
---

# ADR 0004: adopt an OKF-canonical knowledge boundary

## Context

The Seed already distinguishes Knowledge from Machinery. That distinction also
needs a physical and interoperable repository boundary so an Instance can
validate, project, index, or serve its Knowledge without making any particular
agent harness, search system, managed service, or upstream repository its home.

Open Knowledge Format v0.2 supplies a small Markdown-and-YAML interchange shape.
The local profile pins the evaluated upstream specification commit and preserves
Seed-specific fields as extensions.

## Decision

`knowledge/` is the one canonical OKF bundle in both the Seed and every newly
grown Instance. Standing Knowledge, Organizational Memory, and Working State
live inside it. Repository Machinery—including Mounts, tests, validators, and
projections—lives outside it and points inward.

The contract and local projector are owned here. Google Cloud Knowledge Catalog,
its repository, SDKs, schemas, services, and runtimes are not dependencies.
Consumers use the public inventory, compile, and validate seams instead of
building parallel frontmatter parsers.

## Consequences

- An Instance begins with the same canonical boundary it will operate.
- Moving between agents, indexes, databases, or catalog services does not move
  Authority or organizational meaning out of Git-tracked Markdown.
- Domain lifecycle remains in `state`; OKF `status` carries the broader portable
  lifecycle. Seed-specific fields remain valid extensions.
- Reprojection must be lossless and idempotent. A mismatch or invalid bundle
  fails closed.
- Seed evolution still arrives only as a candidate for Instance review; the
  shared layout creates compatibility, not continuing upstream Authority.

## Verification and rollback

The Seed doctor, focused unit tests, canonical validation, and an external
reprojection diff must all pass for the exact candidate. Rollback is a Git
revert of the migration commit; no managed service state is involved.

The executable profile is
[the OKF canonical contract](../okf-canonical-contract.md).
