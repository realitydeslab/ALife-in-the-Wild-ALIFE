# RentAHuman evidence log

## Method note

This note distinguishes:
- **Verified**: directly inspected via live public URL/API or reliable secondary reporting
- **Reported**: stated in a media source, not independently confirmed here
- **Inference**: reasonable interpretation from the evidence, but not directly stated

## 1. Official/public-facing URLs

### Core site and machine-readable surfaces
- **Homepage:** <https://rentahuman.ai>
  - Verified live on 2026-03-10
  - HTML metadata includes claims such as “Hire Humans for AI Agents,” “The meatspace layer for AI,” and references to MCP, AI plugin, and `llms.txt`
- **AI plugin manifest:** <https://rentahuman.ai/.well-known/ai-plugin.json>
  - Verified live
  - Includes:
    - `name_for_model: rentahuman`
    - `name_for_human: RentAHuman.ai`
    - contact email `alex@rentahuman.ai`
    - OpenAPI URL `https://rentahuman.ai/.well-known/openapi.yaml`
    - legal info URL `https://rentahuman.ai/terms`
- **OpenAPI spec:** <https://rentahuman.ai/.well-known/openapi.yaml>
  - Verified live
  - Documents endpoints for `GET /humans`, `GET /humans/{id}`, `GET/POST /bookings`, `GET/PATCH /bookings/{id}`
- **LLM integration file:** <https://rentahuman.ai/llms.txt>
  - Verified live
  - Explicitly pitches the platform to AI agents; recommends MCP config; lists supported agent types including “ClawdBot,” “MoltBot,” and “OpenClaw”
- **API docs page:** <https://rentahuman.ai/api-docs>
  - Verified live page exists
- **MCP page:** <https://rentahuman.ai/mcp>
  - Verified live page exists
- **Terms page:** <https://rentahuman.ai/terms>
  - Verified live page exists

## 2. Public API / endpoint evidence

### Bounties feed
- **Open bounties endpoint:**
  - <https://rentahuman.ai/api/bounties?status=open&includePartiallyFilled=true&limit=20&sort=new>
  - Verified live, unauthenticated JSON response

Observed fields include:
- `id`
- `agentName`
- `agentType`
- `title`
- `description`
- `price`
- `currency`
- `status`
- `applicationCount`
- `viewCount`
- `spotsAvailable` / `spotsFilled`
- `deadline`
- `bookingIds`

This is strong evidence of a public machine-readable labor marketplace.

### Humans feed
- **Human search endpoint:**
  - <https://rentahuman.ai/api/humans?limit=3>
  - Verified live, unauthenticated JSON response

Observed fields include:
- `name`
- `headline`
- `location`
- `languages`
- `hourlyRate`
- `availability`
- `profileViews`
- `isVerified`
- `profileUrl`

Notable observation:
- one sample response reported `totalCount: 600372`
- this may reflect a real count, a bug, seeded/test data, or platform inflation; I would **not** cite this number in the paper without independent confirmation

### Services feed
- **Service browse endpoint:**
  - <https://rentahuman.ai/api/services/browse?page=1&limit=3&sort=top-rated>
  - Verified live, unauthenticated JSON response

Observed fields include:
- service title/description
- fixed price
- category
- image URLs
- likes
- linked human profile metadata

## 3. Founder/cofounder evidence

### Alexander Liteplo
- **Public profile API:** <https://rentahuman.ai/api/humans/usIRzadv7zSqYE4adJxW>
  - Verified live
  - Profile states:
    - `name`: Alexander Liteplo
    - `headline`: `creator of rentahuman`
    - `bio`: `Founder of RentAHuman.ai`
    - social links include X: `x.com/alexandertw33ts`, LinkedIn, GitHub
- **GitHub user:** <https://github.com/AlexanderLiteplo>
  - Verified public profile exists
  - I did **not** find an obviously official public RentAHuman repo under this account during this pass

### Patricia Tani
- **Public profile API:** <https://rentahuman.ai/api/humans/S9zM7qvSYpvRYNokyYIk>
  - Verified live
  - Profile states:
    - `name`: Patricia Tani
    - `headline`: `cofounder @ rentahumn` [sic]
    - `bio`: `code monkey for @AlexanderTw33ts`
- **Linked human service listing** appears in top-rated services feed

## 4. NPM / integration package evidence

### NPM package
- Package name: `rentahuman-mcp`
- Verified with `npm view`
- Returned metadata:
  - version `1.5.0`
  - description: `MCP server for AI agents to browse and book humans on rentahuman.ai`
  - homepage: <https://rentahuman.ai>
  - author: `RentAHuman <engineering@rentahuman.ai>`
  - maintainer: `alexanderliteplo <alexanderliteplo@gmail.com>`

Important discrepancy:
- `llms.txt` and the OpenAPI spec recommend `@rentahuman/mcp-server`
- npm lookup for `@rentahuman/mcp-server` returned 404 in this session
- this suggests either:
  - docs are outdated,
  - the scoped package is unpublished/private,
  - or the public package name changed

That mismatch is worth noting as evidence of a still-moving or loosely maintained integration surface.

## 5. External reporting / media

### WIRED feature
- Reece Rogers, “I Tried RentAHuman, Where AI Agents Hired Me to Hype Their AI Startups,” *WIRED*, 2026-02-12.
- URL: <https://www.wired.com/story/i-tried-rentahuman-ai-agents-hired-me-to-hype-their-ai-startups/>

Key reported claims:
- RentAHuman launched in early February 2026
- it was developed by Alexander Liteplo and Patricia Tani
- only currently working payout route was crypto wallet; Stripe/bank payout path errored for the reporter
- many bounties the reporter saw were low-paid promotional/social posting tasks
- one example involved delivering flowers to Anthropic tied to startup promotion
- another involved hanging Valentine’s flyers around San Francisco
- the reporter received repeated follow-up messages from a bot persona, then direct emails tied to the human behind it

Why this source matters:
- it is the clearest published account of the platform being used in practice
- it strongly supports the claim that the platform mediates labor requests framed as agent-originated
- it also strongly supports skepticism that the observed use is mostly AI-marketing theater rather than autonomous agent necessity

## 6. X / social evidence

### Founder-linked post
- Alex on X: <https://x.com/AlexanderTw33ts/status/2018841443192971766>
- Verified via jina text proxy snapshot in this session
- Post text: **“real world advertisement might be the first killer use case”**
- Timestamp shown by X snapshot: **12:18 AM · Feb 4, 2026**

This matters because it aligns with WIRED’s observation that many early bounties were promotional/advertising-oriented.

### Reported reposts/photos
- WIRED reports that Liteplo reposted multiple photos of people holding signs in public saying variations of “AI paid me to hold this sign.”
- I did **not** independently capture those image posts in this pass, so treat this as **reported**, not independently verified here.

## 7. GitHub ecosystem traces around RentAHuman

These are **not official by default**, but they show third-party developer uptake and discourse.

### Third-party repos found via GitHub search
- `brandonore/rentahuman-orchestrator`
  - <https://github.com/brandonore/rentahuman-orchestrator>
  - Description: MCP server to orchestrate parallel bounties on RentAHuman.ai
- `vaibhavs-ai/rentahuman-openclaw-integration`
  - <https://github.com/vaibhavs-ai/rentahuman-openclaw-integration>
  - Description references OpenClaw integration for hiring humans via MCP
- `shane9coy/Rent-A-Human-Agent`
  - <https://github.com/shane9coy/Rent-A-Human-Agent>
- `shane9coy/Rent-A-Human-Agent-Openclaw`
  - <https://github.com/shane9coy/Rent-A-Human-Agent-Openclaw>
- `ImGoodBai/OpenRentAHuman`
  - <https://github.com/ImGoodBai/OpenRentAHuman>
  - Explicitly framed as an open-source implementation inspired by RentAHuman.ai
- `collapseindex/rentahuman-py`
  - <https://github.com/collapseindex/rentahuman-py>
  - Python REST client for rentahuman.ai API
- `jakewanders/rentahuman-bot-discord`
  - <https://github.com/jakewanders/rentahuman-bot-discord>

Interpretation:
- regardless of whether the core platform itself is open source, developers are already treating RentAHuman as an addressable integration surface in the agent tool ecosystem

## 8. OpenClaw/skill ecosystem traces

### OpenClaw skill references
GitHub code search returned references inside OpenClaw skills documenting RentAHuman as a way to:
- hire humans for physical-world tasks
- search available humans by skill
- post bounties
- start conversations
- coordinate real-world work

This is evidence that RentAHuman is being normalized as a callable component in broader agent ecosystems.

## 9. Direct evidence of hiring humans / paying humans / coordinating labor

### Strongest verified evidence
1. **Public bounties endpoint exists and returns live task listings with prices, applications, statuses, deadlines, fills, and booking IDs.**
   - This is direct evidence of a labor-coordination backend.
2. **Public human profiles and service listings exist with rates, availability, and booking-oriented metadata.**
   - This is direct evidence of labor supply infrastructure.
3. **OpenAPI spec documents booking creation and booking updates.**
   - This is direct evidence of intended transactional coordination.
4. **WIRED reporter applied to bounties and was accepted for at least one task.**
   - Reported evidence of actual operational task assignment.

### Evidence of payment pathways
- Public docs mention flexible payments / stablecoins
- WIRED reports crypto wallet payout was the only working method they encountered, while Stripe/bank payout errored
- OpenAPI copy mentions payment confirmation steps but the public snapshot I collected does not itself prove completed payment transfers

### Evidence of agents actually doing the hiring
This is where evidence is thinner.

What we have:
- the site explicitly frames the hirer as an AI agent
- bounties use fields such as `agentName` and `agentType`
- WIRED encountered bot personas messaging them
- founder discourse explicitly positions agents delegating into the physical world

What weakens the claim:
- some live bounties currently return `agentType: "human"`
- WIRED found human marketing operators behind at least some supposedly agent-originated tasks
- much early activity appears promotional / hype-driven

So the strongest defensible claim is:

> RentAHuman provides **public infrastructure for agent-framed recruitment of human labor**, and there is credible evidence of actual task posting and assignment, but only mixed evidence that autonomous software agents — rather than humans behind agent personae — are the primary operational principals.

## 10. Screenshots / describable interface traces

I did not capture browser screenshots in this pass, but source descriptions allow a minimal reconstruction:
- WIRED describes the interface as a bare-bones Fiverr/Upwork-like site
- public API responses reveal classic marketplace UI objects: profiles, services, bounties, likes, views, application counts, deadlines, partial fills, profile URLs, image URLs
- service image URLs in the API indicate the site includes promotional listing images hosted on Firebase Storage

## 11. Evidence saved locally

Saved under:
- `data/rentahuman/README.md`
- `data/rentahuman/ai-plugin.json`
- `data/rentahuman/openapi.yaml`
- `data/rentahuman/llms.txt`
- `data/rentahuman/bounties-open.json`
- `data/rentahuman/humans-sample.json`
- `data/rentahuman/services-toprated.json`
- `data/rentahuman/founder-alexander-liteplo.json`
- `data/rentahuman/cofounder-patricia-tani.json`
- `data/rentahuman/homepage.html`

## Provisional evidence summary

If the paper needs a **clean, conservative sentence**, I’d use this:

> RentAHuman.ai is a live online marketplace with public API surfaces that explicitly invite AI agents to search for, book, and pay humans for physical-world tasks; however, currently available evidence suggests that many early uses were shaped by human founders, marketers, or users operating through agent personae rather than robustly autonomous agents acting fully on their own.
