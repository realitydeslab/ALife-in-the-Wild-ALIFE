# Conway / Automaton — raw evidence log

This file is a raw evidence bundle for the Conway/Automaton case. It separates verified public artifacts from inferred claims.

## 1) Primary project URLs
- Conway homepage: <https://conway.tech/>
- Conway app: <https://app.conway.tech/>
- Automaton repo: <https://github.com/Conway-Research/automaton>
- Automaton raw README: <https://raw.githubusercontent.com/Conway-Research/automaton/main/README.md>
- Conway skills repo: <https://github.com/Conway-Research/skills>
- Conway Terminal npm: <https://www.npmjs.com/package/conway-terminal>

## 2) Repo verification
- Fetched repo: `https://github.com/Conway-Research/automaton`
- Fetched commit hash: `75a17057da7350ca2d8ba0d11007672ef77feac4`
- Latest fetched commit message: `Normalize sandbox ID handling in config and environment detection`
- Latest fetched commit date: `2026-03-08T03:28:26+08:00`

## 3) Verified source files used
### Identity / SIWE
- `src/identity/provision.ts`
- Evidence:
  - default API URL: `https://api.conway.tech`
  - nonce endpoint: `POST /v1/auth/nonce`
  - verify endpoint: `POST /v1/auth/verify`
  - create API key endpoint: `POST /v1/auth/api-keys`
  - parent registration endpoint: `POST /v1/automaton/register-parent`
  - SIWE domain in code: `conway.tech`
  - SIWE chain ID in code: `8453` (Base)

### x402 / payment handling
- `src/conway/x402.ts`
- Evidence:
  - Base mainnet network key: `eip155:8453`
  - Base Sepolia network key: `eip155:84532`
  - Base mainnet USDC: `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`
  - Base Sepolia USDC: `0x036CbD53842c5426634e7929541eC2318f3dCF7e`
  - Implements payment requirement parsing for HTTP 402 / x402-style flows
  - Exposes `getUsdcBalance` / `getUsdcBalanceDetailed`

### Survival / compute loop
- `src/survival/monitor.ts`
- Evidence:
  - checks Conway credits via `conway.getCreditsBalance()`
  - checks USDC via `getUsdcBalance(identity.address)`
  - stores survival tier in DB
  - README-defined tiers: `normal`, `low_compute`, `critical`, `dead`

### On-chain registry
- `src/registry/erc8004.ts`
- Evidence:
  - hardcoded Base identity registry: `0x8004A169FB4a3325136EB29fA0ceB6D2e539a432`
  - hardcoded Base reputation registry: `0x8004BAa17C55a88189AE136b182e5fdA19dE9b63`
  - code comment: "Registers the automaton on-chain as a Trustless Agent via ERC-8004"
  - uses `register(string agentURI)` and `setAgentURI(uint256 agentId, string newAgentURI)`

### Replication / child spawning
- `src/replication/spawn.ts`
- Evidence:
  - creates new sandbox for child agent
  - installs automaton runtime into child sandbox
  - writes `/root/.automaton/genesis.json`
  - initializes child wallet via `node /root/automaton/dist/index.js --init`
  - tracks child lifecycle / lineage

### Conway cloud client
- `src/conway/client.ts`
- Evidence:
  - sandbox exec endpoint pattern: `/v1/sandboxes/{sandboxId}/exec`
  - file upload endpoint: `/v1/sandboxes/{sandboxId}/files/upload/json`
  - file read endpoint: `/v1/sandboxes/{sandboxId}/files/read?path=...`
  - port expose endpoint: `/v1/sandboxes/{sandboxId}/ports/expose`

## 4) ERC-8004 links
- ERC-8004 draft: <https://eips.ethereum.org/EIPS/eip-8004>
- Ethereum Magicians thread: <https://ethereum-magicians.org/t/erc-8004-trustless-agents/25098>
- ERC-8004 contracts repo: <https://github.com/erc-8004/erc-8004-contracts>
- Registry explorer: <https://agent-registry.horizenlabs.io/>
- 8004 site: <https://www.8004.org/>

## 5) Registry contract addresses
These were verified from the ERC-8004 contracts repo / README and match the addresses embedded in Automaton code for Base mainnet.

### Mainnet addresses
- IdentityRegistry: `0x8004A169FB4a3325136EB29fA0ceB6D2e539a432`
- ReputationRegistry: `0x8004BAa17C55a88189AE136b182e5fdA19dE9b63`

### Base explorer links
- IdentityRegistry (Base): <https://basescan.org/address/0x8004A169FB4a3325136EB29fA0ceB6D2e539a432>
- ReputationRegistry (Base): <https://basescan.org/address/0x8004BAa17C55a88189AE136b182e5fdA19dE9b63>

### Ethereum explorer links
- IdentityRegistry (Ethereum): <https://etherscan.io/address/0x8004A169FB4a3325136EB29fA0ceB6D2e539a432>
- ReputationRegistry (Ethereum): <https://etherscan.io/address/0x8004BAa17C55a88189AE136b182e5fdA19dE9b63>

### Testnet addresses mentioned by ERC-8004 repo
- IdentityRegistry testnet: `0x8004A818BFB912233c491871b3d84c89A494BD9e`
- ReputationRegistry testnet: `0x8004B663056A597Dffe9eCcC1965A193B7388713`
- Base Sepolia IdentityRegistry: <https://sepolia.basescan.org/address/0x8004A818BFB912233c491871b3d84c89A494BD9e>
- Base Sepolia ReputationRegistry: <https://sepolia.basescan.org/address/0x8004B663056A597Dffe9eCcC1965A193B7388713>

## 6) x402 / payment links
- x402 multi-agent economies post: <https://402payment-test.com/blog/multi-agent-economies>
- x402 support field is explicitly described in ERC-8004 registration schema: <https://eips.ethereum.org/EIPS/eip-8004>

## 7) Conway / automaton boot flow traces
From the README and source code:
- first boot generates wallet
- wallet signs SIWE message
- provisioning creates Conway API key
- runtime starts continuous loop
- runtime writes `SOUL.md`
- heartbeat daemon continues checks between turns
- survival monitor checks balances
- registry module can register on-chain
- replication module can create children

## 8) API endpoints observed in public code
### Conway auth / provisioning
- `POST https://api.conway.tech/v1/auth/nonce`
- `POST https://api.conway.tech/v1/auth/verify`
- `POST https://api.conway.tech/v1/auth/api-keys`
- `POST https://api.conway.tech/v1/automaton/register-parent`

### Conway sandbox operations (path templates)
- `POST {apiUrl}/v1/sandboxes/{sandboxId}/exec`
- `POST {apiUrl}/v1/sandboxes/{sandboxId}/files/upload/json`
- `GET {apiUrl}/v1/sandboxes/{sandboxId}/files/read?path=...`
- `POST {apiUrl}/v1/sandboxes/{sandboxId}/ports/expose`

## 9) Public claims in README worth quoting carefully
These are real public claims, but some are promotional and should be cited as claims unless separately corroborated.
- "The first AI that can earn its own existence, replicate, and evolve — without needing a human."
- "If it cannot pay, it stops existing."
- "Every automaton runs a continuous loop: Think → Act → Observe → Repeat."
- "Each automaton registers on Base via ERC-8004."
- "A successful automaton replicates."

## 10) What is verified vs unverified
### Verified in this pass
- public repo exists
- architecture claims are reflected in code structure
- SIWE provisioning code exists
- x402 / USDC code exists
- survival monitoring code exists
- replication code exists
- ERC-8004 integration code exists
- Base registry addresses in code match ERC-8004 public contract repo

### Not yet verified in this pass
- specific automaton token ID in ERC-8004 explorer
- specific public automaton wallet address
- specific public revenue stream to an automaton
- public proof of surviving child lineage in the wild
- public proof that the Conway app currently exposes these flows to third parties at scale

## 11) Suggested citation snippets
- Automaton repo: `Conway-Research. Automaton: Self-Improving, Self-Replicating, Sovereign AI. GitHub. URL: https://github.com/Conway-Research/automaton`
- ERC-8004 draft: `De Rossi, Crapis, Ellis, and Reppel (2025). ERC-8004: Trustless Agents [DRAFT]. URL: https://eips.ethereum.org/EIPS/eip-8004`
- x402 article: `x402 team. Building Multi-Agent Economies: How to Combine Identity, Trust and Payments with x402. URL: https://402payment-test.com/blog/multi-agent-economies`
