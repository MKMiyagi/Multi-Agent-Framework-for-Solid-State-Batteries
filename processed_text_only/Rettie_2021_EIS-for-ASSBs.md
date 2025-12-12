## Electrochemical Impedance Spectroscopy for All-Solid-State Batteries: Theory, Methods and Future Outlook

Pooja Vadhva + , [a] Ji Hu + , [a, b] Michael J. Johnson + , [a] Richard Stocker, [c] Michele Braglia, [c] Dan J. L. Brett, [a, b] and Alexander J. E. Rettie* [a, b]

Electrochemical impedance spectroscopy (EIS) is widely used to probe the physical and chemical processes in lithium (Li)-ion batteries (LiBs). The key parameters include state-of-charge, rate capacity or power fade, degradation and temperature dependence, which are needed to inform battery management systems as well as for quality assurance and monitoring. All-solid-state batteries using a solid-state electrolyte (SE), promise greater energy densities via a Li metal anode as well as enhanced safety, but their development is in its nascent stages and the

## 1. Introduction

Electrochemical energy storage devices have received increased attention in recent years due to the importance of electrifying the transport sector to minimize the effects of climate change. Generally, battery systems with higher gravimetric energy densities (important for range and vehicle weight) and improved safety are desired. All-solid-state battery (ASB) systems with a solid-state electrolyte (SE) could exceed the performance of state-of-the-art lithium (Li)-ion batteries (LiBs) with liquid electrolytes in these respects. [1,2]

The reasoning behind these improvements is that a SE could enable a Li-metal anode (LMA) over the commonly used graphite intercalation anode, by stabilizing the reactive Li j electrolyte interface. [3] Lithium has the lowest reduction potential of any known element ( GLYPH&lt;0&gt; 3.04 V vs. the standard hydrogen electrode) and a high theoretical specific capacity of 3860 mAhg GLYPH&lt;0&gt; 1 . Additionally, bipolar stacking is possible with ASBs which further increases the energy density. [4] As the conventional organic liquid electrolytes used in LiBs are flammable, replacement with a SE also improves battery safety by mitigating thermal run-away and leakage. However, challenges exist at moderate to high rate operation due to Li metal dendrites, which can propagate through the electrolyte and short ASBs. [5]

Recently, an ASB composed of an LMA, SE and high-capacity intercalation electrode exhibited an energy density in excess of &gt; 900 WhL GLYPH&lt;0&gt; 1 (versus ~770 WhL GLYPH&lt;0&gt; 1 for current Li-ion) [6] at the cell level over hundreds of cycles. [7] SEs are likely to play a

[a] P. Vadhva, + J. Hu, + M. J. Johnson, + Prof. D. J. L. Brett, Dr. A. J. E. Rettie Electrochemical Innovation Lab, Department of Chemical Engineering University College London

Bloomsbury, London, WC1E 6BT, UK

E-mail: a.rettie@ucl.ac.uk

[b] J. Hu, + Prof. D. J. L. Brett, Dr. A. J. E. Rettie The Faraday Institution Quad One, Harwell Campus, OX11 0RA, UK

[c] R. Stocker, M. Braglia Horizon Scanning Department, HORIBA MIRA Ltd. Watling Street, Nuneaton, Warwickshire, CV10 0TU, UK

EIS measurement, cell set-up and modelling approach can be vastly different for various SE chemistries and cell configurations. This review aims to condense the current knowledge of EIS in the context of state-of-the-art solid-state electrolytes and batteries, with a view to advancing their scale-up from the laboratory to commercial deployment. Experimental and modelling best practices are highlighted, as well as emerging impedance methods for conventional LiBs as a guide for opportunities in the solid-state.

significant role in other 'beyond Li-ion technologies' based on LMAs such as Li-sulfur (Li GLYPH&lt;0&gt; S) and Li-air. These may be completely solid-state devices, or hybrid devices with a SEprotected LMA and a liquid electrolyte, [8] however for simplicity we will focus on all-solid systems in this review.

The bulk and interfacial transport processes that determine battery performance take place over many length- and timescales. Electrochemical impedance spectroscopy (EIS) is a nondestructive technique which spans ~10 9 orders of magnitude in the frequency domain (mHz to MHz) and is widely used to investigate new SE materials and probe stability at various interfaces. Sample and interfacial contributions to the impedance can be separated and tracked with respect to temperature, applied pressure, state-of-charge (SoC) and ageing. These can be used to inform quality and assurance monitoring on the cell and pack level, give insights into battery degradation, develop virtual tools to quickly yet effectively simulate vehicle development (saving cost and time), and provide a wealth of information for battery management systems (BMS).

Currently, the only commercially available ASBs are thin-film devices or those based on a solid polymer electrolyte which must be operated at elevated temperatures and are incompatible with high voltage cathode materials. [9] The discovery of highly conductive inorganic Li-ion conductors [10] and the recent advent of cell-level devices in the laboratory motivates a thorough review of cell designs and analytical approaches for EIS applied to solid-state batteries. EIS measurement and interpretation are often non-standardized and Li-containing solid-state configurations pose unique experimental and modelling challenges. This review aims to highlight the diversity of experimental and modelling approaches with a focus on best practices and identify future opportunities both from state-ofthe-art Li-ion and solid-state devices from related fields. It is intended that these insights will be useful to the electrochemists and engineers working in this burgeoning area to push ASBs from laboratory-scale devices to large-format cells and drive their uptake into commercial packs.

## 2. Theory, Methods and Analysis

In a typical EIS experiment, a small sinusoidal perturbation voltage, E ( t ) is applied to an electrochemical system. The resulting linear current density, j ( t ) shares the frequency of the input, but its phase and amplitude may differ (Figure 1). The ratio of these quantities is the impedance, Z ( t ) [Equation (1)],

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

Figure 1. Plot describing the relationship between the input voltage, E ( t ) and output current, j ( t ) (or vice versa), the ratio of which results in impedance.

<!-- formula-not-decoded -->

The above experiment is termed potentiostatic EIS (PEIS) and the analogue when the input is an alternating current is known

Pooja Vadhva is a Ph.D. student in the Department of Chemical Engineering, University College London (UCL, UK). She holds a Masters' degree in Physics from the University of Manchester where she worked on solar energy conversion. Her current interests are solid electrolytes and thin-film membranes for protection of lithium metal anodes, working in collaboration with industry.

Ji Hu is a Ph.D. student at the Electrochemical Innovation Lab (EIL) in the Department of Chemical Engineering at UCL (UK). Ji received his B.Eng. degree from Monash University in Australia and Central South University in China. Prior to joining the EIL, he was an engineer for BYD battery group for over three years. His research interests are in solid-state and Li-sulfur batteries.

Michael Johnson is a Ph.D. student in the Department of Chemical Engineering at the Electrochemical Innovation Lab, UCL (UK). He received his M.Chem. from the University of Liverpool in 2019, where his work focused on the synthesis of lithiumand sodium-ion battery materials. His current research focuses on the advanced characterization of battery materials using X-ray and neutron scattering techniques.

Richard Stocker is an Innovation Lead for the Energy Systems Division of the HORIBA MIRA Horizon Scanning Department (UK). He is also currently doing a Ph.D. in battery degradation analysis and modelling with Coventry University. His research interests span electrochemical devices including batteries, fuel cells and flow cells, with a focus on holistic testing and modelling methodology, and novel state estimation and control strategies.

as galvanostatic EIS (GEIS). By varying frequency, processes at different timescales can be observed. At high frequencies only the fastest processes, such as ion migration, can respond, while slow phenomena, such as diffusion, dominate the low-frequency tail of the spectrum.

In the case of PEIS, the alternating voltage input E ( t ) can be written as Equation (2):

<!-- formula-not-decoded -->

(2)

where, j Δ E j is the peak voltage amplitude, ω is the angular frequency and t is time. A small amplitude perturbation (typically ( &lt; 50 mV) means two important assumptions hold: (i) the functional form of the input and output are the same, and (ii) they have a linear relationship, which simplifies data analysis by avoiding higher harmonic terms and minimizing irreversible changes to the electrochemical system under study. These conditions can be verified using the Kramers-Kronig (K GLYPH&lt;0&gt; K) relations (see Section 2.2). In this case, Equation (3) follows,

Dr. Michele Braglia is a Research Scientist in Electrochemical Conversion and Storage in the Horizon Scanning Department at HORIBA MIRA (UK). He received his Ph.D. from the AixMarseille University in 2017, with a thesis on single-ion conducting polymers for solid-state batteries and fuel cells. His current research focuses on non-invasive diagnostic and characterization techniques at cell level, modelling and virtual tools development around batteries.

Dan Brett is a Professor of Electrochemical Engineering in the Electrochemical Innovation Lab at UCL. His research interests include batteries, fuel cells and supercapacitors and in particular the application of novel diagnostic techniques to understand the operation of these technologies. Dan has been applying EIS to the study of electrochemical power systems for over 20 years.

Dr. Alex Rettie is a Lecturer (Assistant Professor) in Electrochemical Conversion and Storage in the Department of Chemical Engineering, UCL (UK). His interests are in the experimental discovery and characterization of electrochemical energy materials and their incorporation into devices, with a focus on electronic and ionic charge transport.

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

<!-- formula-not-decoded -->

where, j Δ j j is the amplitude of the current density, Δ t is the phase difference which is closely related to the time constant of the system and the quantity ( ω t + Δ t ) is the phase angle, ϕ . Because the quantities E ( t ) and j ( t ) contain magnitude and phase information they can be represented as complex numbers; thus, Z ( t ) is also a complex number with real and imaginary components: Re( Z ) and Im( Z ) or Z' and Z'' , respectively. We will avoid mathematical definitions of these and other quantities in the interest of clarity, but direct the reader to excellent references containing detailed derivations. [11-14]

## 2.1. Impedance Plots

A significant amount of information is acquired by varying the applied frequency in an EIS measurement. Two graphs are commonly used to fully represent this complex dataset: Nyquist and Bode plots (Figure 2). They are complementary and contain the same data, i.e., Re( Z ), Im( Z ), the modulus of Z [Equation (4)],

<!-- formula-not-decoded -->

and ϕ as a function of ω [Equation (5)],

<!-- formula-not-decoded -->

These related quantities provide visual cues in the aforementioned plots that aid in the analysis of experimental data. To illustrate their use, it is instructive to consider a simple, idealized charge transfer process.

Deconvolution of processes and their characteristic time constants is achieved by modelling the electrochemical system as an equivalent electrical circuit. A commonly employed element combination is a resistor and capacitor in parallel: an ' RC ' unit which has a characteristic time constant, τ [s] =

Figure 2. a) Equivalent circuit for single electron transfer and ion migration in the electrolyte. b) Nyquist plot of the real impedance against the imaginary impedance showing the resistance for the electrolyte. c) Bode plot of the magnitude of the impedance and phase angle against frequency.

resistance [Ohms] � capacitance [Farads]. For example, a resistor, R0 in series with an ( RC)1 element and capacitor, C2 is commonly used to model dielectric materials and determine SE conductivity using ion-blocking electrodes (Figure 2a). A key assumption in the use of this circuit is that conduction in the SE is purely ionic.

As shown in Figure 2b, the Nyquist plot ( GLYPH&lt;0&gt; Im( Z ) vs. Re( Z )) contains a symmetrical arc with an offset from the origin on the x -axis corresponding to the resistance, R0 , which may include resistances from wires and contacts. The frequency at the apex of the semicircle gives an estimate of the time constant associated with the conduction process, τ = ( RC ) 1 (where ω in radians s GLYPH&lt;0&gt; 1 is related to f in s GLYPH&lt;0&gt; 1 or Hz by ω = 2 π f ), while the capacitor, C2 manifests as a vertical line at low frequency. Complementary information is given in the Bode plot, which plots both j Z ( ω ) j and ϕ vs. frequency. This is visible in j Z ( ω ) j vs. f (Figure 2c): a plateau followed by a slope of GLYPH&lt;0&gt; 1 is equal to a semicircle in the Nyquist plot, while ϕ vs. f is sensitive to model fitting parameters.

Additionally, the Bode plots present EIS data in the time domain, thus we can relate specific impedance contributions to their respective time constants, which is not explicitly obtained from the Nyquist plot. Nyquist plots are by far the most common in ASB research, though complementary Bode plots may be included in the detailed evaluation of specific impedance spectra.

## 2.2. Cell Design

EIS can be used to determine bulk electrolyte/electrode properties, probe interfacial reactions and analyse full cell device behaviour. Electrochemical cell design - electrode type, configuration, geometry, etc. - is hugely influential on the resulting impedance spectra and a critical part of any EIS experiment. [15]

Three general types of electrodes are used in electrochemical measurements: ion-blocking, electron-blocking and reversible. [16] In all cases, the contacting material should be inert and stable against the sample being tested . Ion-blocking electrodes do not accept or provide Li-ions but do allow the passage of electrons. Examples include metals such as platinum, stainless steel and gold. SEs with high ionic conductivity and negligible electronic conductivity (see Sections 3-6 for examples) may function as electron-blocking contacts to isolate the ionic component of charge transport. This can be especially useful in the study of mixed ionic-electronic conductors (MIECs) such as cathode or anode materials and solid electrode-electrolyte composites. [17] Finally, reversible electrodes facilitate both ionic and electronic transport. Li metal is by far the most common reversible electrode material, despite the fact most materials are chemically unstable against it. [6,18,19] Li alloys, such as Li-indium (In) and intercalation electrodes may function as alternatives, providing the material under study is stable against them.

Two-electrode EIS measurements are typical as they are experimentally simple and can be applied to a material, cell or pack straightforwardly without modification. For example, EIS of a 2-electrode cell using symmetric ion-blocking electrodes is

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

routinely used to extract the ionic conductivity, σ ion of SEs, [20] given by:

<!-- formula-not-decoded -->

where, Rtotal is the total resistance of the electrolyte sample (corresponding to R1 in Figure 2a), l is the sample thickness and A is the area. In this case, Rtotal may include different resistance contributions: the resistance from the grain but additionally the grain or phase boundaries depending on the material's microstructure (see Sections 4, 5 and 6). Also, any impedances associated with the electrodes and their interfaces will be included in the resulting spectra as are any physical or chemical changes that may occur. When these processes are convoluted, additional electrodes can be beneficial for analysis.

Four-point probe measurements remove electrode contributions by adding sensing electrodes through which no current flows and so may aid in the assignment of medium- and lowfrequency features, e.g. grain boundaries or interfacial layers. This configuration is seldom used in the ASB literature. Kežionis et al. developed a 4-point probe for EIS measurements using polycrystalline Gd-doped ceria as a model electro-ceramic system. [21] As can be seen in Figure 3, the feature that represents the impedance from the electrode j electrolyte interface was eliminated, allowing a more accurate value of the bulk electrolyte conductivity to be obtained. This is especially important for high ionic conductivity SEs where interfacial impedances can dominate. Caution should be exercised as stray capacitances (e.g., due to long cabling, additional connections) can affect measurements in the bar sample geometry (Figure 3b) due to reduced geometric capacitance compared with cylindrical samples (Figure 3a). [22]

Three-electrode cells are well-known to electrochemists, where the inclusion of a reference electrode (RE) at a fixed, stable potential is standard practice to monitor processes at the working electrode. However, the case for RE inclusion is controversial in the field of batteries, as the position, material and geometry of the RE can affect the readings taken and result in artefacts. [18] More so than batteries with liquid electrolytes, fabrication of solid-state cells with REs is non-trivial, especially if

Figure 4. Schematic representation of an all-solid-state 3-point probe cell of a) cell design 1 and b) cell design 2. Reproduced from Ref. [23] with permission. Copyright (2018) Royal Society of Chemistry.

the materials involved are air-sensitive, reactive or require high synthesis temperatures.

Several setups using a Li RE and a mechanically soft, sulfidebased SE have been proposed (Figure 4). [23] One example places the RE around the outer edge of the SE layer (Figure 4a), but this design suffers from the requirement of the SE layer being at least 1 mm in thickness for practical assembly in an inert atmosphere. An alternative design incorporates an additional SE layer sandwiched between the reference and working electrode, allowing for the thickness to be reduced (Figure 4b). As for reversible electrode materials, Li is a non-ideal choice due to its reactivity and unstable physical nature, and Li alloys, such as Li-indium, [24] and partially-lithiated intercalation electrodes have been proposed as alternatives. [18] Rigorous studies of SE-electrode compatibility and cell design to avoid artefacts are desirable.

Full cells represent working batteries, with positive and negative electrodes separated by an electrolyte. Spectra from these complete devices can be challenging to interpret as they may contain features from both electrodes, cell components and their interfaces. When EIS is performed, the charge or discharge is interrupted, and the cell is given sufficient time to relax to open circuit potential before data is acquired. A powerful experimental approach in the analysis of these complex systems in comparison with complementary symmetric cells, i. e. with two blocking or two reversible contacts to isolate each contribution. Currently, due to the relatively high resistance and minimal cell components compared to largeformat batteries, inductance does not play a significant role in

Figure 3. Schematic representation of the cell geometry for impedance measurements by the a) 2-electrode and b) 4-electrode setups. c) Nyquist plot of resistivity measured at 650 K of 2- and 4-electrode setups. Reprinted from Ref. [21] with the permission. Copyright (2013) AIP Publishing.

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

the EIS of laboratory-scale ASBs (even up to frequencies of several MHz). An exception to this is a hard short-circuit, where Li dendrite formation has resulted in direct electrical contact between the anode and cathode and inductive behaviour is observed. [25]

Temperature and pressure are important parameters in ASB research. The ionic conductivity is temperature-activated and commonly assigned an Arrhenius-like temperature dependence [Equation (7)]:

<!-- formula-not-decoded -->

where, Ea is the activation energy and R is the universal gas constant . A ( T ) is a model-dependent prefactor, which contains a T GLYPH&lt;0&gt; 1 term that must be incorporated to accurately extract Ea . [26] Robust determination of all parameters in Equation 7 requires that a sufficient temperature range is explored (at least 1 decade). Other resistance contributions have been tracked as functions of temperature and their activation energies estimated for assignment in LiBs. [27] Applied pressure is used both during initial cell formation and during cycling of ASBs to maintain good physical contact between the numerous solidsolid interfaces. Laboratory cells are usually bespoke and take three main forms: a pellet or coin-cell-type assembly, a leaktight cell [23] assembled in an inert environment that can be transferred to a temperature-controlled environment for testing, or a heated pressure apparatus within an inert-gas glovebox. [28,29]

Recently, the electronic conductivity, σ eon of SEs has been suggested to play a key role in the Li dendrite formation that limits the rate capability of ASBs. [30] Decoupling of the electronic and ionic conductivities by EIS is non-trivial, especially when σ ion @ σ eon as is the case for SEs. [16] Asymmetric two-electrode assemblies, i.e., one reversible and one blocking, are primarily used to determine the partial electronic conductivity by dc polarization in a Hebb-Wagner cell. [31,32] This technique cannot be used for many SE materials as it requires stability against Li metal. [33] Estimates of σ eon have been obtained by applying a constant dc voltage to a cell with symmetric ion-blocking electrodes and monitoring the residual leakage current until a steady-state value is reached ( &gt; 24 hrs). [26,34-37] However, we note that 2-electrode measurements will include additional contact resistances in a dc measurement and thus, underestimate the electronic conductivity. [38,39] Therefore, 4-point measurements are important for accurate determination. [40] Experimental EIS data must satisfy the conditions of linearity, stability and causality. An important check of data quality is to use Kronig-Kramers (K GLYPH&lt;0&gt; K) relations, [41,42] which test the expected interdependence of the real and imaginary components of a dataset adhering to the aforementioned criteria. Convenient tools exist for this evaluation [43] and their application is recommended to avoid time-consuming modelling of lowquality data and erroneous parameter estimation.

## 2.3. Modelling

The impedance of real systems is much more complex than the simulated circuit presented in Figure 2. Experimentally, a perfect semicircle in the Nyquist plot is rarely observed and processes with similar time constants will overlap, necessitating detailed modelling and fitting of spectra. Equivalent circuit modelling is the most widely used method and is accomplished by approximating the experimental data with an electrical circuit, followed by complex non-linear least squares (CNLS) fitting using dedicated software, e. g., ZView (Scribner Associates), RelaxIS 3 (rhd Instruments). Due to the CNLS fitting approach good starting values are required, which may or may not be available. As no solution to an EIS spectrum is unique, and the inclusion of more elements will tend to improve the fit of the equivalent circuit model (ECM), standard scientific modelling practice should be adhered to, i.e., using the simplest ECM with the fewest elements possible and ensuring that physical and chemical meaning is maintained. Table 1 contains commonly used circuit elements and plausible meanings.

Figure 5a depicts a generic ECM for different components in a conventional LiB: current collectors, electrodes, separator, liquid electrolyte and any insulating layers including solidelectrolyte interphase or decomposition products. [44] Each component is modelled by resistive, capacitive or diffusive elements and many physical elements may be negligible or convoluted in the resulting impedance (Figure 5b). [45] ASBs exhibit similar processes to LiBs with a liquid electrolyte, but with alterations, such as the SEI being represented by a solidsolid interphase impedance. One of the main differences is the SE itself, which may exhibit microstructural contributions and require more complex circuit modelling than in the case for a liquid electrolyte, where a single resistor is sufficient.

Ideal capacitors do not often feature in experimental data. Therefore, a constant phase element (CPE, symbol Q ) is used to simulate a non-ideal capacitor and an RQ element appears as a depressed semicircle in a Nyquist plot. The underlying reasons for the non-ideality of the capacitive process are not explicitly known, but have been assigned to inhomogeneity, surface roughness, porosity and tortuosity of the battery materials. [46] Jorcin et al. observed the contribution of geometry inhomogeneity through spatially-resolved EIS, where the depression factor was found to vary locally across an electrode surface. [47]

Although generic ECMs are available, it is often challenging to decipher how many time constants are present in a given dataset and their assignment can be highly subjective. Physical features in the cell may not be visible in the EIS spectra, particularly for larger cells where the inductance can obscure the visibility at high frequency while OCV variation due to small capacity changes can affect the low-frequency range, due to the difference in SoC at the start and end of the measurement. Order-of-magnitude evaluation of capacitance values can be used to assign features, e.g., grain vs. grain boundary, as shown by Irvine et al. [48] A powerful tool to guide ECM selection is the distribution of relaxation times (DRT) technique. [49] Here, impedance data is transformed from the frequency to time domain such that peaks associated with characteristic time-

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

Figure 5. a) Schematic representation of the equivalent circuit model used for a Li-ion battery. Republished from Ref. [44] with permission. Copyright (2016) The Westerhoff et.al. b) Depicts the Nyquist plot produced by fitting these parameters to the ECM shown for a typical Li-ion battery. Reproduced from Ref. [45] with permission. Copyright (2020) The Authors.

constants can be observed. Although DRT analysis is powerful and intuitive, it is limited in that the data must be bounded ( via somewhat arbitrary data preprocessing) and data inversion is mathematically ill-posed, requiring regularization methods. [50] DRT analysis is also very sensitive to experimental errors, meaning practical precautions and data evaluation, such as K GLYPH&lt;0&gt; K analysis are essential. The non-uniqueness of an ECM solution to an impedance spectrum means that information theory can be used to rank various ECMs against each other, for example, by the Akaike information criterion (AIC). [51] This method has only recently been applied to simulated immittance data [52] and thorough validation against experiment in the context of ASBs is desirable. In order to model a porous electrode, a transmission line model (TLM) can be introduced. [53,54] However, this model has only recently been used to investigate ASBs which incorporate composite electrodes. [55-57]

Beyond ad hoc equivalent circuit modelling, physical models can provide a deeper physical and chemical understanding of the system under study. [58,59] For electrochemical devices, these models start from the Nernst-Planck differential equations with suitable boundary conditions and are often simplified to one dimensional (1D) transport. Full cell battery models have been constructed in this way, with ECM fitting of experimental EIS data used to parameterize and validate the physical model. [60-62] Such 1D modelling is now readily available in commercial software packages, e. g. COMSOL Multiphysics. Further, 3D physical models of ASBs can make use of experimentallymeasured microstructural information to simulate high-capacity thin-film batteries [63] and bulk devices using porous solid-state electrodes. [64,65]

In the following sections, the application of EIS to ASB materials and devices is reviewed. These are differentiated based on SE chemistry as this most affects cell/device design

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

and modelling decisions. First, a model ASB system is considered: thin-film cells based on a lithium phosphorous oxynitride (LiPON) electrolyte. This is followed by SE candidates for highcapacity ASBs: sulfides, oxides, and polymer SEs.

## 3. LiPON Electrolytes

Developed by Bates and co-workers at Oak Ridge National Laboratory, [66,67] LiPON is an amorphous oxynitride SE with the approximate chemical formula Li a PO b N c , where a = ~3, b = ~4, c = 0.1-1.3 for optimal SE properties is reported, although marked variation exists in the literature. [34] LiPON forms a stable interphase against Li metal [68] and thin-film cells of the form Li j LiPON j LiCoO2 (LCO) and can be cycled over 1000 times at rates &gt; 1C. [67] Micron-thickness films are sputtered in a nitrogen (N) atmosphere, with N incorporation being key to moderate ionic conductivity (~10 GLYPH&lt;0&gt; 6 Scm GLYPH&lt;0&gt; 1 at room temperature). Their format is planar and thus the capacity is restricted to μ Ah values, only suitable for miniature devices and microelectronics. Micro-/ nano-structuring toward 3D thin-film batteries to increase capacity is an active field of research. [63,69]

As one of the most stable and well-established SE systems, the understanding of EIS in LiPON-based batteries is quite advanced. [71,72] Iriyama et al. [70] conducted an extensive and systematic EIS study using symmetric blocking (Pt j LiPON j Pt) and reversible (Li j LiPON j Li) configurations with a Li j LiPON j LCO cell to deconvolute full cell impedances. The lack of grain boundaries in amorphous LiPON means a single arc describes ionic transport in the Pt j LiPON j Pt cell (Figure 6a). A complementary symmetric cell with Li electrodes (Figure 6b) included both bulk and anode contributions. Robust assignment of bulk and interfacial features allowed the positive effect of temperature treatment to be attributed to reduced impedance at the LiPON j LCO interface.

The simple planar structure and the availability of LiPON devices have been beneficial for the development and

Figure 6. a) Cross-sectional SEM of a LiPON micro-battery. Reprinted from Ref. [67] with permission. Copyright (2000) Elsevier. b) EIS of Pt j LiPON j Pt and c) Li j LiPON j Li cells. Reprinted from Ref. [70] with permission. Copyright (2005) Elsevier. d) Compares EIS of a Li j LiPON j LiCoO2 full cell at 90 % and 10% SoC, whilst e) shows the overlay of EIS (dark blue) over DRT (light blue) at 90% SoC where three peaks can clearly be seen. Republished from Ref. [62] with permission. Copyright (2019) Royal Society of Chemistry.

validation of physical models. Recently, Pang et al. [62] developed a 1D physical model to describe the pulsed behaviour of a Li j LiPON j LCO battery. Experimental EIS at various SoC values was used to extract the following parameters for model validation: the ionic conductivity of LiPON, the exchange current densities and the diffusion coefficient in LCO. Data quality was explicitly confirmed using K GLYPH&lt;0&gt; K analysis before being analysed using the DRT method. This unambiguously identified three semicircles in the EIS spectra (Figure 6d), corresponding to bulk SE, SE j Li and SE j LCO from high to low frequency, consistent with previous work (Figure 6e). [70] The full cell was determined to be limited by Li-ion diffusion in the pure LCO electrode (i.e. no conductive additive) as opposed to the SE conductivity.

Ageing effects have been examined by comparing the EIS of pristine cells and those stored for 60 hours at 60 ° C. Larfaillou et al. [73] found that the typical ECM with 3 serial RQ units was only suitable initially and that the aged cells required the inclusion of a fourth RQ unit, ascribed to degradation of the Li j LiPON interface and/or in the LCO bulk. Temperature-dependent measurements of a Pt j LiPON j Pt cell were used to extract ionic conductivity and dielectric constant - these were invariant, highlighting the excellent thermal stability of LiPON. Unlike bulk ASBs with a LMA, applied pressure is not required during operation for stable plating and stripping of Li at appreciable rates. This is likely due to the high quality of SE interfaces produced by vacuum deposition and the low amount of Li transported per cycle (on the order of 1 μ m thickness) [74] in the thin-film configuration. Large-format batteries with capacities greater than mAh will make use of thick Li anodes ( &gt; 10 μ m) and porous positive electrodes, but with these caveats, studies of thin-film ASBs have value for large-format ASB research.

## 4. Sulfide Electrolytes

The discovery of superionic sulfide Li-ion conductors has been a critical step towards large-format ASBs. At room temperature, these materials offer Li-ion conductivities that rival liquid electrolytes ( &gt; 10 GLYPH&lt;0&gt; 3 Scm GLYPH&lt;0&gt; 1 ) and are mechanically soft, meaning that cold-pressing is sufficient to produce dense compacts. However, they have narrow electrochemical stability windows [75-78] and are moisture-sensitive, so handling must be performed in a dry environment (typically under inert gas in academic laboratories). The most studied compounds are those based on crystalline Li 10 GeP2S12 (LGPS), [4,79] Li 6PS5X (X = halide) [80] and Li2 S-P 2 S5 (LPS) bulk glasses. [81] EIS is commonly used to evaluate bulk ionic transport properties (using Equations 6 and 7), interfacial stability and degradation in full cells.

In 2011, Kamaya et al. [79] discovered LGPS, which at the time had the highest room temperature ionic conductivity of 12 mScm GLYPH&lt;0&gt; 1 . This was determined on a polycrystalline coldpressed pellet using ion-blocking electrodes (Au) in a 2-probe arrangement from GLYPH&lt;0&gt; 110 to 110 ° C (Figure 7). Their experiments were repeated 2 or 3 times to ensure the reproducibility and stability of their set-up. However, it is noted that these EIS measurements were taken with large perturbation voltages of

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

Figure 7. Impedance plots of the conductivity data from lower (upper insert) to higher (lower insert) temperatures and Arrhenius conductivity plots of LGPS. The plotted total conductivity represents the sum of the bulk and grain boundary contributions. Reprinted from Ref. [79] with permission. Copyright (2011) Springer Nature.

100 to 500 mV, which may enter the non-linear regime and data were not explicitly checked using K GLYPH&lt;0&gt; K tests.

The spectra for LGPS in Figure 7 consist of a single semicircle with a sharply rising 'tail' at low frequency which can be modelled by the equivalent circuit in Figure 2a, but with the capacitors replaced with CPEs: R0 (RQ) 1 Q2. The ( RQ ) 1 unit models the bulk ionic behaviour where the resistance consists of two contributions : the bulk resistance within the grains of the polycrystalline SE, Rb and the grain boundary resistance, Rgb . In the sulfides and other soft materials, Rb and Rgb can be difficult to resolve as they overlap strongly, both scale with the geometry of the sample and only limited EIS data may be available in typical frequency ranges (see lower inset in Figure 7).

Bron et al. [82] measured several sulfide SEs as a function of temperature, where Rgb could be identified in some systems at low temperatures (Figure 8). In these cases, the ECM was altered by adding a second ( RQ ) gb unit to account for this additional resistance contribution. Once identified, Rgb could be tracked through to room temperature and used to validate values of the bulk ionic conductivity. Applied pressure during fabrication and operation is also important for electrolyte and device properties. Kodama et al. [83] conducted in-situ X-ray tomography of symmetric cells under applied pressure in order to identify optimal processing conditions. The ionic conductivity of Li 6 PS5 X, (X = Cl, Br) and LPS glass pellets appeared to level off at ~120 MPa (the maximum pressure applied) at room temperature, though we note that the ionic conductivity of Li 6 PS5 Cl has been observed to continually increase up to pressures of ~400 MPa. [84]

The exceptionally high ionic conductivities and favourable processing properties of the sulfides also pose issues in their characterization. In a round-robin test of five commonly used compounds, Ohno et al. [85] found that the relative median error on higher conductivity materials ( &gt; 1 mScm GLYPH&lt;0&gt; 1 ) was 22% com-

Figure 8. a-e) Five sulfide SEs impedance plots showing that some exhibit grain/bulk (red) and grain boundary (pink) contributions while some only exhibit contribution from the bulk solid electrolyte (grain only) at low temperatures. The red and pink colours relate to the grain and grain boundary contributions as seen in the Nyquist plot and fitted using the equivalent circuit model. The electrode polarization is modelled by a single CPE. Reprinted from Ref. [82] with permission. Copyright (2016) Elsevier.

pared with ~10% for those under 1 mScm GLYPH&lt;0&gt; 1 . They concluded that some of this discrepancy may arise from the fitting of limited EIS data and microstructural relaxation. The cell set-up, such as the contacting electrodes and sample dimensions, can influence the EIS spectra and must be fully reported. They also recommended the acquisition of data in triplicate and validation of σ ion values &gt; 1 mScm GLYPH&lt;0&gt; 1 with external collaborators.

Sulfides have narrow electrochemical stability windows [75] and will be reduced by metallic Li on contact and/or during plating/stripping. Analogous to the SEI layer in LiBs, the impedance associated with this interphase should be low and stable and can be studied using symmetric Li j SE j Li setups. Time-resolved EIS can be used to assess stability, with an undesirable MIEC interphase identified by the continuous increase of interfacial impedance with time. [86,87] Whiteley et al. [88] modelled the EIS of a symmetric cell containing a Li 10 SiP 2 S12 (LiSiPS) electrolyte by using Rb element in series with two RQ units, for the interphase and charge transfer impedance respectively, and finally a Warburg element for diffusion through the reversible electrodes. LiSiPS was shown to produce a more stable interphase with lower resistance than LGPS over 250 hrs. Kasier et al. analysed composite electrodes comprised of lithium titanate and a Li 7 P2 S8 I SE at various volume fractions. [57] The effective ionic tortuosities and conductivities were determined using both a TLM and electronic-blocking symmetric cells, and a SE σ ion &gt; 5 mScm GLYPH&lt;0&gt; 1 was estimated to provide comparable (or even superior) power densities to Li-ion cells with a liquid electrolyte.

Sulfide SEs are also often unstable at the oxidizing potentials of positive electrode materials. Ohta et al. [89] systematically showed this using LiNbO 3 buffer layers coated onto LCO powder, which resulted in a stable interface against LGPS. Even when stability is achieved, large interfacial impedances can be generated by resistive interphases or space charge layers. [90-92] These can be mitigated by the addition of coatings, binders or

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

nanocomposites to the cathode or soft inorganic electrolyte mixed with the cathode powder. [93-95]

With some exceptions, the generic ECM for a full cell ASB with a LMA consists of (from high to low frequency): ( RQ ) b ( RQ ) gb-( RQ ) anode ( RQ ) cathode and a CPE or Warburg element for diffusion processes into the electrodes. [85,96,97] The final CPE can be used instead of the Warburg element in cases where non-ideal diffusion and more capacitive behaviour is seen. [97] As in LiB research, the SoC-dependent impedance is important to fully understand battery behaviour during operation. Figure 9 shows the evolution of a In j LGPS j LCO cell during charge and discharge, [97] with 3 distinct processes identified in high, mid and low frequency ranges (Figure 9a). Upon charging, the In anode interface resistance (low frequency) was largely unchanged, but the cathode interface resistance (mid frequency) increased. This is the opposite assignment of the anode and cathode interfacial impedances observed in full cells with an

Figure 9. Stacked Nyquist plots of a In j LGPS j LCO cell with LiNb 0.5 Ta0.5O3 (LNTO)-coated LCO as the active material. a) ECM and EIS during b) charge and c) discharge at different SoC points. The low-frequency semicircle is assigned to the anode interface resistance with the electrolyte, while the mid-frequency semicircle is assigned to the cathode interface resistance. Reprinted from Ref. [97] with permission. Copyright (2017) American Chemical Society.

LMA (with respect to frequency) and highlights the need for thorough EIS studies on a system-by-system basis. This trend on charging was attributed to loss of interfacial contact in the composite cathode due to volumetric expansion and the formation of a decomposition layer on exposed LCO. At higher SoCs, a more noticeable Warburg impedance began to appear which was assigned to the diffusion of Li-ions in the cathode material. However, during discharge the anode interface resistance increases becoming greatest at the end of discharge (Figure 9c). This increase in interfacial resistance at the In j SE interface was ascribed to the degree of lithiation of the In GLYPH&lt;0&gt; Li alloy anode, which becomes more In-rich during discharge.

Literature reports of detailed EIS on all-solid-state Li GLYPH&lt;0&gt; S full cells are limited. [98-103] Generally, Rb is observed at highfrequency, a combination of anode and cathode impedances is seen at mid-frequency and lowest frequency attributed to charge transfer resistance of combined anode and cathode contributions. Wang et al. [103] reasoned that the sulfur-composite cathode impedance was the limiting factor by comparison with previous data on Li symmetric cells with the same SE, and analysed the composite cathode using a transmission line model.

Other classes of mechanically-soft inorganic SEs have been discovered, such as phosphides [29,104,105] and halides. [106-109] Approaches to EIS measurement and ECM modelling are very similar to the sulfides, e.g. cold-pressing of dense compacts and strongly overlapping bulk and grain boundary impedances at room temperature. Interestingly, a recently reported halide SE, Li 2 Sc2/3 Cl 4 [110] does not require oxide-coating of cathode materials due to the greater electrochemical stability of this material class.

## 5. Oxide Electrolytes

Oxide-based SEs have also been extensively investigated. These tend to be less sensitive to air and moisture and have larger electrochemical stability windows compared to sulfide SEs, but exhibit only moderate ionic conductivities (10 GLYPH&lt;0&gt; 4 -10 GLYPH&lt;0&gt; 3 Scm GLYPH&lt;0&gt; 1 at room temperature), are mechanically brittle and processed at high temperatures. These latter characteristics make full cell fabrication difficult due to the necessity of large-area, dense, thin ( &lt; 50 μ m) SE layers and intimate solid-solid contact in electrode-SE composites. The most-studied oxide SEs can be grouped into three crystalline classes: [111] perovskite-type, [112] NASICON-type [113] and garnet-type. [114] We will primarily discuss EIS of the garnet-type, namely Li 7 La3 Zr 2 O12 (LLZO) -whose good ionic transport and stability against Li metal have pushed this class to the forefront of the field. The cubic phase of LLZO was first reported in 2007 with a room temperature conductivity of 10 GLYPH&lt;0&gt; 4 Scm GLYPH&lt;0&gt; 1 . [115] Further work showed that undoped LLZO adopts a tetragonal crystal structure at ambient conditions with much lower Li-ion conductivity (~10 GLYPH&lt;0&gt; 6 Scm GLYPH&lt;0&gt; 1 ) [114] and that unintentional Al 3 + -doping, introduced through solid-state synthesis at &gt; 1000 ° C in alumina crucibles, could stabilize the high-temperature, ion-conducting cubic phase. [116] Such aliovalent doping strategies are common in inorganic SEs to

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

introduce and charge-balance bulk defects favourable to ionic conduction, e.g. Li vacancies or interstitials. [117,118] Traditionally, EIS studies relevant to oxide SEs focused on new synthesis routes or to methods to increase the ionic conductivity, however recent work has investigated its fascinating interfacial properties with Li and several oxide-based devices have been reported.

Murugan et al. measured ceramic pellets with ion-blocking Au electrodes in a two-probe configuration which showed an evident grain boundary impedance, even at room temperature (Figure 10a). [115] As it is the total conductivity (bulk and grain boundary) that is important in devices, much research has been dedicated to reducing this grain boundary contribution through optimization of sintering conditions or techniques such as hotpressing (Figure 10b). [119] There is a complex relationship between doping and microstructure, as dopants may not be homogenously distributed in the bulk, but segregated at grain boundaries. [120] Additionally, single-crystalline samples allow detailed impedance investigations without the influence of grain boundaries. [121,122]

Figure 10. a) Impedance plot of Li 7 La3 Zr 2 O12 measured in air at 18.8 ° C for the thick pellet (1.02 cm in thickness). The solid line represents simulated data. The impedance plot measured in air at 18.8 ° C for the thin pellet (0.18 cm in thickness) is shown in the inset. Reproduced from Ref. [115] with permission. Copyright (2007) Wiley-VCH. b) Hot-pressing to control grain boundary effects in LLZO. Republished with permission from Ref. [119] Copyright (2015) The American Ceramic Society.

The large impedance commonly observed at the Li j LLZO interface can be ameliorated using interfacial layers [123] and by the removal of Li2CO3, which forms on the surface of LLZO in ambient conditions. [124] Recently, Krauskopf and co-workers used a Li j LLZO j Li symmetric cell to analyse the influence of applied pressure on the Li j LLZO interface. [28] They showed that, with careful surface preparation and handling under inert gas to avoid Li2CO3 formation, sufficient applied pressure reduced the interfacial impedance to a negligible value ( &lt; 1 Ω cm 2 ), which remained after the pressure was removed (Figure 11a). Further, this Li electrode with low overpotential served as a reference electrode to separate impedance contributions during operando GEIS of Li plating and stripping (Figure 11b and c). Further work by this team used this quasi-3-electrode set-up and GEIS to monitor impedance changes when stripping/ plating Li on copper and Au electrodes, observing a lowfrequency feature not seen in symmetric cell experiments and providing evidence for Li deposition within LLZO that leads to so-called 'soft' short-circuits'. As these precede 'hard' short-

Figure 11. a) Pressure-dependent Nyquist plots of Li j LLZO j Li cells showing the large impact of external force on the interfacial resistance R int. Operando EIS spectrum for lithium metal b) stripping and c) plating. Reprinted from Ref. [28] with permission. Copyright (2019) American Chemical Society.

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

circuits (where the voltage drops to zero), this configuration could be used to monitor Li dendrite formation. A Rleak element was introduced in the ECM to account for the increase in partial electronic conductivity that occurred. As dendrites grew in the SE, the resistance of Rleak and Rb decreased until a hard shortcircuit occurred. By monitoring Rleak , Rb and Rgb while cycling, the absence of a soft short-circuit was indicated by stable resistances for Rb and Rgb . [28] Interfacial modification can be helpful at the cathode j LLZO interface as well; for example, a Nb-containing interlayer resulted in significantly reduced interfacial resistance in a LCO j LLZO j Li battery. [125]

The high-temperature processing requirements and stiffness of oxide SEs means that composite cathodes, and hence oxide ASBs, are difficult to fabricate and cycle. Thus, full cell EIS studies based on LLZO tend to use either vacuum-deposited thin-film cathodes [125,126] or composites containing a Li salt. [37,127,128] Systematic work by Ohta et al., measured LCO j LLZO j Li (LCO was deposited by pulsed laser deposition) and Li symmetric cells (Figure 12) to assign their EIS features. [126] By comparison, it was concluded that the SE impedance dominated at high frequency, followed by the Li j SE interface, leaving the low-frequency contribution to be attributed to the charge transfer resistance experienced at the LCO interface. A similar approach and assignments were made for the three semicircles observed in

Figure 12. a) Nyquist plot for the LiCoO 2 j Li 6.75 La3 Zr 1.75 Nb0.25 O12 j Li cell at 3.95 V. b) Nyquist plot for the Li j Li 6.75 La3 Zr 1.75 Nb0.25 O12 j Li cell. Reprinted from Ref. [126] with permission. Copyright (2012) Elsevier.

Nyquist plots of LCO j LLZO j Li full cells using a Li GLYPH&lt;0&gt; C GLYPH&lt;0&gt; B GLYPH&lt;0&gt; O salt mixture in the composite positive electrode. [37] Beyond intercalation electrodes, solid-state Li GLYPH&lt;0&gt; S and Li-air batteries have been constructed with an LLZO SE (cf Table 3 in Ref. [129]). However, studies that systematically assign EIS features in these systems are lacking and future work interrogating the impedances in these ASBs will be of great interest.

## 6. Polymer-Based Electrolytes

In the 1970's, Wright et al. discovered Li-ion conducting polymers by dissolving simple alkali salts (NaI, NaSCN, etc.) in semicrystalline polymers like poly(ethylene) oxide (PEO). [130-132] Since this finding, there has been significant interest in employing these materials in ASBs, initiated by Armand et al. [133-136] However, these original conducting polymers were shown to have low ionic conductivity at room temperature and so were only employed in high-temperature applications. [137,138] Though there are now several polymer-based electrolytes that exhibit appreciable ionic conductivity, none have a practical value ( &gt; 5 mScm GLYPH&lt;0&gt; 1 ) at room temperature. [139] This remains the biggest factor preventing their application, alongside their instability against Li metal and 4Vclass cathode materials. [140,141] However, their facile processing and low cost are compelling and motivate continuing research.

Polymer-based electrolytes can be divided up into four subcategories: (1) solid-polymer electrolytes (SPE); (2) plasticized polymer electrolytes (PPE); (3) composite solid-polymer electrolytes (CSPE) and (4) gel-polymer electrolytes (GPE). In the case of GPEs these materials incorporate a liquid electrolyte into the polymer matrix and therefore, are beyond the scope of this review. The most standard form of ion-conducting polymer electrolytes are the SPEs that continue the design strategy outlined by Wright and co-workers. [130,131] On dissolution of the salt Li-ions coulombically coordinate to the oxygen sites on the polymer backbone. When an electric field is applied to the material the Li-ions can migrate between weakly coordinated sites and hence, become ionically conducting. To improve the ionic conductivity of these polymer electrolytes, researchers began to investigate PPEs, which incorporate a low molecular weight compound into the polymer matrix. Common plasticizers can be salts, solvents or low molecular weight polymers such as ethylene carbonate (EC), propylene carbonate (PC) or polyethylene glycol (PEG), respectively. [142-144] These compounds lower the intermolecular and intramolecular forces between the polymer chains, increasing the number of amorphous regions. It is well established that for polymer-based electrolytes the ionic conductivity is closely related to the degree of crystallinity of the matrix. [145,146]

Lastly, the CSPEs contain either inert ceramic fillers that have high dielectric constants, e. g. SiO2 , Al 2O3 and TiO2 , or active Li-ion conducting SEs like LLZO or LGPS. [147-151] The dielectric fillers decrease the amount of ion-ion association inherent in the polymer matrix, thereby increasing the availability of Li-ions. They also increase the mechanical strength. On the other hand, the inorganic SEs can facilitate ion migration but are generally limited by their poor interfacial contact and

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

stability. [152,153] By incorporating these materials into a polymer matrix, a high ionic conductivity can be maintained through the solid, while the polymer provides a more stable interface with the electrodes.

One of the most significant factors that can affect the conductivity reported for polymer-based electrolytes is the temperature at which the measurement is made. This is due to the semi-crystalline nature of polymers that are used, which exhibit a defined glass transition temperature ( T g) and melting temperature ( T m). [154] The T g is defined as the temperature at or above which the amorphous structure exhibits macromolecular mobility, changing the physical appearance from a glass-like state to a rubber-like state, while the T m is a specific property of the crystalline regions, above which they experience a phase change to an amorphous state. [155] Therefore, the T m is the property that significantly affects the ionic conductivity of the polymers as the number of amorphous domains are increased. This effect is largely misrepresented in the literature as heating above the T g . Due to the ionic conductivity being closely related to the concentration of amorphous regions it is therefore expected that the ionic conductivity will significantly increase, on heating. Aziz et al. used temperature-dependent EIS to observe and track the phase change between crystalline to amorphous that occur in SPEs. [156] Using a SS blocking electrode configuration when the SPE is heated towards ~60 ° C ( T m for PEO) the impedance assigned to the phase boundaries was gradually lost from the Nyquist plot. Above 60 ° C the phase impedance was completely lost leaving only the bulk resistance of the polymer electrolyte. The bulk impedance showed a significant decrease in size, leading to an increase in ionic conductivity. This phenomenon helps to explain why current polymer-based electrolytes are only applied to high-temperature applications.

There are a number of studies that use EIS to probe stability against Li metal, an important requirement for a practical polymer-based electrolyte. [157-159] By placing the new SE between two Li metal electrodes and collecting EIS data as a function of time, any instability can be tracked by the increases in impedance. Zhao et al. have shown that monitoring the evolution of an interfacial resistance between their PPE and Li metal over a 24-hour period can be accomplished using EIS (Figure 13). [160] For the PEO/LiTFSI system, a &lt; 5% increase in impedance was observed (Figure 13b). However, for the hydrogenated nitrile butadiene rubber (HNBR)-based electrolytes a significant increase in interfacial resistance can be seen (Figure 13c and d). This was an indication that an unstable interface had been formed between the Li and the PPE. Since the standard SPE showed a relatively stable impedance, the increase observed for the PPE were assigned to side reactions of the HNBR plasticizer. [160]

After investigating the conductivity and electrochemical stability of the new materials some researchers have begun full cell testing. This can give a more realistic representation of how the electrolyte will behave with the anode and cathode in a working battery. He et al. have shown full cell impedance for their lithium bis(oxalate)borate (LiBOB)-modified polymer electrolyte membrane (PEM) against its standard PEM counterpart

Figure 13. a) Equivalent circuit used to model impedance of Li metal symmetric cells at 70 ° C with impedance evolution over 24 h with b) PEO/ LiTFSI c) non-plasticized HNBR/LiTFSI and d) HNBR/LiTFSI/20% DEP electrolytes. Reprinted from Ref. [160] with permission. Copyright (2019) American Chemical Society.

(Figure 14). [161] The impedance of assembled cells comprising of a LiFePO4 (LFP) cathode and a LMA were measured after 50 cycles for each polymer electrolyte.

From the EIS data they were able to show that on increasing the cell cycling temperature from 20 to 60 ° C the interfacial charge transfer resistance increased. In the case of the unmodified-PEM cell, the resistance increased from 600 to 4,000 Ω . This implied that during high-temperature operation the interfacial layers were altered either at the LFP j PEM or Li j PEM interfaces. However, the modified LiBOB-PEM was shown to be relatively more stable to the temperature change in comparison. This indicated that the LiBOB additive suppressed the adverse reaction that occurred at high temperatures in the unmodified-PEM. To further investigate at which interface (LFP j PEM or Li j PEM) this change occurred, symmetric cells of LFP j PEM j LFP and Li j PEM j Li were studied. By collecting EIS data under the same conditions as the full cells, they observed that the LFP j PEM j LFP cell remained relatively stable at both temperatures, while the Li j PEM j Li cells were shown to have a

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

Figure 14. Complex plane impedance plot showing LFP j PEM j Li cells after being cycled for 50 times at 20 ° C (solid square) and 60 ° C (open square) and LFP j m-PEM j Li cells after being cycled for 50 times at 20 ° C (solid circle) and 60 ° C (open circle). Note that the m-PEM contains 0.4 wt% of LiBOB concentration. Reprinted from Ref. [161] with permission. Copyright (2017) Elsevier.

significant change in impedance at 60 ° C due to a chemical reaction occurring at elevated temperature. Comparing this to the Li j LiBOB-PEM j Li cells the change in impedance was significantly decreased, showing that the addition of LiBOB was effective at stabilizing the Li j PEM interface. [161]

Although ASBs utilizing a SPE have been commercialized since 2013 by the Bolloré Group, there is a lack of full cell EIS data on these particular cells. They are reported to contain a LFP cathode with a LMA, separated by a Li-containing PEO-based electrolyte, and due to the low ionic conductivity of the polymer SE the battery must be operated in a temperature range of 7080 ° C to provide 100 Whkg GLYPH&lt;0&gt; 1 . [162] A more detailed electrochemical understanding of these systems could provide the fundamental insights required to improve SPEs, whether this be to their conductivity, interfacial stability with electrode materials or to inform future physical models of ASBs. In addition, these improvements could aid in the development of all-solid-state Li GLYPH&lt;0&gt; S and Li-air technologies that harness SPEs. Despite the fact that there are examples of SPEs being employed in these systems, [163,164] there are limited reports of full cell EIS. [165-168] In agreement with Section 4, Li GLYPH&lt;0&gt; S cells with a SPE have a highfrequency impedance contribution from the electrolyte, followed by the anode and lastly the cathode impedance. [169] However, impedance contributions for solid-state Li-air batteries are yet to be identified in the literature.

## 7. Emerging EIS-related Techniques for Li-ion Batteries

LiBs have been commercially available for over 25 years. As such, their EIS measurement and modelling approaches are advanced compared to ASBs. We have identified several emerging EISrelated techniques reported for LiBs which will be applicable to future ASB research also.

A considerable limitation of EIS is the ambiguity of equivalent circuit modelling and interpretation. As discussed in Section 2.3, DRT analysis can aid in robust ECM design by identifying the characteristic time constants of the system, but is limited to resistive-capacitive elements, requires data pre-processing and care must be taken when choosing regularization methods for data inversion. [170] A recent study by Danzer addresses the first two issues with the development of 'generalized' DRT analysis, incorporating resistive-inductive circuit elements and eliminating data pre-processing. [171] Huang et al. have reported a promising approach to improve the accuracy of initial data inversion based on Bayesian statistics and a pre-calibration parameter tuning step. [172] By improving the robustness of DRT analysis, these are steps towards automated batch processing of the large, multidimensional EIS datasets inherent to in-situ and operando experiments. A single-step DRT analysis of such 2D data ( Z vs. temperature, SoC, etc.) has been demonstrated to improve the signal-to-noise ratio and thus, data resolution compared to 1D. [173]

Beyond equivalent circuit modelling, machine learning (ML) can use large EIS datasets taken over wide parameter space to understand degradation [174] and predict parameters such as SoC and state-of-health [175] in LiBs. The current database of EIS measurements for ASBs is not nearly as large, but is poised to grow, and knowledge gained from applying ML will likely complement chemical and physical insights from the other techniques discussed here. A considerable challenge of ML is its inherent black-box nature, which makes it difficult to generalize the derived models or quantify their robustness. As such, these models could perform well for the majority of the time but occasionally, and unpredictably, give incorrect results. Highthroughput experimentation (and possibly fabrication) [175] techniques will be needed to generate sufficiently large datasets in a timely fashion. Ultimately, ML-based models could be used to track and learn the behaviour of battery systems under different conditions (temperature, SoC, etc.), and then be used as an assurance algorithm to see if a specific cell type is behaving as expected, with significant deviations from predicted behaviour indicating damage to the cell or internal shorts.

Conventional EIS must adhere to the criterion of stability (Section 2). Strictly speaking, this rules out measurements during the passage of current and thus, typical measurement conditions are far removed from battery operation. In-situ and operando EIS takes place as the system is slowly changed, such that quasi-steady-state conditions (QSS) are achieved, and the acquisition of impedance spectra during charge or discharge is possible. This has been applied to continuous [176,177] and pulsed charge/discharge of LiBs. [178] Itagaki et al. used a Li RE to

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

deconvolute cathode and anode contributions during in-situ EIS and were thus able to track a low-frequency inductance process associated with the graphite anode. [177] However, a study using pulsed charge/discharge conditions on a similar cell set-up, concluded that this inductance feature was measurement artefact, due to the violation of the QSS condition at low frequencies. [178] Clearly, the low-frequency cut-off must be carefully considered relative to the rate of change of the system, this may be quantified using K GLYPH&lt;0&gt; K relations or DRT transforms [179,180] as data quality criteria. To the best of our knowledge, dynamic/operando EIS has not yet been reported for a full cell ASB, but recent operando GEIS on symmetric [28] and asymmetric [181] solid-state cells with an LLZO SE during Li stripping and plating revealed signatures of internal Li plating within the SE and differences in symmetric and asymmetric cell behaviour (Section 5).

Linearity is also a requirement of conventional EIS. However, many processes in batteries are non-linear, e.g. electrochemical reactions. [182] Non-linear EIS (NLEIS) increases the magnitude of the perturbation voltage or current such that linearity is not ensured, and higher harmonics can be analysed. In LiBs this has been used to probe subtle degradation processes [183] and detect undesirable Li plating during operation [184] in commercial cells. Similarly, NLEIS may be useful for probing non-linear processes within ASBs, such as space charge layers at electrode j SE solidsolid interfaces, whose significance on ASB operation is hotly debated. [90-92,185,186] To the best of our knowledge, no NLEIS measurements have been reported on ASBs. With the qualification that the data analysis is significantly more complex than for conventional EIS, [187] future NLEIS studies on ASBs are warranted.

## 8. Summary and Outlook

ASBs promise greater energy density as well as improved safety compared to conventional LiBs. The recent discoveries of Li superionic conductors have boosted their prospects enormously; however, many challenges remain that must be addressed to realize large-format cells. EIS is a powerful tool to interrogate the charge transport properties, stability and performance of these materials and devices by non-destructive means.

We began this review with relevant EIS theory for ASBs followed by electrode/cell configurations for electrochemical measurements and modelling strategies for the impedance spectra. While ECMs are often lacking in physical justification, they can be applied quickly without detailed system knowledge. Further, complementary cells, experiments investigating temperature, pressure and SoC effects and techniques such as DRT analysis can be leveraged to more robustly construct ECMs. In Sections 3 through 6 we reviewed EIS approaches to ASBs organized by SE chemistry, beginning with the most mature: LiPON. While this SE pertains only to thin-film solid-state devices, the approaches used -namely the comparison of symmetrical cells (using blocking and reversible electrodes) to full cells, and the use of physical models parameterized by

equivalent circuit modelling informed by DRT analysis -are highly relevant to high-capacity ASBs with porous cathodes. Next, sulfide SEs were discussed. Their high ionic conductivity and ability to be processed at room temperature via coldpressing have led to advanced device-level studies. However, reproducibility can be challenging due to their mechanically soft nature, in addition to the convolution of bulk and grain boundary contributions at room temperature. Additionally, reactivity with electrode materials necessitates the use of protective coatings or interlayers. With suitable surface preparation, oxide SEs have exhibited negligible interfacial impedance against Li, which can then function as a quasi-RE for sophisticated operando studies. Polymer-based SEs are inherently attractive for manufacturing at scale but currently suffer from low ionic conductivity and interfacial instability. As ECMs are widely applied at all device levels and across all SE types, it is worthwhile to summarize these findings in detail.

Although ASB fabrication can be very different depending on SE chemistry, ECM feature assignment appears broadly similar to LiBs based on the handful of relevant device studies performed. [62,70,97,126,188] That is, several RQ units in series are used, where the high-frequency arc characterizes the electrolyte (which may include a microstructural contribution for SEs), followed by interfacial losses and finally diffusion modelled by CPE or Warburg elements. As in LiBs, it is hard to be prescriptive in the mid-to-low frequency range as the characteristic frequencies of the electrode interfaces overlap, [189] but these details have both great fundamental and applied value. From our review, full devices using a LMA and an intercalation cathode typically assign the SE j cathode interface as the lowest frequency arc, while those utilising an In GLYPH&lt;0&gt; Li anode assign this to the SE j anode interface. Detailed EIS studies on all-solid-state Li GLYPH&lt;0&gt; S and Li-air batteries are lacking at present and further device-level research will be required to elucidate any general spectral assignment strategies.

Finally, we identified several state-of-the-art EIS techniques employed in LiB research that will have utility in future ASB studies. We conclude with 4 directions that will enable highperformance ASBs and packs:

1. Standardized reporting of experimental processing and measurement conditions to move beyond bespoke test rigs. New SEs with high σ ion ( &gt; 5 mScm GLYPH&lt;0&gt; 1 ) are needed for use in composite cathodes where the effective σ ion is lower. [57,190] Measurement accuracy is known to be reduced in this range for sulfide SEs, [191] so four-point measurements, as well as ion-selective electrodes, may be valuable. Additionally, suitable RE materials and 3-electrode cell designs are needed to interrogate individual cell components in the solid-state.
2. Further development and consistent adoption of DRT analysis, in addition to multi-variable (temperature, pressure and SoC) testing for equivalent circuit modelling. The determination of characteristic frequencies is valuable for feature assignment and comparison between different devices and studies. It is worth noting that characteristic frequencies of the SE and interfaces are significantly higher for ASBs than for LiBs ( &gt; 1 kHz vs. &lt; 1 kHz), hinting that useful EIS data can be rapidly acquired in real-time during

Dpm)GCpmG7DpCpm7Dmm7DFownloadedDfromDhttpswTTchemistry©europe2onlinelibrary2wiley2comTdoiTmC2mCCpTcelc2pCpmCCmCIDbyDéeadcubeD3;abtivaDYnc207DèileyDžnlineD;ibraryDonD&amp;mITCmTpCpW]2DQeeDtheDüermsDandD'onditionsD3httpswTTonlinelibrary2wiley2comTterms©and©conditions0DonDèileyDžnlineD;ibraryDforDrules

- battery and pack operation. However, whether this highfrequency range is accessible in large-format ASBs operating with increased inductance contributions remains to be seen.
3. Physical models for ASBs. Once validated for a given system, physical models can be extremely useful in predicting cell behaviour under different cycling conditions, thereby saving time and cost compared with experimental testing alone. Physical modelling of bulk ASBs with porous cathodes is in its early stages but, when combined with experiment as for thin-film batteries, [60-62] is likely to yield important fundamental understanding of these systems. Where cell information (chemistry, physical dimensions, etc.) is limited or proprietary, hybrid approaches using ECMs with improved physical justification or machine learning-based modelling may be optimal.
4. Advanced EIS methods such as in-situ/operando EIS and NLEIS can give valuable information on the Li dendrites that plague ASBs, as well as subtle ageing processes. Further studies using and expanding these techniques will aid material and device development.

ASB research progress has been rapid in the last 10 years across SE discovery, interfacial modification and laboratory-scale device fabrication. However, current state-of-the-art cells fall short of the commercial benchmarks set by Li-ion. [188] Sustained research effort on the fundamental and applied aspects of ASBs, in which EIS will play a vital role, is needed to translate the promise of ASBs out of the laboratory and into real-world applications. Given the current steep trajectory of ASBs, the outlook is optimistic.

## Acknowledgements

We gratefully acknowledge The Faraday Institution LiSTAR programme (FIRG014, EP/S003053/1) for funding and UCL for start-up funds. M.J.J. acknowledges HORIBA-MIRA, UCL and EPSRC (EP/R513143/1) for a CASE studentship.

## Conflict of Interest

The authors declare no conflict of interest.

Keywords: All-Solid-State Batteries · Electrochemical Impedance Spectroscopy · Energy Storage · Modelling · SolidState Electrolytes

- [1] T. Famprikis, P. Canepa, J. A. Dawson, M. S. Islam, C. Masquelier, Nat. Mater. 2019 , 18 , 1278-1291.
- [2] M. Pasta, D. Armstrong, Z. L. Brown, J. Bu, M. R. Castell, P. Chen, A. Cocks, S. A. Corr, E. J. Cussen, E. Darnbrough, V. Deshpande, C. Doerrer, M. S. Dyer, H. El-Shinawi, N. Fleck, P. Grant, G. L. Gregory, C. Grovenor, L. J. Hardwick, J. T. S. Irvine, H. J. Lee, G. Li, E. Liberti, I. McClelland, C. Monroe, P. D. Nellist, P. R. Shearing, E. Shoko, W. Song, D. S. Jolly, C. I. Thomas, S. J. Turrell, M. Vestli, C. K. Williams, Y. Zhou, P. G. Bruce, J. Phys. Energy 2020 , 2 , 032008.
- [3] J. Janek, W. G. Zeier, Nat. Energy 2016 , 1 , 1-4.
- [4] Y. Kato, S. Hori, T. Saito, K. Suzuki, M. Hirayama, A. Mitsui, M. Yonemura, H. Iba, R. Kanno, Nat. Energy 2016 , 1 , 1-7.

[5]

D. Cao, X. Sun, Q. Li, A. Natan, P. Xiang, H. Zhu,

Matter

2020

,

3

, 57-94.

- [6] T. Krauskopf, F. H. Richter, W. G. Zeier, J. Janek, Chem. Rev. 2020 , 120 , 7745-7794.
- [7] Y. G. Lee, S. Fujiki, C. Jung, N. Suzuki, N. Yashiro, R. Omoda, D. S. Ko, T. Shiratsuchi, T. Sugimoto, S. Ryu, J. H. Ku, T. Watanabe, Y. Park, Y. Aihara, D. Im, I. T. Han, Nat. Energy 2020 , 5 , 299-308.
- [8] A. Manthiram, X. Yu, S. Wang, Nat. Rev. Mater. 2017 , 2 , 1-16.
- [9] J. R. Nair, L. Imholt, G. Brunklaus, M. Winter, Electrochem. Soc. Interface 2019 , 28 , 55-61.
- [10] S. Ohno, A. Banik, G. F. Dewald, M. A. Kraft, T. Krauskopf, N. Minafra, P. Till, M. Weiss, W. G. Zeier, Prog. Energy 2020 , 2 , 22001.
- [11] M. E. Orazem, P. Agarwal, A. N. Jansen, P. T. Wojcik, L. H. Garcia-Rubio, Electrochim. Acta 1993 , 38 , 1903-1911.
- [12] A. Lasia, Electrochemical Impedance Spectroscopy and Its Applications , Springer, New York, NY, 2014 .
- [13] E. von Hauff, J. Phys. Chem. C 2019 , 123 , 11329-11346.
- [14] E. Barsoukov, J. R. Macdonald, WILEY-INTERSCIENCE 2005 .
- [15] I. V. Krasnikova, M. A. Pogosova, A. O. Sanin, K. J. Stevenson, Chem. Mater. 2020 , 32 , 2232-2241.
- [16] H. Bouwmeester, P. Gellings, J. Schoonman, I. Riess, Electrodics , CRC Press, 1997 .
- [17] M. Falco, S. Ferrari, G. B. Appetecchi, C. Gerbaldi, Mol. Syst. Des. Eng. 2019 , 4 , 850-871.
- [18] R. Raccichini, M. Amores, G. Hinds, Batteries 2019 , 5 , 1-24.
- [19] K. B. Hatzell, X. C. Chen, C. L. Cobb, N. P. Dasgupta, M. B. Dixit, L. E. Marbella, M. T. McDowell, P. P. Mukherjee, A. Verma, V. Viswanathan, A. S. Westover, W. G. Zeier, ACS Energy Lett. 2020 , 5 , 922-934.
- [20] R. A. Huggins, Ionics 2002 , 8 , 300-313.
- [21] A. Kezionis, P. Butvilas, T. Salkus, S. Kazlauskas, D. Petrulionis, T. Zukauskas, E. Kazakevicius, A. F. Orliukas, Rev. Sci. Instrum. 2013 , 84 , 13902.
- [22] J. H. Kim, E. C. Shin, D. C. Cho, S. Kim, S. Lim, K. Yang, J. Beum, J. Kim, S. Yamaguchi, J. S. Lee, Solid State Ionics 2014 , 264 , 22-35.
- [23] Y. J. Nam, K. H. Park, D. Y. Oh, W. H. An, Y. S. Jung, J. Mater. Chem. A 2018 , 6 , 14867-14875.
- [24] A. L. Santhosha, L. Medenbach, J. R. Buchheim, P. Adelhelm, Batteries &amp; Supercaps 2019 , 2 , 524-529.
- [25] Y. Ren, Y. Shen, Y. Lin, C. W. Nan, Electrochem. Commun. 2015 , 57 , 2730.
- [26] Y. Gao, A. M. Nolan, P. Du, Y. Wu, C. Yang, Q. Chen, Y. Mo, S.-H. Bo, Chem. Rev. 2020 , 120 , 5954-6008.
- [27] S. Gantenbein, M. Weiss, E. Ivers-Tiffée, J. Power Sources 2018 , 379 , 317-327.
- [28] T. Krauskopf, H. Hartmann, W. G. Zeier, J. Janek, ACS Appl. Mater. Interfaces 2019 , 11 , 14463-14477.
- [29] S. Strangmüller, H. Eickhoff, D. Müller, W. Klein, G. Raudaschl-Sieber, H. Kirchhain, C. Sedlmeier, V. Baran, A. Senyshyn, V. L. Deringer, L. Van Wüllen, H. A. Gasteiger, T. F. Fässler, J. Am. Chem. Soc. 2019 , 141 , 14200-14209.
- [30] F. Han, A. S. Westover, J. Yue, X. Fan, F. Wang, M. Chi, D. N. Leonard, N. J. Dudney, H. Wang, C. Wang, Nat. Energy 2019 , 4 , 187-196.
- [31] M. H. Hebb, J. Chem. Phys. 1952 , 20 , 185.
- [32] C. Wagner, Zeitschrift für Elektrochemie, Berichte der Bunsengesellschaft für Phys. Chemie 1956 , 60 , 4-7.
- [33] I. Riess, Solid State Ionics 1996 , 91 , 221-232.
- [34] L. Le Van-Jodin, F. Ducroquet, F. Sabary, I. Chevalier, Solid State Ionics
30. 2013 , 253 , 151-156.
- [35] A. Nasar, M. Shamsuddin, Thermochim. Acta 1992 , 205 , 157-169.
- [36] Y. Su, J. Falgenhauer, A. Polity, T. Leichtweiß, A. Kronenberger, J. Obel, S. Zhou, D. Schlettwein, J. Janek, B. K. Meyer, Solid State Ionics 2015 , 282 , 63-69.
- [37] F. Han, J. Yue, C. Chen, N. Zhao, X. Fan, Z. Ma, T. Gao, F. Wang, X. Guo, C. Wang, Joule 2018 , 2 , 497-508.
- [38] K. A. Borup, J. De Boor, H. Wang, F. Drymiotis, F. Gascoin, X. Shi, L. Chen, M. I. Fedorov, E. Müller, B. B. Iversen, G. J. Snyder, Energy Environ. Sci. 2015 , 8 , 423-435.
- [39] A. J. E. Rettie, W. D. Chemelewski, D. Emin, C. B. Mullins, J. Phys. Chem. Lett. 2016 , 7 , 471-479.
- [40] M. R. Busche, M. Weiss, T. Leichtweiss, C. Fiedler, T. Drossel, M. Geiss, A. Kronenberger, D. A. Weber, J. Janek, Adv. Mater. Interfaces 2020 , 2000380.
- [41] B. A. Boukamp, Solid State Ionics 1993 , 62 , 131-141.
- [42] B. A. Boukamp, J. Electrochem. Soc. 1995 , 142 , 1885-1894.

- [43] M. Schonleber, 'Kramers-Kronig Validity Test Lin-KK for Impedance Spectra,' can be found under https://www.iam.kit.edu/et/index.php, 2015 .
- [44] U. Westerhoff, K. Kurbach, F. Lienesch, M. Kurrat, Energy Technol. 2016 , 4 , 1620-1630.
- [45] W. Choi, H. C. Shin, J. M. Kim, J. Y. Choi, W. S. Yoon, J. Electrochem. Sci. Technol. 2020 , 11 , 1-13.
- [46] W. H. Mulder, J. H. Sluyters, T. Pajkossy, L. Nylkos, J. Electroanal. Chem. 1990 , 285 .
- [47] J. B. Jorcin, M. E. Orazem, N. Pébère, B. Tribollet, Electrochim. Acta 2006 , 51 , 1473-1479.
- [48] J. T. S. Irvine, D. C. Sinclair, A. R. West, Adv. Mater. 1990 , 2 , 132-138.
- [49] E. Ivers-Tiffee, A. Weber, J. Ceram. Soc. Jpn. 2017 , 125 , 193-201.
- [50] F. Ciucci, Curr. Opin. Electrochem. 2019 , 13 , 132-139.
- [51] H. Akaike, IEEE Trans. Autom. Control 1974 , 19 , 716-723.
- [52] M. Ingdal, R. Johnsen, D. A. Harrington, Electrochim. Acta 2019 , 317 , 648-653.
- [53] E. Barsoukov, J. H. Kim, J. H. Kim, C. O. Yoon, H. Lee, Solid State Ionics 1999 , 116 , 249-261.
- [54] H. Nara, D. Mukoyama, T. Yokoshima, T. Momma, T. Osaka, J. Electrochem. Soc. 2015 , 163 , A434-A441.
- [55] Z. Siroma, T. Sato, T. Takeuchi, R. Nagai, A. Ota, T. Ioroi, J. Power Sources 2016 , 316 , 215-223.
- [56] P. Braun, C. Uhlmann, M. Weiss, A. Weber, E. Ivers-Tiffée, J. Power Sources 2018 , 393 , 119-127.
- [57] N. Kaiser, S. Spannenberger, M. Schmitt, M. Cronau, Y. Kato, B. Roling, J. Power Sources 2018 , 396 , 175-181.
- [58] J. Jamnik, J. Maier, J. Electrochem. Soc. 1999 , 146 , 4183-4188.
- [59] J. Jamnik, Solid State Ionics 2003 , 157 , 19-28.
- [60] S. D. Fabre, D. Guy-Bouyssou, P. Bouillon, F. Le Cras, C. Delacourt, J. Electrochem. Soc. 2011 , 159 , A104-A115.
- [61] L. H. J. Raijmakers, D. L. Danilov, R. A. Eichel, P. H. L. Notten, Electrochim. Acta 2020 , 330 , 135147.
- [62] M. C. Pang, Y. Hao, M. Marinescu, H. Wang, M. Chen, G. J. Offer, Phys. Chem. Chem. Phys. 2019 , 21 , 22740-22755.
- [63] A. A. Talin, D. Ruzmetov, A. Kolmakov, K. McKelvey, N. Ware, F. El Gabaly, B. Dunn, H. S. White, ACS Appl. Mater. Interfaces 2016 , 8 , 32385-32391.
- [64] J. Park, D. Kim, W. A. Appiah, J. Song, K. T. Bae, K. T. Lee, J. Oh, J. Y. Kim, Y. G. Lee, M. H. Ryou, Y. M. Lee, Energy Storage Mater. 2019 , 19 , 124129.
- [65] M. Finsterbusch, T. Danner, C. L. Tsai, S. Uhlenbruck, A. Latz, O. Guillon, ACS Appl. Mater. Interfaces 2018 , 10 , 22329-22339.
- [66] J. B. Bates, N. J. Dudney, G. R. Gruzalski, R. A. Zuhr, A. Choudhury, C. F. Luck, J. D. Robertson, Solid State Ionics 1992 , 53-56 , 647-654.
- [67] J. B. Bates, N. J. Dudney, B. Neudecker, A. Ueda, C. D. Evans, Solid State Ionics 2000 , 135 , 33-45.
- [68] D. Cheng, T. A. Wynn, X. Wang, S. Wang, M. Zhang, R. Shimizu, S. Bai, H. Nguyen, C. Fang, M. Cheol Kim, W. Li, B. Lu, S. J. Kim, Y. S. Meng, Joule 2020 , 4 , 2484-2500.
- [69] M. Braglia, I. V. Ferrari, T. Djenizian, S. Kaciulis, P. Soltani, M. L. Di Vona, P. Knauth, ACS Appl. Mater. Interfaces 2017 , 9 , 22902-22910.
- [70] Y. Iriyama, T. Kako, C. Yada, T. Abe, Z. Ogumi, Solid State Ionics 2005 , 176 , 2371-2376.
- [71] J. Collins, J. P. de Souza, Y. S. Lee, A. Pacquette, J. M. Papalia, D. M. Bishop, T. Todorov, M. Krishnan, E. Joseph, J. Rozen, D. Sadana, J. Vac. Sci. Technol. A 2020 , 38 , 033212.
- [72] M. Haruta, S. Shiraki, T. Suzuki, A. Kumatani, T. Ohsawa, Y. Takagi, R. Shimizu, T. Hitosugi, Nano Lett. 2015 , 15 , 1498-1502.
- [73] S. Larfaillou, D. Guy-Bouyssou, F. Le Cras, S. Franger, J. Power Sources 2016 , 319 , 139-146.
- [74] P. Albertus, S. Babinec, S. Litzelman, A. Newman, Nat. Energy 2018 , 3 , 16-21.
- [75] W. D. Richards, L. J. Miara, Y. Wang, J. C. Kim, G. Ceder, Chem. Mater. 2016 , 28 , 266-273.
- [76] G. F. Dewald, S. Ohno, M. A. Kraft, R. Koerver, P. Till, N. M. VargasBarbosa, J. Janek, W. G. Zeier, Chem. Mater. 2019 , 31 , 8328-8337.
- [77] T. K. Schwietert, V. A. Arszelewska, C. Wang, C. Yu, A. Vasileiadis, N. J. J. de Klerk, J. Hageman, T. Hupfer, I. Kerkamm, Y. Xu, E. van der Maas, E. M. Kelder, S. Ganapathy, M. Wagemaker, Nat. Mater. 2020 , 19 , 428435.
- [78] D. H. S. Tan, E. A. Wu, H. Nguyen, Z. Chen, M. A. T. Marple, J. M. Doux, X. Wang, H. Yang, A. Banerjee, Y. S. Meng, ACS Energy Lett. 2019 , 18 , 2418-2427.
- [79] N. Kamaya, K. Homma, Y. Yamakawa, M. Hirayama, R. Kanno, M. Yonemura, T. Kamiyama, Y. Kato, S. Hama, K. Kawamoto, A. Mitsui, Nat. Mater. 2011 , 10 , 682-686.
- [80] H. J. Deiseroth, S. T. Kong, H. Eckert, J. Vannahme, C. Reiner, T. Zaiß, M. Schlosser, Angew. Chem. Int. Ed. 2008 , 47 , 755-758; Angew. Chem. 2008 , 120 , 767-770.
- [81] Y. Seino, T. Ota, K. Takada, A. Hayashi, M. Tatsumisago, Energy Environ. Sci. 2014 , 7 , 627-631.
- [82] P. Bron, S. Dehnen, B. Roling, J. Power Sources 2016 , 329 , 530-535.
- [83] M. Kodama, S. Komiyama, A. Ohashi, N. Horikawa, K. Kawamura, S. Hirai, J. Power Sources 2020 , 462 , 228160.
- [84] J. M. Doux, Y. Yang, D. H. S. Tan, H. Nguyen, E. A. Wu, X. Wang, A. Banerjee, Y. S. Meng, J. Mater. Chem. A 2020 , 8 , 5049-5055.
- [85] M. A. Kraft, S. Ohno, T. Zinkevich, R. Koerver, S. P. Culver, T. Fuchs, A. Senyshyn, S. Indris, B. J. Morgan, W. G. Zeier, J. Am. Chem. Soc. 2018 , 140 , 16330-16339.
- [86] S. Wenzel, S. Randau, T. Leichtweiß, D. A. Weber, J. Sann, W. G. Zeier, J. Janek, Chem. Mater. 2016 , 28 , 2400-2407.
- [87] P. Bron, B. Roling, S. Dehnen, J. Power Sources 2017 , 352 , 127-134.
- [88] J. M. Whiteley, J. H. Woo, E. Hu, K.-W. Nam, S.-H. Lee, J. Electrochem. Soc. 2014 , 161 , A1812-A1817.
- [89] N. Ohta, K. Takada, I. Sakaguchi, L. Zhang, R. Ma, K. Fukuda, M. Osada, T. Sasaki, Electrochem. Commun. 2007 , 9 , 1486-1490.
- [90] J. Haruyama, K. Sodeyama, L. Han, K. Takada, Y. Tateyama, Chem. Mater. 2014 , 26 , 4248-4255.
- [91] N. J. J. De Klerk, M. Wagemaker, ACS Appl. Mater. Interfaces 2018 , 1 , 5609-5618.
- [92] S. Braun, C. Yada, A. Latz, J. Phys. Chem. C 2015 , 119 , 22281-22288.
- [93] M. Yamamoto, Y. Terauchi, A. Sakuda, M. Takahashi, Sci. Rep. 2018 , 8 , 1212.
- [94] S. Ito, S. Fujiki, T. Yamada, Y. Aihara, Y. Park, T. Y. Kim, S.-W. Baek, J.-M. Lee, S. Doo, N. Machida, J. Power Sources 2014 , 248 , 943-950.
- [95] J. H. Woo, J. E. Trevey, A. S. Cavanagh, Y. S. Choi, S. C. Kim, S. M. George, K. H. Oh, S.-H. Lee, J. Electrochem. Soc. 2012 , 159 , A1120A1124.
- [96] Z. Zhang, S. Chen, J. Yang, J. Wang, L. Yao, X. Yao, P. Cui, X. Xu, ACS Appl. Mater. Interfaces 2018 , 10 , 2556-2565.
- [97] W. Zhang, D. A. Weber, H. Weigand, T. Arlt, I. Manke, D. Schröder, R. Koerver, T. Leichtweiss, P. Hartmann, W. G. Zeier, J. Janek, ACS Appl. Mater. Interfaces 2017 , 9 , 17835-17845.
- [98] A. Hayashi, T. Ohtomo, F. Mizuno, K. Tadanaga, M. Tatsumisago, Electrochem. Commun. 2003 , 5 , 701-705.
- [99] N. Machida, K. Kobayashi, Y. Nishikawa, T. Shigematsu, Solid State Ionics 2004 , 175 , 247-250.
- [100] H. Nagata, Y. Chikusa, J. Power Sources 2016 , 329 , 268-272.
- [101] M. Agostini, Y. Aihara, T. Yamada, B. Scrosati, J. Hassoun, Solid State Ionics 2013 , 244 , 48-51.
- [102] X. Yao, D. Liu, C. Wang, P. Long, G. Peng, Y. S. Hu, H. Li, L. Chen, X. Xu, Nano Lett. 2016 , 16 , 7148-7154.
- [103] Y. Wang, T. Liu, L. Estevez, J. Kumar, Energy Storage Mater. 2020 , 27 , 232-243.
- [104] T. F. Fässler, T. M. F. Restle, J. V. Dums, G. Raudaschl-Sieber, Chem. A Eur. J. 2020 , 26 , 6812-6819.
- [105] T. F. Fässler, T. M. F. Restle, C. Sedlmeier, H. Kirchhain, W. Klein, G. Raudaschl-Sieber, V. L. Deringer, L. van Wüllen, H. A. Gasteiger, Angew. Chem. Int. Ed. 2019 , 59 , 5665-5674.
- [106] T. Asano, A. Sakai, S. Ohuchi, M. Sakaida, A. Miyazaki, S. Hasegawa, ECS Meet. Abstr. 2018 , MA2018-01 , 484.
- [107] W. Weppner, P. Hartwig, A. Rabenau, J. Power Sources 1981 , 6 , 251259.
- [108] T. Asano, A. Sakai, S. Ouchi, M. Sakaida, A. Miyazaki, S. Hasegawa, Adv. Mater. 2018 , 30 , 1803075.
- [109] K. H. Park, K. Kaup, A. Assoud, Q. Zhang, X. Wu, L. F. Nazar, ACS Energy Lett. 2020 , 533-539.
- [110] L. Nazar, L. Zhou, C. Y. Kwok, A. Shyamsunder, Q. Zhang, X. Wu, Energy Environ. Sci. 2020 , 13 , 2056.
- [111] P. Knauth, Solid State Ionics 2009 , 180 , 911-916.
- [112] W. Bucheli, T. Durán, R. Jimenez, J. Sanz, A. Varez, Inorg. Chem. 2012 , 51 , 5831-5838.
- [113] J. Wang, C. W. Sun, Y. D. Gong, H. R. Zhang, J. A. Alonso, M. T. Fernández-Diaz, Z. L. Wang, J. B. Goodenough, Chinese Phys. B 2018 , 27 , 0-6.
- [114] J. Awaka, N. Kijima, H. Hayakawa, J. Akimoto, J. Solid State Chem. 2009 , 182 , 2046-2052.

- [115] R. Murugan, V. Thangadurai, W. Weppner, Angew. Chem. Int. Ed. Engl. 2007 , 46 , 7778-7781.
- [116] A. J. Samson, K. Hofstetter, S. Bag, V. Thangadurai, Energy Environ. Sci. 2019 , 12 , 2957-2975.
- [117] V. Thangadurai, D. Pinzaru, S. Narayanan, A. K. Baral, J. Phys. Chem. Lett. 2015 , 6 , 292-299.
- [118] A. G. Squires, D. O. Scanlon, B. J. Morgan, Chem. Mater. 2020 , 32 , 18761886.
- [119] I. N. David, T. Thompson, J. Wolfenstine, J. L. Allen, J. Sakamoto, B. Viyas, J. Am. Ceram. Soc. 2015 , 98 , 1209-1214.
- [120] F. M. Pesci, R. H. Brugge, A. K. O. Hekselman, A. Cavallaro, R. J. Chater, A. Aguadero, J. Mater. Chem. A 2018 , 6 , 19817-19827.
- [121] K. Kataoka, H. Nagata, J. Akimoto, Sci. Rep. 2018 , 8 , 9965.
- [122] F. Flatscher, M. Philipp, S. Ganschow, H. M. R. Wilkening, D. Rettenwander, J. Mater. Chem. A 2020 , 8 , 15782-15788.
- [123] X. Han, Y. Gong, K. Fu, X. He, G. T. Hitz, J. Dai, A. Pearse, B. Liu, H. Wang, G. Rubloff, Y. Mo, V. Thangadurai, E. D. Wachsman, L. Hu, Nat. Mater. 2017 , 16 , 572-579.
- [124] L. Cheng, E. J. Crumlin, W. Chen, R. Qiao, H. Hou, S. Franz Lux, V. Zorba, R. Russo, R. Kostecki, Z. Liu, K. Persson, W. Yang, J. Cabana, T. Richardson, G. Chen, M. Doeff, Phys. Chem. Chem. Phys. 2014 , 16 , 18294-18300.
- [125] T. Kato, T. Hamanaka, K. Yamamoto, T. Hirayama, F. Sagane, M. Motoyama, Y. Iriyama, J. Power Sources 2014 , 260 , 292-298.
- [126] S. Ohta, T. Kobayashi, J. Seki, T. Asaoka, J. Power Sources 2012 , 202 , 332-335.
- [127] S. Ohta, S. Komagata, J. Seki, T. Saeki, S. Morishita, T. Asaoka, J. Power Sources 2013 , 238 , 53-56.
- [128] K. Park, B. C. Yu, J. W. Jung, Y. Li, W. Zhou, H. Gao, S. Son, J. B. Goodenough, Chem. Mater. 2016 , 28 , 8051-8059.
- [129] C. Wang, K. Fu, S. P. Kammampata, D. W. McOwen, A. J. Samson, L. Zhang, G. T. Hitz, A. M. Nolan, E. D. Wachsman, Y. Mo, V. Thangadurai, L. Hu, Chem. Rev. 2020 , 120 , 4257-4300.
- [130] D. E. Fenton, Polymer 1973 , 14 , 589.
- [131] P. V. Wright, Br. Polym. J. 1975 , 7 , 319-327.
- [132] P. V. Wright, Electrochim. Acta 1998 , 43 , 1137-1143.
- [133] M. B. Armand, J. M. Chabagno, M. Duclot, in St Andrews, Scotl. , 1978 , pp. 20-22.
- [134] M. B. Armand, M. J. Duclot, P. Rigaud, Solid State Ionics 1981 , 3/4 , 429430.
- [135] M. Armand, Solid State Ionics 1983 , 9-10 , 745-754.
- [136] M. B. Armand, J. M. Chabagno, M. J. Duclot, in Fast Ion Transp. Solids Electrodes Electrolytes , Elsevier Ltd, 1979 , p. 131.
- [137] M. Vervaeke, G. Calabrese, Int. J. Veh. Des. 2015 , 68 , 245-264.
- [138] H. Eitouni, J. Yang, R. Pratt, X. Wang, U. Grape, High-Voltage Solid Polymer Batteries for Electric Drive Vehicles , Seeo, Inc., Hayward, CA (United States), 2014 .
- [139] N. Boaretto, L. Meabe, M. Martinez-Ibañez, M. Armand, H. Zhang, J. Electrochem. Soc. 2020 , 167 , 70524.
- [140] Y. Xia, T. Fujieda, K. Tatsumi, P. P. Prosini, T. Sakai, J. Power Sources 2001 , 92 , 234-243.
- [141] M. Wetjen, G. T. Kim, M. Joost, G. B. Appetecchi, M. Winter, S. Passerini, J. Power Sources 2014 , 246 , 846-857.
- [142] S. Ramesh, O. P. Ling, Polym. Chem. 2010 , 1 , 702-707.
- [143] H. Jia, H. Onishi, N. von Aspern, U. Rodehorst, K. Rudolf, B. Billmann, R. Wagner, M. Winter, I. Cekic-Laskovic, J. Power Sources 2018 , 397 , 343351.
- [144] M. Jaipal Reddy, J. Siva Kumar, U. V. Subba Rao, P. P. Chu, Solid State Ionics 2006 , 177 , 253-256.
- [145] Z. Gadjourova, Y. G. Andreev, D. P. Tunstall, P. G. Bruce, Nature 2001 , 412 , 520-523.
- [146] Z. Stoeva, I. Martin-Litas, E. Staunton, Y. G. Andreev, P. G. Bruce, J. Am. Chem. Soc. 2003 , 125 , 4619-4626.
- [147] D. Lin, W. Liu, Y. Liu, H. R. Lee, P.-C. Hsu, K. Liu, Y. Cui, Nano Lett. 2016 , 16 , 459-465.
- [148] R. Tan, R. Gao, Y. Zhao, M. Zhang, J. Xu, J. Yang, F. Pan, ACS Appl. Mater. Interfaces 2016 , 8 , 31273-31280.
- [149] F. Croce, G. B. Appetecchi, L. Persi, B. Scrosati, Nature 1998 , 394 , 456458.
- [150] K. K. Fu, Y. Gong, J. Dai, A. Gong, X. Han, Y. Yao, C. Wang, Y. Wang, Y. Chen, C. Yan, Proc. Nat. Acad. Sci. 2016 , 113 , 7094-7099.
- [151] Y. Zhao, C. Wu, G. Peng, X. Chen, X. Yao, Y. Bai, F. Wu, S. Chen, X. Xu, J. Power Sources 2016 , 301 , 47-53.
- [152] R. C. Xu, X. H. Xia, S. Z. Zhang, D. Xie, X. L. Wang, J. P. Tu, Electrochim. Acta 2018 , 284 , 177-187.
- [153] M. Otoyama, A. Sakuda, M. Tatsumisago, A. Hayashi, ACS Appl. Mater. Interfaces 2020 , 12 , 29228-29234.
- [154] K. Balani, V. Verma, A. Agarwal, R. Narayan, in Biosurfaces A Mater. Sci. Eng. Perspect. , John Wiley &amp; Sons, 2015 , pp. 329-344.
- [155] S. B. Aziz, T. J. Woo, M. F. Z. Kadir, H. M. Ahmed, J. Sci. Adv. Mater. Devices 2018 , 3 , 1-17.
- [156] S. B. Aziz, M. G. Faraj, O. G. Abdullah, Sci. Rep. 2018 , 8 , 14308.
- [157] Z. Wei, Y. Ren, M. Wang, J. He, W. Huo, H. Tang, Nanoscale Res. Lett. 2020 , 15 , 122.
- [158] Z. Wu, Z. Xie, J. Wang, T. Yu, X. Du, Z. Wang, X. Hao, A. Abudula, G. Guan, Int. J. Hydrogen Energy 2020 , 45 , 19601-19610.
- [159] A. Swiderska-Mocek, P. Jakobczyk, A. Lewandowski, J. Solid State Electrochem. 2017 , 21 , 2825-2831.
- [160] Y. Zhao, W. E. Tenhaeff, ACS Appl. Polym. Mater. 2020 , 2 , 80-90.
- [161] R. He, F. Peng, W. E. Dunn, T. Kyu, Electrochim. Acta 2017 , 246 , 123134.
- [162] Groupe Bolloré, 'Blue solutions registration documents,' can be found under https://www.blue-solutions.com/en/blue-solutions/investissors/ informations-reglementees/, 2015 .
- [163] H. Wang, X. Cao, W. Liu, X. Sun, Front. Energy Res. 2019 , 7 , 112.
- [164] J. Yi, S. Guo, P. He, H. Zhou, Energy Environ. Sci. 2017 , 10 , 860-884.
- [165] X. Xu, G. Hou, X. Nie, Q. Ai, Y. Liu, J. Feng, L. Zhang, P. Si, S. Guo, L. Ci, J. Power Sources 2018 , 400 , 212-217.
- [166] F. Lee, M.-C. Tsai, M.-H. Lin, Y. L. Ni'mah, S. Hy, C.-Y. Kuo, J.-H. Cheng, J. Rick, W.-N. Su, B.-J. Hwang, J. Mater. Chem. A 2017 , 5 , 6708-6715.
- [167] C. Zhang, Y. Lin, J. Liu, J. Mater. Chem. A 2015 , 3 , 10760-10766.
- [168] M. Balaish, E. Peled, D. Golodnitsky, Y. Ein-Eli, Angew. Chem. Int. Ed. 2015 , 54 , 436-440; Angew. Chem. 2015 , 127 , 446-450.
- [169] F. Lee, M.-C. Tsai, M.-H. Lin, Y. L. Ni'mah, S. Hy, C.-Y. Kuo, J.-H. Cheng, J. Rick, W.-N. Su, B.-J. Hwang, J. Mater. Chem. A 2017 , 5 , 6708-6715.
- [170] B. A. Boukamp, A. Rolle, Solid State Ionics 2017 , 302 , 12-18.
- [171] M. A. Danzer, Batteries 2019 , 5 , 53.
- [172] J. Huang, M. Papac, R. O'Hayre, Electrochim. Acta 2020 , 367 , 137493.
- [173] A. Mertens, J. Granwehr, J. Energy Storage 2017 .
- [174] Y. Zhang, Q. Tang, Y. Zhang, J. Wang, U. Stimming, A. A. Lee, Nat. Commun. 2020 , 11 , 1706.
- [175] M.-F. Ng, J. Zhao, Q. Yan, G. J. Conduit, Z. W. Seh, Nat. Mach. Intell. 2020 , 2 , 161-170.
- [176] M. Itagaki, N. Kobari, S. Yotsuda, K. Watanabe, S. Kinoshita, M. Ue, J. Power Sources 2005 , 148 , 78-84.
- [177] M. Itagaki, K. Honda, Y. Hoshi, I. Shitanda, J. Electroanal. Chem. 2015 , 737 , 78-84.
- [178] J. Huang, H. Ge, Z. Li, J. Zhang, Electrochim. Acta 2015 , 176 , 311-320.

[179]

B. A. Boukamp, J. Ross Macdonald,

Solid State Ionics

1994

,

74

, 85-101.

- [180] D. Klotz, J. P. Schmidt, A. Kromp, A. Weber, E. Ivers-Tiffée, ECS Trans. 2019 .
- [181] T. Krauskopf, R. Dippel, H. Hartmann, K. Peppler, B. Mogwitz, F. H. Richter, W. G. Zeier, J. Janek, Joule 2019 , 3 , 2030-2049.
- [182] N. Wolff, N. Harting, F. Röder, M. Heinrich, U. Krewer, Eur. Phys. J. Spec. Top. 2019 , 227 , 2617-2640.
- [183] M. D. Murbach, V. W. Hu, D. T. Schwartz, J. Electrochem. Soc. 2018 , 165 , A2758-A2765.
- [184] N. Harting, N. Wolff, U. Krewer, Electrochim. Acta 2018 , 281 , 378-385.
- [185] C. Chen, X. Guo, Acta Chim. Slov. 2016 , 63 , 489-495.
- [186] D. Brogioli, F. Langer, R. Kun, F. La Mantia, ACS Appl. Mater. Interfaces 2019 , 11 , 11999-12007.
- [187] F. Fasmin, R. Srinivasan, J. Electrochem. Soc. 2017 .
- [188] S. Randau, D. A. Weber, O. Kötz, R. Koerver, P. Braun, A. Weber, E. IversTiffée, T. Adermann, J. Kulisch, W. G. Zeier, Nat. Energy 2020 , 1-12.
- [189] J. Vetter, P. Novák, M. R. Wagner, C. Veit, K. C. Möller, J. O. Besenhard, M. Winter, M. Wohlfahrt-Mehrens, C. Vogler, A. Hammouche, J. Power Sources 2005 , 147 , 269-281.
- [190] A. Bielefeld, D. A. Weber, J. Janek, ACS Appl. Mater. Interfaces 2020 , 12 , 12821-12833.
- [191] S. Ohno, T. Bernges, J. Buchheim, M. Duchardt, A. K. Hatz, M. A. Kraft, H. Kwak, A. L. Santhosha, Z. Liu, N. Minafra, F. Tsuji, A. Sakuda, R. Schlem, S. Xiong, Z. Zhang, P. Adelhelm, H. Chen, A. Hayashi, Y. S. Jung, B. V. Lotsch, B. Roling, N. M. Vargas-Barbosa, W. G. Zeier, ACS Energy Lett. 2020 , 5 , 910-915.

Manuscript received: January 24, 2021 Revised manuscript received: March 25, 2021 Accepted manuscript online: April 8, 2021