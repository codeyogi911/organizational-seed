---
type: Glossary
status: stable
access-scope: core
write-class: conserved
---
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

**Knowledge**:
Organizational meaning, evidence, or current state that a human or agent may
use to understand, decide, or perform work. It is Standing Knowledge,
Organizational Memory, or Working State; Machinery is outside it.
_Avoid_: files, content, machinery

**Standing Knowledge**:
Durable knowledge that future work must follow or interpret consistently:
identity, Authority, Roles, vocabulary, Kind definitions, Processes, and the
rules for changing them. Its current form is governed in an Instance.
_Avoid_: meta knowledge, configuration, policy layer

**Organizational Memory**:
Durable evidence of what happened, what was decided, and what experience
taught. It grows through ordinary work and is corrected by superseding rather
than rewriting history.
_Avoid_: archive, logs, historical data

**Working State**:
Knowledge about work that is active, draft, or awaiting Judgment. It may be
updated by its performing Process and gains no standing Authority merely by
existing.
_Avoid_: temporary knowledge, mutable layer

**Machinery**:
Replaceable infrastructure that reads, checks, projects, or presents Knowledge
without owning organizational meaning or Authority. Machinery is not Knowledge.
_Avoid_: source of truth, governance layer

**Seed Process**:
A Process shipped with the Seed because it maintains the knowledge system
itself and is useful to every Instance. It is a starting rule, not continuing
upstream Authority: after an Instance is created, that Instance owns its copy
and reviews any later Seed change before adopting it.
_Avoid_: global process, upstream policy, automatic update

**Instance Process**:
A Process created or adapted by one Instance for its own organizational work.
It belongs to that Instance and does not enter the Seed unless separately
generalized, reviewed, and published as a reusable pattern.
_Avoid_: tenant override, local workflow

**Intent**:
An expression by the founder to the system — spoken, typed, ephemeral. Never stored
as its own artifact. The system realizes intent by turning it into bounded work
using the durable Processes and policies.
_Avoid_: request ticket, intent file

**Outcome**:
The state a Process performance or Task is trying to make true. Every Task has
an outcome; only direction that must coordinate work beyond that Task becomes a
Goal.
_Avoid_: organizational Goal, output file

**Goal**:
An optional durable outcome chosen to coordinate several Tasks, people, or time
periods. It may be organization-wide or scoped by a delegated Role, and grants
no Authority.
_Avoid_: Task outcome, user request, Purpose, permission

**Process**:
The durable definition of how a kind of work is done: standing intent, inputs, steps
a human could follow manually, and explicit success criteria. One definition, many
performances. In an Instance, changed only through that Instance's approval path.
Processes may be Seed Processes or Instance Processes; the distinction says where
the definition begins, not who controls an Instance's current copy.
_Avoid_: workflow, playbook, SOP

**Task**:
One bounded performance of one Process: who asked, its outcome, status, the
output produced, evidence links, and the evaluation verdict. It may link one
durable Goal. Cheap to create; ends **checked** (all Checks pass, awaiting
judgment), then **accepted** or **rejected** (the judge's ruling, with
reasoning).
_Avoid_: job, ticket, run, work item

**Check**:
A deterministic success criterion — pass/fail is a fact any human or script can
establish without judgment (citations resolve, sections present, arithmetic
correct). The code-graded half of an eval.
_Avoid_: test, gate

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
A governed category of Knowledge artifact, defined by one `_kind.md` in its
folder: what it is, its identity rule, required fields, and lifecycle. Records,
Goals, Tasks, Lessons, and leases may each have a Kind.
_Avoid_: file extension, schema class

**Ontology**:
The set of Kind definitions an organization currently has. It lives beside the
artifacts it defines, never as a separate modeling layer, and grows only when a
Process first needs a new Kind. A graph database over it, if ever needed, is an
index (a Mount), not the home.
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
The organization's rulebook — `AUTHORITY.md` — binding Roles to what they may do
freely and what requires Founder approval. Enforced by compliance first, review of
diffs second, Mount-level backstops third; access to a tool never implies permission
to use it.
_Avoid_: permissions, ACL, policy file

**Access scope**:
A repository-native discovery compartment declared on each Knowledge node and
granted to a Role through a trusted Mount. It controls what the Role may find,
read, search, or infer from projections; it never grants Authority to act.
_Avoid_: permission, Role, team, folder visibility

**Write class**:
The mutation ceremony declared on a Knowledge node: `ledger`, `conserved`, or
`ruled`. It selects how a write must land, not who may perform it. Generated
indexes are Machinery and carry no Knowledge write class.
_Avoid_: access level, filesystem mode, edit permission

**Role**:
A durable position in the organization — responsibilities plus authority — that a
human or an agent can occupy. The Role is org state; whoever occupies it is not.
_Avoid_: person, agent, user

**Mount**:
A thin harness-specific binding (a skill, an agent file, a CLAUDE.md/AGENTS.md
pointer, a connector) that connects a harness to durable state it does not own.
Mounts may be regenerated or deleted freely; deleting every Mount leaves the
organization intact.
_Avoid_: integration, plugin, wrapper

**Decision**:
A recorded exercise of Authority: who ruled, what, when, why, and — for a
governed repository mutation — the exact base commit, candidate commit, target
set, and target-diff digest. Task verdicts remain in the Task; rulings on the
organization live as repository-native receipts in `decisions/`.
_Avoid_: approval log, minutes

**Lesson**:
Preserved knowledge from performed work: what happened, what it taught, evidence
links. Free to record — a Lesson changes no behavior by itself. Lessons name
the Standing Knowledge they may affect and enter behavior only through
[Review Lessons](processes/review-lessons.md) and an approved
[Change Standing Knowledge](processes/change-standing-knowledge.md). A Lesson's
standing weight must track its evidence: recurring evidence upgrades it; a
closed one-off decays.
_Avoid_: learning, insight, retro note

**Governed candidate**:
An exact target-only Git commit prepared for a Standing Knowledge change. It is
Working State, carries no Authority, and becomes current only when an
authenticated Founder Decision binds its complete target diff and ordinary Git
history retains both candidate and receipt.
_Avoid_: Proposal artifact, unbound branch, mutable draft

**Conserved**:
A change rule applied to Standing Knowledge: its current form changes only
through an exact governed candidate and authenticated Founder Decision.
Conserved is not a folder or a separate Knowledge class.
_Avoid_: conserved core, locked files, protected configuration

**ORG.md**:
The canonical entry file of an Instance. The single file a new human or agent opens
to understand the organization's purpose, Roles, Authority, knowledge model,
and links to current state. Deliberately not README.md, which describes the repo
as a project.

**Lease**:
A session's advisory claim on mutation scopes, held as a file in
`work/_active/`. Heartbeat-kept, stale-breakable, fenced by self-re-read.
Collision *avoidance*; the write discipline is collision *safety*.
_Avoid_: distributed lock, mutex (implies enforcement that files cannot give)

**Steward**:
A chartered Role occupied by agents: narrow enumerated grants, hard never-
boundaries, probation with per-mutation review. The unit of "hiring" in an
agent-driven organization.

**Deadman check**:
Every scheduled process has a date-stamped expected report; the next run (and
the weekly review) verifies the previous one exists. Silence is never success.

**Correction**:
A change that replaces a false or contradictory current claim while preserving
truthful history. Correct Standing Knowledge through its governed change path;
correct Organizational Memory with a dated superseding entry.
_Avoid_: silent fix, historical rewrite
