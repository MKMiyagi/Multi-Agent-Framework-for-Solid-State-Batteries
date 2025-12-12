## Energy &amp; Environmental Science

## PAPER

Cite this: Energy Environ. Sci. 2022, , 3933

,

1

5

Received 10th March 2022, Accepted 28th July 2022

DOI: 10.1039/d2ee00803c

rsc.li/ees

## 1 Introduction

State-of-the-art lithium-ion batteries (LIB) with a liquid organic electrolyte currently satisfy the ever-increasing demand for powering long-range electric vehicles, but are asymptotically reaching limits in performance. 1 The development of solidstate batteries (SSBs) is one of the most promising avenues towards advanced rechargeable energy storage systems with lower safety risks and maximized energy density. 2-5 This calls for the design of non-flammable solid-state lithium superionic

a Department of Chemistry and the Waterloo Institute for Nanotechnology, University of Waterloo, 200 University Ave W, N2L 3G1, Waterloo, Ontario,

Canada. E-mail: juergen.janek@phys.chemie.uni-giessen.de, lfnazar@uwaterloo.ca

b Institute of Physical Chemistry &amp; Center for Materials Research, Justus Liebig University, Heinrich-Buff-Ring 17, 35392, Giessen, Germany

c Joint Centre for Energy Storage Research, Argonne National Laboratory, Argonne, IL, USA

† Electronic supplementary information (ESI) available. See DOI: https://doi.org/ 10.1039/d2ee00803c

View Article Online View Journal | View Issue

## Different interfacial reactivity of lithium metal chloride electrolytes with high voltage cathodes determines solid-state battery performance †

Ivan Kochetkov, Tong-Tong Zuo, Raffael Ruess, Baltej Singh, Laidong Zhou, ac Kavish Kaup, ac Ju ¨ rgen Janek * b and Linda Nazar * ac

a b b ac

A deep understanding of the interaction of the surface of cathode materials with solid electrolytes is crucial to design advanced solid-state batteries (SSBs). This is especially true for the new class of lithium metal chloride (Li-M-Cl) solid electrolytes which are receiving rapidly growing attention due to their very high oxidative stability ( 4 4 V) in combination with good ionic conductivity that can enable long cell cycle life. While Li-M-Cl electrolytes typically contain resource-limited metals (M) such as indium or rare earths, work has focused on substituting M with more abundant elements such as zirconium. Via operando resistance measurements using intermittent current interruption we explore the dynamic evolution of the interphase at the surface of Ni-rich NCM85 or NCM111 cathode particles inside a working SSB with three different Li-(M1,M2)-Cl catholytes (Li3InCl6, Li2Sc1/3In1/3Cl4 and Li5/2Y1/2Zr1/2Cl6) to reveal the impact of the cationic metal substitution on the interfacial chemistry. We show that the metal plays a critical role in determining high voltage stability, contrary to prior assumptions. Using a combination of cyclic voltammetry and ultraviolet photoelectron spectroscopy measurements of the electronic band structure to assess oxidative stability; coupled with DFT calculations and ToF-SIMS to evaluate products formed at the interface at different upper cutoff potentials and degrees of delithiation, we are able to differentiate between electrochemical and chemical degradation. We find that Li2Sc1/3In1/3Cl4 yields the highest (and Li3InCl6 the lowest) stability against electrochemical oxidation, while Li5/2Y1/2Zr1/2Cl6 undergoes a detrimental chemical reaction with oxygen released from Ni-rich NCM85 at high potentials, resulting in fast capacity fading. Overall, our work establishes a platform for the metrics and an approach that can be utilized to efficiently evaluate the stability of new halide SEs in SSB cells.

electrolytes (SEs) that combine high conductivity with electrochemical stability at the positive electrode. Although sulfidebased SEs still exhibit the highest ionic conductivities (above 10 mS cm /C0 1 ), 6-10 their applicability in SSBs with 4 V cathodeactive-materials (CAMs) and high energy density is limited due to their electrochemical oxidation around 2.6 V 11-13 and chemical instability in contact with oxide-type CAMs. 14-17 Protective coatings of CAMs 18-22 may solve this issue, but also necessitate additional and potentially costly processing steps. In contrast to sulfide-based SEs, those with a chloride anion sublattice exhibit thermodynamic oxidation potentials well above this range - typically B 4.2-4.3 vs. Li + /Li - and exhibit good conductivity of 1-2 mS cm /C0 1 at room temperature, which makes them a promising choice as catholyte while still leaving room for further improvement. 23-29

Although many of these chloride-based SEs exhibit similar values of ionic conductivity and onset of electrochemical oxidation, their performance in SSBs with Ni-rich CAMs differs significantly and the fundamental origin for this is not yet

,

2

0

|

understood. For example, LiNi0.85Co0.1Mn0.05O2-based CAMs exhibit low capacity fading over hundreds of cycles with Li2Sc2/3Cl4 30 and Li2In1/3Sc1/3Cl4 31 chlorospinel SEs as the catholyte, the latter showing stable performance even up to 4.8 V and at high CAM loadings. However, similar CAMs ( e.g. LiNi0.83Co0.12Mn0.05O2) with Li2.5Yb0.5Zr0.5Cl6 as the catholyte suffer from a 20% percent capacity decay on cycling up to 4.3 V within the first 50 cycles. 32 Although recent studies hint at the possible role of the metal M in the oxidative stability of the chloride SEs, 33 its impact on interfacial compatibility between a SE and a Ni-rich CAM still lacks comprehensive insight. This is especially true given the quest to devise SSBs that function above 4.3 V.

Here, we demonstrate the critical role of the central metal cation in Li-M-Cl-based SEs for the capacity retention of SSB cells with LiNi0.85Co0.1Mn0.05O2 (NCM85). Three different chloride-based SEs (Li3InCl6 (LIC), Li2.5Y0.5Zr0.5Cl6 (LYZC), and Li2In1/3Sc1/3Cl4 (LSIC)) were chosen due to their unique properties: LSIC was selected because it enables long-term cycling of SSBs with NCM85, especially at very high voltages ( Z 4.8 V). 31 LYZC was chosen because the relatively low price of Zr and Y makes it a promising cost-effective SE, as reported in the seminal paper by Panasonic. 23 LIC was chosen as the currently most well-known halide SE and can serve as a reference. Most importantly, all three SEs exhibit very similar ionic conductivity of 1-2 mS cm /C0 1 , and their structures are well defined and understood, unlike Li3YCl6 34 and Li2ZrCl6 35 which exhibit sufficient ionic conductivity only in a quasi-amorphous state. The selected electrolytes are compared in terms of their performance and stability as catholytes. Galvanostatic cycling and electrochemical impedance spectroscopy (EIS) reveal that cells with Li2In1/3Sc1/3Cl4 show superior cycling stability and the least impedance growth. On the other hand, Li2.5Y0.5Zr0.5Cl6 shows significant capacity decay accompanied by appreciable growth of cathode impedance at or above 4.3 V. Cyclic voltammetry (CV), ultraviolet photoelectron spectroscopy (UPS), and time-of-flight secondary ion mass spectrometry (ToF-SIMS) reveal the nature of both chemical and electrochemical side reactions between the lithium metal chloride SEs and delithiated NCM85. We find that the chemical reaction of the Li-M-Cl SE with oxygen evolved from NCM85 ( Z 4.3 V) at the interface can lead to interphase growth and severe capacity fading. By combining the experimental techniques with DFT calculations, we demonstrate that the stability of the interface between Li-M-Cl and delithiated NCM85 is highly dependent on M: namely, In 3+ and Sc 3+ central cations favor a kinetically stable interface between Li-M-Cl and delithiated NCM85, while in the case of LYZC, side-reactions with NCM are triggered that result in the accumulation of the decomposition products upon cycling ( i.e. , YOCl) and hence, faster capacity fading. The highly exergonic thermodynamics of ZrO2 formation also drives degradation of the NCM85|LYZC interface. Moreover, minimization of the electronic conductivity of an SE improves its stability in the SSB cells above its decomposition potential and thus, this is a broad avenue towards high-energy-density SSBs. Overall, our work manifests for the first time the decisive role of the central

|

metal ion(s) of lithium chloride SEs in the performance of SSBs and highlights the often-overlooked role of the electronic properties of SEs.

## 2 Results and discussion

## 2.1. Electrochemical performance of NCM85 SSB cells as a function of chloride SE composition and upper cutoff potential.

The cell performance is directly linked to the nature of the metal ion(s) M 3+ /M 4+ in the Li-M-Cl SEs (Fig. 1A-C), and the higher the voltage cutoff, the greater the difference between them. Fig. 1A shows that the NCM85-LYZC cell shows a capacity fade rate of 0.3 mA h g /C0 1 per cycle at a cutoff of 4.3 V, and thus still retains 80% of its maximum capacity after 120 cycles. At a cutoff of 4.6 V, however, retention drops to 45% due to the faster capacity decay (1.8 mA h g /C0 1 per cycle). The behavior of the NCM85-LIC-based cathode is noticeably different: the capacity fade is moderate at voltage cutoffs of either 4.3 and 4.6 V, yielding an average rate of 0.13 and 0.24 mA h g /C0 1 per cycle, respectively. In marked contrast to either of these two SEs, the fade rate of the SSB cells with NCM85-LSIC cathodes is only B 0.08 mA h g /C0 1 per cycle at both cutoff voltages (Fig. 1C).

The capacity retention of the SSB cells is consistent with their evolution of polarization during cycling. At the 4.3 V cutoff, the NCM85-LYZC cathode suffers from appreciable growth in polarization from the 10th to the 100th cycle (Fig. 1D), while its NCM85-LIC counterpart exhibits a minor increase in overpotential (Fig. 1E). Meanwhile, the overpotential of the NCM85-LSIC cathodes does not exhibit any increase after 100 cycles (Fig. 1F). The dependence of the polarization of the SSB cells on the nature of the M 3+ /M 4+ ion(s) becomes more evident upon cycling to 4.6 V (bottom row Fig. 1G-I). Especially in contrast to NCM85-LYZC (Fig. 1G) but also NCM85-LIC (Fig. 1H), the SSB cells with the NCM85-LSIC cathodes exhibit only a minor increase in overpotential after 100 cycles (Fig. 1I). It is noteworthy that the high capacity of NCM85 and high utilization levels can be achieved without carbon additives at moderate current density (0.2C rate), apparently due to continuous electronic and ionic percolation pathways within the cathode (Fig. S1A-F, ESI † ). We note that the capacity of the NCM85LIC and NCM85-LSIC cathodes systematically increases by 515 mA h g /C0 1 during the first 10 cycles, which is more similar to the behavior of liquid Li-batteries with advanced liquid electrolytes 36-38 than sulfide 39 or halide 40 SEs. That behavior may be ascribed to changes in the morphology and/or wetting of the cathode/SE interface, but needs further exploration.

The better stability of LSIC was further confirmed via operando EIS studies. The evolution of the impedance of the SSB cells over 50 cycles within the 2.7-4.3 V window ( vs. Li + /Li) is depicted in Fig. 2, where EIS data were collected in situ during every cycle at exactly 3.8 V by interrupting the charge to collect the spectrum. The impedance response of the SSB cells was fitted with the equivalent circuit shown in Fig. 2A (left panel). The bulk resistance of the bilayer SE ( R bulk) defines the positive offset of the real part, C dl represents the capacitance

Fig. 1 (A-C) Capacity retention of the In/InLi||NCM85 SSB cells comprised of cathode composites with (A) LYZC, (B) LIC, and (C) LSIC SEs at a rate of 0.2C within the voltage windows of 2.7-4.3 V and 2.7-4.6 V vs. Li + /Li. (D-F) Representative voltage profile of In/InLi||NCM85 SSB cells with (D) LYZC, (E) LIC, and (F) LSIC SEs cycled between 2.7 and 4.3 V at 0.2C. The 1st, the 10th (solid squares line), and the 100th cycles are represented by open circles, solid squares, and solid lines, respectively. (G-I) Representative voltage profile of In/InLi||NCM85 SSB cells with (G) LYZC, (H) LIC, and (I) LSIC SEs cycled between 2.7 and 4.6 V at 0.2C. The 1st, the 10th (solid squares line), and the 100th cycles are represented by open circles, solid squares, and solid lines, respectively.

of the double layer that is formed at the electrode-SE junction, 41 and the impedance of the anode is found in the frequency region below 10 Hz, which is masked by the dominating cathode contribution. The NCM85-SE cathode generates a depressed semicircle in the frequency range 10 5 -10 Hz with a distinctive Gerischer-type shape 42 which describes charge transport and charge transfer in mixed conducting solid-state materials (Fig. 2B-D). Due to the complexity of charge transport and charge transfer within the cathode that includes ionic ( R ion ), electronic ( R e), and interfacial contributions ( R int), a transmission line model (TLM) - as described by Gabers ˇc ˇek et al. 41 and IversTiffe ´e et al. 43 - with blocking boundary conditions was used to fit the experimental data (Fig. 2A, right panel). The cathode resistance ( R cathode) is expressed as the geometric mean of ( R e + R ion ) and R int (eqn (1)):

ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi ffi

p

<!-- formula-not-decoded -->

We note that independent evaluation of the interfacial contributions, R int, is not possible for Gerischer-type impedances.

In agreement with the capacity decay of the SSB cells during cycling to 4.3 V, the NCM85-LIC and NCM85-LSIC cathodes exhibit only a tiny impedance increase of R cathode of B 2.4 O cm 2 , while the LYZC-based cathodes suffer from a 7fold rise (Fig. 2E(i)). Notably, the increase in R bulk exhibited by the SSB cells with NCM85-LYZC ( B 5 O cm 2 ) and NCM85-LIC ( B 20 O cm 2 ) cathodes (Fig. 2E (ii)) indicates possible sidereactions between the sulfide and halide SEs. After the initial growth, R bulk of the cells with LYZC levels off due to the formation of a kinetically stabilized interface. The 2-fold increase in R bulk of the LIC-based cells might arise from more extensive side reactions between LIC and Li5.5PS4.5Cl1.5, as recently reported. 44 However, the growth in bulk resistance by 25 O cm 2 increases ohmic polarization of those cells only by B 7 mV at the given current density of 0.28 mA cm /C0 2 , which will have an insignificant effect on the capacity.

To further investigate the influence of holding the cells at high potentials on R cathode, we performed time-resolved EIS at cutoff voltages of 4.1, 4.3, and 4.6 V (Fig. 3) over a period of 30 h. We call this period ''interphase growth''. Before

Fig. 2 (A) The equivalent circuit used to fit the EIS spectrum of the In/InLi||NCM85 SSB cells (left panel), and TLM scheme of the NCM85-SE cathodes (right panel). (B-D) Representative Nyquist plot of In/InLi||NCM85 SSB cells with (B) LYZC, (C) LIC, and (D) LSIC SEs cycled between 2.7 and 4.3 V at 0.2C measured at 3.8 V vs. Li + /Li during cycling at a rate of 0.2C between 2.7 and 4.3 V vs. Li + /Li, by briefly interrupting the charge cycle. The shift (shaded solid lines) of the impedance at 10 Hz and 10 mHz from the 10th to the 50th cycle illustrates higher instability of the (B) NCM85-LYZC cathode compared to the (C) NCM85-LIC cathode. (E) Evolution of R cathode and R bulk upon continuous cycling of the corresponding In/InLi||NCM85 SSB cells.

impedance measurements, the cells were fully charged via a CCCV (constant current -constant voltage) protocol until a constant and negligible current was achieved (equivalent to a 0.01C rate) (Fig. S2, ESI † ) to reach a stable state-of-charge (SOC). Hence, the temporal growth of R cathode during the growth period is driven by chemical reactivity at the cathodeSE interface. The decreased stability of the SSB cells at cutoff potentials at or above 4.3 V corresponds to a faster increase of R cathode. While R cathode for all three SEs remains almost constant at 4.1 V (Fig. 3A), the LIC- and LYZC based SSB cells exhibit noticeable degradation upon interphase growth at 4.3 V as shown in Fig. 3B (corresponding Nyquist plots are shown in Fig. S3A-H, ESI † ). The temporal evolution of R cathode obeys parabolic growth behavior that is only evident at 4.3 and 4.6 V (Fig. 3B and C), indicating that decomposition at the NCM85|SE interface is a diffusion-controlled reaction with a kinetic constant k , as recently reported for a sulfide SE by Zuo et al. , 17 (see reference for details):

<!-- formula-not-decoded -->

where R 0 and t 0 are empirical parameters indicating the initial interfacial resistance (at the start of the EIS measurements) and its growth, while the kinetic constant k is a measure of the growth rate.

The high initial R cathode of NCM85-LYZC at 4.3 V is ascribed to the formation of an interphase for this SE even before the start of the measurements at R 0, which likely contributes to the capacity fade (Fig. 3D). Thus R cathode of LYZC grows slower than that of NCM85-LIC, (potentially because of the pre-formation of a passivating interphase during the CCCV step) as indicated by the kinetic constants (Fig. 3D): 4.4 O h /C0 0.5 (LYZC) vs. 8.0 O h /C0 0.5 (LIC). However, NCM85-LSIC - in contrast to NCM85-LIC and

Fig. 3 (A) The stability of R cathode of the charged In/InLi||NCM85 SSB cells during the aging at 4.1 V vs. Li + /Li. Fitting of the corresponding R cathode ( t ) profiles results in the k -values very close to 0. (B and C) Evolution of R cathode of the charged In/InLi||NCM85 SSB cells during the aging at (B) 4.3 and (C) 4.6 V vs. Li + /Li. The solid lines represent the parabolic fitting of the corresponding R cathode ( t ). (D) Room temperature (25 1 C) ionic ( s ion) and electronic ( s e) conductivity of Li-M-Cl SEs, voltage-dependence of the fading rate of the In/InLi||NCM85 SSB cells and rate constant k of the NCM85-SE cathodes. The corresponding DC and AC polarization of the SEs is shown in Fig. S4 and S5 (ESI † ). The experimental details and evaluation of the errors are given in the Experimental Section.

NCM85-LYZC - exhibits only minor growth in R cathode (Fig. S3H, ESI † ) which results in a very low kinetic constant of 0.6 O h /C0 0.5 (Fig. 3D). The increased R cathode (Fig. 3C, F and I) at 4.6 V originates from the enhanced decomposition of the SEs and the lower lithium mobility and low concentration of lithium in NCM at a high SOC. 45 Although the LSIC-based cathodes exhibit some growth of R cathode during aging at 4.6 V, that interface is more stable than NCM85-LIC and especially NCM85-LYZC, as denoted by the increase in k : 30 O h /C0 0.5 (LSIC), 44 O h /C0 0.5 (LIC), and 240 O h /C0 0.5 (LYZC). The response of R cathode exhibited by LYZC indicates that the interface might be effective in lowering its electrochemical reactivity (decomposition at r 4.3 V), but may not be efficient to suppress the chemical reactivity, as will be demonstrated later. Nonetheless, the improved stability of NCM85-LSIC compared to NCM85-LIC is evident by normalizing the k -values to R cathode at the beginning of the aging step - and thus comparing only the temporal component of the interfacial growth 17 - at the beginning of the aging step. The k 0 value for LSIC (0.14 h /C0 0.5 ) is about half that of LIC (0.27 h /C0 0.5 ) (Table S1, ESI † ).

We note that the capacity fade rate of NCM85-LSIC is almost independent of the cutoff voltage (0.08 mA h g /C0 1 at 4.3 and 4.6 V) despite the increase in k (Fig. 3D) which confirms that k is more affected by the reduced conductivity of NCM85 at higher SOC than by any degradation during aging at 4.6 V. These results are completely consistent with our previous report of the long-term stable cycling of NCM85-LSIC even up to 4.8 V. 31

## 2.2. Composition-dependent electrochemical stability window of the Li-M-Cl SEs.

The dependence of the oxidative stability of the Li-M-Cl phases on the M 3+ /M 4+ metal cation(s) was further probed via ultraviolet photoelectron spectroscopy (UPS) and cyclic voltammetry (CV) of the C65-SE||In SS cells. The UP spectra of the chloride SEs are shown in Fig. 4A. The valence band edge energy ( E VB) was calculated via linear approximation of the density of states near the edge of the valence band (VB), as illustrated in the inset of Fig. 4A. 46 The highest E VB of the LSIC SE matches the results discussed above, as it confirms a lower tendency for electrochemical oxidation. Meanwhile, the LIC SE exhibits the lowest E VB, as expected from the higher electronegativity of In 3+ . 47 According to the scale developed by Diaz and Campero, w (In 3+ ) = 1.87, w (Y 3+ ) = 1.22, w (Zr 4+ ) = 1.43, and w (Sc 3+ ) = 1.29. 48

CV analysis of the SEs confirms the observed trend in E VB. The oxidation potential of the SEs mixed with carbon (see Experimental details for cell assembly), calculated as the onset of exponential growth in current, increases from LIC (4.27 V) to LSIC (4.36 V). These values are in agreement with other CV studies 26,30 and theoretical prediction of the electrochemical stability window of the chloride SEs. 49 There is also a clear connection between the oxidative stability of the SEs and E VB (Fig. 4C). We assume that the difference between energies from UPS and CV originates from the energy required to transfer a Li + ion in the same direction as an electron to maintain electroneutrality. 50,51 In fact, CV data contain information on oxidation of the SE by removing one electron and one ion, while UPS only accounts for the electronic part. The highest intrinsic electrochemical stability of the LSIC SE explains the superior performance of NCM85-LSIC, but the origin of the fast fading of the NCM85-LYZC cathodes above 4.3V - in comparison with its NCM85-LIC counterpart - is a remaining question that we address below.

The apparent contradiction between the stability of the NCM85-LIC and NCM85-LYZC cathodes and the intrinsic

Fig. 4 (A) Ultraviolet photoelectron spectra of the SEs. Extrapolation of the valence band edge ( E VB) is demonstrated in the inset plot by the solid dark blue lines. The values of E VB are calculated as the intercept of the extrapolation with the background blue dash-dot line. The spectra were shifted along the energy axis to match the high-binding energy cutoff to 21.22 eV (He-I a ). (B) Cyclic voltammetry of the C65-SE||In cells within 2.7 and 4.6 V at 0.1 mV s /C0 1 . The onset of electrochemical oxidation of the SEs is estimated from the intercept between the extrapolation of the anodic scans (solid lines) to the background (dash-dotted line), as shown in the inset. (C) The correlation between the oxidative stability determined by CVA and E vb. For a more comprehensive illustration, the Li metal work function (WFLi = 2.93 eV) 65 is subtracted from E VB, and the difference is normalized by a unit charge.

oxidation potential of the SEs indicates that the capacity fading of NCM85-LYZC must be driven by chemical decomposition. As demonstrated by Gasteiger, the H2 -H3 phase transition in NCM811 at 4.1 V occurs in step with oxygen evolution at 4.3 V and thus drives capacity fading of the graphite||NCM811 cells with organic electrolytes. 52 Oxygen evolution from NCM622 has also been evidenced in SSB cells at 4.5 V. 53 Due to the higher Ni content in NCM85 used in this work, oxygen evolution is expected to occur even below 4.3 V, which is confirmed by the onset of the H2 -H3 phase transition at 4.16 V (Fig. S6, ESI † ).

Owing to its lower Ni content, the cathode LiNi1/3Co1/3Mn1/3O2 (NCM111) does not exhibit a H2 -H3 phase transition at 4.3 V, so we used that material to probe the inherent electrochemical stability of the SEs in the absence of oxygen evolution. We observe a 4-fold faster capacity fading rate of the NCM111-LIC cathode compared to its LYZC-counterpart (Fig. S7A, ESI † ). This is in concert with the lower potential for the onset of SE electrochemical oxidation for LIC than LYZC (Fig. 4C). Thus, while we observe similar decay of the normalized capacity of both NCM111 and NCM85 (Fig. S7B, ESI † ) with LIC because interface reactivity is dominated by LIC's electrochemical stability, the stability of the SSB cells with LYZC is more directly influenced by the oxygen evolution of the more delithiated NCM85. A similar effect of oxygen release from NCM85 on the interfacial stability with Li10GeP2S12 SE has been demonstrated. 17 Furthermore, the NCM111-LIC and NCM111-LYZC SSB cells exhibit similar cathode impedance before the voltage hold at 4.3 V (Fig. S8A and B, ESI † ), but upon aging, the impedance of NCM111-LIC grows faster due to electrochemical degradation, as indicated by the higher rate constant (Fig. S8C, ESI † ).

In summary, the stable cycling of NCM111-LYZC - but severe capacity fading of NCM85-LYZC - indicates lower chemical stability of LYZC with highly delithated NCM. The pronounced and continuous growth of the NCM85-LYZC interface indicates that the interfacial decomposition products facilitate the mass transfer of oxygen-containing species produced by NCM85. In contrast, LIC and especially LSIC, appear more stable towards chemical side-reactions arising from evolution of oxygen species. For a deeper understanding of the role of M leading to the instability of the halide SE, the degradation products were characterized with time-of-flight secondary ion mass spectrometry (ToF-SIMS) coupled with DFT calculations of interphase reactivity.

## 2.3. Analysis of the degradation products by DFT and ToF-SIMS.

To better understand the chemical reactivity between NCM85 and Li-M-Cl SEs, we performed DFT calculations to predict the enthalpy change and products of the interfacial reactions between Li-M-Cl and Li1 /C0 x NiO2 (a model system for high-Ni NCM85). While these calculations do not capture the kinetics, they are useful as a guideline. The effect of oxygen evolution from Li1 /C0 x NiO2 on the stability is taken into account by tuning the Li-fraction ( x ). For all high-Ni NCM materials, the critical H2-H3 phase transition occurs at around x = 0.75, which is responsible for the irreversible transition to rock salt NiO at the surface accompanied by oxygen release as discussed above. 54

Therefore, the calculated enthalpies account for the reactivity between the SEs and both released oxygen and delithiated oxygen-deficient Li1 /C0 x NiO2 /C0 d . Among all the possible reactions, those involving metal oxides and oxide chlorides as products show the most negative reaction energies (printed in bold in the Table 1). These reactions that predict the formation of InOCl, ScOCl, YOCl, and ZrO2 are shown in Table 1. LYZC SE exhibits a significant negative reaction enthalpy at any SOC, suggesting the greater chemical instability of the NCM85-LYZC cathodes and correlates well with the performance of the SSB cells. The greater reactivity of LYZC may result from the strong thermodynamic contribution of forming ZrO2, as suggested by the less negative enthalpy of the reaction between Li3YCl6 and LiNiO2 than between Li2ZrCl6 and LiNiO2; on the other hand, a purely Zr-based SE may benefit from the passivating nature of stable ZrO2 at the interface (as opposed to YOCl). 33 The formation of In2O3 and Sc2O3 instead of InOCl and ScOCl decreases the reaction enthalpy by 0.012 eV per atom, which does not affect the predicted stability of the NCM85-LIC or NCM85-LSIC in comparison with their LYZC-based counterpart (Table S2, ESI † ).

To verify the thermodynamics-driven chemical decomposition of LYZC predicted by the DFT calculations, the cathodes were analyzed by ToF-SIMS. Due to the high mass sensitivity of ToF-SIMS as reported previously, 16 this method is implemented here to study the degradation mechanism of chloride SEs upon continuous cycling of the NCM85 SSB cells. It is noteworthy that although transmission electron microscopy (TEM) may be implemented to investigate the structural evolution of the cathode active material surface, as was well demonstrated by Jung et al. , 40 ToF-SIMs is more capable of probing the chemical composition of the cathode interphase. It also avoids possible interphase evolution induced during the sample thinning necessary for TEM study or electron beam irradiation in the TEM. To minimize the inhomogeneity on the surface, ten spectra in different areas on each sample were collected and then averaged. Taking the matrix effect into account, the intensity of the specific fragment ( e.g. , MCl n /C0 ) may vary with the SEs. Therefore, the compositional changes at the interface were determined by comparing the normalized signal intensity of the NCM85-SE pellets before and after cycling. Our DFT calculations suggest that M-oxides (In2O3, Sc2O3, ZrO2) and M-oxide chlorides (M-OCl) will be formed at the interface. Additionally, the intrinsic electrochemical oxidation of the SE would result in the formation of a corresponding M-chloride (InCl3, ScCl3, YCl3, and ZrCl4). 55,56 Therefore, the evolution of the signal from MCl n /C0 fragments arises from pure electrochemical oxidation of the SEs, while the change in OCl /C0 fragments illustrates how reactive the NCM85|SE interface is. We note that the intensity of M-oxide fragments in the ToF-SIMS data was generally too low to be reliably detected, because of the low ionization possibilities of M-oxide fragments and mass interferences by adjacent signals.

The evolution of the MCl n /C0 signal (Fig. 5A-C) after long-term cycling of the In/InLi||NCM85 SSB cells between 2.7 and 4.3 V is in good agreement with the CV results. While NCM85-LYZC (Fig. 5A) and NCM85-LSIC (Fig. 5C) do not indicate an increase in the corresponding MCl n /C0 signals, InCl3 /C0 generated by NCM85-LIC (Fig. 5B) exhibits a noticeable growth after 120 cycles. The greater susceptibility of LIC to electrochemical oxidation is also confirmed by the stronger growth of the InCl2 /C0 signal generated by LIC (Fig. S9A, ESI † ).

While the change in MCl n /C0 confirms the effect of M on the intrinsic electrochemical stability of Li-M-Cl and its appearance in the SSB cells, the evolution of the OCl /C0 fragment (Fig. 5D) proves the influential role of M on compatibility with NCM85 ( i.e. , oxygen-induced degradation). As discussed above, ZrO2 and YOCl are the oxygen-derived degradation products of LYZC. Limited by the low ionization possibility and mass interference, ZrO2 /C0 fragments are almost undetectable and cannot be

Table 1 DFT computed interfacial reaction products and corresponding reaction energies for cathode/electrolytes interfaces at various SOC of the cathode material. Energetically favorable reactions involving oxide chloride products are displayed

|               |                                | Reaction products                 | D E rxt (eV per atom)   |
|---------------|--------------------------------|-----------------------------------|-------------------------|
| LiNiO 2       | Li 3 InCl 6                    | LiClO 4 , NiO, LiCl, InClO        | /C0 0.060               |
|               | Li 2.125 Sc 0.375 In 0.25 Cl 4 | LiClO 4 , NiO, LiCl, InClO, ScClO | /C0 0.079               |
|               | Li 2.5 Y 0.5 Zr 0.5 Cl 6       | LiClO 4 , NiO, LiCl, ZrO 2 , YClO | /C0 0.124               |
|               | Li 3 YCl 6                     | LiClO 4 , NiO, LiCl, YClO         | /C0 0.082               |
|               | Li 2 ZrCl 6                    | LiClO 4 , NiO, LiCl, ZrO 2        | /C0 0.155               |
| Li 0.75 NiO 2 | Li 3 InCl 6                    | LiClO 4 , NiO, LiCl, InClO        | /C0 0.064               |
|               | Li 2.125 Sc 0.375 In 0.25 Cl 4 | LiClO 4 , NiO, LiCl, InClO, ScClO | /C0 0.081               |
|               | Li 2.5 Y 0.5 Zr 0.5 Cl 6       | LiClO 4 , NiO, LiCl, ZrO 2 , YClO | /C0 0.122               |
|               | Li 3 YCl 6                     | LiClO 4 , NiO, LiCl, YClO         | /C0 0.084               |
|               | Li 2 ZrCl 6                    | LiClO 4 , NiO, LiCl, ZrO 2        | /C0 0.148               |
| Li 0.5 NiO 2  | Li 3 InCl 6                    | LiClO 4 , NiO, LiCl, InClO        | /C0 0.071               |
|               | Li 2.125 Sc 0.375 In 0.25 Cl 4 | LiClO 4 , NiO, LiCl, InClO, ScClO | /C0 0.084               |
|               | Li 2.5 Y 0.5 Zr 0.5 Cl 6       | LiClO 4 , NiO, LiCl, ZrO 2 , YClO | /C0 0.118               |
|               | Li 3 YCl 6                     | LiClO 4 , NiO, LiCl, YClO         | /C0 0.087               |
|               | Li 2 ZrCl 6                    | LiClO 4 , NiO, LiCl, ZrO 2        | /C0 0.138               |
| Li 0.25 NiO 2 | Li 3 InCl 6                    | LiClO 4 , NiO, LiCl, InClO        | /C0 0.095               |
|               | Li 2.125 Sc 0.375 In 0.25 Cl 4 | LiClO 4 , NiO, LiCl, InClO, ScClO | /C0 0.103               |
|               | Li 2.5 Y 0.5 Zr 0.5 Cl 6       | LiClO 4 , NiO, LiCl, ZrO 2 , YClO | /C0 0.127               |
|               | Li 3 YCl 6                     | LiClO 4 , NiO, LiCl, YClO         | /C0 0.106               |
|               | Li 2 ZrCl 6                    | LiClO 4 , NiO, LiCl, ZrO 2        | /C0 0.140               |

o

.

S

c

v

i

g

y

E

n

e

r

|

Fig. 5 (A-C) Evolution of the mass-spectra of MCl n /C0 fragments upon the cycling of In/InLi||NCM85 SSB cells at a 0.2C rate between 2.7 and 4.3 V vs. Li/ Li + . (D) Evolution of the mass-spectra of OCl /C0 fragment upon cycling. (E and F) Quantification of the decomposition of Li-M-Cl SEs.

quantified (Fig. S9B, ESI † ). 22 However, the OCl /C0 signal proves that the thermodynamically favorable degradation of NCM85LYZC occurs in the SSB. Note that electrochemical decomposition of LIC results in a B 1.4-fold increase in the InCl3 /C0 signal (Fig. 5E), while for LYZC the amount of OCl /C0 is doubled after 120 cycles.

While the performance of In/InLi||NCM85 SSB cells with LYZC SE matches the predictions of the DFT calculations, there is no evidence for the chemical decomposition of LIC and LSIC SEs even though the predicted enthalpy between LIC (LSIC) and fully discharged LiNiO2 is negative. Nonetheless, the amount of OCl /C0 in the uncycled NCM85-LIC and NCM85-LSIC cathodes is half that of its LYZC-counterpart (Fig. 5F). Note that the non-zero intensity of OCl /C0 in the uncycled cathode is likely caused by its exposure to traces of moisture in the glovebox. Nevertheless, the amount of OCl /C0 does not change after 120 cycles to 4.3 V despite the more negative reaction enthalpy between LIC (LSIC) and Li1 /C0 x NiO2 at higher SOC (Table 1). This tendency suggests that In 3+ and Sc 3+ might contribute to the kinetic stabilization of the interface formed between the SEs and NCM85. However, the study of the mechanism of kinetic stabilization is outside the scope of this study and requires a separate investigation.

The reduced accumulation of InCl3 /C0 exhibited by the NCM85-LSIC cathode highlights another critical property that M influences in Li-M-Cl: the electronic conductivity of the SE. The electronic conductivity of LSIC (4.7 /C2 10 /C0 10 S cm /C0 1 ) is almost an order of magnitude below the electronic conductivity

o

.

S

c

v

i

g

y

E

n

e

r

of LIC (5.4 10 /C0 9 S cm /C0 1 ), which, in turn, kinetically stabilizes the SE against electrochemical oxidation. 31 This effect is also responsible for the improved performance of LSIC in comparison with its unsubstituted version - Li2Sc2/3Cl4 31 that undoubtedly illustrates that electronic conductivity of the SE is an as important property as ionic conductivity and the electrochemical stability window.

## 3 Conclusions

A multi-pronged experimental and theoretical analysis of the origins of the different cycling stability of high energy-density NCM85 with three Li-M-Cl solid electrolytes - Li3InCl6 (LIC), Li2Sc1/3In1/3Cl4 (LSIC), and Li5/2Y1/2Zr1/2Cl6 (LYZC) - demonstrates that these SEs behave very differently despite their similar anionic sublattice and ionic conductivity. For the first time, we establish the decisive effect of the central metal M on the performance of the solid state battery (SSB) cells upon cycling to cutoff voltages of 4.3 and 4.6 V and deconvolute the decomposition pathways of the chloride SEs. We demonstrate that while LYZC facilitates very stable cycling of the SSB cells with an NCM111 cathode, this SE is not suitable for highcapacity NCM85 cycled at high voltage ( Z 4.3 V) due to the limited interfacial chemical stability caused by the formation of YOCl (and likely ZrO2) triggered by the oxygen redox reactions of NCM85. Meanwhile, SSB cells with LSIC outperform LIC due

to the lower electronic conductivity of LSIC and better electrochemical stability.

Our work presents a comprehensive approach for analyzing the applicability of novel halide SEs. We suggest that the chemical compatibility with a target cathode material should be evaluated alongside the electrochemical stability window. For example, a theoretical calculation predicted products at the interphase and the reaction enthalpy could be the initial criterion for stability, followed by more advanced simulations that take kinetics into account. Additionally, the electronic conductivity of the SEs must not be underrated and requires exceptional attention due to its extreme importance in achieving the stable performance of the SSB cells.

Overall, our work establishes a platform for the metrics and the approach that can be utilized to efficiently evaluate the stability of new halide (chloride and fluoride) SEs in SSB cells.

## 4 Experimental details

## 4.1. Synthesis of the SEs

Chloride SEs were synthesized by the solid-state route in an Ar-filled glovebox ( p (O2)/ p o 0.5 ppm, p (H2O)/ p o 0.5 ppm). Li2.5Y0.5Zr0.5Cl6 25 (LYZC) and L2Sc1/3In1/3Cl4 31 (LSIC) were synthesized following our previously reported procedures. For Li3InCl6 (LIC), a stoichiometric mixture of LiCl (Sigma-Aldrich, 99.9%) and InCl3 (Sigma-Aldrich, 99.99%) was hand-ground and sealed in a quartz tube under vacuum. The quartz tube was ramped at a rate of 5 1 C min /C0 1 to 450 1 C, dwelled for 48 hours, and cooled to room temperature at a rate of 1 1 C min /C0 1 . Argyrodite Li5.5PS4.5Cl1.5 SE was synthesized by a solid-state reaction at 550 1 C for 48 hours. The heating and cooling rates were 5 1 C min /C0 1 .

## 4.2. Cell assembly and electrochemical measurements

The electronic conductivity of the SE was measured by the DC polarization of the SE pellets in a symmetric Ti|SE|Ti cell under the constant pressure of 255 MPa. In brief, the SE powder was pressed into a B 400 m m pellet for 1 minute, and then DC polarization of 1 V was applied. The steady-state current was averaged over time, and the average was used to calculate the partial electronic conductivity of the SE. The error in electronic conductivity is based on averaging the steady-state current.

A thicker pellet ( B 800 m m) of the SE was pressed for the ionic conductivity measurements. The ionic conductivity was measured by the EIS (200 mV amplitude) of the SE pellets in the frequency range from 1 MHz to 100 Hz under the constant pressure of 255 MPa. The bulk ionic resistance of the SE was estimated from the positive intercept of the experimental spectra. The error in ionic conductivity is based on multiple measurements.

The cells were assembled in an Ar-filled glovebox. LiNi0.85Co0.1Mn0.05O2 (NCM85, BASF, D50 = 5 m m) or LiNi1/3Co1/3Mn1/3O2 (NCM111, NEI Corporation, D50 = 8-12 m m) active materials were ground with a chloride SE in a mass ratio of 4 : 1 for 1 hour. No carbon was added to the cathode to avoid oxidation of the SE at the carbon surface.

The NCM SSB cells were assembled in several steps. First, 70 mg of argyrodite (Li5.5PS4.5Cl1.5) SE and 30 mg of a chloride SE were pressed into a bilayer pellet in a 10 mm PEEK cylinder at 1 ton for 2 minutes. Then, B 6.5-7.5 mg of the NCM-chloride SE composite was uniformly spread over the chloride side of the SE and pressed at 2 tons for 5 minutes. We note that 30 mg of a halide SE translates into a 4 100 m mthick layer ( r (halide SE) E 2.5 g cm /C0 3 ) that prevents any physical contact between the argyrodite Li5.5PS4.5Cl1.5 layer and the NCM-chloride SE composite. Next, an In/InLi anode was prepared by attaching a 10 mm In electrode (100 m mthick) to the sulfide layer of the cathode/SE pellet. Finally, an 8 mm 50 m m Li on Cu foil (China Lithium Energy) was placed on the In disc, and the cell was placed into a custom-made stainless steel cage with a constantly applied pressure of B 250 MPa. The In/InLi anode was separated from the Li-M-Cl by the argyrodite layer to prevent reduction of the Li-M-Cl. 57 The areal loading of NCM B 7 mg cm /C0 2 provides a theoretical capacity of 1.4 mA h cm /C0 2 . SSB cells were cycled at a constant current of 0.2C (1C = 200 mA h g /C0 1 ) within the voltage windows of 2.08-3.68 V and 2.08-3.98 V vs. In/InLi (ie, 2.7-4.3 V and 2.7-4.6 V vs. Li + /Li) at room temperature. Voltage vs. In/InLi was converted to voltage vs. Li + /Li by adding 0.62 V because polarization of the In/InLi anode is effectively negligible, as its contribution to the overall cell polarization is only B 3 mV at a cathode loading of B 7 mg cm /C0 2 and a current density of 0.28 mA cm /C0 2 .

Two cells made with each SE were cycled to 4.3 V vs. Li + /Li, and one cell with each SE was cycled to 4.6 V vs. Li + /Li. The performance retention of the In/InLi||NCM85 SSB cells is consistent with the previously reported by our group. 31

In situ EIS of the SSB cells was measured at a voltage of 3.8 V vs. Li + /Li every charging step between 1 MHz and 20 mHz. Before the EIS acquisition, the SSB cells were held at constant voltage until a C/100 current cutoff. EIS of the SSB cells during aging was recorded from 1 MHz to 100 mHz hourly for 30 hours. Before the aging step, the SSB cells were charged to the cutoff voltage of 4.1, 4.3, or 4.6 V vs. Li + /Li Li at a current of 0.2C and then held at the cutoff voltage until the current decayed to 0.01C. The voltage amplitude was 10 mV for all the experiments.

The temporal evolution of the cathode resistance ( R cathode) at different cutoff voltage was fitted via a parabolic growth function as described by Zuo et al. 17 The values of R cathode at 4.1 V are based on one cell per SE. At 4.3 V R cathode of NCM85-LYZC is the average of three cells, and R cathode of NCM85-LIC is the average of 2 cells. At 4.6 V, R cathode of NCM85-LIC was calculated as an average of three reproducible cells. Due to the significantly higher impedance of NCM85-LYZC, its growth constant k was calculated based on one cell. R cathode of NCM85-LSIC at 4.3 V and 4.6 V were calculated based on one cells per voltage point due to their consistency with the previously reported results. 31 The error in kinetic constant k represents the fitting error.

The cells for CV measurements were prepared similarly to the NCM SSB cells, except no Li was placed on In foil. The carbon-SE composites for CV studies were prepared by grinding C65 carbon (MTI) and chloride SE in a mass ratio of 1: 9.

Electrochemical stability of the SEs mixed with C-65 carbon was studied by stepwise CV between 2.7 and 4.6 V vs. Li + /Li. Initially, the voltage was swept from OCV to 4.1 V and then cycled once between 2.7 and 4.1 V vs. Li + /Li. Then, the cells were cycled twice within the range of 2.7-4.3 V vs. Li + /Li and 2.7-4.6 V vs. Li + /Li. The onset of the SE oxidation was evaluated from the last scan to 4.6 V vs. 4.6 V vs. Li + /Li. The CV was performed at a rate of 0.1 mV s /C0 1 .

## 4.3. UPS

For measuring UPS on chloride SSEs, the SSE powders were dispersed in xylene and screen printed on Al foil, followed by pressing with 100 MPa to obtain thin and flat films of the SSEs. The samples were prepared and transferred to the photoelectron chamber without air contact. The coverage of the films was confirmed by measuring XPS spectra prior to UPS, showing no signal of the Al substrate. UPS was carried out on a PHI5000 Versa Probe II system (Physical Electronics Inc) equipped with a He-I a source (21.22 eV). In order to properly observe the high binding energy cutoff, a sample bias of /C0 9 V was applied.

## 4.4. FIB-SEM

FIB-SEM images of SSB cathodes were recorded on a XEIA3 system (Tescan). Prior to the measurement, the cathodes were covered by a copper tape to ensure a flat surface and reduce the curtaining effect. Cross-sections were cut by a 2.5 m A Xe-ion beam and polished with a 0.1 m A Xe-ion beam. SEM was performed on these cross-sections by probing with a 5 kV, 500 pA electron beam and detecting the backscattered electrons with an in-beam detector.

## 4.5. Time-of-flight secondary ion mass spectrometry (ToFSIMS)

All pellet samples were transferred from Waterloo to Giessen under argon atmosphere. The cathodes were removed from the SSB cells in an Ar-filled glovebox and attached on a sample holder using an insulative tape. A transfer system Leica EM VCT500 (Leica Microsystems GmbH) was used to transfer the samples from glovebox to the ToF-SIMS instrument. ToF-SIMS characterization was performed by using a ToF-SIMS 5-100 system (IONTOF GmbH) equipped with a 25 keV Bi cluster primary ion gun for analysis.

During ToF-SIMS measurement, the surface of the samples was flooded with low-energy electrons to compensate charge. The negative ion mode using Bi3 + species and a cycle time of 60 m s were chosen for analysis. To minimize the effect of mass interference, the spectrometry (bunched) mode was used for surface analysis to enable a high signal intensity and a high mass resolution (FWHM m / D m 4 5000 @ m / z = 34.97 (Cl /C0 )). The analysis area was set to 150 /C2 150 m m 2 and rasterized with 256 /C2 256 pixels, and every patch was analyzed with 1 frame and 1 shot per pixel and frame. The primary ion current was ca. 0.5 pA, and the stop condition was set to a primary ion dose of 10 12 ions cm /C0 2 . To quantitatively compare the specific signal intensity, we collected more than 10 mass spectra at different areas on each sample.

|

o

.

S

c

v

i

g

y

E

n

e

r

All ToF-SIMS data was evaluated with SurfaceLab 7.0 (IONTOF GmbH) software. In this work, the spectra were normalized in relation to the total ion signal, and the signal intensities in the box plots were extracted from the respective normalized secondary ion images.

## 4.6. DFT calculations

The Vienna ab initio simulation package (VASP) 58,59 was used to perform density functional theory (DFT) total energy calculations. The planewave pseudopotentials with projector augmented wave (PAW) potentials for core electrons were used, and the exchange-correlation term was treated with the Perdew-BurkeErnzerhof (PBE) version within the generalized gradient approximation (GGA). 60,61 All the DFT calculations were performed with input parameters compatible with the Materials Project (MP) database. 62 The ScOCl ground state, missing in the Materials Project (MP) database, was obtained using a reported structure from Springer Material. 63 To obtain the low energy configurations of LIC, LSIC, and LYZC we have generated, using pymatgen, 64 the 50 lowest Ewald energy structural orderings considering the partial occupancies of the atomic species in their experimental structures. 25,31 These structural orderings were computed using DFT, and the lowest DFT energy configurations were used to explore the interface reaction energies. We have used a pseudo-binary mixing approach of two reactants to calculate interfacial reactivity among Li x NiO2 (an approximation to NCM85) and chloride SEs as described in detail elsewhere. 14,15,17 The calculated reaction energies and reaction products for most energetically favorable reactions involving oxide chlorides as products, at various states of charges of Li x NiO2, are summarized in Table 1.

## Author contributions

L. F. N. and J. J. conceived the concept and designed the experimental work. I. K, L. Z. and K. K. performed the synthesis of the solid electrolytes. I. K. and K. K. carried out the electrochemistry of the all-solid-state batteries; I. K. carried out the CV experiments and the EIS measurements and their analysis. R. R. carried out the FIB-SEM and UPS studies and contributed to the EIS data analysis; B. S. performed the DFT calculations. T. T. Z. performed the TOF-SIMS measurements, data analysis was performed by T. T. Z. and J. J. I. K. and L. F. N. wrote the manuscript with much input from the other co-authors for their sections.

## Conflicts of interest

There are no conflicts to declare.

## Acknowledgements

This work was supported (L. F. N., L. Z, K. K and B. S) by the Joint Center for Energy Storage Research, an Energy Innovation Hub funded by the US Department of Energy (DOE), Office of

Science, Basic Energy Sciences. Platform support to L. F. N was provided by NSERC via their Canada Research Chair and Discovery Grant programs, and partial funding (I. K.) was provided by BASF SE, who are also gratefully acknowledged for supplying the NCM85 cathode active material. J. J. thanks the German Federal Ministry of Education and Research (BMBF) for funding of the project EProFest (03XP0346D).

## References

- 1 T. Placke, R. Kloepsch, S. Du ¨hnen and M. Winter, J. Solid State Electrochem. , 2017, 21 , 1939-1964.
- 2 J. Janek and W. G. Zeier, Nat. Energy , 2016, 1 , 1-4.
- 3 R. Schmuch, R. Wagner, G. Ho ¨rpel, T. Placke and M. Winter, Nat. Energy , 2018, 3 , 267-278.
- 4 S. Randau, D. A. Weber, O. Ko ¨tz, R. Koerver, P. Braun, A. Weber, E. Ivers-Tiffe ´e, T. Adermann, J. Kulisch, W. G. Zeier, F. H. Richter and J. Janek, Nat. Energy , 2020, 5 , 259-270.
- 5 Y. Y.-K. Sun, ACS Energy Lett. , 2020, 5 , 3221-3223.
- 6 N. Kamaya, K. Homma, Y. Yamakawa, M. Hirayama, R. Kanno, M. Yonemura, T. Kamiyama, Y. Kato, S. Hama, K. Kawamoto and A. Mitsui, Nat. Mater. , 2011, 10 , 682-686.
- 7 M. A. Kraft, S. Ohno, T. Zinkevich, R. Koerver, S. P. Culver, T. Fuchs, A. Senyshyn, S. Indris, B. J. Morgan and W. G. Zeier, JACS , 2018, 140 , 16330-16339.
- 8 P. Adeli, J. D. Bazak, K. H. Park, I. Kochetkov, A. Huq, G. R. Goward and L. F. Nazar, Angew. Chem. , 2019, 131 , 8773-8778.
- 9 L. Zhou, A. Assoud, Q. Zhang, X. Wu and L. F. Nazar, JACS , 2019, 141 , 19002-19013.
- 10 X. Feng, P.-H. Chien, Y. Wang, S. Patel, P. Wang, H. Liu, M. Immediato-Scuotto and Y.-Y. Hu, Energy Storage Mater. , 2020, 30 , 67-73.
- 11 G. F. Dewald, S. Ohno, M. A. Kraft, R. Koerver, P. Till, N. M. Vargas-Barbosa, J. Janek and W. G. Zeier, Chem. Mater. , 2019, 31 , 8328-8337.
- 12 T. K. Schwietert, A. Vasileiadis and M. Wagemaker, JACS Au , 2021, 1 , 1488-1496.
- 13 S. Ohno, C. Rosenbach, G. F. Dewald, J. Janek and W. G. Zeier, Adv. Funct. Mater. , 2021, 31 , 2010620.
- 14 W. D. Richards, L. J. Miara, Y. Wang, J. C. Kim and G. Ceder, Chem. Mater. , 2016, 28 , 266-273.
- 15 Y. Zhu, X. He and Y. Mo, J. Mater. Chem. A , 2016, 4 , 3253-3266.
- 16 F. Walther, R. Koerver, T. Fuchs, S. Ohno, J. Sann, M. Rohnke, W. G. Zeier and J. Janek, Chem. Mater. , 2019, 31 , 3745-3755.
- 17 T.-T. Zuo, R. Rueß, R. Pan, F. Walther, M. Rohnke, S. Hori, R. Kanno, D. Schro ¨der and J. Janek, Nat. Commun. , 2021, 12 , 1-10.
- 18 S. H. Jung, K. Oh, Y. J. Nam, D. Y. Oh, P. Bru ¨ner, K. Kang and Y. S. Jung, Chem. Mater. , 2018, 30 , 8190-8200.
- 19 S. P. Culver, R. Koerver, W. G. Zeier and J. Janek, Adv. Energy Mater. , 2019, 9 , 1900626.
- 20 A.-Y. Kim, F. Strauss, T. Bartsch, J. H. Teo, T. Hatsukade, A. Mazilkin, J. Janek, P. Hartmann and T. Brezesinski, Chem. Mater. , 2019, 31 , 9664-9672.
- 21 J.-M. Kim, X. Zhang, J.-G. Zhang, A. Manthiram, Y. S. Meng and W. Xu, Mater. Today , 2021, 46 , 155-182.
- 22 Y. Ma, J. H. Teo, F. Walther, Y. Ma, R. Zhang, A. Mazilkin, Y. Tang, D. Goonetilleke, J. Janek, M. Bianchini
- and T. Brezesinksi, Adv. Funct. Mater. , 2022, 2111829.
- 23 T. Asano, A. Sakai, S. Ouchi, M. Sakaida, A. Miyazaki and S. Hasegawa, Adv. Mater. , 2018, 30 , 1803075.
- 24 X. Li, J. Liang, J. Luo, M. N. Banis, C. Wang, W. Li, S. Deng, C. Yu, F. Zhao, Y. Hu, T.-K. Sham, L. Zhang, S. Zhao, S. Lu, H. Huang, R. Li, K. R. Adair and X. Sun, Energy Environ. Sci. , 2019, 12 , 2665-2671.
- 25 K.-H. Park, K. Kaup, A. Assoud, Q. Zhang, X. Wu and L. F. Nazar, ACS Energy Lett. , 2020, 5 , 533-539.
- 26 S. Y. Kim, K. Kaup, K.-H. Park, A. Assoud, L. Zhou, J. Liu, X. Wu and L. F. Nazar, ACS Mater. Lett. , 2021, 3 , 930-938.
- 27 J. Park, D. Han, H. Kwak, Y. Han, Y. J. Choi, K.-W. Nam and Y. S. Jung, Chem. Eng. J. , 2021, 425 , 130630.
- 28 E. A. Wu, S. Banerjee, H. Tang, P. M. Richardson, J.-M. Doux, J. Qi, Z. Zhu, A. Grenier, Y. Li, E. Zhao, G. Deysher, E. Sebti, H. Nguyen, R. Stephens, G. Verbist, K. W. Chapmen, R. J. Clement, A. Banerjee, Y. S. Meng and S. P. Ong, Nat. Commun. , 2021, 12 , 1-11.
- 29 H. Kwak, D. Han, J. P. Son, J. S. Kim, J. Park, K.-W. Nam, H. Kim and Y. S. Jung, Chem. Eng. J. , 2022, 437 , 135413.
- 30 L. Zhou, C. Y. Kwok, A. Shyamsunder, Q. Zhang, X. Wu and L. F. Nazar, Energy Environ. Sci. , 2020, 13 , 2056-2063.
- 31 L. Zhou, T.-T. Zuo, C. Y. Kwok, S. Y. Kim, A. Assoud, Q. Zhang, J. Janek and L. F. Nazar, Nat. Energy , 2022, 7 , 83-93.
- 32 G. Xu, L. Luo, J. Liang, S. Zhao, R. Yang, C. Wang, T. Yu, L. Wang, W. Xiao, J. Wang, J. Yu and X. Sun, Nano Energy , 2021, 92 , 106674.
- 33 H. Kwak, D. Han, J. Lyoo, J. Park, S. H. Jung, Y. Han, G. Kwon, H. Kim, S.-T. Hong, K.-W. Nam and Y. S. Jung, Adv. Energy Mater. , 2021, 11 , 2003190.
- 34 R. Schlem, A. Banik, S. Ohno, E. Suard and W. G. Zeier, Chem. Mater. , 2021, 33 , 327-337.
- 35 K. Wang, Q. Ren, Z. Gu, C. Duan, J. Wang, F. Zhu, Y. Fu, J. Hao, J. Zhu, L. He, C.-W. Wang, Y. Lu, J. Ma and C. Ma, Nat. Commun. , 2021, 12 , 1-11.
- 36 R. Weber, M. Genovese, A. J. Louli, S. Hames, C. Martin, I. G. Hill and J. R. Dahn, Nat. Energy , 2019, 4 , 683-689.
- 37 S.-J. Cho, D.-E. Yu, T. P. Pollard, H. Moon, M. Jang, O. Borodin and S.-Y. Lee, iScience , 2020, 23 , 100844.
- 38 Z. Yu, H. Wang, X. Kong, W. Huang, Y. Tsao, D. G. Mackanic, K. Wang, X. Wang, W. Huang and S. Choudhury, Nat. Energy , 2020, 5 , 526-533.
- 39 R. Ruess, S. Schweidler, H. Hemmelmann, G. Conforto, A. Bielefeld, D. A. Weber, J. Sann, M. T. Elm and J. Janek, J. Electrochem. Soc. , 2020, 167 , 100532.
- 40 Y. Han, S. H. Jung, H. Kwak, S. Jun, H. H. Kwak, J. H. Lee, S.-T. Hong and Y. S. Jung, Adv. Energy Mater. , 2021, 11 , 2100126.

- 41 J. Mos ˇkon, J. Z ˇuntar, S. D. Talian, R. Dominko and M. Gabers ˇc ˇek, J. Electrochem. Soc. , 2020, 167 , 140539.
- 42 B. A. Boukamp and H. J. Bouwmeester, Solid State Ionics , 2003, 157 , 29-33.
- 43 P. Braun, C. Uhlmann, M. Weiss, A. Weber and E. IversTiffe ´e, J. Power Sources , 2018, 393 , 119-127.
- 44 T. Koç, F. Marchini, G. Rousse, R. Dugas and J.-M. Tarascon, ACS Appl. Energy Mater. , 2021, 4 , 13575-13585.
- 45 K. Ma ¨rker, P. J. Reeves, C. Xu, K. J. Griffith and C. P. Grey, Chem. Mater. , 2019, 31 , 2545-2554.
- 46 J. Emara, T. Schnier, N. Pourdavoud, T. Riedl, K. Meerholz and S. Olthof, Adv. Mater. , 2016, 28 , 553-559.
- 47 A. H. Nethercot Jr, Phys. Rev. Lett. , 1974, 33 , 1088.
- 48 A. Campero and J. A. Diaz Ponce, ACSOmega , 2020, 5 , 25520-25542.
- 49 D. Park, H. Park, Y. Lee, S.-O. Kim, H.-G. Jung, K. Y. Chung, J. H. Shim and S. Yu, ACS Appl. Mater. Interfaces , 2020, 12 , 34806-34814.
- 50 T. Krauskopf, F. H. Richter, W. G. Zeier and J. Janek, Chem. Rev. , 2020, 120 , 7745-7794.
- 51 T. K. Schwietert, V. A. Arszelewska, C. Wang, C. Yu, A. Vasileiadis, N. J. de Klerk, J. Hageman, T. Hupfer, I. Kerkamm, Y. Xu, E. van der Mass, E. M. Kelder, S. Ganapathy and M. Wagenmaker, Nat. Mater. , 2020, 19 , 428-435.
- 52 R. Jung, M. Metzger, F. Maglia, C. Stinner and H. A. Gasteiger, J. Electrochem. Soc. , 2017, 164 , A1361.
- 53 T. Bartsch, F. Strauss, T. Hatsukade, A. Schiele, A.-Y. Kim, P. Hartmann, J. Janek and T. Brezesinski, ACS Energy Lett. , 2018, 3 , 2539-2543.

|

- 54 H. Li, A. Liu, N. Zhang, Y. Wang, S. Yin, H. Wu and J. R. Dahn, Chem. Mater. , 2019, 31 , 7574-7583.
- 55 S. Wang, Q. Bai, A. M. Nolan, Y. Liu, S. Gong, Q. Sun and Y. Mo, Angew. Chem., Int. Ed. , 2019, 58 , 8039-8043.
- 56 H. Chun, K. Nam, S. J. Hong, J. Kang and B. Han, J. Mater. Chem. A , 2021, 133 , 15605.
- 57 L. M. Riegger, R. Schlem, J. Sann, W. G. Zeier and J. Janek, Angew. Chem. , 2021, 133 , 6792-6797.
- 58 G. Kresse and J. Furthmu ¨ller, Phys. Rev. B: Condens. Matter Mater. Phys. , 1996, 54 , 11169.
- 59 G. Kresse and J. Furthmu ¨ller, Comput. Mater. Sci. , 1996, 6 , 15-50.
- 60 P. E. Blo ¨chl, Phys. Rev. B: Condens. Matter Mater. Phys. , 1994, 50 , 17953.
- 61 J. P. Perdew, K. Burke and M. Ernzerhof, Phys. Rev. Lett. , 1996, 77 , 3865.
- 62 A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D. Richards, S. Dacek, S. Cholia, D. Gunter, D. Skinner, G. Ceder and K. A. Persson, APL Mater. , 2013, 1 , 011002.
- 63 ScOCl (ScClO, T = 540 K) Crystal Structure: ( https://materi als.springer.com/isp/crystallographic/docs/sd\_1238827 ).
- 64 S. P. Ong, W. D. Richards, A. Jain, G. Hautier, M. Kocher, S. Cholia, D. Gunter, V. L. Chevrier, K. A. Persson and G. Ceder, Comput. Mater. Sci. , 2013, 68 , 314-319.
- 65 J. Hozl and F. K. Schulte, Work function of metals, in Holzl's, Schulte's, Wagner's Solid Surface Physics, Springer Tracts in Modern Physics , Springer; Berlin, Heidelberg, 1979, vol. 85, p. 28.