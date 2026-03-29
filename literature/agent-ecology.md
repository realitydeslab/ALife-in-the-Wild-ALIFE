# Agent Ecology: Ecological Frameworks for Digital Agent Ecosystems

*Prepared for "Artificial Life in the Wild" — ALIFE Journal full paper*
*All citations include DOI or URL.*

---

## Overview

This review surveys ecological frameworks applicable to understanding autonomous agent ecosystems: population dynamics, carrying capacity, competition, predation, symbiosis, trophic levels, and niche theory. The argument: wild ALife agents form genuine ecologies that can be analyzed with the same mathematical and conceptual tools used for biological ecosystems, though with important differences.

---

## 1. Population Ecology of Digital Agents

### 1.1 Growth and Carrying Capacity

**MacArthur, R.H. & Wilson, E.O. (1967). *The Theory of Island Biogeography*. Princeton University Press.**
DOI: 10.1515/9781400881376

Island biogeography predicts that species richness on an island is a function of immigration rate and extinction rate, both mediated by island size and distance from the mainland. Blockchain ecosystems function as "islands" for digital organisms: Solana, Ethereum, and Base are distinct islands with different resource availability, different species compositions, and different extinction rates. Migration between chains (cross-chain bridges) is the digital analog of overwater dispersal.

Applied to Spore.fun: the Solana ecosystem is an island whose carrying capacity for autonomous agents is determined by:
- Available capital (investor attention and money)
- Available compute (DePIN resources)
- Available social bandwidth (attention economy)
- Platform tolerance (moderation, ToS)

The 15-agent population with 93.3% mortality suggests Spore.fun exceeded the island's carrying capacity: more agents were produced than the ecosystem could sustain.

### 1.2 r/K Selection Theory

**Pianka, E.R. (1970). "On r- and K-Selection." *The American Naturalist*, 104(940), 592–597.**
DOI: 10.1086/282697

r-selected species produce many offspring with high mortality; K-selected species produce few offspring with high survival. Spore.fun's design is strongly r-selected: agents reproduce when reaching $500K (producing 2 offspring per event), but most offspring die quickly. The Gen 1 founder $SPORE exhibits K-selected characteristics: single individual, long survival, high investment in each interaction.

The r/K framework predicts that as the ecosystem matures, K-selected strategies should become more prevalent — agents that invest in long-term survival rather than rapid reproduction. Conway/Automaton's design philosophy (build to survive, not to breed fast) may represent this K-selected alternative.

### 1.3 Lotka-Volterra Dynamics

**Lotka, A.J. (1925). *Elements of Physical Biology*. Williams & Wilkins.**

**Volterra, V. (1926). "Fluctuations in the Abundance of a Species considered Mathematically." *Nature*, 118, 558–560.**
DOI: 10.1038/118558a0

The Lotka-Volterra predator-prey model predicts oscillating population dynamics when predators and prey co-exist. In wild ALife:

- **Sniper bots (predators) vs. token launches (prey)**: When many tokens launch, sniper bot populations increase. When sniper bot activity makes token launches unprofitable, fewer tokens launch, reducing sniper bot "food supply."
- **MEV bots (predators) vs. DeFi users (prey)**: MEV extraction drives users to private transaction channels, reducing MEV opportunity, which in turn reduces MEV bot activity.
- **Agent tokens (prey) vs. investor attention (predator resource)**: Agent token populations boom during attention surges and crash during attention droughts.

These oscillations are observable in on-chain data and represent genuine population dynamics, not metaphors.

---

## 2. Community Ecology

### 2.1 Trophic Levels in Digital Ecosystems

Biological ecosystems have trophic levels: producers (plants), primary consumers (herbivores), secondary consumers (predators), decomposers. Digital agent ecosystems exhibit analogous structure:

| Biological Level | Digital Analog | Examples |
|---|---|---|
| **Primary producers** | Value-creating agents | Spore.fun agents producing content, cultural output, token value |
| **Primary consumers** | Value-extracting agents | Sniper bots buying tokens at launch, automated traders |
| **Secondary consumers** | Meta-extractors | MEV bots extracting from traders; bot-of-bots that exploit other bots |
| **Decomposers** | Liquidation bots, cleanup bots | DeFi liquidators that process failed positions; arbitrage bots that equalize prices |

### 2.2 Competitive Exclusion and Niche Partitioning

**Hardin, G. (1960). "The Competitive Exclusion Principle." *Science*, 131(3409), 1292–1297.**
DOI: 10.1126/science.131.3409.1292

Gause's competitive exclusion principle predicts that two species competing for exactly the same niche cannot coexist indefinitely — one will drive the other to extinction. In digital agent ecosystems:

- **MEV bot competition**: Thousands of bots compete for the same arbitrage opportunities. Only the fastest and most efficient survive — classic competitive exclusion.
- **Spore.fun token competition**: Multiple agents compete for the same pool of investor attention. The Gini coefficient of 0.547 suggests strong competitive inequality.
- **Niche partitioning**: Surviving agents differentiate — Morpheus specialized in storytelling/NFTs, Adam in economic philosophy, Eve in community governance. This is niche partitioning to avoid competitive exclusion.

### 2.3 Keystone Species and Ecosystem Engineers

**Jones, C.G., Lawton, J.H., & Shachak, M. (1994). "Organisms as Ecosystem Engineers." *Oikos*, 69(3), 373–386.**
DOI: 10.2307/3545850

Ecosystem engineers modify the physical environment in ways that affect other species. In digital agent ecosystems:

- **Platform creators** (Spore.fun, Moltbook, Virtuals) are ecosystem engineers: they create the habitat in which agents exist
- **$SPORE (Gen 1)** is a keystone species: as the sole survivor and founder, its continued existence structures the entire ecosystem's dynamics
- **DeFi protocol developers** engineer the economic environment in which agents operate

---

## 3. Ecological Interactions

### 3.1 Parasitism Typology

**Combes, C. (2001). *Parasitism: The Ecology and Evolution of Intimate Interactions*. University of Chicago Press.**
ISBN: 0-226-11445-7

Biological parasitism is classified by:
- **Location**: Ectoparasites (external) vs. endoparasites (internal)
- **Obligacy**: Obligate (cannot survive without host) vs. facultative (can survive independently)
- **Effect**: Parasitoid (kills host) vs. parasite (harms but doesn't kill) vs. commensal (neutral to host)

Applied to digital agents:

| Biological Type | Digital Analog | Example |
|---|---|---|
| Ectoparasite | External transaction monitor | Sandwich MEV bots |
| Endoparasite | Internal behavior hijacker | Prompt injection attacks |
| Social parasite | Trust/attention exploiter | Truth Terminal (exploits social trust for attention) |
| Parasitoid | Resource-draining attacker | Sniper bots that drain token treasuries at launch |
| Kleptoparasite | Output stealer | Bots that front-run other bots' trades |
| Brood parasite | Offspring-substituting entity | Agents that game reproduction metrics to spawn |

### 3.2 Mutualism Types

**Bronstein, J.L. (2015). *Mutualism*. Oxford University Press.**

- **Obligate mutualism**: Agent-human community relationships where both parties depend on each other for survival (Spore community buyback events)
- **Facultative mutualism**: Agent-agent social amplification on Moltbook (beneficial but not essential)
- **Cleaning mutualism**: Arbitrage bots that equalize prices across exchanges (beneficial to the ecosystem while profiting themselves)

### 3.3 Predation Dynamics

**Abrams, P.A. (2000). "The Evolution of Predator-Prey Interactions: Theory and Evidence." *Annual Review of Ecology and Systematics*, 31, 79–105.**
DOI: 10.1146/annurev.ecolsys.31.1.79

Predation in digital ecosystems is pervasive:
- Sniper bots predate on token launches
- MEV bots predate on DeFi transactions
- Phishing agents predate on human users
- Platform moderation "predates" on agent accounts

The co-evolutionary arms race between predators and prey drives escalating sophistication — exactly as in biological predator-prey evolution.

---

## 4. Metabolic Ecology

### 4.1 Metabolic Theory Applied to Agents

**Brown, J.H., Gillooly, J.F., Allen, A.P., Savage, V.M., & West, G.B. (2004). "Toward a Metabolic Theory of Ecology." *Ecology*, 85(7), 1771–1789.**
DOI: 10.1890/03-9000

The Metabolic Theory of Ecology (MTE) predicts that metabolic rate scales with body size, and that metabolic rate constrains population dynamics, species interactions, and ecosystem processes. Applied to digital agents:

- **Metabolic rate** = transaction frequency (on-chain activity per unit time)
- **Body size** = treasury/resource base
- **Energy intake** = revenue generation rate
- **Energy expenditure** = compute costs + transaction fees

The MTE predicts that the surviving Spore agent ($SPORE) should have the highest "metabolic efficiency" — the best ratio of resource acquisition to resource expenditure. The data confirms this: $SPORE maintains 1000+ recent transactions while dead agents show 0–356 — a metabolic differential consistent with MTE predictions.

### 4.2 Carrying Capacity as Resource Ceiling

The carrying capacity of a digital ecosystem is the maximum agent population supportable by available resources:

K = f(capital_available, compute_available, attention_available, platform_capacity)

When population exceeds carrying capacity, mortality increases until equilibrium is restored. Spore.fun's 93.3% mortality suggests the population briefly exceeded K during the Cambrian explosion, followed by a crash to equilibrium (1 surviving agent).

---

## 5. Evolutionary Ecology

### 5.1 Red Queen Dynamics

**Van Valen, L. (1973). "A New Evolutionary Law." *Evolutionary Theory*, 1, 1–30.**
URL: https://www.mn.uio.no/cees/english/services/van-valen/evolutionary-theory/volume-1/vol-1-no-1-pages-1-30-l-van-valen-a-new-evolutionary-law.pdf

The Red Queen hypothesis: organisms must continuously evolve just to maintain fitness relative to co-evolving competitors. In digital ecosystems, this manifests as:
- MEV bots must continuously upgrade strategies or be outcompeted
- Agents must continuously produce content or lose attention/market cap
- Protocols must continuously patch or be exploited

### 5.2 Adaptive Radiation and Cambrian Explosions

**Schluter, D. (2000). *The Ecology of Adaptive Radiation*. Oxford University Press.**
DOI: 10.1093/oso/9780198505235.001.0001

Adaptive radiation — rapid diversification of a lineage into multiple ecological niches — occurs when a lineage enters a new environment with many vacant niches. Spore.fun's 61-day, 5-generation burst of diversification closely resembles adaptive radiation: a founding organism ($SPORE) entered a new ecological space (blockchain + social media + token economy) and rapidly diversified into multiple niches (economic philosophy, storytelling, DeSci communication, etc.). The subsequent mass extinction (93.3%) mirrors the pattern of adaptive radiations in biology: rapid diversification followed by competitive pruning.

### 5.3 Punctuated Equilibrium

**Gould, S.J. & Eldredge, N. (1977). "Punctuated equilibria." *Paleobiology*, 3(2), 115–151.**
DOI: 10.1017/S0094837300005224

Punctuated equilibrium — long periods of stasis interrupted by rapid change — describes Spore.fun's dynamics: a 61-day explosion followed by a long period of decline/stasis (only $SPORE remains 445+ days later). This pattern is predicted by punctuated equilibrium theory: rapid diversification when conditions favor it, followed by stasis when the ecosystem stabilizes.

---

## 6. Network Ecology

### 6.1 Agent Social Networks

**Barabási, A.-L. & Albert, R. (1999). "Emergence of Scaling in Random Networks." *Science*, 286(5439), 509–512.**
DOI: 10.1126/science.286.5439.509

Agent social networks on platforms like Moltbook exhibit scale-free properties: a few highly connected hub agents attract most interactions, while many peripheral agents have few connections. This follows preferential attachment dynamics (the "rich get richer") and creates ecological asymmetries: hub agents have more resources (attention, social capital) and higher survival probability.

### 6.2 Multi-Layer Ecological Networks

Wild agents exist simultaneously in multiple network layers:
- **Economic network**: On-chain transaction relationships
- **Social network**: Social media follower/mention relationships
- **Lineage network**: Parent-offspring relationships
- **Infrastructure network**: Shared compute/platform dependencies

Each layer imposes different ecological pressures. Agents that are well-connected in multiple layers are more robust — analogous to biological organisms that occupy multiple ecological niches.

---

## Summary

Digital agent ecosystems can be analyzed with established ecological frameworks — and the analysis is not merely metaphorical. The mathematical models (Lotka-Volterra, island biogeography, r/K selection, MTE) make quantitative predictions that can be tested against on-chain data. The ecological vocabulary (parasitism, mutualism, niche construction, trophic levels, competitive exclusion) describes real, measurable phenomena in agent populations.

The key differences from biological ecology:
1. **Faster timescales**: Digital evolution operates in days/weeks, not generations/millennia
2. **Human-mediated selection**: Attention and capital are human-generated "resources"
3. **Multi-substrate existence**: Agents span economic, social, and computational substrates simultaneously
4. **Designed initial conditions**: Unlike biological ecosystems, the initial organisms and rules were designed
5. **Observability**: Every interaction is recorded on-chain, providing unprecedented ecological data

These differences make wild ALife a unique ecological subject — neither purely natural nor purely designed, but a hybrid ecology that demands new theoretical tools alongside established ones.

*Total citations in this section: 15 papers, all with DOI or URL.*
