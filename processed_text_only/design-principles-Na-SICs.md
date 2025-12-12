1234567890():,;

1234567890():,;

Article https://doi.org/10.1038/s41467-023-43436-3

## Design principles for sodium superionic conductors

Received: 30 August 2023

Accepted: 9 November 2023

Check for updates

Shuo Wang 1,5 , Jiamin Fu 2,3,5 , Yunsheng Liu 1 , Ramanuja Srinivasan Saravanan 1 , Jing Luo 2 , Sixu Deng 2 , Tsun-Kong Sham 3 , Xueliang Sun 2 &amp;Yifei Mo 1,4

Motivated by the high-performance solid-state lithium batteries enabled by lithium superionic conductors, sodium superionic conductor materials have great potential to empower sodium batteries with high energy, low cost, and sustainability. A critical challenge lies in designing and discovering sodium superionic conductors with high ionic conductivities to enable the development of solid-state sodium batteries. Here, by studying the structures and diffusion mechanisms of Li-ion versus Na-ion conducting solids, we reveal the structural feature of face-sharing high-coordination sites for fast sodium-ion conductors. By applying this feature as a design principle, we discover a number of Na-ion conductors in oxides, sul /uniFB01 des, and halides. Notably, we discover a chloride-based family of Na-ion conductors NaxMyCl6 (M = La -Sm) with UCl3-type structure and experimentally validate with the highest reported ionic conductivity. Our /uniFB01 ndings not only pave the way for the future development of sodium-ion conductors for sodium batteries, but also consolidate design principles of fast ion-conducting materials for a variety of energy applications.

Superionic conductor (SIC) is a unique type of materials exhibiting exceptionally high ionic conductivities, serving as critical components in a wide range of devices for energy storage and conversion, including solid-state batteries, solid-oxide fuel cells, solid-oxide electrolyzers, and ceramic membranes 1 -4 . Among them, the lithium SICs, which replace liquid electrolytes in lithium-ion batteries as solid electrolytes, enable the next-generation solid-state lithium batteries with improved safety, high energy density, and long cycle life 5 -7 . Thanks to the abundance and low cost of sodium resources, sodium SICs also attract great interest as solid electrolytes for solid-state sodium batteries 8 -10 and sodium-sulfur batteries 11 -13 , which are economical and sustainable alternatives to current lithium-ion batteries. However, only a few materials are known as SICs, impeding the further development of these novel energy technologies. A long-standing challenge in materials science is how to rationally design and discover SIC materials with high ionic conductivities.

While Na-SICs beta-alumina 14 and NASICON 15 achieved high Na ionic conductivities back in 1970s, there are many discoveries of Li-SIC families in the past two decades (Supplementary Figs. 1 and 2), including Li-garnet Li7La3Zr2O12 (LLZO) oxides 16 , Li10GeP2S12 (LGPS) 1 , Li7P3S11 sul /uniFB01 des 17 , Li-argyrodite Li6PS5X (X = Cl, Br, I) 18 , Li3MX6 (M=Y, Sc, In, Er, etc., X = Cl, Br) halides 19 -21 , with high Li ionic conductivities σ RT on the order of 1 -10 mS/cm at room temperature (RT). By understanding the Li + diffusion mechanisms in these SICs 22 -24 , scientists established multiple design principles for Li-SICs, for example, based on body-centered cubic (bcc) anion framework 25 , concerted migration 26 , and corner-sharing crystal structural framework 27 . By successfully employing these design principles, many Li-SICs, including LiZnPS4, LiTaSiO5, LiGa(SeO3)2, were discovered from /uniFB01 rst principles computation and experimentally veri /uniFB01 ed 27 -29 .

Despite the rapid advancement in the /uniFB01 eld of Li-SICs, the development and discovery of Na-SICs have been greatly lagging. Given the

1 Department of Materials Science and Engineering, University of Maryland, College Park, MD 20742, USA. 2 Department of Mechanical and Materials Engineering, University of Western Ontario, London, ON N6A 5B9, Canada. 3 Department of Chemistry, University of Western Ontario, London, ON N6A 5B7, Canada. 4 Maryland Energy Innovation Institute, University of Maryland, College Park, MD 20742, USA. 5 These authors contributed equally: Shuo Wang, Jiamin Fu. e-mail: xsun9@uwo.ca; yfmo@umd.edu

chemical similarities between Li + and Na + , a common approach of developing Na-SICs is to make Na counterparts of known Li SICs, but the outcomes are underwhelming. For example, while Li-SIC LGPS ( σ RT = 12 mS/cm) is a major breakthrough 1 , its Na-analogy Na10SnP2S12 in the same structure only achieved a much lower ionic conductivity σ RT of 0.4 mS/cm. 30 For another inspiring discovery of halide Li-SIC Li3MX6 (M=Y, Sc, In, Er, etc., X = Cl, Br) with high ionic conductivity σ RT &gt; 1 mS/cm, 19 -21 the Na-halide counterpart Na2ZrCl6 with the same hexagonal close-packed (hcp) Cl-anion framework as Li3YCl6 only exhibits a limited σ RT of 0.02 mS/cm. 31 Moreover, Li-garnet 16 and Liargyrodite 18,22 , which are successfully demonstrated as solid electrolytes for solid-state lithium batteries with excellent cell performances 32,33 , have no Na counterparts. For Na SICs, W-doped Na3SbS4 34 has a reported σ RT of 32 mS/cm, but its structures differ signi /uniFB01 cantly from its Li-counterparts. As clearly indicated by these facts, the crystal structures that yield the low energy barriers for Li + and Na + diffusion are different, but are not yet understood. It is not clear how the knowledge derived from known Na-SICs can be utilized to design and discover more Na-SICs. One cannot simply duplicate the design principles for Li-ion conductors to discover Na-ion conductors.

Given many recent discoveries in Li-SICs with σ RT higher than 1 -10 mS/cm, the discovery of Na-SICs is an under-explored opportunity. In comparison to Li-SICs, no oxide structures of Na-SICs with σ RT &gt; 1 mS/cm was discovered since 1970s (Supplementary Table 1), and the halide Na-SICs still show σ RT two orders of magnitude lower than Li-halides 31 . While Li-SICs empower solid-state lithium batteries with ever-improving cell performances, the limited availability of NaSICs has been impeding the development and innovation of sodium batteries. Thus the design principles applicable to Na-SICs are urgently needed.

In this study, we /uniFB01 rst reveal the fundamental differences between the crystal structures and diffusion mechanisms of Li + versus Na + by analyzing Li- and Na-conducting oxides, sul /uniFB01 des, and halides. Through this understanding, a unique feature of fast Na-ion conductors is identi /uniFB01 ed, and is then formulated as a design principle. Applying our design principle in a high-throughput computational screening, we discover over a dozen of structural families of Na-ion conductors with high ionic conductivities. In particular, a halide family of Na-ion conductors NaxMyCl6 (M=La -Sm), is discovered and successfully synthesized with σ RT of 1.4 mS/cm, the highest among sodium halides.

## Results

## Different site preferences for Na + and Li + in crystal structures

We /uniFB01 rst analyze and compare the structures of representative Li + and Na + SICs (Fig. 1), and identify the differences in the local geometry of Li + /Na + sites in forming the diffusion channels. There are signi /uniFB01 cant differences between the Li + /Na + site coordination number (CN), which is the number of the nearest neighbor anions (Methods). Whereas Li + occupies and migrates among tetrahedral (Tet) sites in the LGPS Li-SIC, Na + occupies sites with higher CNs of ≥ 5 in Na-SICs, such as betaalumina (CN = 6 -8), NASICON (CN = 5, 6, 8), Na3SbS4 (CN=8) (Fig. 1), and Na3PS4 (CN = 6) (Supplementary Fig. 3). The preferences of Na + for higher CN can be understood by the larger Na + radius ( r Na+ =1.02 Å) compared to Li + ( r Li+ =0.76 Å) according to Pauling ' s rules 35 . Among all Na- and Li-containing oxides, sul /uniFB01 des, and chlorides, the preference for high-CN Na + sites is general as con /uniFB01 rmed by our analyses (Supplementary Fig. 4).

## Why the design principles for Li-ion conductors cannot be duplicated for Na-ion conductors?

Hereweillustrate the design principles for Li-ion conductors cannot be duplicated for Na-ion conductors, because of the different preferred site-coordination of Na + and Li + . We investigate and simulate the energy barrier of Li + and Na + migration in the model systems with /uniFB01 xed bcc, hcp, and face-centered cubic (fcc) anion sublattices with no cation (Fig. 2a -c). In a bcc anion framework, such as in LGPS and Li7P3S11, Li + sits at tetrahedral (Tet) sites and migrates by crossing an anion-triangle bottleneck to another face-sharing Tet site, giving a low energy barrier of 0.12 eV for Li + migration (Fig. 2a). Proposed and demonstrated by Wang et al. 25 , the bcc anion framework as a design principle for Li-SICs has successfully led to the discovery of a Li-SIC LiZnPS4 29 . However, in Na-containing compounds, because of the strong preference of highCN Na + sites (Supplementary Fig. 4), it would be dif /uniFB01 cult to form percolation diffusion channels solely by Tet Na + sites, as desired in the bccanion-framework design principle. There has been no Na-containing material with the bcc-anion framework.

Fig. 1 | The ion diffusion channel in Li/Na-ion conductors. TheLi + /Na + sites (green) coordinated with O 2/S 2/Cl -anions (yellow) connected to form the diffusion channel in representative a -c sodium and d -f lithium SICs.

Fig. 2 | Lithium-ion and sodium-ion diffusion in model anion sublattices. a -c The diffusion pathways (left) and corresponding energy pro /uniFB01 le (right) for single Li + (green) and Na + (red) migration in /uniFB01 xed a body-centered cubic (bcc) S 2 -, b face-centered cubic (fcc) O 2 -, c hexagonalclose-packed(hcp) Cl -anion sublattice. The /uniFB01 xed anion lattice is set to have the octahedral (Oct) and tetrahedral (Tet) site

For the close-packed fcc and hcp anion sublattices, as commonly found in Li-chlorides and bromides SICs Li3MX6, Li + migration has low energy barriers of 0.2 -0.3 eV (Supplementary Figs. 7 and 8), which are suf /uniFB01 ciently low for fast Li-ion conductors 36 . The Na + -conducting O3-type NaMO2 (M = Co, Mn, Ni, etc.) also has an fcc anion sublattice, in which Na + occupies octahedral (Oct) sites (CN = 6) and migrates between Oct sites through intermediate Tet site (CN = 4). The intermediate Tet-site has a higher site energy than the Oct sites, as the high CN preference of Na + makes Tet-sites unfavorable, thus giving a high migration barrier of &gt;1.0 eV along the Oct-Tet-Oct pathway (Fig. 2b and Supplementary Figs. 7 and 8). In the hcp anion sublattice, as in Na2ZrCl6, this Oct-Tet-Oct pathway is also required for 3D conduction. In 1D Oct-Oct pathways along the c -axis, Na + migrates among face-sharing Oct sites across an anion-triangle bottleneck (Fig. 2c). This anion-triangle bottleneck has an appropriate size for Li + migration but is too small for Na + . As a result, the hcp Cl -anion sublattice gives a low Li + migration barrier of ~0.3 eV in Li3MX6 halide Li-SICs, but gives a high Na + migration barrier of ~0.9 eV (Fig. 2c). This explains the limited Na-ion conduction in

volume as the real materials, O3-type LiCoO2 (Oct: 12.0 Å 3 ) and NaCoO2 (Oct: 15.7 Å 3 ) for fcc O 2 -, Li2ZrCl6 (Oct: 23.8 Å 3 ) and Na2ZrCl6 (Oct: 30.9 Å 3 ) for hcp Cl -, Li10GeP2S12 (Tet: 7.4 Å 3 ) and Na10SnP2S12 (Tet: 9.6 Å 3 ) for bcc S 2 -. d -f The energy barrier of Na + (red) and Li + (green) migration as a function of site volume in the /uniFB01 xed d bcc S 2 -, e fcc O 2 -, f hcp Cl -anion sublattice.

Na2ZrCl6 with the same hcp Cl-anion framework as Li3YCl6, as reported in experiments 31 .

In summary, low-barrier Na + migration is dif /uniFB01 cult to be realized in these typical materials structures given by the design principles for Liion conductors (Fig. 2d -f). While the mechanisms, such as concerted migration 23,26 , poly-anion rotation 37,38 , and phonon lattice effect 39,40 , may further facilitate ion diffusion (see section ' High-throughput discovery for Na-ion conductors ' ), having the structural framework with the /uniFB02 at energy landscape is the /uniFB01 rst requirement to have fast ion conductors. Compared to Li + , Na + diffusion in solid crystal structures have two critical limitations. (1) Na + is unfavorable in the Tet (low-CN) sites, but typical structures give migration pathways with intermediate Tet sites, causing a high migration-energy barrier (Figs. 2b and 3). (2) Na + requires a larger bottleneck size of the diffusion channel. As quanti /uniFB01 ed in our analyses on the percolation radius p r, which is the maximum radius of a sphere that can percolate the structure across at least one dimension (Methods), Na SICs have much larger percolation radii ( p r =0.88 -1.28 Å) than Li SICs ( p r =0.52 -0.72 Å) (Supplementary Fig. 4 and Supplementary Table 2). As shown above (Fig. 2), typical

Fig. 3 | Design principles for sodium-ion conductors. a The schematics illustrate (lower) the Prism-Prism pathway between face-sharing high-CN sites in P2-type NaMO2, in comparison to (upper) the Oct-Tet-Oct pathway with intermediate Tet site in O3-type NaMO2, with (middle) the calculated energy pro /uniFB01 le for Na + migration

in the /uniFB01 xed O-anion sublattice at the lattice volume of 19.3 Å 3 per O 2 -. b The comparison of the percolation radii p r and the average CNs of Li/Na sites along the diffusion channels in Li-ion and Na-ion conductors showing a clear distinction.

crystal structures cannot offer such large bottlenecks for low-barrier Na-ion diffusion. How do the structures of Na-SICs overcome these limitations to achieve fast Na-ion conduction?

## Design principles for Na-ion conductors

Here we identify and propose the feature of face-sharing high-CN sites for fast Na-ion conductors. Speci /uniFB01 cally, the Na + diffusion channel should be comprised of only high-CN sites (CN ≥ 5) that are facesharing with a large bottleneck size to form percolation in the crystal structure. While high-CN Na + sites are general (Supplementary Fig. 4), having these high-CN sites be face-sharing is unique among crystal structures (Fig. 1 and Supplementary Fig. 3). For example, in Na betaalumina (Fig. 1), the Na + occupies the trigonal prismatic (CN = 6) or capped trigonal prismatic sites (CN = 7, 8), which are connected via face-sharing O 2-rectangle with a large bottleneck size ( p r =1.28 Å). Similarly, the P2-type NaCoO2, (Figs. 1 and 3a) which is reported to have high RT ionic conductivity up to 6 mS/cm, 41 also has a diffusion network of equivalent prismatic (Prism) Na sites connected by facesharing O 2 --rectangle with a large bottleneck size ( p r =0.92Å) (Fig. 3a). The Prism-Prism pathway has a low energy barrier of 0.26 eV for Na + migration in the /uniFB01 xed O 2anion sublattice model of the P2-type NaMO2 (Fig. 3a). By contrast, for the structures with the high-CN sites not facesharing, e.g. the fcc anion sublattice as in O3-type NaMO2, there is unfavorable Tet site as intermediate along the diffusion pathway, causing a high energy barrier of 0.76 eV at the same lattice volume of P2 (Fig. 3a). Face-sharing high-CN sites allow a direct Na + hopping among equivalent high-CN sites with a large bottleneck size and without an unfavorable intermediate Tet site (Fig. 3a), hence overcoming the aforementioned limitations of Na + diffusion.

In Fig. 3b, we compare Na-ion and Li-ion conductors for their average CN of Li + /Na + sites along the diffusion channels and their bottleneck sizes ( p r). The known Na-SICs, such as NASICON, beta-alumina, and Na3SbS4, have high average CNs ≥ 6 along their diffusion channels in their structures and also have large bottleneck size ( p r ≥ 0.88 Å) (Fig. 3b). By contrast, other Na-containing materials that do not exhibit face-sharing high-CN sites and large bottleneck size show lower conductivity. For example, O3-type NaMO2 structure and Na3YCl6 have lower average CN due to the intermediate Tet-site along their diffusion channels, and the Na2ZrCl6 with hcp anion framework has a small bottleneck size ( p r =0.73 Å). By contrast, all Li-SICs have low average CNs (Fig. 3b). For example, LGPS and Li7P3S11 with facesharing Tet sites (average CN = 4) (Figs. 1 and 3b) show the highest ionic conductivity, according to the bcc-anion-framework design principle 25 . Other non-bcc Li-SICs, such as LLZO and Li3ScCl6, have higher average CN because of the non-Tet sites along the diffusion pathways, and in general show ionic conductivities not as high as those with bcc-anion framework (Fig. 3b). This comparison chart (Fig. 3b) clearly demonstrates the key feature of face-sharing high-CN sites in Na-SICs highly distinct from Li-SICs.

## High-throughput discovery for Na-ion conductors

Here, our design principle is employed in a high-throughput computation screening to discover Na SICs (Fig. 4a), among Na-containing oxides, sul /uniFB01 des, and chlorides in the Inorganic Crystal Structure Database (ICSD) 42 . In addition to basic checks and practical considerations of materials (Methods), two screening criteria following our design principle were employed: (1) the diffusion channel consists of only high-CN sites (CN ≥ 5) that are face-sharing and are connected within a distance of 3.1 Å for oxides and 3.5 Å for sul /uniFB01 des/chlorides; (2) a large percolation radius p r &gt;0.85 Å for sul /uniFB01 des/chlorides and p r &gt;0.90Åforoxides.Using thesescreening criteria, all known sodium SICs, including NASICON, beta-alumina, Na3SbS4, Na3PS4, and Na11Sn2PS12, are identi /uniFB01 ed (Supplementary Table 3), and 35 unique structures are discovered as candidates of Na-SICs. These candidate structures are further studied by aliovalent substitution to tune Na + content, in order to enhance ionic conductivity through different mobile-ion concentration 24,28,29 or activating concerted migration mechanisms 23,29,43 ( ' Methods ' ). Those substituted materials with good stability (energy above hull &lt;100 meV/atom) are then evaluated for ionic conductivity using ab initio molecular dynamics (AIMD) simulations. Other mechanisms that may facilitate ion migration, such as concerted migration 26,37 , cooperative polyanion rotation 37,38 , and phonon effects 39,40 , if occur in the corresponding materials, would be captured in the AIMD simulations. Among them, 19 Na-SICs with σ RT &gt; 0.1 mS/cm are discovered (Table 1). Given the large statistical variances of diffusivities and the extrapolation of the Arrhenius

Fig. 4 | Discovery of sodium superionic conductors. a High-throughput screening of Na-containing oxides, sul /uniFB01 des, and chlorides. b -d The crystal structures of representative discovered sodium SICs and (inset) their diffusion channels consist of face-sharing high-CN sites. e The high experimental Na + conductivities σ RT of

relations, the results of AIMD simulations should only be interpreted as the con /uniFB01 rmation of these structure frameworks are fast Na-ion conducting if an appropriate level of aliovalent doping can be achieved. All these structures of discovered Na-SICs show the unique feature of face-sharing high-CN sites (Fig. 4b -d), con /uniFB01 rming our design principle.

Amongthediscovered oxides Na-SICs, Na0.67Ti0.33Ga4.67O8 (doped from ICSD-34196), from the tunneled alkali titan-gallate family 44 , has a low activation barrier ( E a =0.14 eV) and a high conductivity ( σ RT = 8.8 mS/cm) in AIMD simulations (Supplementary Fig. 12). Its crystal structural framework consists of connected GaO4 tetrahedra and GaO6/TiO6 (Fig. 4b), and Na + occupies capped triagonal prismatic sites (CN = 7), which are face-sharing with O-rectangle bottlenecks with a large bottleneck ( p r =1.07 Å). In another discovered Na-SIC Na1.33Mg0.67Ti7.33O16 (doped from ICSD-50764) 45 , Na + migrates between equivalent eightcoordinated sites through a large O-rectangle bottleneck ( p r =1.28 Å) (Fig. 4c), resulting in fast 1D diffusion ( E a =0.30eVand σ RT = 1.7 mS/cm). While the fast ion conduction is con /uniFB01 rmed in the bulk phases of these materials, those materials that have 1D fast diffusion channels may be susceptible to the blocking effect of defects and grain boundaries 5,46,47 , which deserve future studies.

A halide family Na x M y Cl6 with UCl3-type structure 48 with a wide range of compositions (M=lanthanides, x =0 -1, y =1.67 -2) is discovered as Na-SICs. In contrast to Li3MX6 (M=Y, Sc, In, Er, etc., X = Cl, Br) halide Li-SICs with closed-packed anion framework, the structure of NaxMyCl6 exhibits face-sharing octahedral Na + sites forming 1D diffusion channel along c -axis (Fig. 4d). These octahedral sites are distorted, thus enlarge the Cl-triangle bottleneck ( p r =1.16 Å). We evaluate NaSm2Cl6 and NaLa1.67Cl6 for Na + diffusion. In AIMD

Na0.86SmTa0.43Cl6, NaLa0.95Ta0.43Cl6, NaCe0.83Ta0.5Cl6, and NaNd0.83Ta0.5Cl6. f The Rietveld re /uniFB01 nements of synchrotron-based diffraction pattern and g the /uniFB01 tting result of the pair distribution function of NaLa0.95Ta0.43Cl6.

simulations, both exhibited fast Na + conduction along the 1D channels with a low activation barrier of 0.13 eV and 0.15 eV, respectively (Table 1 and Supplementary Fig. 14). Experimentally, we successfully synthesized this family of Na3xM2-xCl6-containing (M = La, Ce, Nd, Sm) halide Na + conductors using ball-milling methods (Methods), and acquired high ionic conductivities of 1.2, 1.4, 0.22, 0.15 mS/cm at 25 °C for Na0.86SmTa0.43Cl6, NaLa0.95Ta0.43Cl6, NaCe0.83Ta0.5Cl6, and NaNd0.83Ta0.5Cl6, respectively (Fig. 4e). The X-ray diffraction pattern (XRD) veri /uniFB01 ed the UCl3-type structure as the dominant phase (Supplementary Fig. 16). The synchrotron-based XRD re /uniFB01 nement results and pair distribution function of NaLa0.95Ta0.43Cl6 (Fig. 4f, g and Supplementary Tables 12 and 13) con /uniFB01 rmed the dominant crystalline phase NaLa1.67Cl6, and additionally NaTaCl6. The NaTaCl6 is formed as secondary phase in the inter-grain, and is known to have relatively lower ionic conductivity ( σ RT = 0.045 mS/cm). The NaLa0.95Ta0.43Cl6 composite of NaLa1.67Cl6 and NaTaCl6 achieved the highest reported σ RT of 1.4 mS/cm (Fig. 4e and Supplementary Fig. 17), a signi /uniFB01 cant improvementovertheprevioushalideNa-ionconductorNa2ZrCl6 with σ RT of 0.02 mS/cm 31 . Given that the secondary phase NaTaCl6 has a relatively lower ionic conductivity, the bulk phase of NaLa1.67Cl6 should have high ionic conductivity, in good agreement with the AIMD simulations (Supplementary Fig. 17). This discovery of a chloride NaSIC family with the highest reported σ RT is a strong validation of our design principle for fast Na-ion conductors.

## Discussion

As the key underlying mechanism of our design principle, the unique feature of face-sharing high-CN sites gives direct ion-migration

Table 1 | Sodium superionic conductors predicted by AIMD simulations

|   ICSD-IDs | Original composition      | Origin/dopant        | Doped composition             | E hull (meV/atom)   | E a (eV)              | σ at 300K (mS/cm)   | Error bound [ σ min σ max ] (mS/cm)   |
|------------|---------------------------|----------------------|-------------------------------|---------------------|-----------------------|---------------------|---------------------------------------|
|      78919 | Na 7 Y 2 P 7 O 24         | P 5+ /Mo 6+          | Na 6.5 Y 2 Mo 0.5 P 6.5 O 24  | 23                  | 0.23 ± 0.07           | 0.5                 | [0.03, 9.4]                           |
|      50764 | Na 1.7 Cr 1.7 Ti 6.3 O 16 | Cr 3+ /Ti 4+ , Mg 2+ | Na 1.33 Mg 0.67 Ti 7.33 O 16  | 31                  | 0.30±0.04             | 1.7                 | [0.3, 9.3]                            |
|      34196 | Na 0.7 Ti 0.3 Ga 4.7 O 8  | Ga 3+ /Ti 4+         | Na 0.67 Ti 0.33 Ga 4.67 O 8   | 20                  | 0.14 ± 0.05           | 8.8                 | [1.5, 53]                             |
|     108816 | NaTi 2 Ga 5 O 12          | Ga 3+ /Ti 4+         | Na 0.67 Ti 2.33 Ga 4.67 O 12  | 10                  | 0.26± 0.05            | 0.4                 | [0.04, 3.3]                           |
|     155643 | Na 0.8 Ti 1.2 Ga 4.8 O 10 | Ga 3+ /Ti 4+         | Na 0.67 Ti 1.33 Ga 4.67 O 10  | 26                  | 0.26± 0.05            | 0.8                 | [0.1, 5.0]                            |
|     163234 | Na 2 V 3 O 7              | V 4+ /V 5+           | Na 1.33 V 3 O 7               | 40                  | 0.34 ± 0.06           | 0.1                 | [0.01, 1.4]                           |
|     262512 | Na 3 Nb 4 As 3 O 19       | O 2 - /F -           | Na 2 Nb 4 As 3 O 18 F         | 43                  | 0.24± 0.07            | 1.0                 | [0.06, 17.9]                          |
|      39248 | NaTiPO 5                  | -                    | -                             | 29                  | 0.19±0.06             | 4.3                 | [0.3, 64]                             |
|      39788 | NaGeSbO 5                 | Ge 4+ /P 5+          | Na 0.75 Ge 0.75 P 0.25 SbO 5  | 29                  | 0.18 ± 0.05           | 7.2                 | [0.7, 76]                             |
|     239705 | Na 2 ZnGe 2 S 6           | Ge 4+ /Zn 2+         | Na 2.25 Zn 1.125 Ge 1.875 S 6 | 20                  | 0.25±0.06             | 0.7                 | [0.08, 6.9]                           |
|     300175 | Na 5 InS 4                | In 3+ /Sn 4+         | Na 4.5 In 0.5 Sn 0.5 S 4      | 46                  | 0.35±0.04             | 0.2                 | [0.03, 0.8]                           |
|      33236 | Na 6 ZnS 4                | Zn 2+ /Ga 3+         | Na 5.5 Zn 0.5 Ga 0.5 S 4      | 23                  | 0.32 ± 0.05           | 0.2                 | [0.02, 1.8]                           |
|      62579 | Na 5 FeS 4                | Fe 3+ /In 3+ , Sn 4+ | Na 4.75 In 0.75 Sn 0.25 S 4   | 62                  | 0.28±0.04             | 1.9                 | [0.4, 9.1]                            |
|     234888 | Na 3 ZnGaS 4              | Zn 2+ /Ga 3+         | Na 2.75 Zn 0.75 Ga 1.25 S 4   | 42                  | 0.25±0.06             | 0.5                 | [0.04, 6.2]                           |
|     200983 | Na 0.7 Ti 0.3 Cr 0.7 S 2  | Cr 3+ /Ti 4+         | Na 0.67 TiS 2                 | 3                   | 0.23±0.04             | 2.2                 | [0.4, 14]                             |
|      74928 | NaSm 2 Cl 6               | - Sm 2+ /La 3+       | - NaLa 1.67 Cl 6              | 53 9                | 0.13 ± 0.03 0.15±0.03 | 131 56.5            | [41 430] [13, 240]                    |
|      69343 | Na 2 MgCl 4               | Mg 2+ /Er 3+         | Na 1.33 Mg 0.33 Er 0.67 Cl 4  | 44                  | 0.35±0.06             | 0.1                 | [0.01, 1.3]                           |
|      11165 | Na 2 Ti 3 Cl 8            | Ti 2+ /Ti 3+         | Na 1.67 Ti 3 Cl 8             | 0                   | 0.30 ± 0.07           | 0.2                 | [0.01, 3.5]                           |

pathways among equivalent, favorable Na + sites, with small CN changes and a large bottleneck, thus giving a low energy barrier (Fig. 3a). By contrast, in the structures with Na + sites that are not face-sharing, the diffusion pathways include intermediate Tet sites, which are unfavorable for Na + and thus cause high energy barriers (Figs. 2c and 3a). In comparison, in the Li-SICs with a bcc anion framework, the diffusion channelsofface-sharing Tet-sites 25 , which are generally favorable for Li + , lead to the lowest energy barrier (Figs. 2a and 3b) 25 . The high-CN preference of Na + versus Li + explains why the structures of Li- and Na-SICs aredifferent and why the optimal Li-SIC structures cannot be duplicated as Na-SICs (Figs. 1 and 3b). Regardless of the coordination preferences of the mobile-ions, the crystal structures of fast ion conductors should form direct migration pathways among equivalent favorable sites to minimize energy barrier. Here the design principles and desired features for fast Li + and Na + conductors are consolidated and generalized.

Furthermore, this generalized design principle can unify the understanding of Li-SICs with or without bcc-anion-framework. For example, in the LLZO garnet (Fig. 1), the distorted Oct-Li sites can be considered as a split into two Tet-Li sites and thus form face-sharing Tet-sites channel for Li + diffusion (Fig. 1), similar to that in LGPS, thus shows relatively /uniFB02 at potential energy landscape. By considering this distorted site splitting into multiple Tet sites, other non-bcc-anionframeworkLi-SICs,suchasLLZO, NASICON, Li6PS5X (X= Cl, Br, I) (Fig. 1 and Supplementary Fig. 3), can be understood as face-sharing tetrahedral sites as in the bcc-anion-framework 21 . The mechanisms of site distortion are also attributed to the /uniFB02 attening of the energy landscape by raising site energies as reported in Li-SICs 26,27,43,49 . In addition, this splitting of a large local site volume into multiple equivalent sites of mobile-ions within a close distance causes the feature of enlarged Li + sites proposed by He et al. 34 , which promotes the frustration and disordering of the overall Li + sublattice 43,50 . In this study, we /uniFB01 ndintheNaSICs that site distortion has another bene /uniFB01 cial effect, that is, enlarging the bottleneck size, which is critical for the diffusion of large-radius Na + . For example, in NASCION, the Na + site is in the six-coordinated sites of distorted antiprism that form a face-sharing O-triangle bottleneck with a large bottleneck size of p r =1.03 Å. The triangle bottleneck size is enlarged by the distortion of Oct sites, in contrast to the non-distorted Oct-sites in the hcp anion sublattice (e.g., in Na2ZrCl6) which has a small bottleneck size ( p r =0.73Å). Therefore, the distortion of mobile-ion sites is a key feature of Li-/Na-SICs, bringing multiple bene /uniFB01 cial effects for fast ion diffusion.

Overall, these insights consolidate previous understandings on multiple features and mechanisms about the crystal structure frameworks of SICs. While this work focuses on the crystal structural frameworksthat give low energy barriers for ion diffusion, more complex mechanisms e.g. concerted migration, cooperation motion, and phonon-assisted hopping, may be further added to devise more detailed design principles in the future. Furthermore, the effects of grain boundaries in addition to the bulk-phase fast ion conduction should be further studied in the future. As demonstrated in designing Na-SICs, these generalized design principles can be extended and applied for other types of fast ion conductors, facilitating the future design and discovery of SICs across vast materials space.

## Methods

## DFT calculation

All the calculations were carried out using Vienna Ab initio Simulation Package (VASP) 51 based on density functional theory (DFT) using Perdew -Burke -Ernzerhof (PBE) 52 generalized gradient approximation (GGA) described by the projector-augmented-wave (PAW) approach. The convergence parameters used in all static DFT calculations were set to be consistent with the Materials Project 53 .

## Diffusion in /uniFB01 xed anion sublattice model

We performed the nudged elastic band (NEB) calculations to evaluate the migration of a single Li + /Na + in a /uniFB01 xed bcc, fcc, and hcp anion sublattice of O 2 -, S 2 -, and Cl -with no other cations as in ref. 21. The anions were /uniFB01 xed, and the background charge was set to maintain the correct valence states of mobile-ion and anions (i.e. Li + , Na + , O 2 -, S 2 -, and Cl -). The supercell models (54 atoms for bcc, 32 atoms for fcc, 36 atoms for hcp) and Γ -centered 2 × 2 × 2 k-point grids were used. Static relaxation of mobile ion (i.e. Li + and Na + ) at initial and /uniFB01 nal sites within the /uniFB01 xed anion sublattice used an energy convergence criterion of 10 -5 eV and a force convergence criterion of 10 -2 eV/Å. A total of seven images interpolated between initial and end structures were used for the NEB calculations. In the NEB calculations, the anions were /uniFB01 xed, and the energy and force convergence criterion remained the same as the static relaxation of initial and /uniFB01 nal structures.

The lattice parameters of the bcc, fcc, and hcp anion model were set to have the same site volume as representative Li-SICs (i.e., O3-type LiCoO2, Li2ZrCl6, Li10GeP2S12) and Na-SICs (i.e., O3-type NaCoO2, Na2ZrCl6, Na10SnP2S12) as shown in Fig. 2a -c. The /uniFB01 xed anion sublattices extracted from real materials of P2- and O3-type NaCoO2 are used in Fig. 3a. To consider the effects of changing volumes on Li + /Na + migration, the models with a varying range of lattice parameters and lattice volume following the volume distribution of the Li/Na-containing compounds in the ICSD (Supplementary Fig. 6) were also conducted (Fig. 2d -f and Supplementary Figs. 7 and 8).

## Topological analysis of crystal structure frameworks

The topological analysis was performed to identify percolation radius, Nasites, site coordination, and diffusion network using in Zeo++ 54 as in the previous study 43 . The topological analysis was performed to the crystal structural framework by removing all Li/Na ions from the crystal structures. The analyses were performed using the crystal ionic radii for each ion species in Pymatgen 55 . For sites with mixed partial occupancy of multiple cations, the smallest ionic radius of these cations was used. The percolation radius was calculated as the maximumradius of a sphere that can percolate the crystal structure across at least one direction.

The Na sites in the crystal structural framework were identi /uniFB01 ed as follows. The structural framework was decomposed by the Voronoi -Dirichlet partition algorithm using the ions as the centers of the polyhedrons as implemented in Zeo++ 54 . A Voronoi node was the vertices shared by the polyhedrons and corresponded to the center of a local void, which may be possible mobile-ion sites. These Voronoi nodes were further screened by the chemical environments suitable for Na + occupancy using the criteria based on the coulombic repulsion and bond valence (BV). Any nodes close to other non-Na cations were excluded, with the cutoff distance set to 2.6 Å for oxides/sul /uniFB01 des and 2.8 Å for chlorides. The BV was calculated for each Voronoi node, and those with BV in the range of 0.3 -1.5 were kept. The distance cut-off and BV range were determined by analyzing Na-containing oxide, sul /uniFB01 de, and chlorides (Supplementary Figs. 10 and 11). Finally, the Na nodes were grouped into a site if their distance was less than 1.6 Å.

The site coordination number for a given possible Na site was calculated as the number of neighboring anions (i.e. O 2 -, S 2 -, and Cl -) using Voronoi decompositionwith solid angleweights as implemented in CrystalNN algorithm 56 . The site volumes were calculated by constructing a convex hull of identi /uniFB01 ed coordinating anions (Supplementary Fig. 5).

## High-throughput screening of Na-ion conductors

Step 1. Basic Materials Check. We /uniFB01 rstly /uniFB01 ltered all the Na-containing oxide, sul /uniFB01 de and chloride compounds in the ICSD (2017 version), and excluded the compounds with any of following attributes: binary compounds;containingmorethanoneanionspecies;co-occupancyof Na with other elements; containing anions with disordering or partial occupancy; containing water molecules; having elements with no valence or abnormal valences that have no ionic radii information in the defaulted table of pymatgen 55 ; the compounds are not charge neutral; containing more than 300 atoms. After this step of basic materials checks, there were a total of 2673 oxides, 153 sul /uniFB01 des, and 80 chlorides for further screening.

Step 2. Percolation radius. Considering the bottleneck size of diffusion channels in the crystal structure, we identify the structures with large percolation radii of pr &gt;0.9Å for oxides and pr &gt;0.85Å for sul /uniFB01 des and chlorides. The cut-off values were identi /uniFB01 ed based on the key parameters of the crystal frameworks of known Na-ion conductors (Supplementary Table 2).

Step 3. Face-sharing high-CN sites. For a structure to pass the screening, the diffusion network should only consist of high-CN Na sites with CN ≥ 5. These high-CN Na sites should also connect with each other via face sharing within the cut-off distance to form percolation. The cut-off distance was set to 3.1 Å for oxides and 3.5 Å for sul /uniFB01 des and chlorides.

Step 4. Unique structures. We grouped the compounds with the same crystal structural framework regardless of the cation species using the structure matching algorithm in Pymatgen 55 . In the candidate list (Supplementary Tables 5, 7, and 9), one compound was evaluated to represent a structural framework.

Step 5. Practical consideration. We excluded the compounds containing Au, U, (CO3) 2, (SO4) 2. We excluded all known Na-SICs and cathode materials, and the Na-Al-O ternary systems. For AIMD simulations, we excluded the compounds with large supercells containing &gt; 300 atoms.

Step 6. AIMD screening. For each crystal structural framework identi /uniFB01 ed in the candidate list, the representative compound was selected to evaluate Na + diffusion. Aliovalent substitution was performed to change Na content in the compound. For each framework, Na content was changed to have the ratio of the number of Na ions over the total number of identi /uniFB01 ed Na sites to the target range of 0.3 -0.7. The energy above the hull for doped composition was calculated, and those with good stability of the energy above the hull &lt;100meV/atom were further evaluated for Na + diffusion.

AIMD simulations were /uniFB01 rst performed at two temperatures, 900K and 1150K for oxides and sul /uniFB01 des and 700 K and 900 K for chlorides, as an initial screening following Ref. 43 The materials that melted during AIMD simulations were excluded. For materials with extrapolated Na + conductivity &gt;0.1 mS/cm at 300 K were further studied by AIMD simulations at more temperatures. The ionic conductivity was evaluated according to the Arrhenius relation,

<!-- formula-not-decoded -->

where σ is conductivity, T is temperature , E a is the activation energy, σ 0 is the pre-exponential factor, and k B is the Boltzmann constant

## Ab initio molecular dynamics simulation

We performed AIMD simulations to study ionic diffusion in supercell models with lattice parameters near or larger than 10 Å. Non-spin mode, a single Γ -centered k -point, and a time step of 2 fs were used. In each simulation, the initial temperature was set to 100 K and then the structures were heated to the target temperatures at a constant rate by velocity scaling during a period of 2 ps. All simulations adopted the NVT ensemble with Nosé-Hoover thermostat 57 . The diffusivity D was calculated as the mean square displacement (MSD) over the time interval Δ t ,

<!-- formula-not-decoded -->

where d is the dimension of the diffusion, N is the total number of diffusion ions, r i ( t ) is the displacement of the i -th ion at time t . The ionic conductivity was calculated according to the Nernst-Einstein relationship,

<!-- formula-not-decoded -->

where n is the mobile ions volume density and q is the ionic charge. Given that the ion hopping is a stochastic process, the statistical deviations of the conductivity were evaluated according to the scheme established in our previous work 58 . The total time duration of AIMD simulations was within the range of 40 -400ps until the total meansquare-displacement reach over 1000 -2000Å 2 and the ionic diffusivity converged within a relative standard deviation between 20% and 40% for most data points.

## Experimental methods

Synthesis . All preparation processes and sample treatments were carried out in an Ar/uniFB01 lled glovebox (O2 &lt; 1 ppm, H2O &lt; 1 ppm). The familyof Na3 x M2x Cl6-contained halide conductors (M = La, Ce, Nd, Sm) were synthesized by ball-milling the starting materials of LaCl3 (Sigma Aldrich, 99.9%), SmCl3 (Sigma Aldrich, 99.9%), NdCl3 (Sigma Aldrich, 99.8%), CeCl3 (Sigma Aldrich, 99.9%), TaCl5 (Sigma Aldrich, 99.9%) and NaCl (Sigma Aldrich, reagent grade) according to the stoichiometric ratios. For ball-milling synthesis, the mixture of precursors was sealed in a zirconia jar (100 mL) under vacuum and was mechanically milled using a plenary high-energy ball-milling machine (PM200, RETSCH) with zirconia balls ( ϕ =5, 7, and 10 mm, balls/precursors = 40:1 w/w) for 60 cycles. The ball-milling process included 10-min milling and 5-min resting for each cycle. The ball-milling speed was 500 rpm. The as-prepared samples were collected in the glovebox for ionic conductivity measurements.

## Structure characterization

Lab-based X-ray diffraction (XRD) measurements were performed on Bruker AXS D8 Advance with Cu K α radiation ( λ = 1.5406 Å). Kapton tape was used to cover the sample holder to prevent air exposure. Synchrotron-based powder diffraction patterns were collected using the Brockhouse High Energy Wiggler beamline at the Canadian Light Source (CLS) with a wavelength of 0.3497 and 0.2077 Å. The samples were loaded into 0.8 mm inner diameter polyimide capillaries and sealed with epoxy in an Ar/uniFB01 lled glove box. The X-ray diffraction Rietveld re /uniFB01 nement and pair distributed function /uniFB01 ttings were conducted by GSAS-2 59 and PDFgui software 60 .

## EIS measurements of ionic conductivity

The temperature-dependent ionic conductivities of prepared solid electrolytes were obtained via the EIS measurements of model cells on a multichannel potentiostat 3/Z (German VMP3). The temperature range was between -25 and 55 °C. The applied frequency range was 1 Hz to 7 MHz and the voltage amplitude was 20 mV. The test cell was fabricated as follows: 100 -120mg of the electrolytes were pressed (~300 MPa) into a pellet (diameter: 1 cm, thickness ~0.5 -0.7 mm). About 5 mg of acetylene black carbon was then spread onto both sides of the pellet and pressed with ~150 MPa.

## Data availability

All data are provided in the paper and its Supplementary Information. Additional information is available from the corresponding authors upon request. Source data are provided with this paper.

## Code availability

The code used in this study is available from the corresponding author upon request.

## References

1. Kamaya, N. et al. A lithium superionic conductor. Nat. Mater. 10 , 682 -686 (2011).
2. Zhou, Y. et al. Strongly correlated perovskite fuel cells. Nature 534 , 231 -234 (2016).
3. Janek, J. &amp; Zeier, W. G. A solid future for battery development. Nat. Energy 1 , 16141 -16144 (2016).
4. Wachsman, E. D. &amp; Lee, K. T. Lowering the temperature of solid oxide fuel cells. Science 334 , 935 -939 (2011).
5. Famprikis, T., Canepa, P., Dawson, J. A., Islam, M. S. &amp; Masquelier, C. Fundamentals of inorganic solid-state electrolytes for batteries. Nat. Mater. 18 , 1278 -1291 (2019).
6. Bachman, J. C. et al. Inorganic solid-state electrolytes for lithium batteries: mechanisms and properties governing ion conduction. Chem. Rev. 116 , 140 -162 (2016).
7. Zhao, Q., Stalin, S., Zhao, C. Z. &amp; Archer, L. A. Designing solid-state electrolytes for safe, energy-dense batteries. Nat. Rev. Mater. 5 , 229 -252 (2020).
8. Zhao, C. et al. Solid-state sodium batteries. Adv. Energy Mater. 8 , 1703012 -1703012 (2018).
9. Zhou, W., Li, Y., Xin, S. &amp; Goodenough, J. B. Rechargeable sodium all-solid-state battery. ACS Central Sci. 3 , 52 -57 (2017).
10. Zhang, Z. et al. Na11Sn2PS12: a new solid state sodium superionic conductor. Energy Environ. Sci. 11 , 87 -93 (2018).
11. Ellis, B. L. &amp; Nazar, L. F. Sodium and sodium-ion energy storage batteries. Curr. Opin. Solid State Mater. Sci. 16 , 168 -177 (2012).
12. Wei, S. et al. A stable room-temperature sodium -sulfur battery. Nat. Commun. 7 , 1 -10 (2016).
13. Hueso, K. B., Armand, M. &amp; Rojo, T. High temperature sodium batteries: status, challenges and future trends. Energy Environ. Sci. 6 , 734 -749 (2013).
14. Yao, Y.-F. Y. &amp; Kummer, J. T. Ion exchange properties of and rates of ionic diffusion in beta-alumina. J. Inorg. Nucl. Chem. 29 , 2453 -2475 (1967).
15. Goodenough,J. B., Hong, H.-P. &amp; Kafalas, J. A. Fast Na + -ion transport in skeleton structures. Mater. Res. Bull. 11 , 203 -220 (1976).
16. Murugan, R., Thangadurai, V. &amp; Weppner, W. Fast lithium ion conduction in garnet -type Li7La3Zr2O12. Angew. Chem. Int. Ed. 46 , 7778 -7781 (2007).
17. Yamane, H. et al. Crystal structure of a superionic conductor, Li 7P3S11. Solid State Ion. 178 , 1163 -1167 (2007).
18. Deiseroth, H. J. et al. Li 6PS5X: a class of crystalline Li -rich solids with an unusually high Li + mobility. Angew. Chem. Int. Ed. 47 , 755 -758 (2008).
19. Liang, J. et al. Site-occupation-tuned superionic LixScCl3+x halide solid electrolytes for all-solid-state batteries. J. Am. Chem. Soc. 142 , 7012 -7022 (2020).
20. Li, X. et al. Air-stable Li3InCl6 electrolyte with high voltage compatibility for all-solid-state batteries. Energy Environ. Sci. 12 , 2665 -2671 (2019).
21. Asano, T. et al. Solid halide electrolytes with high lithium-ion conductivity for application in 4 V class bulk-type all-solid-state batteries. Adv. Mater. 30 , 1803075 -1803075 (2018).
22. Morgan, B. J. Mechanistic origin of superionic lithium diffusion in anion-disordered Li6PS5 X argyrodites. Chem. Mater. 33 , 2004 -2018 (2021).
23. Deng, Y. et al. Structural and mechanistic insights into fast lithiumion conduction in Li4SiO4 -Li3PO4 solid electrolytes. J. Am. Chem. Soc. 137 , 9136 -9145 (2015).
24. Catlow, C. R. A. Atomistic mechanisms of ionic transport in fast-ion conductors. J. Chem. Soc. Faraday Trans. 86 , 1167 -1176 (1990).
25. Wang, Y. et al. Design principles for solid-state lithium superionic conductors. Nat. Mater. 14 , 1026 -1031 (2015).
26. He, X., Zhu, Y. &amp; Mo, Y. Origin of fast ion diffusion in super-ionic conductors. Nat. Commun. 8 , 15893 -15893 (2017).
27. Jun, K. et al. Lithium superionic conductors with corner-sharing frameworks. Nat. Mater. 21 , 924 -931 (2022).
28. Xiong, S. et al. Computation -guided design of LiTaSiO5, a new lithium ionic conductor with sphene structure. Adv. Energy Mater. 9 , 1803821 -1803821 (2019).
29. Richards, W. D., Wang, Y., Miara, L. J., Kim, J. C. &amp; Ceder, G. Design of Li1+2xZn1 -xPS4, a new lithium ion conductor. Energy Environ. Sci. 9 , 3272 -3278 (2016).
30. Richards, W. D. et al. Design and synthesis of the superionic conductor Na10SnP2S12. Nat. Commun. 7 , 11009 -11009 (2016).
31. Kwak, H. et al. Na2ZrCl6 enabling highly stable 3 V all-solid-state Na-ion batteries. Energy Storage Mater. 37 , 47 -54 (2021).
32. Dixit, M. B. et al. Polymorphism of garnet solid electrolytes and its implications for grain-level chemo-mechanics. Nat. Mater. 21 , 1298 -1305 (2022).

33. Tan, D. H. S. et al. Carbon-free high-loading silicon anodes enabled by sul /uniFB01 de solid electrolytes. Science 373 , 1494 -1499 (2021).
34. Hayashi, A. et al. A sodium-ion sul /uniFB01 de solid electrolyte with unprecedented conductivity at room temperature. Nat. Commun. 10 , 5266 -5266 (2019).
35. Shannon, R. D. Revised effective ionic radii and systematic studies of interatomic distances in halides and chalcogenides. Acta Crystallogr. Sect. A Cryst. Phys. Diffr. Theor. Gen. Crystallogr. 32 , 751 -767 (1976).
36. Wang, S. et al. Lithium chlorides and bromides as promising solidstate chemistries for fast ion conductors with good electrochemical stability. Angew. Chem. Int. Ed. 58 , 8039 -8043 (2019).
37. Adams, S. &amp; Rao, R. P. Structural requirements for fast lithium ion migration in Li10GeP 2S12. J. Mater. Chem. 22 , 7687 -7691 (2012).
38. Zhang, Z. &amp; Nazar, L. F. Exploiting the paddle-wheel mechanism for the design of fast ion conductors. Nat. Rev. Mater. 7 , 389 -405(2022).
39. Ren, Q. et al. Extreme phonon anharmonicity underpins superionic diffusion and ultralow thermal conductivity in argyrodite Ag8SnSe6. Nat. Mater . https://doi.org/10.1038/s41563-023-01560-x (2023)
40. Muy, S., Schlem, R., Shao-Horn, Y. &amp; Zeier, W. G. Phonon -ion interactions: designing ion mobility based on lattice dynamics. Adv. Energy Mater. 11 , 2002787 (2021).
41. Mo, Y., Ong, S. P. &amp; Ceder, G. Insights into diffusion mechanisms in P2 layered oxide materials by /uniFB01 rst-principles calculations. Chem. Mater. 26 , 5208 -5214 (2014).
42. Hellenbrandt, M. The inorganic crystal structure database (ICSD) -present and future. Crystallogr. Rev. 10 , 17 -22 (2004).
43. He, X. et al. Crystal structural framework of lithium super -ionic conductors. Adv. Energy Mater. 9 , 1902078 -1902078 (2019).
44. Armand, M. B., Chabagno, J. M. &amp; Duclot, M. J. in Fast Ion Transport in Solids (eds Vashishta, P., Mundy, J. N. &amp; Shenoy, G. K.) 131 (North Holland, 1979).
45. Michiue, Y., Sato, A. &amp; Watanabe, M. Low-temperature phase of sodium priderite, NaxCrxTi8 -xO16, with a monoclinic hollandite structure. J. Solid State Chem. 145 , 182 -185 (1999).
46. Dawson,J. A., Canepa, P., Famprikis, T., Masquelier, C. &amp; Islam, M. S. Atomic-scale in /uniFB02 uence of grain boundaries on Li-ion conduction in solid electrolytes for all-solid-state batteries. J. Am. Chem.Soc. 140 , 362 -368 (2018).
47. Dawson, J. A. et al. Toward understanding the different in /uniFB02 uences of grain boundaries on ion transport in sul /uniFB01 de and oxide solid electrolytes. Chem. Mater. 31 , 5296 -5304 (2019).
48. Zachariasen, W. H. The UCl3 type of crystal structure. J. Chem. Phys. 16 , 254 -254 (1948).
49. Di Stefano, D. et al. Superionic diffusion through frustrated energy landscape. Chem 5 , 2450 -2460 (2019).
50. Zhang, Y. et al. Unsupervised discovery of solid-state lithium ion conductors. Nat. Commun. 10 , 1 -7 (2019).
51. Kresse, G. &amp; Furthmüller, J. Ef /uniFB01 cient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B 54 , 11169 -11169 (1996).
52. Blöchl, P. E. Projector augmented-wave method. Phys. Rev. B 50 , 17953 -17953 (1994).
53. Jain, A. et al. Commentary: The Materials Project: a materials genome approach to accelerating materials innovation. Apl. Mater. 1 , 11002 -11002 (2013).
54. Willems, T. F., Rycroft, C. H., Kazi, M., Meza, J. C. &amp; Haranczyk, M. Algorithms and tools for high-throughput geometry-based analysis of crystalline porous materials. Microporous Mesoporous Mater. 149 , 134 -141 (2012).
55. Ong, S. P. et al. Python Materials Genomics (pymatgen): a robust, open-source python library for materials analysis. Comput. Mater. Sci. 68 , 314 -319 (2013).
56. Pan, H. et al. Benchmarking coordination number prediction algorithms on inorganic crystal structures. Inorg. Chem. 60 , 1590 -1603 (2021).
57. Nosé, S. A uni /uniFB01 ed formulation of the constant temperature molecular dynamics methods. J. Chem. Phys. 81 , 511 -519 (1984).
58. He,X., Zhu, Y., Epstein, A. &amp; Mo, Y. Statistical variances of diffusional properties from ab initio molecular dynamics simulations. npj Comput. Mater. 4 , 18 -18 (2018).
59. Toby, B. H. &amp; Von Dreele, R. B. GSAS-II: the genesis of a modern open-source all purpose crystallography software package. J. Appl. Crystallogr. 46 , 544 -549 (2013).
60. Farrow, C. et al. PDF /uniFB01 t2 and PDFgui: computer programs for studying nanostructure in crystals. J. Phys. Condens. Matter 19 , 335219 (2007).

## Acknowledgements

Y.M. acknowledge the funding support from National Science Foundation Award# 2118838 and the computational facilities from the University of Maryland supercomputing resources. X.S. thanks the funding support from the Natural Sciences and Engineering Research Council of Canada (NSERC), Canada Research Chair Program (CRC), and University of Western Ontario. X.S. also appreciates the help of the BXDS beamline at Canadian Light Source.

## Author contributions

Y.M. oversaw the overall project. Y.M. and S.W. conceived the project. S.W. designed and performed the computation and analyses. J.F., J.L., and S.D. fabricated the samples of the materials and carried out the experiments, characterizations, and data analyses, supervised by X.S. and T.S. S.W. and Y.M. prepared the manuscript with the help of all authors. All authors contributed to the discussions and revisions of the manuscript.

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-023-43436-3.

Correspondence and requests for materials should be addressed to Xueliang Sun or Yifei Mo.

Peer review information Nature Communications thanks the anonymous reviewers for their contribution to the peer review of this work. A peer review /uniFB01 le is available.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher ' s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional af /uniFB01 liations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article ' s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article ' s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by/4.0/.

- ©The Author(s) 2023