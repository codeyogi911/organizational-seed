---
id: _kind
type: kind-definition
of: task
state: active
status: stable
access-scope: core
write-class: conserved
---

# Kind: Task

A Task is one bounded performance of one Process. Its local outcome comes from
that Process and the request; it may also advance one longer-lived Goal.

The Seed source ships this definition but carries no live Task members.

**Identity rule:** one top-level Markdown file per performance under `work/`,
named `YYYY-MM-DD-what-is-being-done.md` or another stable time-scoped id defined
by the Process.

**Required frontmatter:** `id`, `type`, `process`, `state`, `opened`,
`requested-by`, and `output`. `type` is **Task**. `process` is the active Process
id used for the performance. `state` is **open**, **checked**, **accepted**, or
**rejected**; `opened` is `YYYY-MM-DD`.

**Optional frontmatter:** `goal`, the root-relative path to one active Goal under
`goals/` when this Task advances durable organizational direction. Do not add it
for a one-off user request or merely repeat the Task outcome as a Goal.

The body quotes the request, links the Process and any Goal, records evidence
and the output, and preserves the applicable Judgment. Open and checked Tasks
are Working State. Accepted and rejected Tasks are Organizational Memory and
remain at their stable paths.

A Task may advance a Goal only within its Process and Authority. Linking a Goal
never grants permission, widens a Process, or substitutes for a required
Decision.
