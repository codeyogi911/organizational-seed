# The write discipline — how external mutations survive crashes and collisions

Distilled from live operation (concurrent agents working the same books).

**These rules are why repository leases could be removed.** Git protects the
repository ([ADR 0003](adr/0003-git-owns-repository-concurrency.md)), but no
version-control system protects a payment, an email, or another company's
database. Everything outside this repository is guarded here instead — by
idempotency and verification rather than by locking. One mutator per external
effect at a time remains the standing advisory rule; these nine make a
collision survivable when it happens anyway.

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

   Four distinct ways a read lies about absence, each found the hard way:

   - **A misspelled key and a genuine absence return the same thing.** Before
     reporting absence, list the keys the object actually has and prove the
     field exists on a known-positive case. Absence is the one finding a typo
     can manufacture out of nothing.
   - **The absence of a link is not the absence of the thing.** Prove absence
     against the population that would contain it, not against the object's
     own back-reference.
   - **A field written along only one path measures which path was taken**, not
     whether the thing was done. Ask what writes a field before trusting its
     emptiness.
   - **A source can be fully functional, correctly queried, and still have a
     hard ceiling below the window you asked for** — returned as no error at
     all. Probe the boundary (the oldest record visible under any filter)
     before trusting any "nothing happened before this date".

   Always name the field that established a finding, and scale your doubt to
   the size of the claim.

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

10. **A claim is only as wide as the check you actually ran.** A passing narrow
    check and a true broad claim look identical from outside — both are
    silence. If you assert *only*, *once*, *all*, *every* or *the last one*,
    run the search first and say what you searched. If you did not search,
    narrow the claim to what you verified.

    The failure mode is specific and worth naming: after fixing several copies
    of something you have a vivid memory of fixing them, and that memory feels
    like knowledge. It is a record of what you touched, never of what exists.
    One instance made four completeness claims in a single piece of work, each
    checkable in seconds, none checked — and three successive adversarial
    reviewers each found one more copy than the last.

    For a constraint, the same rule reads: the detection predicate must cover
    the whole statement, or the statement shrinks to what the predicate covers.
    A constraint whose check is narrower than its wording reports healthy while
    being breached — worse than having no constraint, because an absent
    constraint is visibly absent.

11. **A two-sided invariant needs both directions run.** An invariant written
    *"every A has exactly one B"* is two claims, and they fail differently.
    A→B catches the **missing** B. B→A catches the **spurious** B.

    Running B→A alone is seductive, because B is usually the side you own: it
    is easy to enumerate, and it all comes back correct. But **you cannot find
    a missing record by reading the records you have — the absence lives in the
    other system.**

    Name both directions before running either, and state which direction
    produced each conclusion. Never net two populations' totals to decide
    whether to look closer: netting cancels out exactly the pairs of errors
    that were worth finding.
