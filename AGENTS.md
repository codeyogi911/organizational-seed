# For any coding agent entering this repo

First determine which repo you are in.

## If this is the Seed source

`ORG.md` still begins with `# {Organization Name}`. You are maintaining the
reusable starting pattern, not operating an Instance.

1. Read [README.md](README.md), [CONTEXT.md](CONTEXT.md), and
   [AUTHORING.md](AUTHORING.md).
2. Make changes on a branch, review the exact diff, and use the repository's PR
   approval rules. Do not create an organizational Proposal merely to change
   the Seed source; the Proposal template is content shipped to Instances.
3. Keep the Seed general. It must contain no tenant facts and must never update
   an Instance automatically.
4. Do not store live Tasks, Lessons, Proposals, or organizational Decisions in
   the Seed source. Seed-maintenance evidence lives in issues, reviewed PRs,
   Git history, and ADRs; the runtime folders are content for Instances.

## If this is an Instance

`ORG.md` names a real organization. You are entering an **organization, not a
codebase**.

1. Read [ORG.md](ORG.md) first, then obey [AUTHORITY.md](AUTHORITY.md). Tool
   access never grants permission.
2. Find the relevant Process through [processes/index.md](processes/index.md).
3. Before changing durable knowledge, read [AUTHORING.md](AUTHORING.md). Never
   touch a conserved file without the approval required by the Instance.
4. Perform bounded work as Tasks and cite Records as evidence for material
   claims.

This file and everything harness-specific (`.claude/`, `CLAUDE.md`) are
disposable Mounts. Never store organizational state in them.
