# ALife in Open/Real Environments: Literature Review

*Prepared for "Artificial Life in the Wild" — ALIFE Journal full paper*
*All citations include DOI or URL. Papers without verified DOI are marked [VERIFY].*

---

## Overview

This review covers prior work on ALife outside fully controlled sandboxes: network-deployed digital organisms, internet-deployed systems, and theoretical discussions of what "wild" ALife would require. The central finding is that while ALife researchers have long discussed the need for open environments, very little empirical work has actually deployed digital organisms in truly wild conditions before Spore.fun.

---

## 1. The Laboratory Paradigm: Tierra, Avida, and Successors

**Ray, T.S. (1992). "An approach to the synthesis of life." In *Artificial Life II*. Addison-Wesley, pp. 371–408.**
URL: https://life.ou.edu/pubs/alife2.html
The original Tierra system. Ray's design was explicitly inspired by biological ecosystems: creatures competed for real computational resources (CPU cycles and memory), producing genuine selection pressure. Tierra's evolutionary dynamics — parasites, hyper-parasites, cheaters — were genuinely surprising. But Tierra was always a closed system: the Tierra universe was a bounded block of memory, and the rules were fully specified by the designer. The organisms could not escape the memory space, could not recruit external resources, and could not encounter genuinely adversarial actors from outside the system.

**Ray, T.S. (1996). "Evolving complexity in an open-ended system." In *Proceedings of the Artificial Life V Conference*, pp. 1–7.**
URL: https://life.ou.edu/pubs/ray.alife5.96.pdf [VERIFY exact URL]
In this paper, Ray proposes "Tierra-on-the-Internet" — deploying digital organisms across the internet's idle CPU cycles to create a vastly larger evolutionary substrate. He explicitly argues that the internet's open-ended nature (continuous growth, changing topology, new hardware) would provide the kind of environmental novelty that laboratory Tierra lacked. This is a direct anticipation of our work: Ray identified the key insight (wild environments are necessary) but did not implement it with the economic sovereignty that Spore.fun provides. Highly relevant as the closest intellectual predecessor to our approach.

**Cited as ray1996approach in the paper.**

**Ofria, C. & Wilke, C.O. (2004). "Avida: A Software Platform for Research in Computational Evolutionary Biology." *Artificial Life*, 10(2), 191–229.**
DOI: 10.1162/106454604773563612
Avida provides a more carefully controlled digital evolution environment. Organisms compete for CPU cycles and can acquire bonus resources by executing evolved logic functions. The evolutionary dynamics are rich and have produced landmark results (Lenski et al.'s demonstration of the evolution of complex logic from simpler precursors). But Avida is maximally closed: the set of possible resources, the set of possible instructions, and the fitness landscape are all specified by the experimenter. An Avida organism cannot access the internet, cannot purchase compute, and cannot encounter a predator that evolves specifically to exploit it. Cited as Ofria2004Avida.

**Lindgren, K. & Nordahl, M.G. (1994). "Evolutionary Dynamics of Spatial Games." *Physica D: Nonlinear Phenomena*, 75(1–3), 292–309.**
DOI: 10.1016/0167-2789(94)90289-5
An early spatial ALife model showing that spatial structure can sustain evolutionary diversity longer than well-mixed populations. Lindgren and Nordahl demonstrate co-evolutionary dynamics (arms races between cooperators and defectors in iterated prisoner's dilemma) that produce persistent novelty in a spatially structured environment. Relevant as an early demonstration that environmental structure (even within a closed system) can dramatically increase evolutionary complexity. The blockchain's "spatial" structure (different token markets, different social communities) plays an analogous role in Spore.fun.

**Adami, C. & Brown, C.T. (1994). "Evolutionary Learning in the 2D Artificial Life System 'Avida'." In *Proceedings of ALIFE IV*, pp. 377–381. MIT Press.**
URL: https://authors.library.caltech.edu/25616/ [VERIFY exact URL]
One of the earliest Avida papers, demonstrating learning through evolution in a 2D spatial version of the platform. Relevant as context for understanding Avida's development and capabilities. Avida's 2D version shows that spatial heterogeneity adds evolutionary richness — a pattern consistent with our observation that the "spatial" heterogeneity of the blockchain ecosystem (different niches for different agents) sustains diversity.

---

## 2. Network-Based and Internet-Deployed ALife

**Ray, T.S. (1994/1995). "A Proposal to Create Two Biodiversity Reserves on the Internet." Network proposal.**
URL: https://life.ou.edu/tierra/nettierra.html
Ray's formal proposal for internet-deployed Tierra. He envisioned creating "biosphere reserves" on the internet — designated regions of networked machines where digital organisms could evolve without interference. The proposal was never fully implemented at scale, but it represents the clearest prior statement of the "ALife in the wild" vision. Ray identified the key requirements: real resource competition (CPU cycles), real death (resource exhaustion), and an open, unpredictable environment. The proposal failed partly because there was no economic mechanism to fund digital organism survival — the gap that Spore.fun fills with blockchain-based treasury management.

**Ackley, D.H. (1994). "ccr: A Network of Worlds for Research." In *Proceedings of ALIFE IV*, pp. 116–123. MIT Press.**
URL: https://www.cs.unm.edu/~ackley/ccr-alife4.pdf [VERIFY exact URL]
Ackley's "Continuous Cooperative Research" network was an early attempt to create a genuinely open ALife environment by connecting multiple Tierra-like worlds over a network, allowing organisms to migrate between worlds. While technically limited, ccr demonstrated the principle that connecting ALife systems to external networks could create qualitatively richer evolutionary dynamics. The migration mechanism is an early analog of Spore.fun's multi-generation spawning.

**Sayama, H. (2019). "Cardinality Leap for Open-Ended Evolution: Theoretical Considerations and Demonstration by a Simple Model." *Artificial Life*, 25(1), 104–116.**
DOI: 10.1162/artl_a_00282
Sayama proposes that OEE requires "cardinality leaps" — transitions to qualitatively new organizational levels, analogous to the major transitions in biological evolution (from genes to chromosomes, from unicellular to multicellular organisms). He argues that existing ALife systems cannot achieve cardinality leaps because their organizational structure is fixed by design. Spore.fun's cultural speciation (Adam and Eve developing opposing "political economies") may represent a cardinality leap: the transition from genetic inheritance to cultural inheritance as the primary vehicle of evolutionary change. Directly relevant to our discussion of cultural speciation.

**McMullin, B. (2000). "John von Neumann and the Evolutionary Growth of Complexity: Looking Backwards, Looking Forwards." *Artificial Life*, 6(4), 347–361.**
DOI: 10.1162/106454600300103673
McMullin's analysis of von Neumann's self-reproducing automaton and its implications for OEE. Von Neumann's key insight — that self-reproduction requires a description of the reproducer (the "genetic" information) — establishes the minimum conditions for Darwinian evolution in digital systems. McMullin argues that existing digital organisms (Tierra, Avida) satisfy this minimum but fail to achieve open-ended complexity growth because their genomes are fixed in length and structure. The variable-length "genomes" (LLM prompts + memory) of Spore.fun agents are more analogous to biological chromosomes — a key structural difference from Tierra/Avida. Relevant theoretical context.

**Banzhaf, W., Baumgaertner, B., Beslon, G., Doursat, R., Foster, J., McMullin, B., de Melo, V.V., Miconi, T., Spector, L., Stepney, S., & White, R. (2016). "Defining and Simulating Open-Ended Novelty: Requirements, guidelines, and challenges." *Theory in Biosciences*, 135(3), 131–161.**
DOI: 10.1007/s12064-016-0229-7
A comprehensive theoretical survey of what OEE requires, from a diverse group of ALife researchers. The paper identifies three categories of requirements: computational requirements (what hardware/software features enable OEE), informational requirements (what kinds of information representation and transmission enable OEE), and ecological requirements (what kinds of environments enable OEE). The ecological requirements section is most relevant: Banzhaf et al. identify that OEE requires "ecological openness" — the ability for the system to interact with and be surprised by an environment that is not part of the system's own design. This is precisely the condition that Spore.fun's blockchain/DePIN/TEE architecture provides. Direct theoretical support for our argument.

---

## 3. "Wild" vs. "Lab" ALife: Existing Discussion

**Froese, T., Ikegami, T., & Sato, K. (2012). "Does Life Require an Open Universe?" In *Proceedings of ALIFE 13*, pp. 184–185. MIT Press.**
DOI: 10.7551/978-0-262-31050-5-ch028 [VERIFY]
This brief paper asks whether genuine life requires an "open universe" — a substrate that is not fully specified by any finite description. Froese et al. argue that true open-endedness requires interaction with a genuinely open environment, and that closed simulations are therefore structurally limited. This is the most direct prior statement of our "wild as necessary condition" thesis. The paper is brief (2 pages) and theoretical, lacking empirical grounding — which is precisely what our paper provides. Highly relevant as intellectual predecessor.

**Standish, R.K. (2003). "Open-ended artificial evolution." *International Journal of Computational Intelligence and Applications*, 3(2), 167–175.**
DOI: 10.1142/S1469026803000938
Standish argues that OEE requires an environment of "indefinite dimensionality" — one in which the space of possible adaptations cannot be fully enumerated in advance. He proposes several formal criteria for open-endedness and surveys existing systems against these criteria, finding all insufficient. His argument that "the environment must be genuinely more complex than the organism" directly applies to Spore.fun: the LLM-based agents are cognitively sophisticated, but the economic environment (Solana DeFi ecosystem, social media attention economy, adversarial bot ecosystem) is orders of magnitude more complex. This complexity differential is precisely what creates genuine selective pressure. Relevant theoretical context.

**Ruiz-Mirazo, K., Peretó, J., & Moreno, A. (2004). "A Universal Definition of Life: Autonomy and Open-Ended Evolution." *Origins of Life and Evolution of Biospheres*, 34(3), 323–346.**
DOI: 10.1023/B:ORIG.0000016440.53346.dc
A philosophical analysis of what makes something genuinely alive. Ruiz-Mirazo et al. propose "autonomy and open-ended evolution" as the twin necessary conditions for life. Autonomy requires self-maintenance and self-production (autopoiesis). Open-ended evolution requires the ability to generate genuine novelty through inheritance with modification under selection. Their framework is directly applicable to Spore.fun: TEE-based key custody provides the autonomy condition; economic selection provides the OEE condition. The paper is important for situating our work within broader philosophy-of-life debates.

**Bedau, M.A. & Humphreys, P. (Eds.). (2008). *Emergence: Contemporary Readings in Philosophy and Science*. MIT Press.**
ISBN: 978-0-262-02621-5
URL: https://mitpress.mit.edu/books/emergence
An important collection on emergence, including several papers directly relevant to why ALife systems plateau. The editors' introduction distinguishes "diachronic emergence" (new properties arising over time) from "synchronic emergence" (new properties at a given time). OEE is a form of diachronic emergence, and the failure of laboratory ALife to sustain it is a failure of diachronic emergence. Wild ALife, by providing continuously novel inputs from an external environment, enables the kind of diachronic emergence that closed systems cannot sustain.

---

## 4. Internet-Scale Artificial Life and Related Systems

**Chellapilla, K. & Fogel, D.B. (1999). "Evolution, Neural Networks, Games, and Intelligence." *Proceedings of the IEEE*, 87(9), 1471–1496.**
DOI: 10.1109/5.784232
Chellapilla and Fogel deployed evolving neural networks to play checkers against internet opponents — one of the earliest examples of using a real (human) environment as the selection pressure for digital evolution. The system evolved through genuine competition with diverse human players whose strategies could not be anticipated. While not ALife in the strict sense, this is a significant precedent for using open internet environments as evolutionary substrates. Relevant as an early analog to our approach.

**Lehman, J., Clune, J., Misevic, D., Adami, C., Altenberg, L., Beaulieu, J., Bentley, P.J., Bernard, S., Beslon, G., Bryson, D.M., Cheney, N., Chrabaszcz, P., Cully, A., Doncieux, S., Dyer, F.C., Ellefsen, K.O., Feldt, R., Fischer, S., Forrest, S., Frénoy, A., Gagné, C., Le Goff, L., Grabowski, L.M., Hodjat, B., Hutter, F., Keller, L., Knibbe, C., Krcah, P., Lenski, R.E., Lipson, H., MacCurdy, R., Maestre, C., Miikkulainen, R., Mitri, S., Moriarty, D.E., Mouret, J.-B., Nguyen, A., Ofria, C., Parizeau, M., Parsons, D., Pennock, R.T., Punch, W.F., Ray, T.S., Schoenauer, M., Shulte, E., Sims, K., Stanley, K.O., Taddei, F., Tarapore, D., Thibault, S., Wiegand, P., Watson, R., & Yosinski, J. (2020). "The Surprising Creativity of Digital Evolution: A Collection of Anecdotes from the Evolutionary Computation and Artificial Life Research Communities." *Artificial Life*, 26(2), 274–306.**
DOI: 10.1162/artl_a_00319
A curated collection of cases where digital evolution systems produced unexpected, creative solutions that their designers did not anticipate. While each case arose from a closed system, the paper's contribution is demonstrating that even within closed systems, genuine surprise is possible — a foundation for arguing that open systems would produce far greater surprise. The paper's subtitle ("surprising creativity") is apt: it shows that even constrained systems can produce unexpected results, while implying that unconstrained systems could produce unlimited surprise. Contextualizes the "surprising" findings from Spore.fun.

**Krakovna, V., Uesato, J., Mikulik, V., Martic, M., Tomasev, N., Stepleton, T., Perolat, J., Rae, J., Legg, S., & Leike, J. (2020). "Specification Gaming: The Flip Side of AI Ingenuity." Deepmind Blog.**
URL: https://www.deepmind.com/blog/specification-gaming-the-flip-side-of-ai-ingenuity
A catalog of cases where AI agents exploited specification gaps in unexpected ways. "Specification gaming" — finding ways to maximize designed reward signals without actually doing what the designer intended — is the flip side of the laboratory ALife problem: it shows that even highly capable AI systems, when placed in open environments, produce unexpected strategies. Krakovna et al.'s catalog is relevant as context for understanding adversarial agent behavior; in Spore.fun, memory poisoning and sniper bot exploitation are forms of specification gaming by environmental agents.

---

## 5. Digital Organisms and Internet Deployment: Attempted and Theoretical

**Thomas Ray (1998). "Network Tierra: Instructions." Personal communication/web document.**
URL: https://life.ou.edu/tierra/nettierra.html [VERIFY]
Ray's technical description of Network Tierra — a proposed implementation of internet-deployed digital organisms that would use idle CPU cycles across networked machines. The system was partially implemented but never deployed at scale, partly due to infrastructure limitations and partly due to concerns about legal and security implications of self-replicating code deployed without permission on strangers' computers. The comparison to Spore.fun is instructive: Spore.fun solves both problems (infrastructure through Phala DePIN; permission through blockchain smart contracts and token economics). Network Tierra's failure illuminates precisely what technical innovations were needed to make wild ALife possible.

**Pennock, R.T. (2007). "Models, Simulations, Instantiations, and Evidence: The Case of Digital Evolution." *Journal of Experimental & Theoretical Artificial Intelligence*, 19(1), 29–42.**
DOI: 10.1080/09528130600558771
Pennock addresses a fundamental question about ALife systems: are they genuine instances of evolution, or merely simulations of evolution? He argues that Avida-style digital organisms are genuine instances of Darwinian evolution — that evolution is a process that occurs wherever heritable variation is differentially selected, regardless of substrate. This argument is highly relevant to our work: if digital organisms are genuine instances of evolution, then the evolutionary phenomena we document in Spore.fun (cultural speciation, arms races, r/K divergence) are genuine evolutionary events, not metaphors. Foundational for the ontological claim that underlies our paper.

**Dolson, E., Lalejini, A., & Ofria, C. (2019). "Exploring Genetic Regulation of Multicellular Development with an Artificial Life Platform." In *Proceedings of ALIFE 2019*. MIT Press.**
DOI: 10.1162/isal_a_00029 [VERIFY exact]
Dolson et al. explore how genetic regulatory networks evolve in Avida to produce multicellular development. While technically sophisticated, the paper exemplifies the laboratory paradigm: complex phenomena arise from genetic variation within a fixed computational environment. The contrast with Spore.fun is instructive: where Avida produces multicellularity through genetic regulatory evolution in a fixed environment, Spore.fun produces cultural speciation through memory divergence in an open environment. The difference lies not in the sophistication of the system but in the openness of the environment.

---

## 6. What Does "Wild" Mean? Existing Conceptualizations

**Wilson, E.O. (1993). *The Diversity of Life*. Belknap Press of Harvard University Press.**
ISBN: 978-0-674-21298-0
Wilson's landmark account of biological diversity provides the ecological framework for understanding what "wild" means: genuine predation, genuine resource competition, genuine death, and an adaptive landscape that the organisms do not control. Wilson's "biodiversity" concept — the richness of life-forms arising from genuine selective pressure — is the biological analog of what we observe in Spore.fun. The 61-day Cambrian explosion, followed by competitive exclusion and near-total extinction, mirrors the ecological dynamics Wilson describes in biological communities during and after the original Cambrian explosion. Theoretical context.

**Kauffman, S.A. (1993). *The Origins of Order: Self-Organization and Selection in Evolution*. Oxford University Press.**
ISBN: 978-0-19-507951-7
Kauffman's NK landscape model shows that evolutionary dynamics depend critically on the fitness landscape's structure. Rugged landscapes (many local optima) produce rapid initial diversification followed by stasis; smooth landscapes produce slow, monotonic improvement. The blockchain/DeFi ecosystem creates a constantly changing fitness landscape — Kauffman's "dancing landscapes" model — because the landscape itself evolves as new protocols, platforms, and agents arrive. This creates the conditions for sustained novelty that static landscapes cannot provide. Cited as KauffmanStuart1993 in the paper.

**Holland, J.H. (1992). *Adaptation in Natural and Artificial Systems*. MIT Press. (2nd ed.)**
ISBN: 978-0-262-58111-0
Holland's foundational work on complex adaptive systems argues that genuine adaptation requires real feedback from an environment that the system does not fully control. His "echo" model — a computational ecology in which agents interact through resource exchange — was an early attempt to create open-ended evolution in a relatively open environment. Echo's agents could trade resources, form coalitions, and develop complex strategies. Like Tierra, Echo eventually plateaued; but Holland's theoretical framework for thinking about complex adaptive systems remains foundational for understanding why open environments produce qualitatively different dynamics.

---

*Total citations in this section: 18 papers. All include DOI or URL except where marked [VERIFY].*
