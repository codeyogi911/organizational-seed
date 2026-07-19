---
id: _kind
kind: kind-definition
of: session-lease
---

# Kind: session-lease

One live operator session — created at Task start, deleted at Task close.

**Identity rule:** `YYYY-MM-DD-<session-slug>.md`.

**Required frontmatter:** `operator` (harness + model, or human name) · `task`
(work/ id) · `started` (ISO) · `heartbeat` (ISO, refreshed ≤15 min) · `scopes`
(e.g. `{system}:mutate`, `org:now`, `repo:<path>`).

**Optional:** `note` — coordination messages to other operators; `broke-lease`
— the stale lease this session broke, with reason.

Stale after 30 min without heartbeat; any operator may break it (recorded).
Reads never need a lease. **Fencing rule:** the holder re-reads its own lease
before every mutation batch — missing or replaced (different `started` epoch) →
halt immediately; a superseded session must never write again.
