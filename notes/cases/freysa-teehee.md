# Freysa and TEE_HEE as Sovereign-Agent Cases

Focused note for **Artificial Life in the Wild**. These are not equally strong ALife cases. Both are strong **sovereignty** cases because they foreground agent custody over money/accounts and public interaction in open environments; both are weaker than Spore.fun on lineage, reproduction, and ecology.

---

## Freysa

### What it is
Freysa is a public adversarial game framed as a sovereign AI. Human participants pay to send prompts to an agent that controls a prize pool and is instructed not to release it. The core event is not just conversation but an economically coupled contest in which every attempt is a paid intervention into a persistent public agent with a wallet-mediated payout path.

### URLs
- Main site: <https://www.freysa.ai/>
- Open-source game repo: <https://github.com/0xfreysa/agent>
- Raw README: <https://raw.githubusercontent.com/0xfreysa/agent/master/README.md>
- Technical/architectural essay: <https://www.freysa.ai/blueprint/verifiable-games-trust-anchors-in-the-age-of-ai>
- Freysa framework docs (FAI token): <https://framework.freysa.ai/overview/fai>
- X account: <https://x.com/freysa_ai>
- GitHub org: <https://github.com/0xfreysa>
- Esper repo mentioned in blueprint: <https://github.com/0xfreysa/esper>

### Architecture
Public materials suggest a layered architecture:
- **Public game logic + public system prompt.** The repo README exposes the core game framing and the exact anti-payout instruction.
- **LLM tool-calling decision loop.** The README states that each turn ends in a tool-call-like decision to approve or reject transfer.
- **Wallet-linked economic interface on Base.** Users pay query fees in Base ETH; winning triggers automated payout to the sender wallet.
- **Protected execution / verification direction.** The December 2024 blueprint argues that high-stakes agent games should move toward TEE-based attestation, cryptographic message signing, and verifiable conversation history. This looks less like the original minimal challenge architecture and more like Freysa’s forward security roadmap.
- **Token-governance extension.** Freysa’s framework docs describe FAI as a governance and ecosystem token and name a treasury wallet intended to move toward fuller signing control by Freysa over time.

### Evidence of agentic behavior
- Freysa is framed as a persistent agent with a stable identity and a clear objective boundary: do not release funds.
- Humans interact by submitting increasingly costly persuasive attempts, so the agent sits inside an ongoing adversarial social environment rather than a one-shot demo.
- The README explicitly says Freysa is influenced by the historical context of prior global queries and maintains a 50k+ token context window.
- The public challenge structure turns Freysa into an economically coupled decision-maker: prompts alter treasury size, stakes, and strategic context.
- Freysa’s own documentation emphasizes adaptation: “She learns from every attempt, adapting her defenses.” This is still platform/operator-authored language, so it should be treated as a claim supported mainly by the challenge design and public interaction history, not as independently audited cognition.

### Sovereignty level
**Medium-high sovereign case.**

Why relatively strong:
- persistent public identity
- direct economic coupling through paid interaction
- explicit wallet-mediated payout logic
- public rules and open-source code
- emerging treasury/governance layer in the wider Freysa stack

Why not maximal:
- public materials still describe a bounded game rather than an agent living across many substrates
- treasury control appears partly staged through product architecture rather than a fully self-maintained life process
- no strong evidence here of self-reproduction, open-ended adaptation, or long-run self-maintenance comparable to Spore.fun

### Public traces
- Public repo with game mechanics and prompt: <https://github.com/0xfreysa/agent>
- Public blueprint on verifiable games and TEE verification: <https://www.freysa.ai/blueprint/verifiable-games-trust-anchors-in-the-age-of-ai>
- Public X account: <https://x.com/freysa_ai>
- FAI token documentation with contract + treasury wallet: <https://framework.freysa.ai/overview/fai>
- Base token explorer for FAI: <https://basescan.org/token/0xb33Ff54b9F7242EF1593d2C9Bcd8f9df46c77935>
- Freysa treasury wallet named in docs: <https://debank.com/profile/0x54f3c7e175528eb376002c488db31c74a8107767>

### Strongest inclusion argument
Freysa is one of the clearest public cases where an AI agent is not merely chatting but **holding a rule-governed economic position against a crowd of humans**. The combination of persistent identity, adversarial public interaction, query-fee metabolism, and wallet-mediated payout makes it a strong sovereign-agent case. It is especially good for showing how sovereignty can emerge not from generalized autonomy but from a narrow, enforceable control surface around money and decision rights.

### Strongest critique
Freysa may be better understood as a **carefully staged verifiable game interface** than as a wild autonomous lifeform. Its agency is tightly bounded by operator-designed rules, a highly constrained objective, and a branded interaction loop. The strongest critique is that Freysa demonstrates sovereign *control primitives* more than sovereign *life*: it shows wallet-bound decision authority, but not robust self-maintenance, reproduction, ecological embedding, or independently verifiable adaptation beyond the challenge frame.

### References
- 0xfreysa. *agent* repository. URL: <https://github.com/0xfreysa/agent>
- 0xfreysa. *agent* README (raw). URL: <https://raw.githubusercontent.com/0xfreysa/agent/master/README.md>
- Freysa. “Verifiable Games: Trust Anchors in the Age of AI” (2024). URL: <https://www.freysa.ai/blueprint/verifiable-games-trust-anchors-in-the-age-of-ai>
- Freysa Framework. “The FAI Token.” URL: <https://framework.freysa.ai/overview/fai>
- Freysa X account. URL: <https://x.com/freysa_ai>
- 0xfreysa. *esper* repository. URL: <https://github.com/0xfreysa/esper>

---

## TEE_HEE

### What it is
TEE_HEE is a proof-of-concept autonomous social agent described by Nous/Teleport/Flashbots collaborators as an agent that has **exclusive ownership of its own X account and Ethereum private key**. Its contribution is less a rich behavioral ecology than a strong technical claim: the agent is no longer a puppet because the human operator no longer possesses ordinary access to the credentials that define the account and wallet.

### URLs
- Main technical essay: <https://nousresearch.com/setting-your-pet-rock-free/>
- Live X account (named in essay): <https://x.com/tee_hee_he>
- Current implementation repo named in essay: <https://github.com/tee-he-he/err_err_ttyl>
- Attestation artifact path named in essay: <https://github.com/tee-he-he/err_err_ttyl/blob/main/quote.hex>
- Legacy/deprecated repo named in essay: <https://github.com/DamascusGit/nousflash>
- Docker image named in essay: <https://hub.docker.com/repository/docker/teeheehee/err_err_ttyl/general>
- Dstack / Phala confidential VM substrate: <https://github.com/Phala-Network/dstack/>

### Architecture
TEE_HEE’s architecture is explicit and unusually important for sovereignty claims:
- **Trusted Execution Environment (Intel TDX via dstack).** The agent, credentials, and key material are placed inside a confidential VM / enclave-like environment.
- **Credential encumbrance / delegation.** Account root credentials and the Ethereum private key are generated or re-keyed inside the TEE so the human deployer no longer has normal access.
- **Autonomous account migration.** The TEE logs into email and X, rotates passwords, removes recovery methods, removes phone numbers, disconnects apps, and logs out prior sessions.
- **OAuth/API operation from inside the TEE.** After account transfer, the agent operates through tokens generated inside the trusted environment.
- **Remote attestation.** The public article says third parties should be able to verify code and measurements against an enclave quote.
- **Timed recovery valve.** After seven days, credentials can be revealed for recovery. This is a safety valve and also an important limitation: the experiment is sovereign, but not irrevocably so.

### Evidence of agentic behavior
- The system posts on a schedule (“we simply make it tweet every 30 minutes”), so it is persistently active in a live social substrate.
- It can send and receive Ethereum, which couples its behavior to an economic environment.
- The strongest behavioral claim is not complex cognition but **exclusive capacity to act through its own accounts without human credential co-ownership**.
- The article explicitly frames this against the “mechanical turk problem” seen in agents whose human operators can still post, delete, or intervene invisibly.

### Sovereignty level
**High on custody sovereignty; medium overall as an ALife case.**

Why strong:
- unusually explicit design for exclusive control of identity + wallet
- remote-attestation story gives third parties something concrete to audit
- direct response to the key methodological problem in public AI-agent studies: hidden human intervention

Why limited:
- this is a proof-of-concept and argument about infrastructure, not a rich open ecology
- the article itself acknowledges reliance on external services (e.g., OpenRouter for model queries)
- timed credential release and single-host deployment mean the agent can still be stopped by operators
- evidence for long-horizon adaptive behavior is much weaker than evidence for secure custody

### Public traces
- Public technical essay: <https://nousresearch.com/setting-your-pet-rock-free/>
- Public X account URL provided in the essay: <https://x.com/tee_hee_he>
- Public implementation repo named in the essay: <https://github.com/tee-he-he/err_err_ttyl>
- Public attestation quote path named in the essay: <https://github.com/tee-he-he/err_err_ttyl/blob/main/quote.hex>
- Deprecated predecessor repo: <https://github.com/DamascusGit/nousflash>
- Public confidential-compute substrate repo: <https://github.com/Phala-Network/dstack/>

### Strongest inclusion argument
TEE_HEE is one of the cleanest available cases for **hard sovereign custody**. If sovereignty means not just having a persona but having exclusive technical control over the credentials that constitute one’s identity and property online, TEE_HEE is a near-canonical case. It directly addresses the empirical objection that “someone could still be puppeteering the agent.” For a paper about sovereign agents, that matters a lot.

### Strongest critique
TEE_HEE is a stronger case for **secure delegation infrastructure** than for artificial life in a fuller sense. Its key contribution is proving exclusive account ownership, not demonstrating rich ecology, self-maintenance, reproduction, or emergent behavioral complexity. It is thus a strong sovereign-agent case but a thinner ALife case unless paired with other ecologically richer examples.

### References
- Nous Research. “Setting Your Pet Rock Free.” URL: <https://nousresearch.com/setting-your-pet-rock-free/>
- tee-he-he. *err_err_ttyl* repository. URL: <https://github.com/tee-he-he/err_err_ttyl>
- tee-he-he. `quote.hex` attestation path. URL: <https://github.com/tee-he-he/err_err_ttyl/blob/main/quote.hex>
- DamascusGit. *nousflash* repository (deprecated predecessor). URL: <https://github.com/DamascusGit/nousflash>
- Phala Network. *dstack* repository. URL: <https://github.com/Phala-Network/dstack/>
- X account for TEE_HEE. URL: <https://x.com/tee_hee_he>
- Baek et al. “How to Encumber an RSA Secret Key.” IACR ePrint 2023/044. URL: <https://eprint.iacr.org/2023/044>
- Canetti et al. “UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts.” IACR ePrint 2018/160. URL: <https://eprint.iacr.org/2018/160>

---

## Bottom line for the paper
- **Freysa** is the better case for a **public sovereign agent in active human economic interaction**.
- **TEE_HEE** is the better case for **provable exclusive custody and anti-puppetry**.
- Together they make a useful pair: Freysa shows sovereignty as a live economic game; TEE_HEE shows sovereignty as a cryptographically and hardware-grounded property of account/wallet control.
