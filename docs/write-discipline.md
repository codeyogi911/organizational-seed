# The write discipline — how external mutations survive crashes and collisions

Distilled from live operation (concurrent agents working the same books).
These rules are what make the concurrency convention's leases safely
*advisory* rather than load-bearing.

1. **Deterministic references.** Every external write carries an identity
   derived from its cause (e.g. a hash of the source transaction id). The same
   event maps to the same reference on every run, forever — so re-runs detect
   prior work instead of repeating it.

2. **The external system is the write-ahead log.** Stamp evidence into the
   system you are mutating (references, notes naming source signal ids, a
   comment on the parent document). A crashed session's progress is then
   readable by any successor from the system itself — no local state needed.

3. **Recovery is re-running the process.** With 1 + 2 there is no separate
   crash-recovery procedure: idempotency branches find what landed and do only
   what is missing. Design every mutation sequence so that stopping anywhere
   leaves a state a fresh run can finish.

4. **Fresh pre-write reads, never cache.** Immediately before every write,
   re-read the exact documents involved. If the state changed since you looked
   — a document voided, deleted, or edited by another hand — halt mutations
   and flag. An unexplained mid-run change is an implicit foreign lease.

5. **Post-read every write.** A write you did not read back is a write you do
   not know happened. Require the post-read to match intent exactly; log
   before → after.

6. **Bulk pulls prove presence, never absence.** Paged lists lie at the
   cutoff and under load. Any "X does not exist" conclusion must be
   re-verified with a targeted direct lookup before it becomes a flag or
   (worse) a create.

7. **Derive state from the owning side.** A document's state lives on the
   document (match by id and deterministic reference), not on whatever
   happens to name it from the other side of a link.

8. **Corrections supersede, never rewrite.** Reports are append-only; a wrong
   conclusion is retracted by a dated `## Correction` section that names what
   it supersedes. The org may be publicly wrong and self-repair — that is a
   feature, and it is only possible if history is never edited.

9. **A confident-looking signal is not verification.** An empty search
   result, a validation error's literal wording, a document's own stated
   cadence, another system's ledger — each can be mistaken for ground truth
   because it *looks* authoritative. When a check is meant to establish
   presence, absence, cause, or schedule, trace it to the source that
   actually knows, not a description or proxy of it. Rules 4, 6, and 7 above
   are this principle applied specifically to writes; it holds just as well
   for reads, diagnosis, and doctrine — a process's own documentation
   describing its intended cadence is a claim about intent, not evidence of
   what actually runs.
