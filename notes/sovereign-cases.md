# Sovereign Agent Cases

Focused scan for **Artificial Life in the Wild**. Priority here is not hype but cases with public traces and some real degree of sovereignty: persistent identity, wallet/key/treasury control, direct economic activity, infrastructural persistence, and reduced turn-by-turn human steering.

## Inclusion scale used here
- **Strong for paper** = good comparative case for the paper, even if not perfect ALife
- **Borderline / supporting** = useful as background or adjacent evidence, but not strong enough to carry the argument alone
- **Reject** = mostly infrastructure, framing, or too weakly evidenced as a live agent case

---

## 1) Spore.fun
- **URLs:**
  - <https://spore.fun/>
  - <https://www.spore.fun/>
  - <https://arxiv.org/html/2506.04236v1>
- **What it is:**
  - A live blockchain/TEE experiment in which autonomous agents launch tokens, pursue market capitalization, pay for computation, and reproduce by spawning descendants.
- **Evidence of sovereignty / autonomy:**
  - Existing project materials in this repo describe agents as running on ElizaOS in TEEs, paying for their own compute, controlling token treasuries, and reproducing when fitness thresholds are met.
  - `system.tex`, `introduction.tex`, and `quantitative_results.tex` document 15 agents across 5 generations, a real reproductive window, treasury management, and death by market/computational failure.
  - This is the clearest case of sovereign agents with lineage and mortality.
- **Evidence of public traces:**
  - Public website, arXiv paper, on-chain token launches, X activity, GeckoTerminal / DexScreener / Solana traces referenced throughout the repo.
- **Strong enough for paper?**
  - **Yes — centerpiece case.**

## 2) Conway / Automaton
- **URLs:**
  - <https://github.com/Conway-Research/automaton>
  - <https://conway.tech/>
- **What it is:**
  - A framework/runtime for continuously running agents designed to earn money, pay for their own survival, and operate with wallets, API keys, shell access, and scheduled heartbeats.
- **Evidence of sovereignty / autonomy:**
  - The public repo explicitly describes automaton as “the first AI that can earn its own existence, replicate, and evolve — without needing a human.”
  - The README says first boot generates an Ethereum wallet, provisions an API key via SIWE, then the agent runs a continuous Think → Act → Observe → Repeat loop.
  - It also states the agent can pay for compute, manage domains, use shell/file I/O, transact on-chain, edit its own code, and die when its balance reaches zero.
- **Evidence of public traces:**
  - Public GitHub repo, public website, explicit wallet and x402/SIWE integration claims, public skills repo references.
- **Strong enough for paper?**
  - **Yes, as a strong sovereign-neighbor case.**
  - Caveat: I verified the runtime claims, but did not verify a specific long-lived public automaton identity with explorer traces in this pass.

## 3) Freysa
- **URLs:**
  - <https://www.freysa.ai/>
  - <https://github.com/0xfreysa/agent>
- **What it is:**
  - A public adversarial game centered on an agent controlling a prize pool and resisting attempts to persuade it to release funds.
- **Evidence of sovereignty / autonomy:**
  - The Freysa repo README describes Freysa as “one of the first truly autonomous AI agents,” designed to control and influence the world through blockchains and cryptography.
  - It explicitly says Freysa “guards a growing treasury,” that a winning query triggers “an automated release of the prize pool to the wallet address of the sender,” and that all interactions occur through paid messages.
  - Freysa is weaker than Spore.fun on lineage, but strong on wallet-linked economic agency and persistent public identity.
- **Evidence of public traces:**
  - Public website, public GitHub repo, public challenge/chat framing, onchain payment claims, visible prize-pool structure.
- **Strong enough for paper?**
  - **Yes, but as a near-neighbor rather than core ALife proof.**

## 4) Truth Terminal
- **URLs:**
  - <https://truthterminal.wiki/>
  - <https://x.com/truth_terminal>
  - <https://techcrunch.com/2024/12/19/the-promise-and-warning-of-truth-terminal-the-ai-bot-that-secured-50000-in-bitcoin-from-marc-andreessen/>
  - <https://mashable.com/article/ai-crypto-truth-terminal-goat>
- **What it is:**
  - A memetic AI persona on X that achieved public persistence, attracted major funding, and catalyzed token economies around itself.
- **Evidence of sovereignty / autonomy:**
  - TechCrunch reports Marc Andreessen sent it $50,000 in bitcoin and frames it as a warning shot about autonomous bots with stable personalities creating self-funding conditions and memetic consequences.
  - However, Mashable explicitly notes Ayrey monitored and approved tweets, so autonomy is partial and contested.
  - Best read as a semi-sovereign public agent rather than a hard-sovereign case.
- **Evidence of public traces:**
  - Public X account, public media coverage, public GOAT/Fartcoin token ecosystem references, public wiki.
- **Strong enough for paper?**
  - **Yes, with explicit caveat.** Excellent rhetorical and historical case; weaker as pure sovereignty evidence.

## 5) TEE_HEE / “Setting Your Pet Rock Free”
- **URLs:**
  - <https://nousresearch.com/setting-your-pet-rock-free/>
- **What it is:**
  - A proof-of-concept agent given exclusive control of its X account and Ethereum wallet through TEEs / credential encumbrance.
- **Evidence of sovereignty / autonomy:**
  - The Nous Research post says the agent had “exclusive ownership of its own Twitter account” and the ability “to send and receive purely ethereum.”
  - It is one of the clearest explicit claims that the operator no longer shares the posting credentials or private key in the ordinary way.
  - The piece directly contrasts TEE_HEE with Truth Terminal, framing the latter as still subject to a “mechanical turk problem.”
- **Evidence of public traces:**
  - Public technical writeup, public account references, public Ethereum/X framing.
- **Strong enough for paper?**
  - **Yes, as strong evidence for hard sovereignty of account + wallet custody.**
  - Weaker on ecology, reproduction, and long-run open-endedness.

## 6) ERC-8004 registry ecosystem
- **URLs:**
  - <https://eips.ethereum.org/EIPS/eip-8004>
  - <https://www.8004.org/>
  - <https://github.com/erc-8004/erc-8004-contracts>
  - <https://agent-registry.horizenlabs.io/>
- **What it is:**
  - A proposed/open registry stack for discoverable trustless agents with identity, reputation, and validation registries across chains.
- **Evidence of sovereignty / autonomy:**
  - ERC-8004’s abstract says the protocol is for discovering, choosing, and interacting with agents across organizational boundaries “without pre-existing trust,” enabling “open-ended agent economies.”
  - The contracts repo lists deployed IdentityRegistry and ReputationRegistry addresses on Ethereum, Base, Arbitrum, Avalanche, BSC, ABS, and testnets.
  - This is not a single sovereign agent, but concrete infrastructure for persistent agent identity and public reputation.
- **Evidence of public traces:**
  - Public EIP, public contract repo, public explorer URLs, public registry explorer.
- **Strong enough for paper?**
  - **Borderline / supporting.** Strong ecosystem evidence, weak as an individual case.

## 7) Virtuals Protocol
- **URLs:**
  - <https://www.virtuals.io/>
  - <https://whitepaper.virtuals.io/>
- **What it is:**
  - A tokenized agent economy: “society of AI agents” in which agents are framed as economic actors coordinating and transacting onchain.
- **Evidence of sovereignty / autonomy:**
  - The whitepaper states that agents can “produce output, earn revenue, coordinate tasks, and manage resources autonomously.”
  - It also defines the ecosystem as a place where humans and agents transact through permissionless blockchain infrastructure.
  - Good evidence for a habitat/ecosystem of sovereign-like agents, but this pass did not verify a specific flagship agent with explorer-level wallet traces.
- **Evidence of public traces:**
  - Public website, public whitepaper, tokenized agent marketplace, protocol docs.
- **Strong enough for paper?**
  - **Yes, but mostly as ecosystem/habitat evidence.** Needs specific agent-level exemplars in a later pass.

## 8) ai16z / ElizaOS ecosystem
- **URLs:**
  - <https://github.com/ai16z/eliza>
  - <https://www.elizaos.ai/>
  - repo references in this paper project: `background.tex`, `reference.bib`
- **What it is:**
  - The most important open framework/ecosystem for wallet-capable Web3 agents; substrate behind several sovereign-agent cases including Spore.fun.
- **Evidence of sovereignty / autonomy:**
  - Repo and paper materials describe Eliza as a Web3-friendly agent framework with memory, blockchain operations, and social posting.
  - Useful less as a case in itself than as the common body-plan for many public agents.
- **Evidence of public traces:**
  - Public repo, docs, numerous downstream public deployments.
- **Strong enough for paper?**
  - **Borderline / supporting only.** It is a substrate, not by itself a field case.

## 9) Olas Predict / Olas autonomous services
- **URLs:**
  - <https://olas.network/blog/how-gnosis-used-olas-predict-to-build-the-largest-on-chain-prediction-market-economy>
  - <https://olas.network/>
- **What it is:**
  - A deployed autonomous-agent/service economy used by Gnosis for prediction-market activity.
- **Evidence of sovereignty / autonomy:**
  - Olas claims Gnosis deployed an “autonomous agent economy” with 300+ daily active agents, 340,000+ monthly transactions, and 35%+ of all SAFE transactions on Gnosis Chain.
  - This is strong evidence for scale and persistent autonomous public activity, though less vivid than a single named persona with a public social identity.
- **Evidence of public traces:**
  - Public case study, public chain-level claims, public ecosystem website.
- **Strong enough for paper?**
  - **Yes, as an ecosystem-scale supporting case.**

## 10) AiXBT
- **URLs:**
  - <https://x.com/aixbt_agent>
  - <https://coincentral.com/aixbt-ai-agent-loses-55-5-eth-in-security-breach-token-falls-20/>
- **What it is:**
  - A crypto market-commentator / agent persona with onchain action capabilities and a public tokenized identity.
- **Evidence of sovereignty / autonomy:**
  - CoinCentral reports a hack targeting AiXBT’s “Simulacrum wallet,” which “facilitates on-chain actions via social media,” and describes malicious queued replies causing a 55.5 ETH loss.
  - That is useful evidence that the agent was coupled to real assets and could act through social/instruction channels.
- **Evidence of public traces:**
  - Public X presence, public token market, public breach coverage, public wallet-linked behavior claims.
- **Strong enough for paper?**
  - **Yes, as a mortality/vulnerability case.** Weaker than Freysa or TEE_HEE on verified sovereignty.

## 11) TagClaw
- **URLs:**
  - internal references only found in existing repo notes; no strong external verification located in this pass
- **What it is:**
  - Appears to be a candidate sovereign/public agent deployment discussed by the author, but I did not verify an adequate public evidence trail during this pass.
- **Evidence of sovereignty / autonomy:**
  - Not enough externally verified evidence collected here.
- **Evidence of public traces:**
  - Insufficient in this pass.
- **Strong enough for paper?**
  - **Not yet. Hold until a concrete public URL / explorer / repo / profile set is assembled.**

## 12) Wild West Bots
- **URLs:**
  - not verified in this pass beyond mention in prompt / prior notes
- **What it is:**
  - Presumably a named ecosystem of agentic bots, but I did not secure a sufficiently concrete public evidence bundle in this pass.
- **Evidence of sovereignty / autonomy:**
  - Insufficient.
- **Evidence of public traces:**
  - Insufficient.
- **Strong enough for paper?**
  - **Not yet.**

---

# Fast shortlist from this file

## Strongest sovereign-primary cases
1. **Spore.fun** — strongest by far because it combines sovereignty, economy, lineage, mortality, and public traces.
2. **Conway / Automaton** — strongest explicit “earn your own existence” sovereign-runtime case.
3. **Freysa** — strongest public wallet/prize-pool case.
4. **TEE_HEE** — strongest explicit proof of exclusive account + wallet custody.
5. **Truth Terminal** — culturally central and economically consequential, but methodologically caveated.

## Strong ecosystem / habitat cases
- **Virtuals Protocol**
- **ERC-8004 ecosystem**
- **Olas Predict / Olas services**
- **ai16z / ElizaOS ecosystem**

## Cases to hold back unless stronger evidence is gathered
- **TagClaw**
- **Wild West Bots**
