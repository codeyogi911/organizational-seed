# Authoring durable knowledge

Use these rules when changing reusable knowledge in the Seed or an Instance.

1. **Write for a cold reader.** The file must make sense without conversation
   history.
2. **Keep one current home.** Link to a rule instead of copying it. When
   teaching moves from a Lesson into a Process, leave a short pointer and let
   Git keep the old detail.
3. **Keep one purpose per file.** A reader should know why the file exists.
4. **Cite material claims.** Name the Record or source and its freshness when
   either may change.
5. **Keep machinery replaceable.** A tool or Mount may check durable knowledge;
   it may not become its canonical home.

## Process review

Before approving a new or materially changed Process:

1. Apply the Process contract's
   [name-the-outcome review](processes/_contract.md#name-the-outcome) and record
   whether all four names agree.
2. Confirm that no existing Process already owns the outcome.
3. Confirm that the change preserves every prior boundary or explicitly names
   what is being removed.
4. Confirm that copied teaching was removed from its old live home.
5. Run the mechanical checks and review the exact Git diff.
6. In an Instance, confirm the change carries the Founder ruling required by
   `ORG.md` and `AUTHORITY.md`. In the Seed source, confirm the branch or pull
   request received the repository's required maintainer review.

The doctor is a tripwire for obvious drift. It cannot decide whether two names
mean the same outcome; that remains part of review.
