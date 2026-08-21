---
status: accepted
---

# Bindings, not homes

Harness constructs — skills, agent files, CLAUDE.md — are tempting homes for
processes and roles: they auto-load and feel alive. We decided all durable state
lives in neutral Markdown (`ORG.md`, `processes/`, `records/`), and harness files
are thin Mounts that point at it. A process stored in a SKILL.md would be state
hidden inside machinery, written in a harness dialect, and subject to free
regeneration — while Process changes in an Instance use its approved Proposal or
fast-track path, and Seed source changes use maintainer PR review. Deleting every
Mount must leave the organization fully operable; the harness-replacement drill
(remove all mounts, verify the org runs from ORG.md alone, restore) tests exactly
that.
