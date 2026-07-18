---
id: _kind
kind: kind-definition
of: system
---

# Kind: system

An external counterparty holding state the organization uses but does not govern —
Gmail, a storefront, a helpdesk, the bank. The organization can never own a
System's state; it owns exactly three things about it: what we know of its state
(Records with `source` + `as-of`), who may touch it
([AUTHORITY.md](../../AUTHORITY.md)), and how we touch it (Mounts). The System is a
durable fact about the org's world; any connector to it is disposable machinery.

**Identity rule:** one record per external system relationship; slug = common name
(e.g. `gmail`, `shopify`).

**Required frontmatter fields:**

- `id` — the slug
- `kind` — `system`
- `name` — what it is
- `owns` — the state this system is the **source of truth** for
- `access` — what access exists and through what kind of Mount (`none` if none)
- `status` — `active` | `retired`

**Recommended:** `resource` — canonical URI of the system itself (omit rather than
guess); `description` — one-line summary.

**Rules:**

- Any Record mirroring a System's state must carry `source` and `as-of` — mirrors
  decay, so processes that consume them should bound their staleness with a Check.
- Access is not permission: an available Mount grants nothing; only AUTHORITY.md
  does.

**Why this Kind exists — the adoption note:** no organization adopts the seed
greenfield. Adoption is acknowledgment, not migration: enumerate your systems as
records, declare who owns which truth, and run one process against them. State
migrates inward only if a process ever earns it; otherwise the seed stays a
federation — it owns the *why*, the *who-may*, and the *what-we-learned*, while
each System keeps owning its data.
