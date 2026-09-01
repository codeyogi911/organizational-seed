---
type: Execution
status: stable
access-scope: core
write-class: ruled
---
# Execution

How to run work in this organization — read at boot, applied before the first
tool call. **This file shapes strategy; it grants nothing.**
[AUTHORITY.md](AUTHORITY.md) is the ceiling, a Process supplies permission,
and where this file seems to disagree with either, this file yields.

## Size the work before starting

- One bounded question with an obvious reader: answer it directly. No ceremony.
- Anything multi-step: name the independent pieces first — what each must
  read, what it must produce, and which pieces share state. The decomposition
  is worth thirty seconds even when you will do every piece yourself.

## Parallelize what is independent

- Pieces that share no working state may run at the same time. Pieces that
  write the same file, ledger, or Record never do — follow the
  [write discipline](docs/write-discipline.md) and the session-lease
  convention under [work/_active](work/_active/).
- Reads parallelize freely. Writes serialize per artifact.

## Delegate when your harness offers subagents

**A large task is a management job.** When subagents are available, delegate
bounded pieces and act as the manager:

- Every delegation names the exact paths to read, the bounded question, and
  the shape of what comes back. Require citations; discard uncited claims.
- Delegation moves work, never Authority. A subagent inherits your limits,
  and the reserved powers in [AUTHORITY.md](AUTHORITY.md) stay reserved no
  matter how many agents are running. Judgment is never delegated.
- The Task, its receipts, and the answer to the Judge remain yours. "A
  subagent said so" is not evidence; the citation it carried is.
- No subagent tool? The same decomposition runs sequentially. Nothing in this
  file requires any particular harness.

## Stay the manager

- Merge results yourself; verify every citation resolves before a claim
  crosses into a Record or an answer.
- Surface disagreement between pieces as a finding, never a silent pick.
- Stop delegating when coordination costs more than the work: three bounded
  pieces beat eight vague ones.

> Template note: these defaults are safe for any organization. Sharpen them —
> preferred decomposition sizes, when a checkout beats a Mount, which
> Processes justify parallel agents — through the ordinary governed route.
> Keep tenant facts out of this file; its pattern may travel back to the Seed.
