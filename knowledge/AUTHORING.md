---
type: Authoring Rules
status: stable
access-scope: core
write-class: conserved
---
# Authoring durable knowledge

Use these rules when changing durable knowledge in the Seed or an Instance.
First classify it through [KNOWLEDGE.md](KNOWLEDGE.md); a file's class, not its
extension, determines its change route.

1. **Write for a cold reader.** The file must make sense without conversation
   history.
2. **Keep one current home.** Link to a rule instead of copying it. When
   teaching moves from a Lesson into Standing Knowledge, leave a short pointer
   and let Git keep the old detail.
3. **Keep one purpose per file.** A reader should know why the file exists.
4. **Cite material claims.** Name the Record or source and its freshness when
   either may change.
5. **Keep machinery replaceable.** A tool or Mount may check durable knowledge;
   it may not become its canonical home.
6. **Classify before exposure.** When [ACCESS.md](ACCESS.md) is active, every
   Knowledge node declares one `access-scope` and one `write-class`. Missing or
   unknown classification must fail closed for non-Founder readers.

## Write the agent team as knowledge

The team's Roles, responsibilities, reporting relationships, Process bounds and
named channels are Standing Knowledge. The agents and host configuration that
execute those Roles are replaceable Machinery. Keep the team in the knowledge
bundle so another human or harness can understand it without the original chat.

When a conversation establishes or changes the team, prepare the corresponding
knowledge update without waiting for a separate request to write it down. Cite
the instruction or Decision, reuse existing Role charters and member identities,
and leave unresolved choices explicit. Do not invent seats, reporting lines or
grants just because no team has been recorded.

Use `roles/agent-team.md` as an index of existing Role charters, unless `ORG.md`
names another home. Each Role owns its purpose, responsibility and boundaries;
the index links them. Record portable names for Roles, Processes and channels.
Keep credentials, vendor channel IDs used as the only name, and host-only setup
outside the organizational map.

For a Mainmind Mount, the following fictional example shows the index and two
seat headers. Paths are relative to this knowledge bundle: in a checkout,
`roles/books.md` is `knowledge/roles/books.md`; the Mount reads `roles/books.md`.
Adapt the example to an evidenced team through the normal governed change route.
These code blocks do not create active Roles in the Seed.

Index at `roles/agent-team.md`:

```yaml
---
kind: Role
title: Agent team
access-scope: core
write-class: conserved
agent-team:
  - roles/chief-of-staff.md
  - roles/books.md
---
```

Header for the Chief of Staff's charter at `roles/chief-of-staff.md`:

```yaml
---
kind: Role
title: Chief of staff
access-scope: core
write-class: conserved
seat: cos
boot-order: 1
channels:
  - Operations
---
```

Header for the Books charter at `roles/books.md`:

```yaml
---
kind: Role
title: Books
access-scope: core
write-class: conserved
seat: agent
boot-order: 2
reports-to: chief-of-staff
channels:
  - Finance review
---
```

Write each charter's body using the existing
[Role charter template](roles/_charter-template.md). Cite the governing Processes
rather than restating their rules. Use the organization's actual access scopes.
The optional `member` field binds a seat to an existing live member slug; without
it the Role basename is the seat slug. A `reports-to` value names another seat's
slug. Optional `process-bounds` lists governing Process names or paths. The
[Mainmind agent-team reference](https://mainmind.app/docs/agent-team) gives the
full reader contract and limits; the organization's Authority still governs use.

A nonempty Mainmind team names exactly one `cos`, unique seat slugs and unique
positive `boot-order` values. Put the Chief of Staff first. An empty index does
not define a team. A scoped Mount may hide an existing index or Role: verify
source and access before proposing a replacement. Recording a seat does not
invite a member, grant access or start an agent.

Prepare one exact candidate covering the index and affected Roles, and `ORG.md`
when its team declaration changes. Follow
[Change Standing Knowledge](processes/change-standing-knowledge.md) for the
required Instance ruling. Preparing the update does not approve it. After an
approved change lands, verify it through the normal reading route; with Mainmind,
a fresh `boot` should return the intended team at the serving commit.

This authoring trigger is guidance for writers and reviewers, not a mechanical
check that detects every conversation or creates a team automatically. Existing
Instances adopt Seed changes only through their own review; this Seed never
updates their authoring rules on their behalf.

## Standing Knowledge review

Before approving new or materially changed Standing Knowledge:

1. Confirm the file is the one current owner of the rule, definition,
   capability, or authority being changed.
2. Name the operation: create, correct, improve, merge, rename, or retire.
3. Confirm every material claim matches cited evidence and that removed rules
   or exceptions are named explicitly.
4. Confirm it contradicts no other governed file — AUTHORITY.md, ORG.md, a Role,
   a standing Decision, a Record, or another Process covering the same outcome.
   A Process that instructs an Operator to perform a reserved power reads as
   clean in its own diff; only this check catches it.
5. Confirm Organizational Memory remains truthful; supersede history instead
   of rewriting it.
6. Confirm the governed candidate names its complete target set and exact
   before/after bytes. Power-expanding and non-expanding changes use the same
   exact-candidate Founder Decision contract; Authority effect never lowers the
   receipt standard.
7. Run the mechanical checks and review the exact Git diff.
8. Confirm each invariant the change adds or amends is **enforced or
   advisory**: it names the check that fails when it stops being true — a
   doctor rule, a CI check, or a per-process Check — or the rule itself states
   that it is guidance. A rule with no checker decays
   ([enforcement](docs/enforcement.md#a-rule-with-no-checker-decays)); a
   checker whose failures are routinely ignored is the same defect.
9. In an Instance, confirm the exact change carries the Founder ruling required
   by `ORG.md` and `AUTHORITY.md`. In the Seed source, confirm the branch or
   pull request received the repository's required maintainer review.

## Additional Process review

Before approving a new or materially changed Process:

1. Apply the Process contract's
   [name-the-outcome review](processes/_contract.md#name-the-outcome) and record
   whether all four names agree.
2. Confirm that no existing Process already owns the outcome.
3. Confirm that the change preserves every prior boundary or explicitly names
   what is being removed.
4. Confirm the Boundaries section states the permission this Process supplies,
   including an explicit "nothing beyond AUTHORITY.md" where that is the answer,
   and that it links rather than restates anything the ceiling already owns.
5. Confirm that copied teaching was removed from its old live home.

The doctor is a tripwire for obvious drift. It cannot decide whether two names
mean the same outcome; that remains part of review.
