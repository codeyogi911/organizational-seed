---
state: accepted
supersedes: 0001 change-route sentence; 0002 mechanism description
type: Architecture Decision
status: stable
---

# Classify knowledge before changing it

The earlier directed-evolution decision correctly put Founder selection before
governed change, but described the organization only as a conserved core and
free remainder. That model does not distinguish artifacts that must behave
differently: Kind definitions govern meaning, historical Decisions must not be
rewritten, open work must remain easy to update, and tools must remain
replaceable.

We therefore classify every artifact by origin and responsibility. Seed versus
Instance records origin and current ownership. An artifact is either Knowledge
or Machinery. Knowledge is Standing Knowledge, Organizational Memory, or
Working State. Machinery sits outside Knowledge: it may read, check, project,
or present Knowledge but cannot own organizational meaning or Authority.
Conserved names the approval rule applied to Standing Knowledge rather than a
separate Knowledge class.

Three Seed Processes divide evolution without overlapping ownership:
`handle-uncovered-work` reaches the smallest safe result when no Process fits;
`review-lessons` selects absorb, keep, reroute, or close; and
`change-standing-knowledge` creates, corrects, improves, merges, renames, or
retires what future work follows. Process creation is one operation of the last
route, not a separate mutation system. A directly evidenced error may enter it
without manufacturing a Lesson.

This preserves ADR 0001's Mount boundary and ADR 0002's directed selection
while superseding their narrower change-route and Lesson-to-change descriptions.
The cost is an explicit classification step before durable edits; the benefit
is that current work stays easy to update without leaving governing definitions
or historical evidence equally mutable.
