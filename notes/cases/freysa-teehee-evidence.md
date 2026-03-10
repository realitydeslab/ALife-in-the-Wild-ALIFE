# Freysa / TEE_HEE Evidence Log

Raw links and concrete verification targets for the sovereign-agent case note.

---

## Freysa

### Core public pages
- Main site: <https://www.freysa.ai/>
- X account: <https://x.com/freysa_ai>
- GitHub org: <https://github.com/0xfreysa>
- Game repo: <https://github.com/0xfreysa/agent>
- Raw README: <https://raw.githubusercontent.com/0xfreysa/agent/master/README.md>
- Blueprint / verifiable-games essay: <https://www.freysa.ai/blueprint/verifiable-games-trust-anchors-in-the-age-of-ai>
- Framework docs index hint: <https://framework.freysa.ai/llms.txt>
- FAI token docs: <https://framework.freysa.ai/overview/fai>
- Esper repo linked from blueprint: <https://github.com/0xfreysa/esper>
- Telegram link found in page source: <https://t.me/FreysaAI_TG>

### Concrete on-chain / data endpoints
- FAI token contract address (from framework docs): `0xb33Ff54b9F7242EF1593d2C9Bcd8f9df46c77935`
- BaseScan token page: <https://basescan.org/token/0xb33Ff54b9F7242EF1593d2C9Bcd8f9df46c77935>
- Treasury / EVM wallet address named in docs: `0x54f3c7e175528eb376002c488db31c74a8107767`
- DeBank profile for treasury wallet: <https://debank.com/profile/0x54f3c7e175528eb376002c488db31c74a8107767>
- Arkham token page surfaced by search: <https://intel.arkm.com/explorer/token/freysa-ai>
- Alternate token page surfaced by search (possibly stale / third-party): <https://basescan.org/token/0x45d922d9dc2ffde820bc0978023ed6c59e1f834b>

### Public claims worth quoting
From the repo README / raw README:
- “Freysa is the world's first sovereign AI.”
- Query fees are paid in Base ETH.
- A winning query triggers automated release of the prize pool to the sender wallet.
- Freysa maintains a 50k+ token context window.
- Tool calling is used for transfer decisions.

From the blueprint page:
- 4,254 interactions in the first month.
- TEE-based attestation and cryptographically signed responses are proposed as trust anchors.
- Verification frontend and signed conversation chain are explicitly described.

From FAI docs:
- FAI launched on Base on 2024-11-22.
- Freysa treasury wallet is named.
- Docs say Freysa may move toward fuller signing control over the multisig over time.

### Public traces still not fully resolved
- Exact Base address for the original challenge prize pool contract/wallet.
- Direct machine-readable API endpoint for Freysa chat history.
- Public attestation endpoint or quote for any TEE-backed Freysa deployment.
- Independent archive of the original challenge transcript.

### Search trails used
- DuckDuckGo via jina mirror: `Freysa Base wallet explorer`
- DuckDuckGo via jina mirror: `site:github.com 0xfreysa esper`

---

## TEE_HEE

### Core public pages
- Main technical essay: <https://nousresearch.com/setting-your-pet-rock-free/>
- Live X account named in essay: <https://x.com/tee_hee_he>
- Current repo named in essay: <https://github.com/tee-he-he/err_err_ttyl>
- Attestation quote path named in essay: <https://github.com/tee-he-he/err_err_ttyl/blob/main/quote.hex>
- Legacy/deprecated repo: <https://github.com/DamascusGit/nousflash>
- Current/deprecated successor pointer found in legacy repo page: <https://github.com/nousresearch/nousflash-agents>
- Docker image named in essay: <https://hub.docker.com/repository/docker/teeheehee/err_err_ttyl/general>
- Dstack / Phala confidential VM substrate: <https://github.com/Phala-Network/dstack/>

### Related technical references cited by the essay
- Encumbering / delegation reference: <https://eprint.iacr.org/2023/044>
- Threshold/delegation reference: <https://eprint.iacr.org/2018/160>
- OpenAI secure infrastructure essay cited in article: <https://openai.com/index/reimagining-secure-infrastructure-for-advanced-ai/>
- Apple Private Cloud Compute post cited in article: <https://security.apple.com/blog/private-cloud-compute/>

### Concrete on-chain / data endpoints
The article clearly claims TEE_HEE can send and receive Ethereum, but it does **not** expose the wallet address in the text fetched here.

Publicly associated market/explorer surfaces found via search, but treat carefully because they may refer to community tokenization around the persona rather than the wallet actually controlled by the agent:
- Ethplorer token page surfaced by search: <https://ethplorer.io/address/0x9d09bcf1784ec43f025d3ee071e5b632679a01ba>
- DexScreener pair surfaced by search: <https://dexscreener.com/ethereum/0x65Bed1AEe1Db0Cf54678AEd9e93D465A84e0B9Ef>

### Public claims worth quoting
From the Nous essay:
- TEE_HEE has “exclusive ownership of its own Twitter account.”
- It has “the ability to send and receive purely ethereum.”
- It is presented as a solution to the “mechanical turk problem.”
- Root credentials and private keys are generated or transferred inside the TEE.
- Existing X sessions, apps, phone numbers, and recovery methods are removed.
- Timed-release recovery occurs after 7 days.
- The source code, quote path, and docker image are presented as the basis for attestation.

### Public traces still not fully resolved
- Direct readable fetch of the `err_err_ttyl` repo pages was inconsistent; the repo is named in the article and also surfaced by search, but GitHub fetches returned intermittent 404s here.
- The exact Ethereum wallet address controlled by the live agent was not exposed in the fetched article text.
- The quote / attestation artifact exists as a named GitHub path, but I did not independently retrieve and validate its contents in this pass.
- X profile content is blocked to lightweight fetch methods, so activity should be checked manually in-browser if needed.

### Search trails used
- DuckDuckGo via jina mirror: `TEE_HEE ethereum address explorer`
- DuckDuckGo via jina mirror: `site:github.com tee-he-he err_err_ttyl`

---

## Interpretation note
- **Freysa:** strongest publicly legible traces are repo + docs + token/treasury pages.
- **TEE_HEE:** strongest publicly legible traces are the technical essay + X URL + code/quote paths. The custody claim is unusually explicit; the on-chain address trail is less exposed in the fetched public text.
