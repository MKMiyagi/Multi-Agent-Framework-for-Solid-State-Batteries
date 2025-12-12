## Realizing Low-Pressure Operation of All-Solid-State Lithium-Sulfur Batteries Enabled by Carbon-Coated Current Collectors

Jaehee Park, Jinkwan Jung, Seungbo Yang, Dong Hyeon Kim, Jeong Beom Lee, Jin An Sam Oh, Hedi Yang, Mahadeen Nashiru, Chen-Jui Huang,* and Ying Shirley Meng*

All-solid-state lithium-sulfur batteries (ASSLSBs) face challenges due to the need for high stack pressures to maintain interfacial contact. This study demonstrates that surface-engineered current collectors coated with carbon-based primer layers enable low stack-pressure (10 MPa) operation of ASSLSBs. Dry-processed lithium sulfide (Li 2 S)-composite cathodes, using carbon-coated aluminum (Al) foil, show significantly reduced interfacial resistance, enhanced adhesion, and improved cycling stability. Interfacial resistance is reduced by 5-10 times compared to bare aluminum, and surface analyses confirmed improved mechanical interlocking between the composite cathode and current collector. Notably, carbon black-coated Al collector leads to superior performance, with ≈ 800 mAh g -1 reversible capacity and 78% retention over 350 cycles at 10 MPa. Even at 1 C (1 C = 1166 mAh g -1 ), carbon-coated cells maintained 96% of the capacity obtained at C/10. This practical strategy provides a scalable approach to enable low-stack-pressure operation and broaden ASSB implementation.

## 1. Introduction

All-solid-state lithium-sulfur batteries (ASSLSBs) are a promising next-generation energy storage system that combines the high theoretical energy density of Li-S chemistry with the safety

J. Park, H. Yang, M. Nashiru, C.-J. Huang, Y. S. Meng

Pritzker School of Molecular Engineering

The University of Chicago

Chicago, IL 60637, USA

E-mail: bencjhuang@uchicago.edu;shirleymeng@uchicago.edu

J. Jung, Y . S. Meng

Aiiso Yufeng Li Family Department of NanoEngineering

University of California San Diego

LaJolla, CA 92093, USA

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/aenm.202504272

©2025 The Author(s). Advanced Energy Materials published by Wiley-VCH GmbH. This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

DOI: 10.1002/aenm.202504272

Adv. Energy Mater. 2025 , e04272

and stability of solid electrolytes. [ 1-3] In particular, using lithium sulfide (Li 2 S) as the cathode active material is attractive for ASSLSBs because it provides a high theoretical capacity (1166 mAh g -1 ) while eliminating the need of lithium-containing anode material. [ 4,5] However, the insulating nature of Li 2S and its significant volume shrinkage (45%) upon delithiation during charging to sulfur pose severe challenges for maintaining solid-solid interfacial contact within the composite cathode and at the cathode/separator interface. [ 6,7] Unlike liquid-electrolyte cells, where the liquid can wet and infiltrate into the electrode, ASSLSBs must maintain intimate solid-solid contact among the Li 2 S, solid electrolyte, and current collector (CC) at all times to enable e/uniFB03cient lithium-ion transport and electron conduction. [8-10] In practice, even slight detachment or void formation at the cathode interface, for instance, due to Li 2 S volume changes during cycling, can sharply increase interfacial resistance, leading to rapid capacity loss. [ 6,11-13] As a result, most reported ASSLSB cells require the application of high external

S. Yang, D. H. Kim, J. B. Lee

LG Energy Solution, Ltd.

LG Science Park

Magokjungang 10-ro, Gangseo-gu, Seoul 07796, Republic of Korea

J. A. S. Oh

Institute of Materials Research and Engineering (IMRE)

Agency for Science

Technology and Research (A*STAR)

2 Fusionopolis Way, Innovis #08-03, Singapore 138634, Singapore

C.-J. Huang

Advanced Photon Source

Argonne National Laboratory

Lemont, IL 60439, USA

Y. S. Meng

Energy Storage Research Alliance

Argonne National Laboratory

Lemont, IL 60439, USA

www.advancedsciencenews.com stack pressures (on the order of tens to a few hundred MPa) during both cell fabrication and cycling to maintain intimate interfacial contact and suppress impedance growth. [14] This reliance on extreme pressure is a significant roadblock for practical batteries, complicating cell design, packaging, and scale-up manufacturing. [15] Reducing the stack pressure requirementideally to the range of a few megapascals or less-is therefore crucial for the realistic implementation of solid-state Li-S technology. [ 16]

Recent research has begun to address the interfacial contact problem in all-solid-state batteries (ASSBs) by developing materials and engineering solutions that enable stable cycling at reduced pressures. [17,18] For example, more compliant or self-healing solid electrolytes can accommodate volume changes and maintain contact with active materials under lower pressure. [ 19-21] Viscoelastic polymer-based electrolytes and ductile halide electrolytes have each shown the ability to sustain particle contact and suppress polarization at stack pressures well below 50 MPa. [22] Similarly, optimizing the electrode structure, such as introducing soft interfacial layers or using advanced composite designs, can mitigate stack pressure requirements. [23-25] Notably, a recent study demonstrated that a co-rolled electrolyte/cathode architecture (producing an intimately bonded interface) enabled high-loading ASSB cells to cycle over 500 times with &gt; 80% capacity retention at only 2 MPa. [22] Other works have employed interfacial additives or sintering techniques to achieve nearly zero external pressure operation in specialized systems. [10] While these approaches are encouraging, many involve developing new materials or multi-step processing to reinforce the interface. There remains a need for a simple, scalable strategy to improve solid-state cathode interfaces such that high-performance cycling is possible under minimal pressure. [21,26,27]

One practical and industry-friendly approach to enhance cathode interfaces is surface engineering of the CC with a conductive carbon coating. [ 28,29] Carbon-coated aluminum foils (often referred to as 'primer-coated' CCs) are already well-established in lithium-ion and liquid-phase Li-S batteries to improve electrode performance. [30,31] The carbon primer-typically a thin ( ≈ 1 µ m) layer of graphite or carbon black particles bound to the metal foil-serves multiple roles: It 1) increases the surface roughness and porosity of the CC, 2) provides a continuous conductive carbon network, and 3) protects the aluminum from corrosion or side reactions. [ 32] Crucially, the rough, carbonaceous surface promotes mechanical interlocking with the cathode composite, leading to stronger adhesion and lower contact resistance at the interface. [ 31] In conventional Li-S cells, for instance, using a primer-coated Al CC was shown to diminish electrochemical polarization and enable higher sulfur utilization and better cycle life compared to a bare Al foil. [ 33] Likewise, in emerging solid-state systems, surface-structured or primer-coated CCs have been reported to significantly improve electrode adhesion and stability. [ 30,34-36] O/uniFB00ermann et al. demonstrated that physically micro-structuring an Al foil, to create a rough, interlocking interface, increased cathode adhesion, reduced interfacial impedance, and boosted Li-S cell capacity and rate capability. [ 37] The concept of a primer coating o/uniFB00ers a similar mechanical interlocking e/uniFB00ect in a simpler format: the primer layer con-

www.advenergymat.de forms around cathode particles and accommodates their expansion. This e/uniFB00ect can especially be beneficial for dry-processed or binder-minimal electrodes, where traditional binders are absent or scarce. In such electrodes, including the dry-pressed Li 2 S cathodes in this work, the cathode's adhesion to a smooth metallic foil is inherently poor, often leading to delamination or cracking upon cycling. A conductive primer-coated foil can alleviate this problem by providing a microscopically rough, adhesive interface that locks the active material in place and ensures continuous electron pathways. [30,37] Equally important, primer-coated foils are commercially available and compatible with existing cell fabrication processes, making them an immediately applicable solution. [ 31]

Despite these known advantages of primer-coated CCs, their e/uniFB03cacy in enabling truly low-pressure ASSLSB operation has not been fully established. Previous studies have largely demonstrated the benefits of primer-coated foils at conventional stack pressures or in liquid-electrolyte cells, [ 30,31,38,39] but it remains unclear to what extent this strategy alone can o/uniFB00set the need for external pressure in a solid-state Li-S cell. In other words, can a simple primer coating on the CC allow a high-capacity Li 2S cathode to cycle stably at lower stack pressures without other special accommodations? This work aims to answer that question by systematically investigating the role of primercoated vs uncoated CCs in ASSLSBs designed for low-pressure operation. We focus on a challenging yet practically relevant cathode system: a dry-processed Li 2 S-carbon-sulfide composite with high areal loading ( ≈ 7 mAh cm -2 ). Such a cathode provides a stringent test of interfacial engineering, as it combines the volume-change and electronic insulating issues of Li 2 S with the adhesive limitations of a low-binder dry-processed electrode.

In this work, two types of conductive primer coatings are evaluated (graphite-based and carbon-black-based) on Al foils in comparison to bare Al, keeping all other cell components identical. By measuring the interfacial resistance, mechanical adhesion, and electrochemical performance across a range of stack pressures (from the typical 75 MPa down to 1 MPa), we directly assess how the CC surface influences the pressure requirement of the cell. Consequently, we demonstrate that the use of primer-coated CCs enables a drastic reduction of stack pressure for all-solid-state Li-S cells. Even at a low pressure of 10 MPa, Li 2 S half-cells with primer-coated Al foils exhibit stable and high capacity for over 350 cycles, whereas cells with bare Al foils rapidly fail under the same conditions. The primer layer reduces the cathode-collector interfacial resistance by an order of magnitude, from 65.5 to 21.0 Ω , e/uniFB00ectively maintaining electronic percolation and physical contact without the assistance of heavy external pressure. Notably, cell using a carbon black-coated Al, which provides a highly porous, high-surface-area interface, delivers an initial discharge capacity of 799 mAh g -1 at C/3 and retains ≈ 78% of retention after 350 cycles under 10 MPa. They also show excellent rate capability at 10 MPa, with 96% of the low-rate capacity preserved even at 1 C discharge. By contrast, equivalent cells on a bare Al CC su/uniFB00er rapid capacity decay and severe polarization when the pressure is lowered to 10 MPa. These results provide one of the first quantitative validations that commercial primer-coated foils can largely overcome the notorious pressure constraints in ASSLSBs.

www.advancedsciencenews.com

Figure 1. Interface engineering of CCs for Li 2 S cathodes. Schematic comparison of cathode/collector interfaces using bare Al and carbon-coated Al CCs at 75 and 10 MPa in ASSBs. The carbon coating improves adhesion, increases surface contact, and lowers interfacial resistance, enabling stable Li 2 S cycling under low stack pressure.

Thefindings not only bridge a critical gap in the solid-state battery field-demonstrating low-pressure, long-life operation in a highenergy Li-S cell-but also highlight a simple and scalable engineering solution. By employing a modest primer coating on the CC, a well-established industrial material, it is possible to achieve performance that rivals or exceeds prior low-pressure strategies which rely on novel electrolytes or complex architectures. Overall, this work identifies primer-coated CCs as a practical key to unlocking low-pressure ASSLSB operation, and it underscores the importance of interface-focused design for bringing solid-state Li-S batteries closer to real-world viability.

## 2. Results and Discussion

## 2.1. Designing Criteria of Current Collector/Electrode Interface

Figure 1 illustrates a schematic comparison of the interface engineering approach for Li 2 S cathodes using bare Al and carboncoated Al CCs at stack pressures of 75 and 10 MPa in ASSBs. In pristine conditions, the interfaces between Li 2 S cathodes and bare Al CCs initially exhibit relatively poor adhesion due to their smooth surfaces, creating potential for delamination and interface gaps during battery cycling. Upon cycling at 75 MPa, the Li 2 S cathode undergoes significant volume changes, which can exacerbate the formation of pores and interfacial gaps, leading to delamination between the cathode layer and the bare Al CC. Reducing the stack pressure further to 10 MPa results in even greater volume expansion, intensifying delamination and gap formation at the cathode-CC interface. In contrast, carboncoated Al CCs present significantly rougher surfaces, promoting enhanced mechanical interlocking and increased contact areas. This surface engineering significantly improves adhesion,

Adv. Energy Mater. 2025 , e04272

resulting in reduced interfacial resistance. Consequently, cells with carbon-coated Al CCs maintain robust adhesion and intimate contact between cathode and CC under both 75 and 10 MPa conditions.

To improve electrode uniformity and mechanical integrity, we employed a dry-process fabrication of the Li 2 S cathode. This low-binder dry process, using 4 wt.% PTFE, is expected to enhance the contact between active material and electrolyte and eliminate solvent-induced inhomogeneities. Below, we compare a traditionally mixed powder cathode to our dry-processed cathode to verify improved homogeneity and performance. Figure 2 presents a detailed characterization and electrochemical comparison of powder and dry-processed Li 2 S cathodes. X-ray di/uniFB00raction (XRD) patterns (Figure 2a) show that the ball-milled Li 2S cathode composite exhibits characteristic peaks consistent with raw Li 2 S, with the amorphous nature of the Li 6 PS5 Cl (LPSCl) electrolyte indicated by the lack of distinct crystalline peaks. Raman spectroscopy further supports this observation, showing a distinct peak at 418 cm -1 for the milled Li 2 S composite of Li 2 S and LPSCl, confirming the e/uniFB00ective incorporation of amorphous LPSCl electrolyte into the composite structure as shown in Figure 2b. A shift of P-S stretching in PS4 3 -from 425 to 418 cm -1 , assigned to Li 3 PS4 (LPS), suggesting that Li 2S reduced LPSCl to LPS. [40] Electrochemical evaluations conducted at 0.05 C under 75 MPa (Figure 2c,d) demonstrate comparable electrochemical behaviors between powder and dry-processed Li 2 S cathodes. However, the dry-processed Li 2 S cathodes exhibit slightly improved initial charge and discharge capacities, indicative of superior electrochemical performance attributed to better composite homogeneity and enhanced mechanical integrity provided by the dry processing method.

www.advancedsciencenews.com

www.advenergymat.de

Figure 2. Characterization and comparison of powder and dry-processed Li 2 S cathode. a) X-ray di/uniFB00raction (XRD) patterns and b) Raman spectra of the bulk-state powder of the milled Li 2 S composite and raw materials. c) Initial charge/discharge curves of Li 2 S//Li 0.5 In half-cell at 0.05 C under 75 MPa using powder and dry-processed Li 2 S cathode at the 6.8 mAh cm -2 level. d) Di/uniFB00erential capacity (dQ/dV) analysis of ASSBs of the initial cycle using powder and dry-processed Li 2 S cathode.

## 2.2. Correlation Between Surface Roughness and Adhesion

Given the proposed criteria of an optimal CC/cathode interface, which necessitates good interfacial contact, we selected three different Al CCs, namely bare Al foil, graphite-coated Al foil, and carbon black-coated Al foil, with di/uniFB00erent surface roughness for comparison. The SEM images ( Figure 3 a-c) of the three CCs clearly illustrate that carbon-coated CCs exhibit significantly increased surface roughness compared to bare Al. The bare Al foil presents a smooth, relatively featureless surface, whereas graphite-coated Al shows distinct protrusions and carbon blackcoated Al displays a uniformly coarse and porous surface with rounded, entangled features. This morphological trend reflects the intrinsic particle characteristics of the coatings: graphite comprises large, plate-like particles (tens of microns), while carbon black consists of nanoscale ( ≈ 20 nm) agglomerates that form porous, irregular clusters with high surface area [ 41] Phillips et al. These intrinsic di/uniFB00erences explain why the carbon black layer yields a rougher and more porous surface than the relatively flatter graphite coating. Quantitative AFM analysis (Figure 3d-i) confirms this observation, revealing root mean square roughness (Sq) values of 8.5, 87, and 104.2 nm for bare Al, carbon black-coated Al, and graphite-coated Al, respectively. This enhanced surface roughness provides numerous mechanical contact points, facilitating strong mechanical interlocking with the cathode composite, thereby ensuring robust adhesion and opti-

Adv. Energy Mater. 2025 , e04272

mal electrical contact. The carbon black coating layer, with much higher surface roughness (Sq ≈ 100 nm vs ≈ 10 nm for graphitecoated Al), facilitates better interfacial contact and more e/uniFB00ective electron transport pathways, leading to better adhesion and lower interfacial resistance than the smoother graphite-based coating (8.5 nm). Profilometric measurements further corroborate these findings at a larger measurement scale of 400 × 400 µ m (Figure S2 and Table S1, Supporting Information).

Cross-sectional SEM images of pristine Li 2 S cathode-CC interfaces ( Figure 4 a-c) highlight distinct di/uniFB00erences among the tested foils. After cathode lamination at 75 MPa, the cathode/CC interfaces using coated Al foils (Figure 4b,c) demonstrate excellent conformity with no visible gaps. In contrast, bare Al interfaces exhibit micro-gaps (Figure 4a), suggesting inadequate initial adhesion that could lead to high local impedance and rapid interfacial degradation. To conclude, the primer coatings show promise in e/uniFB00ectively mitigating such interface degradation at lower pressures.

Interfacial adhesion was quantitatively assessed using crosshatch adhesion tests (Figure 4d). The adhesion classification (0B, 1B, 2B) corresponds to the percentage of area removed, determined by optical imaging of the cross-hatch grid after tape pull. [ 42] The carbon black-coated Al exhibited superior adhesion, with only 32% of the area removed (classification 2B), while graphite-coated Al showed slightly less adhesion (65% removed; classification 1B), and bare Al performed poorly with significant

www.advancedsciencenews.com

Figure 3. Surface roughness measurement. SEM and 3D views and top views of AFM images of each a,d,g) bare Al, b,e,h) graphite-coated Al and c,f,i) carbon black coated Al foils.

delamination (89% removed; classification 0B). (Figure 4e,f). Tpeel tests confirmed these trends, yielding average peel strengths of 5.02 ± 0.14 gf mm -1 for carbon black-coated Al, 3.80 ± 0.22 gf mm -1 for graphite-coated Al, and only 1.13 ± 0.12 gf mm -1 for bare Al (Figure S3, Supporting Information). These results clearly illustrate that carbonaceous coatings enhance mechanical interlocking and improve adhesion of the cathode composite.

## 2.3. Pressure-Responsive Activation of Li 2 S Cathodes

Next, we investigate how the CC interface influences the initial Li 2 S activation and the minimum stack pressure required for stable operation. By comparing the electrochemical behavior and interface resistance from 75 MPa down to 1 MPa, we aim to identify the critical pressure at which each cell can function without performance compromise. Initial charge/discharge curves and corresponding di/uniFB00erential capacity (dQ/dV) analysis for Li 2 S//Li 0.5 In half cells at 0.05 C and 6.8 mAh cm -2 under 75 MPa demonstrate superior cycling performance using primercoated Al foils compared to bare Al ( Figure 5 a,b). While all cells exhibited similar electrochemical reactions, carbon-coated cells achieved higher utilization and lower polarization due to improved interface contact and adhesion. Notably, carbon-coated foils have been shown to accommodate volume changes in electrodes and preserve interfacial integrity during cycling (e.g., a carbon primer layer bu/uniFB00ering expansion in a Si-based anode [43] ). Similarly in our cells, the slight compressibility of the carbon primer's compliance likely absorbs stress between the sti/uniFB00 Al current collector and the Li 2 S-composite cathode, mitigating interfacial pressure fluctuations. Considering the significant volume expansion of S to Li 2 S (79%) during lithiation/delithiation, this compliance is crucial. Bare Al, lacking this compliance, con- centrates stress at the interface, potentially causing cracking and delamination, whereas carbon-coated Al distributes mechanical stress e/uniFB00ectively. Post-mortem FIB-SEM images (Figures S4 and S5, Supporting Information) indicate that the bare Al cell developed a prominent interfacial gap after cycling, whereas the primer-coated Al cell maintained close and uniform contact, exhibiting only minor pores within the cathode layer. Therefore, the apparent increase in measured porosity for the bare Al electrode predominantly results from this interfacial void rather than intrinsic electrode porosity, highlighting the improved mechanical stability provided by the primer-coated interface.

To understand the interfacial resistance and its e/uniFB00ect on the cathode/CC interface at low stack pressure, interfacial resistance at the cathode-CC interface, a critical parameter in solid-state batteries, was evaluated through DC polarization measurements under varying stack pressures using the above-mentioned three types of CCs (Figure 5c). Bare Al interface exhibited notably high resistance at low pressures, exceeding 200 Ω cm 2 at ≈ 1 MPa, and required up to 50 MPa to reduce resistance to ≈ 20 Ω cm 2 . In sharp contrast, graphite- and carbon black-coated Al foils displayed substantially lower interfacial resistances even at pressures as low as 1 MPa. Specifically, at 10 MPa, interfacial resistances were ≈ 30 Ω cm 2 and 21 Ω cm 2 for graphite-coated and carbon black-coated Al, respectively, significantly lower than the 50 Ω cm 2 resistance of bare Al. E/uniFB00ective electronic conductivity calculated from these DCP measurements (Figure S7, Supporting Information) indicates enhanced electron transport pathways provided by carbon coatings at reduced stack pressures. To conclude, carbon-coating layers reduce the interfacial resistance at the cathode/CC interface and maintain su/uniFB03cient electron transport at reduced stack pressure. This can be attributed to the facilitated adhesion from the enhanced surface roughness of carbon-coating layers, which is critical to enable low stack

Figure 4. Adhesion test of dry-processed Li 2 S cathode layer with di/uniFB00erent CC via ASTM D3359 Method-B (cross-hatch). Obtained zoomed-out and zoomed-in cross-sectional SEM images of ASSBs based on a) bare Al, b) graphite-coated Al, and c) carbon black coated Al CCs at pristine state with Li 2 S cathode composite. d) Schematic steps of the adhesion test using the cross-hatch pattern-transfer method. e) Images of the cathode materials on the tested CCs after detachment. f) Classification of the adhesion results based on ASTM D3359.

pressure operation. As shown by the four-point-probe results (Table S2, Supporting Information), all foils maintained high conductivity ( ≈ 10 7 S m -1 ), so the substantially lower interfacial impedance observed in Figure 5 with coated foils must arise from enhanced adhesion and contact quality rather than from di/uniFB00erences in primer resistivity.

With respect to thickness, prior reports [ 44,45] indicate that a 1 µ m carbon primer provides adequate coverage, conductivity, and strain bu/uniFB00ering to enable stable low-pressure operation at high areal capacities, while avoiding the drawbacks of excessively thin or overly thick coatings. Our commercial foils employ a 1 µ m primer, and Figure 5c shows that its through-plane contribution to interfacial resistance is negligible compared with the total impedance. Together with the high in-plane conductivity values in Table S2 (Supporting Information), this indicates that adhesion and contact quality dominate the impedance behavior rather than the bulk resistivity of the primer coating layer. A 1 µ mthickness, therefore, represents a practical compromise: it is thick enough to ensure complete coverage and mechanical compliance, while remaining thin enough to avoid excess resistance or inactive mass. Although systematic variation was not possible here, design-of-experiments (DOE)-style studies across 0.52 µ mwould be highly valuable. In particular, coupling thickness variation with interfacial contact-resistance measurements (as in Figure 5c), adhesion strength testing, and coverage/morphology analysis, such as cross-sectional SEM or profilometry, would provide the quantitative insight needed to establish robust design rules for practical scale-up.

To determine the critical pressure required to maintain stable interfacial contact among the three CCs, discharge capacities were measured under varying stack pressures from 75 to 1 MPa (Figure 5d). We used the house-made constant pressure pellet cell setup, reported in our previous work, [ 46] that has springs which can control the pressure, and I have manually changed the pressure every three cycles at every pressure for the pressure test in Figure 5d. It can be calibrated via monitor for load cell and can

www.advancedsciencenews.com

Figure 5. Investigation of critical pressure of dry-processed Li 2 S cathode layer with di/uniFB00erent CC using constant pressure setup. a) Initial charge/discharge curves and b) di/uniFB00erential capacity (dQ/dV) analysis of Li 2 S//Li 0.5 In half cell using di/uniFB00erent Al CCs at 0.05 C in 6.8 mAh cm -2 level under 75 MPa. c) Plot of resistance of CC/Li 2 S/CC configuration and d) discharge capacity of Li 2 S//Li 0.5 In half-cell of 0.33 C in 6.8 mAh cm -2 level at varying operating pressure in the range between 1 and 75 MPa with constant pressure pellet cell set up.

hold the pressure deviation was only 104% after one cycle. Bare Al showed a significant capacity drop at 10 MPa, whereas graphitecoated Al maintained performance until ≈ 5 MPa, and carbon black-coated Al showed a gradual decline down to 1 MPa. Under pressures below 5 MPa, the highly porous carbon black layer may not sustain perfectly stable contact during repeated cycling, potentially leading to faster capacity fade despite its superior adhesion at higher pressures. These results corroborate with the electronic conductivity that carbon coatings significantly reduce the pressure threshold to 10 MPa necessary to maintain stable electrochemical performance. Cross-sectional FIB-SEM images of interfaces under pressure (Figure 4a-c) further highlight this advantage, demonstrating that carbon coatings facilitate intimate cathode contact even at significantly reduced pressures. This beneficial e/uniFB00ect makes carbon-coated CCs a promising strategy for practical low-pressure operation of solid-state lithium-sulfur batteries.

To activate the Li 2 S cathode material, an initial charging step up to 3.5 V (vs Li/Li + ) was required due to the insulating nature of Li 2 S. Following the high-pressure formation step (75 MPa, RT, 0.05 C for three cycles), all cells activated successfully. Additionally, the LPSCl electrolyte likely undergoes partial reduction to LPS during the first discharge. [ 40,47] Raman spectra show that the P-S stretching mode of LPSCl (425 cm -1 ) shifts to 418 cm -1 upon contact with Li 2 S, consistent with partial reduction to LPS as reported previously. [ 48,49] We note that this reaction occurs mainly during initial mixing and the first discharge. The ef-

Adv. Energy Mater. 2025 , e04272

fect could be more pronounced in cells with primer-coated foils due to their higher interfacial contact area, potentially contributing to the higher initial capacity seen for those cells. The initial charge capacities at C/3 - 780.9, 697.8, and 499.6 mAh g -1 for cells with carbon black-coated, graphite-coated, and bare CCs, respectively -indicated partial delithiation to sulfur with possible residual Li 2 S or formation of intermediate Li 2 S2 species, accounting for the observed deviation from the theoretical capacity of 1166 mAh g -1 . The uncoated Al cell displayed notably lower initial capacities, attributable to higher polarization. Specifically, from the dQ/dV plot, the initial charge peak for the uncoated Al cell was at 2.8 V compared to 2.7 V for both coated cells. The uncoated cell also exhibited multiple lower discharge peaks at ≈ 1.6 V, whereas carbon-coated cells showed peaks ranging from 1.6 to 1.9 V, indicative of better kinetics and more e/uniFB00ective utilization. Among the coated cells, the carbon black-coated collector consistently showed slightly better utilization compared to the graphite-coated variant. The reduced polarization in primercoated cells enabled a more complete discharge of Li 2 S even at lower pressure, leading to higher delivered capacity compared to bare Al cells.

Thepractical advantage of carbon-coated CCs is clearly demonstrated through the cathode active material utilization under varied stack pressures. Figure 6 a-c presents the initial voltage profiles of Li 2 S//Li 0.5 In half cells cycled at C/3 under both 10 and 75 MPa, following three initial formation cycles at C/20 at 75 MPa. Corresponding di/uniFB00erential capacity (dQ/dV) curves

16146840, 0, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202504272 by University Of Chicago Library, Wiley Online Library on [22/10/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advenergymat.de

Figure 6. Cycling performance at 75 and 10 MPa with di/uniFB00erent CC. a-c) Initial charge/discharge curves and d-f) corresponding dQ/dV curves of 0.33 C at 10 and 75 MPa after formation cycles with bare Al, graphite-coated Al, and carbon black coated Al CCs, respectively.

shown in Figure 6d-f highlight the electrochemical reactions and utilization of active material. Under 75 MPa, all cells exhibited the characteristic two-step Li 2S ↔ S conversion plateaus at ≈ 2.6 and 1.7 V (vs Li/Li + ). The carbon black-coated Al collector showed the smallest voltage gap at 75 MPa, indicating the lowest internal resistance. Graphite-coated and bare Al exhibited progressively higher resistance, consistent with Table S3 (Supporting Information). Corresponding initial discharge capacity at 75 MPa was measured as 789 mAh g -1 (carbon black), 703 mAh g -1 (graphite), and 494 mAh g -1 (bare Al), which consistently exceeded the capacity measured at 10 MPa in each CC type.

At the reduced pressure of 10 MPa, performance di/uniFB00erences became apparent. The cell employing bare Al exhibited severe polarization and a truncated capacity of only 392 mAh g -1 . Conversely, cells utilizing graphite-coated and carbon blackcoated CCs delivered substantially higher discharge capacity of 670 mAh g -1 and 702 mAh g -1 , respectively, along with reduced polarization. Notably, the carbon black-coated cell maintained similar electrochemical behavior and a comparable utilization profile at 10 MPa to that observed at 75 MPa, albeit with slightly increased polarization (150 mV). All cells demonstrated high Coulombic e/uniFB03ciencies exceeding 98% after initial stabilization. These results underscore that carboncoated CCs enable enhanced utilization of Li 2 S cathodes even at substantially reduced external stack pressure (10 MPa). Interestingly, the primer-coated CC cells at 10 MPa achieved utilization comparable to or superior to bare Al cells cycled at 75 MPa, clearly illustrating the e/uniFB00ectiveness of carbon coatings in alleviating loss of cathode utilization at low stack pressure.

Adv. Energy Mater. 2025 , e04272

## 2.4. Electrochemical Performance at Low Pressure

The strong mechanical interlocking and enhanced adhesion demonstrated in the previous section are particularly critical in preserving the cathode's structural integrity during long-term cycling. Given the 79% volume change of Li 2 S during lithiation/delithiation, inadequate adhesion-such as that seen with bare Al-can result in progressive delamination, cracking, or loss of electrical contact. In contrast, the rough primer-coated interfaces likely act as mechanical bu/uniFB00ers that maintain intimate contact even as the active material expands and contracts. This structural robustness at the interface is expected to mitigate impedance growth and support sustained electrochemical performance over extended cycles, as investigated in Figure 7 . Evaluating high-rate performance is critical to assessing practical applicability, particularly under low-pressure conditions that could exacerbate ionic or electronic limitations. Figure 7a details the Crate performance of cells at 10 MPa. Both carbon-coated CC cells demonstrated excellent capacity retention and active material utilization at increasing C-rates. Notably, the carbon black-coated Al cell retained 96% of its initial C/10 capacity after the C-rate tests up to 1 C, compared to 84% for the graphite-coated Al cell. The measurements revealed capacities of 1231 and 1189 mAh g -1 at C/20, 532 and 360 mAh g -1 at C/2, and 224 and 137 mAh g -1 at 1 C for carbon black-coated and graphite-coated collectors, respectively (Table S3, Supporting Information). In stark contrast, the uncoated Al cell drastically dropped to ≈ 20%of its original capacity at C/10 following the rate test and exhibited negligible capacity (36 mAh g -1 ) at 1 C. Compared to bare Al, carbon-coated foils exhibited consistently lower charge-transfer resistance (R ct ) and reduced polarization during cycling (Figure 7d,e and Table S4,

www.advancedsciencenews.com

Figure 7. Cyclability and EIS analysis at 10 MPa with di/uniFB00erent CC. a) Discharge capacity of Li 2 S//Li 0.5 In half-cells for various C-rates from 0.05 C to 1.0 C at 10 MPa at the 6.8 mAh cm -2 level based on Table S3. b) Discharge capacity of Li 2 S//Li 0.5 In half-cells at room temperature over 350 charging/discharging cycles at the C-rate of 0.33 C under 10 MPa at the 6.8 mAh cm -2 level. The open circles represent the calculated coulombic e/uniFB03ciency at each cycle. c) Li 2 S utilization from the C-rate test calculated based on the designed Li 2 S cathode capacity of 6.8 mAhcm -2 . Nyquist plot from the measured electrochemical impedance spectroscopy (EIS) results d) before and e) after 100 cycles with equivalent circuit used for fitting the measured impedance data.

Supporting Information). This demonstrates that the primer not only provides mechanical compliance but also decreases interfacial impedance, thereby facilitating stable Li + and electron transport. These dual benefits are consistent with prior reports showing that carbon-coated foils improve interfacial kinetics in Li-S [ 33] and LiFePO 4 [ 44] systems. The pronounced deterioration in the uncoated cell is attributable to increased interfacial impedance and compromised electronic percolation pathways at high current densities and low stack pressures.

Long-term cycling at 10 MPa revealed distinct performance differences between coated and uncoated CCs. The carbon blackcoated Al cell demonstrated exceptional cycling stability over 350 cycles at a C/3 rate, with an average Coulombic e/uniFB03ciency of 99.75% and negligible capacity degradation. Similarly, the graphite-coated Al cell retained 96% of its initial capacity for 206 cycles. In contrast, the bare Al cell experienced rapid capacity decay, dropping below 100 mAh g -1 within ten cycles and essentially failing by 50 cycles. Figure 7b clearly illustrates these diverging trends: both carbon-coated cells maintained stable cycling, whereas the bare Al cell rapidly deteriorated. Between the two coated variants, the carbon black-coated cell exhibited marginally 5% higher initial capacity, likely due to improved electronic conductivity. Conversely, its slightly reduced fade rate suggested superior interfacial stability. Importantly, both carbon-coated collectors significantly outperformed the bare Al foil, a/uniFB03rming their practical advantages.

Our achieved electrochemical performance at 10 MPa is notable compared to previously reported ASSLSBs, often requiring elevated temperatures ( &gt; 60 ° C) for improved kinetics. [ 47] To further contextualize our findings, we benchmarked them against recent reports of low-pressure ASSLSBs. Many prior demonstra- tions required elevated temperatures or specialized designs. For example, Cronk et al. [ 47] reported &gt; 80% retention over 500 cycles at 10 MPa, but only at 60 ° C. By contrast, our carbon-coated Al current collector enabled ≈ 800 mAh g -1 and 78% retention over 350 cycles at 10 MPa, all at room temperature. Other approaches, such as polymer-based electrolytes [ 10] or compliant interlayers, [ 50] also improve low-pressure cycling but require new materials or extra steps. Our strategy-using a commercially available carboncoated foil-achieves similar benefits without altering the chemistry or operating conditions, underscoring its practical significance. To place our results in context, Table S5 (Supporting Information) compares this work with several recent all-solid-state Li-S batteries. Our ambient 10 MPa cell achieves high capacity and long-term stability comparable to or better than other stateof-the-art cells, including those operated at elevated temperature or with specialized interlayers.

Here, competitive capacities near theoretical value at C/20 were demonstrated under room temperature and low pressure (10 MPa), facilitated by highly conductive sulfide electrolyte (LPSCl) and optimized interfacial engineering. Figure 7d,e shows Nyquist plots measured before and after 100 cycles at C/3. The uncoated Al cell initially showed a high-frequency impedance (R ohm ) of 65.5 Ω , increasing significantly to 95.5 Ω after cycling. In contrast, carbon-coated cells exhibited minor increases (from 63.1 to 66.1 Ω for carbon black-coated and 63.3-68 Ω for graphitecoated Al), indicating stable interfaces throughout cycling. The sustained low R ohm and stable capacity suggest that the primer layer prevented major contact loss or cracking at the interface throughout long-term cycling. In addition to the 10 MPa case shown in Figure 7d,e, we also measured cells at lower pressures (1-5 MPa), with the full spectra provided in Figure S9

www.advancedsciencenews.com

(Supporting Information). These data confirm that cells operated at 1-2 MPa experience a pronounced increase in interfacial resistance even after one cycle, whereas ≥ 5 MPa maintains nearly unchanged impedance. This trend is consistent with the faster capacity fade observed under insu/uniFB03cient stack pressure and highlights the importance of maintaining moderate pressure to preserve stable interfacial contact. The substantial di/uniFB00erence in impedance evolution aligns closely with observed cycling trends, with stable low-resistance interfaces in coated cells correlating directly to enhanced electrochemical stability and longevity.

## 3. Conclusion

This study demonstrated that applying a thin ( ≈ 1 µ m) conductive carbon coating (graphite and carbon black) to the aluminum CC enables stable, high-performance operation of all-solid-state lithium-sulfur batteries at significantly reduced stack pressures down to 10 MPa. Notably, at a low stack pressure of 10 MPa, cells with carbon-coated CCs exhibited exceptional electrochemical performance, delivering an initial discharge capacity of ≈ 800 mAhg -1 at C/3 and retaining 78% of the initial capacity after 350 cycles. In contrast, cells employing bare aluminum foils rapidly deteriorated under identical conditions, retaining only 20% of the initial capacity. This highlights the substantial advantage a/uniFB00orded by the carbon coating.

Morphological and adhesion analyses, including AFM surface roughness measurements, cross-sectional FIB-SEM imaging, and quantitative mechanical adhesion tests, confirmed that the primer-coated CCs provided significantly enhanced interfacial contact. The increased surface roughness facilitated robust mechanical interlocking between the cathode and the CC, effectively preventing cathode delamination and maintaining electrode integrity even under the considerable volume changes (79%) of the Li 2 S active material during repeated cycling.

Consequently, these structural improvements translated directly into notable electrochemical improvements. Primercoated cells exhibited significantly lower interfacial resistancesreduced by a factor of 5-10 compared to bare aluminum-and markedly decreased electrochemical polarization, enabling more e/uniFB00ective utilization of the Li 2 S cathode. Furthermore, even under demanding rate conditions (1 C), the carbon black-coated cells retained 96% of their initial C/10 capacity, underscoring their exceptional rate capability at low pressures.

EIS provided additional confirmation of the interface stability improvements. The carbon-coated CCs consistently exhibited low and stable interfacial impedance throughout prolonged cycling, in sharp contrast to the increasing resistance observed in cells with bare aluminum foils. These findings collectively a/uniFB03rm the critical role of carbon-based coatings in preserving stable, lowresistance interfaces under practical cycling conditions.

Taken together, the results of this work highlight that a straightforward, scalable interface engineering strategy-namely the use of commercially available primer-coated CCs-can significantly alleviate the traditionally stringent high-pressure requirements for all-solid-state lithium-sulfur batteries. This practical approach o/uniFB00ers a viable pathway toward realizing low-pressure, high-performance ASSBs, representing an important step toward their commercial viability and broader real-world implementation.

Adv. Energy Mater. 2025 , e04272

## 4. Experimental Section

Materials Preparation and Composite Fabrication : All materials were dried under vacuum at 80 ° C unless otherwise specified as anhydrous and subsequently stored and handled in an argon-filled glovebox to prevent air exposure. LPSCl solid-state electrolyte, purchased from NEI Corporation, was selected due to its high ionic conductivity (3 × 10 -3 S cm -1 at 25 ° C). For use as a catholyte, LPSCl was ball-milled at 500 rpm for 2 h using a high-energy planetary ball mill to achieve a uniform particle size of ≈ 10 µ m. Commercial Li 2 S (99.98%, Sigma Aldrich) was utilized either as received or ball-milled at 400 rpm for 10 h to reduce particle size to the micron scale, as verified by SEM (Figure S1, Supporting Information). Optimal cathode composites were prepared by initially ball-milling the cathode active material (Li 2 S) and conductive agent (acetylene black) at 600 rpm for 1 h. Subsequently, the pre-milled mixture was thoroughly hand-mixed with LPSCl electrolyte using a mortar and pestle. The final composite formulation consisted of 30 wt.% Li 2 S, 50 wt.% LPSCl, and 20 wt.% acetylene black. Al foils (15 µ mthick, 99.5% purity) served as cathode CCs, including bare Al and two types of carbon-coated foils. Commercial graphite-coated Al foil (16 µ m thick with ≈ 1 µ m conductive carbon coating, MTI Corp.) and carbon-black-coated Al foil (16 µ mthick with ≈ 1 µ mcarbon coating, LG Energy Solution) were used as received. According to vendor specifications, the graphite-coated foil had a surface density of ≈ 0.5 g m -2 , surface resistivity &lt; 30 Ω per 25 µ m2, and employs a water-based modified acrylate adhesive binder; the carbon-black-coated foil had a bulk density of ≈ 1.8 g cm -3 . Both primer layers were ≈ 1 µ mthick.

Dry-Process Cathode Fabrication and Lamination : Cathode composite powders were mixed with 4 wt.% PTFE (Chemours) using a heated mortar and pestle until a dough-like consistency was achieved. The resulting mixture was hot-rolled at 80 ° C using a precision hot roller (MTI Corp.), gradually reducing its thickness to form a 100 µ m-thick cathode film. This dry-processed cathode film was then laminated onto the respective Al CCs at 120 ° C using the same hot-rolling procedure.

Electrochemical Measurements : Electrochemical tests were conducted using custom-designed 10 mm diameter pellet cells consisting of Grade 5 titanium plungers and polyether ether ketone (PEEK) dies. For cell fabrication, the cathode and solid electrolyte separator layers were pressed at three tons (375 MPa), while the Li 0.5 In anode was pressed at one ton (125 MPa) for 10 s. After assembly, the pellet cells were inserted into custom cell holders and hand-tightened to apply a stack pressure of 75 MPa for initial activation, then lowered to 10 MPa unless otherwise stated.

Electrochemical impedance spectroscopy (EIS) was performed using a Biologic SP-300 potentiostat at open circuit with a 30 mV amplitude and a frequency range from 7 MHz to 20 mHz. Spectra were acquired at room temperature in the pristine state and after 100 cycles, following full discharge and 1 h relaxation. Electronic conductivity measurements were carried out under various pressures via DC polarization on CC/Li 2 S composite/CC symmetric cells. A constant voltage (50, 100, and 200 mV) was applied, and the steady-state current attributed to electronic leakage was measured (Figure S6, Supporting Information). Cycling and capacity utilization were evaluated on Neware cyclers (CT-4008T), with three initial activation cycles performed at 75 MPa and room temperature.

Adhesion Testing : Adhesion between the cathode layer and CC was assessed via ASTM D3359 Method-B (cross-hatch) and T-peel testing. In the cross-hatch test, 10 × 10 perpendicular lattice patterns were scratched into the cathode layer, followed by uniform tape application and removal at a 90 ° angle. The T-peel test involved peeling 10 mm-wide cathode strips from the CC at 5 mm min -1 using a tensile tester. The steady-state peel force was recorded for analysis.

Surface Roughness Measurements : Surface morphology and roughness were evaluated using atomic force microscopy (AFM) and optical profilometry. AFM measurements were performed on a Bruker Dimension Icon (NanoScope 6 controller, ScanAsyst mode). A Bruker silicon probe with a nominal tip radius of 8 nm was used. Data were processed in NanoScope Analysis with standard line-by-line flattening and noise filtering. Sample areas of 1.0 × 1.0 mm 2 were scanned and postprocessed using appropriate software to extract quantitative roughness parameters.

www.advenergymat.de

www.advancedsciencenews.com

Scanning Electron Microscopy (SEM) : SEMimaging was performed using a ThermoFisher Scientific Aquilos Cryo-focused ion beam (FIB)/SEM. Powder and pellet samples were prepared in an argon-filled glovebox and transferred using an airtight transfer arm. FIB cross-sectional milling was conducted using gallium ions at 30 kV and 50 nA, followed by polishing at 30 kV and 15-7 nA as needed. ImageJ software was used for postprocessing and porosity analysis.

X-Ray Di/uniFB00raction (XRD) and Raman Spectroscopy : XRDwasconducted on a Rigaku SmartLab di/uniFB00ractometer equipped with Cross-Beam Optics and a HyPix-3000 detector using Mo K /u1D6FC radiation ( /u1D706 = 0.7107 Å) over a 2 /u1D703 range of 5 ° -50 ° . Samples were sealed in 0.5 mm boron capillaries under argon to prevent air exposure. Raman spectroscopy was performed using a HORIBA LabRAM HR Evolution Confocal Raman Microscope with 532 nm excitation. A 50 × objective lens was used to focus the laser on a 2 µ m-diameter spot, with a spectral resolution of 3 µ mand an integration time of 5 s. The spectral range was 100-800 cm -1 .

Four-Point Probe Measurements : Electronic conductivity of bare and carbon-coated Al foils was measured with a Jandel RM3000 four-point probe (Nano3, UCSD). A constant current (10 nA-99.99 mA) was applied and the voltage drop recorded across the inner probes. Sheet resistance ( Ω / □ ) was converted to bulk resistivity ( /u1D70C = Rs × t) using the foil thickness (12-18 µ m including ≈ 1 µ m carbon coating), and conductivity was calculated as /u1D70E = 1/ /u1D70C . Reported values represent averages of three measurements per sample.

## Supporting Information

Supporting Information is available from the Wiley Online Library or from the author.

## Acknowledgements

The authors acknowledge the use of the following facilities at the University of Chicago: the Pritzker Nanofabrication Facility, the Soft Matter Characterization Facility, the Advanced Electron Microscopy Core Facility (RRID: SCR \_ 019198), the X-ray Research Facilities in the Department of Chemistry, and the Materials Research Science and Engineering Center (MRSEC). AFM measurements were supported by the Soft and Hybrid Nanotechnology Experimental (SHyNE) Resource (NSF ECCS-2025633), a node of the NSF National Nanotechnology Coordinated Infrastructure (RRID: SCR \_ 022955). Raman spectroscopy work was supported by NSF Award Number DMR-2011854 through MRSEC. The authors thank the technical sta/uniFB00 and research teams at these facilities for assistance with characterization and instrumentation. This work was funded by the LG Energy Solution through the Frontier Research Laboratory (FRL) Program and the Coherent/II/VI Foundation through the Block-Gift Program.

## Conflict of Interest

A joint patent application on this work has been filed (US 63/847709) between UC San Diego's O/uniFB03ce of Innovation and Commercialization as well as LG Energy Solution, Ltd.

## Data Availability Statement

The data that support the findings of this study are available in the supplementary material of this article.

## Keywords

carbon coating, current collectors, dry-process, interfacial engineering, lithium-sulfur batteries, low-pressure, solid-state batteries

www.advenergymat.de

Received: July 31, 2025 Revised: October 3, 2025 Published online:

- [1] B. B. Gicha, L. T. Tufa, N. Nwaji, X. Hu, J. Lee, Nano-Micro Lett. 2024 , 16 , 172.
- [2] T. Jin, K. Liang, J.-H. Yu, T. Wang, Y . Li, T.-D. Li, S. P. Ong, J.-S. Yu, Y . Yang, Nano Lett. 2024 , 24 , 6625.
- [3] J. Park, T. Watanabe, K. Yamamoto, T. Uchiyama, T. Takami, A. Sakuda, A. Hayashi, M. Tatsumisago, Y. Uchimoto, Chem. Commun. 2023 , 59 , 7799.
- [4] Y. Liu, X. Meng, Z. Wang, J. Qiu, Sci. Adv. 2022 , 8 , abl8390.
- [5] J.-Y . Hwang, H. Park, H. Kim, S. Kansara, Y.-K. Sun, Acc. Mater. Res. 2025 , 6 , 245.
- [6] Y. Fujita, K. Münch, T. Asakura, K. Motohashi, A. Sakuda, J. Janek, A. Hayashi, Chem. Mater. 2024 , 36 , 7533.
- [7] Z. Hu, P. Gao, S. Ju, Y. Li, T. Zhang, C. Lu, T. Huang, P. Liu, Y . Lv, M. Guo, W. Zhang, W. Teng, G. Xia, S. Zhu, D. Sun, X. Yu, Nat. Commun. 2025 , 16 , 3979.
- [8] E. P. Alsaç, D. L. Nelson, S. G. Yoon, K. A. Cavallaro, C. Wang, S. E. Sandoval, U. D. Eze, W. J. Jeong, M. T. McDowell, Chem. Rev. 2025 , 125 , 2009.
- [9] S. A. Han, J. H. Suh, M.-S. Park, J. H. Kim, Electrochem. Energy Rev. 2025 , 8 , 5.
- [10] J. Zhang, J. Fu, P. Lu, G. Hu, S. Xia, S. Zhang, Z. Wang, Z. Zhou, W. Yan, W. Xia, C. Wang, X. Sun, Adv. Mater. 2025 , 37 , 2413499.
- [11] I. D. Seymour, E. Quérel, R. H. Brugge, F. M. Pesci, A. Aguadero, ChemSusChem 2023 , 16 , 2202215.
- [12] B. D. Dandena, D.-S. Tsai, S.-H. Wu, W.-N. Su, B. J. Hwang, EES Batteries 2025 , 1 , 692.
- [13] S. Wang, R. Fang, Y. Li, Y . Liu, C. Xin, F. H. Richter, C.-W. Nan, J. Mater. 2021 , 7 , 209.
- [14] A. Parejiya, R. Amin, M. B. Dixit, R. Essehli, C. J. Jafta, D. L. Wood, I. Belharouak, ACS Energy Lett. 2021 , 6 , 3669.
- [15] P. Albertus, V. Anandan, C. Ban, N. Balsara, I. Belharouak, J. BuettnerGarrett, Z. Chen, C. Daniel, M. Doe/uniFB00, N. J. Dudney, B. Dunn, S. J. Harris, S. Herle, E. Herbert, S. Kalnaus, J. A. Libera, D. Lu, S. Martin, B. D. McCloskey, M. T. McDowell, Y. S. Meng, J. Nanda, J. Sakamoto, E. C. Self, S. Tepavcevic, E. Wachsman, C. Wang, A. S. Westover, J. Xiao, T. Yersak, ACS Energy Lett. 2021 , 6 , 1399.
- [16] H. Pan, L. Wang, Y. Shi, C. Sheng, S. Yang, P. He, H. Zhou, Nat. Commun. 2024 , 15 , 2263.
- [17] T. Schmaltz, F. Hartmann, T. Wicke, L. Weymann, C. Neef, J. Janek, Adv. Energy Mater. 2023 , 13 , 2301886.
- [18] S. Kim, Y. A. Chart, S. Narayanan, M. Pasta, Nano Lett. 2022 , 22 , 10176.
- [19] S. Kalnaus, N. J. Dudney, A. S. Westover, E. Herbert, S. Hackney, Science 2023 , 381 , abg5998.
- [20] R. Narayan, C. Laberty-Robert, J. Pelta, J. M. Tarascon, R. Dominko, Adv. Energy Mater. 2022 , 12 , 2102652.
- [21] T. H. Dolla, S. O. Ajayi, L. L. Sikeyi, M. K. Mathe, N. Palaniyandy, J. Energy Storage 2025 , 106 , 114737.
- [22] D. J. Lee, Y . Jeon, J.-P. Lee, L. Zhang, K. H. Koh, F. Li, A. U. Mu, J. Wu, Y.-T. Chen, S. McNulty, W. Tang, M. Vicencio, D. Xu, J. Kim, Z. Chen, Nat. Commun. 2025 , 16 , 4200.
- [23] M. Hou, Y. Pan, F. He, K. Xu, H. Zhang, Y. Zhou, B. Zhao, Y. Chen, M. Liu, Adv. Funct. Mater. 2022 , 32 , 2203722.
- [24] G. Lu, G. Meng, Q. Liu, L. Feng, J. Luo, X. Liu, Y. Luo, P. K. Chu, Adv. Powder Mater. 2024 , 3 , 100154.
- [25] F. Zhang, Y. Guo, L. Zhang, P. Jia, X. Liu, P. Qiu, H. Zhang, J. Huang, eTransportation 2023 , 15 , 100220.

## www.advancedsciencenews.com

- [26] W. D. Richards, L. J. Miara, Y . Wang, J. C. Kim, G. Ceder, Chem. Mater. 2016 , 28 , 266.
- [27] M. D. Bouguern, A. K. M R, K. Zaghib, J. Power Sources 2024 , 623 , 235457.
- [28] H. Rostami, J. Valio, P. Suominen, P. Tynjälä, U. Lassi, Chem. Eng. J. 2024 , 495 , 153471.
- [29] Z. Chen, Q. Zhang, Q. Liang, Nanomaterials 2022 , 12 , 1936.
- [30] H. Hao, R. Tan, C. Ye, C. T. J. Low, Carbon Energy 2024 , 6 , 604.
- [31] M. Fritsch, M. Coeler, K. Kunz, B. Krause, P. Marcinkowski, P. Pötschke, M. Wolter, A. Michaelis, Batteries 2020 , 6 , 60.
- [32] S. Park, Y .-W. Song, B. Ryu, H. Son, M.-Y. Kim, J. Kim, J. Lim, C. Yun, J. Mater. Chem. A 2024 , 12 , 25530.
- [33] T. Li, H. Bo, H. Cao, Y. Lai, Y. Liu, Int. J. Electrochem. Sci. 2017 , 12 , 3099.
- [34] M. Li, B. Wang, J. Ma, Z. Wang, Y. Liang, Z. Wang, L. Zhang, Y. Tang, Q. Huang, J. Huang, Adv. Energy Mater. 2024 , 14 , 2303156.
- [35] H. Kim, H. Lee, G. H. Kwon, J. Kim, D. Jeong, H. G. Jung, J. S. Bae, D. Shin, J. Cho, J. H. Kim, H. S. Kim, J. Mun, O. Kwon, Small 2025 , 21 , 2409523.
- [36] H. Oh, J. T. Kim, H.-J. Shin, A. Y . Kim, C. Bak, S.-O. Kim, K. Y . Chung, J. Mun, J. Kim, Y . M. Lee, S.-Y . Lee, H.-G. Jung, Mater. Sci. Eng.: R: Rep. 2025 , 164 , 100970.
- [37] J. O/uniFB00ermann, E. Gayretli, C. Schmidt, J. Carstensen, H.-G. Bremes, A. Würsig, S. Hansen, M. Abdollahifar, R. Adelung, J. Colloid Interface Sci. 2024 , 664 , 444.
- [38] S. S. Zhang, X. Fan, C. Wang, Sustain. Energy Fuels 2018 , 2 , 163.

www.advenergymat.de

- [39] C. Busson, M. A. Blin, P. Guichard, P. Soudan, O. Crosnier, D. Guyomard, B. Lestriez, J. Power Sources 2018 , 406 , 7.
- [40] M. Tachez, J. Malugani, R. Mercier, G. Robert, Solid State Ionics 1984 , 14 , 181.
- [41] C. Phillips, A. Al-Ahmadi, S.-J. Potts, T. Claypole, D. Deganello, J. Mater. Sci. 2017 , 52 , 9520.
- [42] R. B. Leggat, S. R. Taylor, W. Zhang, R. G. Buchheit, Corrosion 2002 , 58 , 283.
- [43] L. Zeng, P. Li, M. Ouyang, S. Gao, K. Liang, Batteries 2025 , 11 , 114.
- [44] M. Onsrud, A. O. Tezel, S. Fotedar, A. M. Svensson, SN Appl. Sci. 2022 , 4 , 225.
- [45] R. Dominko, M. Bele, M. Gaberscek, M. Remskar, D. Hanzel, S. Pejovnik, J. Jamnik, J. Electrochem. Soc. 2005 , 152 , A607.
- [46] S.-Y. Ham, H. Yang, O. Nunez-Cuacuas, D. H. S. Tan, Y.-T. Chen, G. Deysher, A. Cronk, P. Ridley, J.-M. Doux, E. A. Wu, J. Jang, Y . S. Meng, Energy Storage Mater. 2023 , 55 , 455.
- [47] A. Cronk, X. Wang, J. A. S. Oh, S.-Y. Ham, S. Bai, P. Ridley, M. Chouchane, C.-J. Huang, D. Cheng, G. Deysher, H. Yang, B. Sayahpour, M. Vicencio, C. Lee, D. Lee, M.-S. Song, J. Jang, J. B. Lee, Y. S. Meng, ChemRxiv 2024 , hj829.
- [48] D. H. S. Tan, E. A. Wu, H. Nguyen, Z. Chen, M. A. T. Marple, J.-M. Doux, X. Wang, H. Yang, A. Banerjee, Y. S. Meng, ACS Energy Lett. 2019 , 4 , 2418.
- [49] E. Lee, H. Kim, H. Choi, S. Y . Kim, K. Y . Chung, Chem. Commun. 2024 , 60 , 14834.
- [50] C. Doerrer, M. Metzler, G. Matthews, J. Bu, D. Spencer-Jolly, P. G. Bruce, M. Pasta, P. S. Grant, Device 2024 , 2 , 100468.