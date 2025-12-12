## Role of Na + Interstitials and Dopants in Enhancing the Na + Conductivity of the Cubic Na3PS4 Superionic Conductor

Zhuoying Zhu, Iek-Heng Chu, Zhi Deng, and Shyue Ping Ong *

Department of NanoEngineering, University of California, San Diego, 9500 Gilman Drive, Mail Code 0448, La Jolla, California 92093, United States

## * S Supporting Information

ABSTRACT: In this work, we performed a /uniFB01 rst-principles investigation of the phase stability, dopant formation energy and Na + conductivity of pristine and doped cubic Na3PS4 (c-Na3PS4). We show that pristine c-Na 3PS4 is an extremely poor Na ionic conductor, and the introduction of Na + excess is the key to achieving reasonable Na + conductivities. We studied the e /uniFB00 ect of aliovalent doping of M 4+ for P 5+ in c-Na 3 PS4, yielding Na 3+ x M x P1 -x S4 (M = Si, Ge, and Sn with x = 0.0625; M = Si with x = 0.125). The formation energies in all the doped structures with dopant concentration of x = 0.0625 are found to be relatively low. Using ab initio molecular dynamics simulations, we predict that 6.25% Si-doped c-Na3PS4 has a Na + conductivity of 1.66 mS/cm, in excellent agreement with previous experimental results. Remarkably, we /uniFB01 nd that Sn 4+ doping at the same concentration yields a much higher predicted Na + conductivity of 10.7 mS/cm, though with a higher dopant formation energy. A higher Si 4+ doping concentration of x = 0.125 also yields

a signi /uniFB01 cant increase in Na + conductivity with an even higher dopant formation energy. Finally, topological and van Hove correlation function analyses suggest that the channel volume and correlation in Na + motions may play important roles in enhancing Na + conductivity in this structure.

## ■ INTRODUCTION

Rechargeable Na-ion batteries have enjoyed a resurgence of interest in recent years, 1 -4 propelled in part by concerns about the global availability of lithium, and also by the exciting possibility of novel chemistries. Though signi /uniFB01 cant advances have been made in the development of Na-ion cathodes and anodes, 5 -7 a major impediment to the commercial viability of rechargeable Na-ion batteries is the lack of an e /uniFB00 ective electrolyte. Current Na-ion electrolytes are mostly based on the same fundamental chemistry as Li-ion electrolytes, a mixture of cyclic and linear organic carbonates with a Na-salt. 8 Such organic solvent-based liquid electrolytes are /uniFB02 ammable and have limited electrochemical windows. 9 -12

A promising alternative architecture is all-solid-state Na-ion battery utilizing non /uniFB02 ammable ceramic Na superionic conductor electrolytes. Na solid electrolytes such as β -alumina and NAtrium Superionic CONductors (NASICON) are wellstudied, but they typically exhibit reasonable ionic conductivities only at higher temperatures. 7,13 -16

An exciting recent development is the discovery of the cubic phase of Na3PS4 (c-Na3PS4, space group: I 4 ̅ 3 m ) in 2012. 14 Initially reported to have a Na + conductivity of 0.2 mS/cm, 14 Hayashi and co-workers were able to subsequently enhance the conductivity of c-Na3PS4 to 0.46 mS/cm using crystalline Na 2S with high purity of over 99% followed by heat treatment. 17 Further e /uniFB00 orts at optimizing the conductivity within the (1 -x )Na3PS4 · x Na4SiS4 pseudobinary system yield a maximum

ionic conductivity as high as 0.74 mS/cm at x around 0.06. 18,19 Recent /uniFB01 rst-principles work also shows that Na3PS4 is likely to have favorable elastic properties that allow good electrode contact to be achieved with cold-press sintering. 20

c-Na3PS4 is therefore a promising solid electrolyte candidate, particularly if its ionic conductivity is further improved with proper doping strategies. Using /uniFB01 rst-principles computational methods, one can rapidly investigate the microscopic mechanisms of di /uniFB00 usion in c-Na3PS4 and the e /uniFB00 ect of doping on its overall conductivity. 21,22 The insights gained from such an exercise would not only guide further optimization, but also provide important insights for design of other novel Na superionic conductors.

In this article, we performed a /uniFB01 rst-principles investigation of the phase stability and Na + ionic transport in undoped and M 4+ -doped (M = Si, Ge, and Sn) c-Na3PS4. We demonstrate that pristine c-Na3PS4 is in fact an extremely poor ionic conductor, but with the introduction of Na + interstitials, a reasonably high conductivity can be achieved. We further demonstrate that 6.25% doping of Si 4+ for P 5+ with the concomitant introduction of compensating Na + interstitials result in Na 3+ x Si x P1 -x S4 with predicted Na + conductivities that are in excellent agreement with previous experimental results.

Received:

September 18, 2015

Revised:

November 24, 2015

Published:

November 30, 2015

Chem. Mater.

pubs.acs.org/cm

Figure 1. (a) Crystal structure of c-Na3PS4 primitive cell with green -white spheres, which represent the partially occupied Na sites, whereas dark purple tetrahedrons are PS 4 3 -. (b) The lowest energy ordering of the 2 × 2 × 2 c-Na3PS4 supercell with an Na + interstitial (located within the dashed rectangle).

Furthermore, we show that increased Si 4+ doping (from x = 0.0625 to 0.125) and Sn 4+ doping can potentially achieve even higher conductivities.

## ■ METHODS

All calculations were performed with the Vienna Ab initio Simulation Package (VASP), 23 within the projector augmented wave (PAW) approach. 24 The Perdew -Burke -Ernzerhof (PBE) generalizedgradient approximation (GGA) 25 was adopted for the exchangecorrelation functional. Other parameters such as kinetic energy cuto /uniFB00 , k -mesh were carefully chosen under di /uniFB00 erent situations to ensure the convergence of energies while keeping the computational cost reasonable, as detailed in the subsections below. The Python Materials Genomics (pymatgen) materials analysis library 26 was used for all analyses.

Phase Stability. Cubic Na3PS4 ( I 4 ̅ 3 m ) has two symmetrically distinct Na sites: the 6 b site (Na1) with a partial occupancy of 0.8, and the 12 d site (Na2) with a partial occupancy of 0.1 (Figure 1a). 19 Structural optimizations were carried out on all symmetrically distinct orderings of the primitive cell enumerated using the algorithm of Hart et al. 27 We then selected the lowest energy con /uniFB01 guration in subsequent calculations.

We also studied Na3+ x M x P1 -x S4 with M = Si, Ge, and Sn in this work. Since the maximum ionic conductivity reported by Hayashi et al. 18,19 was achieved with Si/P ratio equal to 6:94, an initial value of x = 0.0625 was chosen to mimic the reported dopant concentration. The doped systems were constructed using a 2 × 2 × 2 supercell of the conventional unit cell of c-Na 3 PS4, in which one P 5+ is replaced by M 4+ (Si, Ge, or Sn) and a Na + added to maintain overall charge neutrality. For M = Si, we also studied the e /uniFB00 ect of dopant concentration by doubling x to 0.125 with corresponding increase in Na + concentration.

The calculation parameters used (spin-polarized, kinetic energy cuto /uniFB00 of 520 eV and k -point density of 1000 per atom) are consistent with those used in the Materials Project (MP). 28 The phase stabilities of c-Na3PS4 and Na3+ x M x P1 -x S4 were investigated by constructing the Na -M -P -S phase diagrams 29 using precomputed energies of existing Na x P y S z and Na w M x P y S z compounds in the MP database extracted via the Materials Application Programming Interface. 30 To ensure a good coverage of the Na -P -S chemical space, we also performed S for O substitution of all Na -P -O and Na for Li substitution of all Li -P -S compounds and included the Na4P2S6 and Na2P2S6 structures that were reported recently. 31,32

For all materials of interest, we computed the decomposition energy (also known as the energy above hull), E decomp , of each phase of interest to the most stable linear combination of equilibrium phases in the Na -P -S or Na -M -P -S phase diagram. 29 Stable phases would have an E decomp of 0, while the higher the E decomp , the more unstable a phase is.

Correction for Sulfur. In our investigations, we found that the binding energy of ground state sulfur (monoclinic S 8 ) is signi /uniFB01 cantly overestimated by the PBE functional, similar to the well-known overbinding observed for the O2 molecule. 33 Following a similar methodology as that proposed by Wang et al., we have /uniFB01 tted a correction for sulfur using the formation energies of main group sul /uniFB01 des (see Supporting Information). This correction, which corrects for both the overbinding as well as the incomplete self-interaction error cancellation in going from S 8 to S 2 -, is estimated to be -0.66 eV per S atom and is applied to all subsequent analyses. This correction will be incorporated into the Materials Project to improve predicted sul /uniFB01 de formation energies.

Dopant Formation Energy. Neutral dopant formation energies were calculated using the formalism presented by Wei et al. 34

<!-- formula-not-decoded -->

where E tot[M] and E tot [bulk] are the total energies of the structure with and without the neutral dopant M, respectively; μ i is the atomic chemical potential of species i that varies based on di /uniFB00 erent experimental conditions; ni indicates the number of atoms of species i being added ( ni &gt; 0) or removed ( ni &lt; 0) from the pristine structure. μ i can be de /uniFB01 ned as μ i = Ei + Δ μ i , where Δ μ i is the chemical potential of species i referenced to the elemental solid/gas with energy Ei . In the case of Na 3+ x M x P1 -x S4 with M = Si, Ge, and Sn, and x = 0.0625, the formation of the defect structure involves an addition of the dopant M 4+ and a Na + interstitial, together with the removal of a host P 5+ ion. The corresponding formation energy E f can be expressed as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Additional constraints can be applied to the atomic chemical potentials μ i under equilibrium growth conditions. First, to avoid precipitation of the elemental M, Na, P, and S, Δ μ i ≤ 0. Second, to maintain a stable c-Na3PS4 framework structure during synthesis

<!-- formula-not-decoded -->

where E f [Na3PS4] is the formation energy of the pristine c-Na3PS4 per formula unit (f.u.). Third, possible secondary phases formed between the dopant M and the framework structure are to be avoided as well. In the case of Na3+ x Si x P1 -x S4 with x = 0.0625, for example, the formation of the possible secondary phase Na4SiS4, as indicated in Table 1, should be avoided. This leads to the following inequality:

<!-- formula-not-decoded -->

where E f [Na4SiS4] is the formation energy of Na 4 SiS 4 .

DOI: 10.1021/acs.chemmater.5b03656 Chem. Mater. 2015, 27, 8318 - 8325

Table 1. Decomposition Energies E decomp , the Corresponding Decomposed Products, and Neutral Dopant Formation Energies E f of the Doped c-Na3PS4 Compared with Undoped Case

| dopant M   | x      | E f (eV/f.u.)   |   E decomp (meV/atom) | decomposed products                  |
|------------|--------|-----------------|-----------------------|--------------------------------------|
| undoped    | N/A    | N/A             |                     5 | t-Na 3 PS 4                          |
| Si         | 0.125  | 1.65            |                    30 | t-Na 3 PS 4 , Na 4 SiS 4             |
| Si         | 0.0625 | 1.04            |                    13 | t-Na 3 PS 4 , Na 4 SiS 4             |
| Ge         | 0.0625 | 1.04            |                    13 | t-Na 3 PS 4 , Na 6 Ge 2 S 7 , Na 2 S |
| Sn         | 0.0625 | 1.32            |                    15 | t-Na 3 PS 4 , Na 4 SnS 4             |

The lower bound of the dopant formation energy can be directly estimated using the above formalism and is equal to E decomp[M] -E decomp[bulk] where E decomp[M] and E decomp [bulk] are, respectively, the decomposition energies of the M-doped and pristine c-Na3PS4. 35,36 Unless mentioned explicitly, the calculated dopant energies presented in the next section refer to this lower bound.

Ab Initio Molecular Dynamics Simulations. The di /uniFB00 usivities and conductivities of the pristine and doped c-Na3PS4 structures were calculated using ab initio molecular dynamics (AIMD) simulations. Apart from the aforementioned doped structures, defect structure where a single Na + excess is introduced was also studied by removing an electron with a compensating background charge. In all simulations, the lowest energy con /uniFB01 gurations with a unit cell size equivalent to that of the 2 × 2 × 2 c-Na3PS4 were selected.

Similar AIMD simulation parameters were used as per previous work by the authors. 21,37 Nonspin-polarized AIMD simulations were conducted in the NVT ensemble at 800 -1400 K with a Nose -Hoover thermostat. 38,39 A smaller plane-wave energy cuto /uniFB00 of 280 eV and a minimal Γ -centered 1 × 1 × 1 k -point mesh were adopted. The time step of the simulations was 2 fs. The initial structure was fully relaxed at 0 K, and the volume was /uniFB01 xed for AIMD simulations at elevated temperatures until the di /uniFB00 usivity is converged. No framework melting was observed in all simulations. All calculations were automated using an in-house AIMD work /uniFB02 ow. 40,41 The central quantity obtained from each AIMD simulation is the Na ion di /uniFB00 usivity that can be expressed as

<!-- formula-not-decoded -->

where d is the dimensionality factor and equals 3 for 3-D crystal structures, and ⟨ [ Δ r ( t )] 2 ⟩ is the average mean square displacement (MSD) over a time duration t .

The di /uniFB00 usivity was obtained by performing a linear /uniFB01 tting of the MSD vs 2 dt . The Arrhenius plots were constructed to determine the activation energies and obtain extrapolated room-temperature di /uniFB00 usivities D 300K. The room-temperature Na ion conductivity σ 300K can then be derived from the Nernst -Einstein equation as follows:

<!-- formula-not-decoded -->

where ρ is the molar density of di /uniFB00 using Na ions in the unit cell; z = +1 is the charge of Na ions; and F and R are the Faraday ' s constant and the gas constant, respectively. T = 300 K was used in the above equation. It should be noted that the Nernst -Einstein relation applies only for uncorrelated species di /uniFB00 usion. The implication of correlated motion will be discussed in the Discussion section.

van Hove Correlation Function Analysis. To investigate the correlations in the Na ionic motions, we calculated and plotted the van Hove correlation function using trajectories from our AIMD simulations, which can be split into the self-part G s and the distinctpart G d as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Here, δ ( · ) is the one-dimensional Dirac delta function. The angular bracket stands for the ensemble average over the initial time t 0 . r i ( t ) denotes the position of the i th particle at time t. N d and r are the number of di /uniFB00 using Na ions in the unit cell and radial distance, respectively. The presence of the average number density ρ serves as the ' normalization factor ' in G d such that G d → 1 when r ≫ 1. For a given r and t , G s ( r , t ) describes how probable a particle di /uniFB00 uses away from its initial position by a distance of r after time t , whereas G d ( r , t ) describes the radial distribution of N -1 particles after time t with respect to the initial reference particle. In particular, G d ( r , t ) is reduced to the static pair distribution function when t = 0.

## ■ RESULTS

Phase Stability Analysis. c-Na3PS4 belongs to the I 4 ̅ 3 m space group with a lattice parameter of 6.9965(9) Å. 19 It is the high-temperature phase of the tetragonal Na3PS4 (t-Na3 PS4). The lattice parameters for t- and c-Na3PS4 di /uniFB00 er only by around 0.1 Å, and the experimental transition temperature from tNa3PS4 to c-Na3PS4 is around 540 K. 14,42 The major di /uniFB00 erence is that the tetragonal phase is an ordered structure, whereas the cubic phase is disordered with two distinct sodium sites.

The E decomp and the corresponding equilibrium phases for the undoped and doped c-Na3PS4 phases are listed in Table 1. For the undoped c-Na3PS4, our calculation predicts its E decomp to be only 5 meV/atom, with t-Na3PS4 being the stable phase. This result is consistent with previous experimental data that the cubic phase is the metastable phase that is likely entropically stabilized. 14 With the introduction of a Na + interstitial, we /uniFB01 nd that the Na sites redistribute to maintain an approximately even distribution within a chain, leading to Na atoms that are slightly displaced from the Na1 and Na2 positions (Figure 1b).

Our results show that at x = 0.0625, the E decomp of the M 4+ -doped structures are 13 meV/atom for M = Si and Ge, and 15 meV/atom for Sn, respectively. The relatively low decomposition energies indicate that though these doped structures are metastable at 0 K, they can potentially be stabilized at room temperature by entropic e /uniFB00 ects. This is in qualitative agreement with the synthesizibility of Si-doped Na 3PS4 with similar dopant concentration in experiments. 18 At a higher Si dopant concentration with x = 0.125, the resulting E decomp increases to 30 meV/atom, indicating that the structure is more unstable. For Si, Sn-doped structures, the predicted equilibrium phases are t-Na3PS4 and Na4MS4 (M = Si, Sn), while the Ge-doped structure has the equilibrium phases of Na 6 Ge2S7, Na2S, and tNa3PS4. Note that the sulfur energy correction does not a /uniFB00 ect the decomposition products in the systems studied in this work. This is because the t-Na3PS4 and Na4SiS4 remain stable before and after the sul /uniFB01 de correction.

Dopant Formation Energies. The dopant formation energy is an important quantity that measures the synthesizibility of the materials with dopants. The dopant formation energies of all dopants studied are tabulated in Table 1. At x = 0.0625, we /uniFB01 nd relatively low doping energies of 1.04 eV for both 6.25% Ge and Si doping compared to 6.25% Sn doping (1.32 eV) or 12.5% Si doping (1.65 eV). We note that Si doping in c-Na 3PS4 was experimentally achieved for x up to 0.1. Since the dopant formation energy of 6.25% Sn lies between the dopant formation energies of 6.25% and 12.5% Si doping, we expect that 6.25% Sn-doping of c-Na3PS4 to be achievable experimentally.

DOI: 10.1021/acs.chemmater.5b03656

Chem. Mater.

2015, 27, 8318 - 8325

Figure 2. Isosurfaces (blue) of Na ion probability density distribution P for Na3+ x Si x P1 -x S4 ( x = 0.0625) at 800 K.

Probability Density and Site Occupancy. The probability density distribution de /uniFB01 ned on a uniform 3-D grid, namely, P ( r ), is a powerful tool for investigating the ion di /uniFB00 usion of a given species. Two important pieces of information can be obtained from the distribution: (1) high probability sites where the ions tend to reside, which correspond to the low-energy sites in the structure, (2) the pathways of the ions among the low-energy sites. 43 In this work, P is obtained by /uniFB01 rst counting the number of Na ions at each point in the spatial uniform grid within a given time scale. A time averaging is then performed for P . Also, P is normalized such that ∫ Ω P d r = 1 with Ω being the volume of the unit cell. We de /uniFB01 ne the maximum of P ( r ) as P max .

Figure 2 shows the isosurfaces of probability density distributions for Na ions in Na3+ x Si x P1 -x S4 ( x = 0.0625) at 800 K (the lowest temperature at which the AIMD simulations were performed) at various cuto /uniFB00 s. In general, the P ( r ) are fairly similar across all systems investigated. As expected, we /uniFB01 nd that the high probability density positions correspond to the high occupancy (low energy) Na1 sites. As the cuto /uniFB00 is decreased, the isosurfaces show that the Na1 sites are connected to one another via the lower occupancy Na2 sites. We may therefore surmise that the Na2 sites are local minima sites with non-negligible occupation probability that help mediate Na + transport in this structure.

We also calculated the average site occupancies of the di /uniFB00 erent Na sites at 800 K. The site occupancies for the Na1 and Na2 sites for the Na 3+ x Si x P1 -x S4 ( x = 0.0625) are 0.76 and 0.13, respectively, which are fairly close to the reported site occupancies of 0.8 and 0.11, respectively. 19 The deviations between the calculated occupancies and experiments are likely due to the fact that the AIMD simulations are carried out at higher temperatures (800 K) compared to experiments (300 K). Similar trends are observed for Ge-doped, Sn-doped, and Na-excess c-Na3PS4 (see Table S1 in Supporting Information). For the pristine c-Na 3 PS4, the average site occupancy for Na2 is less than 0.1 even at 800 K.

Na + Conductivity. Figure 3 shows the Arrhenius plots of the log of the di /uniFB00 usivity, D , versus the reciprocal of the temperature, 1000/ T , for the systems of interest. Di /uniFB00 usivities at six temperatures (800, 900, 1000, 1100, 1200, and 1400 K) are plotted for all systems except for pristine c-Na3PS4 where simulations at only four temperatures were run. Table 2 summarizes the extrapolated di /uniFB00 usivities D 300K and ionic conductivities σ 300K , including the error range for σ 300K .

From Figure 3a, we may observe that the calculated Na + conductivity is extremely low (1.1 × 10 -4 mS/cm) and the activation barrier is extremely high (537 meV) in the pristine cNa3PS4 material. The introduction of a Na + interstitial increases

Figure 3. Arrhenius plots for (a) c-Na3PS4 with Na + excess and pristine structures; (b) doped structures Na 3+ x M x P1 -x S4 (M = Si, Ge, or Sn).

the conductivity by 4 orders of magnitude to 1.06 mS/cm, while the activation energy decreases to 256 meV.

In practical materials, aliovalent doping is a common approach to modifying the Na concentration. In c-Na3PS4, Na + interstitials can be created by doping the P 5+ sites with M 4+ cations such as Sn 4+ , Ge 4+ , and Si 4+ . The Arrhenius plots for doped Na3+ x M x P1 -x S4 with di /uniFB00 erent values of M and x are given in Figure 3b, and the corresponding room-temperature conductivities and activation energies are reported in Table 2 as well. In general, we observe that similar Na + concentrations tend to result in similar conductivities (e.g., for x = 0.0625 in the Na-excess, Si-doped, and Ge-doped cases), indicating that this is the dominant factor in /uniFB02 uencing the overall ionic conductivity. The predicted room-temperature Na + conductiv-

DOI: 10.1021/acs.chemmater.5b03656

Chem. Mater.

2015, 27, 8318 - 8325

Figure 4. Plots of the distinct-part of the van Hove correlation function ( G d ) for Na3+ x M x P1 -x S4 at 800 K. G d is a function of the Na -Na pair distance r and time t .

|                          | x      |   channel size (Å) |   channel volume (Å 3 ) | σ 300K (mS/cm)   | error range of σ 300K (mS/cm)   | D 300K (cm 2 /s)   |   E a (meV) |
|--------------------------|--------|--------------------|-------------------------|------------------|---------------------------------|--------------------|-------------|
| pristine                 | N/A    |               2.15 |                     863 | 1.1 × 10 - 4     | 0.68 - 1.9 × 10 - 4             | 1.1 × 10 - 12      |         537 |
| Na + excess              | 0.0625 |               2.15 |                     874 | 1.06             | 0.79 - 1.40                     | 9.8 × 10 - 9       |         256 |
| Na 3+ x Si x P 1 - x S 4 | 0.125  |               2.16 |                     879 | 2.99             | 2.27 - 3.94                     | 2.8 × 10 - 8       |         241 |
| Na 3+ x Si x P 1 - x S 4 | 0.0625 |               2.13 |                     869 | 1.66             | 1.14 - 2.41                     | 1.5 × 10 - 8       |         242 |
| Na 3+ x Ge x P 1 - x S 4 | 0.0625 |               2.16 |                     873 | 0.54             | 0.38 - 0.78                     | 5.1 × 10 - 9       |         280 |
| Na 3+ x Sn x P 1 - x S 4 | 0.0625 |               2.16 |                     910 | 10.7             | 6.86 - 16.8                     | 1.0 × 10 - 7       |         171 |

Table 2. Channel Size, Channel Volume, Extrapolated Na + Conductivity, Di /uniFB00 usivity at 300 K, and Activation Energy

ity for Na3.0625 Si 0.0625 P0.9375 S4 is 1.66 mS/cm, in excellent agreement with the previously measured experimental value of 0.74 mS/cm for 0.94Na3PS4 · 0.06Na4SiS4. 18,19

Remarkably, the Sn-doped c-Na3PS4 is predicted to have a signi /uniFB01 cantly higher Na + conductivity of 10.7 mS/cm compared to the other doped structures. The activation energy for di /uniFB00 usion in this material is also the smallest at 171 meV. We also investigated the e /uniFB00 ect of di /uniFB00 erent dopant concentrations in the case of the Si-doped structure. From Figure 3b and Table 2, we may observe that higher doping concentrations can potentially enhance the Na + conductivity further to 2.99 mS/ cm, though at the cost of increased dopant formation energy and decreased phase stability (see Table 1).

Channel Size, Channel Volume, and van Hove Function. Using the open source Zeo++ software, 44,45 we performed a topological analysis of all systems of interest. In all these materials, Na ions were removed from the relaxed structures to compute the largest radius of the free sphere that can pass through the remaining structure formed by framework cations and anions (P 5+ , S 2 -, and M 4+ ), which is de /uniFB01 ned as ' channel size ' and shown in Table 2. In general, the channel sizes for all cases are very similar to the di /uniFB00 erence of no more than 0.03 Å. At a dopant concentration of x = 6.25%, both Geand Sn-doped structures have the largest channel sizes.

Using the ionic trajectories from AIMD simulations at 800 K, we also calculated the average channel volumes of all systems investigated. This quantity is de /uniFB01 ned as the unit cell volume minus the volume of the framework polyhedrons (PS4 or MS4), and it describes the ' free volume ' for Na ions during the di /uniFB00 usion. The results are given in Table 2. We /uniFB01 nd that the channel volumes in all doped structures are very similar to each other, with the exception of Sn-doped structure where the channel volume is more than 4% higher than those in the rest of the cases.

Figure 4 presents the distinct part of the van Hove correlation function G d for each doped-structure at 800 K.

Our calculations show that G d of all the doped structures always exhibit a pronounced peak at the proximity of r = 0, indicating that the Na ion motions in these materials are highly correlated. The correlated motion in the Sn 4+ doped structure (Figure 4c) takes place sooner than the other doped structures with the same dopant concentration. This is in accordance with the higher di /uniFB00 usion coe /uniFB03 cient found in this structure. In fact, we observe a large amount of single Na + hops between neighboring Na1 and Na2 sites within a 1 ps time scale as well as correlated hops between adjacent Na ions in our AIMD trajectories.

## ■ DISCUSSION

c-Na3PS4 is a highly promising sodium superionic conductor whose ionic conductivity can be further enhanced by aliovalent doping. In this work, we conducted a comprehensive investigation of the phase stability, dopant formation energies, and Na + conductivities of pristine and doped c-Na 3 PS4, with the aim of understanding the reasons for its high conductivity and elucidating potential strategies to further push its conductivity beyond 1 mS/cm.

Our work shows that Na disorder induced by Na excess is key to the high ionic conductivity in c-Na3PS4. We /uniFB01 nd that stoichiometric c-Na3PS4 has a very low ionic conductivity, which is similar to reported value of t-Na 3 PS4. 42 Stoichiometric c-Na3PS4 also has relatively low occupancy on the Na2 site (&lt;0.1 at 800 K), similar to t-Na 3 PS4. Both these observations are not surprising, given the small di /uniFB00 erences in lattice parameters between t- and c-Na3PS4. It is only when the Na + interstitials are introduced to c-Na3PS4 that the Na2 site occupancy increases and the Na + conductivity increases appreciably to the 0.1 -1 mS/cm levels observed experimentally.

With these results in mind, it is therefore somewhat surprising that the initially reported ionic conductivity of pristine c-Na3PS4 by Hayashi et al. is as high as 0.2 mS/cm. 14 We speculate that there may have been doped impurities in the original sample, e.g., from the carbon electrodes or Zr, resulting in Na excess. It should be noted that Hayashi et al. speci /uniFB01 cally excluded Zr as a possible contaminant, and the calculated dopant formation energy of 6.25% Zr doping is estimated to be 1.45 eV/f.u., substantially higher than that for 6.25% Si doping (1.04 eV/f.u.). The fact that the same authors were subsequently able to obtain a signi /uniFB01 cant increase in conductivity to 0.46 mS/cm using a Na2S precursor with high purity 17 further supports the hypothesis that Na + interstitial defects are crucial to achieving high Na + conductivity in this structure. Though a purer Na2S does not necessarily mean Na + interstitials will be formed, a less pure Na2S precursor can potentially result in Na de /uniFB01 ciency and reduce the likelihood of forming Na + interstitials.

The increase in conductivity with the introduction of Na + interstitials is likely caused by the increased Coulombic repulsion between Na + , leading to a redistribution that causes Na to be slightly displaced from the Na1 and Na2 positions. We speculate that this redistribution leads to a shallow energy landscape that promotes the cooperative motion of Na, leading to lower activation barriers and increased conductivity. The van Hove correlation function analysis, which indicates that correlated Na motion happens within a relatively short time scale, supports this hypothesis. Indeed, the higher the conductivity (e.g., in Sn-doped c-Na3PS4), the shorter the time scale in which correlated motion occurs.

A typical strategy to introduce Na + interstitials is through aliovalent substitution of M 4+ for P 5+ in c-Na3PS4. At a Si doping concentration of 6.25%, the predicted room-temperature Na + conductivity of 1.66 mS/cm is in excellent agreement with the reported experimental conductivity of 0.74 mS/cm for 0.94Na3PS4 · 0.06Na4SiS4 reported by Tanibata et al. 18,19 At a higher Si doping concentration of 12.5%, the predicted Na + conductivity further increases to 2.99 mS/cm, but the dopant formation energy increases substantially. This increased dopant formation energy is a possible reason why Tanibata et al. reported ' unknown secondary phases ' at doping concentrations beyond 10%. 18,19

Among the M 4+ dopants investigated, our calculations indicate that a particularly promising candidate for further investigation is Sn-doped structure. Na3.0625 Sn0.0625 P0.9375 S4 is predicted to have a much higher Na + conductivity of 10.7 mS/ cm, while the dopant formation energy is only slightly higher than Si doping at a similar concentration. Given that Si doping in c-Na3PS4 as high as 10% have been achieved experimentally, 6.25% Sn doping should be achievable. As of now, we can only speculate on the reasons why there is such a signi /uniFB01 cant di /uniFB00 erence in conductivity between Sn versus Si doping. Topological analyses /uniFB01 nd that the Sn-doped structure has a slightly larger channel size and free channel volume for Na + di /uniFB00 usion than the Si-doped structure. However, a similar relative di /uniFB00 erence in channel size and volume in the Li10MP2S12 (M = Si, Ge, and Sn) superionic conductor 26 leads to the opposite trend in Na + conductivity of Si &gt; Sn. It may be that such di /uniFB00 erent trends are the result of (a) the di /uniFB00 erent dimensionality of di /uniFB00 usion in Li10MP2S12 systems (quasi 1D) and doped Na3PS4 systems (3D), and (b) the di /uniFB00 erent di /uniFB00 using species, i.e., Li + in Li10MP2S12 and Na + in c-Na3PS4. It is our hope that future experiments will verify if the Sn-doped structure can be synthesized, and if it does indeed exhibit higher conductivities than the Si and Ge-doped structures.

It should be noted that eq 6 provides a good estimate of the di /uniFB00 usivity only in the case of uncorrelated di /uniFB00 usion. The degree to which ionic motion is correlated is frequently described using the Haven ratio, H R , which is de /uniFB01 ned as the ratio of the tracer di /uniFB00 usivity to the charge or dc di /uniFB00 usivity. 46,47 We have not attempted to determine this ratio from AIMD due to the extremely slow convergence of the charge di /uniFB00 usivity. Nevertheless, typical H R values for similar highly correlated di /uniFB00 usion systems are in the range of 0.3 -0.6 (e.g., H R [Li 10SnP2S12] ≈ 0.3). 48 We therefore expect that the computed di /uniFB00 usivities and conductivities in this work to be lower bound estimates that are o /uniFB00 by no more than a factor of 3 and that the qualitative trends should remain valid.

## ■ CONCLUSIONS

To conclude, we have performed a comprehensive investigation of the phase stability, dopant formation energy, and Na + conductivity of c-Na3PS4 and Na3+ x M x P1 -x S4 (M = Si with x = 0.0625 and 0.125; M = Ge, Sn with x = 0.0625). Our results show that Na disorder induced by Na + excess is a key factor to enhancing the Na + conductivity in c-Na3PS4. Si 4+ , Ge 4+ , and Sn 4+ are all viable dopants to introduce Na + excess in c-Na3PS4 for this purpose due to their relatively low dopant formation energies. Our calculated Na + conductivity of 1.66 mS/cm for 6.25% Si-doped c-Na3PS4 is in an excellent agreement with experiments. We also /uniFB01 nd that the Na + conductivity can be further enhanced by increasing Si dopant concentration from 6.25% to 12.5%, but at the cost of much higher dopant

DOI: 10.1021/acs.chemmater.5b03656

Chem. Mater.

2015, 27, 8318 - 8325

formation energy. Finally, we predict that 6.25% Sn-doped cNa3PS4 is a potentially promising Na superionic conductor with a signi /uniFB01 cantly higher Na + conductivity than 6.25% Si-doped cNa3PS4.

## ■ ASSOCIATED CONTENT

## * S Supporting Information

The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.chemmater.5b03656.

Average Na1, Na2 site occupancies of all systems in this work, determination of sulfur correction, and the self-part of the van Hove correlation function for M-doped cNa3PS4 (M = Si, Ge, Sn) (PDF)

## ■ AUTHOR INFORMATION

## Corresponding Author

*

E-mail: ongsp@eng.ucsd.edu.

## Notes

The authors declare no competing /uniFB01 nancial interest.

## ■ ACKNOWLEDGMENTS

This work was supported by the National Science Foundation ' s Designing Materials to Revolutionize and Engineer our Future (DMREF) program under Grant No. 1436976. Some of the computations in this work were performed using the Extreme Science and Engineering Discovery Environment (XSEDE), which is supported by National Science Foundation grant number ACI-1053575.

## ■ REFERENCES

- (1) Larcher, D.; Tarascon, J.-M. Towards Greener and More Sustainable Batteries for Electrical Energy Storage. Nat. Chem. 2015 , 7 , 19 -29.
- (2) Hueso, K. B.; Armand, M.; Rojo, T. High Temperature Sodium Batteries: Status, Challenges and Future Trends. Energy Environ. Sci. 2013 , 6 , 734 -749.
- (3) Ellis, B. L.; Nazar, L. F. Sodium and Sodium-ion Energy Storage Batteries. Curr. Opin. Solid State Mater. Sci. 2012 , 16 , 168 -177.
- (4) Ong, S. P.; Chevrier, V. L.; Hautier, G.; Jain, A.; Moore, C.; Kim, S.; Ma, X.; Ceder, G. Voltage, Stability and Diffusion Barrier Differences Between Sodium-ion and Lithium-ion Intercalation Materials. Energy Environ. Sci. 2011 , 4 , 3680.
- (5) Yabuuchi, N.; Kubota, K.; Dahbi, M.; Komaba, S. Research Development on Sodium-Ion Batteries. Chem. Rev. 2014 , 114 , 11636 -11682.
- (6) Li, X.; Ma, X.; Su, D.; Liu, L.; Chisnell, R.; Ong, S. P.; Chen, H.; Toumar, A.; Idrobo, J.-c.; Lei, Y.; Bai, J.; Wang, F.; Lynn, J. W.; Lee, Y. S.; Ceder, G. Direct Visualization of the Jahn-Teller Effect Coupled to Na Ordering in Na5/8MnO2. Nat. Mater. 2014 , 13 , 586 -592.
- (7) Pan, H.; Hu, Y.-S.; Chen, L. Room-temperature Stationary Sodium-ion Batteries for Large-scale Electric Energy Storage. Energy Environ. Sci. 2013 , 6 , 2338.
- (8) Ponrouch, A.; Marchante, E.; Courty, M.; Tarascon, J.-M.; Palacín, M. R. In Search of An Optimized Electrolyte for Na-ion Batteries. Energy Environ. Sci. 2012 , 5 , 8572.
- (9) Tarascon, J.-M.; Armand, M. Issues and Challenges Facing Rechargeable Lithium Batteries. Nature 2001 , 414 , 359 -367.
- (10) Xu, K. Electrolytes and Interphases in Li-Ion Batteries and Beyond. Chem. Rev. 2014 , 114 , 11503 -11618.
- (11) Armand, M.; Tarascon, J.-M. Building Better Batteries. Nature 2008 , 451 , 652 -657.
- (12) Xu, K. Nonaqueous Liquid Electrolytes for Lithium-based Rechargeable Batteries. Chem. Rev. 2004 , 104 , 4303 -4417.
- (13) Tatsumisago, M.; Hayashi, A. Sulfide Glass-Ceramic Electrolytes for All-Solid-State Lithium and Sodium Batteries. Int. J. Appl. Glass Sci. 2014 , 10 , 226 -235.
- (14) Hayashi, A.; Noi, K.; Sakuda, A.; Tatsumisago, M. Superionic Glass-Ceramic Electrolytes for Room-temperature Rechargeable Sodium Batteries. Nat. Commun. 2012 , 3 , 856.
- (15) Anantharamulu, N.; Koteswara Rao, K.; Rambabu, G.; Vijaya Kumar, B.; Radha, V.; Vithal, M. A Wide-ranging Review on Nasicon Type Materials. J. Mater. Sci. 2011 , 46 , 2821 -2837.
- (16) Hooper, A. A Study of the Electrical Properties of Single-crystal and Polycrystalline β -alumina Using Complex Plane Analysis. J. Phys. D: Appl. Phys. 1977 , 10 , 1487 -1496.
- (17) Hayashi, A.; Noi, K.; Tanibata, N.; Nagao, M.; Tatsumisago, M. High Sodium Ion Conductivity of Glass-Ceramic Electrolytes with Cubic Na3PS4. J. Power Sources 2014 , 258 , 420 -423.
- (18) Tanibata, N.; Noi, K.; Hayashi, A.; Tatsumisago, M. Preparation and Characterization of Highly Sodium Ion Conducting Na3PS4 · Na4SiS4 Solid Electrolytes. RSC Adv. 2014 , 4 , 17120 -17123.
- (19) Tanibata, N.; Noi, K.; Hayashi, A.; Kitamura, N.; Idemoto, Y.; Tatsumisago, M. X-ray Crystal Structure Analysis of Sodium-Ion Conductivity in 94Na3PS4 · 6Na4SiS4 Glass-Ceramic Electrolytes. ChemElectroChem 2014 , 1 , 1130 -1132.
- (20) Deng, Z.; Wang, Z.; Chu, I.-H.; Luo, J.; Ong, S. P. Elastic Properties of Alkali Superionic Conductor Electrolytes from First Principles Calculations. J. Electrochem. Soc. 2016 , 163 , A67 -A74.
- (21) Ong, S. P.; Mo, Y.; Richards, W. D.; Miara, L.; Lee, H. S.; Ceder, G. Phase Stability, Electrochemical Stability and Ionic Conductivity of the Li 10 ± 1 MP2X12 (M = Ge, Si, Sn, Al or P, and X = O, S or Se) Family of Superionic Conductors. Energy Environ. Sci. 2013 , 6 , 148 -156.
- (22) Miara, L. J.; Ong, S. P.; Mo, Y.; Richards, W. D.; Park, Y.; Lee, J.-m.; Lee, H. S.; Ceder, G. Effect of Rb and Ta Doping on the Ionic Conductivity and Stability of the Garnet Li 7+2x -y(La3 -xRbx) (Zr2 -y Tay)O12. Chem. Mater. 2013 , 25 , 3048 -3055.
- (23) Kresse, G. Efficient Iterative Schemes for Ab Initio Total-energy Calculations Using a Plane-wave Basis Set. Phys. Rev. B: Condens. Matter Mater. Phys. 1996 , 54 , 11169 -11186.
- (24) Blo ̈ chl, P. E. Projector Augmented-wave Method. Phys. Rev. B: Condens. Matter Mater. Phys. 1994 , 50 , 17953 -17979.
- (25) Perdew, J. P.; Burke, K.; Ernzerhof, M. Generalized Gradient Approximation Made Simple. Phys. Rev. Lett. 1996 , 77 , 3865 -3868.
- (26) Ong, S. P.; Richards, W. D.; Jain, A.; Hautier, G.; Kocher, M.; Cholia, S.; Gunter, D.; Chevrier, V. L.; Persson, K. a.; Ceder, G. Python Materials Genomics (Pymatgen): A Robust, Open-source Python Library for Materials Analysis. Comput. Mater. Sci. 2013 , 68 , 314 -319.
- (27) Hart, G. L. W.; Forcade, R. W. Algorithm for Generating Derivative Structures. Phys. Rev. B: Condens. Matter Mater. Phys. 2008 , 77 , 224115.
- (28) Jain, A.; Ong, S. P.; Hautier, G.; Chen, W.; Richards, W. D.; Dacek, S.; Cholia, S.; Gunter, D.; Skinner, D.; Ceder, G.; Persson, K.
- A. Commentary: The Materials Project: A Materials Genome Approach to Accelerating Materials Innovation. APL Mater. 2013 , 1 , 011002.
- (29) Ong, S. P.; Wang, L.; Kang, B.; Ceder, G. Li-Fe-P-O2 Phase Diagram from First Principles Calculations. Chem. Mater. 2008 , 20 , 1798 -1807.
- (30) Ong, S. P.; Cholia, S.; Jain, A.; Brafman, M.; Gunter, D.; Ceder, G.; Persson, K. a. The Materials Application Programming Interface (API): A Simple, Flexible and Efficient API for Materials Data Based on REpresentational State Transfer (REST) Principles. Comput. Mater. Sci. 2015 , 97 , 209 -215.
- (31) Bergerhoff, G.; Hundt, R.; Sievers, R.; Brown, I. D. The Inorganic Crystal Structure Data Base. J. Chem. Inf. Model. 1983 , 23 , 66 -69.
- (32) Kuhn, A.; Eger, R.; Nuss, J.; Lotsch, B. V. Synthesis and Structural Characterization of the Alkali Thiophosphates Na2P2S6, Na4P2S6, K4P2S6 and Rb4P2S6. Z. Anorg. Allg. Chem. 2014 , 640 , 689 -692.

DOI: 10.1021/acs.chemmater.5b03656

Chem. Mater.

2015, 27, 8318 - 8325

- (33) Wang, L.; Maxisch, T.; Ceder, G. Oxidation Energies of Transition Metal Oxides within the GGA+U Framework. Phys. Rev. B: Condens. Matter Mater. Phys. 2006 , 73 , 195107.
- (34) Wei, S.-H.; Zhang, S. Chemical Trends of Defect Formation and Doping Limit in II-VI Semiconductors: The Case of CdTe. Phys. Rev. B: Condens. Matter Mater. Phys. 2002 , 66 , 155211.
- (35) Miara, L. J.; Suzuki, N.; Richards, W. D.; Wang, Y.; Kim, J. C.; Ceder, G. Li-ion Conductivity in Li 9S3N. J. Mater. Chem. A 2015 , 3 , 20338 -20344.
- (36) Miara, L. J.; Richards, W. D.; Wang, Y. E.; Ceder, G. Firstprinciples Studies on Cation Dopants and Electrolyte | cathode Interphases for Lithium Garnets. Chem. Mater. 2015 , 27 , 4040 -4047.
- (37) Mo, Y.; Ong, S. P.; Ceder, G. First Principles Study of the Li10GeP2S12 Lithium Super Ionic Conductor Material. Chem. Mater. 2012 , 24 , 15 -17.
- (38) Nose ́ , S. A Unified Formulation of the Constant Temperature Molecular Dynamics Methods. J. Chem. Phys. 1984 , 81 , 511 -519.
- (39) Hoover, W. G. Canonical Dynamics: Equilibrium Phase-space Distributions. Phys. Rev. A: At., Mol., Opt. Phys. 1985 , 31 , 1695 -1697.
- (40) Jain, A.; Ong, S. P.; Chen, W.; Medasani, B.; Qu, X.; Kocher, M.; Brafman, M.; Petretto, G.; Rignanses, G.-M.; Hautier, G.; Gunter, D.; Persson, K. A. FireWorks: A Dynamic Workflow System Designed for High-throughput Applications. Concurrency Computat.: Pract. Exp. 2015 , 27 , 5037.
- (41) Deng, Z.; Radhakrishnan, B.; Ong, S. P. Rational Composition Optimization of the Lithium-Rich Li3OCl1 -x Brx Anti-Perovskite Superionic Conductors. Chem. Mater. 2015 , 27 , 3749 -3755.
- (42) Jansen, M.; Henseler, U. Synthesis, Structure Determination, and Ionic Conductivity of Sodium Tetrathiophosphate. J. Solid State Chem. 1992 , 99 , 110 -119.
- (43) Wang, Y.; Richards, W. D.; Ong, S. P.; Miara, L. J.; Kim, J. C.; Mo, Y.; Ceder, G. Design Principles for Solid-state Lithium Superionic Conductors. Nat. Mater. 2015 , 14 , 1026 -1031.
- (44) Willems, T. F.; Rycroft, C. H.; Kazi, M.; Meza, J. C.; Haranczyk, M. Algorithms and Tools for High-throughput Geometry-based Analysis of Crystalline Porous Materials. Microporous Mesoporous Mater. 2012 , 149 , 134 -141.
- (45) Martin, R. L.; Smit, B.; Haranczyk, M. Addressing Challenges of Identifying Geometrically Diverse Sets of Crystalline Porous Materials. J. Chem. Inf. Model. 2012 , 52 , 308 -318.
- (46) Murch, G. E. The Haven Ratio in Fast Ionic Conductors. Solid State Ionics 1982 , 7 , 177 -198.
- (47) Morgan, B. J.; Madden, P. A. Relationships between Atomic Diffusion Mechanisms and Ensemble Transport Coefficients in Crystalline Polymorphs. Phys. Rev. Lett. 2014 , 112 , 145901.
- (48) Bron, P.; Johansson, S.; Zick, K.; Schmedt, J.; Gu ̈ nne, D.; Dehnen, S. S.; Roling, B. Li 10 SnP2S12: An Affordable Lithium Superionic Conductor. J. Am. Chem. Soc. 2013 , 135 , 15694 -15697.

DOI: 10.1021/acs.chemmater.5b03656

Chem. Mater.

2015, 27, 8318 - 8325