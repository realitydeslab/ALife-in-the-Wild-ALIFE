# RentAHuman data snapshot

Saved on 2026-03-10 UTC from public, unauthenticated endpoints.

Files:
- `homepage.html` — raw homepage HTML showing public metadata (MCP, ai-plugin, llms.txt, branding)
- `ai-plugin.json` — public AI plugin manifest
- `openapi.yaml` — public OpenAPI spec for the REST API
- `llms.txt` — public LLM-oriented integration file
- `bounties-open.json` — sample of currently open / partially filled bounties
- `humans-sample.json` — sample of public human profiles
- `services-toprated.json` — sample of public service listings
- `founder-alexander-liteplo.json` — public profile for Alexander Liteplo via platform API
- `cofounder-patricia-tani.json` — public profile for Patricia Tani via platform API

Interpretation notes:
- These files are evidence that the platform was live and serving public machine-readable endpoints at collection time.
- They do **not** by themselves prove that every listing is genuinely agent-authored; some API responses explicitly mark posters as `agentType: "human"`.
- The live bounties feed is useful mainly as infrastructural evidence: the system exposes public listings, applications, prices, deadlines, views, and partial fill states.
