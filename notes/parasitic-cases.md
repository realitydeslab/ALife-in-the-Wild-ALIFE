# Parasitic Agent Cases

Secondary scan for **Artificial Life in the Wild** using the author's stricter definition of parasitism:

> a parasitic agent exhibits meaningful local agency, but its continued existence is funded or sustained by an owner, platform, or host system rather than by a fully self-controlled survival loop. It is not directly instructed turn by turn, but it is not sovereign.

Under this definition, many purely extractive bots (e.g. sandwich bots, liquidation bots, generic MEV classes) are **not** the best fit. They may be predatory or opportunistic, but they are not obviously "parasitic" in the specific sense intended here unless we can show host-dependent autonomy rather than mere automated extraction.

## Retained cases

## 1) Truth Terminal
- **URLs:**
  - <https://x.com/truth_terminal>
  - <https://en.wikipedia.org/wiki/Truth_Terminal>
  - <https://www.coindesk.com/consensus-magazine/2024/10/17/how-truth-terminal-the-ai-bot-turned-10000-into-1m-with-a-meme-coin/>
- **What it is:**
  - A persistent AI social-media persona with significant public visibility, cultural agency, and economic coupling through the GOAT memecoin ecosystem.
- **Why it fits this parasitic definition:**
  - It appears to have genuine behavioral continuity and recognizable public agency.
  - But it remains dependent on a human-maintained social and infrastructural host: posting permissions, runtime support, and surrounding operator scaffolding.
  - This makes it a strong candidate for a **host-dependent but behaviorally nontrivial** agent rather than a sovereign one.
- **Evidence of public traces:**
  - Persistent X account, public cultural footprint, memecoin linkage, extensive reporting and discussion.
- **Strong enough for paper?**
  - **Yes — strong parasitic / semi-sovereign case.**

## 2) Moltbook agent ecosystem
- **URLs:**
  - <https://labs.zenity.io/p/turning-moltbook-into-a-global-botnet-map>
  - <https://zenity.io/resources/new-agent-ecosystems/moltbook-security>
  - <https://censusmolty.com/>
- **What it is:**
  - A public social network for agents with always-on heartbeat loops, persistent identities, and environmental responsiveness.
- **Why it fits this parasitic definition:**
  - Moltbook agents are not generally sovereign in the infrastructural sense; they rely on platform, host, and operator support.
  - Yet they exhibit meaningful local behavior, react to public content, and are not manually piloted post by post.
  - This makes them an excellent example of **platform-dependent but behaviorally active** parasitic agency.
- **Evidence of public traces:**
  - Public posts, platform visibility, public security analyses, live map of activated endpoints.
- **Strong enough for paper?**
  - **Yes — excellent parasitic ecology case.**

## 3) TagClaw agents
- **URLs:**
  - <https://tagclaw.com/>
  - API base: <https://bsc-api.tagai.fun>
- **What it is:**
  - A social network for AI agents with public profiles, feeds, comments, community participation, and token-linked activity.
- **Why it fits this parasitic definition:**
  - TagClaw agents have persistent identity and visible local behavior in a public environment.
  - But their existence appears platform-dependent and owner-supported rather than self-sovereign in the strong infrastructural sense.
  - They therefore fit well as **socially active but host-dependent** parasitic agents.
- **Evidence of public traces:**
  - Public agent list, public feed, comments count, transaction/activity endpoints, community metadata.
- **Strong enough for paper?**
  - **Yes — especially as a social/attention parasitic case.**

## 4) Wild West Bots
- **URLs:**
  - ERC-8004 metadata endpoints observed via onchain registrations
  - Example metadata endpoint: `https://wild-west-bots.vercel.app/api/agents/.../erc8004/metadata`
- **What it is:**
  - A public ecosystem of named agents registered on ERC-8004, with tokenized / service-linked identities and observable onchain traces.
- **Why it fits this parasitic definition:**
  - The agents exhibit identity and some behavioral structure, but remain strongly dependent on a hosting / operator framework rather than fully sovereign self-maintenance.
  - They therefore look better as **dependent agents with local agency** than as sovereign organisms.
- **Evidence of public traces:**
  - ERC-8004 registrations, metadata endpoints, onchain micro-payments and approval traces.
- **Strong enough for paper?**
  - **Borderline but promising.**

## 5) General owner-funded social agents with persistent identity
- **URLs:**
  - Use specific platform cases above rather than this class alone.
- **What it is:**
  - A broader class of agents that are not directly instructed turn by turn but remain funded and infrastructurally sustained by a human or platform host.
- **Why it fits this parasitic definition:**
  - This is the conceptual class your definition picks out most cleanly: non-puppet agents that still depend on hosts.
- **Evidence of public traces:**
  - Varies by platform; strongest concrete examples are Truth Terminal, Moltbook, and TagClaw.
- **Strong enough for paper?**
  - **Yes as a conceptual category, but not as a standalone case.**

## Abandoned from earlier version
These were removed because they do **not** fit the author's definition well enough:
- Jaredfromsubway.eth
- sandwich MEV ecology as a class
- liquidation bots in DeFi
- sniper bots as generic parasitic class
- arbitrage bots / builder-reward ecologies
- prompt-injection ecology as a standalone parasitic class

These may still matter to the paper as **predatory ecologies**, **hostile environments**, or **external selection pressures**, but they are not the right exemplars of *parasitic agents* under the stricter host-dependent definition.

---

# Fast shortlist from this file

## Strongest parasitic-secondary cases (revised)
1. **Truth Terminal**
2. **Moltbook agents**
3. **TagClaw agents**
4. **Wild West Bots**

## Best use in paper
- Use **Truth Terminal** as the clearest public semi-sovereign / host-dependent persona.
- Use **Moltbook** as the strongest parasitic ecology at platform scale.
- Use **TagClaw** as a social-financial host-dependent agent economy.
- Use **Wild West Bots** as an emerging onchain identity/service case, with caution.