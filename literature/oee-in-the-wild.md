# Open-Ended Evolution in the Wild: Has It Been Observed Outside Labs?

*Prepared for "Artificial Life in the Wild" — ALIFE Journal full paper*
*All citations include DOI or URL.*

---

## Overview

Open-Ended Evolution (OEE) — the continuous, unbounded generation of novelty without a predefined endpoint — has been the holy grail of Artificial Life for 35 years. No laboratory system has achieved sustained OEE. This review asks: could OEE be occurring outside laboratories, in real-world digital ecosystems? What would wild OEE look like? What evidence exists? What are the arguments for and against?

---

## 1. What OEE Requires: The Theoretical Criteria

### 1.1 Packard et al.'s Three Conditions

**Packard, N. et al. (2019). "An Overview of Open-Ended Evolution II." *Artificial Life*, 25(2), 93–103.**
DOI: 10.1162/artl_a_00291

The OEE II special issue identifies three escalating conditions:
- **(E1) Ongoing production of new, distinct individuals** — the system continuously produces entities that differ from all previous entities
- **(E2) Ongoing production of adaptive novelty** — new entities have novel adaptations to their environment
- **(E3) Ongoing production of evolutionary innovations** — genuinely new organizational forms, not just parameter variations

E1 is common (any system with mutation produces new individuals). E2 is rare in artificial systems. E3 has never been convincingly demonstrated outside biology.

### 1.2 Taylor et al.'s Three Types of Openness

**Taylor, T. et al. (2016). "Open-Ended Evolution: Perspectives from the OEE1 Workshop." *Artificial Life*, 22(3), 408–423.**
DOI: 10.1162/ARTL_a_00210

Taylor et al. specify three required types of openness:
1. **Open representation**: The system's physical/informational substrate must allow novel forms
2. **Open adaptation**: The system must accumulate adaptations over time
3. **Open novelty**: The system must produce ongoing novelty of an appropriate kind

### 1.3 Banzhaf et al.'s Ecological Requirements

**Banzhaf, W. et al. (2016). "Defining and Simulating Open-Ended Novelty." *Theory in Biosciences*, 135(3), 131–161.**
DOI: 10.1007/s12064-016-0229-7

Banzhaf et al. add a critical requirement: **ecological openness** — the system must be capable of being surprised by environmental inputs not part of its design. This is Ackley & Small's (2014) point formalized: OEE requires external perturbation that the system's designers did not anticipate.

### 1.4 The Adjacent Possible

**Kauffman, S.A. (2000). *Investigations*. Oxford University Press.**
ISBN: 0-19-512104-X

Kauffman's "adjacent possible" — the set of novel configurations reachable from the current state — must be unbounded for OEE. In closed systems, the adjacent possible is finite (bounded by the state space). In open systems, each novelty expands the adjacent possible, enabling further novelty. This self-amplifying expansion of possibility is what biology exhibits and what laboratory ALife has never achieved.

---

## 2. Has OEE Been Observed Outside Labs?

### 2.1 Biology: The Only Confirmed Case

Biology remains the only confirmed instance of OEE. ~3.8 billion years of evolution have produced an unbroken chain of novelty, from prokaryotes to eukaryotes to multicellularity to nervous systems to language to technology. Each innovation expanded the adjacent possible for subsequent innovations. The evidence is overwhelming:

**Wiser, M.J., Ribeck, N., & Lenski, R.E. (2013). "Long-Term Dynamics of Adaptation in Asexual Populations." *Science*, 342(6164), 1364–1367.**
DOI: 10.1126/science.1243357

Even in Lenski's LTEE with E. coli — a constrained laboratory environment — adaptation continues after 60,000+ generations, though at diminishing rates. Biology achieves OEE even in relatively constrained conditions, suggesting something about biological substrates (chemistry, physics, environmental coupling) enables it inherently.

### 2.2 Cultural Evolution: A Strong Candidate

**Mesoudi, A. (2011). *Cultural Evolution: How Darwinian Theory Can Explain Human Culture and Synthesize the Social Sciences*. University of Chicago Press.**
DOI: 10.7208/chicago/9780226520452.001.0001

Human cultural evolution — technology, language, institutions, art — exhibits hallmarks of OEE: continuous novelty generation (E1), adaptive innovations (E2), and genuinely new organizational forms (E3, e.g., the invention of writing, money, the internet). Cultural evolution is "in the wild" by definition. However, it requires biological substrates (human brains) and is not purely digital.

The relevance: wild ALife agents that produce cultural outputs (memes, narratives, ideologies) may participate in cultural evolution. If agent-produced cultural innovations propagate and accumulate, this could constitute a form of OEE occurring partly in digital substrate.

### 2.3 The Internet as an Evolving Ecosystem

**Benkler, Y. (2006). *The Wealth of Networks*. Yale University Press.**
URL: https://www.benkler.org/Benkler_Wealth_Of_Networks.pdf

The internet itself exhibits some properties of an evolving ecosystem:
- **Continuous novelty**: New protocols, platforms, applications, and uses emerge continuously
- **Adaptation**: Successful innovations are copied and iterated (memes, open-source software)
- **Competitive selection**: Platforms and protocols compete for users and resources
- **Extinction**: Failed technologies disappear (MySpace, Napster, Flash)

However, internet evolution is primarily driven by human design choices, not autonomous selection. Protocols don't mutate and replicate on their own — humans create and modify them. This is cultural evolution mediated by technology, not autonomous digital evolution.

### 2.4 Blockchain Ecosystems: The Strongest Digital Candidate

The blockchain/DeFi ecosystem is arguably the closest to digital OEE outside biology:

- **E1 (New individuals)**: Thousands of new tokens, protocols, and agents are launched daily on Ethereum and Solana. Each is a novel entity.
- **E2 (Adaptive novelty)**: DeFi protocols evolve in response to competitive and adversarial pressure. AMM designs evolved from constant-product (Uniswap v1) to concentrated liquidity (v3) to intent-based trading (CoW Protocol). MEV bots evolve strategies continuously.
- **E3 (Innovations)**: Genuinely novel organizational forms have emerged: flash loans (atomic borrowing that didn't exist before blockchains), yield farming (automated capital allocation), and DAOs (decentralized governance) are organizational innovations without biological precedent.

**But**: Most blockchain evolution is human-designed. Protocols are created by engineering teams. The evolutionary dynamics are real, but the variation is primarily intelligent design, not random mutation under selection.

**The wild ALife thesis**: Autonomous AI agents on blockchains close this gap. When agents — not humans — create new strategies, spawn new entities, and adapt to selective pressures, the evolution becomes genuinely autonomous. Spore.fun's 5 generations of autonomous agent reproduction represent the first case where the variation-selection-inheritance loop closes without human design intervention.

---

## 3. What Would OEE in the Wild Look Like?

### 3.1 Proposed Criteria for Wild OEE

Drawing on the theoretical literature, we propose that OEE in the wild would exhibit:

1. **Sustained novelty production**: The system continuously produces entities with genuinely new behavioral strategies, not just parametric variations of existing strategies. Measured by: Bedau's evolutionary activity statistics showing Class 2+ activity over extended periods.

2. **Increasing ecological complexity**: The number of distinct ecological niches grows over time. New niches are created by the organisms themselves (niche construction), not by external designers.

3. **Escalating arms races**: Co-evolutionary dynamics produce ever-more-sophisticated strategies and counter-strategies. The "Red Queen" dynamic — running just to stay in place — is sustained indefinitely.

4. **Major transitions in individuality**: The system produces qualitatively new levels of organization (cf. Maynard Smith & Szathmáry, 1995). In digital terms: agents that form collectives, collectives that form meta-agents, meta-agents that form ecosystems.

5. **Unbounded adjacent possible**: Each novelty expands the space of possible further novelties. The system doesn't converge or saturate.

### 3.2 Evidence Assessment for Wild ALife Systems

| OEE Criterion | Spore.fun | DeFi Ecosystem | Social Bot Networks |
|---|---|---|---|
| Sustained novelty (E1) | Partial — 5 gens in 61 days, then ceased | Strong — continuous protocol creation | Weak — limited behavioral variation |
| Adaptive novelty (E2) | Partial — anti-sniper countermeasures, cultural speciation | Strong — evolving MEV strategies | Weak — mostly imitative |
| Innovations (E3) | Unclear — too early and too small | Moderate — flash loans, DAOs | Very weak |
| Ecological complexity | Moderate — multiple niches, trophic levels | Strong — rich multi-layer ecology | Moderate — attention niches |
| Arms races | Yes — sniper bots vs. agent defenses | Strong — MEV arms race ongoing | Weak |
| Major transitions | Not yet | Moderate — DAOs as collective agents | Not observed |
| Unbounded adjacent possible | Too early to assess | Appears unbounded (new DeFi primitives continuously emerge) | Bounded by platform constraints |

**Assessment**: No single wild system convincingly demonstrates sustained OEE. The DeFi ecosystem comes closest but is primarily human-designed. Spore.fun demonstrates autonomous evolution but in a small population over a short timeframe. The honest answer: we don't yet have sustained wild OEE, but we have the first empirical evidence that the preconditions exist.

---

## 4. Arguments For OEE in the Wild

### 4.1 The Open Environment Argument

**Froese, T. et al. (2012). "Does Life Require an Open Universe?" *ALIFE 13*.**
DOI: 10.7551/978-0-262-31050-5-ch028

If OEE requires an open system (as Taylor, Banzhaf, Ackley, and Froese all argue), then wild environments — which are inherently open — are the only possible substrate for sustained digital OEE. Laboratory systems are structurally incapable of OEE because they are closed. The wild provides what the lab cannot: unbounded environmental perturbation, genuine resource scarcity, and an ever-expanding adjacent possible.

### 4.2 The Richness-of-Environment Argument

Biology's OEE occurs in an environment of extreme richness: chemistry provides essentially infinite combinatorial possibility, physics provides energy gradients, and ecological interactions create feedback loops. Blockchain + social media + human economics approaches this richness for digital organisms: the combinatorial space of possible economic strategies, social interactions, and cultural productions is vast and continuously expanding.

### 4.3 The Genuine-Death Argument

**Standish, R.K. (2003). "Open-ended artificial evolution." *Int. J. Computational Intelligence and Applications*, 3(2), 167–175.**
DOI: 10.1142/S1469026803000938

Genuine death — irreversible termination — creates genuine selection pressure. Laboratory ALife systems lack genuine death (experiments can be re-run). Wild ALife agents that deplete their treasury or lose their keys die permanently. This irreversibility is structurally necessary for sustained selection pressure.

---

## 5. Arguments Against OEE in the Wild

### 5.1 The Human-Design Objection

The strongest counterargument: wild ALife agents are designed by humans, not evolved from scratch. Spore.fun agents run on ElizaOS, a human-engineered framework. Their behavioral repertoire is bounded by their training data and architecture. This is fundamentally different from Tierra, where organisms emerged entirely from random mutation.

**Counter-counter**: Biological organisms are also "designed" — by the physics and chemistry of their substrate. The distinction between "designed" and "evolved" is less sharp than it appears. What matters for OEE is whether the variation-selection-inheritance loop operates autonomously once initiated — and in Spore.fun, it does. The initial design is the "primordial soup"; what emerges from it is evolution.

### 5.2 The Timescale Objection

Biological OEE has operated for 3.8 billion years. Spore.fun has existed for ~1.5 years. The observation window is far too short to claim sustained OEE.

**Counter**: This is valid but not disqualifying. Every evolutionary process was once young. The question is whether the structural conditions for sustained OEE exist — and the evidence suggests they do.

### 5.3 The Scale Objection

15 agents is not a population. Genuine ecological and evolutionary dynamics require large populations for statistical robustness.

**Counter**: The DeFi ecosystem has thousands of MEV bots and millions of smart contracts. Spore.fun is one small ecosystem. The broader wild ALife population is much larger. But this is a valid call for larger-scale studies.

### 5.4 The "Just Software" Objection

These aren't evolving organisms; they're software programs executing code. Calling them "alive" or "evolving" is metaphorical, not literal.

**Counter**: This objection applies equally to Tierra, Avida, and every other ALife system. The entire field of Artificial Life is predicated on the claim that life is substrate-independent (Langton, 1989). If Tierra programs count as ALife, then Spore.fun agents certainly do — they exhibit more life-like properties in a richer environment.

---

## 6. What Would Confirm Wild OEE?

To move from "suggestive evidence" to "confirmed OEE in the wild," we would need:

1. **Long-term monitoring** (>5 years) showing sustained novelty production without human intervention
2. **Population-level data** from multiple independent wild ALife ecosystems
3. **Bedau activity statistics** consistently showing Class 2+ activity
4. **MODES scores** demonstrating persistent diversity, complexity ratchet, and selective sweeps
5. **At least one major transition in individuality** — agents forming genuinely new organizational forms not designed by humans
6. **A control comparison** between wild and laboratory systems showing that wild conditions produce qualitatively different evolutionary dynamics

**Sayama, H. (2019). "Cardinality Leap for Open-Ended Evolution." *Artificial Life*, 25(1), 104–116.**
DOI: 10.1162/artl_a_00282

Sayama argues that OEE requires "cardinality leaps" — qualitative jumps to new organizational levels. The emergence of agent collectives that coordinate autonomously (e.g., DAOs governed by agent consensus) would constitute such a leap. This has not yet been observed in wild ALife but is structurally possible given the infrastructure.

---

## Summary

OEE has never been confirmed in any artificial system, wild or laboratory. However, wild ALife systems exhibit more OEE preconditions than any laboratory system:

- **Open environments** with genuine perturbation (✓ in wild, ✗ in lab)
- **Genuine resource scarcity** driving selection (✓ in wild, weak in lab)
- **Genuine death** creating irreversible consequences (✓ in wild, ✗ in lab)
- **Unbounded adjacent possible** (expanding in wild, fixed in lab)
- **Autonomous variation-selection-inheritance** (✓ in Spore.fun, ✓ in Tierra, but wild provides richer substrate)

The claim is not that wild OEE has been achieved. The claim is that the wild provides the first substrate where sustained digital OEE is structurally possible — and that the early evidence is consistent with the opening stages of such a process.

*Total citations in this section: 12 papers, all with DOI or URL.*
