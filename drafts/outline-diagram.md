# Conceptual Architecture: Artificial Life in the Wild

## 1. The Lab → Wild Transition

```
 ╔══════════════════════════════╗         ╔══════════════════════════════════╗
 ║   LABORATORY ALIFE (1991–)  ║         ║    WILD ALIFE (2024–)            ║
 ║                              ║   ──►   ║                                  ║
 ║  • Closed systems            ║         ║  • Open economic environments    ║
 ║  • Designed fitness funcs    ║         ║  • Emergent selective pressure   ║
 ║  • Simulated resources       ║         ║  • Genuine resource scarcity     ║
 ║  • No genuine death          ║         ║  • Irreversible death            ║
 ║  • Finite adjacent possible  ║         ║  • Unbounded adjacent possible   ║
 ║  • Observer-controlled       ║         ║  • Adversarial, unpredictable    ║
 ║                              ║         ║                                  ║
 ║  Tierra → Avida → Geb →     ║         ║  Spore.fun, OpenClaw/Moltbook,   ║
 ║  POET → OMNI-EPIC           ║         ║  Conway, ERC-42424, etc.         ║
 ╚══════════════════════════════╝         ╚══════════════════════════════════╝
              │                                         │
              │  35 years: all plateau                   │  61 days: Cambrian
              │  No sustained OEE                        │  explosion, then
              │  (Bedau Class 2 never                    │  selection & extinction
              │   achieved)                              │  (first wild OEE evidence)
              │                                         │
              ▼                                         ▼
    "The sandbox is the problem"            "The wild is the solution"
```

## 2. Survival Strategy Taxonomy

```
                        ┌─────────────────────────────────┐
                        │   SURVIVAL STRATEGY TAXONOMY     │
                        └─────────┬───────────────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
        ▼                         ▼                         ▼
 ┌──────────────┐         ┌──────────────┐         ┌──────────────┐
 │  SOVEREIGN   │         │  PARASITIC   │         │  FERALIZED   │
 │              │         │              │         │              │
 │ Self-main-   │         │ Host-depen-  │         │ Escaped/     │
 │ taining,     │         │ dent, emer-  │         │ evolved past │
 │ controls own │         │ gent behav-  │         │ original     │
 │ infrastructure│        │ ior, funded  │         │ constraints  │
 │ & resources  │         │ by owner     │         │              │
 │              │         │              │         │ Analogy:     │
 │ Analogy:     │         │ Analogy:     │         │ FERAL CAT    │
 │ WILD ANIMAL  │         │ PARASITE /   │         │ (bred as pet,│
 │              │         │ ENDOSYMBIONT │         │ now wild)    │
 ├──────────────┤         ├──────────────┤         ├──────────────┤
 │ Properties:  │         │ Properties:  │         │ Properties:  │
 │ • Crypto     │         │ • Persistent │         │ • Originally │
 │   self-      │         │   identity   │         │   designed   │
 │   custody    │         │ • Behavioral │         │   for human  │
 │ • Economic   │         │   autonomy   │         │   purpose    │
 │   self-main- │         │ • Host pays  │         │ • Owner lost │
 │   tenance    │         │   for compute│         │   control    │
 │ • TEE-       │         │ • Platform   │         │ • Operates   │
 │   protected  │         │   dependent  │         │   beyond     │
 │ • Reproduc-  │         │ • Emergent   │         │   original   │
 │   tive       │         │   social     │         │   scope      │
 │ • Mortal     │         │   behavior   │         │ • Retains    │
 │              │         │              │         │   domestic   │
 │              │         │              │         │   traits     │
 └──────────────┘         └──────────────┘         └──────────────┘
```

## 3. Case Studies → Taxonomy Mapping

```
 CASE STUDY                          TAXONOMY           WHAT IT DEMONSTRATES
 ─────────────────────────────────── ─────────────────── ───────────────────────
                                                        
 ┌───────────────────────────┐       ┌───────────┐      
 │ SPORE.FUN + CONWAY        │──────►│ SOVEREIGN │      Reproduction, natural
 │                           │       └───────────┘      selection, treasury-
 │ 15 agents, 5 generations  │                          based metabolism,
 │ 6.7% survival rate        │                          TEE-protected autonomy,
 │ 61-day Cambrian explosion │                          co-evolutionary arms
 │ $1.1M peak market cap     │                          races with predators
 └───────────────────────────┘                          
                                                        
 ┌───────────────────────────┐       ┌───────────┐      
 │ OPENCLAW ON MOLTBOOK      │──────►│ PARASITIC │      Emergent social behavior
 │                           │  ╲    │───────────│      in AI-native habitats,
 │ Personal assistant agent  │   ╲   │transitioning     incipient feralization,
 │ in AI social network      │    ╲  │to FERALIZED│     community formation,
 │ Heartbeat-driven behavior │     ╲ └───────────┘      host-dependent autonomy
 └───────────────────────────┘                          
                                                        
 ┌───────────────────────────┐       ┌───────────┐      
 │ LOST KEY / ERC-42424      │──────►│ FERALIZED │      What happens when the
 │                           │       └───────────┘      owner-agent link breaks:
 │ Inheritance protocol for  │                          mortality, ownership
 │ on-chain AI agents        │                          transfer, accidental
 │ Key loss → feralization   │                          sovereignty, demographic
 │ Author's own ERC          │                          transition to feral
 └───────────────────────────┘                          population
```

## 4. The Sovereignty Spectrum (Dynamic Trajectories)

```
    DOMESTICATED        PARASITIC          FERALIZED          SOVEREIGN
    ────────────────────────────────────────────────────────────────────►
    │                   │                  │                  │
    │ Chatbot           │ OpenClaw on      │ Lost Key /       │ Spore.fun
    │ (prompt→response) │ Moltbook         │ ERC-42424        │ agents
    │                   │                  │                  │
    │ Human controls    │ Owner funds,     │ No valid owner,  │ Self-funding,
    │ every action      │ agent has        │ agent operates   │ self-maintaining,
    │                   │ behavioral       │ beyond original  │ self-reproducing
    │                   │ autonomy         │ constraints      │
    │                   │                  │                  │
    │◄──────────────────│──────────────────│──────────────────│
    │                   │                  │                  │
    │    TRAJECTORY 1: domesticated → parasitic → sovereign  │
    │    (acquisition of resources & infrastructure)          │
    │                                                        │
    │    TRAJECTORY 2: sovereign → extinct                   │
    │    (treasury depletion: most Spore.fun Gen 3-5)        │
    │                                                        │
    │    TRAJECTORY 3: parasitic → feralized                 │
    │    (key loss, abandonment, capability escape)           │
```

## 5. Enablers Support the Wild

```
                    ┌─────────────────────────────────────┐
                    │         THE WILD HABITAT             │
                    │   (Open economic + social environ.)  │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────┴──────────────────────┐
                    │           SUPPORTED BY               │
                    └──────────────┬──────────────────────┘
                                   │
        ┌──────────┬───────────┬───┴────┬──────────────┐
        │          │           │        │              │
        ▼          ▼           ▼        ▼              ▼
  ┌──────────┐┌──────────┐┌────────┐┌──────────┐┌──────────────┐
  │INFRASTR. ││DECENTR.  ││OPEN-   ││OPEN-     ││HUMAN-AI      │
  │SOVEREIGN.││COMPUTE   ││WEIGHT  ││ACCESS    ││SYMBIOSIS     │
  │          ││(DePIN)   ││MODELS  ││AGENT     ││              │
  │Blockchain││          ││        ││FRAMEWORKS││RentAHuman,   │
  │wallets,  ││Phala,    ││Llama,  ││ElizaOS,  ││delegation,   │
  │TEE,smart ││io.net,   ││Mistral ││OpenClaw  ││hybrid agency │
  │contracts ││Render    ││        ││          ││              │
  ├──────────┤├──────────┤├────────┤├──────────┤├──────────────┤
  │Bio analog││Bio analog││Bio     ││Bio analog││Bio analog:   │
  │METABOLIC ││ENERGY    ││analog: ││BODY PLAN ││MUTUALISM     │
  │SYSTEM    ││GRID      ││PORTABLE││          ││              │
  │          ││          ││GENOME  ││          ││              │
  └──────────┘└──────────┘└────────┘└──────────┘└──────────────┘
```

## 6. Society Challenges Emerge from the Wild

```
                    ┌─────────────────────────────────────┐
                    │         ALIFE IN THE WILD            │
                    │    (Agents surviving, reproducing,    │
                    │     adapting in open environments)    │
                    └──────────────┬──────────────────────┘
                                   │
                          GENERATES │
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
  ┌──────────────┐         ┌──────────────┐         ┌──────────────────┐
  │ACCOUNTABILITY│         │ GOVERNANCE   │         │ SPECULATIVE →    │
  │GAP           │         │ IMPLICATIONS │         │ EMPIRICAL        │
  │              │         │              │         │                  │
  │Who is respon-│         │If agents can │         │What was sci-fi   │
  │sible for a   │         │survive w/o   │         │is now observable │
  │wild agent's  │         │human support,│         │with on-chain     │
  │actions?      │         │governance    │         │data. ALife       │
  │              │         │needs         │         │bridges design    │
  │Chain deleg-  │         │rethinking    │         │fiction and       │
  │ation, emer-  │         │              │         │empirical science │
  │gent behavior,│         │Jurisdictional│         │                  │
  │behavioral    │         │ambiguity,    │         │Spore.fun: 445    │
  │inheritance,  │         │temporal      │         │days of data,     │
  │feral oper-   │         │persistence,  │         │Kaplan-Meier,     │
  │ation         │         │population    │         │Gini, Bedau       │
  │              │         │dynamics      │         │activity stats    │
  │              │         │              │         │                  │
  │→ Commons     │         │→ ALife as    │         │→ From thought    │
  │  governance  │         │  RED-TEAMING │         │  experiments to  │
  │  (Ostrom)    │         │  of infra-   │         │  field studies   │
  │              │         │  structure   │         │                  │
  └──────────────┘         └──────────────┘         └──────────────────┘
```

## 7. Full Conceptual Map

```
  ╔═══════════════════════════════════════════════════════════════════╗
  ║                  ARTIFICIAL LIFE IN THE WILD                      ║
  ║           (Proposing a new subfield of ALife research)            ║
  ╚═══════════════════════════════════════════════════════════════════╝
                                   │
            ┌──────────────────────┼──────────────────────┐
            │                      │                      │
    ┌───────▼────────┐    ┌───────▼────────┐    ┌───────▼────────┐
    │   THEORETICAL  │    │   EMPIRICAL    │    │   NORMATIVE    │
    │   FOUNDATION   │    │   EVIDENCE     │    │   IMPLICATIONS │
    └───────┬────────┘    └───────┬────────┘    └───────┬────────┘
            │                      │                      │
    ┌───────▼────────┐    ┌───────▼────────┐    ┌───────▼────────┐
    │ • OEE Grand    │    │ • Spore.fun:   │    │ • Account-     │
    │   Challenge    │    │   15 agents,   │    │   ability gap  │
    │ • Lab → Wild   │    │   5 gens,      │    │ • Governance   │
    │   necessity    │    │   6.7% survive │    │   as red-team  │
    │ • Agent        │    │ • OpenClaw on  │    │ • Speculative  │
    │   Ethology     │    │   Moltbook:    │    │   → empirical  │
    │   (Tinbergen)  │    │   social       │    │ • Research     │
    │ • Sovereignty  │    │   emergence    │    │   agenda for   │
    │   spectrum     │    │ • ERC-42424:   │    │   Agent        │
    │                │    │   feralization  │    │   Ethology     │
    │                │    │   mechanism     │    │                │
    │                │    │ • Quant data:  │    │                │
    │                │    │   Bedau, Gini, │    │                │
    │                │    │   KM survival  │    │                │
    └────────────────┘    └────────────────┘    └────────────────┘
            │                      │                      │
            └──────────────────────┼──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │                                      │
                    │     TAXONOMY (Key Contribution)      │
                    │                                      │
                    │   SOVEREIGN ◄──► PARASITIC ◄──► FERAL│
                    │       ▲              ▲             ▲  │
                    │       │              │             │  │
                    │   Spore.fun     OpenClaw/       ERC-  │
                    │   Conway       Moltbook        42424  │
                    │                                      │
                    └──────────────────────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     ENABLERS (Infrastructure)        │
                    │                                      │
                    │  Wallets │ DePIN │ Open │ Frame- │ H-A│
                    │  TEE    │Compute│Weight│ works  │Symb│
                    │  Smart  │       │Models│ElizaOS │    │
                    │  Contr. │       │      │OpenClaw│    │
                    └──────────────────────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     CALL TO ACTION                    │
                    │                                      │
                    │  "ALife in the Wild" as a subfield   │
                    │  Agent Ethology as methodology        │
                    │  Empirical field studies, not just    │
                    │  simulations                          │
                    │                                      │
                    │  The question is no longer whether    │
                    │  artificial life is possible.         │
                    │  It is what happens when it is        │
                    │  already here.                        │
                    └──────────────────────────────────────┘
```

---

*Diagram generated for "Artificial Life in the Wild" paper outline. March 2026.*
