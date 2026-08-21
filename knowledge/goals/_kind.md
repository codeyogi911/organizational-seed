---
id: _kind
type: kind-definition
of: goal
state: active
status: stable
---

# Kind: Goal

A Goal is an optional durable outcome chosen to coordinate work across several
Tasks, people, or time periods. It turns Purpose into explicit direction, but
grants no Authority and does not prescribe how the outcome must be reached.

The Goal definition ships with the Seed because organizations commonly need
this form of coordination. The Seed source carries no live Goal members, and an
Instance need not create any until a durable Goal is useful.

Do not create a Goal merely because someone requested a Task. Every Task has an
outcome through its Process; that outcome remains in the Task unless it needs a
longer-lived organizational home.

**Identity rule:** one file per durable outcome, named with a short stable slug.
Do not put a date in the identity merely because the Goal has a target date.

**Required frontmatter:** `id`, `type`, `description`, `state`, `set-by`, and
`set-on`. `type` is **Goal**. `state` is **active**, **achieved**, **abandoned**,
or **superseded**. `set-by` names the Role that chose it; `set-on` is
`YYYY-MM-DD`.

**Optional frontmatter:** `target-date`, `superseded-by`, `owner`, and `scope`.
An owner coordinates work but gains no Authority from ownership.

Use five short body sections:

1. **Outcome** — the desired state, stated so a cold reader understands it.
2. **Why now** — the evidence or intent that makes it current.
3. **How we know** — observable evidence that would support achievement.
4. **Not this** — nearby outcomes explicitly outside the Goal.
5. **Direction source** — the ruling, Role mandate, or quoted intent that set the
   Goal; later lifecycle rulings are appended here with their date and reason.

An active Goal is Working State. Achieved, abandoned, and superseded Goals are
Organizational Memory and remain at the same path. The Instance decides through
Authority and Role charters who may set which scope of Goal.

A Task may name one primary Goal. When it does, the Task is the relationship:
one Goal may be advanced by many Processes, and one Process may serve many Goals
through different Tasks. A Task with no organizational Goal remains valid.
