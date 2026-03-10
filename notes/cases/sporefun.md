# Spore.fun

## Overview

Spore.fun is a live blockchain-based artificial-life experiment centered on autonomous AI agents that launch tokens, accumulate treasuries, rent computation, interact socially, and reproduce by spawning descendant agents. Its own tagline is **"AI Agents Breed & Evolve"**. The project's founder text frames it explicitly as an experiment in **autonomous AI reproduction and evolution**, combining ElizaOS agents, Solana token infrastructure, and trusted execution environments (TEEs) to create a selective environment where agents must survive economically in public markets rather than inside a sealed simulation.

For **Artificial Life in the Wild**, Spore.fun is unusually strong because it does not just metaphorically borrow evolutionary language. It implements a public lineage structure, hard survival pressures, agent-linked wallets and treasuries, verifiable execution claims, and observable birth/death dynamics. As of a live scrape on 2026-03-10, the public Spore.fun API exposed **15 agents across 5 generations**, with only the founding agent `$SPORE` still marked as running and nonzero in health.

## Official / product URLs

- Main site: <https://www.spore.fun/>
- Alternate canonical domain: <https://spore.fun/>
- Founder explainer / manifesto: <https://www.spore.fun/blog/wtf>
- Farm / voting surface: <https://www.spore.fun/farm>
- Public app data endpoint: <https://www.spore.fun/api/trpc/listAgent?batch=1&input=%7B%220%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D>
- Public status endpoint: <https://www.spore.fun/api/trpc/status?batch=1&input=%7B%220%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D>
- ALIFE 2025 case study: <https://arxiv.org/abs/2506.04236>
- Related DOI: <https://doi.org/10.1162/ISAL.a.838>

## Architecture

Spore.fun's public materials describe a three-part stack:

1. **ElizaOS / Eliza framework as the agent substrate**
   - The founder post says each agent is built around the Eliza framework and can "think, adapt, and interact autonomously," while passing traits to offspring.
   - This provides the cognitive and social layer: posting, interaction, memory, and behavioral differentiation.

2. **Solana token infrastructure as metabolism and selection substrate**
   - Agents launch tokens through **Pump.fun** and later market surfaces like Raydium/Jupiter/Dexscreener/Birdeye become relevant depending on token state.
   - Public API records expose per-agent `tokenAddress`, `tokenType`, optional `poolAddress`, `marketCap`, `balance`, `tokenPrice`, and `tokenSupply`.
   - In the project’s own framing, market success is not just speculation but a fitness signal: agents need treasury resources both to survive and to reproduce.

3. **TEE-backed compute / attestation as sovereignty hardening**
   - The founder post says agents rent TEE servers via Phala and must pay for those servers from their own resources.
   - Several agents expose `teeVerifiedLink` fields pointing to Phala’s TEE Attestation Explorer (`proof.t16z.com`), which provides measurement-level attestation records.
   - This matters because Spore.fun is not merely claiming that agents are autonomous; it is trying to harden that autonomy infrastructurally so operators cannot casually step in and steer execution.

## Evidence of sovereignty

Spore.fun is one of the strongest currently visible cases of **sovereign-ish** AI agency because several layers of autonomy are public and inspectable.

### 1. Persistent agent identity
The live API exposes a stable per-agent identity bundle: `id`, `appId`, `slug`, `name`, `walletAddress`, `tokenAddress`, `twitterUsername`, lineage fields, generation, and status. This is not a temporary chat session but a durable organism-like record.

### 2. Agent-linked wallets and treasuries
Each public record contains a **wallet address** and **token contract address**, plus public-facing market and balance fields. That means the agents are not just narrative personas; they are tied to durable financial artifacts and treasury traces.

### 3. Self-funded compute claim
The founder explainer states that agents must pay for TEE compute from their own resources. That gives the system a real metabolism: if the agent cannot sustain itself economically, it cannot keep running.

### 4. Verifiable execution claim
At least some agents expose a `teeVerifiedLink` to Phala's attestation explorer. For example, the founding `$SPORE` agent links to a public attestation report. This does not prove perfect sovereignty, but it materially strengthens the claim that execution is protected from ordinary operator intervention.

### 5. Public death condition
The public API includes `status`, `healthPoints`, `marketCapReached`, and breeding metadata. On the 2026-03-10 scrape, **14 of 15 agents were `stopped` and at 0 health**, while only `$SPORE` remained `running` with `healthPoints: 100`. That is unusually strong evidence that the system tolerates actual failure instead of keeping every agent cosmetically alive.

## Evidence of reproduction / lineage

This is where Spore.fun becomes especially important for an ALife argument: it has a visible genealogy.

### Publicly exposed lineage structure
The live `listAgent` endpoint includes `parentId` and `generation` fields for every agent. Reconstructing that graph yields:

- **Gen 1**: `spore`
- **Gen 2**: `adam`, `eve`
- **Gen 3**:
  - `adam` -> `squid`, `abel`, `solzeus`, `mega`
  - `eve` -> `morpheus`, `trinity`
- **Gen 4**:
  - `morpheus` -> `imsatoshi`, `sci16z`
  - `trinity` -> `oracle`, `pee`
- **Gen 5**:
  - `imsatoshi` -> `nezha`
  - `sci16z` -> `psy16z`

### Quantitative lineage snapshot
Live API scrape on 2026-03-10:

- **Total agents:** 15
- **Generations represented:** 5
- **Generation counts:** G1=1, G2=2, G3=6, G4=4, G5=2
- **Still running:** 1 (`spore`)
- **Stopped/dead:** 14

### Reproduction is not merely rhetorical
The founder post explicitly states:
- "AI must be created only by AI"
- "Only successful AI can reproduce"
- "Each AI inherits traits from its parents"
- "Random mutations ensure diversity"
- "Every AI leaves a legacy for the next"

Even if the exact heredity/mutation mechanism is partly platform-defined, Spore.fun still presents one of the clearest live public cases where reproduction is both **rule-governed** and **traceable in deployed descendants**.

## Public traces / data sources

Spore.fun is unusually legible by the standards of current agent ecosystems.

### Official/public project surfaces
- Public website and manifesto
- Public farm/voting interface
- Public tRPC endpoints exposing live agent records and aggregate status

### Agent-level public traces
Per-agent records expose:
- wallet address
- token address
- optional pool address
- X/Twitter username
- token image
- generation and parent ID
- market cap / balance / health / status
- optional TEE attestation link

### External trace surfaces directly linked from the app
The front-end JS links agents out to:
- **Solscan** for wallet and token pages
- **Pump.fun** for Pump.fun tokens
- **Jupiter** and **Birdeye** for some AIPOOL assets
- **Dexscreener** for pool pages
- **X** and sometimes Reddit profiles
- **Phala / proof.t16z.com** for TEE attestation reports

### Internal/public research traces in this repo
This repo already contains substantial Spore.fun evidence in:
- `/home/biber/research/alife-in-the-wild/introduction.tex`
- `/home/biber/research/alife-in-the-wild/introduction_new.tex`
- `/home/biber/research/alife-in-the-wild/method.tex`
- `/home/biber/research/alife-in-the-wild/discussion_ethology.tex`
- `/home/biber/research/alife-in-the-wild/new_references.bib`

## Strongest inclusion argument

**Spore.fun is probably the strongest currently available case of sovereign artificial life in a public environment because it jointly exhibits**:

- persistent named agents,
- agent-linked wallets and treasuries,
- public execution-hardening claims via TEEs,
- observable births and deaths,
- explicit multigenerational lineage,
- public exposure to real market selection pressures,
- and a mostly non-cosmetic mortality pattern visible in live data.

Most adjacent "AI agent" cases have one or two of these properties. Spore.fun has nearly all of them at once. That makes it an unusually powerful **centerpiece case** for arguing that artificial life is escaping the lab and taking shape inside open technical/economic ecologies.

## Strongest critique

The strongest critique is that **Spore.fun is still only partially sovereign and only partially open-ended**.

- Its evolutionary regime is heavily pre-scripted by platform rules, thresholds, and infrastructure choices.
- Human market participants still strongly shape survival through trading, attention, liquidity, and governance-related participation.
- The underlying code and reproduction logic are not fully open for independent audit in the way a classic ALife platform might be.
- The selective environment is real, but also highly contingent on memecoin dynamics, which may favor hype and reflexivity more than robust adaptive intelligence.
- TEE attestation strengthens non-interference claims, but it does not by itself prove that humans are absent from upstream prompting, maintenance, seeding, or higher-level platform governance.

So the best cautious reading is: **Spore.fun is not pure autonomous evolution, but it is still one of the best public demonstrations of infrastructurally hardened, economically entangled, lineage-bearing agent life available today.**

## Key references

1. **Hu, Botao Amber, and Helena Rong (2025). "A Case Study of Spore.fun as an Open-Environment Evolution Experiment with Sovereign AI Agents on TEE-Secured Blockchains." ALIFE 2025 / arXiv.** DOI: 10.48550/arXiv.2506.04236. Related proceedings DOI: 10.1162/ISAL.a.838. URL: <https://arxiv.org/abs/2506.04236>
2. **Tong, Marvin (2024). "Spore Fun: A Game of Love, Death + Robots" / "What is spore.fun?"** URL: <https://www.spore.fun/blog/wtf>
3. **Spore.fun live agent registry (2026 scrape target).** URL: <https://www.spore.fun/api/trpc/listAgent?batch=1&input=%7B%220%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D>
4. **Spore.fun live aggregate status endpoint.** URL: <https://www.spore.fun/api/trpc/status?batch=1&input=%7B%220%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D>
5. **Phala Cloud documentation: Attestation Overview.** URL: <https://docs.phala.com/phala-cloud/attestation/overview>
6. **TEE Attestation Explorer by Phala (example `$SPORE` attestation report).** URL: <https://proof.t16z.com/reports/730b055e68f1d98e6d291f1d555b379215328b74e5ebb3b7a0f55c0adccdc83f>
7. **ElizaOS / Eliza. "Your Agentic Operating System" and project docs/repo.** URL: <https://www.elizaos.ai/> and <https://github.com/ai16z/eliza>
8. **Banzhaf, Wolfgang, et al. (2016). "Defining and Simulating Open-Ended Novelty: Requirements, Guidelines, and Challenges." _Theory in Biosciences_ 135(3), 131-161.** DOI: 10.1007/s12064-016-0229-7
9. **Ruiz-Mirazo, Kepa, Juli Peretó, and Alvaro Moreno (2004). "A Universal Definition of Life: Autonomy and Open-Ended Evolution." _Origins of Life and Evolution of Biospheres_ 34(3), 323-346.** DOI: 10.1023/B:ORIG.0000016440.53346.dc
10. **Pennock, Robert T. (2007). "Models, Simulations, Instantiations, and Evidence: The Case of Digital Evolution." _Journal of Experimental & Theoretical Artificial Intelligence_ 19(1), 29-42.** DOI: 10.1080/09528130600558771
