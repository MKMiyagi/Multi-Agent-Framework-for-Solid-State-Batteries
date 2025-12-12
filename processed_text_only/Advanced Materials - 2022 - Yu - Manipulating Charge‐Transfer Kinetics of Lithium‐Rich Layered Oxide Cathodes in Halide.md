www.advmat.de

## Manipulating Charge-Transfer Kinetics of Lithium-Rich Layered Oxide Cathodes in Halide All-Solid-State Batteries

Ruizhi Yu, Changhong Wang, Hui Duan, Ming Jiang, Anbang Zhang, Adam Fraser, Jiaxuan Zuo, Yanlong Wu, Yipeng Sun, Yang Zhao, Jianwen Liang, Jiamin Fu, Sixu Deng, Zhimin Ren, Guohua Li, Huan Huang, Ruying Li, Ning Chen, Jiantao Wang,* Xifei Li,* Chandra Veer Singh,* and Xueliang Sun*

Employing lithium-rich layered oxide (LLO) as the cathode of all-solid-state batteries (ASSBs) is highly desired for realizing high energy density. However, the poor kinetics of LLO, caused by its low electronic conductivity and significant oxygen-redox-induced structural degradation, has impeded its application in ASSBs. Here, the charge transfer kinetics of LLO is enhanced by constructing high-e/uniFB03ciency electron transport networks within solidstate electrodes, which considerably minimizes electron transfer resistance. In addition, an infusion-plus-coating strategy is introduced to stabilize the lattice oxygen of LLO, successfully suppressing the interfacial oxidation of solid electrolyte (Li 3 InCl 6 ) and structural degradation of LLO. As a result, LLO-based ASSBs exhibit a high discharge capacity of 230.7 mAh g -1 at 0.1 C and ultra-long cycle stability over 400 cycles. This work provides an in-depth understanding of the kinetics of LLO in solid-state electrodes, and a/uniFB00ords a practically feasible strategy to obtain high-energy-density ASSBs.

## 1. Introduction

All-solid-state batteries (ASSBs) have attracted significant attention  in  recent  years  because  of  their  exceptional  safety  and high  theoretical  energy  density,  derived  from  employing  nonflammable  inorganic  solid-state  electrolytes (SSEs). [1]   Many

R. Yu, C. Wang, H. Duan, A. Fraser, Y. Sun, Y. Zhao, J. Liang, J. Fu, S. Deng, R. Li, X. Sun

Department of Mechanical and Materials Engineering

University of Western Ontario

London, Ontario N6A 5B9, Canada

E-mail: xsun9@uwo.ca

R. Yu

Institute of Micro/Nano Materials and Devices Ningbo University of Technology Ningbo, Zhejiang 315211, China

C. Wang, H. Huang, J. Wang

Glabat Solid-State Battery Inc 700 Collip Circle, London, Ontario N6G 4X8, Canada

E-mail: wangjt@glabat.com

M. Jiang Institute of Physical Science and Information Technology Anhui University Hefei, Anhui 230601, China

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/adma.202207234.

DOI: 10.1002/adma.202207234

Adv. Mater. 2023 , 35 , 2207234

inorganic SSEs based on sulfides, [2] oxides, [3] halides, [4] and borohydrides [5] have  been  developed  over  the  past  decades, including those demonstrating high ionic  conductivity  (e.g.,  12  mS  cm -1 for Li 10GeP2S12,  LGPS,  and  25  mS  cm -1 for Li 9.54 Si 1.74 P1.44 S11.7 Cll0.3 , LSPSCl), [2] highvoltage  stability  (e.g.,  4.21  V  versus  Li + / Li for Li 3YCl6, LYC, and 4.3 V versus Li + / Li  for  Li 3 InCl6,  LIC), [6] low  cost  (Li 2 ZrCl6 and Li 2.25 Zr0.75 Fe0.25 Cl6 ), [7] and appropriate mechanical properties. [8]  With these advances  in  SSEs,  various  cathode  materials have been attempted in ASSBs, such as LiCoO2 (LCO), [9] LiNi0.5 Mn0.3Co0.2 O 2 (NMC532), [10]   and  Ni-rich  layered  cathode materials (e.g., LiNi0.8 Mn0.1Co0.1 O 2 , NMC811, [4c] LiNi0.85 Co0.1 Mn0.05O2,Ni85, [11] and LiNi0.90 Co0.05 Mn0.05O2, Ni90 [12] ).

These  cathode  materials  typically  show  a  specific  capacity  of &lt; 200  mAh  g -1 , [13] which  limits  the  energy  density  of  ASSBs to  less  than  450  Wh  kg -1 . [14] Comparatively,  lithium-rich  layered oxide (LLO) possesses a higher theoretical capacity of ≥ 250  mAh  g -1 , [15] and  is  thus  a  promising  candidate  for achieving  ASSBs  with  an  energy  density  of  500  Wh  kg -1

A. Zhang, Y. Wu, Z. Ren, G. Li, J. Wang China Automotive Battery Research Institute Co., Ltd No. 11 Xingke East Street, Yanqi Economic Development Area,

Huairou District, Beijing 101407, China

J. Zuo, X. Li

Key Laboratory of Advanced Batteries Materials for Electric Vehicles of China Petroleum and Chemical Industry Federation

Institute of Advanced Electrochemical Energy &amp; School of Materials

Science and Engineering

Xi'an University of Technology

Xi'an, Shaanxi 710048, China

E-mail: xfli@xaut.edu.cn

N. Chen

Canadian Light Source

44 Innovation Boulevard, Saskatoon, Saskatchewan S7N 2V3, Canada

C. V. Singh

Department of Materials Science and Engineering University of Toronto

Toronto, Ontario M5S 3E4, Canada

E-mail: chandraveer.singh@utoronto.ca

www.advancedsciencenews.com www.advmat.de

Figure 1. Schematic for constructing ASSBs with high energy density. A) SSE thickness-dependent gravimetric energy density of LLO-based ASSBs. The capacity of the cathode sheet is 4 mAh cm -2  and other parameters are listed in Table S1 (Supporting Information). B) Electronic conductivities of the proposed cathode materials (LCO, [18a]  NMC532, [18b] NMC811, [18b] and LLO [17b] ). C) Electrochemical stability windows of proposed SSEs (Li 7 La 3 Zr 2 O12, LLZO, [3,21a] Li 6 PS5Cl, LPSCl, [21a,b] Li 3 PS4, LPS, [21a,c] and Li 3 InCl 6 , LIC [4c,6] ), charge/discharge voltage windows of the proposed cathode materials (LCO, [18a] NMC532, [24]  NMC811, [24] and LLO [17b] ), and electrochemical stability windows of proposed coating materials (Li 2 SiO 3 , LSO, LiNbO 3 , LNO, LiTaO 3 , LTO, and LPO). [21a]  The dashed boxes mark the potential for the compound to be fully delithiated. D) Concept of the bulk-type ASSBs enabled by carbon additives and LLO with LPO infusion-plus-coating architecture.

( Figure 1 A;  Figure  S1,  Supporting  Information). [16]   However, until now, manganese-based LLO is rarely explored in bulk-type ASSBs.

Several  grand  challenges  that  have  yet  to  be  solved  hinder the application of LLO in the solid-state electrodes of ASSBs. [16c,17] First,  unlike  other  layered  oxide  cathodes, [18]   LLO possesses  an  extremely  low  electronic  conductivity  of ≈ 10 -8 S cm -1 (Figure 1B) [17b]  due to its large bandgap and the formation

Adv. Mater. 2023 , 35 , 2207234

of charge  polarons. [17b,19] Therefore,  su/uniFB03cient electronically conducting  pathways  cannot  be  obtained  within  conventional carbon-free  solid-state  electrodes  based  on  LLO. [20]   Second, the  upper  operating  voltage  of  LLO  (4.8  V  vs  Li + /Li)  greatly exceeds  the  intrinsic  electrochemical  windows  of  most  SSEs (Figure  1C), [3,21]   leading  to  unavoidable  SSE  degradation  and considerable  interfacial  side  reaction.  Third,  the  anion  redox, a unique electrochemical mechanism of LLO, generates highly

www.advancedsciencenews.com active oxygen species O (2 -n) -(0 &lt; n &lt; 2), [22]   which may oxidize SSEs and further block interfacial lithium-ion transport. Fourth, LLO undergoes a phase transition from layered to spinel due to irreversible  lattice  oxygen  loss. [23] This  structural  degradation increases  interfacial  resistance,  and  thus  impedes  interfacial lithium-ion  transport.  These  perplexing  interfacial  issues  may explain why LLO has not been successfully deployed in ASSBs until now.

In the present work, we design the solid-state electrode composition  and  surface  chemistry  of  LLO  to  boost  electron  and lithium-ion  transport  kinetics.  First,  continuous  electronically conducting pathways are established by introducing an appropriate  amount  of  carbon  additives  into  solid-state  LLO  electrodes. Second, an interfacial layer with high oxidative stability and satisfactory ionic conductivity-Li 3 PO 4  (LPO, Figure 1C)is  constructed  on  LLO  via  an  infusion-plus-coating  strategy (Figure  1D),  which  e/uniFB00ectively  stabilizes  LLO's  lattice  oxygen, minimizes local structural change, inhibits LLO/SSE interfacial degradation,  and  facilitates  interfacial  lithium-ion  transport. As  a  result,  LLO-based  ASSBs  exhibit  a  high  initial  capacity of 230.7 mAh g -1 and ultra-long cycling life of 431 cycles. Even at  2  C,  the  discharge  capacity  is  high  at  62.4  mAh  g -1 .  To  the best of our knowledge, this is the first demonstrated LLO-based ASSB using a solid-state halide electrolyte (LIC). This work provides  new  strategies  and  in-depth  insight  into  solid-state  LLO electrodes and opens a new avenue for developing high-energydensity ASSBs.

## 2. Results and Discussion

## 2.1. The Electronic Conductivity of Solid-State LLO Electrodes

In this study, the halide SSE (LIC) is selected due to its higher oxidation  stability  (4.3  V  vs  Li + /Li,  Figure  1C)  than  sulfidebased  SSEs  ( &lt; 2.31  V  vs  Li + /Li),  relatively  high  ionic  conductivity  ( &gt; 10 -3 S  cm -1 ),  and  moderate  mechanical  properties. [4c,6] In  general,  carbon  additives  are  excluded  in  conventional solid-state  electrodes  to  minimize  side  reactions  between  the carbon  additives and  SSEs. [25] Carbon-free  solid-state electrodes  work  well  with  common  cathode  materials,  (e.g.,  LCO, NMC532, and NMC811) because they  possess  high  electronic conductivity above 10 -5 S  cm -1 (Figure  1B).  However,  the  conventional  carbon-free  electrodes  cannot  function  well  when using a cathode material with low electronic conductivity (e.g., LLO  and  S8 )  due  to  insu/uniFB03cient  electron  transport  networks ( Figure 2 A). [17b]   For  example,  a  carbon-free  solid-state  LLO electrode can only be charged to 157 .7 mAh g -1  and discharged to  103.7  mAh  g -1 ,  and  shows  a  considerable  overpotential between charge and discharge curves (Figure 2B; Figure S2A, Supporting  Information).  In  addition,  a  voltage  peak  at  the beginning of  the  charging  process  is  also  identified,  which  is associated with an activation barrier owing to the low chargetransfer kinetics. [26]   Comparatively, by adding 5% carbon additive  by  weight,  the  solid-state  LLO  electrode  delivers  a  much higher charge capacity (219.7 mAh g -1 )  and discharge capacity (166.9 mAh g -1 ). Moreover, the solid-state LLO electrode with 5% carbon  additive  shows  a  negligible  overpotential  (Figure  S2A, Supporting  Information)  and  improved  lithium-ion  di/uniFB00usion

www.advmat.de coe/uniFB03cients (Figure S2B,C, Supporting Information), indicating that the electrode engineering can e/uniFB00ectively accelerate chargetransfer kinetics. Therefore, it is essential to construct e/uniFB00ective electron  transport  networks  for  those  cathodes  with  low  electronic conductivity such as LLO. Figure 2C displays the cycling performance of the LLO-based ASSBs at 0.2 C. Solid-state LLO electrode with 5% carbon additive exhibits a capacity retention of &gt; 60% after 100 cycles, whereas the solid-state LLO electrode with  10%  carbon  additive  delivers  fast  capacity  fading  with a  capacity  retention  of  only  20.9%,  suggesting  that  the  detrimental e/uniFB00ect of carbon additives on cycling performance can be minimized by controlling the carbon contents.

Direct current (DC) polarization test and linear sweep voltammetry (LSV) were performed to quantify the electronic conductivities  of  solid-state  LLO  electrodes  with  di/uniFB00erent  contents  of carbon additives. The carbon-free solid-state LLO electrode shows a  low  electronic  conductivity of 1.20 × 10 -8 S  cm -1 (Figure  2D), implying  that  the  limited  electron  transfer  leads  to  the  low capacity  of  the  LLO-based  ASSBs.  With  5%  and  10%  carbon additives,  the  electronic  conductivity  increases  to  4.09 × 10 -2 (Figure 2E) and 6.89 × 10 -1  S cm -1 (Figure 2F), respectively, suggesting  that  the  carbon  additives  provide  su/uniFB03cient  electronically conducting pathways within the solid-state LLO electrodes. However, a prominent oxidation peak at ≈ 4.0  V  is  identified  in the  LSV  curve  of  the  LIC  electrode  with  10%  carbon  additive (Figure 2G), indicating that excess carbon can lead to significant SSE decomposition. Therefore, an appropriate content of carbon additive with minimized detrimental influence on SSEs should be guaranteed when constructing solid-state LLO electrodes.

In  situ  electrochemical  impedance  spectroscopy  (EIS)  was further conducted to investigate the interfacial evolution upon cycling.  The  stepwise  charge  curves  and  corresponding  EIS profiles  are  presented  in  Figure  S3A-C  (Supporting  Information)  and  Figure  2H-J,  respectively.  An  equivalent  circuit  of  R(RQ)(RQ)(RQ)Q  (Figure  S3D,  Supporting  Information)  is  applied  to  fit  the  EIS  spectra.  It  is  well-documented that  the  semi-circle  at  high-frequency  ( &gt; 20  kHz),  mid-frequency (20 kHz -100 Hz, indicated by dashed lines), and lowfrequency ( &lt; 100 Hz) regions correspond to the bulk resistance of  SSE  (R SSE ),  charge-transfer  resistance  through  cathode/ SSE  interface  (RLLO | SSE ), and  anode/SSE  interfacial  resistance  (R anode | SSE ),  respectively. [27] The  most  critical  parameter, RLLO | SSE , depending on the state of charge (SOC), is utilized to track the variation of interfacial properties (Figure 2K). When the  charge  voltage  increases  from  3.9  to  4.1  V,  the  R LLO | SSE value  decreases,  which  is  closely  related  to  the  adequate  activation of the solid interface and the consolidation of SSE. [27a] However,  the  interfacial  resistance  of  carbon-free  solid-state LLO electrodes is much higher than those electrodes with 5% and 10% carbon additives, demonstrating insu/uniFB03cient chargetransfer  pathways at the cathode/SSE interface. [27b]   At  further charging to 4.8  V,  the  R LLO | SSE   value  increases  rapidly  for  the solid-state  LLO  electrode  with  10%  carbon  additive,  implying significant  SSE  decomposition  caused  by  excess  carbon  additives. It should be noted that a noticeable increase in R LLO | SSE value  from  4.3  to  4.6  V  can  be  observed  in  both  the  carbonfree LLO electrode and the electrode with 5% carbon additive, which hints that the electrochemical anion redox of LLO also has considerable influence on interfacial stability.

15214095, 2023, 5, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202207234 by University Of Chicago Library, Wiley Online Library on [15/05/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com www.advmat.de

Figure 2. E/uniFB00ects  of  the  intrinsic  electronic conductivity and electrochemical redox of LLO on the properties of ASSBs. A) Schematic illustration of the electronic channel block around the cathode/SSE and cathode/cathode interfaces. B) Initial charge/discharge curves of the solid-state LLO electrodes with di/uniFB00erent contents of carbon additives at 0.1 C. C) Cycling performance of the solid-state LLO electrodes with di/uniFB00erent contents of carbon additives at 0.2 C. The corresponding Coulombic e/uniFB03ciencies are shown in Figure S8 (Supporting Information). D,F) Electronic conductivities of the solid-state LLO electrodes with 0 (D), 5% (E), and 10% (F) carbon additives. The corresponding DC polarization curves are shown in Figure S9 (Supporting Information). G) LSV profiles of the solid-state LLO electrodes with di/uniFB00erent contents of carbon additives at 0.05 mV s -1 . H-J) Intra-cycle impedance measurements during the initial charge cycle for the solid-state LLO electrodes with 0 (H), 5% (I), and 10% (J) carbon additives. K) Evolution of cathode/SSE interfacial resistance as a function of charge voltage in the solid-state LLO electrodes with di/uniFB00erent contents of carbon additives. L,M) Ex-situ Ni (L) and Co (M) K-edge XANES spectra of the solid-state LLO electrode with 5% carbon additive at di/uniFB00erent charge/discharge states. N) Fourier transformed In K-edge EXAFS spectra of the solid-state LLO electrode with 5% carbon additive at di/uniFB00erent charge/discharge states. The enlarged spectra between 1.0 and 2.5 Å are shown in Figure S10 (Supporting Information). The In reference spectra were collected from InCl3 and In2O3. O) Di/uniFB00erential capacity versus voltage (d Q /d V versus V )  profile  of  the  solid-state  LLO  electrode  with  5% carbon additive at 0.1 C.

www.advancedsciencenews.com

## 2.2. Oxygen-Redox-Triggered Interfacial Degradation

Ex situ X-ray absorption spectroscopy (XAS) was performed on the solid-state LLO electrode with 5% carbon additive to probe electrochemical  redox-induced  interfacial  structural  degradation. When the cell is charged from open-circuit voltage (OCV) to  4.35  V,  the  X-ray  absorption  near  edge  structure  (XANES) spectra  of  Ni  (Figure  2L)  and  Co  (Figure  2M)  shift  to  higher energy, suggesting that Ni and Co are oxidized in this voltage range.  On  the  contrary,  no  apparent  change  can  be  found  in the Mn spectra (Figure S4, Supporting Information), indicating that Ni and Co redox are responsible for the capacity within the voltage range from OCV to 4.35 V. [28]  When further charging to 4.8 V, the XANES spectra of Ni and Co display no edge shift. For the  Mn,  the  white  line  of  the  XANES  spectra,  corresponding to the 1s → 4p transition, [29]  shifts to higher energy, whereas the main edge moves in the opposite direction. Furthermore, the pre-edge peak associated with the Mn 1s → 3d transition transforms from a pair of  splitting  peaks  (empty  t 2g and  e g states) into a sharp single peak. [29,30]  These changes in the Mn XANES spectra  suggest  the  local  structure  distortion  of  the  MnO 6 octahedron  but  no  direct  contribution  to  the  capacity,  indicating  that  oxygen  anion  oxidation  instead  of  cation  oxidation is  mainly responsible for the voltage plateau (4.35-4.8 V). [29,30] In  this  high  voltage  plateau,  highly  active  oxygen  species, O (2 -n) -,  are  produced,  which  can  easily  de-coordinate  from the  MO6  structure  (M  refers  to  the  transition  metal  and  Li) and chemically attack  the  SSEs. [31] This  process  results  in  the structural degradation of LLO and SSE oxidation. To verify the SSE oxidation, XANES spectra and extended X-ray absorption fine  structure  (EXAFS)  spectra  for  the  In  K-edges  during  the charge/discharge  process  were  collected.  The  XANES  spectra (Figure  S5,  Supporting  Information)  display  that  the  local environment  around  In  changes  considerably  after  charging from  4.35  to  4.8  V.  Furthermore,  the  Fourier  transformed  In K-edge EXAFS spectra (Figure 2N) show that the average bond length of the first shell (In-Cl bond) shrinks dramatically when charging from 4.35 to 4.8 V. As the In 3 + in  the  LIC  cannot be further oxidized, this bond length shrinkage should be caused by the change of ligand Cl around In. At the high SOC of 4.8 V, the average bond length ( ≈ 1.72 Å) is much lower than that of a typical In-Cl ( ≈ 1.94 Å) in LIC and closer to that of a typical In-O ( ≈ 1.60 Å) in In 2 O3, suggesting the partial oxidation of LIC. The interfacial reaction product (In 2 O 3 )  can  also  be  determined by X-ray photoelectron spectroscopy (XPS, Figure S6, Supporting Information).  During  discharging,  the  XANES  spectra  of  Ni and  Co  recover  to  their  pristine  energy,  corresponding  to  the reduction  of  these  ions  back  to  their  initial  states.  However, the white line of Mn shifts to lower than pristine energy and the pre-edge peak splitting is less resolved, indicating that the local structure  around  Mn  ions  has  changed  and  oxygen  vacancies have formed due to the side reaction at the voltage plateau. [30] More importantly, after discharging to 2.0 V, the local structure (Figure S5, Supporting Information) and average bond length of the first shell (Figure 2N) around In cannot recover to their pristine  state,  further  validating  the  irreversible  LIC  degradation.  Additionally,  owing  to  the  lower  microstrain  variation (0.088%  at  4.8  V,  Figure  S7A-C,  Supporting  Information)  of LLO during charging as compared to those of Ni-rich layered

www.advmat.de cathode materials (0.315% at 4.3 V and 0.415% at 4.6 V), [32]  the morphology  of  solid-state  LLO  electrode  can  be  maintained after  cycling  (Figure  S7D,E,  Supporting  Information).  Thus, the electro-chemo-microstructure coupling rather than electromechanics coupling,  dominates  the  interfacial  stability.  Based on the above analyses, a map of the redox couples and the SSE oxidation  can  be  illustrated  as  shown  in  Figure  2O.  It  can  be concluded that the anion oxidation reaction leads to the interfacial structural degradation between LLO and LIC, resulting in considerable charge-transfer resistance and the low capacity of LLO in ASSBs. The local structural change and interfacial side reactions between LLO and LIC should be suppressed to secure good cycling stability, as discussed in Section 2.3.

## 2.3. Surface Chemistry Reconstruction to Enhance Electrochemical Performance

Here  we  adopted  an  infusion-plus-coating  strategy  to  reconstruct  the  surface  of  LLO.  LPO,  as  an  excellent  ionic  conductor,  possesses  higher  oxidation  stability  than  conventional oxide  coatings,  such  as  LSO,  LNO,  and  LTO,  and  was  therefore selected as the coating layer (Figure 1C). [21a]   To  maximize the protective e/uniFB00ect of LPO, atomic layer deposition (ALD) and annealing  techniques  were  performed  to  construct  the  LLO with  infusion-plus-coating  architecture  (LPOn-iLPO  LLO,  see the supplemental information for a detailed description of the process).  The  infusion-plus-coating  architecture  ( Figure 3 A) is  evidenced  by  scanning  electron  microscopy  (SEM),  energydispersive X-ray (EDX) elemental mapping, and scanning transmission  electron  microscopy  (STEM)  analyses,  as  shown  in Figures S11-S13 (Supporting Information). Moreover, X-ray diffraction  (XRD)  patterns  (Figure  S14,  Supporting  Information) of the bare LLO and LPO5-iLPO LLO (surface chemistry modified  LLO, SCM LLO) reveal that the ALD-based infusion-pluscoating strategy do not change the stability of layered structure. The optimization procedure of the electrochemical performance for the LLO-based ASSBs is presented in Figure S15A-D (Supporting  Information).  It  should  be  mentioned  that  the  solidstate electrode contains 5% carbon additive. The SCM LLO cell demonstrates the best electrochemical performance among all modified  samples.  Compared  with  the  bare  LLO  cell,  the  initial  charge/discharge  capacity  and  Coulombic  e/uniFB03ciency  are remarkably enhanced after the surface chemistry modification (Figure 3B). The high initial discharge capacity of 230.7 mAh g -1 and Coulombic e/uniFB03ciency  of  83.0%  for  the  SCM  LLO  cell  are similar to those of liquid-based lithium-ion batteries with LLO (240.7 mAh g -1 ,  82.8%, Figure S15E, Supporting Information). In particular, the SCM LLO cell exhibits a long voltage plateau at  charge  voltage  between  4.35  and  4.8  V,  whereas  the  voltage plateau is  less  evident  in  the  bare  LLO  cell,  denoting  that  the infusion-plus-coating architecture can stabilize the oxygen redox. [33]   Furthermore,  the  cycling  performance  is  improved from 69.1% to 87 .9% after 100 cycles at 0.2 C (Figure 3C), and the  polarization  (Figure  S15F,G,  Supporting  Information)  and voltage  decay  (Figure  S15H,I,  Supporting  Information)  are also  e/uniFB00ectively  suppressed.  As  shown  in  Figure  3D,  the  SCM LLO  cell  delivers  increased  rate  capability,  which  can  achieve ≈ 26% (62.4 mAh g -1 )  of  the  capacity at 0.05 C. Even at a high

15214095, 2023, 5, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202207234 by University Of Chicago Library, Wiley Online Library on [15/05/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com www.advmat.de

Figure 3. Understanding the improved stability in ASSBs using LLO with infusion-plus-coating architecture. A) A diagram of the infusion-plus-coating architecture, in which LPO is infused into the grain boundaries and coated on the secondary particle surface. B) Initial charge/discharge curves of the bare LLO and SCM LLO cells at 0.1 C. C) Cycling performance of the bare LLO and SCM LLO cells at 0.2 C. D) Normalized rate capabilities of the bare LLO and SCM LLO cells at di/uniFB00erent current rates. Their corresponding capacity variations at di/uniFB00erent rates are shown in Figure S15B (Supporting Information). E) Normalized long-term cycling performance of the bare LLO and SCM LLO cells at 0.5 C. Their corresponding capacity and Coulombic e/uniFB03ciency variations are shown in Figure S15J,K (Supporting Information). F) The Nyquist plots of the EIS spectra of the bare LLO and SCM LLO cells after 100 cycles at 0.2 C. The interfacial resistances are illustrated by colored semicircles. G,H) Mn K-edge XANES spectra of the bare LLO (G) and SCM LLO (H) electrodes at di/uniFB00erent cycling stages. I,J) Fourier transformed In K-edge EXAFS spectra of the bare LLO (I) and SCM LLO (J) electrodes at di/uniFB00erent cycling stages. The In reference spectra were collected from InCl 3  and In2 O 3 . K,L) Raman spectra and fitted results of bare LLO (K) and SCM LLO (L) electrodes after 100 cycles at 0.2 C. M) Charge density di/uniFB00erence of a simulated interface between the LLO (001) surface and LPO (010) surface. N) The variations of O vac formation energy in the bare LLO and SCM LLO structures at di/uniFB00erent delithiation stages.

rate of 0.5 C, the SCM LLO cell exhibits long cycle life of 431 cycles, which significantly outperforms that of the bare LLO cell (149  cycles),  as  shown  in  Figure  3E.  Even  using  a  carbon-free solid-state electrode, the SCM LLO shows an improved cycling performance (Figure S16, Supporting Information). More importantly, the infusion-plus-coating strategy can enhance the

www.advancedsciencenews.com cycling stability of LLO in other solid-state battery system (e.g., using LYC and LLZO as SSEs, Figure S17, Supporting Information),  suggesting  the  surface  chemistry  reconstruction  of  LLO can enhance the stability of LLO/SSE interface.

## 2.4. Suppressed Interfacial Structural Deterioration upon Electrochemical Cycling

EIS  was  conducted  to  evaluate  the  e/uniFB00ects  of  surface  chemistry  modification  on  the  interfacial  properties  during  cycling (Figure  3F),  and  reveal  the  mechanism  for  enhanced  electrochemical performance of LLO-based ASSBs. The equivalent circuit of R(RQ)(RQ)(RQ)Q (Figure S3D, Supporting Information) is  applied  to  fit  the  EIS  spectra.  After  100  cycles  at  0.2  C,  the interfacial  resistance  R LLO | SSE of  the  SCM  LLO  cell  is  121.0 Ω , which is much lower than that of the bare LLO cell (296.2 Ω ), and  therefore  the  improved  electrochemical  performance  for the SCM LLO cell is ascribed to the decreased charge-transfer resistance  at  the  cathode/SSE  interface.  Furthermore,  XAS was  employed  to  understand  the  change  in  interfacial  resistance.  The  Ni  (Figure  S18A,  Supporting  Information)  and Co  (Figure  S18B,  Supporting  Information)  K-edge  XANES spectra  of  the  bare  solid-state  LLO  electrode  display  a  noticeable shift to higher energy when the cell is charged/discharged from the pristine to the 100th cycle at 0.2 C. These results indicate the oxidation of Ni and Co even after discharging to 2.0 V, whereas  the  changes  for  the  solid-state  SCM  LLO  electrode (Figure  S18C,D,  Supporting  Information)  are  less  prominent. The Mn K-edge XANES spectra of the bare solid-state LLO electrode  (Figure  3G)  show  a  noticeable  shape  change  and  shift to  lower  energy  after  cycling,  implying  significant  Mn  reduction  and  structural  transformation. [31a] In  contrast,  the  local environment around Mn in the solid-state SCM LLO electrode (Figure  3H)  can  be  maintained  well  after  cycling.  The  maintained  transition  metal  valences  in  the  SCM  LLO  electrode are  connected  with  the  stable  cation-anion  redox  couples  and high  reversibility  of  the  lithiation/delithiation  process,  suggesting  a  suppressed  side  reaction  at  the  cathode/SSE  interface.  Moreover,  in  the  Fourier  transformed  In  K-edge  EXAFS spectra (Figure 3I), a severe shrink of the average bond length of first shell can be observed for the bare solid-state LLO electrode, demonstrating the oxidation of SSEs. With the interfacial modification, the degeneration of SSEs in the SCM LLO electrode (Figure 3J) can be significantly mitigated during cycling, conforming the protective e/uniFB00ect of surface chemistry modification, which can also be verified by XPS (Figure S19, Supporting Information) and time-of-flight secondary ion mass spectrometry (ToF-SIMS, Figure S20, Supporting Information).

To visualize the structural transformation of cathode materials, Raman spectra were collected for the cycled solidstate electrodes. For the LLO, the broad peak at ≈ 648.8 cm -1 is  ascribed  to  Mn-O  polyhedral  distortion  and  shrinkage of  the  Mn-O  bond,  indicating  the  oxygen-release-induced phase  transition  from  layered  to  spinel-like  structure  after cycling. [34] The  ratio of spinel-like phase  in the cycled solid-state  SCM  LLO  electrode  (Figure  3L)  is  obviously lower than that in the cycled bare solid-state LLO electrode (Figure 3K), suggesting a suppressed phase transition.

www.advmat.de

Moreover, high-resolution transmission electron microscopy (HRTEM) results show that the layered structure disappears and the spinel phase dominates on the surface of bare LLO  (Figure  S21A,  Supporting  Information)  after  cycling, indicating  severe  structural  degradation.  On  the  contrary, only  a  slight  spinel  phase  can  be  detected,  and  primary layered  structure  can  be  maintained  well  for  the  SCM  LLO (Figure  S21B,  Supporting  Information).  These  results  confirm  that  the  surface  structure  of  LLO  can  be  stabilized  by surface chemistry modification.

As  the  structural  degradation  at  the  LLO/SSE  interface  is highly correlated with the stability of lattice oxygen within LLO, first-principles calculations were conducted on the (001) surface of LLO as well as the interface between the (001) surface of LLO and  (010)  surface  of  LPO.  Figure  S22A  (Supporting  Information)  displays  the  relaxed  atomic  structure  of  a  LLO  slab  with top and bottom (001) surfaces, where the lattice oxygen is only bonded by 1) two TM (TM refers to the transition metal) and one Li (Figure S22B, Supporting Information) or 2) three TM (Figure  S22C,  Supporting  Information).  The  formed  Li-O-□ structure ( □ symbolizes a vacancy) in configuration (1), which is similar to the highly active orphaned Li  O  Li structure, can introduce labile oxygen electrons to participate in redox activity during cycling. [35] At  the  interface  between  the  LLO  (001)  surface  and  LPO  (010)  surface  (Figure  S23,  Supporting  Information), the lattice oxygen of LLO is bonded by the P atom and the intense  electron  cloud  sharing  demonstrates  the  strong  covalent interaction between P and O (Figure 3M). Considering the local structure of lattice oxygen, the strong P-O bond can pull the energy of the O 2p states to the lower direction compared to the pristine lattice oxygen (Figure S24, Supporting Information),  indicating reduced oxygen activity. Moreover, the formation energy of oxygen vacancy (O vac ) for the bare LLO and SCM LLO at di/uniFB00erent  delithiation  states  is  presented  in  Figure  3N. In the bare LLO structure, the O vac  formation energy decreases with the delithiation process and O vac  can be created spontaneously when the lithium content is less than 50%, as indicated by the negative value of O vac  formation energy. While the O vac in SCM LLO is also easier to form with the delithiation process, the formation energy is constantly higher than that of bare LLO at any delithiation state, corroborating the higher stability of lattice oxygen due to surface modification.

## 3. Conclusion

In  summary,  to  overcome  the  poor  charge-transfer  kinetics of LLO  in conventional carbon-free solid-state electrodes ( Figure 4 A),  we  rationally  construct  electron  and  lithium-ion transport  networks  in  which  electronically  conducting  pathways  are  established  by  introducing  an  appropriate  amount of  carbon  additives,  and  lithium-ion  transport  barriers  are removed  by  reconstructing  the  LLO/SSE  interface  using  an ALD-based infusion-plus-coating strategy. First, by introducing 5% carbon additive in the solid-state LLO electrodes, the discharge  capacity  is  increased  from  103.7  to  166.9  mAh  g -1 , indicating  that  introducing  carbon  additives  into  solid-state electrodes with low-electronic-conductivity cathode materials  can  establish  high-e/uniFB03ciency  electron  transfer  networks

15214095, 2023, 5, Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202207234 by University Of Chicago Library, Wiley Online Library on [15/05/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com www.advmat.de

Figure 4. Schematic illustrations of the electronic and ionic migration at the interface. A) Conventional carbon-free solid-state LLO electrode. B) Carboncontaining solid-state LLO electrode. C) Carbon-containing solid-state electrode with modified LLO.

(Figure 4B). Second, an infusion-plus-coating strategy is employed to reconstruct the surface and grain boundaries  of  LLO  by  ion-conductive  and  high-voltage-stable  LPO (Figure  4C),  which  not  only  suppresses  the  interfacial  side reaction  between  LLO  and  the  halide  SSE  (LIC)  but  also inhibits the phase degradation of LLO from layered to spinel. As  a  result,  LLO-based  ASSBs  with  LIC  demonstrate  a  high discharge  capacity  of  230.7  mAh  g -1 at  0.1  C  and  long  cycle life of 431 cycles. This solid-state electrode design provides an essential  reference  for  upgrading  the  electrochemical  performance of other ASSBs, whose cathode materials may possess low electronic conductivity and highly active surfaces.

## 4. Experimental Section

Detailed  information  is  in  the  Supporting  Experimental  Section  of  the Supporting Information.

## Supporting Information

Supporting  Information  is  available  from  the  Wiley  Online  Library  or from the author.

## Acknowledgements

This work was supported by Natural Sciences and Engineering Research Council  of  Canada  (NSERC),  Canada  Research  Chair  Program  (CRC),

Canada Foundation for Innovation (CFI), Ontario Research Fund (ORF), China  Automotive  Battery  Research  Institute  Co.,  Ltd.,  Glabat  SolidState  Battery  Inc.,  Canada  Light  Source  at  University  of  Saskatchewan (CLS), and University of Western Ontario. R.Y. and H.D. appreciate the support of Mitacs through the Mitacs Accelerate program. R.Y. thanks research  start-up  funds  from  Ningbo  University  of  Technology  (Grant No. 3090011540010). R.Y. appreciates Bing Wu at University of Chemistry and Technology, Prague, for discussing the computational analysis and Jing Xia at Tianjin University for figure art work.

## Conflict of Interest

The authors declare no conflict of interest.

## Author Contributions

R.Y.,  C.W.,  H.D.,  M.J.,  and  A.Z.  contributed  equally  to  this  work.  R.Y . conceptualized  the  study.  R.Y.,  C.W.,  M.J.,  A.Z.,  Y .S.,  and  Y .Z.  were associated with methodology. R.Y., C.W., H.D., M.J., A.Z., J.Z., Y.W., J.L., J.F.,  S.D.,  Z.R.,  G.L.,  and  N.C.  performed  investigations.  R.Y .  wrote  the original  draft.  C.W.,  H.D.,  M.J.,  A.F.,  Y .S.,  and  J.F.  reviewed  and  edited the  final  manuscript.  X.S.  acquired  funding.  H.H.  and  R.L.  acquired resources.  J.W.,  X.L.,  C.V.S.,  and  X.S.  supervised  the  study.  All  authors have approved the final version of the manuscript.

## Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

www.advancedsciencenews.com

## Keywords

all-solid-state batteries, charge-transfer kinetics, lithium-rich layered oxide, oxygen redox, solid-state halide electrolyte

Received: August 9, 2022

Revised: November 22, 2022 Published online: December 18, 2022

- [1]  a)  A.  Manthiram,  X.  Yu,  S.  Wang, Nat.  Rev.  Mater. 2017 , 2 , 1; b) X. Feng, H. Fang, N. Wu, P. Liu, P. Jena, J. Nanda, D. Mitlin, Joule 2022 , 6 , 543.
- [2]  a)  N.  Kamaya,  K.  Homma, Y. Yamakawa, M. Hirayama, R. Kanno, M.  Yonemura,  T.  Kamiyama,  Y.  Kato,  S.  Hama,  K.  Kawamoto, A.  Mitsui, Nat.  Mater. 2011 , 10 ,  682;  b)  Y .  Kato,  S.  Hori,  T .  Saito, K. Suzuki, M. Hirayama, A. Mitsui, M. Yonemura, H. Iba, R. Kanno, Nat. Energy 2016 , 1 , 1.
- [3]  R.  Murugan,  V.  Thangadurai,  W.  Weppner, Angew.  Chem.  Int.  Ed. 2007 , 46 , 7778.
- [4]  a) T. Asano, A. Sakai, S. Ouchi, M. Sakaida, A. Miyazaki, S.  Hasegawa, Adv.  Mater. 2018 , 30 ,  1803075;  b)  X.  Li,  J.  Liang, J. Luo, M. N. Banis, C. Wang, W. Li, S. Deng, C. Yu, F. Zhao, Y. Hu, T.-K. Sham, L. Zhang, S. Zhao, S. Lu, H. Huang, R. Li, K. R. Adair, X. Sun, Energy Environ. Sci. 2019 , 12 , 2665; c) X. Li, J. Liang, N. Chen, J.  Luo,  K.  R.  Adair,  C.  Wang,  M.  N.  Banis,  T.-K.  Sham,  L.  Zhang, S. Zhao, S. Lu, H. Huang, R. Li, X. Sun, Angew. Chem. Int. Ed. 2019 , 58 ,  16427;  d)  J.  Liang,  X.  Li,  S.  Wang,  K.  R.  Adair,  W.  Li,  Y .  Zhao, C. Wang, Y. Hu, L. Zhang, S. Zhao, S. Lu, H. Huang, R. Li, Y. Mo, X. Sun, J.  Am. Chem. Soc. 2020 , 142 ,  7012; e) L. Zhou, C. Y. Kwok, A.  Shyamsunder,  Q.  Zhang,  X.  Wu,  L.  F.  Nazar, Energy  Environ. Sci. 2020 , 13 ,  2056; f) J. Park, D. Han, H. Kwak, Y. Han, Y. J. Choi, K.-W. Nam, Y. S. Jung, Chem. Eng. J. 2021 , 425 , 130630; g) J. Liang, E.  van  der  Maas,  J.  Luo,  X.  Li,  N.  Chen,  K.  R.  Adair,  W.  Li,  J.  Li, Y. Hu, J. Liu, L. Zhang, S. Zhao, S. Lu, J. Wang, H. Huang, W. Zhao, S.  Parnell,  R.  I.  Smith,  S.  Ganapathy,  M.  Wagemaker,  X.  Sun, Adv. Energy Mater. 2022 , 12 , 2103921; h) H. Kwak, S. Wang, J. Park, Y. Liu, K. T. Kim, Y. Choi, Y . Mo, Y . S. Jung, ACS Energy Lett. 2022 , 7 , 1776.
- [5]  a)  S.  Kim,  H.  Oguchi,  N.  Toyama,  T.  Sato,  S.  Takagi,  T.  Otomo, D. Arunkumar, N. Kuwata, J. Kawamura, S.-I. Orimo, Nat. Commun. 2019 , 10 ,  1;  b)  J.  Cuan,  Y .  Zhou,  T .  Zhou,  S.  Ling,  K.  Rui,  Z.  Guo, H. Liu, X. Yu, Adv. Mater. 2019 , 31 , 1803533.
- [6]  S.  Wang,  Q.  Bai,  A.  M.  Nolan,  Y .  Liu,  S.  Gong,  Q.  Sun,  Y .  Mo, Angew. Chem. Int. Ed. 2019 , 58 , 8039.
- [7]  a) K. Wang, Q. Ren, Z. Gu, C. Duan, J. Wang, F. Zhu, Y. Fu, J. Hao, J.  Zhu,  L.  He,  C.-W.  Wang,  Y .  Lu,  J.  Ma,  C.  Ma, Nat.  Commun. 2021 , 12 , 1; b) H. Kwak, D. Han, J. Lyoo, J. Park, S. H. Jung, Y. Han, G.  Kwon,  H.  Kim,  S.-T.  Hong,  K.-W.  Nam,  Y .  S.  Jung, Adv.  Energy Mater. 2021 , 11 , 2003190.
- [8]  A. Sakuda, A. Hayashi, M. Tatsumisago, Sci. Rep. 2013 , 3 , 1.
- [9]  a)  L.  Wang,  X.  Sun,  J.  Ma,  B.  Chen,  C.  Li,  J.  Li,  L.  Chang,  X.  Yu, T.-S.  Chan,  Z.  Hu,  M.  Noked,  G.  Cui, Adv.  Energy  Mater. 2021 , 11 ,  2100881;  b)  C.  Wang,  J.  Liang,  M.  Jiang,  X.  Li,  S.  Mukherjee, K.  Adair,  M.  Zheng,  Y .  Zhao,  F.  Zhao,  S.  Zhang,  R.  Li,  H.  Huang, S. Zhao, L. Zhang, S. Lu, C. V. Singh, X. Sun, Nano Energy 2020 , 76 , 105015.
- [10]  a)  C.  Wang,  R.  Yu,  S.  Hwang,  J.  Liang,  X.  Li,  C.  Zhao,  Y .  Sun, J.  Wang,  N.  Holmes,  R.  Li,  H.  Huang,  S.  Zhao,  L.  Zhang,  S.  Lu, D.  Su,  X.  Sun, Energy  Storage  Mater. 2020 , 30 ,  98;  b)  T.  Wang, J.  Duan,  B.  Zhang,  W.  Luo,  X.  Ji,  H.  Xu,  Y .  Huang,  L.  Huang, Z.  Song,  J.  Wen,  C.  Wang,  Y .  Huang,  J.  B.  Goodenough, Energy Environ. Sci. 2022 , 15 , 1325.
- [11]  L.  Zhou,  T.-T.  Zuo,  C.  Y .  Kwok,  S.  Y .  Kim,  A.  Assoud,  Q.  Zhang, J. Janek, L. F. Nazar, Nat. Energy 2022 , 7 , 83.

www.advmat.de

- [12]  Y .-G.  Lee,  S.  Fujiki,  C.  Jung,  N.  Suzuki,  N.  Yashiro,  R.  Omoda, D.-S. Ko, T. Shiratsuchi, T. Sugimoto, S. Ryu, J. H. Ku, T. Watanabe, Y. Park, Y . Aihara, D. Im, I. T. Han, Nat. Energy 2020 , 5 , 299.
- [13]  a)  Y .  Lyu,  X.  Wu,  K.  Wang,  Z.  Feng,  T.  Cheng,  Y .  Liu,  M.  Wang, R.  Chen,  L.  Xu,  J.  Zhou,  Y .  Lu,  B.  Guo, Adv.  Energy  Mater. 2021 , 11 ,  2000982; b) H.-J. Noh, S. Youn, C. S. Yoon, Y.-K. Sun, J.  Power Sources 2013 , 233 ,  121;  c)  J.  Li,  A.  R.  Cameron,  H.  Li,  S.  Glazier, D. Xiong, M. Chatzidakis, J. Allen, G. A. Botton, J. R. Dahn, J. Electrochem. Soc. 2017 , 164 , A1534; d) H.-H. Ryu, K.-J. Park, C. S. Yoon, Y.-K. Sun, Chem. Mater. 2018 , 30 , 1155; e) W. Mo, Z. Wang, J. Wang, X. Li, H. Guo, W. Peng, G. Yan, Chem. Eng. J. 2020 , 400 , 125820.
- [14]  C. Wang, R. Yu, H. Duan, Q. Lu, Q. Li, K. R. Adair, D. Bao, Y. Liu, R. Yang, J. Wang, S. Zhao, H. Huang, X. Sun, ACS Energy Lett. 2022 , 7 , 410.
- [15]  J.-L. Shi, J.-N. Zhang, M. He, X.-D. Zhang, Y .-X. Yin, H. Li, Y .-G. Guo, L. Gu, L.-J. Wan, ACS Appl. Mater. Interfaces 2016 , 8 , 20138.
- [16]  a) R. Malik, Joule 2017 , 1 , 647; b) S. Zhao, K. Yan, J. Zhang, B. Sun, G.  Wang, Angew.  Chem.  Int.  Ed. 2021 , 60 ,  2208;  c)  M.  Zhang, D. A. Kitchaev,  Z.  Lebens-Higgins,  J.  Vinckeviciute,  M.  Zuba, P. J. Reeves, C. P. Grey, M. S. Whittingham, L. F. J. Piper, A. Van der Ven, Y. S. Meng, Nat. Rev. Mater. 2022 , 7 , 522.
- [17]  a)  R.  Yu,  M.  N.  Banis,  C.  Wang,  B.  Wu,  Y .  Huang,  S.  Cao,  J.  Li, S.  Jamil,  X.  Lin,  F.  Zhao,  W.  Lin,  B.  Chang,  X.  Yang,  H.  Huang, X.  Wang,  X.  Sun, Energy  Storage  Mater. 2021 , 37 ,  509;  b)  M.  Gao, C.  Yan,  Q.  Shao,  J.  Chen,  C.  Zhang,  G.  Chen,  Y .  Jiang,  T.  Zhu, W. Sun, Y. Liu, M. Gao, H. Pan, Small 2021 , 17 , 2008132.
- [18]  a) P. Ghosh, S. Mahanty, R. N. Basu, Mater. Chem. Phys. 2008 , 110 , 406; b) S. Wang, M. Yan, Y. Li, C. Vinado, J. Yang, J.  Power Sources 2018 , 393 , 75.
- [19]  F.  Kong,  R.  C.  Longo,  M.-S.  Park,  J.  Yoon,  D.-H.  Yeon,  J.-H.  Park, W.-H.  Wang,  S.  Kc,  S.-G.  Doo,  K.  Cho, J.  Mater.  Chem.  A 2015 , 3 , 8489.
- [20]  W. Zhang, T. Leichtweiß, S. P. Culver, R. Koerver, D. Das, D. A. Weber, W. G. Zeier, J. Janek, ACS Appl. Mater. Interfaces 2017 , 9 , 35888.
- [21]  a) Y . Zhu, X. He, Y . Mo, ACS Appl. Mater. Interfaces 2015 , 7 , 23685; b) C. Yu, S. Ganapathy, J. Hageman, L. van Eijck, E. R. H. van Eck, L. Zhang, T. Schwietert, S. Basak, E. M. Kelder, M. Wagemaker, ACS Appl.  Mater.  Interfaces 2018 , 10 ,  33296;  c)  K.  Yamamoto,  S.  Yang, M.  Takahashi,  K.  Ohara,  T.  Uchiyama,  T.  Watanabe,  A.  Sakuda, A.  Hayashi,  M.  Tatsumisago,  H.  Muto,  A.  Matsuda,  Y.  Uchimoto, ACS Appl. Energy Mater. 2021 , 4 , 2275.
- [22]  a)  E.  McCalla,  A.  M.  Abakumov,  M.  Saubanère,  D.  Foix,  J.  Berg Erik,  G.  Rousse,  M.-L.  Doublet,  D.  Gonbeau,  P.  Novák,  G.  Van Tendeloo,  R.  Dominko,  J.-M.  Tarascon, Science 2015 , 350 ,  1516; b)  K.  Luo,  M.  R.  Roberts,  N.  Guerrini,  N.  Tapia-Ruiz,  R.  Hao, F. Massel, D. M. Pickup, S. Ramos, Y.-S. Liu, J. Guo, A. V. Chadwick, L.  C.  Duda,  P.  G.  Bruce, J.  Am.  Chem.  Soc. 2016 , 138 ,  11211; c) R. A. House, G. J. Rees, M. A. Pérez-Osorio, J.-J. Marie, E. Boivin, A. W. Robertson, A. Nag, M. Garcia-Fernandez, K.-J. Zhou, P. G. Bruce, Nat. Energy 2020 , 5 , 777.
- [23]  a)  P.  Yan,  J.  Zheng,  Z.-K.  Tang,  A.  Devaraj,  G.  Chen,  K.  Amine, J.-G.  Zhang,  L.-M.  Liu,  C.  Wang, Nat.  Nanotechnol. 2019 , 14 , 602;  b)  A.  Grenier,  G.  E.  Kamm,  Y .  Li,  H.  Chung,  Y .  S.  Meng, K. W. Chapman, J. Am. Chem. Soc. 2021 , 143 , 5763.
- [24]  Y . Xia, J. Zheng, C. Wang, M. Gu, Nano Energy 2018 , 49 , 434.
- [25]  a) F. Strauss, T. Bartsch, L. de Biasi, A. Y . Kim, J. Janek, P. Hartmann, T.  Brezesinski, ACS  Energy  Lett. 2018 , 3 ,  992;  b)  P.  Minnmann, L. Quillman, S. Burkhardt, F. H. Richter, J. Janek, J. Electrochem. Soc. 2021 , 168 ,  040537; c) W. Jiang, X. Zhu, R. Huang, S. Zhao, X. Fan, M. Ling, C. Liang, L. Wang, Adv. Energy Mater. 2022 , 12 , 2103473.
- [26]  C.  L.  Bender,  P.  Hartmann,  M.  Vračar,  P.  Adelhelm,  J.  Janek, Adv. Energy Mater. 2014 , 4 , 1301863.
- [27]  a) W. Zhang, D. A. Weber, H. Weigand, T. Arlt, I.  Manke, D.  Schröder,  R.  Koerver,  T.  Leichtweiss,  P.  Hartmann,  W.  G.  Zeier,

## www.advancedsciencenews.com

- J.  Janek, ACS  Appl.  Mater.  Interfaces 2017 , 9 ,  17835;  b)  B.  Zahiri, A. Patra, C. Kiggins, A. X. B. Yong, E. Ertekin, J. B. Cook, P. V. Braun, Nat. Mater. 2021 , 20 , 1392.
- [28]  a) H. Koga, L. Croguennec, M. Ménétrier, P. Mannessiez, F. Weill, C. Delmas, S. Belin, J. Phys. Chem.  C 2014 , 118 , 5700;  b)  C.  Cui,  X.  Fan,  X.  Zhou,  J.  Chen,  Q.  Wang,  L.  Ma, C. Yang, E. Hu, X.-Q. Yang, C. Wang, J.  Am. Chem. Soc. 2020 , 142 , 8918.
- [29]  J.  Rana,  R.  Kloepsch,  J.  Li,  T.  Scherb,  G.  Schumacher,  M.  Winter, J. Banhart, J. Mater. Chem. A 2014 , 2 , 9099.
- [30]  S. Tao, W. Huang, S. Chu, B. Qian, L. Liu, W. Xu, Mater. Today Phys. 2021 , 18 , 100403.

Adv. Mater. 2023 , 35 , 2207234

www.advmat.de

- [31]  a)  E.  Hu,  X.  Yu,  R.  Lin,  X.  Bi,  J.  Lu,  S.  Bak,  K.-W .  Nam,  H.  L.  Xin, C.  Jaye,  D.  A.  Fischer,  K.  Amine,  X.-Q.  Yang, Nat.  Energy 2018 , 3 , 690; b) G. Assat, J.-M. Tarascon, Nat. Energy 2018 , 3 , 373.
- [32]  a)  R.  Robert,  P.  Novák, J.  Electrochem.  Soc. 2015 , 162 ,  A1823; b) C. R. Fell, D. Qian, K. J. Carroll, M. Chi, J. L. Jones, Y . S. Meng, Chem. Mater. 2013 , 25 , 1621.
- [33]  T. Lin, T. U. Schulli, Y . Hu, X. Zhu, Q. Gu, B. Luo, B. Cowie, L. Wang, Adv. Funct. Mater. 2020 , 30 , 1909192.
- [34]  X. Ding, D. Luo, J. Cui, H. Xie, Q. Ren, Z. Lin, Angew. Chem. Int. Ed. 2020 , 59 , 7778.
- [35]  D.-H. Seo, J. Lee, A. Urban, R. Malik, S. Kang, G. Ceder, Nat. Chem. 2016 , 8 , 692.