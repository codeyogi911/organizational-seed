# Biomimicry — the seed's design vocabulary

The word for nature-inspired design is **biomimicry** (engineering:
*biomimetics*). The seed has used it implicitly since birth; this page makes
it a deliberate design tool: when a new organizational problem appears, ask
*what does biology do about this?* before inventing.

| Biological mechanism | Seed mechanism | Status |
|---|---|---|
| Conserved genome vs somatic tissue | conserved files (Proposal/fast-track ruling) vs free files (ordinary work) | core since v0.1 |
| Directed evolution / selection pressure | Founder Judgment on every performance; lessons feed proposals | core since v0.1 |
| Immune memory | `lessons/` — the org remembers every infection, tagged by process | core since v0.1 |
| Immune tolerance (don't attack self) | probation: new roles act under per-mutation review until trusted | v0.2 |
| **Immune surveillance** | **`tools/doctor` — continuous self-inspection for malformed cells** (dead links, kind violations, invalid ledger rows, stale leases, unruled "applied" proposals) | **v0.3** |
| Self/non-self recognition | kind definitions (`_kind.md`) validated mechanically; full schema compilation continues in later versions | v0.3 (frontmatter), v0.5 (schemas) |
| Apoptosis (programmed cell death) | stale-lease self-termination: a superseded session must never write again; broken leases are recycled with a record | v0.2 |
| Homeostasis | deadman expected-report checks; drift checks with "growth is the flag, not existence" | v0.2 |
| Quorum / territorial signaling | session leases — advisory scent-marks, not walls; the write discipline is the real boundary | v0.2 |
| Scar tissue (and its pathology) | the right-size-scar-tissue rule: a lesson's standing weight must track its evidence; closed one-offs decay | learned live |
| Horizontal gene transfer | folding proven ideas in from neighbouring projects, with attribution | practiced (v0.3 owes CODEOWNERS-as-gate to Agentic Enterprise) |
| Redundancy / degeneracy | deliberate audit-vs-housekeep overlap: two organs, same function, never simultaneous | core since v0.1 |
| Membrane (selective permeability) | AUTHORITY.md + the human boundary: nothing spends, sends, signs, or files without crossing a human | core since v0.1 |

Open biomimetic questions worth future versions: **senescence** (when does a
process retire? nothing dies on purpose yet), **caste differentiation**
(one Operator role vs specialized stewards — when to split), and
**symbiosis** (two instances trading services under each other's AUTHORITY —
the v1.0 network question).
