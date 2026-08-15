# `tools/doctor` — operator note

[`tools/doctor`](../doctor) is the instance's mechanical surveillance: six
checks that a human could run by hand, none of which needs a model. Stdlib
Python, no configuration, no network.

```sh
tools/doctor              # the current directory
tools/doctor path/to/instance
```

| Severity | Means | Exit |
|---|---|---|
| `FAIL` | Something is wrong and the instance is not honest about it | 1 |
| `WARN` | Something is missing that this instance may not have chosen yet | 0 |
| `NOTE` | Not a defect: a next step for a tree that is still the template | 0 |

Warnings never fail a run. A warning that should fail is a warning in the
wrong severity — change it, rather than teaching operators to read past it. A
`NOTE` rides along under a `clean` run and is never counted.

## The checks

| Tag | Severity | What it protects |
|---|---|---|
| `links` | FAIL | A cold reader can reach the next file |
| `kinds` | FAIL | Each Kind's declared frontmatter is actually present |
| `owners` | FAIL / WARN / NOTE | The conserved core has a mechanical gate |
| `boot` | FAIL | The boot path stays inside the budget `ORG.md` sets |
| `now` | FAIL | Mutable state stays out of the organization's law |
| `freshness` | WARN | Nothing ages past the limit its Kind declared |

**`links`** — every relative Markdown link resolves. Blockquoted lines are
exempt: a template note or quoted excerpt carries the links of the file it is
talking about, not of the file it sits in.

**`kinds`** — for every directory holding a `_kind.md`, each sibling carries
the frontmatter that Kind declares required. Two things about the parse are
worth knowing before you write a Kind. It reads only the *head* of each
bullet — the backticked names ahead of the em dash — because the explanation
after the dash is full of backticked *values* (`open`, `codified`, `declined`)
that are not field names. And it skips a bullet that marks itself conditional
("required once…", "required when…", "optional"), because a flat list cannot
express `disposition`'s rule and demanding it always would be a false failure
the operator has to argue with.

**`owners`** — a CODEOWNERS that exists but leaves a conserved path unowned is
a failure, because it reads as covered and is not, which is worse than having
none. No CODEOWNERS at all is a warning in an organization and only a note in
the template — see [Two states](#two-states-template-and-organization) below.
The conserved list is the one in
[`CODEOWNERS.example`](../../CODEOWNERS.example) and
[docs/enforcement.md](../../docs/enforcement.md). This is a string check on the
file, not a CODEOWNERS matcher: it proves the line is there, not that your host
resolves it the way you meant.

**`boot`** — the caps come from the table under `ORG.md`'s "The boot path is
size-capped" heading, and never from the tool. A budget a tool keeps privately
is a budget the organization cannot amend, and the amendment is the point: the
cap is a governance statement that happens to be machine-readable. A listed
file that does not exist costs zero lines. A table that cannot be parsed is
itself a failure — silence there would mean the cap quietly stopped applying.

**`now`** — `ORG.md` may not carry a `Now` section. Current work belongs in
Records, work notes and Git history. In the most-read governance file it is
paid for by every session, and no session can tell how stale it is.

**`freshness`** — a Kind opts in by declaring `max-age-days`, and narrows with
`freshness-applies-to`. That is how
[`records/gaps/_kind.md`](../../records/gaps/_kind.md) gets its open gaps
reported instead of forgotten. The check is generic on purpose: the rule lives
in the Kind that set it, so a new Kind gets the same enforcement without a code
change here.

## Two states: template and organization

**The template ships no CODEOWNERS on purpose, so on the template that absence
is not a defect.** A gate checked in naming `@founder-handle` is an unusable
gate handed to every fork; `CODEOWNERS.example` is the shipped artifact, and
copying it is step one of adoption.

That leaves the `owners` check needing to tell two trees apart, and the
discriminator is already in the repository: an un-instantiated seed still
carries unreplaced `{placeholders}` in `ORG.md`. Adoption replaces them.
Nothing else does.

| `ORG.md` | CODEOWNERS | Result |
|---|---|---|
| has `{placeholders}` | none | `NOTE` — clean, with the next step for a forker |
| filled in | none | `WARN` — an organization with no gate |
| either | present, conserved path unowned | `FAIL` — never ambient |

**Do not "fix" the quiet case.** A validator that warns about its own
repository on every single run teaches every forker, on day one, to ignore its
output — and [docs/enforcement.md](../../docs/enforcement.md) already names
that failure: once a checker reports on every run, a genuinely new finding has
to be discovered by diffing output rather than by reading it, and the gate has
become noise. Making the template warn about itself again is not finding a bug.
It is re-creating one.

The placeholder match is deliberately narrow — a brace, a letter, then prose on
one line — and code fences and inline spans are removed before matching, so
`${VAR}`, `{{mustache}}`, `map[string]any{}` and a JSON example cannot be
mistaken for an unfilled blank. Swept across the whole seed the pattern matches
only genuine blanks, in `ORG.md`, `AUTHORITY.md`, `processes/index.md`,
`roles/_charter-template.md` and `decisions/_template.md`. The trade-off is
real and worth stating: an organization that writes `{like this}` in prose in
its own `ORG.md` will read as un-instantiated. Use a different notation, or
fill the gate in and the question never arises.

## The walk prunes other work trees

**A directory containing a `.git` entry — file or directory — is another work
tree, whatever it is called. It is pruned.**

[EXECUTION.md](../../EXECUTION.md#repository-changes) tells every writer to use
a change-specific worktree, so sibling checkouts appear inside the tree under
whatever this week's change happens to be named. No skip list can enumerate
them, and the failure is not theoretical: on the origin instance, one commit of
this tool reported **32 failures from a checkout holding three nested worktrees
and 10 from a clean one**. All 22 extra findings were true. Every one of them
was about somebody else's half-finished work, and acting on any of them would
have meant one session "fixing" another session's files.

A skip list would also have to be maintained by the person who least wants to
think about it — the one debugging why the tool is shouting. The structural
rule needs no maintenance because it asks Git the same question Git asks.

Still pruned by name, for reasons that are not "another session": `.git`
itself (machinery by definition), `node_modules`, `__pycache__` and `.venv`
(generated), and `.claude/` — a harness binding is a disposable adapter that
owns no durable knowledge ([ORG.md § For harnesses](../../ORG.md)), so an
instance gets linted, not its mounts.

One walk, one prune, shared by every check. The version this replaced had two
walks with two different skip lists, and they had already drifted — which is
[AUTHORING.md](../../AUTHORING.md) rule 3 ("one capability, one owner") failing
in miniature, in a file small enough to read in one sitting.

## A remediation string is doctrine

**A remediation string is doctrine, and it goes stale like any other copy of
doctrine. When a rule changes, grep the check *messages*, not just the check
logic.**

The instance learned this the expensive way: it once shipped a check whose
message told operators to undo an applied Founder Decision. The logic had been
updated for the new rule. The sentence the operator actually read had not — and
the sentence is the part with authority at three in the morning, because it is
the only part anyone reads.

Two consequences for this file's neighbours. Every message here names its rule
in the organization's own words, so a stale one is visible as prose rather than
hiding as behaviour. And when a governance rule changes, the diff is not done
until `tools/doctor` has been read *as text*, top to bottom.

## What it deliberately does not check

- **Business truth.** Nothing here knows whether a number is right, an external
  system agrees, or a ruling was wise.
- **Authority.** It reports; it never edits, and it grants nothing. It is
  replaceable machinery and owns no fact ([AUTHORING.md](../../AUTHORING.md)
  rule 9) — if it disagrees with the Markdown, the Markdown wins and the tool
  is the thing that gets fixed.
- **Concurrency.** That is Git's, through worktrees, branches and merge
  conflicts ([ADR 0003](../../docs/adr/0003-git-owns-repository-concurrency.md)).

## Checks that were retired

If you are upgrading an older instance, these are gone on purpose, not lost:

| Retired check | Why |
|---|---|
| Fast-track ledger rows carry a verbatim ruling | The tier is retired. One route: branch, reviewed diff, Decision file ([ADR 0004](../../docs/adr/0004-one-governance-route.md)) |
| Lease heartbeat freshness | Repository path leases are retired; Git owns concurrency ([ADR 0003](../../docs/adr/0003-git-owns-repository-concurrency.md)) |
| Applied proposals carry a Ruling | The Proposal route is retired; the Decision file is the ruling |

Adding one back means adding its rule back to the durable knowledge first. A
check with no rule behind it is a tool inventing governance.
