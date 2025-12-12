Halide-based solid electrolytes are currently growing in interest in solidstate batteries due to their high electrochemical stability window compared to sulfide electrolytes. However, often a bilayer separator of a sulfide and a halide is used and it is unclear why such setup is necessary, besides the instability of the halides against lithium metal. It is shown that an electrolyte bilayer improves the capacity retention as it suppresses interfacial resistance growth monitored by impedance spectroscopy. By using in-depth analytical characterization of buried interphases by time-of-flight secondary ion mass spectrometry and focused ion beam scanning electron microscopy analyses, an indium-sulfide rich region is detected at the halide and sulfide contact area, visualizing the chemical incompatibility of these two electrolytes. The results highlight the need to consider more than just the electrochemical stability of electrolyte materials, showing that chemical compatibility of all components may be paramount when using halide-based solid electrolytes in solid-state batteries.

C. Rosenbach, J. Ruhl, M. Hartmann, W. G. Zeier Institute of Inorganic and Analytical Chemistry University of Münster (WWU)

Corrensstrasse 28/30, 48149 Münster, Germany E-mail: wzeier@uni-muenster.de

F. Walther, J. Janek

Institute of Physical Chemistry &amp; Center for Materials Research (ZfM/LaMa) Justus-Liebig-University

Heinrich-Bu/uniFB00-Ring 17, 35392 Giessen, Germany

E-mail: Juergen.Janek@phys.Chemie.uni-giessen.de

T. A. Hendriks, W. G. Zeier Institut für Energie- und Klimaforschung (IEK) IEK-12: Helmholtz-Institut Münster Forschungszentrum Jülich Corrensstaße 46, 48149 Münster, Germany

S. Ohno

Department of Applied Chemistry

Graduate School of Engineering

Kyushu University

744 Motooka, Nishi-ku, Fukuoka 819-0395, Japan

The ORCID identification number(s) for the author(s) of this article can be found under https://doi.org/10.1002/aenm.202203673.

© 2022 The Authors. Advanced Energy Materials published by WileyVCH GmbH. This is an open access article under the terms of the Creative Commons Attribution-NonCommercial License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial purposes.

DOI: 10.1002/aenm.202203673

www.advenergymat.de

## Visualizing the Chemical Incompatibility of Halide and Sulfide-Based Electrolytes in Solid-State Batteries

Carolin Rosenbach, Felix Walther, Justine Ruhl, Matthias Hartmann, Theodoor Anton Hendriks, Saneyuki Ohno, Jürgen Janek,* and Wolfgang G. Zeier*

## 1. Introduction

Due  to  the  increasing  energy  consumption and need for energy storage, lithiumion  batteries  have  become  the  most  used battery technology for commercial applications. This widely used cell concept with a liquid electrolyte is close to the limits of its energy density which and a certain degree of safety concerns due to the flammability of organic solvents. [1] These disadvantages  may  be  overcome  using  solid-state batteries. [1-3] By using inorganic solid electrolytes  that  exhibit  high  ionic  conductivities  in  the  mS  cm -1 range,  organic solvents may be replaced. [4-6] A  solid  electrolyte  class  that  fulfills  the  requirement of high ionic conductivity are sulfidebased  materials  of  argyrodite  type  such as  Li 6 PS5X  (X = Cl,  Br,  I), [7-9] Li3PS4 [10,11] or  Li 10 GeP2S12. [12,13] Based  on  their  high ionic  conductivity,  stability  against  In/LiIn  anode  and  advantageous  mechanical  properties  (e.g.,  malleability),  these  sulfides are prominently used as electrolytes in solid-state battery studies. [2,14-18]   Unfortunately,  these  compounds  have  a  narrow thermodynamic  stability  window,  leading  to  limitations  in  the cathode  due  to  decomposition  reactions, [2,16,19] for  example  the electrolyte  Li 6 PS5Cl  with  LiNi 0.6 Co0.2 Mn 0.2 O2  lead  to  PO x and SOx. [19] A  promising  class  of  solid  electrolytes  are  halide-based materials with increased stability against typical cathode active materials  (CAM),  rediscovered  by  Asano  et  al.  in  2018  using mechanochemical  syntheses. [20]   These  compounds  exhibit  a wide range of compositions of the formula Li 6 MX 6  (M 3 + = metal, X = Cl,  Br,  I), [21-24] for  example  Li 3 InCl6, [25,26] Li3YCl6 [27,28] or Li 2 Sc2/3 Cl4 , [29]   and show reasonable ionic conductivity values of mS cm -1 at  room temperature. [21-30]   Based on their wider thermodynamic stability window and with it their suggested higher electrochemical stability against CAMs, when compared to the sulfide materials, this material class might be more suitable for the use in solid-state batteries with high voltage CAMs. [30,31]  Nevertheless,  recent  work  shows  that  while  the  halides  may  show high  electrochemical  stability  (stability  against  a  certain  oxidation potential), [32] chemical stability (stability of the di/uniFB00erent cell components against side reactions) is not necessarily given. [33-35] Li 3 InCl6  is  suggested  to  have  both  a  high  electrochemical  stability  window [30] and  reasonable  conductivity  of  greater  than 1 mS cm -1 . [25,26] However, Li 3 InCl6 is not stable against lithium metal  and  decomposes,  inhibiting  its use as separator in

www.advancedsciencenews.com

Figure 1. Scheme  of  the  di/uniFB00erent  cell  setups  with  di/uniFB00erent  separator and cathode composite combinations and LiNi0.8Co0.1Mn0.1O2 as CAM (black). Cell setup A with Li 6PS5Cl (orange) as the separator and catholyte:  In/LiIn | Li 6 PS5Cl | Li 6 PS5Cl:LiNi 0.8 Co0.1 Mn0.1O2.  Cell  setup  B  with Li 6 PS5Cl as separator and Li 3 InCl 6 (blue) as catholyte: In/LiIn | Li 6 PS5Cl | Li 3 InCl 6 :LiNi 0.8 Co0.1 Mn0.1O2. Cell setup C with Li 6 PS5Cl | Li 3 InCl 6 as bilayer separator and Li 3 InCl 6 as catholyte: In/LiIn | Li 6 PS5Cl | Li 3 InCl 6 | Li 3 InCl 6 : LiNi0.8 Co0.1Mn0.1O2.

solid-state  batteries. [36] First  cell  studies  with  Li 3 InCl6  only  as catholyte,  together  with  LiNi 0.8 Co0.1Mn0.1O2  or  LiCoO2  show decent  capacity  values. [25,26] Clearly,  Li 3 InCl6  is  an  interesting candidate  as  catholyte,  but  an  additional  sulfide  layer  is  often used  to  prevent  the  halide  decomposition  in  direct  contact  to the  lithium  metal  anode. [25] Recently,  a  bi-layer  approach  has been increasingly used for the construction of separators, with a sulfide-based material contacting the anode and a halide solid electrolyte contacting the halide-based cathode composite. [33,37-39] This bilayer approach seems to disagree with the overall goal of creating thinner separator layers for practical use of solid-state batteries.  It  is  also  in  stark  contrast  to  simple  processing  on large  scale.  In  addition,  it  was  recently  found  that  the  incompatibility  of  Li 3 InCl6 and Li6 PS 5 Cl  in  LiNi 0.6 Co0.2 Mn 0.2O2-based cells  lead  to  decomposition  products  and  higher  interfacial resistance, [34,35] suggesting  possible  issues  with  this  approach. Nevertheless,  no  direct  analyses  of  any  ongoing  chemical  and electrochemical processes have been established to explain the chemical processes occurring at the respective interfaces.

Inspired  by  the  question  of  why  a  bilayer  separator  is  often used  and  what  happens  when  it  is  missing,  in  this  work,  we study  the  halide  electrolyte  Li 3 InCl6  in  combination  with  the CAM LiNi0.8Co0.1Mn0.1O2  and  the  separator  material  Li 6 PS 5 Cl. By choosing di/uniFB00erent solid-state battery setups (see Figure 1 ), we aim to better understand the influence of this additional layer. Electrochemical impedance spectroscopy and long-term cycling suggest  that  without  the  additional  halide  electrolyte  layer, decomposition  reactions  occur  between  the  sulfide  solid  electrolyte and the halide-based cathode composite. Although chemical analyses of buried interfaces are typically challenging, here we  were  able  to  analyze  the  ongoing  reaction  at  the  separator | cathode  composite  interphase.  With  ToF-SIMS  (time-of-flight secondary ion mass spectrometry), FIB-SEM (focused ion beam scanning  electron  microscopy)  analyses  and  with  XPS  (X-ray photoelectron  spectroscopy)  analyses  the  existence  of  indium sulfide-based  decomposition  products  is  confirmed.  Overall, this  work  serves  to  show  that  the  use  of  halide  catholytes  in solid-state  batteries  may  not  be  as  straightforward  as  currently believed, and that some unwanted decomposition pathways still exist  and  need  to  be  considered  in  the  search  for  new  halide electrolytes.

## 2. Results

To  reveal  the  reason  for  the  typically  used  bilayer  separator design  and  the  underlying  processes  at  the  interfaces,  in  this study, the solid electrolytes Li 6PS5Cl and Li3InCl6 were used as separator material and catholyte in di/uniFB00erent cell configurations. The following three di/uniFB00erent  cell  configurations  are  used  and schematically shown in Figure 1:

Notation: anode | separator | composite cathode,

- A.  Cell setup A: In/LiIn | Li 6PS5Cl | LiNi 0.8 Co0.1 Mn0.1O2:Li6 PS 5 Cl,
- B.  Cell setup B: In/LiIn | Li 6PS5Cl | LiNi 0.8 Co0.1 Mn0.1O2:Li3 InCl 6 , and
- C.  Cell setup C: In/LiIn | Li 6PS5Cl | Li 3 InCl6 | LiNi 0.8 Co0.1 Mn0.1O2: Li 3 InCl6.

Both  solid  electrolytes  were  successfully  synthesized  and exhibited  ionic  conductivity  values  at  25 ° C  similar  to  those reported in the literature, namely σ (Li 6 PS5Cl) = 1.3 mS cm -1[7,15,40] and σ (Li 3 InCl6) = 0.7 mS cm -1 . [22,25,26] The In/LiIn alloy is used as counter electrode to ensure a stable potential and no ongoing decomposition that would convolute the impedance analyses. [41] Detailed experimental information, refined X-ray di/uniFB00ractograms and  the  impedance  spectra  can  be  found  in  the  Supporting Information and Figures S1 and S2 (Supporting Information).

## 2.1. Cell Cycling

All cell configurations were cycled between 2.0 and 3.7 V versus In/LiIn,  corresponding  to  2.6  V  and  4.3  V  versus  Li + /Li,  with a  current  density  of  0.214  mA  cm -2 . Figure 2 a-c  shows  the potential  profiles  for  the  charging  and  discharging  steps  of the three di/uniFB00erent cell setups. The pure sulfide-based cell (cell setup  A,  orange)  shows  the  highest  initial  charge  capacity  of 217 mAh g -1  (2.32 mAh cm -2 ), followed by the halide cell with Li 3 InCl6  in  the  cathode  composite  (cell  setup  B,  green)  with 200  mAh g -1   (1.83  mAh  cm -2 )  and  the  bilayer-based  cell  (cell setup C, blue) with 176 mAh g -1  (1.61 mAh cm -2 ). The lower initial charge capacity for cell setup C is likely due to higher bulk resistance caused by the comparably thick bilayer separator (see next section). The initial discharge capacity for all cells is 163, 175, and 154 mAh g -1 ,  for cell setups A, B, and C, respectively. The  trend  of  the  discharge  capacities  and  the  Coulomb  e/uniFB03ciencies are shown for 100 cycles in the Figure S3 (Supporting Information).  The  di/uniFB00erences  in  initial  charge  and  discharge capacities are common in solid-state batteries and mainly result from  irreversible  structural  rearrangement,  chemo-mechanical  e/uniFB00ects  and  loss  of  available  lithium. [42-44] In  addition,  the cathode material is prone to react with the sulfides electrolyte forming oxides such as POx or SOx in the case of Li6PS5Cl. [19] Potential chemical decomposition of the halides has also been reported, [33] especially  with  Zr-based  compounds  that  are  very oxyphilic and attack the active material. Overall, the three cell setups  show  a  trend  comparable  in  performance  to  literature.  Accordingly,  pure  sulfide  cells  with  high  nickel  content LiNix Co y MnzO2  typically  show  high  initial  capacities  of  over 200 mAh g -1 . [45]  In comparison, halide-based cells usually show lower initial capacity values. For example, a carbon-containing

www.advenergymat.de

www.advancedsciencenews.com

www.advenergymat.de

Figure 2. Charge and discharge curves of cell setups a) A, b) B and c) C, cycled at 25 ° C. The figures show the 1st, 2nd, 10th, 20th, 30th, 40th, 50th, 60th, 70th, 80th, 90th and 100th cycle of the cells colorized from darker to lighter color.

LiNi0.6 Co0.2 Mn 0.2 O2- and Li3 InCl 6-based composite cathode has shown an initial charge capacity of 166 mAh g -1 , [34]   whereas a LiNi0.85 Co0.1 Mn0.05O2-  and  Li 3 InCl6-based  composite  exhibited an  initial  charge  capacity  slightly  under  200  mAh  g -1 . [33] The general shape of the charge/discharge curves is similar for all setups and is characteristic for the CAM. For example, the plateau in the charge curve at around 3.6 V (vs In/InLi) is typical for  LiNi 0.8 Co0.1 Mn0.1O2  showing  the  conversion  from  the  hexagonal H2 phase to the other hexagonal H3 phase. [43]

The overall capacity values from the first to the 100th cycle are  shown for all  cell  setups  in Figure 3 .  The  charge  capacity of  cell  setup  A  (orange)  decreases  from  217  to  122  mAh  g -1 , showing an overall loss in capacity of 44 %. Cell setup B (green) shows  the  strongest  capacity  fading  over  cell  cycling  with  an overall capacity loss of 86 % (200 to 29 mAh g -1 ). By using the additional Li 3 InCl6 layer (cell setup C, blue) the capacity loss is significantly reduced to 40 % (176 to 105 mAh g -1 ), highlighting the beneficial e/uniFB00ect  of  the  bilayer  separator  design.  The  more stable cell cycling behavior of cell setups A and C compared to cell  setup  B  is  also  reflected  in  the  Coulomb  e/uniFB03ciencies  (see

Figure  S3b,  Supporting  Information).  Accordingly,  the  Coulomb  e/uniFB03ciencies  of  cell  setup  B  scatter  strongly,  while  they are more stable for the other two setups, indicating less detrimental side reactions in the latter cases. The more pronounced capacity fading upon cell cycling (Figure 3a) can be correlated to  the  average  overpotential  (Figure  3b).  While  extracting  the average  potential  between  2.7  and  3.7  V  during  charging  as  a function  of  the  cycle  number,  cell  setup  B  has  the  strongest increase compared to cell setup A and C.

Overall, based on the capacities and Coulomb e/uniFB03ciencies, the sulfide  electrolyte-based  cell  shows  the  best  performance.  The beneficial e/uniFB00ect of the bilayer separator design for halide-based composite  cathodes  is  clearly  evident  from  a  reduced  capacity fading and a slower overpotential evolution upon cell cycling.

## 2.2. Impedance Analyses

To  understand  the  underlying  processes  within  the  three  different cell setups in more detail, impedance data were collected

Figure 3. a) Charge capacities and b) average overpotential of the charging step, showing the most severe degradation when the halide catholyte is in direct contact to the sulfide separator.

www.advancedsciencenews.com

www.advenergymat.de

Figure 4. Nyquist plots of the impedance data (b-g) and the equivalent circuit used for fitting (a). Shown are spectra after the 1st and 100th cycle. b,c) shows the impedance data for cell setup A (orange), d,e) for cell setup B (green) and f,g) for cell setup C (blue). Three microscopic transport/ transfer steps are assigned to the semicircles: R interface,1 (yellow), R interface,2  (red) and R SE/anode (purple).

during  cell  cycling.  Therefore,  an  impedance  spectrum  was recorded after each charging and discharging step to quantify the  di/uniFB00erent  processes  occurring  at  the  interfaces  in  the  cells as  a  function  of  time.  The  impedance  data  obtained  after  the 1st  (b,  d,  and  f)  and  the  100th  charging  step  (c,  e,  and  g)  are shown  in  Nyquist  plots  in Figure 4 with  their  corresponding fits. A  potentially insightful approach  to  extract transport parameters would be the use of transmission-line modeling of the  impedance  spectra,  as  has  been  performed  quite  successfully  recently. [41,46-48] While  transmission-line  modeling  in  the here-investigated cells leads to comparable results for the first charge,  the  subsequent  impedance  spectra  of  the  cycling  process  would  require  a  change  in  the  transmission-line  model. At this stage changing fits cannot be corroborated without too many additional  assumptions.  Therefore,  in  order  to  monitor the  impedance  increase  consistently,  the  data  are  analyzed with  the  equivalent  circuit  shown  in  Figure  4a,  assuming four  di/uniFB00erent  transport/transfer  processes  based  on  previous literature. [15,16]

These four processes typically represent in the literature the resistance  of  the  bulk  of  the  electrolyte R SE,bulk (gray),  a  grain boundary-type  resistance  of  the  electrolyte R SE,grain (yellow), the  resistance  of  the  interface  of  the  electrolyte  and  the  CAM R SE/CAM   (red)  and  the  resistance  of  the  interface  of  the  elec- trolyte  to  the  anode  material R SE/anode (purple).  The  di/uniFB00erent processes were assigned based on the obtained capacitances of the di/uniFB00erent semicircles and the frequency range derived from previous impedance data analysis. [14-16,49] In addition, it remains unclear whether the mid-frequency signal really corresponds to the grain boundary contribution or whether it rather represents a geometric constriction e/uniFB00ect in the catholyte. [50] At the lowest frequencies, a Warburg-type impedance behavior was observed, possibly  related  to  lithium  di/uniFB00usion  in  the  active  materials. [14] Within  this  study,  the  di/uniFB00erent  extractable  resistances  were named R 1 , R 2 , R 3 , and R 4  to avoid a direct relation to the physical process (see below). This is needed as the term R SE/CAM  will not be directly the correct terminology to this interface process here  (see  later  section).  The  fit  results  of  the  resistances,  the capacitances, α -values  (exponent  of  the  constant  phase  element) as well as the frequency ranges of the assigned processes can be found in Table S1 (Supporting Information). The values obtained are in the range of previous works, indicating a strong overlap of relaxation times of the di/uniFB00erent processes. [14-16,49]

The  first  resistance R 1 in  the  high-frequency  range  can  be reliably  assigned  to R separator (gray)  for  all  spectra  and  corresponds to a pre-resistance R in the equivalent circuit (Figure 4a). After the first charge, this resistance is comparably high for cell setup  C,  indicating  that  the  additional  halide  layer  (and  thus

www.advancedsciencenews.com

www.advenergymat.de

Figure 5. Resistances extracted from the fitted impedance data a) R separator tenth cycle from the 1st cycle to the 100th cycle.

, b) R interface  for cell setup A (orange), B (green), and C (blue) over every

thicker  separator)  causes  to  a  higher  total  bulk  resistance.  In contrast, cell setup A and B show similar low values after the first charge. In the middle frequency range, two resistances R 2 and R 3  are found. As discussed above, these are typically related to grain boundaries and the resistance at the CAM in the composite cathode, respectively. However, here we will, for the sake of simplicity R interface,1 (yellow) and R interface,2  (red) while keeping in  mind  that  besides  intrinsic  interfaces,  interphases  may  be growing.  Both  related  processes  are  represented  by  a  parallel resistor and constant-phase element (R/CPE) in the equivalent circuit (Figure 4a) and basically distinguished based on their different capacitances (see Tables S1-S3, Supporting Information). However, due to low α -values and a strong overlap of time constants, the separation of the di/uniFB00erent processes is challenging, leading to wider error ranges. Clearly, assigning the processes correctly to the di/uniFB00erent relaxation times becomes di/uniFB03cult with the increasing number of interfaces and resulting interphases. Nevertheless,  for  a  qualitative  discussion  these  processes  are disentangled with keeping in mind that the increase of one will a/uniFB00ect the others. For all three cell setups, the value of R interface,1 remains relatively stable after the first charge for all cell setups, whereas the values for R interface,2 for cell setup A di/uniFB00er. A higher initial  resistance is found for cell setup A that may be caused either  by  an  irreversible  chemical  reaction  of  the  sulfide  electrolyte  with  the  LiNi 0.8 Co0.1 Mn0.1O2 particles, [16] or  simply  by  a generally higher interfacial impedance. The low frequency processes R 4 can be correlated to R SE/anode   (purple) and contribute the least to the total resistance in all spectra.

For  a  direct  comparison  of  the  three  cell  setups,  the  resistances  obtained  by  fitting  are  shown  as  a  function  of  the  cycle number in Figure 5 . R 1 starts at a similar value for cell setups A and B (orange and green) and shows a comparable increase upon cell cycling. In direct comparison, cell setup A exhibits a slightly reduced  resistance  due  to  the  higher  ionic  conductivity  of  the separator. In contrast, cell setup C (blue) has an initially higher resistance (partially due to the thicker separator) but also shows a more pronounced increase upon cell cycling. This increase of the  bilayer  separator  resistance  has  already  been  reported  for Li 3 InCl6-based  cells  before. [33] The  high  resistance  and  particularly the increase upon cell cycling appears to be caused by the recently reported chemical incompatibility between Li 3 InCl 6  and Li 6 PS5Cl,  which  results  in  the  formation  of  an  interphase  and thus to a higher resistance (see discussion section below). [34,35]

Considering  the  impedance  evolution  of R 2 and R 3 as  a function  of  cycle  number  (Figure  S7a,b,  Supporting  Information),  an  increase  over  time  was  found  in  every  cell  type.  At lower cycle numbers a deconvolution of both processes is challenging, at higher numbers the strongly increasing R 3 makes a deconvolution easier. Nevertheless, as it is di/uniFB03cult to rule out that the fitting of one R-CPE element influences the results of the  other  elements.  Therefore,  for  a  more  indicative  analysis, both  resistances  are  shown  as  their  sum  (Figure  5b).  Overall, the  strongest  changes  are  found  for  cell  setup  B.  Increasing impedances  are  often  caused  by  interfacial  degradation  reactions in solid-state batteries, [14,16,19]  which bears the question of which interface dominates the significant impedance evolution in  the  case  of  cell  setup  B.  The  assignment  of  the  respective frequency range to an interface resistance R interface,2   can imply that the degradation at the Li 3 InCl 6 | LiNi 0.8 Co0.1 Mn0.1O2 interface is causing the almost 50 times higher impedance. [51]  However,  the  halide  electrolyte | CAM  interface  is  supposed  to  be electrochemically  more  stable  compared  to  the  sulfide-based counterpart. [30] In addition, if the halide electrolyte | CAM interface is responsible for the rise in impedance, similar observations  should  be  observable  for  cell  setup  C.  Indeed,  the  only di/uniFB00erence  between cell setup B and C is that of a triple phase boundary of LiNi0.8 Co 0.1 Mn0.1O2, Li 6 PS5Cl, and Li3 InCl 6 ,  which is  avoided  in  cell  type  C  suggesting  that  strong  decomposition  reactions  occur  at  the  interface  between  the  sulfide  separator  and  the  halide-based  cathode  composite.  Clearly  then, an additional layer of Li 3 InCl6 is needed, as it avoids the triple phase boundary and leads to more stability and suppresses fast capacity fading. This will be discussed in the further discussion.

## 2.3. Buried Interface Analyses

To  study  the  origin  of  the  increased  build-up  in  impedance when  halide  catholytes  are  directly  in  contact  with  a  sulfide separator,  cross-sections  of  cycled  cells  of  cell  setup  B  and  C

16146840, 2023, 6, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/aenm.202203673 by Readcube (Labtiva Inc.), Wiley Online Library on [11/12/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

www.advancedsciencenews.com

www.advenergymat.de

Figure 6. a) Scanning electron micrograph of the polished cross-section of a cycled cell of cell setup B with direct interface between sulfide separator and halide-based cathode composite. A backscattered electron image is shown on the left and a secondary electron image on the right. b) ToF-SIMS imaging of the polished cross-section. Shown are exemplary secondary ion images of negatively charged fragments that allow to distinguish the di/uniFB00erent components. The specific secondary ion images are normalized in relation to the total ion intensity to reduce topographic e/uniFB00ects. For the InS -fragment, a binning of 16 pixels was used to increase visibility. Both SEM and ToF-SIMS analyses indicate the formation of an interphase between the composite cathode and the separator.

were investigated by FIB-SEM and ToF-SIMS. Figure 6 a shows scanning  electron  micrographs  of  the  polished  cross-section of  a  cycled  cell  of  cell  setup  B  recorded  with  a  back-scattered electron  (BSE)  and  a  secondary  electron  (secondary)  detector, respectively. The images show a strong curtaining e/uniFB00ect (visible by lines) due to the high roughness of the native cross-sections and related topographic e/uniFB00ects during the milling process. Nevertheless, the composite cathode (top) can be well distinguished from the separator (bottom) with both detectors. Due to di/uniFB00erences  in  atomic  weights  of  the  compounds,  the  BSE  detector allows,  to  a  certain  extent,  the  di/uniFB00erentiation  of  local  changes in  the  composition.  Accordingly,  the  LiNi 0.8 Co0.1 Mn0.1O2 particles (brighter) can be well distinguished from the Li 3 InCl 6  and the Li 6 PS5Cl (darker). Interestingly, an interphase between the composite  cathode  and  the  separator  is  visible,  which  cannot be seen when using the secondary electron detector. The latter suggests  that  this  feature  is  not  due  to  topographical  e/uniFB00ects, but rather has a compositional cause.

To  further  study  the  chemical  nature  of  this  interphase, ToF-SIMS  imaging  was  performed  on  the  crater  sidewall  of the  cycled  cell.  Figure  6b  shows  that  the  various  compounds can  be  well  distinguished  from  each  other.  Accordingly,  the LiNi0.8 Co0.1 Mn0.1O2 particles (represented by O -fragments) are well separated from Li 3 InCl 6  (shows high ionization probability for Cl -and lack of S -fragments) and Li6 PS 5 Cl (represented by Cl -and S -fragments). We found, that the interphase composition is well represented by the InS -fragment. A possible mass interference  with  InO 2 -fragments  can  be  ruled  out,  since  no oxygen-related  fragments  (such  as  O -,  O2 -fragments)  were detected  in  these  areas.  The  local  peak  of  the  InS -fragment count  indicates  the  formation  of  an  indium  sulfide-like  compound in the interfacial region between the composite cathode and  the  separator.  This  in  turn  implies  a  reaction  of  Li 3 InCl6

and  Li 6 PS5Cl  and  thus  a  thermodynamic  instability  of  both materials in contact with each other, which has been suggested recently. [34,35]

Analogous measurements were performed for the cycled cell of cell setup C ( Figure 7 ).  The additional Li 3InCl6 layer makes the sample preparation and analysis further challenging, since the  interfaces/interphases  of  interest  are  buried  even  deeper and  thus  the  region-of-interest  is  much  larger.  Nevertheless, it  was  possible  to  analytically  access  the  composite  cathode | separator  and  the  separator | separator  (Li 6PS5Cl | Li 3 InCl6) interfacial regions separately. While no compositional changes were detected at the composite cathode | separator interface, an enrichment of the InS -fragment was detected at the separator | separator  interface  (Figure  7b),  similar  to  the  observations above. Compared to cell setup B, the fragment exhibits much less  secondary  ion  intensity.  It  is  di/uniFB03cult  to  derive  (semi-) quantitative conclusions from these measurements, since even small deviations in sample geometry and measurement conditions (e.g.,  di/uniFB00erences  in  stray  electric  fields)  can  significantly influence  the  results.  Nevertheless,  it  seems  that  the  reaction of Li 3 InCl6 and Li 6PS5Cl occurs even without the CAM being in close vicinity. As crater milling was not performed under cryo conditions, the highly energetic focused ion beam might be the reason for the apparent reaction between Li 3 InCl 6  and Li 6 PS5Cl. To  rule  this  out,  in-depth  heating  experiments  of  Li 3InCl6/ Li 6PS5Cl  mixtures  complemented  with  XPS  and  ToF-SIMS analyses  were  performed.  In  fact,  these  control  experiments clearly  show  that  the  overserved  reaction  was  not  induced  by the analytical ion beam and a detailed discussion can be found in the Supporting Information.

Overall,  the  combination  of  FIB-SEM,  XPS,  and  ToF-SIMS analyses  confirm  a  chemical  incompatibility  of  Li 3 InCl6  and Li 6 PS5Cl, leading to the formation of an additional interphase

www.advancedsciencenews.com

www.advenergymat.de

Figure 7. a) Scanning electron micrographs of the polished cross-section of a cycled cell of cell setup C. SE images are shown on the left and BSE images on the right. The composite cathode is shown at the top, the bilayer separator at the bottom. b) ToF-SIMS imaging of the interfacial area between Li3InCl6 (top) and Li 6 PS 5Cl (bottom). Shown are exemplary secondary ion images of negatively charged fragments that allow to distinguish the di/uniFB00erent components. The secondary ion images are normalized by the total ion intensity to reduce topographic e/uniFB00ects. For the InS -fragment, a binning of 16 pixels was used to improve contrast. Both SEM and ToF-SIMS analyses indicate the formation of an interphase within the bilayer separator between Li3InCl6  and Li 6 PS5Cl.

between  Li 3 InCl6  and  Li 6 PS5Cl.  The  chemical  reaction  is  predominantly  indicated  by  the  formation  of  indium  sulfide-like species in this study.

## 2.4. Discussion

Overall,  the  electrochemical  testing  in  this  study  reveals  that a  bilayer  separator seems necessary for long-term cycling stability  of  Li3InCl6-based  composite  cathodes  when  combined with  sulfide  electrolyte-based  separators  such  as  Li 6 PS 5 Cl. Accordingly,  using  an  additional  halide  layer  to  separate  the composite  cathode  from  the  sulfide  separator  significantly reduces  the  impedance  evolution  upon  cell  cycling  and  considerably improves the long-term cycling stability. This implies that  the  reason  for  the  pronounced  cell  degradation  without the  bilayer  design  lies  in  the  interfacial  region  between  the Li 6PS5Cl separator and the Li3InCl6-based composite cathode. In  other  words,  the  presence  of  the  CAM  seems  to  play  a strong role. Instrumental analytics confirm that a detrimental chemical reaction of the sulfide and the halide electrolyte at the separator | composite  cathode  interface  causes  these  issues. Our analytical data indicate a general chemical incompatibility of both solid electrolytes, the reaction of which seems to be further promoted by the close vicinity to the CAM. Accordingly, an interphase is generally formed between Li 6 PS 5 Cl and Li 3 InCl 6 , indicated  by  indium  sulfide  fragments  in  the  secondary  ion images  obtained  by  ToF-SIMS,  and  this  seems  to  be  more pronounced at the triple phase boundary with the CAM. The following  hypotheses  for  the  underlying  mechanism  can  be thought of:

- i. the CAM catalyzes the reaction or causes a larger interfacial contact area that facilitates stronger decomposition,
- ii.  the CAM leads to the formation of decomposition products with  higher  impedances,  e.g.  Li x In y S z -like  compounds  are formed as intermediates, which are partially delithiated upon further cycling due to the proximity to the CAM,
- iii. sulfide  electrolyte-based  decomposition  products  formed  at the interface with the CAM are more reactive with the halide electrolyte than the pristine sulfide electrolyte.

At this stage all these hypotheses are yet highly speculative and  require  more  in-depth  analytical  studies.  Nevertheless, latest theoretical evaluations of the interfacial stability of halide solid electrolytes with charged S 8  and discharged Li 2 S cathodes

www.advancedsciencenews.com suggest a chemical instability of halides in contact with sulfide species,  at  least  in  Li 2 S. [52] The  chemical  reaction  of  Li 3 YCl6 and Li3 YBr 6  with Li 2 S to LiYS2  and LiCl/LiBr seems to be thermodynamically favorable as negative formation enthalpies are found, likely driven by the metal sulfide bond formation. Interestingly these chlorides seem to be chemical stable against S 8 , suggesting that the instability stems when sulfide anions are in the vicinity. As Li 2 S and polysulfides can be a reaction product of  the  sulfide  electrolyte [32] and  Li 6 PS5Cl  contains  S 2 -anions, a  reaction  of  Li 3 InCl6  here  to  In-S  species  seems  reasonable. However, at this stage due to the large phase space at the triple phase  boundary  of  the  CAM,  Li 3 InCl 6 and  Li 6 PS5Cl,  a  direction reaction pathway remains speculative. Nevertheless, these findings  support  the  reaction  products  of  the  two  electrolytes Li 6 PS5Cl  and  Li 3 InCl6  that  were  found  here,  with  InS -fragments stemming potentially from In2S3 or LiInS2 and concurrent LiCl decomposition products.

While  the  halide-sulfide  combination  does  not  seem  ideal, possible  protection  of  the  metal  anode  via  polymers  or  oxide separators may be a future option. In addition, a separation of the sulfide and halide interphase with a thin Li 3 PO 4  coating by atomic  layer  deposition  is  possible  and  can  increase  the  cycle stability. [35]  As recent work has shown that the chemical stability of  halides  against  CAM  centers  around  the  metal  ion  in  Li-MCl,  the  chemical  stability  against  sulfides  may  also  be  a  function  of  the  halide  solid  electrolyte  composition,  indicating  the need to search for more stable combinations at the triple phase boundary. [33] This  is  further  substantiated as the Li 3 InCl6-based cell,  with  Li 3 InCl6 in the composite and double separator layer, showed growth in  the R separator resistance  as  well,  whereas  the other  two  tested  single-layer  separators  did  not.  Interestingly, Li 2.5 Y0.5 Zr0.5 Cl6 , one of the halide electrolytes compositions that were found stable against LiNi 1/3 Co 1/3Mn1/3O2 showed no good stability  against  the  oxygen  release  of  LiNi 0.85 Co0.1 Mn0.05O2.  In contrast,  Li 3 InCl6  has  a  lower  stability  against  electrochemical oxidation  compared  to  Li 2 In1/3 Sc1/3 Cl4 . [33] Overall,  these  results highlight that the search for new electrolytes should be inspired by the chemical compatibility of the compounds to the desired CAM and other potential components and taking possible reactions into account.

## 3. Conclusions

In  this  study,  we  analyzed  the  role  of  a  bilayer  separator  for halide-based composite cathodes when combined with sulfidebased separators, using Li 3 InCl 6   and  Li6PS5Cl as an example. We have shown that an additional halide separator layer separating the composite cathode from the sulfide-based separator is  crucial  for  the  cycling  stability.  Accordingly,  the  capacity retention was significantly increased and the impedance evolution upon cycling was suppressed coming in the performance range  of  pure  sulfide-based  cells,  explaining  why  the  bilayer design  is  often  chosen  in  the  literature.  Using  FIB-SEM  and ToF-SIMS  analyses,  we  were  able  to  visualize  the  chemical incompatibility  of  the  two  electrolytes  Li 3 InCl6  and  Li 6 PS5Cl. The  accompanied  interphase  formation,  indicated  by  indium sulfide-based degradation products, is of a general nature, but seems to be further promoted at the triple phase boundary with

Adv. Energy Mater. 2023 , 13 , 2203673

www.advenergymat.de contact to the CAM. This leads to a strong rise in the impedance and a rapid capacity fading upon cell cycling, when only one separator layer is used. However, one may suspect that the general  chemical  incompatibility  of  both  electrolytes  may  be a problem for long-term stability, even if the bilayer design is used.

Overall, the results of this study emphasize the importance of  considering  the  chemical  stability  of  all  cell  components relative to each other. Research currently often focuses on the stability  or  chemical  compatibility  of  compounds  towards  the electrodes, motivating bi- or even multilayer designs for solidstate  batteries  neglecting  the  increasing  number  of  interfaces and possible degradation spots, i.e., evolving interphases. However, reactivity beyond the electrodes is often overlooked so far, which can easily lead to severe capacity fading and poor longterm cycling stability, as shown in this study. Therefore, besides high  electrochemical  stability  of  the  solid  electrolyte  towards high potential active materials, the chemical stability within the di/uniFB00erent battery components must be taken more into account and novel protection concepts or more stable materials need to be developed.

## Supporting Information

Supporting  Information  is  available  from  the  Wiley  Online  Library  or from the author.

## Acknowledgements

The authors acknowledge financial support within the cluster of competence  FESTBATT  funded  by  Bundesministerium  für Bildung und  Forschung  (BMBF;  projects  03XP0430A,  03XP0430F).  The  authors acknowledge  Björn  Wankmiller  for  measuring 7 Li  and 31 P  MAS  NMR (not shown). M.H. and B.W. are members of the International Graduate School for  Battery  Chemistry,  Characterization,  Analysis,  Recycling  and Application  (BACCARA),  which  is  funded  by  the  Ministry  for  Culture and  Science  of  North  Rhine-Westphalia,  Germany.  S.O.  acknowledge financial support from JSPS KAKENHI grant number JP 21K14720.

Open Access funding enabled and organized by Projekt DEAL.

## Conflict of Interest

The authors declare no conflict of interest.

## Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## Keywords

degradation,  halide  solid  electrolytes,  interfaces,  solid-state  batteries, sulfide solid electrolytes

Received: October 30, 2022

Revised: November 30, 2022

Published online: December 23, 2022

www.advancedsciencenews.com

- [1]  J. Janek, W. G. Zeier, Nat. Energy 2016 , 1 , 16141.
- [2]  S.  Randau,  D.  A.  Weber,  O.  Kötz,  R.  Koerver,  P.  Braun,  A.  Weber, E.  Ivers-Ti/uniFB00ée,  T .  Adermann,  J.  Kulisch,  W .  G.  Zeier,  F.  H.  Richter, J. Janek, Nat. Energy 2020 , 5 , 259.
- [3]  A. Manthiram, X. Yu, S. Wang, Nat. Rev. Mater. 2017 , 2 , 16103.
- [4]  Y .  Kato,  S.  Hori,  T.  Saito,  K.  Suzuki,  M.  Hirayama,  A.  Mitsui, M. Yonemura, H. Iba, R. Kanno, Nat. Energy 2016 , 1 , 16030.
- [5]  S.  Ohno,  A.  Banik,  G.  F.  Dewald,  M.  A.  Kraft,  T.  Krauskopf, N.  Minafra,  P.  Till,  M.  Weiss,  W.  G.  Zeier, Prog.  Energy 2020 , 2 , 022001.
- [6]  Y . S. Jung, D. Y . Oh, Y . J. Nam, K. H. Park, Isr. J. Chem. 2015 , 55 , 472.
- [7]  A. Gautam, M. Ghidiu, E. Suard, M. A. Kraft, W. G. Zeier, ACS Appl. Energy Mater. 2021 , 4 , 7309.
- [8]  A.  Gautam,  M.  Sadowski,  M.  Ghidiu,  N.  Minafra,  A.  Senyshyn, K. Albe, W. G. Zeier, Adv. Energy Mater. 2021 , 11 , 2003369.
- [9]  N. Minafra, M. A. Kraft, T. Bernges, C. Li, R. Schlem, B. J. Morgan, W. G. Zeier, Inorg. Chem. 2020 , 59 , 11009.
- [10]  K.  Homma, M. Yonemura, T. Kobayashi, M. Nagao, M. Hirayama, R. Kanno, Solid State Ionics 2011 , 182 , 53.
- [11]  Z. Liu, W. Fu, E. A. Payzant, X. Yu, Z. Wu, N. J. Dudney, J. Kiggans, K. Hong, A. J. Rondinone, C. Liang, J. Am. Chem. Soc. 2013 , 135 , 975.
- [12]  S.  P.  Culver,  A.  G.  Squires,  N.  Minafra,  C.  W.  F.  Armstrong, T.  Krauskopf,  F.  Böcher,  C.  Li,  B.  J.  Morgan,  W.  G.  Zeier, J.  Am. Chem. Soc. 2020 , 142 , 21210.
- [13]  T. Krauskopf, S. P. Culver, W. G. Zeier, Chem. Mater. 2018 , 30 , 1791.
- [14]  W. Zhang, D. A. Weber, H. Weigand, T. Arlt, I. Manke, D. Schröder, R. Koerver, T. Leichtweiss, P. Hartmann, W. G. Zeier, J. Janek, ACS Appl. Mater. Interfaces 2017 , 9 , 17835.
- [15]  J.  Ruhl, L. M. Riegger, M. Ghidiu, W. G. Zeier, Adv. Energy Sustain. Res. 2021 , 2 , 2000077.
- [16]  R. Koerver, I. Aygün, T. Leichtweiß, C. Dietrich, W. Zhang, J. O. Binder, P. Hartmann, W. G. Zeier, J. Janek, Chem. Mater. 2017 , 29 , 5574.
- [17]  A. Sakuda, A. Hayashi, M. Tatsumisago, Sci. Rep. 2013 , 3 , 2261.
- [18]  L. L. Baranowski, C. M. Heveran, V. L. Ferguson, C. R. Stoldt, ACS Appl. Mater. Interfaces 2016 , 8 , 29573.
- [19]  F.  Walther,  R.  Koerver,  T.  Fuchs,  S.  Ohno,  J.  Sann,  M.  Rohnke, W. G. Zeier, J. Janek, Chem. Mater. 2019 , 31 , 3745.
- [20]  T. Asano, A. Sakai, S. Ouchi, M. Sakaida, A. Miyazaki, S. Hasegawa, Adv. Mater. 2018 , 30 , 1803075.
- [21]  X. Li, J. Liang, X. Yang, K. R. Adair, C. Wang, F. Zhao, X. Sun, Energy Environ. Sci. 2020 , 13 , 1429.
- [22]  B. Helm, R. Schlem, B. Wankmiller, A. Banik, A. Gautam, J.  Ruhl,  C.  Li,  M.  R.  Hansen,  W.  G.  Zeier, Chem. Mater. 2021 , 33 , 4773.
- [23]  K.-H. Park, K. Kaup, A. Assoud, Q. Zhang, X. Wu, L. F. Nazar, ACS Energy Lett. 2020 , 5 , 533.
- [24]  R.  Schlem,  T.  Bernges,  C.  Li,  M.  A.  Kraft,  N.  Minafra,  W.  G.  Zeier, ACS Appl. Energy Mater. 2020 , 3 , 3684.
- [25]  X. Li, J. Liang, N. Chen, J. Luo, K. R. Adair, C. Wang, M. N. Banis, T. Sham, L. Zhang, S. Zhao, S. Lu, H. Huang, R. Li, X. Sun, Angew. Chem., Int. Ed. 2019 , 58 , 16427.
- [26]  X. Li, J.  Liang, J. Luo, M. Norouzi Banis, C. Wang, W. Li, S. Deng, C.  Yu,  F.  Zhao,  Y .  Hu,  T.-K.  Sham,  L.  Zhang,  S.  Zhao,  S.  Lu, H. Huang, R. Li, K. R. Adair, X. Sun, Energy Environ. Sci. 2019 , 12 , 2665.

www.advenergymat.de

- [27]  R. Schlem, A. Banik, S. Ohno, E. Suard, W. G. Zeier, Chem. Mater. 2021 , 33 , 327.
- [28]  R.  Schlem,  S.  Muy,  N.  Prinz,  A.  Banik,  Y .  Shao-Horn,  M.  Zobel, W. G. Zeier, Adv. Energy Mater. 2020 , 10 , 1903719.
- [29]  L. Zhou, C. Y . Kwok, A. Shyamsunder, Q. Zhang, X. Wu, L. F. Nazar, Energy Environ. Sci. 2020 , 13 , 2056.
- [30]  S.  Wang,  Q.  Bai,  A.  M.  Nolan,  Y .  Liu,  S.  Gong,  Q.  Sun,  Y .  Mo, Angew. Chemie 2019 , 131 , 8123.
- [31]  D.  Park,  H.  Park,  Y .  Lee,  S.-O.  Kim,  H.-G.  Jung,  K.  Y .  Chung, J. H. Shim, S. Yu, ACS Appl. Mater. Interfaces 2020 , 12 , 34806.
- [32]  L. Zhou, N. Minafra, W. G. Zeier, L. F. Nazar, Acc. Chem. Res. 2021 , 54 , 2717.
- [33]  I.  Kochetkov,  T.-T.  Zuo,  R.  Ruess,  B.  Singh,  L.  Zhou,  K.  Kaup, J. Janek, L. Nazar, Energy Environ. Sci. 2022 , 15 , 3933.
- [34]  T. Koç, F. Marchini, G. Rousse, R. Dugas, J.-M. Tarascon, ACS Appl. Energy Mater. 2021 , 4 , 13575.
- [35]  T. Koç, M. Hallot, E. Quemin, B. Hennequart, R. Dugas, A. M. Abakumov, C. Lethien, J.-M. Tarascon, ACS Energy Lett. 2022 , 7 , 2979.
- [36]  L.  M.  Riegger,  R.  Schlem,  J.  Sann,  W.  G.  Zeier,  J.  Janek, Angew. Chem., Int. Ed. 2021 , 60 , 6718.
- [37]  C.  Wang,  J.  Liang,  J.  Luo,  J.  Liu,  X.  Li,  F.  Zhao,  R.  Li,  H.  Huang, S. Zhao, L. Zhang, J. Wang, X. Sun, Sci. Adv. 2021 , 7 , abh1896.
- [38]  L.  Zhou,  T.-T.  Zuo,  C.  Y .  Kwok,  S.  Y .  Kim,  A.  Assoud,  Q.  Zhang, J. Janek, L. F. Nazar, Nat. Energy 2022 , 7 , 83.
- [39]  X.  Shi,  Z.  Zeng,  M.  Sun,  B.  Huang,  H.  Zhang,  W.  Luo,  Y .  Huang, Y. Du, C. Yan, Nano Lett. 2021 , 21 , 9325.
- [40]  M.  A.  Kraft,  S.  P.  Culver,  M.  Calderon,  F.  Böcher,  T.  Krauskopf, A. Senyshyn, C. Dietrich, A. Zevalkink, J. Janek, W. G. Zeier, J.  Am. Chem. Soc. 2017 , 139 , 10909.
- [41]  P.  Minnmann,  L.  Quillman,  S.  Burkhardt,  F.  H.  Richter,  J.  Janek, J. Electrochem. Soc. 2021 , 168 , 040537.
- [42]  L.  de  Biasi,  B.  Schwarz,  T.  Brezesinski,  P.  Hartmann,  J.  Janek, H. Ehrenberg, Adv. Mater. 2019 , 31 , 1900985.
- [43]  T.  Li,  X.-Z.  Yuan,  L.  Zhang,  D.  Song,  K.  Shi,  C.  Bock, Electrochem. Energy Rev. 2020 , 3 , 43.
- [44]  R.  Koerver,  W.  Zhang,  L.  de  Biasi,  S.  Schweidler,  A.  O.  Kondrakov, S. Kolling, T. Brezesinski, P. Hartmann, W. G. Zeier, J. Janek, Energy Environ. Sci. 2018 , 11 , 2142.
- [45]  D.  H.  S.  Tan,  E.  A.  Wu,  H.  Nguyen,  Z.  Chen,  M.  A.  T.  Marple, J.-M. Doux, X. Wang, H. Yang, A. Banerjee, Y. S. Meng, ACS Energy Lett. 2019 , 4 , 2418.
- [46]  S.  Ohno,  C.  Rosenbach,  G.  F.  Dewald,  J.  Janek,  W.  G.  Zeier, Adv. Funct. Mater. 2021 , 31 , 2010620.
- [47]  N.  Kaiser,  S.  Spannenberger,  M.  Schmitt,  M.  Cronau,  Y.  Kato, B. Roling, J. Power Sources 2018 , 396 , 175.
- [48]  V.  Miß,  A.  Ramanayagam,  B.  Roling, ACS  Appl.  Mater.  Interfaces 2022 , 14 , 38246.
- [49]  R.  Koerver,  F.  Walther,  I.  Aygün,  J.  Sann,  C.  Dietrich,  W.  G.  Zeier, J. Janek, J. Mater. Chem. A 2017 , 5 , 22750.
- [50]  J. K. Eckhardt, T. Fuchs, S. Burkhardt, P. J. Klar, J. Janek, C. Heiliger, ACS Appl. Mater. Interfaces 2022 , 14 , 42757.
- [51]  G. H. Chun, J. H. Shim, S. Yu, ACS Appl. Mater. Interfaces 2022 , 14 , 1241.
- [52]  M. L. Holekevi Chandrappa, J. Qi, C. Chen, S. Banerjee, S. P. Ong, J. Am. Chem. Soc. 2022 , 144 , 18009.