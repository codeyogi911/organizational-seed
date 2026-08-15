# Mounting a harness

A Mount is a disposable binding such as `AGENTS.md`, `CLAUDE.md`, a scheduled
task, a skill or a connector configuration. It points into the organization; it
does not contain the organization.

## What a Mount owns

- repository and entry path;
- Process and Role to use;
- harness-specific identity, schedule or transport;
- a deliberate narrowing of what this trigger will do; and
- mechanics that only this harness can know.

Rules, Process steps, Checks, Authority, current state and connector policy
stay in durable repository files. Copying them into a Mount creates a cache
with no invalidation signal.

## Failure condition

A Mount is defective when it copies durable policy, names a pointer that no
longer exists, widens Authority, or continues from memory after a canonical
file fails to load.

The first of those is the one that bites quietly. A Mount that restates a rule
keeps working after the rule changes — it simply keeps enforcing the old one,
and nothing in the repository can tell. Assume any instruction duplicated into
a Mount will outlive the decision it depended on.

## Changing a Mount

1. Read the durable Process, Role and pointers first.
2. Delete copied knowledge only after verifying its current home.
3. Keep only binding-specific facts or narrowing.
4. Verify every pointer and re-read the trigger or registration after editing.
5. For an in-repository Mount, use the normal Git review path in
   [EXECUTION.md](EXECUTION.md#repository-changes).

No graph classification, path lease or separate node-review record is required.
If a Mount disagrees with the repository, fix the Mount.

## A schedule is not proof of a schedule

A Mount that claims a cadence is a claim, not the cadence. The scheduler's own
registration is the fact. Read the registration when you need to know whether
something is actually scheduled, and give every scheduled Process a
date-stamped expected output so a run that never happened is visible as a
missing file rather than as silence.

Extend that to integration: a scheduler's last-run timestamp proves a run
**started**, and the trunk proves what **landed**. Neither alone can tell work
never done from work done and stranded on a branch — and those need opposite
responses, because re-running a completed close is not harmless.

## A Mount can refuse what Authority permits

"Tool access never grants permission" has an equally true inverse: **an
organizational grant does not guarantee the runtime will execute the call.**

`AUTHORITY.md` answers *may this Role do this*. The harness answers *will this
runtime run this call right now* — and the second can be no while the first is
yes. A permission classifier, a sandbox policy, or a connector's own guardrail
can veto a lawful effect.

That outcome is neither **denied** (nothing in the constitutional ceiling
denied it) nor **decision-required** (no ruling is outstanding). It needs its
own name and its own durable receipt, or every scheduled run re-proves the same
gates from scratch and nobody ever fixes the actual blockage.

Do not route around a refusal. One genuinely different retry to rule out a
call-shape fluke, then stop and report the exact refused action as the
diagnosis. Leave already-landed authorized effects exactly as they are.

## Portability includes data egress

"Read-only" describes what a harness may do to your sources. It does not mean
the performance had no external effect.

Sending organizational material to an inference provider **is** an
information-flow effect. Swapping harnesses can therefore change the
organization's data boundary even when both see the same files and neither
holds a write tool.

So the portability test is stronger than *"delete every Mount and the
organization survives"*. A replacement Runner must preserve organizational
meaning **and permitted information flow** — a harness that reaches the right
answer by disclosing more of the organization is not a conformant substitute.

Where a Process may run across providers, record a manifest naming the provider
and model boundary, the exact context disclosed, whether restricted data is
present, the retention boundary relied on, and the Authority permitting it.
