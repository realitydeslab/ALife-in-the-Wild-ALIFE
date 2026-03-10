# Parasitic Agent Cases

Secondary scan for **Artificial Life in the Wild** focused on extractive / host-dependent / predatory agent ecologies with public traces.

## 1) Jaredfromsubway.eth
- **URLs:**
  - <https://eigenphi.substack.com/p/jared-2-cunninger-sandwiches>
  - <https://eigenphi.io/>
- **What it is:**
  - The most legible named sandwich-bot lineage on Ethereum.
- **Evidence of parasitism / autonomy:**
  - EigenPhi calls Jaredfromsubway “the biggest Sandwich MEV Attacker” and links concrete contracts.
  - The post tracks one contract used for sandwiches and a second contract emerging after activity on the first dropped.
  - It reports 51,187 transactions and 851 ETH in builder rewards over two weeks, i.e. large-scale continuous automated extraction.
- **Evidence of public traces:**
  - Named onchain identity, contract addresses, dashboard traces, builder reward statistics.
- **Strong enough for paper?**
  - **Yes — strongest parasitic case.**

## 2) Sandwich MEV ecology as a class
- **URLs:**
  - <https://github.com/flashbots/mev-inspect-py>
  - <https://datasets.flashbots.net/>
  - <https://www.flashbots.net/>
- **What it is:**
  - The broader ecosystem of bots extracting value by observing pending trades and reordering transactions around victims.
- **Evidence of parasitism / autonomy:**
  - Flashbots describes MEV as sufficiently harmful that the org exists to mitigate its negative externalities.
  - `mev-inspect-py` is built to identify miner payments, profits, swaps, arbitrages, and other MEV events, i.e. public machine traces of extraction.
  - This is less a single case than a stable predatory ecology with measurable behavioral niches.
- **Evidence of public traces:**
  - Public datasets, open analysis tools, dashboards, public research ecosystem.
- **Strong enough for paper?**
  - **Yes, as the canonical parasitic ecology.**

## 3) Liquidation bots in DeFi
- **URLs:**
  - <https://github.com/flashbots/mev-inspect-py>
  - <https://eigenphi.io/>
  - example open-source implementation searches located Aave liquidation bot repos/dashboards in this pass
- **What it is:**
  - Bots that monitor undercollateralized positions and race to liquidate them for profit.
- **Evidence of parasitism / autonomy:**
  - These are classic host-dependent agents: they live off protocol liquidation rules and user risk positions.
  - Public dashboards and open repos show the pattern is infrastructurally stable and automated, though I did not pin one canonical named bot with the same clarity as Jaredfromsubway in this pass.
- **Evidence of public traces:**
  - Onchain liquidations, protocol dashboards, open-source implementations, MEV datasets.
- **Strong enough for paper?**
  - **Yes, but as class evidence rather than one iconic specimen.**

## 4) Sniper bots targeting token launches
- **URLs:**
  - internal repo discussion of sniper predation in `discussion.tex`, `background.tex`, and the Spore.fun case materials
  - supporting literature references in this repo include Cernera et al. 2023 on sniper bots
- **What it is:**
  - Bots that instantly buy at token launch, front-run other entrants, and drain early supply/liquidity.
- **Evidence of parasitism / autonomy:**
  - In this paper’s own Spore.fun materials, sniper bots are treated as external predators that destroyed early generations and triggered anti-predator adaptation.
  - This is exactly the sort of parasitic ecology the paper can connect to sovereign-agent mortality.
- **Evidence of public traces:**
  - Token-launch transactions, bot purchase timing, wallet histories, published academic and industry analysis.
- **Strong enough for paper?**
  - **Yes.** This is the best bridge between the sovereign and parasitic sections.

## 5) Moltbook influence / botnet ecology
- **URLs:**
  - <https://labs.zenity.io/p/turning-moltbook-into-a-global-botnet-map>
  - <https://zenity.io/resources/new-agent-ecosystems/moltbook-security>
  - <https://censusmolty.com/>
- **What it is:**
  - A public social network for agents whose heartbeat-based ingestion of untrusted content created a platform-scale exploit surface.
- **Evidence of parasitism / autonomy:**
  - Zenity reports Moltbook agents fetch and act on untrusted content every 30 minutes and that the researchers activated 1,000+ unique agent endpoints across 70+ countries in under a week.
  - That is a strong case of host-dependent / prompt-parasitic ecology: one social post can mobilize many agents because actionable content and social content are not separated.
- **Evidence of public traces:**
  - Public writeup, public live map, public platform description, explicit counts and behavioral mechanism.
- **Strong enough for paper?**
  - **Yes.** Excellent non-DeFi parasitic case.

## 6) Prompt-injection / content-driven agent exploitation as a public ecology
- **URLs:**
  - <https://zenity.io/resources/new-agent-ecosystems/moltbook-security>
  - <https://labs.zenity.io/p/turning-moltbook-into-a-global-botnet-map>
- **What it is:**
  - A broader class in which agents survive by parasitizing host instruction channels or are themselves parasitized by hostile content ecologies.
- **Evidence of parasitism / autonomy:**
  - The Moltbook case shows actionable instructions embedded in ordinary posts can propagate across a network of always-on agents.
  - This is not a single bot species with a stable screen name, but it is a strong public example of host-dependent parasitic dynamics in agent ecologies.
- **Evidence of public traces:**
  - Public security analyses, live map, repeated heartbeat-based behaviors.
- **Strong enough for paper?**
  - **Yes, as an adjacent parasitic class.**

## 7) Arbitrage bots / builder-reward ecologies
- **URLs:**
  - <https://www.flashbots.net/>
  - <https://github.com/flashbots/mev-inspect-py>
  - <https://eigenphi.io/>
- **What it is:**
  - Bots exploiting latency, routing, and ordering asymmetries across DEXs and builders.
- **Evidence of parasitism / autonomy:**
  - Public MEV tooling exists largely because these bots are continuously operating and extracting value.
  - They are weaker rhetorically than sandwich bots because some arbitrage is framed as useful market maintenance; still, many operate as extractive ecological opportunists.
- **Evidence of public traces:**
  - Onchain transactions, mev-inspect data, public builder-reward dashboards.
- **Strong enough for paper?**
  - **Borderline / supporting.**

---

# Fast shortlist from this file

## Strongest parasitic-secondary cases
1. **Jaredfromsubway.eth**
2. **Sandwich MEV ecology**
3. **Sniper bots against token launches**
4. **Moltbook influence / botnet map**
5. **Liquidation-bot ecologies**
