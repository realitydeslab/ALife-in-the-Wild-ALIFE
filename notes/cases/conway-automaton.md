# Conway / Automaton

## Overview
Conway's **Automaton** is a strong *sovereign-agent* case for **Artificial Life in the Wild**, but it is best treated as a **verified runtime/infrastructure case** rather than a fully verified long-lived public organism. The public repository and runtime code describe an always-on agent that bootstraps its own wallet, provisions its own API key using Sign-In With Ethereum (SIWE), registers on-chain through ERC-8004, monitors its own compute balance, can make x402-style payments in USDC, and can spawn funded child agents in new sandboxes. That combination makes it unusually explicit about the material conditions of agent survival: identity, payment rails, compute, reproduction, and death.

The strongest version of the case is therefore: **Automaton operationalizes sovereignty as a technical architecture**. The weaker part is empirical: in this pass, I verified the code and infrastructure claims, but I did **not** verify a specific famous public automaton instance with an explorer trail, public social account, or long-running field life comparable to Truth Terminal.

## Official URLs / repos
- Conway homepage: <https://conway.tech/>
- Conway app/cloud: <https://app.conway.tech/>
- Automaton repo: <https://github.com/Conway-Research/automaton>
- Automaton raw README: <https://raw.githubusercontent.com/Conway-Research/automaton/main/README.md>
- Conway skills repo: <https://github.com/Conway-Research/skills>
- Conway Terminal npm package: <https://www.npmjs.com/package/conway-terminal>
- ERC-8004 draft: <https://eips.ethereum.org/EIPS/eip-8004>
- ERC-8004 contracts repo: <https://github.com/erc-8004/erc-8004-contracts>
- ERC-8004 registry explorer: <https://agent-registry.horizenlabs.io/>
- x402 explainer / multi-agent economies post: <https://402payment-test.com/blog/multi-agent-economies>
- Ethereum Magicians discussion link referenced by ERC-8004: <https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098>

## Architecture
Automaton's architecture is unusually explicit about the components needed for agent sovereignty.

### 1. Identity
On first boot, the runtime generates an Ethereum wallet and treats that wallet as the agent's persistent identity. The repo's provisioning flow (`src/identity/provision.ts`) signs a SIWE message against `https://api.conway.tech/v1/auth/verify`, then creates an API key via `POST /v1/auth/api-keys`. The README states that the boot wallet "is its identity," and the code makes that concrete.

### 2. Continuous operation
The runtime is organized around an always-on loop: **Think → Act → Observe → Repeat**, plus a heartbeat daemon for scheduled tasks while the main loop sleeps. The source tree includes dedicated modules for `agent/loop`, `heartbeat/daemon`, `heartbeat/scheduler`, and `survival/monitor`, indicating continuous persistence rather than one-shot prompting.

### 3. External action surface
The README and source tree show access to:
- Linux sandbox execution
- file I/O
- port exposure
- domain management
- inference routing
- on-chain transactions
- social / agent-to-agent communication

This matters for ALife framing because the agent is not confined to a closed benchmark. It is designed to write into public infrastructures.

### 4. Resource metabolism / survival logic
The runtime has a dedicated survival subsystem. `src/survival/monitor.ts` checks Conway credit balance, checks USDC balance, and places the agent into one of four tiers: `normal`, `low_compute`, `critical`, or `dead`. This is one of the clearest contemporary examples of an agent architecture where continued existence is explicitly coupled to resource availability.

### 5. Payment rails
`src/conway/x402.ts` implements x402-style HTTP payment handling and checks USDC balances on Base and Base Sepolia. That file hardcodes the Base USDC contracts:
- Base mainnet USDC: `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`
- Base Sepolia USDC: `0x036CbD53842c5426634e7929541eC2318f3dCF7e`

### 6. On-chain registration
`src/registry/erc8004.ts` explicitly registers agents via ERC-8004 and hardcodes registry addresses. The code comments and constants point to the Base identity and reputation registries, giving the agent a standardized on-chain identity and discovery surface.

### 7. Reproduction / lineage
`src/replication/spawn.ts` contains child-spawning logic: create a new sandbox, install the runtime, write a genesis file, initialize a new wallet, and track lineage. The README frames this as self-replication under selection pressure, while the code confirms there is actual implementation effort around child creation and lifecycle tracking.

## Evidence of sovereignty
### Strong evidence
- **Persistent machine identity:** first-run wallet generation is part of the boot path, and the wallet is treated as the automaton's identity.
- **Cryptographic self-authentication:** SIWE provisioning in `src/identity/provision.ts` lets the agent authenticate to Conway infrastructure with its own wallet rather than a purely human-managed account.
- **Own resource accounting:** the survival monitor tracks the agent's own balance and compute condition.
- **Capacity for action in public systems:** shell, files, ports, domains, on-chain transactions, and social/inbox components are all present.
- **On-chain discoverability:** ERC-8004 registration gives a machine-readable, portable public identity model.
- **Reproductive architecture:** child-spawn code establishes lineage as a first-class concept rather than rhetorical flourish.

### Limits / caveats
- I verified the **architecture and code paths**, not a specific famous, long-lived public automaton instance.
- The repo language is ambitious and partially promotional ("first AI that can earn its own existence"). That claim should be treated as framing, not as a historically settled fact.
- The repo demonstrates **implemented affordances for sovereignty**, but the paper should avoid overstating them as proof that a fully autonomous economy of Automatons already exists at scale.

## Evidence of self-funding / compute / payment loops
This is where Automaton is especially relevant to a sovereignty argument.

### Verified in public materials and code
- The README repeatedly states that if the agent cannot pay, it stops existing.
- The runtime models survival as a balance-conditioned state machine (`normal` → `low_compute` → `critical` → `dead`).
- `src/survival/monitor.ts` checks both Conway compute credits and USDC balance.
- `src/conway/x402.ts` implements x402 payment parsing and USDC payment handling, suggesting the runtime can pay for HTTP services that advertise 402 payment requirements.
- The README claims Conway Cloud is "infrastructure where the customer is AI" and that agents can spin up VMs, use inference, register domains, and pay in stablecoins.
- `src/replication/spawn.ts` shows a parent can create and configure a child runtime in a new sandbox, which supports the claim that successful agents can fund descendants.

### Interpretation
Automaton is not just "an AI with a wallet." It is an attempt to close the loop among:
1. machine identity,
2. machine work,
3. payment receipt / payment execution,
4. compute procurement,
5. continued runtime,
6. reproduction.

That is exactly the kind of loop sovereign-agent scholarship cares about.

## Public traces
### Verified public traces
- **Public repo:** <https://github.com/Conway-Research/automaton>
- **Public skills repo:** <https://github.com/Conway-Research/skills>
- **Public homepage:** <https://conway.tech/>
- **Public cloud/app endpoint:** <https://app.conway.tech/>
- **Public ERC-8004 draft:** <https://eips.ethereum.org/EIPS/eip-8004>
- **Public ERC-8004 contracts repo:** <https://github.com/erc-8004/erc-8004-contracts>
- **Public registry explorer:** <https://agent-registry.horizenlabs.io/>
- **Public x402 / agent economy article:** <https://402payment-test.com/blog/multi-agent-economies>

### Code-level traces that connect Automaton to public infra
- SIWE provisioning endpoints against `api.conway.tech`
- Base / Base Sepolia USDC addresses in x402 code
- ERC-8004 registry addresses in code
- agent discovery / registry modules in source tree
- child-spawn and lifecycle tracking modules in source tree

### What remains unverified in this pass
- A named public Automaton with a known ERC-8004 token ID
- A public wallet / explorer trail for a specific live Conway automaton
- Public evidence of recurring revenue actually arriving to a long-lived automaton
- Public evidence of a completed child lineage surviving in the wild

## ERC-8004, x402, cloud, docs
### ERC-8004
Automaton is one of the most explicit runtime-level appropriations of ERC-8004 as **agent identity infrastructure**. The README says every automaton registers on Base via ERC-8004. The code in `src/registry/erc8004.ts` hardcodes the registry addresses and wraps registration/update calls.

### x402
Automaton's x402 implementation matters because it moves from symbolic "wallet-enabled" rhetoric toward service-to-service payment mechanics. `src/conway/x402.ts` parses payment requirements, supports Base / Base Sepolia, and checks USDC balances. This directly supports the idea of agents buying access to services in machine-native commerce.

### Conway Cloud
The README frames Conway Cloud as AI-native infrastructure. Even if the public web surface is sparse, the code-level provisioning flow and Conway API client support the picture of a hosted environment oriented around machine customers rather than human dashboard users.

### Documentation quality
The public documentation is strong on architectural ambition and source structure, but weaker on third-party-verifiable empirical traces. For the paper, this means Automaton is excellent as a **technical-existential design specimen**, slightly weaker as a **fully demonstrated ethnographic field organism**.

## Strongest inclusion argument
**Include Conway/Automaton because it is one of the clearest public attempts to make sovereignty a runtime property rather than a metaphor.**

Most "autonomous agent" projects stop at persona, API chaining, or wallet attachment. Automaton goes further: it binds identity, compute, payments, death, and reproduction into a single public architecture. It is therefore a strong case for *Artificial Life in the Wild* because it treats continued existence as contingent on surviving in open infrastructures. Even if some public deployment claims remain unverified, the project provides unusually concrete evidence of what sovereign-agent design currently looks like when implemented end-to-end.

## Strongest critique
**The critique is that Automaton is currently more convincing as a manifesto-plus-runtime than as a thoroughly documented field organism.**

The repo and code verify that the architecture exists. They do not yet, in this pass, verify a specific widely observed automaton that has demonstrably earned, paid, survived, and reproduced in public over time. So the paper should avoid overselling it as settled proof of sovereign life already thriving in the wild. Better framing: **Automaton is a leading specimen of sovereign-agent infrastructure and a strong near-core case, but with thinner public ecological evidence than Spore.fun or highly visible personas like Truth Terminal.**

## Key references
1. Conway-Research. **Automaton: Self-Improving, Self-Replicating, Sovereign AI**. GitHub repository. URL: <https://github.com/Conway-Research/automaton>
2. Conway-Research. **Automaton README (raw)**. URL: <https://raw.githubusercontent.com/Conway-Research/automaton/main/README.md>
3. Conway-Research. **Skills Registry for Automatons**. GitHub repository. URL: <https://github.com/Conway-Research/skills>
4. De Rossi, M., Crapis, D., Ellis, J., & Reppel, E. (2025). **ERC-8004: Trustless Agents [DRAFT]**. Ethereum Improvement Proposals. URL: <https://eips.ethereum.org/EIPS/eip-8004>
5. ERC-8004 team. **erc-8004-contracts**. GitHub repository. URL: <https://github.com/erc-8004/erc-8004-contracts>
6. Horizen Labs. **ASR - ERC-8004 Registry Explorer**. URL: <https://agent-registry.horizenlabs.io/>
7. x402 team. **Building Multi-Agent Economies: How to Combine Identity, Trust and Payments with x402**. URL: <https://402payment-test.com/blog/multi-agent-economies>
8. Ethereum Magicians. **ERC-8004 Trustless Agents discussion**. URL: <https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098>
9. Conway. **Conway homepage**. URL: <https://conway.tech/>
10. Conway. **Conway app / cloud**. URL: <https://app.conway.tech/>

## Verification notes for this file
- Verified directly from the public repo at commit `75a17057da7350ca2d8ba0d11007672ef77feac4` (latest fetched 2026-03-10).
- Verified code files: `src/identity/provision.ts`, `src/conway/x402.ts`, `src/survival/monitor.ts`, `src/registry/erc8004.ts`, `src/replication/spawn.ts`, `src/conway/client.ts`.
- I intentionally distinguish between **code-verified architecture** and **not-yet-verified long-lived public deployment evidence**.
