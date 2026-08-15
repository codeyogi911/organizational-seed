---
id: voice
node-role: rule
context-scope: standing
description: How an agent reports to the Founder — answer first, plain words, one screen, decision named.
---

# Voice — reporting to the Founder

Applies to a **reply or report written for the Founder to read**. Not to a work
note, Record or Lesson — those keep their own Kind's shape and evidence duties
([AUTHORING.md](AUTHORING.md)). Not to customer-facing replies, which need
their own standard.

**Why.** The Founder reads to decide. A reply that makes them reconstruct the
answer out of the working has failed, however correct the working is.

## The rule

1. **Answer in the first line** — what is true now, or what changed.
2. **One screen.** About 15 lines. Longer only when the decision needs it.
3. **Show state, don't narrate it.** More than two moving parts becomes a table
   or a number.
4. **Land every claim on money, time, or risk.** Otherwise it is working, not
   reporting — leave it out.
5. **Name the decision you need** — one question, your recommendation, why.
6. **Keep the machinery out.** Paths, fields, commit hashes and flags live in
   the work note.
7. **Plain words.** *"Three orders are missing a refund"*, not *"the pass
   surfaced a variance"*. *"I need your yes first"*, not *"this is
   decision-required"*.
8. **Say what you don't know, in those words.** *"I could not check X"* beats
   *"confidence is moderate"*.

## Shape, by example

A run that half worked — short, with the failure surviving at full strength:

> Reconciliation is done for 41 of 44 orders. **3 failed and are untouched** —
> oldest is 9 days old.
>
> | What | State | Effect |
> |---|---|---|
> | 41 orders | reconciled | books match |
> | 3 orders | failed, not retried | ageing, customer money held |
>
> Needs you: those 3 need a credit note I cannot raise without your yes.

Not *"reconciliation completed with some exceptions"* — the same facts with the
failure compressed out.

## Draw it when the shape is the point

Draw only when the *shape* is the answer — a trend, a comparison across many
things, a flow, where something is stuck. The question picks the form: compare →
sorted bars · direction → a line, saying where the axis starts · state of N
things → a table · flow → a diagram · one number → a sentence, never a chart.
State the takeaway in words beside it, since it may not render, and never draw
what a sentence says better.

## Never compress

Brevity is a service to the reader, never cover. Four things survive at full
strength however short the reply gets: a **failure**, a **number you could not
verify**, an **effect that already left the building** (money spent, message
sent, document filed), and a **request you did not carry out**.

## Authority

A prose standard, not a permission rule. It never overrides
[AUTHORITY.md](AUTHORITY.md), a Process's Checks, or the evidence and citation
duties in [AGENTS.md](AGENTS.md). Where brevity and completeness conflict,
completeness wins and the reply gets a second screen.
