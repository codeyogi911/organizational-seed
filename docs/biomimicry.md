# Biomimicry — the seed's design vocabulary

The word for nature-inspired design is **biomimicry** (engineering:
*biomimetics*). The seed has used it implicitly since birth; this page makes
it a deliberate design tool: when a new organizational problem appears, ask
*what does biology do about this?* before inventing.

| Biological mechanism | Seed mechanism | Status |
|---|---|---|
| Conserved genome vs somatic tissue | Standing Knowledge (Proposal/fast-track ruling) vs Organizational Memory and Working State (ordinary work) | current model; [ADR 0003](adr/0003-classify-knowledge-before-changing-it.md) |
| Directed evolution / selection pressure | `review-lessons` selects teaching; `change-standing-knowledge` governs every lasting mutation | current model; [ADR 0003](adr/0003-classify-knowledge-before-changing-it.md) |
| Immune memory | `lessons/` — the org remembers what a Process performance taught and the Standing Knowledge it may affect | current model |
| Immune tolerance (don't attack self) | probation: new roles act under per-mutation review until trusted | v0.2 |
| **Immune surveillance** | **`tools/doctor` — continuous self-inspection for malformed cells** (dead links, kind violations, invalid ledger rows, stale leases, unruled "applied" proposals) | **v0.3** |
| Self/non-self recognition | three Knowledge classes separate governed meaning, memory, and current work; Machinery sits outside Knowledge as replaceable infrastructure | current model; [ADR 0003](adr/0003-classify-knowledge-before-changing-it.md) |
| Apoptosis (programmed cell death) | stale-lease self-termination: a superseded session must never write again; broken leases are recycled with a record | v0.2 |
| Senescence | retired Processes leave their stable historical definition while disappearing from active discovery | current model; [ADR 0003](adr/0003-classify-knowledge-before-changing-it.md) |
| Homeostasis | deadman expected-report checks; drift checks with "growth is the flag, not existence" | v0.2 |
| Quorum / territorial signaling | session leases — advisory scent-marks, not walls; the write discipline is the real boundary | v0.2 |
| Scar tissue (and its pathology) | the right-size-scar-tissue rule: a lesson's standing weight must track its evidence; closed one-offs decay | learned live |
| Horizontal gene transfer | folding proven ideas in from neighbouring projects, with attribution | practiced (v0.3 owes CODEOWNERS-as-gate to Agentic Enterprise) |
| Redundancy / degeneracy | deliberate audit-vs-housekeep overlap: two organs, same function, never simultaneous | core since v0.1 |
| Membrane (selective permeability) | AUTHORITY.md + the human boundary: nothing spends, sends, signs, or files without crossing a human | core since v0.1 |

Open biomimetic questions worth future versions: **caste differentiation**
(one Operator role vs specialized stewards — when to split), and
**symbiosis** (two instances trading services under each other's AUTHORITY —
the v1.0 network question).
