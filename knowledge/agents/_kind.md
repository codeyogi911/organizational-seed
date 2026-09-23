---
id: _kind
type: kind-definition
of: agent
state: active
status: stable
access-scope: core
write-class: conserved
---

# Kind: Agent home

One folder per agent profile, `agents/<profile-slug>/`, holding what that agent
keeps: `AGENT.md` (its instructions), `memory/` (one learned fact per file),
`journal/` (one note per session saying where it stopped) and `routines/` (one
schedule entry per file).

`AGENT.md` and `routines/*` are conserved: they change by proposal and ruling.
`memory/*` and `journal/*` are ledger members written only by Mainmind's
`agent_home` tool for that agent. No other writer lands under `agents/`.

A home grants nothing. Memory is the agent's own and is never policy.
