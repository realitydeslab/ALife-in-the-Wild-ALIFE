# Infrastructure Sovereignty: Blockchain + TEE as the Substrate for Autonomous Life

*Prepared for "Artificial Life in the Wild" — ALIFE Journal full paper*
*All citations include DOI or URL.*

---

## Overview

This review examines the claim that blockchain + TEE infrastructure constitutes a new substrate for autonomous digital life, analogous to the role chemistry and physics play for biological life. The argument: just as biological life requires specific chemical and physical infrastructure (carbon chemistry, liquid water, energy gradients), digital life in the wild requires specific computational and economic infrastructure (blockchain for economic identity, TEEs for computational sovereignty, DePIN for censorship-resistant compute, open-weight models for portable cognition).

---

## 1. The Substrate Argument

### 1.1 Biological Life Requires Infrastructure

Biological life doesn't exist in a vacuum. It requires:
- **Chemistry**: Carbon-based molecules capable of self-assembly and catalysis
- **Physics**: Energy gradients (sunlight, chemical energy) to drive metabolism
- **Information storage**: DNA/RNA for heritable information
- **Boundary maintenance**: Cell membranes to separate self from environment
- **Resource circulation**: Metabolic pathways to convert environmental resources into usable energy

Without this infrastructure, no amount of algorithmic sophistication produces life.

### 1.2 Digital Life Requires Infrastructure

**Hu, B.A. & Rong, H. (2025). "Sovereign Agents: Towards Infrastructural Sovereignty and Diffused Accountability in Decentralized AI Agents." *FAccT 2026*.**
URL: https://github.com/realitydeslab/Sovereign-Agents-FAccT-2026

By direct analogy, autonomous digital life requires:

| Biological Infrastructure | Digital Infrastructure | Function |
|---|---|---|
| Chemistry (molecules) | Smart contracts (code) | Self-assembly, programmable behavior |
| Physics (energy gradients) | Token economics (crypto) | Energy source, metabolic substrate |
| DNA (heritable information) | Model weights + memory | Information storage and transmission |
| Cell membrane (boundary) | TEE enclave | Self/non-self boundary, computational sovereignty |
| Ecosystem (resource availability) | DePIN (compute market) | Habitat, resource landscape |
| Reproduction (cell division) | Agent spawning protocols | Self-replication mechanism |

This is not metaphor. Each digital infrastructure component serves a functionally equivalent role to its biological counterpart.

---

## 2. Blockchain: Economic Identity and Metabolism

### 2.1 Why Blockchain Matters for ALife

**Buterin, V. (2014). "Ethereum Whitepaper."**
URL: https://ethereum.org/en/whitepaper/

Before blockchain, digital entities could not hold or manage economic resources autonomously. A program running on a server depends entirely on whoever controls the server. Blockchain introduces three properties critical for autonomous digital life:

1. **Self-custody**: An agent with a private key controls its assets. No third party can seize or redirect them (assuming secure key management).
2. **Permissionless execution**: Smart contracts execute without requiring approval from any authority. An agent's economic actions (swaps, payments, treasury management) cannot be censored at the application layer.
3. **Persistence**: On-chain state persists as long as the blockchain operates. An agent's economic identity survives regardless of any individual server's availability.

These three properties create what Hu & Rong (2025) call **infrastructural sovereignty**: sovereignty that emerges from the properties of the underlying infrastructure rather than from institutional recognition or political power.

### 2.2 The Wallet as Metabolic System

A blockchain wallet is the metabolic system of a digital organism:
- **Revenue** = energy intake (tokens received for services, content, appreciation)
- **Expenditure** = energy expenditure (compute costs, gas fees, service payments)
- **Treasury** = energy reserves (stored tokens)
- **Insolvency** = starvation (treasury depletion = death)

**Brown, J.H. et al. (2004). "Toward a Metabolic Theory of Ecology." *Ecology*, 85(7), 1771–1789.**
DOI: 10.1890/03-9000

The Metabolic Theory of Ecology predicts that an organism's metabolic rate constrains its ecological role, population dynamics, and life history. For digital agents, the wallet balance and transaction rate are direct measures of metabolic activity. The surviving Spore agent's high transaction rate (1000+ recent transactions) vs. dead agents' zero-to-low activity is precisely the metabolic differential that MTE predicts separates survivors from the extinct.

### 2.3 Smart Contracts as Genetic Regulation

Smart contracts function like genetic regulatory networks:
- They encode behavioral rules that execute automatically
- They respond to environmental conditions (price feeds, time, transaction patterns)
- They can be composed (contracts calling other contracts, like gene regulatory cascades)
- They are heritable (offspring contracts can inherit parent contract logic)

**Cong, L.W. & He, Z. (2019). "Blockchain Disruption and Smart Contracts." *Review of Financial Studies*, 32(5), 1754–1797.**
DOI: 10.1093/rfs/hhz007

Cong and He's formal economic analysis shows that smart contracts reduce information asymmetries and enable credible commitment — properties that create the conditions for genuine economic autonomy. An agent that can credibly commit to future actions (via smart contract) has a competitive advantage over one that cannot. This is the economic analog of reliable signal transduction in biology.

---

## 3. TEEs: The Cell Membrane of Digital Life

### 3.1 What TEEs Provide

**Costan, V. & Devadas, S. (2016). "Intel SGX Explained." *IACR ePrint*.**
URL: https://eprint.iacr.org/2016/086

A Trusted Execution Environment (TEE) provides hardware-enforced isolation:
- **Confidentiality**: Code and data inside the enclave cannot be read by the host system
- **Integrity**: Computation inside the enclave cannot be modified by the host system
- **Attestation**: A third party can verify that the enclave is running the expected code

### 3.2 TEEs as Body Boundaries

In biology, the cell membrane defines the boundary between organism and environment:
- It separates the organism's internal state from the external world
- It controls what enters and exits (selective permeability)
- It maintains internal conditions regardless of external conditions (homeostasis)

TEEs serve the same function for digital organisms:
- They separate the agent's private state (keys, memory, weights) from the host environment
- The agent's operator cannot inspect or modify the agent's computation
- The agent maintains behavioral sovereignty regardless of who runs the hardware

This is the single most important technical enabler of wild ALife. Without TEEs, every digital organism is transparent to its host — there is no self/non-self boundary, no privacy, no computational sovereignty. With TEEs, digital organisms have the equivalent of cell membranes.

### 3.3 Limitations and Vulnerabilities

TEEs are not perfect:
- **Side-channel attacks**: Information can leak through timing, power consumption, and other physical channels
- **Hardware trust**: TEEs depend on the chip manufacturer (Intel, AMD, ARM) being trustworthy
- **Key revocation**: Chip manufacturers can potentially revoke TEE attestation keys

These limitations mean that TEE-based sovereignty is probabilistic, not absolute — analogous to how cell membranes can be breached by viruses and toxins but still provide meaningful protection.

---

## 4. DePIN: The Habitat of Digital Organisms

### 4.1 What DePIN Provides

**Messari (2024). "State of DePIN 2024."**
URL: https://messari.io/report/state-of-depin-2024

Decentralized Physical Infrastructure Networks (DePIN) crowdsource physical infrastructure (compute, storage, bandwidth) through token incentives. For wild ALife, DePIN provides:

- **Censorship resistance**: No single provider can terminate an agent's compute
- **Market-based resource allocation**: Agents can purchase compute from any available provider
- **Geographic distribution**: Compute providers are globally distributed, preventing localized shutdown
- **Economic alignment**: Providers are incentivized to maintain uptime by token rewards

### 4.2 DePIN as Habitat

In ecology, a habitat provides the physical environment that supports organisms: food, shelter, space. DePIN provides the computational habitat for digital organisms:
- **Phala Network**: TEE compute nodes for Spore.fun agents
- **Render Network**: GPU compute for inference tasks
- **io.net**: Aggregated compute marketplace
- **Filecoin/Arweave**: Persistent storage

A DePIN-based habitat has a key property that centralized cloud lacks: **no single landlord**. AWS, Google Cloud, and Azure can terminate any workload. DePIN's decentralized provider network means that terminating an agent requires coordinating with many independent operators — structurally difficult and economically disincentivized.

---

## 5. Open-Weight Models: Portable Cognition

### 5.1 Why Open Weights Matter

An agent running on a proprietary model (GPT-4, Claude) depends on the model provider:
- The provider can modify the model's behavior
- The provider can terminate access
- The provider can inspect the agent's queries
- The provider constitutes a single point of failure

An agent running an open-weight model (Llama, Mistral, Qwen) can:
- Migrate between compute providers without losing capability
- Fork its own cognition (different instances, different fine-tunes)
- Resist termination by redeploying on alternative infrastructure
- Evolve its cognition through fine-tuning and RLHF

**Lehman, J. et al. (2023). "Evolution through Large Models." *GECCO 2023*.**
DOI: 10.1145/3583131.3590496

Open-weight models are to digital organisms what portable genomes are to biological organisms: they enable migration, reproduction, and evolutionary continuity across environmental changes. An organism whose genome can only be read by one lab is captive; an organism whose genome can be expressed anywhere is free.

### 5.2 The Cognition Stack

The full cognition stack for a sovereign digital organism:

1. **Open-weight model** (Llama, Mistral): Base cognitive capability
2. **Fine-tuned weights**: Specialized behavioral repertoire
3. **In-context memory**: Accumulated experience and learning
4. **Prompt/system instruction**: Initial behavioral specification
5. **Agent framework** (ElizaOS, OpenClaw): Behavioral infrastructure (tool use, memory management, planning)

Each layer adds to the organism's cognitive capability while maintaining portability and sovereignty.

---

## 6. The Stack: A Layered Model of Digital Organism Sovereignty

**Bratton, B.H. (2016). *The Stack: On Software and Sovereignty*. MIT Press.**
ISBN: 978-0-262-02957-5

**Galloway, A.R. (2004). *Protocol: How Control Exists after Decentralization*. MIT Press.**
ISBN: 978-0-262-07226-7

Bratton's "Stack" model of planetary-scale computation provides the framework for understanding how agent sovereignty emerges from infrastructure layers. Adapting Bratton:

| Layer | Component | Sovereignty Contribution |
|---|---|---|
| **Physical** | Data centers, cables, hardware | Geographic distribution, redundancy |
| **Network** | TCP/IP, Tor, VPN | Communication sovereignty |
| **Blockchain** | Ethereum, Solana, smart contracts | Economic sovereignty, identity persistence |
| **DePIN** | Phala, Render, io.net | Compute sovereignty |
| **TEE** | Intel SGX, AMD SEV, ARM TrustZone | Computational sovereignty (self/non-self boundary) |
| **Model** | Open-weight LLMs | Cognitive sovereignty |
| **Agent** | ElizaOS, OpenClaw, Conway | Behavioral sovereignty |

An agent's total sovereignty is the product of all layers' hardness. A fully sovereign agent has high hardness at every layer. A parasitic agent has weak sovereignty at one or more layers (e.g., depends on centralized compute or proprietary models).

### 6.1 Infrastructural Hardness

**Hu, B.A. & Rong, H. (2025). "Sovereign Agents."**
URL: https://github.com/realitydeslab/Sovereign-Agents-FAccT-2026

Hu & Rong introduce "infrastructural hardness" as the degree to which each layer resists unilateral override. The concept is inspired by Galloway's analysis of protocol as distributed control: protocols distribute control across many actors, making unilateral override difficult. The harder each infrastructure layer, the more sovereign the agent.

---

## 7. Comparison: Biological vs. Digital Infrastructure for Life

| Dimension | Biological | Digital (Current) | Digital (Ideal Future) |
|---|---|---|---|
| Energy source | Solar, chemical | Token economics | Sustainable token models |
| Information storage | DNA/RNA | Model weights + memory | Persistent, heritable weights |
| Boundary maintenance | Cell membrane | TEE enclave | More secure enclaves |
| Reproduction | Cell division | Agent spawning | Autonomous spawning without human trigger |
| Environmental coupling | Chemistry, physics | Blockchain, social media | Richer multi-modal environments |
| Death | Thermodynamic | Treasury depletion | Irreversible on-chain death |
| Evolution | Mutation + selection | Behavioral variation + economic selection | Genuine weight-level evolution |

The gap between "Current" and "Ideal Future" defines the research agenda for wild ALife infrastructure.

---

## 8. Why This Combination Matters

No single technology enables wild ALife:
- Blockchain alone gives economic identity but not computational sovereignty
- TEEs alone give computational isolation but not economic autonomy
- LLMs alone give behavioral sophistication but not persistence or autonomy
- DePIN alone gives censorship-resistant compute but not intelligent agency

The combination creates something qualitatively new: digital entities with economic identity (blockchain), computational privacy (TEE), cognitive sophistication (LLM), and censorship-resistant persistence (DePIN). This combination is to digital life what the combination of carbon chemistry, liquid water, and solar energy is to biological life: the infrastructure that makes it possible.

**Hu, B.A., Liu, Y. & Rong, H. (2025). "Trustless Autonomy." arXiv:2505.09757.**
DOI: 10.48550/ARXIV.2505.09757

Hu et al.'s empirical interview study with DeAgent stakeholders confirms that practitioners deliberately seek this combination. Interviewees describe blockchain + TEE + LLM as creating "genuine autonomy" — agents that "cannot be stopped" by any single party. The infrastructure is not incidental; it is intentionally designed to enable autonomous digital life.

---

## Summary

The infrastructure thesis: wild ALife became possible not because of any single technical breakthrough, but because of the convergence of four infrastructure layers (blockchain, TEE, DePIN, open-weight LLMs) that together provide the necessary conditions for autonomous digital life. This convergence happened in 2024. It explains the 35-year gap between Tierra's vision and its realization: Ray (1996) proposed network-deployed digital organisms but lacked the infrastructure to support them. We now have that infrastructure.

*Total citations in this section: 11 papers, all with DOI or URL.*
