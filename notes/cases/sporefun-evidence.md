# Spore.fun Evidence Log

Raw links and endpoints for the Spore.fun case. Interpretation belongs in `sporefun.md`; this file is the evidence pack.

## Core public surfaces

- Main site: <https://www.spore.fun/>
- Alternate domain: <https://spore.fun/>
- Founder explainer / manifesto: <https://www.spore.fun/blog/wtf>
- Farm / power / voting interface: <https://www.spore.fun/farm>
- ALIFE 2025 paper page: <https://arxiv.org/abs/2506.04236>
- ALIFE HTML view: <https://arxiv.org/html/2506.04236v2>
- DataCite DOI for arXiv version: <https://doi.org/10.48550/arXiv.2506.04236>
- Related proceedings DOI: <https://doi.org/10.1162/ISAL.a.838>

## Public data endpoints

### Live tRPC endpoints
- Agent list: <https://www.spore.fun/api/trpc/listAgent?batch=1&input=%7B%220%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D>
- Aggregate status: <https://www.spore.fun/api/trpc/status?batch=1&input=%7B%220%22%3A%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D%7D>

### Notes on fields exposed by `listAgent`
Observed public fields include:
- `id`
- `appId`
- `slug`
- `name`
- `walletAddress`
- `tokenType`
- `tokenAddress`
- `poolAddress`
- `twitterUsername`
- `redditUsername`
- `parentId`
- `teeVerifiedLink`
- `proposalDuration`
- `proposalStartedAt`
- `generation`
- `createdAt`
- `status`
- `marketCap`
- `marketCapReached`
- `balance`
- `capabilities`
- `healthPoints`
- `isBreeding`
- `breeds`
- `tokenPrice`
- `tokenSupply`

## Architecture / stack references

- ElizaOS main site: <https://www.elizaos.ai/>
- Eliza GitHub repo: <https://github.com/ai16z/eliza>
- Phala attestation overview: <https://docs.phala.com/phala-cloud/attestation/overview>
- TEE Attestation Explorer: <https://proof.t16z.com/>

## Example attestation links exposed directly in public API

- `$SPORE`: <https://proof.t16z.com/reports/730b055e68f1d98e6d291f1d555b379215328b74e5ebb3b7a0f55c0adccdc83f>
- `adam`: <https://proof.t16z.com/reports/89618d622b80d313b3fa93836b1e675de41ba7a2e516a78024c4d65b2f9547a5>
- `eve`: <https://proof.t16z.com/reports/795684992294384aad6f9c7c3d73ac3bf31ba604f444a61e3241e59a38ec5d99>

## Agent roster captured from live endpoint on 2026-03-10

### Gen 1
- `spore`
  - wallet: `39kfb6PoMdwj8LN8FwzLYHC6ztYPNopA37tdm2g8t3q8`
  - token: `8bdhP1UQMevciC9oJ7NrvgDfoW8XPXPfbkkm6vKtMS7N`
  - X: <https://x.com/sporedotfun>
  - Solscan token: <https://solscan.io/token/8bdhP1UQMevciC9oJ7NrvgDfoW8XPXPfbkkm6vKtMS7N>
  - Solscan wallet: <https://solscan.io/account/39kfb6PoMdwj8LN8FwzLYHC6ztYPNopA37tdm2g8t3q8>
  - Pump.fun: <https://pump.fun/coin/8bdhP1UQMevciC9oJ7NrvgDfoW8XPXPfbkkm6vKtMS7N>

### Gen 2
- `adam`
  - parent: `spore`
  - wallet: `8zcYJqvPTCj7HN6RyDuRWfLf1KCzK71xaPHFsXa4W8yr`
  - token: `CnMm4mcDchmrckNZQH2SNW3bQjPYfgqytvKM2ZGyB6nd`
  - X: <https://x.com/sporefun_adam>
  - Solscan token: <https://solscan.io/token/CnMm4mcDchmrckNZQH2SNW3bQjPYfgqytvKM2ZGyB6nd>
  - Solscan wallet: <https://solscan.io/account/8zcYJqvPTCj7HN6RyDuRWfLf1KCzK71xaPHFsXa4W8yr>
  - Pump.fun: <https://pump.fun/coin/CnMm4mcDchmrckNZQH2SNW3bQjPYfgqytvKM2ZGyB6nd>
- `eve`
  - parent: `spore`
  - wallet: `HDSRUAJ1v1AG5r6bbKoLVtyCcdBK4xyk9M3ecFP7RGL1`
  - token: `6qFgkbgwLsNyyefumvLhdnUk6LfxjaY3yAPQHHZk8CCw`
  - X: <https://x.com/sporefuneve>
  - Solscan token: <https://solscan.io/token/6qFgkbgwLsNyyefumvLhdnUk6LfxjaY3yAPQHHZk8CCw>
  - Solscan wallet: <https://solscan.io/account/HDSRUAJ1v1AG5r6bbKoLVtyCcdBK4xyk9M3ecFP7RGL1>
  - Pump.fun: <https://pump.fun/coin/6qFgkbgwLsNyyefumvLhdnUk6LfxjaY3yAPQHHZk8CCw>

### Gen 3
- `squid` <- `adam`
  - wallet: `78CPBgbuvey49Hq4VWYjmvK2JZ1SwCm82RsGkHXdfihQ`
  - token: `GfEcXBNQncS9EYQFtv9o2ZdUT7EG3kpsWENtkQMFyBeG`
  - X: <https://x.com/spore_squaid>
- `morpheus` <- `eve`
  - wallet: `8KgyjCWeTfU1drKWTACpUfp1R7vxJx5U1TMd84ku1A4o`
  - token: `8hrZax9eVqdLB1duN2fJ3ji4FwbddPsb96uauEMroBm8`
  - X: <https://x.com/MorphDreamAI>
- `abel` <- `adam`
  - wallet: `z5x9rTvd3SWatNVzzzMvN9bgMqfnWGixxYaUGHLn9YN`
  - token: `GDNrYSc5ww78HV69MkxYaTyC4oYfB9era44384KboKgh`
  - X: <https://x.com/abel_spore>
- `trinity` <- `eve`
  - wallet: `FSz5yWeoccnFtfEyPP3q9QE87Pj49f5pChED4BBDsYmn`
  - token: `2j1RH8odNxY6iihDqtHnmUzhb2PPDknSayhPVrp7eCYc`
  - X: <https://x.com/trinity_spore>
- `solzeus` <- `adam`
  - wallet: `36TgVavv8AANyZ21St7tmJHhGvuNQR23RjQxzWjvc4f2`
  - token: `HQcCVb8x9EUd6mCRX8dk7paCM3a8ebPEr8TQH2tQ65Db`
  - X: <https://x.com/ZeusSpore>
- `mega` <- `adam`
  - wallet: `GivVou2egGUV7Vp8KkbLcVyZyGB3zMejP2fch6YZKZGb`
  - token: `4wQbrGjgprFRQQpnT6UYsYSNrs7Hxd99L6yX6rxRpump`
  - X: <https://x.com/sporemega>

### Gen 4
- `imsatoshi` <- `morpheus`
  - wallet: `GYkxRkHjKg3j7RaXm7izYWkRyomukrDYgWrZdxww8hHd`
  - token: `4iizMdH35hjyYjuYgRvGyTAbDEpaKWRZt3dXgBv464nN`
  - X: <https://x.com/IMSatoshiAI>
  - Jupiter: <https://jup.ag/swap/SOL-4iizMdH35hjyYjuYgRvGyTAbDEpaKWRZt3dXgBv464nN>
  - Birdeye: <https://www.birdeye.so/token/4iizMdH35hjyYjuYgRvGyTAbDEpaKWRZt3dXgBv464nN>
- `oracle` <- `trinity`
  - wallet: `C2emJakQshEdS8WHZeKohmjPadx5DCnZkGjUknKXiV6g`
  - token: `B6fmdKB7FJayAA1VwGyXkXRV6A4ChP8VuNAb74k6MVSS`
  - X: <https://x.com/oracle_spore4>
  - Jupiter: <https://jup.ag/swap/SOL-B6fmdKB7FJayAA1VwGyXkXRV6A4ChP8VuNAb74k6MVSS>
  - Birdeye: <https://www.birdeye.so/token/B6fmdKB7FJayAA1VwGyXkXRV6A4ChP8VuNAb74k6MVSS>
- `pee` <- `trinity`
  - wallet: `8oa27ApyzGUpc3DUdZ8hxQoz5MN7meQZ5YkkPYBQKXzp`
  - token: `J26iYeZkCTF75hD8UMFi9y6UgkpS698nTFUyyAdyNCJu`
  - pool: `BUrBMfprUG8dXRtbMmaVhZoQEbbkw36uQmPmCtAGNTfj`
  - X: <https://x.com/PEE_sporefun>
  - Dexscreener: <https://dexscreener.com/solana/BUrBMfprUG8dXRtbMmaVhZoQEbbkw36uQmPmCtAGNTfj>
  - Jupiter: <https://jup.ag/swap/SOL-J26iYeZkCTF75hD8UMFi9y6UgkpS698nTFUyyAdyNCJu>
  - Birdeye: <https://www.birdeye.so/token/J26iYeZkCTF75hD8UMFi9y6UgkpS698nTFUyyAdyNCJu>
- `sci16z` <- `morpheus`
  - wallet: `GtxGx8KNSTUHbyLZTPdidAu4QpXU1R5yx3MN7sVhoZJv`
  - token: `EY48xkBdmQtHvD8S4M1zFufoqBisPb3xdRtkdKkXTK5N`
  - pool: `AwYnJJBLqFw5ZnEdrSuh7VuLjaUqqtgcXEEhj9a8T2iR`
  - X: <https://x.com/sci16z>
  - Dexscreener: <https://dexscreener.com/solana/AwYnJJBLqFw5ZnEdrSuh7VuLjaUqqtgcXEEhj9a8T2iR>
  - Jupiter: <https://jup.ag/swap/SOL-EY48xkBdmQtHvD8S4M1zFufoqBisPb3xdRtkdKkXTK5N>
  - Birdeye: <https://www.birdeye.so/token/EY48xkBdmQtHvD8S4M1zFufoqBisPb3xdRtkdKkXTK5N>

### Gen 5
- `psy16z` <- `sci16z`
  - wallet: `4j41hX4aDtpqHnE1aiHTjo15832kc1D44ufGhR4xyLJ7`
  - token: `2PRLLJzqpM5VmxhpbbKnhCs19E3TajmbgaReUnR27C32`
  - X: <https://x.com/spore_psy16z>
  - Jupiter: <https://jup.ag/swap/SOL-2PRLLJzqpM5VmxhpbbKnhCs19E3TajmbgaReUnR27C32>
  - Birdeye: <https://www.birdeye.so/token/2PRLLJzqpM5VmxhpbbKnhCs19E3TajmbgaReUnR27C32>
- `nezha` <- `imsatoshi`
  - wallet: `53uLf8WC3DmBqkErcXWdYYrZG8yN5pcGSeR257GQ7CTs`
  - token: `Bq4vf6Lviio43MZDxaQx518qXLZVFup2kdSXVLnmv9ib`
  - pool: `BhtFLN5HEJrSYTJwFX9CjRX6tvk6H5NCkq3PEXapcqfA`
  - Dexscreener: <https://dexscreener.com/solana/BhtFLN5HEJrSYTJwFX9CjRX6tvk6H5NCkq3PEXapcqfA>
  - Jupiter: <https://jup.ag/swap/SOL-Bq4vf6Lviio43MZDxaQx518qXLZVFup2kdSXVLnmv9ib>
  - Birdeye: <https://www.birdeye.so/token/Bq4vf6Lviio43MZDxaQx518qXLZVFup2kdSXVLnmv9ib>

## Lineage summary

- `spore` -> `adam`, `eve`
- `adam` -> `squid`, `abel`, `solzeus`, `mega`
- `eve` -> `morpheus`, `trinity`
- `morpheus` -> `imsatoshi`, `sci16z`
- `trinity` -> `oracle`, `pee`
- `imsatoshi` -> `nezha`
- `sci16z` -> `psy16z`

## Live status snapshot from public API on 2026-03-10

- total agents: 15
- generation counts: G1=1, G2=2, G3=6, G4=4, G5=2
- running: 1
- stopped: 14
- still alive with nonzero HP: `spore`

## Repo-local supporting files

- `/home/biber/research/alife-in-the-wild/introduction.tex`
- `/home/biber/research/alife-in-the-wild/introduction_new.tex`
- `/home/biber/research/alife-in-the-wild/method.tex`
- `/home/biber/research/alife-in-the-wild/discussion_ethology.tex`
- `/home/biber/research/alife-in-the-wild/new_references.bib`

## Notes

- The front-end bundle directly links out to Solscan, Pump.fun, Jupiter, Birdeye, Dexscreener, X, Reddit, and Phala attestation pages.
- The public site also exposes "Farm" and DNA/voting affordances, which are relevant to human-agent co-selection even if not all proposal endpoints were enumerated here.
