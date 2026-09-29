# Awesome Fusion Energy

> Every code, dataset, and learning resource you need to work on fusion energy — in one place.

Fusion is being built in the open more than ever before: equilibrium solvers, gyrokinetic turbulence codes, neutronics toolchains, whole-plant systems codes, and open experimental data are all a `git clone` away — if you know where to look. This list is the map. It covers the software, the data, and the places to learn, with the license status of every entry marked so you know what you can run today and what needs a signature first.

Maintained by [fusion-commons](https://github.com/fusion-commons). Founded and maintained by [Kronos Fusion Energy](https://www.kronosfusionenergy.com). Contributions welcome — see [Contributing](#contributing).

## Legend

| Mark | Meaning |
|------|---------|
| 🟢 | Open source — clone and run today |
| 🟡 | Free for research, but requires registration or a signed user agreement |
| 🔴 | Restricted distribution (export-controlled or institution-only) |

## Contents

- [Simulation codes](#simulation-codes)
  - [Plasma equilibrium & MHD](#plasma-equilibrium--mhd)
  - [Gyrokinetics, turbulence & transport](#gyrokinetics-turbulence--transport)
  - [Integrated modeling & systems codes](#integrated-modeling--systems-codes)
  - [Edge, scrape-off layer & divertor](#edge-scrape-off-layer--divertor)
  - [Particle-in-cell & kinetic codes](#particle-in-cell--kinetic-codes)
  - [Stellarator design & optimization](#stellarator-design--optimization)
  - [Heating, current drive & RF](#heating-current-drive--rf)
  - [Neutronics, activation & shielding](#neutronics-activation--shielding)
  - [Materials & fuel cycle](#materials--fuel-cycle)
  - [Plasma control, machine learning & quantum](#plasma-control-machine-learning--quantum)
  - [Diagnostics & synthetic diagnostics](#diagnostics--synthetic-diagnostics)
  - [Inertial confinement & high-energy-density](#inertial-confinement--high-energy-density)
  - [General plasma frameworks & utilities](#general-plasma-frameworks--utilities)
- [Data](#data)
  - [Open experimental & simulation datasets](#open-experimental--simulation-datasets)
  - [Atomic, molecular & nuclear data](#atomic-molecular--nuclear-data)
  - [Standards & interoperability](#standards--interoperability)
- [Learning](#learning)
  - [Textbooks & foundational papers](#textbooks--foundational-papers)
  - [Courses & lectures](#courses--lectures)
  - [Hands-on workshops](#hands-on-workshops)
- [Community](#community)
- [Getting access to licensed codes](#getting-access-to-licensed-codes)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Simulation codes

### Plasma equilibrium & MHD

- 🟢 [DESC](https://github.com/PlasmaControl/DESC) — Stellarator and tokamak equilibrium, stability, and optimization suite built on pseudo-spectral methods and automatic differentiation. Python.
- 🟢 [FreeGS](https://github.com/freegs-plasma/freegs) — Free-boundary Grad–Shafranov equilibrium solver for tokamaks, well suited to scenario design and control studies. Python.
- 🟢 [FreeQDSK](https://github.com/freegs-plasma/FreeQDSK) — Reader/writer for the G-EQDSK, A-EQDSK, and P-EQDSK equilibrium file formats. Python.
- 🟢 [Open FUSION Toolkit](https://github.com/openfusiontoolkit/OpenFUSIONToolkit) — Suite of tools for fusion simulation, including the TokaMaker Grad–Shafranov solver and 3D MHD capabilities. Fortran/Python.
- 🟢 [PARVMEC](https://github.com/ORNL-Fusion/PARVMEC) — Parallel version of the VMEC 3D ideal-MHD equilibrium code, the workhorse of stellarator equilibrium. Fortran.
- 🟢 [SPEC](https://github.com/PrincetonUniversity/SPEC) — Stepped-Pressure Equilibrium Code: 3D MHD equilibria with islands and chaotic fields via multi-region relaxed MHD. Fortran.
- 🟢 [VMEC2000](https://github.com/hiddenSymmetries/VMEC2000) — VMEC build with a Python wrapper and CMake tooling, maintained for the SIMSOPT optimization ecosystem. Fortran/Python.
- 🟡 [EFIT](https://omfit.io/modules/mod_EFIT.html) — The standard tokamak equilibrium reconstruction code from General Atomics; commonly run through OMFIT, access via GA. Fortran.
- 🟡 [JOREK](https://www.jorek.eu) — Nonlinear extended-MHD code for disruptions, ELMs, and 3D instabilities in divertor tokamaks; consortium membership required. Fortran.
- 🟡 [M3D-C1](https://m3dc1.pppl.gov) — High-order 3D extended-MHD code from PPPL for tokamak stability and disruption modeling; request access from PPPL. Fortran.
- 🟡 [NIMROD](https://nimrodteam.org) — Nonlinear 3D extended-MHD code used widely for macroscopic stability; access via the NIMROD team. Fortran.

### Gyrokinetics, turbulence & transport

- 🟢 [GACODE](https://github.com/gafusion/gacode) — General Atomics suite: CGYRO (gyrokinetic turbulence), TGLF (quasilinear transport), NEO (neoclassical), and TGYRO (transport solver). Fortran.
- 🟢 [Gkeyll](https://github.com/ammarhakim/gkylzero) — Modern C/CUDA framework for gyrokinetic, Vlasov–Maxwell, and multi-moment fluid simulation on GPUs. C.
- 🟢 [GKW](https://bitbucket.org/gkw/gkw/src) — Global and flux-tube nonlinear gyrokinetic code for turbulence in rotating plasmas. Fortran.
- 🟢 [QuaLiKiz](https://gitlab.com/qualikiz-group/QuaLiKiz) — Fast quasilinear gyrokinetic transport model, widely used inside integrated modeling loops and as a neural-network surrogate. Fortran.
- 🟢 [stella](https://github.com/stellaGK/stella) — Operator-split gyrokinetic code built for stellarator turbulence and mixed implicit/explicit timestepping. Fortran.
- 🟡 [GENE](https://genecode.org) — Flagship Eulerian gyrokinetic turbulence code (flux-tube to global, tokamaks and stellarators); free after signing a user agreement. Fortran.
- 🟡 [GS2](https://bitbucket.org/gyrokinetics/gs2) — Pioneering flux-tube gyrokinetic code for tokamak and stellarator microinstability and turbulence studies. Fortran.
- 🟡 [XGC](https://xgc.pppl.gov) — Whole-volume gyrokinetic particle-in-cell code for edge and core, scaling to exascale machines; request access from PPPL. Fortran/C++.

### Integrated modeling & systems codes

- 🟢 [Bluemira](https://github.com/Fusion-Power-Plant-Framework/bluemira) — Integrated design framework for fusion power plants: reactor geometry, magnets, balance of plant, and optimization. Python.
- 🟢 [cfspopcon](https://github.com/cfs-energy/cfspopcon) — Fast 0-D plasma operating-contour (POPCON) analysis from Commonwealth Fusion Systems. Python.
- 🟢 [FUSE](https://github.com/ProjectTorreyPines/FUSE.jl) — Whole-facility fusion simulator from General Atomics: plasma, engineering, and costing in one differentiable Julia stack. Julia.
- 🟢 [PROCESS](https://github.com/ukaea/PROCESS) — UKAEA systems code for self-consistent fusion power plant design points and trade studies. Python/Fortran.
- 🟢 [TORAX](https://github.com/google-deepmind/torax) — Differentiable tokamak core transport simulator in JAX from Google DeepMind, built for fast scenario optimization and ML coupling. Python.
- 🟢 [Kronos Toolkit](https://github.com/KronosFE/kronos-toolkit) — Anchor-tested Python research engine reproducing the published Kronos Fusion Energy physics register end-to-end. Python.
- 🟡 [OMFIT](https://omfit.io) — One Modeling Framework for Integrated Tasks: the glue framework connecting dozens of fusion codes and experimental databases; free registration. Python.
- 🟡 [TRANSP](https://transp.pppl.gov) — The reference tokamak time-dependent transport analysis and prediction code, run as a service by PPPL. Fortran.

### Edge, scrape-off layer & divertor

- 🟢 [BOUT++](https://github.com/boutproject/BOUT-dev) — Framework for plasma fluid and turbulence simulation in general curvilinear geometry, the base for many edge codes. C++.
- 🟢 [Hermes-3](https://github.com/boutproject/hermes-3) — Hot-ion multifluid drift-reduced model for tokamak edge and scrape-off-layer transport, built on BOUT++. C++.
- 🟢 [SD1D](https://github.com/boutproject/SD1D) — 1D divertor leg model of plasma–neutral interaction and detachment, built on BOUT++. C++.
- 🟢 [UEDGE](https://github.com/LLNL/UEDGE) — 2D fluid code for plasma and neutrals in the tokamak edge, from LLNL, with a Python interface. Fortran/Python.
- 🟡 [EIRENE](https://www.eirene.de) — Kinetic Monte Carlo neutral particle and radiation transport code, the neutrals engine inside SOLPS-ITER. Fortran.
- 🟡 [SOLPS-ITER](https://www.iter.org/) — The standard coupled plasma/neutrals code package for divertor and scrape-off-layer design, maintained by the ITER Organization; access by agreement.

### Particle-in-cell & kinetic codes

- 🟢 [EPOCH](https://github.com/Warwick-Plasma/epoch) — Widely used relativistic particle-in-cell code for laser–plasma interaction and kinetic physics. Fortran.
- 🟢 [PIConGPU](https://github.com/ComputationalRadiationPhysics/picongpu) — Fully relativistic, many-GPU particle-in-cell code with best-in-class performance. C++.
- 🟢 [Smilei](https://github.com/SmileiPIC/Smilei) — Collaborative open particle-in-cell code for fusion, laser–plasma, and astrophysical kinetic simulation. C++/Python.
- 🟢 [VPIC](https://github.com/lanl/vpic) — Los Alamos 3D relativistic kinetic particle-in-cell code, built for extreme scale. C++.
- 🟢 [WarpX](https://github.com/BLAST-WarpX/warpx) — Exascale mesh-refined particle-in-cell code (2022 Gordon Bell Prize) for kinetic plasma and accelerator modeling. C++/Python.

### Stellarator design & optimization

- 🟢 [booz_xform](https://github.com/hiddenSymmetries/booz_xform) — Transforms stellarator equilibria to Boozer coordinates, with Python bindings. C++/Python.
- 🟢 [FOCUS](https://github.com/PrincetonUniversity/FOCUS) — Flexible optimized coil design using space curves — finds buildable coils for stellarators. Fortran.
- 🟢 [pyQSC](https://github.com/landreman/pyQSC) — Near-axis expansion for rapid design of quasisymmetric stellarator configurations. Python.
- 🟢 [REGCOIL](https://github.com/landreman/regcoil) — Regularized winding-surface coil optimization for stellarators. Fortran.
- 🟢 [SIMSOPT](https://github.com/hiddenSymmetries/simsopt) — Flexible stellarator optimization framework tying together VMEC, SPEC, coil design, and gradient-based optimization. Python/C++.
- 🟢 [STELLOPT](https://github.com/PrincetonUniversity/STELLOPT) — The classic stellarator equilibrium optimization suite, including BEAMS3D and DIAGNO. Fortran.

### Heating, current drive & RF

- 🟢 [Petra-M](https://github.com/piScope/PetraM_Base) — Finite-element RF wave simulation framework (built on MFEM) used for ICRF antenna-to-core modeling. Python.
- 🟢 [Scotty](https://github.com/beam-tracing/Scotty) — Beam-tracing code for Doppler backscattering and microwave beam propagation in fusion plasmas. Python.
- 🟡 [GENRAY / CQL3D](https://www.compxco.com) — Ray-tracing and 3D Fokker–Planck package for RF heating and current drive, from CompX. Fortran.

### Neutronics, activation & shielding

- 🟢 [ALARA](https://github.com/svalinn/ALARA) — Activation, decay-heat, and dose analysis code designed for fusion energy systems. C++.
- 🟢 [DAGMC](https://github.com/svalinn/DAGMC) — Direct Accelerated Geometry Monte Carlo: run neutronics directly on CAD geometry with OpenMC, MCNP, and more. C++.
- 🟢 [Geant4](https://geant4.web.cern.ch) — CERN's general-purpose particle transport toolkit, used for shielding and detector studies. C++.
- 🟢 [OpenMC](https://github.com/openmc-dev/openmc) — Community Monte Carlo neutron and photon transport code — the open standard for fusion neutronics. C++/Python.
- 🟢 [Paramak](https://github.com/fusion-energy/paramak) — Parametric CAD models of fusion reactors, ready for neutronics workflows. Python.
- 🟢 [PyNE](https://github.com/pyne/pyne) — Nuclear engineering toolkit: nuclear data, cross sections, transmutation, and mesh utilities. Python/C++.
- 🟢 [HYPERION activation study](https://github.com/KronosFE/hyperion-activation) — Worked open OpenMC R2S example: activation, waste classification, and shutdown dose for a breeder blanket. Python.
- 🟡 [FISPACT-II](https://fispact.ukaea.uk) — UKAEA inventory code for activation, transmutation, and waste; the fusion-standard companion to TENDL data. Fortran.
- 🟡 [Serpent](https://serpent.vtt.fi) — Continuous-energy Monte Carlo transport and burnup code from VTT with strong fusion adoption. C.
- 🔴 [MCNP](https://rsicc.ornl.gov) — The reference general Monte Carlo N-Particle transport code; export-controlled, distributed through RSICC.

### Materials & fuel cycle

- 🟢 [FESTIM](https://github.com/festim-dev/FESTIM) — Finite-element hydrogen/tritium transport in materials: trapping, permeation, and thermal fields. Python.
- 🟢 [LAMMPS](https://github.com/lammps/lammps) — Molecular dynamics workhorse for radiation damage and plasma-facing materials studies. C++.
- 🟢 [MOOSE](https://github.com/idaholab/moose) — Idaho National Laboratory's multiphysics finite-element framework underlying many fusion materials and blanket tools. C++.
- 🟢 [TMAP8](https://github.com/idaholab/TMAP8) — Tritium Migration Analysis Program, rebuilt on MOOSE — the standard for fuel-cycle tritium safety analysis. C++.
- 🟡 [SRIM](http://www.srim.org) — Stopping and Range of Ions in Matter — the classic ion-implantation and sputtering tables; free binaries, closed source.

### Plasma control, machine learning & quantum

- 🟢 [disruption-py](https://github.com/MIT-PSFC/disruption-py) — Open workflow from MIT PSFC for building disruption-prediction databases from tokamak shots. Python.
- 🟢 [FRNN](https://github.com/PPPLDeepLearning/plasma-python) — Fusion Recurrent Neural Network — deep learning for disruption prediction from PPPL. Python.
- 🟢 [KODEX](https://github.com/KronosFE/kronos-ml) — The Kronos family of codes: benchmarked AI/ML fusion surrogates and physics tools, published in versioned releases. Python.
- 🟢 [kronos-quantum](https://github.com/KronosFE/kronos-quantum) — Runnable quantum-computing-for-fusion codes — honest simulators today, designed to be hardware-ready as the field matures. Python.
- 🟢 [TORAX](https://github.com/google-deepmind/torax) — Also listed under integrated modeling: its differentiability makes it a natural base for control and ML research. Python.

### Diagnostics & synthetic diagnostics

- 🟢 [Cherab](https://github.com/cherab/core) — Spectroscopic modeling framework for synthetic diagnostics, built on the Raysect ray-tracer. Python.
- 🟢 [FIDASIM](https://github.com/D3DEnergetic/FIDASIM) — Synthetic fast-ion D-alpha and neutral-beam diagnostic modeling. Fortran.
- 🟢 [Raysect](https://github.com/raysect/source) — Scientific ray-tracing engine powering Cherab's synthetic camera and spectrometer views. Python.

### Inertial confinement & high-energy-density

- 🟢 [Flash-X](https://flash-x.org) — Multiphysics adaptive-mesh radiation-hydrodynamics code with a long heritage in HED and laboratory astrophysics. Fortran.
- Note: the production ICF radiation-hydrodynamics codes (HYDRA, xRAGE, and kin) are export-controlled and are not publicly distributed; EPOCH, Smilei, and WarpX above cover much of the open kinetic side of HED science.

### General plasma frameworks & utilities

- 🟢 [MDSplus](https://github.com/MDSplus/mdsplus) — The data acquisition and storage system used by most magnetic fusion experiments worldwide. C/Python.
- 🟢 [OMAS](https://github.com/gafusion/omas) — Ordered Multidimensional Array Structure — Python data-schema layer implementing the ITER IMAS ontology. Python.
- 🟢 [PlasmaPy](https://github.com/PlasmaPy/PlasmaPy) — The community Python package for plasma physics: formulary, particles, diagnostics, and simulation primitives. Python.
- 🟢 [fusion-energy org](https://github.com/fusion-energy) — GitHub organization of open fusion neutronics tools and workflows surrounding OpenMC, DAGMC, and Paramak.
- 🟢 [MFEM](https://github.com/mfem/mfem) — Lightweight scalable finite-element library from LLNL, the numerical engine under several fusion codes. C++.

---

## Data

### Open experimental & simulation datasets

- 🟢 [FAIR MAST](https://mastapp.site) — UKAEA's open data service for the MAST spherical tokamak: thousands of shots, browsable and downloadable.
- 🟢 [SPARCPublic](https://github.com/cfs-energy/SPARCPublic) — Commonwealth Fusion Systems' public SPARC design data: equilibria, profiles, and reference scenarios.
- 🟢 [ITER Organization on GitHub](https://github.com/iterorganization) — ITER's open-source releases, including the IMAS data infrastructure and physics codes.
- 🟢 [Zenodo — fusion energy records](https://zenodo.org/search?q=%22fusion%20energy%22) — CERN-hosted open repository where fusion datasets, code archives, and supplementary material receive citable DOIs. Kronos Fusion Energy's open research archive is published here.
- 🟢 [IAEA Nuclear Data Services](https://www-nds.iaea.org) — The IAEA's portal of evaluated nuclear data libraries and related services.

### Atomic, molecular & nuclear data

- 🟢 [OPEN-ADAS](https://open.adas.ac.uk) — Freely downloadable subset of the Atomic Data and Analysis Structure: ionization, recombination, and radiation rates for fusion plasmas.
- 🟢 [IAEA AMDIS](https://amdis.iaea.org) — Atomic and molecular data for fusion, including the ALADDIN database and CollisionDB.
- 🟢 [NIST Atomic Spectra Database](https://physics.nist.gov/asd) — Reference wavelengths, energy levels, and transition probabilities.
- 🟢 [FENDL](https://www-nds.iaea.org/fendl/) — Fusion Evaluated Nuclear Data Library — the IAEA-curated nuclear data library for fusion neutronics.
- 🟢 [ENDF/B (NNDC)](https://www.nndc.bnl.gov/endf/) — The US evaluated nuclear data file, from Brookhaven's National Nuclear Data Center.
- 🟢 [TENDL](https://tendl.web.psi.ch/home.html) — TALYS-based evaluated nuclear data library, the standard companion to FISPACT-II activation calculations ([NEA Data Bank mirror](https://databank.io.oecd-nea.org/data/tendl/)).
- 🟢 [JEFF (OECD NEA)](https://www.oecd-nea.org/dbdata/jeff/) — The Joint Evaluated Fission and Fusion nuclear data library from the OECD Nuclear Energy Agency.

### Standards & interoperability

- 🟢 [IMAS Data Dictionary](https://github.com/iterorganization/imas-data-dictionary) — The ITER-standard ontology for describing fusion experiments and simulations.
- 🟢 [IMAS-Python](https://github.com/iterorganization/imas-python) — Pure-Python library for reading and writing IMAS data structures.
- 🟢 [OMAS](https://github.com/gafusion/omas) — Practical Python implementation of the IMAS schema over NetCDF/HDF5/JSON (also listed under frameworks).
- 🟢 [FreeQDSK](https://github.com/freegs-plasma/FreeQDSK) — The de-facto G-EQDSK equilibrium exchange format, implemented cleanly (also listed under equilibrium).

---

## Learning

### Textbooks & foundational papers

- [Freidberg, *Plasma Physics and Fusion Energy*](https://doi.org/10.1017/CBO9780511755705) — The standard first textbook for fusion-oriented plasma physics.
- [Chen, *Introduction to Plasma Physics and Controlled Fusion*](https://link.springer.com/book/10.1007/978-3-319-22309-4) — The classic gentle introduction to plasma physics.
- [Wesson & Campbell, *Tokamaks*](https://global.oup.com/academic/product/tokamaks-9780198509226) — The encyclopedic reference on tokamak physics and engineering.
- [Progress in the ITER Physics Basis](https://iopscience.iop.org/article/10.1088/0029-5515/47/6/S01) — The community-consensus physics basis for burning-plasma tokamaks, open access in *Nuclear Fusion*.

### Courses & lectures

- [MIT OCW 22.611J — Introduction to Plasma Physics I](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/) — Full graduate course materials, free.
- [MIT OCW 22.012 — Seminar: Fusion and Plasma Physics](https://ocw.mit.edu/courses/22-012-seminar-fusion-and-plasma-physics-spring-2006/) — Approachable seminar-style introduction to fusion from MIT.
- [PPPL Graduate Summer School](https://gss.pppl.gov) — Annual one-week plasma physics school with archived lectures.
- [DOE Fusion Energy Sciences](https://www.energy.gov/science/fes/fusion-energy-sciences) — Program overviews and primers from the US fusion science office.

### Hands-on workshops

- 🟢 [Fusion Neutronics Workshop](https://github.com/fusion-energy/neutronics-workshop) — Self-paced Jupyter workshop covering OpenMC, DAGMC, and Paramak for fusion neutronics.
- 🟢 [PlasmaPy example gallery](https://docs.plasmapy.org/en/stable/examples.html) — Notebook examples for computational plasma physics in Python.

## Community

- [Fusion Industry Association](https://www.fusionindustryassociation.org) — The trade association of private fusion companies; publishes the annual industry report.
- [Fusion Energy Base](https://www.fusionenergybase.com) — Tracking of fusion companies, projects, and technologies.
- [ITER Newsline](https://www.iter.org/news) — News from the world's largest fusion project.
- [EUROfusion](https://euro-fusion.org) — The European fusion research consortium.
- [APS Division of Plasma Physics](https://engage.aps.org/dpp/home) — The main US plasma physics society and annual meeting.
- [GitHub topic: nuclear-fusion](https://github.com/topics/nuclear-fusion) · [plasma-physics](https://github.com/topics/plasma-physics) — Live feeds of open fusion repositories.
- Sibling lists: [awesome-nuclear](https://github.com/paulromano/awesome-nuclear) · [awesome-ML-in-plasma-physics](https://github.com/kharitonov-ivan/awesome-ML-in-plasma-physics) · [List of plasma physics software (Wikipedia)](https://en.wikipedia.org/wiki/List_of_plasma_physics_software)

## Getting access to licensed codes

Many of the field's most important codes are free for research but require a signed agreement. This is normal, and turnaround is usually days to weeks. The front doors:

| Code | Where to ask | Notes |
|------|--------------|-------|
| GENE | [genecode.org](https://genecode.org) | Sign the user agreement on the website |
| TRANSP | [transp.pppl.gov](https://transp.pppl.gov) | Run as a service; request a PPPL account |
| OMFIT | [omfit.io](https://omfit.io) | Free registration form |
| SOLPS-ITER | [ITER Organization](https://www.iter.org/) | Distributed under ITER user agreement |
| GS2 / GX | [bitbucket.org/gyrokinetics](https://bitbucket.org/gyrokinetics/) | Request repository access |
| XGC | [xgc.pppl.gov](https://xgc.pppl.gov) | Request access from PPPL |
| M3D-C1 | [m3dc1.pppl.gov](https://m3dc1.pppl.gov) | Request access from PPPL |
| JOREK | [jorek.eu](https://www.jorek.eu) | Via consortium membership |
| NIMROD | [nimrodteam.org](https://nimrodteam.org) | Contact the NIMROD team |
| FISPACT-II | [fispact.ukaea.uk](https://fispact.ukaea.uk) | UKAEA license, free for academic use |
| Serpent | [serpent.vtt.fi](https://serpent.vtt.fi) | VTT license via national distribution centers |
| MCNP | [rsicc.ornl.gov](https://rsicc.ornl.gov) | Export-controlled; RSICC handles eligibility |

## Roadmap

This index is Phase 1 of the fusion-commons project:

- **Phase 1 — the index** (this repository): the definitive curated map of fusion software, data, and learning.
- **Phase 2 — the data registry**: a structured, DOI-indexed registry of open fusion datasets with machine-readable metadata.
- **Phase 3 — the fusion stack**: a one-command environment (Docker image + conda specification) that installs the open-source fusion toolchain, ready for a first simulation in minutes.

## Contributing

Additions and corrections are very welcome — this list gets better with every pair of eyes. See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format and quality bar. Every pull request is reviewed by a maintainer before merge.

## License

The contents of this list are licensed under [CC BY 4.0](LICENSE). Any code or scripts in this repository are licensed under Apache-2.0. The codes and datasets linked above carry their own licenses — always check before you build on them.
