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
The durable definition of how a kind of work is done: standing intent, inputs, steps
a human could follow manually, and explicit success criteria. One definition, many
performances. Changed only via approved Proposal.
_Avoid_: workflow, playbook, SOP

**Task**:
One bounded performance of a Process: who asked, status, the output produced,
evidence links, and the evaluation verdict. Cheap to create; ends **checked** (all
Checks pass, awaiting judgment), then **accepted** or **rejected** (the judge's
ruling, with reasoning).
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
The organization's rulebook — `AUTHORITY.md` — binding Roles to what they may do
freely and what requires Founder approval. Enforced by compliance first, review of
diffs second, Mount-level backstops third; access to a tool never implies permission
to use it.
_Avoid_: permissions, ACL, policy file

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
A recorded exercise of Authority: who ruled, what, when, and why. Lives in the
artifact it rules on (task verdicts in the Task, proposal rulings in the Proposal);
only decisions that rule on the organization itself get a standalone file in
`decisions/`.
_Avoid_: approval log, minutes

**Lesson**:
Preserved knowledge from performed work: what happened, what it taught, evidence
links. Free to record — a Lesson changes no behavior by itself. Every Process's
first step is to read the Lessons tagged with it. A lesson's standing weight must
track its evidence: recurring evidence upgrades it; a closed one-off decays.
_Avoid_: learning, insight, retro note

**Proposal**:
A requested change to a governed file (Process, Authority, identity), carrying
reason, evidence, expected benefit, validation method, and rollback method. Free to
write; applying it requires a Founder Decision recorded in the Proposal. A Lesson
becomes a Proposal when acting on it would change a governed file.
_Avoid_: change request, RFC, PR (the mechanism, not the artifact), mutation (the
biological reading of the same thing)

**Conserved core**:
The germline of an Instance — identity, Authority, Roles, and Processes — where
change requires an approved Proposal. Everything else is somatic: free to change
through ordinary work. Directed evolution means selection happens before a mutation
reaches the conserved core, never after.
_Avoid_: locked files, protected config, constitution

**ORG.md**:
The canonical entry file of an Instance. The single file a new human or agent opens
to understand the organization, current goal, authority, active work, and next
action. Deliberately not README.md, which is reserved for describing the repo as a
project.
