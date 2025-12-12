Contents lists available at ScienceDirect

## Electrochimica Acta

journal homepage: www.elsevier.com/locate/electacta

## Theory of coupled ion-electron transfer kinetics

Dimitrios Fraggedakis a , ∗ , Michael McEldrew a , Raymond B. Smith a , Yamini Krishnan a , Yirui Zhang b , Peng Bai a , c , William C. Chueh d , Yang Shao-Horn b , e , Martin Z. Bazant a , f , ∗

a Department of Chemical Engineering, Massachusetts Institute of Technology, Cambridge, MA, 02139 USA

b Departments of Mechanical Engineering, Massachusetts Institute of Technology, Cambridge, MA, 02139 USA

c Department of Energy, Environmental and Chemical Engineering, Washington University, Saint Louis, MO, 63130 USA

d Department of Materials Science and Engineering, Stanford University, Stanford, CA, 94305, USA

- e Department of Materials Science and Engineering, Massachusetts Institute of Technology, Cambridge, MA, 02139 USA

f Department of Mathematics, Massachusetts Institute of Technology, Cambridge, MA, 02139 USA

## a r t i c l e i n f o

Article history: Received 26 July 2020 Revised 3 November 2020 Accepted 4 November 2020 Available online 16 November 2020

## Keywords:

Coupled ion-electron transfer Ion intercalation Li-ion batteries Memristors Neuromorphic computing

## 1. Introduction

Charge transfer reactions are paramount in biology, e.g. in protein-protein electron transfer [1-3] and photosynthesis [4,5] , and electrochemical engineering, e.g. in water desalination [610] and energy conversion and storage [11-15] . Well established models, such as Butler-Volmer (BV) and Marcus kinetics, are available to describe the rate of charge transfer carried by ions or electrons [12,16-18] , respectively, as sketched in Fig. 1 . Here, we consider concerted or coupled ion-electron transfer reactions, which have received much less attention and lack a simple rate formula.

Efforts to describe charge-transfer reactions can be traced to the early twentieth century. Building on Tafel's discovery of exponential overpotential dependence for Faradaic reaction rates [19] , the seminal work of Butler [20] and Volmer [21] introduced the phe-

∗ Corresponding

authors.

E-mail addresses: dimfraged@gmail.com (D. Fraggedakis), bazant@mit.edu (M.Z. Bazant).

https://doi.org/10.1016/j.electacta.2020.137432

## a b s t r a c t

The microscopic theory of chemical reactions is based on transition state theory, where atoms or ions transfer classically over an energy barrier, as electrons maintain their ground state. Electron transfer is fundamentally different and occurs by tunneling in response to solvent fluctuations. Here, we develop the theory of coupled ion-electron transfer, in which ions and solvent molecules fluctuate cooperatively to facilitate non-adiabatic electron transfer. We derive a general formula of the reaction rate that depends on the overpotential, solvent properties, the electronic structure of the electron donor/acceptor, and the excess chemical potential of ions in the transition state. For Faradaic reactions, the theory predicts curved Tafel plots with a concentration-dependent reaction-limited current. For moderate overpotentials, our formula reduces to the Butler-Volmer equation and explains its relevance, not only in the well-known limit of large electron-transfer (solvent reorganization) energy, but also in the opposite limit of large iontransfer energy. The rate formula is applied to Li-ion batteries, where reduction of the electrode host material couples with ion insertion. In the case of lithium iron phosphate, the theory accurately predicts the concentration dependence of the exchange current measured by in operando X-Ray microscopy without any adjustable parameters. These results pave the way for interfacial engineering to enhance ion intercalation rates, not only for batteries, but also for ionic separations and neuromorphic computing.

© 2020 Elsevier Ltd. All rights reserved.

nomenological BV equation, which is by far the most widely used rate expression in electrochemistry [17,18,22] and electrochemical engineering [11,23] . The classical derivation of the BV equation [22] is based on Eyring's transition-state theory [24] applied to ion transfer (IT), Fig. 1 (a) [23] . The IT transition state is assumed to be fixed at a distance α d from the reduced state, where d is the distance from the oxidized state. Electron transfer (ET) is not treated explicitly in this picture, but the IT rate expression is sometimes interpreted to imply that a fraction of electrons α is transferred on the reduced side of the transition-state barrier, while the remaining fraction 1 -α is transferred on the oxidized side in order to complete the reaction [17,25] . The BV equation has recently been generalized for consistency with non-ideal thermodynamics [12] , e.g. for phase transformations driven by charge transfer reactions [26] , setting the stage for our analysis below.

Marcus was the first to recognize that classical transition state theory cannot be applied to electrons [27] . Instead, he proposed that ET occurs iso-energetically in response to the environment fluctuations of the RedOx species, whose energy landscape is mod-

Fig. 1. Physical pictures of ion (a) and electron (b) transfer, in terms of landscapes of the excess chemical potential µ ex . In both cases, O , TS and R correspond to the oxidized, transition, and reduced states, respectively. (a) For ion transfer, the reaction coordinate ξ is the the distance of the ion from its reduces state, e.g. the electrode where the charge transfer takes place. Under an applied overpotential η , a cation, for example, is attracted towards the surface of the electrode, where at some distance (red point) towards the electrode it is reduced by an electron (dashed green arrow). This distance is described by the charge transfer coe ffi cient α . (b) For electron transfer, the reaction coordinate x corresponds to the environment polarization coordinate. For an electron transfer to occur, both the reactant and product states need to be at the same energy (orange point) where the electron is able to tunnel between the two states. The reorganization step, which is related to the reorganization energy λ of the environment, is denoted using the blue shade. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

eled as intersecting parabolas in terms of the solvent reorganization coordinate [27-33] , Fig. 1 (b). In the case of outer sphere ET reactions, Marcus related the ET activation energy barrier to the solvent reorganization energy λ , which is dominated by the dielectric polarization of the medium. Soon afterwards, Hush derived a similar rate expression for adiabatic inner sphere ET reactions, where the electrons transfer in response to molecular vibrations, and thus the reorganization energy is dominated by the phonons of the molecular complex [34-37] . Notably, the MarcusHush rate expression reduces to the BV equation for overpotentials much smaller than the reorganization energy [18] .

The quantum mechanical theory of ET, pioneered by Levich, Dogonadze, Chizmadzhev, Christov, and Kuznetsov [16,38-42] , also leads to Marcus-Hush rate expressions. In general, electron transfer depends on the interaction of the electrons that participate in the reaction with the environment of the particular RedOx active sites [16,43] . When fluctuations of the environment are large enough to make the reduced and oxidized states iso-energetic, ET occurs by tunneling with a probability controlled by electronic coupling between the RedOx states. In the case of Faradaic ET reactions, all available electrons can participate in the reaction, so the Marcus-Hush rate must be integrated over the Fermi distribution of electron energies in the band structure [44] . Thus, for the typical case of a metallic electrode [45-47] , the energy landscape of the electron donor is described by a family of parabolas, Fig. 1 (b).

Classical theories assume either IT or ET is the rate limiting step, but there are situations where both processes occur simultaneously. The characteristic example is coupled proton-electron transfer (CPET) [48-53] . The theory of CPET is based on the ideas of electron transfer, where the fluctuating environment of the RedOx species determines how the reaction will proceed. In addition to the isoenergetic requirement for the ET part, the initial and final vibrational state of the proton bond with the molecular complex need also to be at the same energy before the proton transfer occurs [51,54,55] . Once the isoenergetic conditions for both the ET

and PT are satisfied, both the electron and the proton are transferred through tunneling. Although the mathematical framework and concepts behind CPET are mature [56-58] and validated several times [59] , there has still been little attention paid to the limit where the ions behave classically and only the electrons are quantum particles [12,60] , as in the case of ion intercalation [61] .

Ion intercalation has been traditionally modeled by the BV equation in the context of batteries [11,62] without any mention to electron transfer. Additionally, ion intercalation is used for selective separations and water desalination [7,9,10,63] , where the process is thought to be purely classical and dominated by IT. However, it has been recently shown [61] that electron transfer can be the limiting step in ion intercalation in the context of Li-ion batteries. Therefore, a complete microscopic picture of ion intercalation is still lacking, as both IT and ET seem to be important during the process.

In this work, we develop the fundamental theory of coupled ion-electron transfer (CIET) reactions, in which ions and electrons are transferred through a concerted mechanism. Starting from the framework of far-from equilibrium chemical thermodynamics [64] applied to charge-transfer reactions [12] , we derive a simple, closed-form reaction-rate formula, which takes into account: (i) the non-ideal thermodynamics of the reactants and products, (ii) ionic configurational entropy and other non-idealities in the transition state, (iii) the electrostatic coupling between the ions and the electrons, (iv) the tunneling of electrons, (v) the solvation effects of the ions near interfaces, and (vi) the electronic density of states and quantum statistics of the electron donor. Interestingly, our formula reduces to the BV equation in two different limits of moderate overpotentials, when either ET or IT is dominant. In the case of ion intercalation coupled to a metallic electron donor, our formula reduces to Marcus-Hush-Chidsey (MHC) kinetics of ET with a new pre-factor accounting for the crowding of ions during IT. The theory accurately predicts the exchange current versus concentration for LiFePO 4 (LFP) obtained directly from x-ray imaging experiments [13] , as well as the chronoamperometry data [61] , and paves the way for predictive modeling of Li-ion battery reaction kinetics [65] .

## 2. Physical picture

In order to develop a general physical picture of coupled ionelectron transfer, we consider a medium consisting of neutral particles, unpaired cations and electroneutral cation-anion pairs (polarons), Fig 2 (a). The concerted ion-electron transfer requires both the ions and the electrons that participate in the reaction to be transferred together to form the product complex. In the present picture, the electron transfer part corresponds to the reduction of a neutral site by either delocalized (coming from a metal) or localized (from dopants or impurities) electrons, and the ion transfer corresponds to the physical transfer of the cation nearby the reduced site. We assume that the individual completion of the steps (ion or electron transfer) cannot take place due to the prohibitively large electrostatic energy required to separate the cation and the reduced site from their final state.

The physical picture of Fig. 2 (a) can be translated into the energy landscape shown in Figs. 2 (b) &amp; (c). Our representation of coupled ion-electron transfer is a combination of the classical ion [12] and electron [66] transfer treatments as described in Figs. 1 . More specifically, the ionic coordinate is equivalent to the distance travelled by the ion to reach its final state ξ , and the electron coordinate is the solvent polarization one x . Given the non-adiabatic nature of electron transfer, the oxidized and reduced states are described by different parabolic function for constant values of ξ , Figs. 2 (b) &amp; (c).

Fig. 2. Physical and energy picture of coupled ion-electron transfer. (a) Schematic representation of an amorphous medium that consists of neutral particles, reduced, and oxidized species. At first, the transferring ion starts moving towards the site that is going to be reduced (blue shade), where its environment becomes reorganized as a result of thermal fluctuations. Once the environment of the reactant and product states have similar energies and also when the ion is at the transition state (TS), an electron coming either from a metal or a dopant will tunnel and reduce the site. Concurrently with this event, an ion-polaron pair is formed. (b) &amp; (c) Energy landscape drawn as a contour plot and a three-dimensional surface in terms of the ionic ξ and polarization x coordinates. There are four minima, two of which correspond to the RedOx states. These are accessed only through a single point (yellow diamond) that has the lowest energy barrier and allows the transfer of both ions and electrons at their product state. In the contour plot, the minimum energy path is depicted with the red dashed line, while in the three-dimensional surface with the solid and thinly-dashed red lines. Additionally, in the three-dimensional landscape the solid and thinly-dashed green are the intersection of the energy landscape with x -normal planes at x = x O and x = x R , and finally, the thick-dashed red is the projection of the minimum energy path on µ ex = 0 . (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

We consider the energy landscape to have the four local minima as clearly shown in the contour plot of Fig. 2 (b). These minima represent the following cases: i) at ( x , ξ ) = ( x O , ξ O ) both ions and electrons are in reactant/oxidized state, ii) at ( x , ξ ) = ( x R , ξ R ) both ions and electrons are in product/reduced state, iii) at ( x , ξ ) = ( x O , ξ R ) the ion transfer is completed, but the electron transfer has not occurred yet, iv) at ( x , ξ ) = ( x R , ξ O ) the electron has tunneled in the reduced state, while the ion has not moved from its initial position. The system can explore the last two minima only when the driving force (overpotential) is large enough to exceed the electrostatic attraction between the ion and the reduced complex in their final state.

According to Fig. 2 (b) &amp; (c), the non-adiabatic surfaces intersect each other along the dark orange line. Across the intersection, electrons can tunnel from the reactant to the product state as their environments are at the same energy state. However, only one point along the electron transfer line corresponds to the minimum energy barrier (yellow diamond -CIET), where both the ion and the electron transfers occur at the same time.

Similar ideas to coupled ion-electron transfer have been previously demonstrated for electrocatalytic adsorption reactions, where solvated ions transfer at the electrode interface where an electron transfer occurs and covalent bonding takes place [60,67-70] . Another example is that of non-adsorbing RedOx reactions near the electrodes. In that case, the ions have to work against the formed double layer to reach the electrified interface, where along their way an electron is transferred to the ion which consequently moves back to the solution [52,71-73] . In both examples, the con- certed nature of the process translates into a multidimensional energy landscape in the reaction coordinates [71,74] , similar to that shown in Fig. 2 (b) &amp; (c).

## 3. Theory

## 3.1. Thermodynamics of RedOx reactions

We consider a general electrochemical reaction of the form

<!-- formula-not-decoded -->

where O + and R represent oxidized and reduced states, respectively, which may involve multiple ions or neutral molecules, while e -corresponds to the electron which participates in the RedOx reaction. In the general theory of electrochemical thermodynamics [12] , the electrochemical potential of individual species is described in terms of its diffusional chemical potential µ i , which is defined relative to a reference state /Theta1 , as a function of the electrical potential, φ , and species activity, a i

<!-- formula-not-decoded -->

where c i dimensionless species concentrations, k B is the Boltzmann constant, T is the absolute temperature, e is the elementary charge, and G corresponds to the non-equilibrium free energy of the system that can also be defined in terms of reaction coordinates. The excess chemical potential is defined as

<!-- formula-not-decoded -->

where γ i = a i / c i is the activity coe ffi cient of species i and contains all the present non-idealities of the studied system at its reduced and oxidized states (e.g. chemical or mechanical effects).

## 3.2. Reaction kinetics

Coupled ion-electron transfer reactions take place at interfacial regions in thermodynamically non-ideal systems and involve electron tunneling events. For this reason, CIET reactions require a description of reacting species that accounts for thermodynamic nonidealities, the transition state and the tunneling process. We build the theory using the Keizer's principles of nonequilibrium statistical mechanics [64] , as formulated for electrochemical reactions in [12] .

The reaction rate is written in terms of elementary processes as

<!-- formula-not-decoded -->

where R red and R ox correspond to the reduction and oxidation reaction rates, respectively [12] . Each of these rates is further analyzed as separate probabilistic events leading to

<!-- formula-not-decoded -->

In the above two equations, P ( O / R ) corresponds to the probability on finding particles of the oxidized or the reduced species as well as electrons and holes from an electron donor and is proportional to the species concentration n e / h c O / R e -w O / R / k B T . The part c O / R e -w O / R / k B T corresponds to the RedOx species concentration at the reaction site, where w O / R represents the free energy required to form the RedOx species from a chemical reservoir [12,65,75] and can be associated to the electric double layer and/or species adsorption energies at the electrode/electrolyte interface [76] . Also, n e and n h are the normalized concentrations of the electrons and holes [16] , respectively. P ( O / R → O ‡ / R ‡ ) describes the pr obability of thermally exciting the oxidized/reduced species to a state at which electron tunneling becomes iso-energetic, and is proportional to the Boltzmann factor relative to the transition state and local equilibrium excess chemical potential e ( µ ex ‡ -µ ex O / R ) / k B T . Also, P ( ET | O ‡ / R ‡ ) ≡ k T corresponds to the conditional probability of a successful electron tunneling event [16] , given that the oxidized/reduced species are thermally activated. Thus, the formal expressions for the forward and backward rates read [12]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where k 0 is a prefactor that satisfies microscopic reversibility [77,78] and µ ex O includes also the excess chemical potential of the electrons µ ex e . Depending on the context of the reaction one is interested in (e.g. electron transfer in bulk solution or near an electrode), k 0 has different physical meaning. In bulk electron transfer reactions under dilute conditions, for instance, k 0 corresponds to the attempt frequency per unit volume [16] , while for electron transfer reaction near electrodes it corresponds to the the attempt frequency per unit area. In more complex reactions, where all microscopic processes are clearly described (e.g. adsorption of ions on electrode surfaces), k 0 can have an Arrhenius form. Last, the hole concentration can be expressed as n h = 1 -n e [16,17] .

## 3.3. Coupled ion-electron transfer

In the present section, we derive the model for µ ex ‡ found in Eq. ( 5 ) for the case of coupled ion-electron transfer. Electron transfer reactions have been modeled successfully using classical Marcus theory [43] . In general, both µ ex O and µ ex R can be extended to include the reaction coordinate dependencies. We propose a description of the transition state that includes the typical harmonic polarization reaction coordinate x [12] , as well as an additional term that accounts for the ion transfer

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The functions f O and f R describe dependencies with respect to an additional reaction coordinate, the ionic one ξ , which accounts for non-idealities arising from the ion transfer reaction, as well as its coupling to the electron transfer. Here ξ takes the values ξ O in the oxidized state and ξ R in the reduced state and can be interpreted as the distance the ion has to move for the ion transfer to happen. That implies the following conditions on f O and f R

<!-- formula-not-decoded -->

which ensure that reactant/product complexes satisfy their equilibrium thermodynamics description and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In the classical electron transfer theory, where the reaction does not depend on the ionic coordinate, reduction of the oxidized species occurs iso-energetically [16] . Therefore, both the reactant and product environments need to have exactly the same energy for an electron to be transferred -electron tunneling events must conserve energy. This is true when x = x ‡ , where is used to determine x ‡ [12] . Here, µ ex ‡ , ET is the TS chemical potential defined at the intersection of the parabolas. The value of x ‡ from Eq. (8) results in the same activation barrier as the quantum mechanical approach of ET using Fermi's golden rule [16,79] .

<!-- formula-not-decoded -->

Fig. 3 illustrates the energy landscape including the ionic reaction coordinate introduced in Eqs. ( 6a ) &amp; ( 6b ). The idea of including the ionic coordinates for the reaction landscape can be seen as a generalization of Marcus's original picture [28] . The consideration of the ionic coordinate allows for the description of environmental effects on the transition state barrier, e.g. site exclusion due to surface crowding phenomena [12,26] . This is in contrast to existing studies that focus on dilute liquids and solids.

Fig. 3 (a) shows the intersection of the 2D parabolas of both reactant and product species (orange thick line). Solving Eq. ( 6 ) at the intersection, we can express x ‡ in terms of ξ . In principle, ET is possible for any value of ξ along the orange line, and thus the electron or ion transfer occurs separately from each other. However, we expect the ion-electron transfer to be concerted, as opposed to sequential, due to the large electrostatic attraction between the electron and the ion at their product state -the ion and the electron reside nearby each other in ion intercalation materials, where they interact through short-range electrostatics. For example, in the case where ξ = 0 there is a probability for electron transfer without ion transfer. The energy barrier for that process, though, is prohibitively large and is expected to scale as the Coulomb interaction energy /Delta1 E IT between the ion and the electron [80] . In the other limit, where the reaction complex is at its reduced state

( x , ξ ) = ( x R , ξ R ) , again, there is a large energy barrier to separate the electron from the transferred ion ( x , ξ ) = ( x O , ξ R ) due to their electrostatic attraction. In other words, /Delta1 E IT corresponds to the energy required to eliminate an ion-electron pair (break local electroneutrality). This picture leads to the additional conditions for f O and f R , which is

<!-- formula-not-decoded -->

Therefore, we argue that a sequential process would require supplying a considerable amount of energy in order to sacrifice the stabilizing attraction along that reaction pathway.

Assuming the barrier is much larger than the thermal energy k B T , the saddle point approximation for the first passage time [81] is used to derive the rate at the point where ∂ µ O / R / ∂ ξ ∣ ∣ x ‡ , ξ ‡ = 0 (yellow point on the orange line) where the reaction barrier is minimized. At ( x ‡ , ξ ‡ ) , the electrostatic penalty for separating the ions and electrons from their final state is postulated to be approximately the same, Eq. (9) , leading to an additional constraint to the functional forms of f O and f R

In cases where either the species do not interact through electrostatics, or the difference between µ O and µ R is much larger than the stabilizing electrostatic attraction /Delta1 E IT , Eq. (10) might need to be modified. In such situation, 'asymmetry' in the ionic coordinate can exist, and f O differs from f R at the transition state point ( x ‡ , ξ ‡ ) . The true nature of f O and f R can be revealed through detailed ab-initio studies [71] .

<!-- formula-not-decoded -->

The oxidized cluster has to fluctuate on a 2D energy surface until both the reactant and product states are equally likely to exist energetically, while the fluctuating trajectory is most likely to follow the path that passes over the minimum energy barrier for the reaction to happen. The point of the minimum transition state barrier ( x ‡ , ξ ‡ ) is defined by

Additional terms that account for the widening of the RedOx species' density of states upon its interaction with the electrode [82] can be added to Eqs. ( 6a ) and ( 6b ).

<!-- formula-not-decoded -->

The transition state chemical potential is split in two parts: 1) one that describes the polarization coordinate from traditional electron transfer kinetics µ ex ‡ , ET , and 2) another which takes into account ionic effects of the TS landscape f ( x ‡ , ξ ‡ ) , e.g. surface site exclusion due to surface crowding phenomena [12,83] . By assuming symmetric (equal) force constants for the polarization of the initial and final states κ O = κ R = κ , the functional form of the ET contribution is found after solving Eq. (11) for x ‡ , as [43,84]

<!-- formula-not-decoded -->

with reorganization energy λ = κ 2 ( x O -x R ) 2 corresponding to the energy required to alter the environment of the oxidized/reduced state to that of the reduced/oxidized sate without allowing an electron transfer to occur. After substituting Eq. (10) and Eq. (12) in one of the equations in Eq. ( 6 ), the final form of µ ex ‡ reads where µ ex IT = αξ /Delta1 E IT + k B T ln γ ‡ . The first term in µ ex IT is the ion transfer barrier due to the electrostatic penalty on separating the ion from the electron, and the second term describes the ionic non-idealities on the transition state, such as excluded volume effects and activation strain energies [12] . The parameter αξ can be

<!-- formula-not-decoded -->

viewed as an ionic transfer coe ffi cient, the value of which is determined by the exact functional form of f O and f R , as we describe in Section 4 . In the case where the transferred ion is strongly coupled with the final position of the transferred electron, we expect the constants κ O / R to be a function of the ionic coordinate ξ . This can induce asymmetries between the RedOx parabolas in the polarization coordinates. Although, this consideration may be more realistic, it poses analytical di ffi culties on arriving to a simple analytical form for the transition state barrier µ ex ‡ .

## 3.4. Quantum tunneling of electrons

The tunneling of electrons is modeled using the Landau-Zener theory [85,86] . The oxidized and reduced states are coupled to the surrounding reaction media which may fluctuate, leading to a crossing event of the wavefunctions at which tunneling may occur. The probability for such an event allowing for multiple re-crossings is given by [16]

<!-- formula-not-decoded -->

where, k T stands for the electron tunneling probability, H DA is the electronic coupling between the electron donor and acceptor, v ‡ is the thermally averaged reaction coordinate 'velocity', m is the effective mass of the reaction complex, and h is Planck's constant [16] . Because the coupling involves an electrode with electrons/holes of a manifold of energy levels, the electronic coupling is in general a function of electron energy levels ε . For nonadiabatic ET the weak coupling limit, /Gamma1 LZ /lessmuch 1 , we obtain the more classical result [16,85,86]

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where ν ‡ is the frequency of the RedOx species along the harmonic reaction coordinate [16] and ¯ h = h / 2 π .

## 3.5. Electrostatic effects on ion transfer

The main idea behind coupled ion-electron kinetics is the concerted transfer of both ions and electrons along the reaction coordinates. This process is mainly controlled by the interaction between ions and electrons that is described by the energy /Delta1 E IT found in Eq. (13) . Marcus in his original papers connected the reorganization energy with the Born solvation energy [16,43,44] , giving a simple estimate of the electron solvation energy in a dielectric medium. Herein, we develop an analogous formula to estimate /Delta1 E IT based on electrostatics.

We focus on the process ( x R , ξ R ) → ( x R , ξ O ) . In this case, the electron and the ion are in the reduced state where we supply energy /Delta1 E IT to move the ion to the position it occupies when the reaction complex is in its oxidized state ξ O . Therefore, we define /Delta1 E IT as

<!-- formula-not-decoded -->

where /Delta1 G ξ R → ξ O includes the energy to separate the electron and ion pairs as well as desolvate and resolvate the ion between different media, like in the case of ion intercalation. For the solvation part of /Delta1 G ξ R → ξ O , we follow a similar analysis to that presented by Makov &amp; Nitzan [87] , who studied the effects of dielectric mismatch on the solvation of ions with finite size.

According to Figs. 3 (a) and 5 (a), the energy /Delta1 G ξ R → ξ O is split in three contributions: 1) electrostatic interaction between the ion

Fig. 3. (a) Excess chemical potential landscape for both reactants and products vs. the reaction coordinates ( x , ξ ) . The orange line corresponds to the common points of the two parabolas, where iso-energetic electron transfer is possible. The red line depicts a fluctuating path in the two dimensional space where it passes through the maximum with the minimum value of the intersecting parabolas (yellow diamond), enabling the transfer of both the ion and the electron. In this picture, the coupled ion-electron transfer corresponds to concerted reaction process. (b) Excess chemical potential landscape for ξ = ξ O (dashed line), ξ = ξ ‡ (solid line), ξ = ξ R (dashed-dot line). (c) Schematic illustration of the projection of the energy profiles of the oxidized ( x = x O ) and reduced ( x = x R ) species on the energyξ plane is shown. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

Fig. 4. Primitive electrostatic model for the solvation of an ion near an interface that connects two media with dielectric permittivities ε p , 1 and ε p , 2 , respectively. The ion has charge q and radius a i . When the ion is solvated left/right of the interface, its distance from the interface is d 1 / 2 . At the transition state ξ ‡ , the ion is solvated exactly at the interface, where half of it is in the left dielectric medium and the other half on the right one. This model is similar to the one presented by Makov &amp; Nitzan [87] .

and the electron E C , 2) desolvation of the ion from ξ R in vacuum, /Delta1 G ξ R → v , 3) solvation of the ion from vacuum in ξ O , /Delta1 G v → ξ O . This is summarized as

<!-- formula-not-decoded -->

where we need to supply E C in order to separate the ion-e -pair (break of electroneutrality). We expect this term to be the dominant one in the expression above, and can be approximated analytically using either the Coulomb or the screened Coulomb potential (Yukawa) [88]

<!-- formula-not-decoded -->

where ε 0 and ε r are the permittivities of vacuum and the dielectric medium, λ s is the screening length, and r the distance between the localized electron and the ion.

For the solvation process, both /Delta1 G ξ R → v and /Delta1 G v → ξ O depend on the ion radius a i , the permittivities of the dielectric media ε p , 1 , ε p , 2 , and on the distances d 1 and d 2 of the ion from the interface 1 stands for the electrolyte phase and 2 for the solid phase, Fig. 4 . Following [87] , we use Eq. (17) in their work to derive the follow- ing form of /Delta1 E IT

<!-- formula-not-decoded -->

When ξ O and ξ R correspond to the the same physical position, then the second term in Eq. (20) is zero.

One can directly consider the relation between the energy contributions of the transition state due to the solvation effects and /Delta1 E IT . In this case, the two dielectric media are not in equilibrium as the transferring ion is at ξ = ξ ‡ , so ε p , 1 and ε p , 2 correspond to non-equilibrium permittivities [16] . As a first approximation the solvation energy of the transferring ion at the transition state, we assume that its the environment is at equilibrium, and thus ε p , i are the static permittivities of the two media. As discussed earlier, the saddle point approximation predicts that for ξ = ξ ‡ the ion is midway to its final state. One can assume this position to be right on top of a fictitious interface between the two dielectric media where the ion is solvated. Again, using Eq. (18) from Ref. [87] , we can describe the electrostatic part of the transition state as a solvation process from the vacuum state to the interface between the two dielectrics. Thus, we find a simple correspondence between /Delta1 E IT and the electrostatic part due to solvation of the transition state energy as follows

<!-- formula-not-decoded -->

Based on this form, it is apparent that by tuning the dielectric mismatch between the two media, one can promote or suppress the reaction dynamics. Eq. (21) can be seen as an extrapolation from the transition state to the final state of the system - the oxidized or reduced one.

The relations presented are simple approximations to the real system. The actual /Delta1 E IT can be calculated by performing either molecular dynamics [71] or ab-initio simulations, where the structure of the medium as well as the dynamics of the reactant species are taken into account in a systematic way. For example, Maxisch et al. [89] estimated /Delta1 E IT /similarequal E C = 0 . 37 eV for the Li + -polaron interaction in a LFP crystal.

## 3.6. Rate of coupled ion-electron transfer

Combining Eq. (12) with Eq. (13) and using the definition of the formal overpotential and overpotential of Eqs. (24) , (25) , as well as

Fig. 5. (a) Excess chemical potential landscape for both reactants and products vs. the reaction coordinates ( x , ξ ) , when the dependence in ξ is linear. The description of the lines and the fluctuating path in the energy landscape is given in Fig. 3 . (b) Excess chemical potential landscape for ξ = ξ O (dashed line), ξ = ξ ‡ (solid line), ξ = ξ R (dashed-dot line). (c) Schematic illustration of the projection of the energy profiles of the oxidized ( x = x O ) and reduced ( x = x R ) species on the energyξ plane is shown.

the tunnelling probability Eq. (16) in the elementary reaction rate expressions, Eq. ( 5 ), we arrive at

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where E f is the Fermi level of the electron donor and ˜ k 0 is the lumped reaction rate prefactor

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The electron concentration n e = 1 / ( 1 + e ε -E f ) is described by the Fermi-Dirac distribution [16,17] . In both rate expressions, we defined the formal overpotential η f , which is a measure of the departure of the electrode potential from the formal one as a result of RedOx concentration effects [16] , as where η is the overpotential defined as [12]

<!-- formula-not-decoded -->

and the formal potential of the reaction is defined as eV /Theta1 = µ /Theta1 R -µ /Theta1 O -E f . Last, to arrive at the final form of Eq. 22(a) &amp; (b), we considered the excess chemical potential of the electrons to be µ ex e = ε = /epsilon1 -e φ e , and also µ e = E f = ε + k B T ln ( n e / ( 1 -n e ) ) .

We can connect the form of Eq. (22) with those found in classical electron transfer papers [45] and electrochemistry books [18] . In connection to the notation used in Chidsey's paper on electron transfer reactions at metal-electrolyte interfaces [45] , x ≡ ( ε -E f ) / k B T and E 0 ′ -E ≡ e η f , where E 0 ′ and E are the formal and electrode potential, respectively. Related to electrochemistry books like Bard &amp; Faulkner [18] , the formulation of Eq. (22) can be directly translated to the expressions of Eqs. (3.6.34) &amp; (3.6.35) (p. 129-130) under standard conditions where e η f = e η = µ /Theta1 R -µ /Theta1 O -E f . Thus, performing the change of variables x ≡ E -E F in Eqs. (3.6.34) &amp; (3.6.35) of [18] , we arrive at the same form for the forward and backward reaction rates, where E and E F are the electron and Fermi energies, respectively.

In Eq. (22), the term e -α ξ /Delta1 E IT / k B T / γ ‡ is the main contribution of this work, where it describes the ion transfer effects on the transition state coupled with electron transfer. The other contributions such as the electron transfer term, the work required to bring the species to their RedOx states, and the tunneling factor are common in the field of electron transfer [16,43,75] . Finally, we are interested in validating the ionic dependencies on the transition state encoded in γ ‡ . We do so by applying the developed theory in ion intercalation. Thus, we go one step further and absorb the e -α ξ /Delta1 E IT / k B T into the reaction rate prefactor as

<!-- formula-not-decoded -->

For the remainder of the paper, all energetic quantities are normalized to k B T .

## 4. Two limits leading to the Butler-Volmer energy barrier

The ionic coordinate is tightly connected with the Coulomb energy which is a result of the attraction between ions and electrons, and thus f O and f R scale with /Delta1 E IT . From classical Marcus theory [43] , it is known that the electron transfer energy is proportional to the reorganization energy λ , which in our model is expressed in terms of the curvature of the parabolas, κ . Given that we have two characteristic energy scales, dimensionless analysis shows that their ratio κ / /Delta1 E IT serves as a characteristic measure, and helps us understand the limits of the developed model.

## 4.1. Electron-transfer limitation

The first case is that of κ / /Delta1 E IT /greatermuch 1 . In this scenario, ion transfer is decoupled from electron transfer ( f O / R / κ → 0 ), and thus the reaction is limited by the environment reorganization and electron tunneling only. The reaction is solely described in the solvent polarization coordinate and the classical approach of the two intersecting parabolas is followed. As a result, we recover the original Marcus/MHC model, where only the electron transfer needs to be resolved, while ion transfer dependencies are lumped in the constants of the model. For overpotential values smaller than λ / e , one arrives at the BV model with charge transfer coe ffi cient α = 1 / 2 . This result is well-known [12,18] and serves as the classical approach for providing a physical picture to the phenomenological Butler-Volmer kinetics.

Another interesting limit is when the ratio e η / λ /greatermuch 1 . In this case, one finds that µ ex ‡ , ET ∝ η 2 and therefore the activation energy barrier scales with E act ∼ -η 2 / 4 λ k B T . For localized electrons, the resulting reaction rate is predicted to decrease with increasing imposed driving force. This behavior leads to the well-known Marcus inverted region [16,43] .

## 4.2. Ion-transfer limitation

In the limiting case of κ / /Delta1 E IT /lessmuch 1 , which can be due to steep changes in the electrostatic potential nearby the electrode, e.g.

diffuse double layers [73,90,91] , the analysis shows an interesting connection between coupled ion-electron transfer and ButlerVolmer kinetics [18,20,21] . Under these conditions, we consider the dependence of f O and f R to be linear in the ionic coordinate ξ leading to the following expressions for the RedOx species chemical potentials

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

as also shown in Fig. 5 . By following the classical procedure on finding the intersection of µ O and µ R in the x coordinate, Eq. (11) , the transition state line x ‡ as a function of ξ is

<!-- formula-not-decoded -->

Substituting back to µ O or µ R , Eq. ( 6 ), and minimizing over ξ we find the following explicit expression for ξ ‡ :

Finally, the transition state chemical potential, which corresponds to the minimum energy barrier for the reaction to proceed, is found by substituting Eq. (28) and Eq. (27) in Eq. ( 26 )

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where for κ / /Delta1 E IT /lessmuch 1 , Fig. 5 (b), we can drop the λ / 2 term). In this limit, we find µ ex ‡ to be equivalent to the transition state of ButlerVolmer kinetics [12] for α = 1 / 2 , where also we can see that αξ = α . This is understandable in retrospect since the two-dimensional energy landscape can be cast in a form which imitates the phenomenological charge-transfer coordinate used in deriving ButlerVolmer kinetics, Fig. 5 (c). Our analysis reveals a different mechanism that recovers Butler-Volmer kinetics via coupled ion-electron transfer, and is in agreement with Fokker-Planck approaches commonly used in the field of quantum chemistry [73,92] .

## 5. Application to electrodes

## 5.1. Faradaic current

In order to obtain the total Faradaic reaction rate at an electrode, we assume a continuum of electron energy levels with density of states ρ ( ε ) , which corresponds to a family of parabolas in the electron transfer coordinate x [16,17,47,61,93,94] . By integrating Eq. (3) over all available energy levels we arrive at

<!-- formula-not-decoded -->

where in the weak coupling limit /Gamma1 LZ /lessmuch 1 , Eq. 15 , R red , ε and R ox , ε depend on the electron energy level ε through n e . The forward R red and backward R ox reaction rates satisfy the De Donder relation R red / R ox = e -e η / k B T , in compliance with microscopic reversibility [12,77] . Details on the derivation of the De Donder relation for coupled ion-electron transfer kinetics are given in the Appendix.

It is convenient to recast the net reaction rate in current density form, i = eR , as a function of the overpotential, as defined in Eq. (25) , and a prefactor defining the exchange current density [12] ,

<!-- formula-not-decoded -->

After some lengthy algebra for factorizing the current density in the form of Butler-Volmer, we arrive at the following form for the exchange current density

<!-- formula-not-decoded -->

and we define the charge transfer coe ffi cient as

<!-- formula-not-decoded -->

In Eq. (32) , we observe that when ion transfer limitations are negligible, then γ ‡ /similarequal 1 and k ∗ 0 /similarequal k 0 k T e -w and the exchange current density is equal to

<!-- formula-not-decoded -->

where ˜ H DA = H DA / √ ν ‡ ¯ h k B T is the dimensionless energy barrier between the two non-adiabatic electron states of the RedOx species [79] and we considered w O /similarequal w R ≡ w . Eq. (34) in combination with Eq. (31) are the BV-like form of the Marcus-HushChidsey model, which simplifies into the Marcus model [12] when the density of states corresponds to a single electron level.

We see that i 0 is within the integral related to the available energy levels of the electron donor. To be consistent with the electrochemistry literature, the classic exchange current density ˜ i 0 is defined as

The integral does not have an analytical form, except in specific cases, where for instance n e = /Theta1 ( E f -ε ) , with /Theta1 to be the Heaviside step function or when uniformly valid approximations are used [47] . In both of these cases and under dilute conditions, the exchange current density can be written as

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where f ( λ ) = erfc ( √ λ 2 -A 2 √ 1 λ + 1 √ λ ) , with A = 0 for n e = /Theta1 ( E f -ε ) and A = 1 for the uniformly valid approximation of [47] . When electron transfer near a metallic electrode is the limiting step (MHC model [45] ), the exchange current density becomes ˜ i 0 /similarequal ek 0 ˜ H 2 DA e -w c O f ( λ ) . In the case where the reorganization energy λ does not depend on species concentration, the form of ˜ i 0 depends on λ as shown in Fig. 6 (a). For simplicity, we assume dilute solution and for completeness we include the approximated forms of Eq. (36) .

The model parameters can be obtained either through experiments or first-principle calculations. In particular, the chemical potential of the species can be found either using equilibrium statistical mechanical methods [95] , or using experimental (non-)equilibrium measurements [78] such as construction of Tafel plots [61] . The common practice for estimating the electron donor density of states ρ ( ε ) and the reorganization energy λ is by using density functional theory, via the calculation of the band and phonon structures of the materials used in the reaction [96] .

## 5.1.1. Localized electrons

In the case of localized electrons for an insulating electrode or isolated molecule, the density of states can be approximated by a Dirac delta function around the localized energy level ε 0 as ρ = δ ( ε -ε 0 ) . Here, the Fermi level E f corresponds to the single electron level ε 0 . Additionally, the factors which account for the

Fig. 6. (a) Normalized exchange current density in terms of the reorganization energy λ in the case of dilute solution. For completeness we include the results of the numerical integration of Eq. (35) , the uniformly valid approximation of [47] , and the when n e = /Theta1 ( E f -ε ) . (b) Energy landscape in terms of the reorganization coordinate x for constant ξ = ξ ‡ for different values of the overpotential. (c) Tafel plot for the case of localized (black) and delocalized (blue) donor electrons. In the case where the electrons originate from an insulating phase or an isolated molecule, CIET predicts the inverted region observed in the classical model by Marcus [43] , where the current decreases with increasing driving force for η &gt; λ . Here, η is scaled with k B T / e and λ with k B T . When the electron donor has delocalized electrons, a family of parabolas exists that leads to a reaction-limited current for η &gt; λ . (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

probability of finding occupied n e and unoccupied 1 -n e energy levels in Eqs. ( 22a ),( 22b ) need to be set equal to 1. In that case, the total reaction rate expression reads

<!-- formula-not-decoded -->

where the second part of the expression corresponds to the electron transfer event, as has been initially derived by Marcus and others [16,43] . The first part corresponds to the ionic part of the transition state according to the developed framework of coupled ion-electron transfer. A similar form of Eq. (37) has been given in [12] , where the transition state activity coe ffi cient γ ‡ has been included through a 'modified' reorganization energy that depends on the RedOx species concentrations, e.g. λ ( c O , c R ) .

In Figs. 6 , we present the reaction landscape in terms of x at ξ = ξ ‡ and the current vs. overpotential dependence. In both figures, η and λ are scaled with k B T / e and k B T , respectively. At the transition state point ( x ‡ , ξ ‡ ) , CIET predicts the classical picture of the energy landscape that Marcus reported in his seminal works [16-18,43] , where for η = λ the electron transfer reaction becomes barrier-less [97] , Fig. 6 (b). For η &gt; λ , however, the electron transfer barrier starts increasing again leading to the Marcus inverted region [12,97] , Fig. 6 (c). Finally, across the line where the parabolas intersect, there are values of ξ for which x ‡ ( ξ ) lies in the inverted region and others that do not. For η /greatermuch /Delta1 E IT though, the transition state point in the ionic coordinate becomes ξ ‡ = ξ O , resulting in negligible ionic barrier and the reaction becomes electron-transfer limited.

## 5.1.2. Delocalized electrons

When the electrons that participate in the electrochemical reaction come from a metal, the density of states ρ is approximated as uniform nearby the Fermi level E f . In that case, the total reaction rate is calculated by Eq. (30) by setting ρ to be constant. Generally, the resulting integral does not admit an analytical solution, except in certain limits where the Fermi-Dirac distribution can be approximated with the Boltzmann distribution [17] . Despite these di ffi culties, one can either use special quadrature rules to evaluate the integral with very few function evaluations, e.g. GaussLaguerre quadrature, or other analytical approximations with acceptable numerical accuracy. Here, we briefly review an analytical approximation to the integral over all available energy levels for the case of constant ρ [47] . After applying the approximation of Eq. (17) of

Ref. [47] , the total reaction rate becomes where ˆ α = 1 + √ λ . As discussed in [47] , Eq. (38) can be evaluated as quickly as BV and does not require numerical integration, as implied from Eq. (30) . This fact makes it convenient for its use in analytical models. Additionally, it was shown in Fig. 4 of [47] that it is extremely accurate in various limits. More specifically, in the physically relevant case where λ &gt; k B T , the approximation error is always bounded below 5% even for small values of η f . At large η f and/or large λ the formula is able to replicate with extreme accuracy the results obtained from numerical quadrature, since it has exponentially small error in both η f and λ . Therefore, we believe that in the case of a metallic electron donor, the integral appearing in Eq. (30) can be approximated by the formula given in Eq. (38) with high accuracy and numerical e ffi ciency.

<!-- formula-not-decoded -->

In the case of delocalized electrons, the energy landscape of Fig. 6 (b) would correspond to a family of parabolas for the oxidized state, instead of a single one. Thus for metallic electron donors, CIET predicts the current density to saturate for η &gt; λ , Fig. 6 (c), while its limiting value is affected by the ionic energy barrier, Eq. (13) .

## 6. Application to ion intercalation

## 6.1. Motivation

Intercalation is a reversible reaction of ion insertion and extraction, whereby the stoichiometry of the host material changes with increasing/decreasing ion concentration. The insertion of species may be driven chemically, e.g. hydrogen insertion in Pd [98] , or electrochemically, e.g. Li ion intercalation in oxides [99] . Ion intercalation has been traditionally modeled by charge transfer kinetics using the BV equation in the context of batteries [11,62] . While charge transfer kinetics does not explicitly specify the nature of charge, which can be either that of the transferred electron or ion, it is often assumed that ion intercalation is limited by IT due to the experimentally observed concentration-dependent current densities [100-102] . Some have even questioned whether ion intercalation is a Faradaic reaction, arguing that ET from the electrode does not occur, beyond the simple electrostatic response of a capacitor [103] .

Contradicting this paradigm, it was recently proposed that ion intercalation in the Li-ion battery cathode material, Li x FePO 4 (LFP),

Fig. 7. Schematic illustration of the intercalation process described by coupled ionelectron transfer kinetics. The ion originates from a reservoir outside the particle, while the electron is provided by (a) &amp; (b) a metallic or (c) a semiconducting source. In the present figure, the electron ( e -) donor corresponds to a metal or semi-conductor, with Fermi energy E F . In (a) metals, electrons are delocalized within the solid, while in (c) semi-conductors they are localized on homogeneously distributed dopants. In the case of (b) an insulating material like LiFePO 4 , the electrons are provided from a thin conductive coating.

is instead limited by electron transfer. In particular, it was argued that the Li + ion transfer step is fast and follows the slow transfer of electrons between the metallic carbon coating and the neighboring RedOx-active Fe 3 + /Fe 2 + sites in the insulating crystal host [61] . These developments suggest that both ET and IT are important in ion intercalation, and the coupling between them depends on the electronic nature of the host compound. The materials in which ions intercalate can be metallic, semi-conducting or insulating. For example, LFP is a poor electronic conductor, while Li x C 6 (graphite) acts as a metal. Both are common materials found in commercial Li-ion batteries. Figs. 7 illustrate the case of coupled ion-electron transfer applied to ion intercalation, where the electron donor might be conducting or semi-conducting. Initially, ions exist in the electrolyte reservoir, and electrons reside either in the environment of the system (e.g. in the LFP case, where it comes from the carbon coating, Fig. 7 (b)), or in the solid matrix of the intercalation material (e.g. as in Li x CoO 2 (LCO) and graphite, because of their metallic state, Fig. 7 (a) &amp; (c)), or in a combination of both.

## 6.2. CIET applied to ion intercalation

The proposed mechanism of coupled ion-electron transfer takes into account the effects of the ion environment on the transition state. In ion intercalation materials, a non-negligible phenomenon that affects both the thermodynamics and the intercalation rates is the excluded volume interactions that take place either in the bulk or on the surface of the system. For example, in a latticegas model (solid solution) the diffusional chemical potential of the

Fig. 8. (a) Schematic of the reactant and transition state energy landscape for only the ion transfer. With increasing products concentration c R ≡ c , the entropic effects on the transition state increase the effective activation energy for the ion transfer process. As a result, the transition state excess chemical potential µ ex ‡ scales as ln ( 1 -c ) -1 . (b)-(d) Physical picture of the entropic effects on the transition state. Three representative concentrations are shown. With increasing the concentration of products, the ions at the transition state start interacting entropically with their environment, decreasing the probability for the ion transfer to occur.

intercalated ions is described by the following equation [12,104]

<!-- formula-not-decoded -->

where µ ex Li = µ /Theta1 Li + k B T ln γ Li , and γ Li = 1 / ( 1 -c ) that corresponds to the excluded volume effects.

In the case of the transition state, the picture is similar to the bulk [12,12,13,97,104-108] . More specifically, the idea of excluded sites on the transition state is demonstrated in Fig. 8 , where we provide a combined energetic and physical picture. For simplicity, we consider the case of an isolated ion transfer to understand solely the excluded volume effects. Thus, Fig. 8 (a) shows the energy landscape for both x = x O and x = x ‡ to demonstrate the effects of surface crowding on the reaction rate. We focus on three cases: 1) low, 2) intermediate, and 3) high concentration of intercalated ions c R ≡ c .

During ion transfer, ξ = ξ ‡ , the transferring ion occupies a free site from the product state. At the same time, all the other sites are populated by the ions of the product state. For low c , it is clear that there is a high probability for the TS ions to find a free site to be transferred, Fig. 8 (b) which corresponds to the light green curve in Fig. 8 (a). Once the concentration of products increases, Fig. 8 (c), the ions at the transition state start competing with those at the product state for free space. In other words, the entropic effects at the transition state decrease the probability of having a complete ion transfer by effectively increasing (medium green) the 'activation' energy of the process, Fig. 8 (a). At very high product concentrations, Fig. 8 (d), it becomes very rare for the transition state ions to not be repelled back to their reactant state. This translates to even higher (darker green) transition state energies, Fig. 8 (a). In analogy to the activity coe ffi cient of the bulk chemical potential shown in Eq. (39) , and also as described in detail in Fig. 8 and suggested in Ref. [12] , the excluded-volume effect during intercalation can be modeled with the following expression for the transition state activity coe ffi cient

<!-- formula-not-decoded -->

where s is the number of sites the transition state ions occupy during insertion. The species concentration effects on the transition state theory lead to reaction-limited current that depends on species concentration, in agreement with experiments on ion intercalation materials [109] .

In summary, for ion intercalation in a solid, excluding one site in the transition state ( s = 1 ), with electrons provided by a metallic electrode source, the CIET current density, Eq. (30) , can be approx-

imated as [47]

<!-- formula-not-decoded -->

where c is the normalized concentration of Li ions in the material [97,104,108,110] .

In the following sections, we test the predictions of coupled ion-electron transfer on describing Li ion intercalation in LFP on both the single particle and porous electrode scales. The Li intercalation reaction in LFP is modeled as

<!-- formula-not-decoded -->

where Li + sol / s denote the lithium ions in the electrolyte phase and in the particle respectively, while Fe + 3 / + 2 s are the oxidized and reduced states of Fe in the crystal. The electrons originate from the carbon film that surrounds the LFP particles [61] . Finally, the thermodynamic model for LFP can be found in [104,107,111] .

## 6.3. Exchange current density

Most BV-based reaction models admit the factorization of the form [12,26]

<!-- formula-not-decoded -->

where F ( c O , c R ) is a function only of the system species concentrations, which is directly related to the exchange current density i 0 , and G ( η ) is solely a function of the applied overpotential [26,62] . When the CIET model is cast in the same form as BV, Eq. (31) , this factorization is not possible. More specifically, the charge transfer coe ffi cient α becomes a function of both c O and c R , leading to G ( c O , c R , η ) . In fact, this non-linear coupling between α and η is one of the main reasons for distinguishing the models developed based on the quantum-mechanical picture of electron transfer from those which are purely phenomenological.

Table 1 summarizes several models that are commonly used in electrochemical ion intercalation. The first three are based on the BV formulation [12,13,62] , where only F ( c ) differs and α is a material parameter, while the last two correspond to ET kinetics, where α is now a function of the intercalated lithium concentration.

When the chemical potential µ is modeled using regular solution theory [104,105,112] , the first two models differ only by the factor which describes the Li-Li interactions. The regular solution term is responsible for the existence of spinodal points in a thermodynamics system [113] . The exchange current density i 0 used by Srinivasan &amp; Newman [62,114] , corresponds to an ideal lattice gas model with excluded volume effects. By postulating G ( η ) to be similar to the BV model, Lim et al. [13] mapped F ( c ) using the experimentally extracted current.

Both the first [12] and the third [13] models capture the autoinhibition mechanism which is responsible for the suppression of phase separation under non-equilibrium conditions [26] . The former, though, overestimates the range of c for which the reaction rate decreases with concentration [13] . Related to the differences between the ET models, the latter model introduced in Ref. [65] starts with the same general expression predicted by CIET theory, Eq. (38) , but is modified to replicate the exchange current density of the BV model [12] by eliminating the rough √ c dependence of G ( c , η ) , which is only true for large λ . It is thus interesting to test how this ad hoc departure from the CIET theory affects predictions of experimental data in this section and the next.

Fig. 9 shows the predictions of the normalized current i / i max as a function of c . The maximum current i max is defined at the normalized concentration c where i attains its maximum value. We

Fig. 9. Comparison of the observed normalized current [13] versus the predicted ones by the models in table. 1 . Solid lines describe the fitting on the experiments [13] and the theoretical predictions of the models derived in section 3 . With dashed lines are shown the predictions of the phenomenological models as introduced in [12,62,65] . For clarity, we use the following abbreviation for the models compared here: 1) Experiment [13] , 2) Phase-Field BV [12,104] , 3) Classical BV [11,62,114] , 4) Phase-Field MHC [65] . The model of Eq. (41) is not fitted to the experimental data. The parameters for the thermodynamics model of LiFePO 4 can be found in [104] , while the used value for the reorganization energy is taken from [61] , and is λ /similarequal 8 . 3 k B T . The inset figure corresponds to the normalized experimentally measured overpotential e η / k B T as a function of the local Li ion concentration c [13] , where the dashed dark red line corresponds to the average value of e η / k B T /similarequal 2 . 5 .

compare the model predictions with the experimentally measured data of the current density for LFP [13] (blue dots). The measured local concentration c and overpotential η are coupled, as the discharging was performed under constant current. Thus, Fig. 9 is constructed by directly using the experimentally observed values of ( c , η ) into the models presented in table 1 . The solid lines illustrate the fitting (blue) on the experimental data as performed in [13] along with the theoretical predictions of the CIET model (orange). The dashed lines show the predictions of the other models of Table 1 .

It is apparent that the model of our work along with the empirical fit [13] can capture the correct behavior of the normalized current vs. c . It noteworthy that the developed model has not been calibrated to the experimental data and the predictions are based on the material parameters found in Refs. [61,105] . The reorganization energy of LFP is equal to λ = 8 . 3 k B T [61] . Regarding the predictions of the other three models, they either overestimate or underestimate the concentration c max at which the current is maximized.

The quantitative agreement of our model with the experimental data highlights the importance of considering electron transfer coupled with ion transfer for ion intercalation in solids. This aspect is missing in earlier models of ion intercalation based on BV kinetics [12,62,104,114,115] , which we show here could arise in certain limits of the CIET theory for either large reorganization energy or large ion transfer energy at moderate overpotentials. Several similar, thermodynamically consistent generalizations of Marcus [12] and MHC [65] kinetics have also been postulated for ETlimited ion intercalation, but here we provide the first general microscopic theory capable of describing all of these limits and predicting the proper form of the rate expression. In the next section, we provide further quantitative support for the CIET theory by resolving the controversy over the original measurements revealing MHC kinetics in Li-ion batteries [61] .

## Table 1

Constitutive relations for ion intercalation. For clarity, all BV-based and CIET-based models are described with constant reaction constants, k ∗ BV , 0 and k ∗ 0 , respectively. The third model in the table, which is a variant of ET kinetics, is one of the versions suggested in [65] and used for the simulations therein.

| Model                                  | G ( c , η )                                                        | Ref.           |
|----------------------------------------|--------------------------------------------------------------------|----------------|
| F ( c )                                |                                                                    |                |
| k ∗ BV , 0 ( 1 - c ) e µ/ 2            | exp ( - αη ) - exp (( 1 - α ) η )                                  | [12,104]       |
| k ∗ BV , 0 c ( 1 - c )                 | ' '                                                                | [62]           |
| √ 3 k ∗ BV , 0 ( 1 - c ) √ c ( 1 - c ) | ' '                                                                | [13]           |
| k ∗ 0 ( 1 - c ) e µ/ 2 √ c             | exp - ( η 2 4 λ ) [exp ( - α ( c ) η ) - exp (( 1 - α ( c )) η ) ] | [65]           |
| k ∗ 0 ( 1 - c ) e - α 2 λ              | ' '                                                                | Eq. (31), [65] |

## 6.4. Chronoamperometry with porous electrodes

Porous electrode theory [65,83,116] is widely used for predicting the behavior of macroscopic quantities (e.g. current/voltage response, and (dis)charging capacity) which are important in energyrelated applications (e.g. Li-ion batteries [99] ). In general, the resulting voltage and current follow complex dynamics which are a result of coupled processes across multiple scales. In Li-ion batteries for example, the cathode and anode consist of multiple particles where Li insertion and solid diffusion are important. The primary particles and secondary agglomerates are connected to each other through the electrolyte, as well as conducting additives. Here, our goal is to demonstrate how CIET theory performs on the porous electrode scale. More specifically we compare the predictions of the model with the chronoamperometry experiments of [61] on LFP.

The system we are interested in contains N LFP particles and is initially prepared at V cell = 3 . 422 V and room temperature. At t = 0 , we apply a voltage step of magnitude /Delta1 V . We use the same voltage step values as those in [61] . The voltage range under which the experiment is performed covers a large spectrum of Li concentrations inside the active material of the cathode. This is seen from the voltage-capacity curves of LFP, where for the largest voltage drop V cell + /Delta1 V max = 3 . 069 V, the final capacity of the intercalated Li in the cell lies in the spinodal [13,104,118] .

As in the case of single particles, we are interested in comparing the predictions of different reaction models that are commonly used to describe ion intercalation kinetics. In particular, we compare the developed model against BV [12,104] and BV with film resistance R f (BV+film) [65,83,119,120] . The mathematical expression of the latter can be found in Eqs. (35), (36), and (37) of Ref. [65] . BV+film is known to reproduce curved Tafel plots [120] , similar to the ones predicted by electron transfer limitations [61] . Therefore, we test the models not only in terms of their capability to predict the Tafel plots, but also on the time evolution of the resulting current after we apply the voltage step.

We perform the simulation using porous electrode theory, pioneered by Newman [62,121] , as recently modified to describe phase separating materials [65,83] . We refer the readers interested in the porous electrode theory to Refs. [11,65,83] and for the numerical methods for discretizing the equations to [122,123] for more details. The cell has a diameter of 1.27 cm, while each electrode has thickness approximately around L electrode = 4 µ m. The size of the LFP primary particles is described by a log-normal distribution [124] with average diameter &lt; d &gt; = 1 µ m, and variance of σ 2 d = 250 nm, a value found by fitting the theory to the experiments. The total number of particles used in the simulations is of the order N ∼ O ( 10 4 ) . The simulation results using the particle size distribution are denoted with PSD, otherwise we set σ 2 D = 0 . All the parameters related to the geometry of the cell, electrode and the particle size are reported in the Methods section of [61] . In addi- tion to the variance of the particle population, we also adjust the constant reaction rate prefactor k ∗ 0 to fit the experiments, and we find it to be k ∗ 0 = 8 × 10 -3 A/m 2 . The coupled ion-electron transfer and the BV models were calibrated on half of the available experimental data sets [61] that correspond to the lower values of the applied /Delta1 V , while the BV+film model was calibrated on the Tafel plot of [61] . The fitting was performed using a common non-linear least squares procedure [125] . This fitted value of k ∗ 0 is very close to the one calculated in Ref. [13] by assuming a reaction-limited process. For the Butler-Volmer with film resistance, we use R f = 7 /Omega1 m 2 to fit the Tafel plot.

Additionally, we neglect diffusion limitations in the electrolyte within the electrode, and we set the number of volumes in the porous electrode model equal to one. This assumption is based on the estimate of the liquid diffusion timescale for the electrolyte within the electrode τ electrolyte = L 2 electrode / D Li + , where D Li + is the liquid electrolyte diffusion coe ffi cient of the solvated Li ions. Using D Li + /similarequal 5 × 10 -11 m 2 /s as a characteristic value, we find τ electrolyte /similarequal 0 . 3 s, which is much shorter than the operation timescale of the cell (around 1200 seconds for the largest applied overpotential). Under these conditions we can safely assume nearly uniform Li concentration across the electrolyte phase.

In general, porous electrode experiments involve thousands of primary particles of variable sizes. As discussed in [117] , the resulting macroscopic quantities of the cell are affected by several factors such as particle activation/nucleation, phase-separation, variable particle size, inhomogeneous SEI formation amongst different particles, etc. Therefore, the usage of a statistical method is important in order to extract the true reaction constants of the studied reaction. We applied the same protocol to our simulation results to construct in a similar fashion the Tafel plot shown in Fig 10 (c). More specifically, after performing the simulations, we extract the resulting current, and we fit it with Eq.(4) of [61] . Then, we use the fitted k values (reaction constant in the population model) to construct the Tafel plot.

Fig. 10 (a) illustrates the current I vs. time t after we apply a step of /Delta1 V = -0 . 045 V ( e η ∼ 2 k B T ). The experimental measurements are shown with black circles, while the model predictions are shown with continuous lines. As shown in Fig. 10 (a), for conditions near equilibrium (small overpotential) all models behave similarly, reproducing the experimentally observed current-time response. At large applied overpotential, however, the predictions of each model start to deviate from each other.

Fig. 10 (b) shows the transients of the current under /Delta1 V max = -0 . 354 V, a value almost 10 times larger than the previously discussed voltage step. Under these conditions, the predictability of the developed coupled ion-electron transfer is apparent (red line), where it is able to reproduce the experimentally observed current for the largest percentage of the studied time interval. Regarding the predictions of BV kinetics (green line), we know that the model predicts exponentially increasing current with increasing overpotential. Under the experimental conditions the current is overes-

Fig. 10. Comparison of reaction models in chronoamperometry experiments and simulations. Experimental data are from ref. [61] . (a),(b) Transient simulated (solid lines) and experimental (black circles) current responses, under a voltage step of /Delta1 V = -0 . 045 V and /Delta1 V = -0 . 354 V, respectively, for the CIET (red line), CIET with particle size distribution (PSD) (dark red line), BV+film (blue line) and BV (green line) reaction models. (c) Tafel plot constructed using the method presented in [61,117] to extract the representative reaction rate constant k .

timated for the applied overpotential, and decays rapidly at very early times ( t ∼ 100 s), Fig. 10 (b). Finally, the predictions on current vs. t using BV+film are shown with the blue line. The predicted values of current are not able to capture the experimentally measured values, making clear the discrepancies that can be introduced by using only Tafel measurements to characterize the mechanism of a reaction.

This last comparison raises questions on the interpretation of experimental data by using classical methods such as Tafel analysis. Fig. 10 (c) shows the constructed Tafel plot by using the statistical method introduced in [117] and used in [61] . Again, the red line represents the predictions using CIET and the blue line those of BV+film. The agreement between CIET and BV+film is consistent with the discussion in Ref. [120] , where it was shown that curved Tafel plot data can be fitted by Butler-Volmer with film resistances included. However, as shown in Fig. 10 (b), the latter model is not able to capture the experimentally observed trends of the current transients under large values of overpotential ( e η / k B T /greatermuch 1 ). In both current-time tests, as well as on comparing the extracted Tafel plots, we find that CIET predictions are consistent with the experimentally observed behavior on the porous electrode scale.

As a final remark on the porous electrode analysis, we would like to raise general questions related to the characterization of the reaction kinetics by classical electro-analytical methods [18] . It is common practice to use either electrochemical impedance measurements, Tafel analysis, or cyclic voltammetry to characterize the processes present in an electrochemical system. Here, we show that in a reaction-limited system [13] , the Tafel analysis and EIS [120] alone are not able to resolve the rate-determining step of Li-ion intercalation and predict other types of measurements. In a complicated system such as a porous electrode, it is di ffi cult to use the classical electroanalytical machinery to deconvolute different processes that take place across multiple scales involving highly nonlinear couplings of reaction and diffusion.

## 7. Discussion

The application of CIET theory is by no means limited to lithium intercalation in LFP [12,107,126] . The generality of the reaction rate expressions presented in Section 3 makes the theory applicable to CIET reactions in both concentrated solids and liquids. As described earlier, candidate processes in which coupled ion-electron transfer might be the rate-determining step include: (i) lithium intercalation in other host materials, such Li x CoO 2 (LCO) [108] , Li x C 6 (graphite) [126-128] , Li x TiO 2 (anatase) [129] , and Li 4 + 3 x Ti 5 O 12 (LTO) [130-132] , used in Li-ion batteries, as well as in neuromorphic computing devices [108,132-134] , (ii) sodium intercalation in Na-ion batteries [135,136] or capacitive deionization [9,63,137] ,(iii) multivalent aluminum ion intercalation in Alion batteries [138,139] (iv) oxygen insertion in perovskite oxides used in fuel cells [140,141] , or oxygen reduction using perovskites as catalysts for metal-air batteries [142] .

The material parameters which enter the model are directly connected with the microscopic nature of the species which participate in the reaction. In particular, via the explicit usage of chemical potentials, the non-ideal nature of the species is included. Also, the electron energy levels are taken into account by describing the band structure of the donor of the electrons via the density of states of the material. Finally, the interactions between the electrons with their environment is described through the reorganization energy. All this microscopic information establishes coupled ion-electron transfer as a quantitative, physics-based model for intercalation reaction kinetics.

There are several Li ion intercalation studies where coating the intercalation material with anionic additives increases the rate performance [143-150] . Until now, existing models cannot explain the reason why this occurs. More specifically, the parameters in BVbased models cannot be directly related to the physical details of the reaction event process, while ET models describe only the electron transfer event without considering the fate of the ions. On the other hand, the idea of coupled ion-electron transfer takes into account the microscopic physics of both the ion and electron transfer, as we consider both processes to occur simultaneously. Through CIET, we are able to give a possible explanation for why the anionic-coating rate enhancement occurs. The model includes the energies w O / R that correspond to the 'adsorption' of the ion at the reaction interface ( ξ = ξ O ).

In general, w O / R corresponds to the repulsive/attractive interactions between the solvated ions and interface atoms, and the diffuse double-layer effects on the ions that participate in the reaction. For Li-ion intercalation, when anionic groups, for example N -or S -groups [144] , are added on the surface of the intercalation material, the energy barrier w O / R decreases, leading to an increase of the effective reaction rate constant. This behavior is in qualitative agreement with both experimental and ab-initio studies on Li intercalation in LiFePO 4 [143,144,149] .

Coupled ion-electron transfer can be used to provide insights on the design and engineering of interfaces where electrochemical reactions take place. Very recently, it has been shown that by understanding the functional form of the reaction rate expressions, one is able to control, and consequently engineer, the physics of interfaces where reactions take place [26] . Representative examples are the lithiation of LFP and LiNi 1 / 3 Mn 1 / 3 Co 1 / 3 O 2 [151,152] particles, as well as the operation of Li-air batteries, where the thermo-

dynamic stability of the system is controlled by varying the applied current [13,97,104,153,154] . In terms of CIET, by understanding the concentration dependencies of both the reorganization energy and the density of states of the electron donor, we will be able to control interface structure by inducing or suppressing phase separation/island formation.

There are cases where increased interfacial anisotropy is desired. For example in electro-catalytic applications the interface structure of the active area affects the e ffi ciency of processes like dealloying [155] or light absorption [156] . In other cases surface anisotropy can lead to mechanical failure, e.g. in all-solid-state Liion batteries where loss of contact between the active material and the solid electrolyte leads to irreversible capacity loss [157] . Thus, the present theoretical framework of coupled ion-electron transfer draws a connection between the structural information of the species participating in the reaction with the operational conditions, providing direct ways to engineer surfaces using electrochemical methods [97] .

The idea of the coupled ion-electron transfer can be extended to describe the diffusion of ione -pairs in solids. This description can give important insights on the limitations of technologies such as solid-state batteries [158] , where the electronic conductivity of solid electrolytes [159,160] is not fully understood yet [161] .

As a last remark, we would like to stress again that, while the physical picture of coupled ion-electron transfer is general, our mathematical formulation expressing the rates via Eq. (22)(a) &amp; (b) corresponds to non-adiabatic electron transfer. There are important cases where the electronic states of the RedOx states are strongly coupled [162,163] , as in specific ion adsorption, and the electron transfer occurs adiabatically. In such situations, the electron transfer event depends strongly on the electronic interactions between the RedOx species as well as with the solvent [17,60] . These effects have been previously discussed in the context of coupled protonelectron transfer for describing hydrogen evolution, where the proton transfer is characterized by its distance from the electrode and the electron transfer occurs adiabatically [163,164] . In this case, the mathematical formulation of the forward and backward reaction rates is typically analyzed using model Hamiltonians, such as the Newns-Anderson model, combined with mean-field electrostatics for the double layer effects on the proton transfer [72] .

## 8. Summary

In this work, the theory of electron transfer has been extended to incorporate ion transfer effects on the reaction kinetics. In particular, by expanding the reaction space to include additional coordinates in addition to the polarization one, we include phenomena such as surface crowding, (de)solvation effects, misfit stress contributions, etc. on the transition state. Moreover, the thermodynamics of the species are incorporated in the reaction kinetics formalism, allowing for the description of phase separation and its effects on the reaction rate. The results presented here illustrate the importance of coupled ion-electron transfer kinetics in ion intercalation kinetics [12,13,61] . The key expressions for the total reaction rate derived from our theory are

<!-- formula-not-decoded -->

where x ε = ε -E f , e η f = e η -k B T ln ( c O / c R ) , e η = eV /Theta1 + k B T ln ( γ R c R γ O c O ) + e ( z R φ R -z O φ O ) -E f , and n e = ( 1 + e ε -E f ) -1 . For practical purposes, the reaction rate prefactor k ∗ 0 can be fitted to experiments or predicted from first-principles as described in Eq. (23) . Additionally, the transition state activity coe ffi cient can take into account the effects of the environment on the ion transfer event. One example is the exclusion of a free site during the transfer of an ion to its product state, where γ ‡ scales with the number of available free sites, γ ‡ ∝ ( 1 -c R ) -1 . F or insertion of ions in solids, pre-existing strains developed due to concentration fluctuations can also affect the transition state barrier.

The usage of the theory is demonstrated by modeling the insertion of ions in solid materials, a process present in several applications of technological importance. By comparing the predicted current density to available experimental data [13,61] on lithium intercalation in primary FePO 4 particles, we demonstrated the capability of CIET to accurately describe, on microscopic (single particle) and macroscopic (porous electrode) levels, the (dis)charging process of Li-ion batteries. In particular, the model predicts the experimentally observed normalized total current without using any adjustable parameters. Additionally, the surface crowding effects upon Li insertion were found to be crucial in correctly predicting the auto-inhibitory nature of the phenomenon.

## Contributions

D.F. and M.Z.B. formulated the framework of coupled ionelectron transfer, building on earlier attempts by R.B.S., Y.K. and P.B. D.F. and M.M. integrated the quantum mechanical details. D.F., W.C.C and M.Z.B. justified the theory for ion intercalation materials, and D.F. performed the LFP simulations, building on the those of R.B.S. D.F., Y.S.-H. and M.Z.B. connected the developed framework with the notation present in classical electrochemistry literature. Y.Z. and Y.S.-H. provided helpful comments on the narrative and mechanisms. D.F. wrote the manuscript, and M.Z.B. supervised the study and revised the text. All authors contributed to the final manuscript.

## Declaration of Competing Interest

There are no conflicts to declare.

## Acknowledgments

The research was supported by the D 3 BATT program of the Toyota Research Institute and by the Shell International Exploration &amp; Production, Inc. The authors would like to thank Yiyang Li and Dean (Haitao) Deng for providing the raw data from the STXM experiments, Neel Nadkarni, Tao Gao, Tingtao Zhou, and Ryan M. Stephens for discussions related with the validity and application of the theory. Finally, the authors want to thank the anonymous reviewers for the constructive comments they provided, which helped to improve the presentation of the current work.

## Appendix A. Appendix

Derivation of De Donder relation for coupled ion-electron transfer kinetics

An essential constraint on any thermodynamically consistent model of reaction kinetics is that the forward and backward rates satisfy the de Donder relation expressing microscopic reversibility [78] , which takes the following form for an electrochemical reaction [12] ,

<!-- formula-not-decoded -->

In order to prove De Donder relation for the ratio of R red / ox = ∫ ∞ -∞ R red / ox , ε ρ d ε , it is useful to group all ε -dependencies together. In particular, we can recast Eq. (22) in the following form

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where we used the definition of n e = 1 / ( 1 + e x ε / k B T ) . Then, the ratio R red / R ox can be simplified as follows:

<!-- formula-not-decoded -->

which is the De Donder relation.

## References

- [1] J.M. Nocek , J.S. Zhou , S. De Forest , S. Priyadarshy , D.N. Beratan , J.N. Onuchic , B.M. Hoffman , Theory and practice of electron transfer within proteinprotein complexes: application to the multidomain binding of cytochrome c by cytochrome c peroxidase, Chem. Rev. 96 (7) (1996) 2459-2490 .
- [2] S.V. Antonyuk , C. Han , R.R. Eady , S.S. Hasnain , Structures of protein-protein complexes involved in electron transfer, Nature 496 (7443) (2013) 123-126 .
- [3] L.J. Jeuken , Conformational reorganisation in interfacial protein electron transfer, Biochimica et Biophysica Acta (BBA)-Bioenergetics 1604 (2) (2003) 67-76 .
- [4] M. Bixon , J. Jortner , M. Michel-Beyerle , A kinetic analysis of the primary charge separation in bacterial photosynthesis. energy gaps and static heterogeneity, Chem. Phys. 197 (3) (1995) 389-404 .
- [5] H. Wang , S. Lin , J.P. Allen , J.C. Williams , S. Blankert , C. Laser , N.W. Woodbury , Protein dynamics control the kinetics of initial electron transfer in photosynthesis, Science 316 (5825) (2007) 747-750 .
- [6] J. Dykstra , K. Keesman , P. Biesheuvel , A. Van der Wal , Theory of pH changes in water desalination by capacitive deionization, Water Res. 119 (2017) 178-186 .
- [7] C. Zhang , D. He , J. Ma , W. Tang , T.D. Waite , Faradaic reactions in capacitive deionization (CDI)-problems and possibilities: a review, Water Res. 128 (2018) 314-330 .
- [8] D. He , C.E. Wong , W. Tang , P. Kovalsky , T.D. Waite , Faradaic reactions in water desalination by batch-mode capacitive deionization, Environ. Sci. Technol. Lett. 3 (5) (2016) 222-226 .
- [9] K. Singh , H. Bouwmeester , L. de Smet , M. Bazant , P. Biesheuvel , Theory of water desalination with intercalation materials, Phys. Rev. Appl. 9 (6) (2018) 064036 .
- [10] K. Singh , S. Porada , H. de Gier , P. Biesheuvel , L. de Smet , Timeline on the application of intercalation materials in capacitive deionization, Desalination 455 (2019) 115-134 .
- [11] J. Newman , K.E. Thomas-Alyea , Electrochemical Systems, 3rd, John Wiley and Sons, Hoboken, New Jersey, 2004 .
- [12] M.Z. Bazant, Theory of chemical kinetics and charge transfer based on nonequilibrium thermodynamics, Acc. Chem. Res. 46 (5) (2013) 1144-1160, doi: 10.1021/ar300145c .
- [13] J. Lim, Y. Li, D.H. Alsem, H. So, S.C. Lee, P. Bai, D.A. Cogswell, X. Liu, N. Jin, Y.-s. Yu, N.J. Salmon, D.A. Shapiro, M.Z. Bazant, T. Tyliszczak, W.C. Chueh, Origin and hysteresis of lithium compositional spatiodynamics within battery primary particles, Science 353 (6299) (2016) 566-571, doi: 10.1126/science. aaf4914 .
- [14] M. Winter , B. Barnett , K. Xu , Before li ion batteries, Chem. Rev. 118 (23) (2018) 11433-11456 .
- [15] K. Xu , Electrolytes and interphases in li-ion batteries and beyond, Chem. Rev. 114 (23) (2014) 11503-11618 .
- [16] A.M. Kuznetsov , J. Ulstrup , Electron Transfer in Chemistry and Biology: An Introduction to the Theory, Wiley, 1999 .
- [17] W. Schmickler , E. Santos , Interfacial Electrochemistry, Springer Science &amp; Business Media, 2010 .
- [18] A.J. Bard , L.R. Faulkner , Electrochemical Methods, J. Wiley &amp; Sons, Inc., New York, NY, 2001 .
- [19] J. Tafel , Über die polarisation bei kathodischer wasserstoffentwicklung, Z. Phys. Chem 50 (1905) 641 .
- [20] J.A.V. Butler , Studies in heterogeneous equilibria. Part III. A kinetic theory of reversible oxidation potentials at inert electrodes, Trans. Faraday Soc. 19 (March) (1924) 734-739 .
- [21] T. Erdey-Grz , M. Volmer , Zur Frage der elektrolytischen Metallberspannung, Zeitschrift fr Physikalische Chemie 157A (1) (1931) 165 .
- [22] J.O. Bockris , Modern Electrochemistry 2B: Electrodics in Chemistry, Engineering, Biology and Environmental Science, 2, Springer Science &amp; Business Media, 1998 .
- [23] P. Biesheuvel , M. Van Soestbergen , M. Bazant , Imposed currents in galvanic cells, Electrochim. Acta 54 (21) (2009) 4 857-4 871 .
- [24] H. Eyring , The activated complex in chemical reactions, J. Chem. Phys. 3 (2) (1935) 107-115 .
- [25] J.K. Nørskov , F. Studt , F. Abild-Pedersen , T. Bligaard , Fundamental Concepts in Heterogeneous Catalysis, John Wiley &amp; Sons, 2014 .
- [26] M.Z. Bazant, Thermodynamic Stability of Driven Open Systems and Control of Phase Separation by Electroautocatalysis, Faraday Discuss. (2017), doi: 10. 1039/C7FD0 0 037E .
- [27] R.A. Marcus, Electrostatic Free Energy and Other Properties of States Having Nonequilibrium Polarization. I, J. Chem. Phys. 24 (5) (1956) 979, doi: 10.1063/ 1.1742724 .
- [28] R.A. Marcus , Chemical and electrochemical electron-transfer theory, Ann. Rev. Phys. Chem. 15 (1) (1964) 155-196 .
- [29] R.A. Marcus, On the theory of oxidation-reduction reactions involving electron transfer. I, J. Chem. Phys. 24 (5) (1956) 966, doi: 10.1063/1.1742723 .
- [30] R.A. Marcus , On the theory of oxidation-reduction reactions involving electron transfer. II. Applications to data on the rates of isotopic exchange reactions, J. Chem. Phys. 26 (4) (1957) 867-871 .
- [31] R.A. Marcus , On the theory of electrochemical and chemical electron transfer processes, Can. J. Chem. 37 (1) (1959) 155-163 .
- [32] R.A. Marcus , Exchange reactions and electron transfer reactions including isotopic exchange. Theory of oxidation-reduction reactions involving electron transfer. Part 4.A statistical-mechanical basis for treating contributions from solvent, ligands, and inert salt, Discuss. Faraday Soc. 29 (1960) 21-31 .
- [33] R.A. Marcus , On the theory of oxidationreduction reactions involving electron transfer. V. Comparison and properties of electrochemical and chemical rate constants, J. Phys. Chem. 67 (4) (1963) 853-857 .
- [34] N.S. Hush , Electrode reactions of the methyl halides, Berichte der Bunsengesellschaft fr Physikalische Chemie 61 (6) (1957) 734-738 .
- [35] N.S. Hush, Adiabatic rate processes at electrodes. I. energy-charge relationships, J. Chem. Phys. 28 (5) (1958) 962, doi: 10.1063/1.1744305 .
- [36] N.S. Hush , Adiabatic theory of outer sphere electron-transfer reactions in solution, Trans. Faraday Soc. 57 (1961) 557-580 .
- [37] N.S. Hush , Homogeneous and heterogeneous optical and thermal electron transfer, Electrochim. Acta 13 (5) (1968) 1005-1023 .
- [38] R.R. Dogonadze , Y.A. Chizmadzhev , Kinetics of some electrochemical oxidation-reduction reactions on metals, in: Doklady Akademii Nauk SSSR, 145, Mezhdunarodnaya Kniga 39 Dimitrova UL., 113095 Moscow, Russia, 1962, pp. 848-851 .
- [39] V.G. Levich , R.R. Dogonadze , Osnovnie voprosi sovremenoi teoreticheskoi elektrokhimii, in: Proceedings of the 14th CITCE Meeting, Moskow, 1963, p. 21 .
- [40] R.R. Dogonadze , A.M. Kuznetsov , A.A. Chernenko , Theory of homogeneous and heterogeneous electronic processes in liquids, Russ. Chem. Rev. 34 (10) (1965) 759-775 .
- [41] S.G. Christov , Collision Theory and Statistical Theory of Chemical Reactions, 18, Springer Science &amp; Business Media, 2012 .
- [42] S. Christov , Quantum theory of electron-transfer processes in solution, Berichte der Bunsengesellschaft für Physikalische Chemie 79 (4) (1975) 357-371 .
- [43] R.A. Marcus , Electron transfer reactions in chemistry. Theory and experiment, Rev. Mod. Phys. 65 (3) (1993) 599-610 .
- [44] R.A. Marcus, On the theory of electron-transfer reactions. VI. unified treatment for homogeneous and electrode reactions, J. Chem. Phys. 43 (2) (1965) 679, doi: 10.1063/1.1696792 .
- [45] C.E. Chidsey, Free energy and temperature dependence of electron transfer at the metal-electrolyte interface, Science 251 (4996) (1991) 919-922, doi: 10. 1126/science.251.4996.919 .
- [46] M.C. Henstridge, E. Laborda, N.V. Rees, R.G. Compton, MarcusHushChidsey theory of electron transfer applied to voltammetry: A review, Electrochim. Acta 84 (2012) 12-20, doi: 10.1016/j.electacta.2011.10.026 .
- [47] Y. Zeng, R.B. Smith, P. Bai, M.Z. Bazant, Simple formula for MarcusHushChidsey kinetics, J. Electroanal. Chem. 735 (2014) 77-83, doi: 10.1016/j.jelechem. 2014.09.038 .
- [48] M.T.M. Koper, Theory of the transition from sequential to concerted electrochemical protonelectron transfer, Phys. Chem. Chem. Phys. 15 (5) (2013) 1399-1407, doi: 10.1039/C2CP42369C .
- [49] J.-M. Savéant, Concerted proton-electron transfers: fundamentals and recent developments, Ann. Rev. Anal. Chem. 7 (1) (2014) 537-560, doi: 10.1146/ annurevanchem071213020315 .
- [50] J.M. Mayer, Proton-coupled electron transfer: a reaction chemist's view, Ann. Rev. Phys. Chem. 55 (1) (2004) 363-390, doi: 10.1146/annurev.physchem.55. 091602.094 4 46 .
- [51] S. Hammes-Schiffer, Controlling electrons and protons through theory: molecular electrocatalysts to nanoparticles, Acc. Chem. Res. 51 (9) (2018) 1975-1983, doi: 10.1021/acs.accounts.8b00240 .

- [52] J.M. Savéant, Evidence for concerted pathways in ion-pairing coupled electron transfers, J. Am. Chem. Soc. 130 (14) (2008) 4732-4741, doi: 10.1021/ja077480f .
- [53] S. Fukuzumi, K. Ohkubo, Y. Morimoto, Mechanisms of metal ion-coupled electron transfer, Phys. Chem. Chem. Phys. 14 (24) (2012) 8472-8484, doi: 10. 1039/c2cp40459a .
- [54] R.I. Cukier , D.G. Nocera , Proton-coupled electron transfer, Ann. Rev. Phys. Chem. 49 (1) (1998) 337-369 .
- [55] S.Y. Reece , D.G. Nocera , Proton-coupled electron transfer in biology: results from synergistic studies in natural and model systems, Ann. Rev. Biochem. 78 (2009) 673-699 .
- [56] S. Horvath , L.E. Fernandez , A.V. Soudackov , S. Hammes-Schiffer , Insights into proton-coupled electron transfer mechanisms of electrocatalytic h2 oxidation and production, Proc. Natl Acad. Sci. 109 (39) (2012) 15663-15668 .
- [57] S. Hammes-Schiffer , A.V. Soudackov , Proton-coupled electron transfer in solution, proteins, and electrochemistry, J. Phys. Chem. B 112 (45) (2008) 14108-14123 .
- [58] M.M. Melander , Grand canonical rate theory for electrochemical and electrocatalytic systems i: General formulation and proton-coupled electron transfer reactions, J. Electrochem. Soc. 167 (11) (2020) 116518 .
- [59] G.A. Parada , Z.K. Goldsmith , S. Kolmar , B.P. Rimgard , B.Q. Mercado , L. Hammarström , S. Hammes-Schiffer , J.M. Mayer , Concerted proton-electron transfer reactions in the Marcus inverted region, Science 364 (6439) (2019) 471-475 .
- [60] W. Schmickler, Electron and ion transfer reactions on metal electrodes, Electrochim. Acta 41 (14 SPEC. ISS.) (1996) 2329-2338, doi: 10.1016/ 0 013-4686(96)0 0 063-1 .
- [61] P. Bai, M.Z. Bazant, Charge transfer kinetics at the solidsolid interface in porous electrodes, Nat. Commun. 5 (2014), doi: 10.1038/ncomms4585 .
- [62] M. Doyle , T.F. Fuller , J. Newman , Modeling of galvanostatic charge and discharge of the lithium/polymer/insertion cell, J. Electrochem. Soc. 140 (6) (1993) 1526-1533 .
- [63] S. Porada , A. Shrivastava , P. Bukowska , P. Biesheuvel , K.C. Smith , Nickel hexacyanoferrate electrodes for continuous cation intercalation desalination of brackish water, Electrochim. Acta 255 (2017) 369-378 .
- [64] J. Keizer , Statistical Thermodynamics of Nonequilibrium Processes, Springer Science &amp; Business Media, 2012 .
- [65] R.B. Smith, M.Z. Bazant, Multiphase porous electrode theory, J. Electrochem. Soc. 164 (11) (2017) E3291-E3310, doi: 10.1149/2.0171711jes .
- [66] R.A. Marcus , N. Sutin , Electron transfers in chemistry and biology, Biochimica et Biophysica Acta 811 (1985) 265-322 .
- [67] W. Schmickler, A unified model for electrochemical electron and ion transfer reactions, Chem. Phys. Lett. 237 (1-2) (1995) 152-160, doi: 10.1016/ 0 0 09-2614(95)0 0286-D .
- [68] M.T. Koper, G.A. Voth, A theory for adiabatic bond breaking electron transfer reactions at metal electrodes, Chem. Phys. Lett. 282 (1) (1998) 100-106, doi: 10.1016/S0 0 092614(97)01155X .
- [69] E. Santos, K. Pötting, W. Schmickler, On the catalysis of the hydrogen oxidation, Faraday Discuss. 140 (2008) 209-218, doi: 10.1039/b802253d .
- [70] E. Santos, A. Lundin, K. Pötting, P. Quaino, W. Schmickler, Model for the electrocatalysis of hydrogen evolution, Phys. Rev. B -Condens. Matter Mater. Phys. 79 (23) (2009) 1-10, doi: 10.1103/PhysRevB.79.235436 .
- [71] C. Hartnig, M.T. Koper, Solvent reorganization in electron and ion transfer reactions near a smooth electrified surface: A molecular dynamics study, J. Am. Chem. Soc. 125 (32) (2003) 9840-9845, doi: 10.1021/ja035498u .
- [72] C. Lin, E. Laborda, C. Batchelor-McAuley, R.G. Compton, Electrical double layer effects on ion transfer reactions, Phys. Chem. Chem. Phys. 18 (14) (2016) 9829-9837, doi: 10.1039/C6CP01347C .
- [73] A .M. Limaye, A .P. Willard, Modeling interfacial electron transfer in the double layer: the interplay between electrode coupling and electrostatic driving, J. Phys. Chem. C 124 (2) (2020) 1352-1361, doi: 10.1021/acs.jpcc.9b08438 .
- [74] a. Sumi , R. Marcus , Dynamical effects in electron transfer reactions, J. Chem. Phys. 84 (9) (1986) 4 894-4 914 .
- [75] M.V. Fedorov, A .A . Kornyshev, Ionic liquids at electrified interfaces, Chem. Rev. 114 (5) (2014) 2978-3036, doi: 10.1021/cr400374x .
- [76] G. Trefalt , S.H. Behrens , M. Borkovec , Charge regulation in the electrical double layer: ion adsorption and surface interactions, Langmuir 32 (2) (2016) 380-400 .
- [77] D. Kondepudi , I. Prigogine , Modern Thermodynamics: from Heat Engines to Dissipative Structures, John Wiley &amp; Sons, 2014 .
- [78] K. Sekimoto , Stochastic Energetics, Lecture Notes in Physics, 799, Springer Berlin Heidelberg, Berlin, Heidelberg, 2010 .
- [79] R. Zwanzig , Nonequilibrium Statistical Mechanics, Oxford University Press, 2001 .
- [80] S.J. Tracy, L. Mauger, H.J. Tan, J.a. Muñoz, Y. Xiao, B. Fultz, Polaron-ion correlations in LixFePO4 studied by x-ray nuclear resonant forward scattering at elevated pressure and temperature, Phys. Rev. B 90 (9) (2014) 094303, doi: 10.1103/PhysRevB.90.094303 .
- [81] H. Risken , Fokker-Planck equation, in: The Fokker-Planck Equation, Springer, 1996, pp. 63-95 .
- [82] W. Schmickler, A theory of adiabatic electron-transfer reactions, J. Electroanal. Chem. 204 (1986) 31-43, doi: 10.1016/00220728(86)805058 .
- [83] T.R. Ferguson, M.Z. Bazant, Nonequilibrium thermodynamics of porous electrodes, J. Electrochem. Soc. 159 (12) (2012) A1967-A1985, doi: 10.1149/2. 048212jes .
- [84] N. Sutin , Theory of electron transfer reactions: insights and hindsights, Prog. Inorg. Chem 30 (1983) 441-498 .
- [85] L.D. Landau , Zur theorie der energieubertragung ii, Z. Sowjetunion 2 (1932) 46-51 .
- [86] C. Zener , Non-adiabatic crossing of energy levels, Proc. R. Soc. Lond. A 137 (833) (1932) 696-702 .
- [87] G. Makov , A. Nitzan , Solvation and ionization near a dielectric surface, J. Phys. Chem. 98 (13) (1994) 3459-3466 .
- [88] J.N. Israelachvili , Intermolecular and Surface Forces, Academic press, 2011

.

- [89] T. Maxisch, F. Zhou, G. Ceder, Ab initio study of the migration of small polarons in olivine Lix FePO4 and their association with lithium ions and vacancies, Phys. Rev. B -Condens. Matter Mater. Phys. 73 (10) (2006) 1-6, doi: 10.1103/PhysRevB.73.104301 .
- [90] M.Z. Bazant , K.T. Chu , B.J. Bayly , Current-voltage relations for electrochemical thin films, SIAM J. Appl. Math. 65 (5) (2005) 1463-1484 .
- [91] K.T. Chu , M.Z. Bazant , Electrochemical thin films at and above the classical limiting current, SIAM J. Appl. Math. 65 (5) (2005) 1485-1505 .
- [92] A. Nitzan , Chemical Dynamics in Condensed Phases: Relaxation, Transfer and Reactions in Condensed Molecular z systems, Oxford University Press, 2006 .
- [93] M.C. Henstridge, C. Batchelor-McAuley, R. Gusmo, R.G. Compton, MarcusHushChidsey theory of electron transfer to and from species bound at a non-uniform electrode surface: theory and experiment, Chem. Phys. Lett. 517 (1-3) (2011) 108-112, doi: 10.1016/j.cplett.2011.10.023 .
- [94] E. Laborda, M.C. Henstridge, C. Batchelor-McAuley, R.G. Compton, Asymmetric MarcusHush theory for voltammetry, Chem. Soc. Rev. 42 (12) (2013) 4894, doi: 10.1039/c3cs35487c .
- [95] R.W. Ballu ffi , S. Allen , W.C. Carter , Kinetics of Materials, John Wiley &amp; Sons, 2005 .
- [96] D. Emin , Polarons, Cambridge University Press, 2013 .
- [97] D. Fraggedakis , M.Z. Bazant , Tuning the stability of electrochemical interfaces by electron transfer reactions, J. Chem. Phys. 152 (18) (2020) 184703 .
- [98] F. Hayee, T.C. Narayan, N. Nadkarni, A. Baldi, A.L. Koh, M.Z. Bazant, R. Sinclair, J.A. Dionne, In-situ visualization of solute-driven phase coexistence within individual nanorods, Nat. Commun. 9 (1) (2018) 1-8, doi: 10.1038/ s41467018040211 .
- [99] N. Nitta, F. Wu, J.T. Lee, G. Yushin, Li-ion battery materials: present and future, Mater. Today 18 (5) (2015) 252-264, doi: 10.1016/j.mattod.2014.10.040 .
- [100] A. Latz, J. Zausch, Thermodynamic derivation of a ButlerVolmer model for intercalation in Li-ion batteries, Electrochim. Acta 110 (2013) 358-362, doi: 10. 1016/j.electacta.2013.06.043 .
- [101] V.A. Nikitina , S.Y. Vassiliev , K.J. Stevenson , Metal-ion coupled electron transfer kinetics in intercalation-based transition metal oxides, Adv. Energy Mater. 10 (22) (2020) 1903933 .
- [102] W. Dreyer , C. Guhlke , R. Müller , A new perspective on the electron transfer: recovering the butler-volmer equation in non-equilibrium thermodynamics, Phys. Chem. Chem. Phys. 18 (36) (2016) 24966-24983 .
- [103] P. Biesheuvel, J. Dykstra, The difference between faradaic and nonfaradaic processes in electrochemistry, arXiv: 1809.02930 (2018).
- [104] P. Bai , D.A. Cogswell , M.Z. Bazant , Suppression of phase separation in LiFePO 4 nanoparticles during battery discharge, Nano Lett. 11 (11) (2011) 4 890-4 896 .
- [105] D.A. Cogswell , M.Z. Bazant , Coherency strain and the kinetics of phase separation in LiFePO 4 nanoparticles, ACS Nano 6 (3) (2012) 2215-2225 .
- [106] Y. Li, H. Chen, K. Lim, H.D. Deng, J. Lim, D. Fraggedakis, P.M. Attia, S.C. Lee, N. Jin, J. Mo š kon, Z. Guan, W.E. Gent, J. Hong, Y.S. Yu, M. Gaber š ˇ cek, M.S. Islam, M.Z. Bazant, W.C. Chueh, Fluid-enhanced surface diffusion controls intraparticle phase transformations, Nat. Mater. 17 (10) (2018) 915-922, doi: 10. 1038/s4156301801684 .
- [107] N. Nadkarni , E. Rejovitzky , D. Fraggedakis , C.V. Di Leo , R.B. Smith , P. Bai , M.Z. Bazant , Interplay of phase boundary anisotropy and electro-autocatalytic surface reactions on the lithium intercalation dynamics Li X FePO 4 Platelet-like Nanoparticles, Phys. Rev. Mater. (2018) (2018) .
- [108] N. Nadkarni , T. Zhou , D. Fraggedakis , T. Gao , M.Z. Bazant , Modeling the metal-insulator phase transition in lixcoo2 for energy and information storage, Adv. Funct. Mater. 29 (40) (2019) 1902821 .
- [109] N. Besnard , A. Etiemble , T. Douillard , O. Dubrunfaut , P. Tran-Van , L. Gautier , S. Franger , J.-C. Badot , E. Maire , B. Lestriez , Multiscale morphological and electrical characterization of charge transport limitations to the power performance of positive electrode blends for lithium-ion batteries, Adv. Energy Mater. 7 (8) (2017) 1602239 .
- [110] D. Fraggedakis , N. Nadkarni , T. Gao , T. Zhou , Y. Zhang , Y. Han , R.M. Stephens , Y. Shao-Horn , M.Z. Bazant , A scaling law to determine phase morphologies during ion intercalation, Energy Environ. Sci. 13 (2020) 2142-2152 .
- [111] D.A. Cogswell, W.C. Carter, Thermodynamic phase-field model for microstructure with multiple components and phases: the possibility of metastable phases, Phys. Rev. E 83 (6) (2011), doi: 10.1103/PhysRevE.83.061602 .
- [112] D.A. Cogswell, M.Z. Bazant, Theory of coherent nucleation in phase-separating nanoparticles, Nano Lett. 13 (7) (2013) 3036-3041, doi: 10.1021/nl400497t .
- [113] J.W. Cahn , J.E. Hilliard , Free energy of a nonuniform system. I. Interfacial free energy, J. Chem. Phys. 28 (1958) 258 .
- [114] V. Srinivasan, J. Newman, Discharge model for the lithium iron-phosphate electrode, J. Electrochem. Soc. 151 (10) (2004) A1517, doi: 10.1149/1.1785012 .
- [115] T.F. Fuller , M. Doyle , J. Newman , Relaxation phenomena in lithium-ion-insertion cells, J. Electrochem. Soc. 141 (4) (1994) 982-990 .
- [116] J. Newman , W. Tiedemann , Porous-electrode theory with battery applications, AIChE J. 21 (1) (1975) 25-41 .
- [117] P. Bai, G. Tian, Statistical kinetics of phase-transforming nanoparticles in LiFePO 4 porous electrodes, Electrochim. Acta 89 (2013) 644-651, doi: 10.1016/ j.electacta.2012.11.070 .

- [118] W. Dreyer , J. Jamnik , C. Guhlke , R. Huth , J. Mokon , M. Gaberek , The thermodynamic origin of hysteresis in insertion batteries, Nat. Mater. 9 (5) (2010) 448-453 .
- [119] M. Doyle , J. Newman , A.S. Gozdz , C.N. Schmutz , J.-M. Tarascon , Comparison of modeling predictions with experimental data from plastic lithium ion cells, J. Electrochem. Soc. 143 (6) (1996) 1890-1903 .
- [120] C. Heubner , M. Schneider , A. Michaelis , Investigation of charge transfer kinetics of li-intercalation in lifepo4, J. Power Sources 288 (2015) 115-120 .
- [121] J.S. Newman, C.W. Tobias, Theoretical analysis of current distribution in porous electrodes, J. Electrochem. Soc. 109 (12) (1962) 1183, doi: 10.1149/1. 2425269 .
- [122] D. Fraggedakis , C. Kouris , Y. Dimakopoulos , J. Tsamopoulos , Flow of two immiscible fluids in a periodically constricted tube: transitions to stratified, segmented, churn, spray, or segregated flow, Phys. Fluids 27 (8) (2015) 082102 .
- [123] D. Fraggedakis , J. Papaioannou , Y. Dimakopoulos , J. Tsamopoulos , Discretization of three-dimensional free surface flows and moving boundary problems via elliptic grid methods based on variational principles, J. Comput. Phys. 344 (2017) 127-150 .
- [124] E.L. Crow , K. Shimizu , Lognormal Distributions, Marcel Dekker New York, 1987 .
- [125] J. Nocedal , S. Wright , Numerical Optimization, Springer Science &amp; Business Media, 2006 .
- [126] R.B. Smith, E. Khoo, M.Z. Bazant, Intercalation kinetics in multiphase-layered materials, J. Phys. Chem. C 121 (23) (2017) 12505-12523, doi: 10.1021/acs.jpcc. 7b00185 .
- [127] T.R. Ferguson, M.Z. Bazant, Phase transformation dynamics in porous battery electrodes, Electrochim. Acta 146 (2014) 89-97, doi: 10.1016/j.electacta.2014. 08.083 .
- [128] K.E. Thomas-Alyea , C. Jung , R.B. Smith , M.Z. Bazant , In situ observation and mathematical modeling of lithium distribution within graphite, J. Electrochem. Soc. 164 (11) (2017) E3063-E3072 .
- [129] N.J. de Klerk , A. Vasileiadis , R.B. Smith , M.Z. Bazant , M. Wagemaker , Explaining key properties of lithiation in TiO 2-anatase li-ion battery electrodes using phase-field modeling, Phys. Rev. Mater. 1 (2) (2017) 025404 .
- [130] Y. Li, W.C. Chueh, Electrochemical and chemical insertion for energy transformation and switching, Ann. Rev. Mater. Res. 48 (5) (2018) 1-29, doi: 10.1146/ annurevmatsci070317124525 .
- [131] A. Vasileiadis , N.J. de Klerk , R.B. Smith , S. Ganapathy , P.P.R. Harks , M.Z. Bazant , M. Wagemaker , Toward optimal performance and in-depth understanding of spinel Li4Ti5O12 electrodes through phase field modeling, Adv. Funct. Mater. 28 (16) (2018) 1705992 .
- [132] J.C. Gonzalez-Rosillo , M. Balaish , Z.D. Hood , N. Nadkarni , D. Fraggedakis , K.J. Kim , K.M. Mullin , R. Pfenninger , M.Z. Bazant , J.L. Rupp , Lithium-battery anode gains additional functionality for neuromorphic computing through metal-insulator phase separation, Adv. Mater. 32 (9) (2020) 1907465 .
- [133] E.J. Fuller , F.E. Gabaly , F. Léonard , S. Agarwal , S.J. Plimpton , R.B. Jacobs-Gedrim , C.D. James , M.J. Marinella , A .A . Talin , Li-ion synaptic transistor for low power analog computing, Adv. Mater. 29 (4) (2017) 1604310 .
- [134] D. Fraggedakis , M. Mirzadeh , T. Zhou , M.Z. Bazant , Dielectric breakdown by electric-field induced phase separation, J. Electrochem. Soc. 167 (2020) 113504 .
- [135] V. Palomares , P. Serras , I. Villaluenga , K.B. Hueso , J. Carretero-González , T. Rojo , Na-ion batteries, recent advances and present challenges to become low cost energy storage systems, Energy Environ. Sci. 5 (3) (2012) 5884-5901 .
- [136] T. Zhang , M. Kamlah , Sodium ion batteries particles: Phase-field modeling with coupling of cahn-hilliard equation and finite deformation elasticity, J. Electrochem. Soc. 165 (10) (2018) A1997 .
- [137] K.C. Smith , Theoretical evaluation of electrochemical cell architectures using cation intercalation electrodes for desalination, Electrochim. Acta 230 (2017) 333-341 .
- [138] N. Jayaprakash , S. Das , L. Archer , The rechargeable aluminum-ion battery, Chem. Commun. 47 (47) (2011) 12610-12612 .
- [139] T. Leisegang , F. Meutzner , M. Zschornak , W. Münchgesang , R. Schmid , T. Nestler , R.A. Eremin , A.A. Kabanov , V.A. Blatov , D.C. Meyer , The aluminum-ion battery: a sustainable and seminal concept? Front. Chem. 7 (2019) 268 .
- [140] J. Hwang, R.R. Rao, L. Giordano, Y. Katayama, Y. Yu, Y. Shao-Horn, Perovskites in catalysis and electrocatalysis, Science 358 (6364) (2017) 751-756, doi: 10. 1126/science.aam7092 .
- [141] R.M. Ormerod, Solid oxide fuel cells, Chem. Soc. Rev. 32 (1) (2003) 17-28, doi: 10.1039/b105764m .
- [142] J. Suntivich, H.A. Gasteiger, N. Yabuuchi, H. Nakanishi, J.B. Goodenough, Y. Shao-Horn, Design principles for oxygen-reduction activity on perovskite oxide catalysts for fuel cells and metal-air batteries, Nat. Chem. 3 (7) (2011) 546-550, doi: 10.1038/nchem.1069 .
- [143] Y.D. Li, S.X. Zhao, C.W. Nan, B.H. Li, Electrochemical performance of SiO2coated LiFePO4 cathode materials for lithium ion battery, J. Alloys Compd. 509 (3) (2011) 957-960, doi: 10.1016/j.jallcom.2010.08.154 .
- [144] K.-S. Park, P. Xiao, S.-Y. Kim, A. Dylla, Y.-M. Choi, G. Henkelman, K.J. Stevenson, J.B. Goodenough, Enhanced charge-transfer kinetics by anion surface modification of LiFePO 4 , Chem. Mater. 24 (16) (2012) 3212-3218, doi: 10.1021/ cm301569m .
- [145] J. Song, B. Sun, H. Liu, Z. Ma, Z. Chen, G. Shao, G. Wang, Enhancement of the Rate Capability of LiFePO4 by a New Highly Graphitic Carbon-Coating Method, ACS Appl. Mater. Interfaces 8 (24) (2016) 15225-15231, doi: 10.1021/ acsami.6b02567 .
- [146] Z.-X. Chi, W. Zhang, F.-Q. Cheng, J.-T. Chen, A.-M. Cao, L.-J. Wan, Optimizing the carbon coating on LiFePO4 for improved battery performance, RSC Adv. 4 (15) (2014) 7795, doi: 10.1039/c3ra47702a .
- [147] J. Wang, X. Sun, Understanding and recent development of carbon coating on LiFePO &lt; sub&gt;4 &lt; /sub&gt; cathode materials for lithium-ion batteries, Energy Environ. Sci. 5 (1) (2012) 5163-5185, doi: 10.1039/C1EE01263K .
- [148] Y. Lin, Y. Len, T. Zhou, G. Zhao, Y. Huang, Z. Huang, Enhanced electrochemical performances of LiFePO 4 /C by surface modification with Sn nanoparticles, J. Power Sources 226 (2013) 20-26, doi: 10.1016/j.jpowsour.2012.10.074 .
- [149] J. Wang, X. Sun, Olivine LiFePO4: the remaining challenges for future energy storage, Energy Environ. Sci. (2015), doi: 10.1039/C4EE04016C .
- [150] J.B. Goodenough, K.S. Park, The Li-ion rechargeable battery: a perspective, J. Am. Chem. Soc. 135 (4) (2013) 1167-1176, doi: 10.1021/ja3091438 .
- [151] P.-C. Tsai , B. Wen , M. Wolfman , M.-J. Choe , M.S. Pan , L. Su , K. Thornton , J. Cabana , Y.-M. Chiang , Single-particle measurements of electrochemical kinetics in NMC and NCA cathodes for li-ion batteries, Energy Environ. Sci. 11 (4) (2018) 860-871 .
- [152] Y. Zhang , Y. Katayama , R. Tatara , L. Giordano , Y. Yu , D. Fraggedakis , J.G. Sun , F. Maglia , R. Jung , M.Z. Bazant , et al. , Revealing electrolyte oxidation via carbonate dehydrogenation on ni-based oxides in li-ion batteries by in situ fourier transform infrared spectroscopy, Energy Environ. Sci. 13 (1) (2020) 183-199 .
- [153] B. Horstmann, B. Gallant, R. Mitchell, W.G. Bessler, Y. Shao-Horn, M.Z. Bazant, Rate-Dependent Morphology of Li 2 O 2 Growth in LiO 2 Batteries, J. Phys. Chem. Lett. 4 (24) (2013) 4217-4222, doi: 10.1021/jz401973c .
- [154] H. Zhao , M.Z. Bazant , Population dynamics of driven autocatalytic reactive mixtures, Phys. Rev. E 100 (2019) 012144 .
- [155] J. Erlebacher, M.J. Aziz, A. Karma, N. Dimitrov, K. Sieradzki, Evolution of nanoporosity in dealloying, Nature 410 (6827) (2001) 450-453, doi: 10.1038/ 35068529 .
- [156] J. Mandal, D. Wang, A.C. Overvig, N.N. Shi, D. Paley, A. Zangiabadi, Q. Cheng, K. Barmak, N. Yu, Y. Yang, Scalable, dip-and-dry fabrication of a wide-angle plasmonic selective absorber for high-e ffi ciency solar thermal energy conversion, Adv. Mater. 29 (41) (2017) 1-9, doi: 10.1002/adma.201702156 .
- [157] R. Koerver, I. Aygün, T. Leichtweiß, C. Dietrich, W. Zhang, J.O. Binder, P. Hartmann, W.G. Zeier, J. Janek, Capacity fade in solid-state batteries: interphase formation and chemomechanical processes in nickel-rich layered oxide cathodes and lithium thiophosphate solid Electrolytes, Chem. Mater. 29 (13) (2017) 5574-5582, doi: 10.1021/acs.chemmater.7b00931 .
- [158] A.C. Luntz, J. Voss, K. Reuter, Interfacial challenges in solid-state Li Ion batteries, J. Phys. Chem. Lett. 6 (22) (2015) 4599-4604, doi: 10.1021/acs.jpclett. 5b02352 .
- [159] A .A . Kornyshev, M.A . Vorotyntsev, Aspects of conductivity and space charge phenomena in solid electrolytes, Electrochim. Acta 23 (3) (1978) 267-270, doi: 10.1016/00134686(78)850567 .
- [160] A .A . Kornyshev , M.A . Vorotyntsev , Conductivity and space charge phenomena in solid electrolytes with one mobile charge carrier species, a review with original material, Electrochim. Acta 26 (3) (1981) 303-323 .
- [161] F. Han, A.S. Westover, J. Yue, X. Fan, F. Wang, M. Chi, D.N. Leonard, N.J. Dudney, H. Wang, C. Wang, High electronic conductivity as the origin of lithium dendrite formation within solid electrolytes, Nat. Energy 4 (3) (2019) 187196, doi: 10.1038/s415600180312-z .
- [162] E. Santos , A. Lundin , K. Pltting , P. Quaino , W. Schmickler , Model for the electrocatalysis of hydrogen evolution, Phys. Rev. B 79 (23) (2009) 235436 .
- [163] Y.-C. Lam , A.V. Soudackov , Z.K. Goldsmith , S. Hammes-Schiffer , Theory of proton discharge on metal electrodes: Electronically adiabatic model, J. Phys. Chem. C 123 (19) (2019) 12335-12345 .
- [164] J. Huang , S. Chen , Interplay between covalent and noncovalent interactions in electrocatalysis, J. Phys. Chem. C 122 (47) (2018) 26910-26921 .