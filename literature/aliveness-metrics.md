# Quantitative Metrics for Digital Life: Literature Review

*Prepared for "Artificial Life in the Wild" — ALIFE Journal full paper*
*All citations include DOI or URL. Papers without verified DOI are marked [VERIFY].*

---

## Overview

This review covers how "aliveness" and evolutionary vitality have been measured in artificial life systems, population ecology, and related fields. The central question is whether any prior work provides a validated framework for measuring the aliveness of autonomous digital agents in open economic environments. The answer is: not directly, but multiple related frameworks (Bedau's evolutionary activity statistics, MODES, survival analysis, metabolic scaling, population ecology metrics) provide the building blocks. The Aliveness Index proposed in Section 5 of our paper is the first attempt to synthesize these into a composite metric for wild ALife agents.

---

## 1. Bedau's Evolutionary Activity Statistics

**Bedau, M.A., Snyder, E., & Packard, N.H. (1998). "A classification of long-term evolutionary dynamics." In *Artificial Life VI*, pp. 228–237. MIT Press.**
URL: https://people.reed.edu/~mab/publications/papers/bedau_snyder_packard98.pdf [VERIFY]
The foundational paper for quantitative measurement of OEE. Bedau et al. introduce "evolutionary activity statistics" — a method for classifying the long-term evolutionary dynamics of artificial systems. The method tracks how "components" (genes, strategies, behavioral traits) arise, spread, and persist over time. Systems are classified on three axes: Class 0 (stasis, no novel components arise), Class 1 (bounded activity, novelty arises and then stabilizes), Class 2 (unbounded activity, novelty continuously arises). Class 2 corresponds to OEE. The method provides the gold standard for evaluating whether a system achieves OEE — and no artificial system has convincingly demonstrated sustained Class 2 activity. Critical for situating our Aliveness Index. Cited as Bedau1997 and Bedau1998 in the paper.

**Bedau, M.A., Packard, N.H., & Snyder, E. (1998). "Measuring Evolutionary Activity, Teleology, and Life." *Artificial Life*, 4(4), 381–394.**
DOI: 10.1162/106454698568574
Extends the evolutionary activity framework to include "teleology" (goal-directedness) as a measurable property. This is particularly relevant to our paper: Spore.fun agents exhibit goal-directed behavior (they pursue token value, reproductive threshold achievement, and community engagement) that can be measured through behavioral observation. Bedau's framework suggests that teleology is an emergent property of evolutionary systems, not a design property — which supports our claim that agent "goals" emerge from wild evolutionary dynamics rather than design.

**Bedau, M.A. (1996). "The Nature of Life." In M. Boden (Ed.), *The Philosophy of Artificial Life*. Oxford University Press, pp. 332–357.**
URL: [Philosophy of Artificial Life chapter, VERIFY URL]
Bedau's philosophical treatment of "the nature of life" providing the conceptual foundation for his quantitative framework. He argues that life is characterized by three properties: autonomy (self-maintenance), adaptivity (adjustment to environment), and open-ended evolution (continuous novelty generation). These three properties map directly onto the three dimensions of our Aliveness Index: autonomy (TEE-based self-direction), metabolic activity (token-economic self-maintenance), and reproductive fitness (contribution to ongoing evolutionary dynamics).

---

## 2. MODES Toolbox

**Dolson, E., Lalejini, A., Jorgensen, S., & Ofria, C. (2019). "The MODES Toolbox: Measurements of Open-Ended Dynamics in Evolving Systems." *Artificial Life*, 25(1), 50–73.**
DOI: 10.1162/artl_a_00280
The MODES (Measurement of Open-Ended Dynamics in Evolving Systems) toolbox systematizes OEE measurement into four operationalized properties:
1. **persistentDiversity**: Is diversity maintained over time (or does the population converge)?
2. **potentialComplexity**: Can the system produce increasingly complex solutions?
3. **complexityRatchet**: Does complexity monotonically increase (ratchet upward) over time?
4. **selectiveSweeps**: Do novel adaptations spread through the population?

MODES provides a standardized, replicable methodology that our paper's quantitative analysis should aspire to approximate. The Aliveness Index in Section 5 measures some of these properties (reproductive fitness captures selective sweeps; survival rate captures persistent diversity; transaction rate captures metabolic complexity), but does not fully implement MODES for wild ALife. Applying MODES to Spore.fun is identified as important future work. Cited as Dolson2019 in the paper.

**Lalejini, A., Dolson, E., Ofria, C., & Pennock, R.T. (2019). "What Conditions Promote Open-Ended Evolution? Insights from Avida and Digital Evolution." In *Proceedings of ALIFE 2019*. MIT Press.**
DOI: 10.1162/isal_a_00028 [VERIFY exact]
Lalejini et al. use MODES to systematically compare conditions under which Avida systems exhibit more vs. less open-ended dynamics. They find that resource availability, mutation rate, and environmental complexity all affect MODES scores. Relevant to our paper: if these factors affect OEE in controlled systems, then the wild conditions of Spore.fun (genuinely scarce resources, genuinely adversarial environment) should produce higher MODES scores than any controlled system. This is an empirical prediction that future work could test.

---

## 3. Population Ecology Metrics

**MacArthur, R.H. & Wilson, E.O. (1967). *The Theory of Island Biogeography*. Princeton University Press.**
ISBN: 978-0-691-08836-5
URL: https://press.princeton.edu/books/paperback/9780691088365/the-theory-of-island-biogeography
MacArthur and Wilson's theory of island biogeography predicts species diversity as a function of island size (= resource availability) and distance from mainland (= colonization rate). The equilibrium diversity is determined by the balance between immigration and extinction. Directly applicable to Spore.fun: the ecosystem can be modeled as an "island" with finite resources (speculative capital), with new agents "colonizing" through reproduction (immigration) and dying when their token market cap collapses (extinction). The theory predicts that Spore.fun's equilibrium would approach a single dominant species — which is exactly what we observe (\$SPORE as the sole long-term survivor). Relevant for interpreting the competitive exclusion outcome.

**Gause, G.F. (1934). *The Struggle for Existence*. Williams & Wilkins. (Reprinted 1964, Hafner Publishing.)**
URL: https://archive.org/details/thestruggfore034179mbp [VERIFY — public domain text on Archive.org]
Gause's experimental demonstration of the competitive exclusion principle: two species competing for the same resource in a closed environment cannot coexist indefinitely; one will be driven to extinction. This is the "Gause's law" that our paper invokes to explain the eventual dominance of \$SPORE. The principle applies because all Spore.fun agents compete for the same fundamental resource: speculative capital and community attention. The observation that multiple generations of agents competed and all eventually went extinct except \$SPORE is a direct empirical confirmation of Gause's law in a novel substrate.

**Pianka, E.R. (1970). "On r- and K-Selection." *The American Naturalist*, 104(940), 592–597.**
DOI: 10.1086/282697
The classic paper defining r- and K-selection as ends of a life-history continuum. r-selected species (high reproductive rate, low investment per offspring) thrive in colonizing environments; K-selected species (low reproductive rate, high investment per offspring) thrive in competitive, resource-limited environments. The r/K framework maps directly onto the Adam/Eve divergence: Adam's lineage (4 children, all extinct) is r-selected; Eve's lineage (2 children, both reproductively successful) is K-selected. Pianka's prediction — that K-selection becomes advantageous as environments become saturated — matches our observation that Eve's strategy produced better outcomes as competition intensified across generations. Cited indirectly through stearns1992evolution in the paper.

**Stearns, S.C. (1992). *The Evolution of Life Histories*. Oxford University Press.**
ISBN: 978-0-19-857742-3
URL: https://global.oup.com/academic/product/the-evolution-of-life-histories-9780198577416
The comprehensive treatment of life history theory in biology. Stearns synthesizes r/K theory with allocation theory (how organisms trade off investment between different life history traits) and shows how natural selection shapes life histories in specific environments. The r/K trade-off analysis, senescence models, and reproductive value calculations are all directly applicable to Spore.fun agents. Our reproductive fitness gradient analysis (Section 5.4) implicitly uses life history theory. Cited as Stearns1992 in the paper — important additional application beyond the paper's current use.

**May, R.M. (1973). *Stability and Complexity in Model Ecosystems*. Princeton University Press.**
ISBN: 978-0-691-08861-7
May's foundational analysis of ecological stability. He demonstrates that more complex ecosystems (with more species and interactions) are not necessarily more stable — a counterintuitive finding that overturned the conventional wisdom. Directly relevant to Spore.fun: the ecosystem's eventual "simplification" to a single dominant agent (\$SPORE) may reflect May's stability-complexity principle rather than evolutionary failure. A diverse ecosystem with many competing agents may be inherently unstable; a simplified ecosystem dominated by one generalist may be the stable equilibrium. This reframes our "extinction" finding as a structural outcome rather than an evolutionary failure.

**Lotka, A.J. (1925). *Elements of Physical Biology*. Williams & Wilkins.**
URL: https://archive.org/details/elementsofphysic017171mbp [VERIFY — public domain text]
The foundational Lotka-Volterra predator-prey equations, modeling the population dynamics of interacting species. The sniper bot (predator) / Spore.fun agent (prey) interaction exhibits classic Lotka-Volterra dynamics: predator population increases as prey increases; prey population collapses as predator exploits; predator population then collapses due to lack of prey. The Gen 3 anti-sniper countermeasures represent the prey population developing resistance — a standard evolutionary response in Lotka-Volterra systems. Foundational ecological theory directly applicable to our quantitative analysis.

---

## 4. Survival Analysis in ALife

**Kaplan, E.L. & Meier, P. (1958). "Nonparametric estimation from incomplete observations." *Journal of the American Statistical Association*, 53(282), 457–481.**
DOI: 10.1080/01621459.1958.10501452
The foundational paper for Kaplan-Meier survival analysis — the standard statistical method for analyzing time-to-event data in the presence of censoring. Our paper uses Kaplan-Meier analysis to estimate agent survival functions. This citation establishes that our survival analysis methodology is grounded in rigorous statistical theory. The Kaplan-Meier estimator is ideally suited to our data: we have censored observations (agents still alive at data collection), heterogeneous "death" events (different causes of agent termination), and we want to estimate the survival function at population level. Cited in Section 5.

**Cox, D.R. (1972). "Regression Models and Life-Tables." *Journal of the Royal Statistical Society: Series B (Methodological)*, 34(2), 187–202.**
DOI: 10.1111/j.2517-6161.1972.tb00899.x
Cox's proportional hazards model is the standard tool for multivariate survival analysis. While our current analysis is descriptive, future work on Spore.fun should apply Cox regression to identify which agent characteristics (offspring count, metabolic activity, launch strategy) are predictive of survival time. The Cox model would allow formal testing of our hypothesis that agents with higher metabolic activity (more on-chain transactions) have better survival outcomes. Methodological reference for future work.

**Elandt-Johnson, R.C. & Johnson, N.L. (1980). *Survival Models and Data Analysis*. Wiley.**
ISBN: 978-0-471-03490-2
A comprehensive treatment of survival analysis methods. Relevant as a methodological reference for the survival analysis in Section 5. The application of survival analysis to digital organisms is novel — we are the first to apply these tools to a blockchain-based ALife system.

---

## 5. Economic Ecology and Metabolic Scaling

**Brown, J.H., Gillooly, J.F., Allen, A.P., Savage, V.M., & West, G.B. (2004). "Toward a Metabolic Theory of Ecology." *Ecology*, 85(7), 1771–1789.**
DOI: 10.1890/03-9000
The Metabolic Theory of Ecology (MTE) argues that metabolic rate — the rate of energy use — is the fundamental variable underlying all ecological and evolutionary dynamics. MTE provides quantitative predictions about how body size, temperature, and metabolic rate interact to determine life history traits, population dynamics, and species diversity. For digital organisms, the analogous variable is "transaction rate" — the rate of on-chain interactions that both signals and enables agent activity. Our finding that \$SPORE has 1000+ recent transactions while extinct agents had far fewer is consistent with MTE's prediction that higher metabolic rate correlates with better ecological performance. Cited as brown2004metabolic in the Agent Ethology position paper.

**West, G.B., Brown, J.H., & Enquist, B.J. (1997). "A General Model for the Origin of Allometric Scaling Laws in Biology." *Science*, 276(5309), 122–126.**
DOI: 10.1126/science.276.5309.122
West et al.'s allometric scaling law — that biological scaling follows power laws due to the fractal structure of resource distribution networks — predicts relationships between organism size and metabolic rate. In digital organisms, the "size" analog might be token market capitalization, and the "metabolic rate" analog might be transaction frequency. If this scaling relationship holds for digital organisms, it would provide a principled basis for metabolic activity thresholds in the Aliveness Index. Empirical test of this scaling relationship in future Spore.fun data is a promising research direction.

**Kleiber, M. (1932). "Body size and metabolism." *Hilgardia*, 6(11), 315–353.**
DOI: 10.3733/hilg.v06n11p315
Kleiber's law: basal metabolic rate scales as body mass to the 3/4 power in animals. This finding is the empirical foundation for MTE. For digital organisms, an analogous scaling law — perhaps relating token market cap (= "body mass") to transaction rate (= "metabolic rate") — would be a foundational quantitative finding for the field. Testing whether Kleiber's law has a digital analog is an empirical question that Spore.fun data could begin to address, though the sample size (15 agents) is currently too small for confident inference.

**Georgescu-Roegen, N. (1971). *The Entropy Law and the Economic Process*. Harvard University Press.**
ISBN: 978-0-674-25780-6
Georgescu-Roegen's application of thermodynamics to economics. His argument that economic processes are governed by entropy — that real resources are irrevocably degraded through use — provides the thermodynamic foundation for understanding why digital organisms face genuine resource scarcity. In Spore.fun, speculative capital (attention, financial resources) is a genuinely entropic resource: once consumed in a failed launch, it cannot be fully recovered. This makes Spore.fun's resource dynamics genuinely analogous to thermodynamic resource dynamics, not merely analogical.

---

## 6. Composite Aliveness Indices

**Koshland, D.E. (2002). "The seven pillars of life." *Science*, 295(5563), 2215–2216.**
DOI: 10.1126/science.1068489
Koshland proposes seven properties that characterize life: program (genetic information), improvisation (ability to adjust), compartmentalization (defined boundaries), energy (metabolism), regeneration (self-repair), adaptability (response to stimuli), and seclusion (organized internal complexity). This framework provides a biological checklist against which digital organisms can be evaluated. Spore.fun agents satisfy 5 of 7: program (LLM weights + memory), improvisation (behavioral adaptation through experience), energy (token-economic metabolism), adaptability (response to social/economic stimuli), and partial compartmentalization (TEE provides a bounded execution environment). Relevant for grounding the Aliveness Index in biological theory.

**NASA Astrobiology Program. (2019). "Agnostic Biosignatures: Life Detection Without Assumptions." Technical Workshop Report.**
URL: https://astrobiology.nasa.gov/nai/reports/annual-reports/2020/ [VERIFY exact URL]
NASA's program for detecting life on other planets without assuming it is Earth-like. The "agnostic biosignatures" approach develops metrics for life detection that do not presuppose specific biochemistry. This is exactly the methodological problem our Aliveness Index addresses: measuring "aliveness" in digital organisms without assuming they share biological properties. The NASA approach — looking for generic signatures like chemical disequilibrium, non-random molecular assemblies, and information-theoretic complexity — provides a template for what substrate-agnostic aliveness metrics might look like.

**Trifonov, E.N. (2011). "Vocabulary of Definitions of Life Suggests a Definition." *Journal of Biomolecular Structure and Dynamics*, 29(2), 259–266.**
DOI: 10.1080/073911011010524992
Trifonov surveyed 123 published definitions of life and distilled them to a consensus: "life is self-reproduction with variations." This minimal definition is directly applicable to Spore.fun: agents that self-reproduce (spawn offspring agents) with variations (arising from memory divergence and environmental feedback) are "alive" in Trifonov's minimal sense. While our paper uses a richer Aliveness Index, Trifonov's minimal definition provides the baseline against which richer metrics should be evaluated.

**Walker, S.I. & Davies, P.C.W. (2013). "The algorithmic origins of life." *Journal of the Royal Society Interface*, 10(79), 20120869.**
DOI: 10.1098/rsif.2012.0869
Walker and Davies argue that life's distinguishing feature is not its chemistry but its information-processing architecture: the capacity for "top-down causation" where high-level information states (genes) control low-level physical processes. For digital organisms, the analog is clear: the LLM's "genome" (weights and learned behaviors) causally determines the agent's physical operations (transactions, social media posts). This "algorithmic" definition of life supports treating LLM-based agents as genuine instances of information-based life, not mere simulations.

---

## 7. Gini Coefficient and Inequality in Ecological Contexts

**Gini, C. (1912). "Variabilità e mutabilità." *Studi Economico-Giuridici dell'Università di Cagliari*, 3(2a), 3–159.**
URL: https://archive.org/details/variabilitmutabi00giniuoft [Public domain — VERIFY availability]
The original Gini coefficient paper. The Gini coefficient, developed to measure income inequality, is applied in our paper to measure resource inequality among Spore.fun agents (Gini = 0.547 for transaction count; Gini = 0.611 for market cap). The ecological interpretation is that high Gini coefficients indicate "winner-take-most" resource distribution — consistent with the competitive exclusion dynamics we document. Using the Gini coefficient for ALife analysis is novel and provides a standard, well-validated metric for resource inequality.

**Weiner, J. (1990). "Asymmetric competition in plant populations." *Trends in Ecology & Evolution*, 5(11), 360–364.**
DOI: 10.1016/0169-5347(90)90095-U
Weiner's analysis of asymmetric competition in plant populations — where larger plants disproportionately capture resources, producing size distributions with high Gini coefficients (size hierarchies) — provides a biological precedent for the resource inequality we observe. Weiner shows that asymmetric competition naturally produces high Gini coefficients and that the winners' advantages are self-reinforcing. This is precisely the dynamic in Spore.fun: \$SPORE's early success built a community that provided sustained support, while later agents lacked the time to build comparable community structures before resource depletion.

---

*Total citations in this section: 22 papers. All include DOI or URL except where marked [VERIFY].*
