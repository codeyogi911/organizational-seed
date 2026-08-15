# Biomimicry — the seed's design vocabulary

The word for nature-inspired design is **biomimicry** (engineering:
*biomimetics*). The seed has used it implicitly since birth; this page makes
it a deliberate design tool: when a new organizational problem appears, ask
*what does biology do about this?* before inventing.

| Biological mechanism | Seed mechanism | Status |
|---|---|---|
| Conserved genome vs somatic tissue | conserved files (branch + reviewed diff + Decision) vs free files (ordinary work) | core since v0.1 |
| Directed evolution / selection pressure | Founder Judgment before a change reaches the conserved core; lessons feed Decisions | core since v0.1 |
| Immune memory | `lessons/` — the org remembers every infection, tagged by process | core since v0.1 |
| Immune tolerance (don't attack self) | probation: new roles act under per-mutation review until trusted | v0.2 |
| **Immune surveillance** | **a validation tool — continuous self-inspection for malformed cells** (dead links, kind violations, boot-path budget, overdue open gaps) | v0.3 |
| Self/non-self recognition | kind definitions (`_kind.md`) validated mechanically | v0.3 |
| **Sensing what is absent** | **`records/gaps/` — the only Kind that records what the organization *needed and did not have*.** Every other check finds something wrongly present; a missing rule has no file to inspect | **v0.4** |
| Apoptosis (programmed cell death) | retirement as a move: a superseded file leaves the live path once its unique knowledge has a verified home; Git keeps the bytes | v0.4 |
| Homeostasis | deadman expected-report checks; drift checks with "growth is the flag, not existence" | v0.2 |
| Metabolic cost control | the boot-path line budget: context every session pays for is capped, and the cap is never raised to fit new prose | v0.4 |
| Scar tissue (and its pathology) | the right-size-scar-tissue rule: a lesson's standing weight must track its evidence; closed one-offs decay | learned live |
| Horizontal gene transfer | folding proven ideas in from neighbouring projects, with attribution | practiced (v0.3 owes CODEOWNERS-as-gate to Agentic Enterprise) |
| Redundancy / degeneracy | deliberate audit-vs-housekeep overlap: two organs, same function, never simultaneous | core since v0.1 |
| Membrane (selective permeability) | AUTHORITY.md + the human boundary: nothing spends, sends, signs, or files without crossing a human | core since v0.1 |

## Where the metaphor was wrong

Biomimicry is a generator of hypotheses, not a justification. Two v0.2
mechanisms were reasoned into existence largely because they had good
biological analogues, and live operation removed both:

- **Quorum / territorial signalling → session leases.** Advisory scent-marks
  in `work/_active/`. The analogy was sound and the mechanism was still
  redundant: Git already serialises repository writes, mechanically, with
  merge conflicts and non-fast-forward rejection
  ([ADR 0003](adr/0003-git-owns-repository-concurrency.md)).
- **Apoptosis → stale-lease self-termination.** A superseded session was to
  recycle its own lease. It went with the leases; the idea survives in a
  better-earned form as *retirement is a move*, above.

Keep the discipline of asking *what does biology do about this?* — and keep
asking, afterwards, whether the mechanism is doing work the substrate was
already doing for free.

Open biomimetic questions worth future versions: **senescence** (when does a
process retire on purpose, rather than because someone noticed?),
**caste differentiation** (one Operator role vs specialized stewards — when to
split), and **symbiosis** (two instances trading services under each other's
AUTHORITY — the network question).
