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
8. In an Instance, confirm the exact change carries the Founder ruling required
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
