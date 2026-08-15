# Organizational Seed

The domain model for a file-based organizational kernel: durable organizational
state kept as human-readable files in a repo, operated by a human or any coding
agent.

## Language

**Seed**:
The reusable pattern of files and rituals that lets an organization run its
processes from a repo. A pattern, not a repo — it is demonstrated by an Instance.
_Avoid_: template, framework, platform, stencil

**Instance**:
One organization living in one repo, grown from the Seed.
_Avoid_: deployment, installation

**Intent**:
An expression by the founder to the system — spoken, typed, ephemeral. Never stored
as its own artifact. The system realizes intent by turning it into bounded work
using the durable Processes and policies.
_Avoid_: request ticket, intent file

**Process**:
The durable definition of how a kind of work is done: outcome, when to use it,
boundaries, evidence and approvals, steps, and an explicit done condition. One
definition, many performances. Changed only through a reviewed Git change and a
Founder Decision.
_Avoid_: workflow, playbook, SOP

**Draft Process**:
An emerging Process in `processes/draft/`, written when repetition looks
plausible but is unproven. **A draft grants no reusable Authority.** It becomes
active only when the Founder rules it so — no count of successful performances
promotes it by itself.
_Avoid_: beta process, provisional SOP

**Doctrine**:
A Process-kind file that states invariants rather than steps — what a clean
record, a balanced book, or a safe configuration means. When an ordinary
Process disagrees with the doctrine it cites, the doctrine wins.
_Avoid_: policy doc, standard (both read as advisory)

**Work note**:
An *optional* file in `work/` for work that is long-running, resumable,
externally effectful, or otherwise needs a durable checkpoint outside Git
commits: bounded intent, current state, evidence, recovery, outcome. A short
answer or a focused repository change does not need one — the commit is the
record.
_Avoid_: task, job, ticket, run, work item (all imply it is mandatory)

**Done condition**:
The explicit statement, in the Process, of what makes one performance finished
— written so that a human or a script can settle it without judgment (citations
resolve, sections present, arithmetic correct, receipt verified). Replaces a
separate mechanical Checks ceremony.
_Avoid_: test, gate, acceptance criteria

**Judgment**:
A success criterion requiring a judge's ruling ("would I act on this?"), not a
mechanical test. Ruled by whoever holds judgment authority for that Process — the
Founder by default; delegable to an agent only through a governed Authority change,
with the Founder's own rulings as the calibration set. Rejection reasoning is
first-class input to Lessons.
_Avoid_: review, sign-off

**Evidence**:
A citation from a claim to a durable source record in the repo. Evidence is a
property of well-formed output, not a folder — a claim without a citation is
unverified by definition.
_Avoid_: attachment, exhibit, proof folder

**Record**:
A durable noun the business touches — a conversation, a product, a customer —
stored as one Markdown file with YAML frontmatter, referenced everywhere by its
stable slug.
_Avoid_: data file, master data, entity (use the Kind's name instead)

**Kind**:
A category of Record, defined by one `_kind.md` in its folder: what the Kind is, its
canonical-identity rule, and required fields. The set of Kind definitions is the
organization's Ontology.
_Avoid_: type, schema, class

**Ontology**:
The set of Kind definitions an organization currently has. It lives as the structure
of Records — never as a separate modeling layer — and grows only when a Process
first needs a new Kind. A graph database over it, if ever needed, is an index (a
Mount), not the home.
_Avoid_: data model, knowledge graph, master data management

**System**:
An external counterparty holding state the organization uses but does not govern —
Gmail, a storefront, the bank. Recorded as a Record declaring what state it is the
source of truth for, what access exists, what Authority governs touching it, and
(when reliably known) its canonical `resource` URI. The System is durable fact; the
connector to it is a disposable Mount. Records mirroring a System's state carry
`source` and `as-of`.
_Avoid_: integration, connector (those are Mounts), third-party tool

**Authority**:
The organization's legitimacy rules, resolved in three layers: the
constitutional ceiling in `AUTHORITY.md`, the reusable permission an approved
Process supplies inside its scope, and a one-time Decision for a single named
effect. Access to a tool never implies permission to use it.
_Avoid_: permissions, ACL, policy file

**One-time Decision**:
Permission for one named effect or bounded batch, recorded before the effect
with its target, evidence, use limit and expiry, and closed afterwards with a
verified outcome receipt. It expires when used and **creates no future
Authority**.
_Avoid_: standing grant, approval (both imply durability it does not have)

**Outcome receipt**:
Verified evidence, read back from the external system after the fact, that an
effect actually landed — not the tool call that requested it. A draft, a
prepared document or a proposed change is not a receipt.
_Avoid_: confirmation, log line

**Role**:
A durable position in the organization — responsibilities, Process eligibility
and Judgment — that a human or an agent can occupy. **Operational effect
Authority comes from the Process being performed**, narrowed by the named work;
a charter states eligibility and limits and never restates Process effect
policy. The Role is org state; whoever occupies it is not.
_Avoid_: person, agent, user

**Mount**:
A thin harness-specific binding (a skill, an agent file, a CLAUDE.md/AGENTS.md
pointer, a connector) that connects a harness to durable state it does not own.
Mounts may be regenerated or deleted freely; deleting every Mount leaves the
organization intact. Written and changed per [MOUNTING.md](MOUNTING.md).
_Avoid_: integration, plugin, wrapper

**Decision**:
A recorded exercise of Authority: who ruled, what, when, and why, carrying the
Founder's verbatim words. Every conserved change needs one, in `decisions/`. A
one-time effect Decision may instead live in the Process's normal output or a
work note — but it must survive independently of chat.
_Avoid_: approval log, minutes

**Lesson**:
Preserved knowledge from performed work: what happened, what it taught, evidence
links. Free to record — a Lesson changes no behavior by itself. Every Process's
first step is to read the Lessons tagged with it. A lesson's standing weight must
track its evidence: recurring evidence upgrades it; a closed one-off decays.
_Avoid_: learning, insight, retro note

**Conserved core**:
The germline of an Instance — identity, Authority, Roles, and active Processes
and doctrines — where change requires a branch, a reviewed diff, and its own
Founder Decision. Everything else is somatic: free to change through ordinary
work. Directed evolution means selection happens before a mutation reaches the
conserved core, never after. An active Process edit stays conserved **even when
described as a correction**.
_Avoid_: locked files, protected config, constitution

**ORG.md**:
The canonical entry file of an Instance. The single file a new human or agent
opens to understand the organization's purpose, Roles, operating model,
conservation rules, and repository map. Deliberately **not** a status page:
current work lives in Records, work notes and Git history, so that routine work
never has to write to the organization's most sacred file. Deliberately not
README.md, which describes the repo as a project.

**One fact, one home**:
The normalization rule: every durable fact — a definition, a rule, a threshold,
a vocabulary term — is stated in exactly **one** file, and every other file
that needs it **cites** it. A second statement of the same fact is not
redundancy, it is a fork with a delay fuse: the copies drift, and nothing says
which one is true. An index or projection may *show* a fact it does not own,
provided it is derived and declares its source. Where a consumer and a home
disagree, the home wins and the consumer is fixed.
_Avoid_: single source of truth (says where, not what), DRY (a code idiom about
repetition, not about authority)

**Claim precedence**:
The ordering that resolves a conflict between two durable claims of the same
kind, stated once in [AUTHORITY.md](AUTHORITY.md): `governance` › `Founder
intent` › `organizational Record` › `external evidence` › `untrusted
third-party content`. Freshness breaks ties within a class; specificity breaks
a freshness tie. Surface a conflict — never average it.
_Avoid_: priority, trust score, ranking

**Gap**:
One recorded instance of the organization failing to supply something a
performance needed — the counterpart to a Lesson. A Lesson is what was learned;
a gap is what was **missing**. Absence cannot be found by inspecting files,
because a missing rule has no file to inspect; it is observable only at the
moment a performance needs it and comes up empty. Never cited as evidence about
the business — only about the repository.
_Avoid_: bug, todo, backlog item

**Steward**:
A chartered Role occupied by agents: eligibility for named Processes, hard
never-boundaries, probation with per-mutation review. The unit of "hiring" in
an agent-driven organization. Its charter grants no effects of its own — see
**Role**.

**Deadman check**:
Every scheduled Process has a date-stamped expected output; the next run and
the periodic review verify the previous one exists. Silence is never success.

Two layers, because they fail differently. The scheduler's last-run timestamp
proves a run **started**. The trunk proves what **landed**. Neither alone
distinguishes work never done from work done and stranded on a branch — and
those need opposite responses, since re-running a completed period close is not
harmless. Check both, and never infer from cadence prose that a scheduler ran.

**Correction**:
A dated section appended to a report that retracts and supersedes an earlier
conclusion in place. History is append-only; being wrong is recoverable,
rewriting is not.
