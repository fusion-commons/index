# The Fusion Commons

> Every code, dataset, and learning resource you need to work on fusion energy — in one place.

Fusion is being built in the open more than ever before: equilibrium solvers, gyrokinetic turbulence codes, neutronics toolchains, whole-plant systems codes, and open experimental data are all a `git clone` away — if you know where to look. The Fusion Commons is the map. It covers the software, the data, and the places to learn — across GitHub, GitLab, Bitbucket, and Hugging Face — with the license status of every entry marked, so you know what you can run today and what needs a signature first.

New to fusion computing? Start with the [hands-on guides](guides/) — a first equilibrium, a first transport run, and a first neutronics model, each in under an hour. For one picture of how it all fits together, see [the Open Fusion Software Map](site/map.svg).

This index is maintained as data: every entry lives in [`data/entries.yml`](data/entries.yml), and this page is generated from it. Additions and corrections are welcome from everyone — see [Contributing](#contributing).

Founded and maintained by [Kronos Fusion Energy](https://www.kronosfusionenergy.com).

## Legend

| Mark | Meaning |
|------|---------|
| 🟢 | Open source — clone and run today |
| 🟡 | Free for research, but requires registration or a signed user agreement |
| 🔴 | Restricted distribution (export-controlled or institution-only) |

Entries carry a short metadata tag — language, easiest install path (`pip`, `conda`, `source`, …), and the hosting platform when it isn't GitHub.

## Contents

- [Simulation codes](#simulation-codes)
  - [Plasma equilibrium & MHD](#plasma-equilibrium--mhd)
  - [Gyrokinetics, turbulence & transport](#gyrokinetics-turbulence--transport)
  - [Integrated modeling & systems codes](#integrated-modeling--systems-codes)
  - [Edge, scrape-off layer & divertor](#edge-scrape-off-layer--divertor)
  - [Disruptions & runaway electrons](#disruptions--runaway-electrons)
  - [Particle-in-cell & kinetic codes](#particle-in-cell--kinetic-codes)
  - [Stellarator design & optimization](#stellarator-design--optimization)
  - [Alternative concepts](#alternative-concepts)
  - [Heating, current drive & fast particles](#heating-current-drive--fast-particles)
  - [Neutronics, activation & shielding](#neutronics-activation--shielding)
  - [Materials & fuel cycle](#materials--fuel-cycle)
  - [Plant engineering & plasma-facing components](#plant-engineering--plasma-facing-components)
  - [Plasma control, machine learning & quantum](#plasma-control-machine-learning--quantum)
  - [Diagnostics & synthetic diagnostics](#diagnostics--synthetic-diagnostics)
  - [Inertial confinement & high-energy-density](#inertial-confinement--high-energy-density)
  - [General plasma frameworks & utilities](#general-plasma-frameworks--utilities)
- [Data](#data)
  - [Open experimental & simulation datasets](#open-experimental--simulation-datasets)
  - [Machine learning datasets & models](#machine-learning-datasets--models)
  - [Atomic, molecular & nuclear data](#atomic-molecular--nuclear-data)
  - [Standards & interoperability](#standards--interoperability)
- [Learning](#learning)
  - [Textbooks & foundational papers](#textbooks--foundational-papers)
  - [Courses, schools & lectures](#courses-schools--lectures)
  - [Hands-on workshops](#hands-on-workshops)
- [Community](#community)
  - [Regulation & policy](#regulation--policy)
  - [Organizations, news & sibling lists](#organizations-news--sibling-lists)
- [Getting access to licensed codes](#getting-access-to-licensed-codes)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

---

## Simulation codes

### Plasma equilibrium & MHD

- 🟢 [DESC](https://github.com/PlasmaControl/DESC) — Stellarator and tokamak equilibrium, stability, and optimization suite built on pseudo-spectral methods and automatic differentiation. `Python · pip`
- 🟢 [FreeGS](https://github.com/freegs-plasma/freegs) — Free-boundary Grad–Shafranov equilibrium solver for tokamaks, well suited to scenario design and control studies. `Python · pip`
- 🟢 [FreeGSNKE](https://github.com/FusionComputingLab/freegsnke) — Evolutive free-boundary Grad–Shafranov simulator from UKAEA, validated on MAST-U and a standard backend for control and surrogate training pipelines. `Python · pip`
- 🟢 [FreeQDSK](https://github.com/freegs-plasma/FreeQDSK) — Reader/writer for the G-EQDSK, A-EQDSK, and P-EQDSK equilibrium file formats. `Python · pip`
- 🟢 [GSFit](https://github.com/tokamak-energy/gsfit) — Grad–Shafranov equilibrium reconstruction open-sourced by Tokamak Energy, with a real-time sibling (RT-GSFit) running in the ST40 control system. `Rust/Python · source`
- 🟢 [GVEC](https://gitlab.mpcdf.mpg.de/gvec-group/gvec) — Galerkin Variational Equilibrium Code from Max Planck IPP — flexible open 3D ideal-MHD equilibrium solver in the VMEC lineage. `Fortran · source · GitLab`
- 🟢 [Open FUSION Toolkit](https://github.com/openfusiontoolkit/OpenFUSIONToolkit) — Suite of tools for fusion simulation, including the TokaMaker Grad–Shafranov solver and 3D MHD capabilities. `Fortran/Python · source`
- 🟢 [PARVMEC](https://github.com/ORNL-Fusion/PARVMEC) — Parallel version of the VMEC 3D ideal-MHD equilibrium code, the workhorse of stellarator equilibrium. `Fortran · source`
- 🟢 [SPEC](https://github.com/PrincetonUniversity/SPEC) — Stepped-Pressure Equilibrium Code — 3D MHD equilibria with islands and chaotic fields via multi-region relaxed MHD. `Fortran · source`
- 🟢 [VMEC++](https://github.com/proximafusion/vmecpp) — Proxima Fusion's from-scratch open reimplementation of the VMEC 3D MHD equilibrium code, built for modern stellarator optimization. `C++/Python · pip`
- 🟢 [VMEC2000](https://github.com/hiddenSymmetries/VMEC2000) — VMEC build with a Python wrapper and CMake tooling, maintained for the SIMSOPT optimization ecosystem. `Fortran/Python · source`
- 🟡 [EFIT](https://omfit.io/modules/mod_EFIT.html) — The standard tokamak equilibrium reconstruction code from General Atomics; commonly run through OMFIT. `Fortran`
- 🟡 [JOREK](https://www.jorek.eu) — Nonlinear extended-MHD code for disruptions, ELMs, and 3D instabilities in divertor tokamaks. `Fortran`
- 🟡 [M3D-C1](https://m3dc1.pppl.gov) — High-order 3D extended-MHD code from PPPL for tokamak stability and disruption modeling. `Fortran`
- 🟡 [NIMROD](https://nimrodteam.org) — Nonlinear 3D extended-MHD code used widely for macroscopic stability studies. `Fortran`

#### Choosing an equilibrium code

*Editorial guidance for newcomers — start here, then read each code's documentation.*

| Code | Geometry | First run | GPU | License |
|---|---|---|---|---|
| [FreeGS](https://github.com/freegs-plasma/freegs) | Tokamak (free boundary) | 🟩 pip install, laptop | — | 🟢 open |
| [DESC](https://github.com/PlasmaControl/DESC) | Stellarator + tokamak | 🟩 pip install, laptop | 🟩 (JAX) | 🟢 open |
| [TokaMaker (OFT)](https://github.com/openfusiontoolkit/OpenFUSIONToolkit) | Tokamak (free boundary) | 🟨 build from source | — | 🟢 open |
| [VMEC (PARVMEC / VMEC2000)](https://github.com/ORNL-Fusion/PARVMEC) | Stellarator + tokamak (nested surfaces) | 🟨 build from source | — | 🟢 open |
| [SPEC](https://github.com/PrincetonUniversity/SPEC) | Stellarator (islands & chaos) | 🟨 build from source | — | 🟢 open |
| [EFIT](https://omfit.io/modules/mod_EFIT.html) | Tokamak (reconstruction from experiment) | 🟨 via OMFIT | — | 🟡 registration |

### Gyrokinetics, turbulence & transport

- 🟢 [GACODE](https://github.com/gafusion/gacode) — General Atomics suite — CGYRO (gyrokinetic turbulence), TGLF (quasilinear transport), NEO (neoclassical), and TGYRO (transport solver). `Fortran · source`
- 🟢 [Gkeyll](https://github.com/ammarhakim/gkylzero) — Modern C/CUDA framework for gyrokinetic, Vlasov–Maxwell, and multi-moment fluid simulation on GPUs. `C · source`
- 🟢 [GKW](https://bitbucket.org/gkw/gkw/src) — Global and flux-tube nonlinear gyrokinetic code for turbulence in rotating plasmas. `Fortran · source · Bitbucket`
- 🟢 [Gyselalib++](https://github.com/gyselax/gyselalibxx) — Open GPU-ready semi-Lagrangian gyrokinetic library from CEA's GYSELA-X project. `C++ · source`
- 🟢 [QuaLiKiz](https://gitlab.com/qualikiz-group/QuaLiKiz) — Fast quasilinear gyrokinetic transport model, widely used inside integrated modeling loops and as a neural-network surrogate. `Fortran · source · GitLab`
- 🟢 [stella](https://github.com/stellaGK/stella) — Operator-split gyrokinetic code built for stellarator turbulence and mixed implicit/explicit timestepping. `Fortran · source`
- 🟡 [GENE](https://genecode.org) — Flagship Eulerian gyrokinetic turbulence code (flux-tube to global, tokamaks and stellarators); free after signing a user agreement. `Fortran`
- 🟡 [GS2](https://bitbucket.org/gyrokinetics/gs2) — Pioneering flux-tube gyrokinetic code for tokamak and stellarator microinstability and turbulence studies. `Fortran · Bitbucket`
- 🟡 [XGC](https://xgc.pppl.gov) — Whole-volume gyrokinetic particle-in-cell code for edge and core, scaling to exascale machines. `Fortran/C++`
- 🔴 [ORB5](https://orb5.epfl.ch) — Global electromagnetic gyrokinetic particle-in-cell code from EPFL's Swiss Plasma Center; source via collaboration agreement. `Fortran`

#### Choosing a gyrokinetic code

*Editorial guidance for newcomers — start here, then read each code's documentation.*

| Code | Geometry | Approach | GPU | License |
|---|---|---|---|---|
| [QuaLiKiz](https://gitlab.com/qualikiz-group/QuaLiKiz) | Tokamak | Quasilinear (fast, reduced) | — | 🟢 open |
| [CGYRO (GACODE)](https://github.com/gafusion/gacode) | Tokamak, flux tube | Eulerian, nonlinear | 🟩 | 🟢 open |
| [Gkeyll](https://github.com/ammarhakim/gkylzero) | Tokamak + mirror, incl. edge | Continuum, full-f capable | 🟩 | 🟢 open |
| [stella](https://github.com/stellaGK/stella) | Stellarator + tokamak | Eulerian, operator-split | — | 🟢 open |
| [GKW](https://bitbucket.org/gkw/gkw/src) | Tokamak, global + flux tube | Eulerian, nonlinear | — | 🟢 open |
| [GENE](https://genecode.org) | Tokamak + stellarator, global | Eulerian, nonlinear | 🟨 | 🟡 registration |
| [GS2](https://bitbucket.org/gyrokinetics/gs2) | Tokamak + stellarator, flux tube | Eulerian, nonlinear | — | 🟡 registration |
| [XGC](https://xgc.pppl.gov) | Whole volume, incl. edge | Particle-in-cell, full-f | 🟩 | 🟡 registration |

### Integrated modeling & systems codes

- 🟢 [Bluemira](https://github.com/Fusion-Power-Plant-Framework/bluemira) — Integrated design framework for fusion power plants — reactor geometry, magnets, balance of plant, and optimization. `Python · conda`
- 🟢 [cfspopcon](https://github.com/cfs-energy/cfspopcon) — Fast 0-D plasma operating-contour (POPCON) analysis from Commonwealth Fusion Systems. `Python · pip`
- 🟢 [FUSE](https://github.com/ProjectTorreyPines/FUSE.jl) — Whole-facility fusion simulator from General Atomics — plasma, engineering, and costing in one differentiable Julia stack. `Julia · julia`
- 🟢 [Kronos Toolkit](https://github.com/KronosFE/kronos-toolkit) — Anchor-tested Python research engine reproducing the published Kronos Fusion Energy physics register end-to-end ([PyPI](https://pypi.org/project/kronos-toolkit/)). `Python · pip`
- 🟢 [METIS](https://github.com/IRFM/METIS) — CEA-IRFM's fast integrated tokamak scenario and transport simulator, released under the CeCILL-C license. `MATLAB · source`
- 🟢 [MITIM](https://github.com/pabloprf/MITIM-fusion) — MIT integrated-modeling toolbox including PORTALS — surrogate-based optimization that accelerates high-fidelity core transport predictions. `Python · pip`
- 🟢 [PROCESS](https://github.com/ukaea/PROCESS) — UKAEA systems code for self-consistent fusion power plant design points and trade studies. `Python/Fortran · source`
- 🟢 [TORAX](https://github.com/google-deepmind/torax) — Differentiable tokamak core transport simulator in JAX from Google DeepMind, built for fast scenario optimization and ML coupling. `Python · pip`
- 🟡 [OMFIT](https://omfit.io) — One Modeling Framework for Integrated Tasks — the glue framework connecting dozens of fusion codes and experimental databases. `Python`
- 🟡 [TRANSP](https://transp.pppl.gov) — The reference tokamak time-dependent transport analysis and prediction code, run as a service by PPPL. `Fortran · service`

#### Choosing an integrated modeling or systems code

*Editorial guidance for newcomers — start here, then read each code's documentation.*

| Code | Scope | First run | Language | License |
|---|---|---|---|---|
| [cfspopcon](https://github.com/cfs-energy/cfspopcon) | 0-D operating space (POPCON) | 🟩 pip install, laptop | Python | 🟢 open |
| [TORAX](https://github.com/google-deepmind/torax) | 1-D core transport, differentiable | 🟩 pip install, laptop | Python | 🟢 open |
| [PROCESS](https://github.com/ukaea/PROCESS) | Whole-plant systems optimization | 🟨 build from source | Python/Fortran | 🟢 open |
| [Bluemira](https://github.com/Fusion-Power-Plant-Framework/bluemira) | Plant design & engineering | 🟨 conda environment | Python | 🟢 open |
| [FUSE](https://github.com/ProjectTorreyPines/FUSE.jl) | Whole facility, differentiable | 🟨 Julia package | Julia | 🟢 open |
| [OMFIT](https://omfit.io) | Framework gluing many codes | 🟨 registration | Python | 🟡 registration |
| [TRANSP](https://transp.pppl.gov) | Experiment analysis & prediction | 🟨 hosted service | Fortran | 🟡 registration |

### Edge, scrape-off layer & divertor

- 🟢 [BOUT++](https://github.com/boutproject/BOUT-dev) — Framework for plasma fluid and turbulence simulation in general curvilinear geometry, the base for many edge codes. `C++ · source`
- 🟢 [Hermes-3](https://github.com/boutproject/hermes-3) — Hot-ion multifluid drift-reduced model for tokamak edge and scrape-off-layer transport, built on BOUT++. `C++ · source`
- 🟢 [SD1D](https://github.com/boutproject/SD1D) — 1D divertor leg model of plasma–neutral interaction and detachment, built on BOUT++. `C++ · source`
- 🟢 [UEDGE](https://github.com/LLNL/UEDGE) — 2D fluid code for plasma and neutrals in the tokamak edge, from LLNL, with a Python interface. `Fortran/Python · pip`
- 🟡 [DEGAS 2](https://w3.pppl.gov/degas2/) — PPPL Monte Carlo neutral-transport code for fusion edge plasmas. `C`
- 🟡 [EIRENE](https://www.eirene.de) — Kinetic Monte Carlo neutral particle and radiation transport code, the neutrals engine inside SOLPS-ITER. `Fortran`
- 🟡 [GBS](https://gbs.epfl.ch) — EPFL's Global Braginskii Solver for edge and scrape-off-layer plasma turbulence in diverted geometries. `Fortran`
- 🟡 [SOLEDGE3X](https://soledge3x.com) — CEA-IRFM and Aix-Marseille edge-plasma transport and turbulence code including wall geometry, recycling, and impurity physics. `Fortran`
- 🟡 [SOLPS-ITER](https://www.iter.org/) — The standard coupled plasma/neutrals code package for divertor and scrape-off-layer design, maintained by the ITER Organization.

### Disruptions & runaway electrons

- 🟢 [DREAM](https://github.com/chalmersplasmatheory/DREAM) — Disruption Runaway Electron Analysis Model from Chalmers — the standard open tool for simulating runaway-electron generation and mitigation. `C++ · source`
- 🟢 [SOFT2](https://github.com/hoppe93/SOFT2) — Synthetic synchrotron diagnostic from Chalmers reproducing camera images and spectra of runaway-electron radiation. `C++ · source`

### Particle-in-cell & kinetic codes

- 🟢 [EPOCH](https://github.com/Warwick-Plasma/epoch) — Widely used relativistic particle-in-cell code for laser–plasma interaction and kinetic physics. `Fortran · source`
- 🟢 [OSIRIS](https://github.com/osiris-code/osiris) — The widely used UCLA/IST relativistic particle-in-cell code, historically agreement-only and now public under AGPL-3.0. `Fortran · source`
- 🟢 [PIConGPU](https://github.com/ComputationalRadiationPhysics/picongpu) — Fully relativistic, many-GPU particle-in-cell code with best-in-class performance. `C++ · source`
- 🟢 [Smilei](https://github.com/SmileiPIC/Smilei) — Collaborative open particle-in-cell code for fusion, laser–plasma, and astrophysical kinetic simulation. `C++/Python · source`
- 🟢 [VPIC](https://github.com/lanl/vpic) — Los Alamos 3D relativistic kinetic particle-in-cell code, built for extreme scale. `C++ · source`
- 🟢 [WarpX](https://github.com/BLAST-WarpX/warpx) — Exascale mesh-refined particle-in-cell code (2022 Gordon Bell Prize) for kinetic plasma and accelerator modeling. `C++/Python · conda`

### Stellarator design & optimization

- 🟢 [booz_xform](https://github.com/hiddenSymmetries/booz_xform) — Transforms stellarator equilibria to Boozer coordinates, with Python bindings. `C++/Python · pip`
- 🟢 [FOCUS](https://github.com/PrincetonUniversity/FOCUS) — Flexible optimized coil design using space curves — finds buildable coils for stellarators. `Fortran · source`
- 🟢 [Open stellarator models](https://github.com/proximafusion/open_stellarator_models) — Simplified stellarator CAD models published by Proxima Fusion as an open engineering and design resource.
- 🟢 [pyQSC](https://github.com/landreman/pyQSC) — Near-axis expansion for rapid design of quasisymmetric stellarator configurations. `Python · pip`
- 🟢 [REGCOIL](https://github.com/landreman/regcoil) — Regularized winding-surface coil optimization for stellarators. `Fortran · source`
- 🟢 [SIMSOPT](https://github.com/hiddenSymmetries/simsopt) — Flexible stellarator optimization framework tying together VMEC, SPEC, coil design, and gradient-based optimization. `Python/C++ · pip`
- 🟢 [STELLOPT](https://github.com/PrincetonUniversity/STELLOPT) — The classic stellarator equilibrium optimization suite, including BEAMS3D and DIAGNO. `Fortran · source`

### Alternative concepts

- 🟢 [MCTrans++](https://github.com/ianabel/MCTrans) — 0-D scoping model for transport in centrifugally confined magnetic mirrors, used for the CMFX experiment at the University of Maryland. `C++ · source`
- 🟢 [Pleiades](https://github.com/eepeterson/pleiades) — Green's-function equilibrium and coil-design code used to generate magnetic-mirror equilibria for the WHAM experiment. `Python · source`

*Kinetic FRC and Z-pinch studies in the open literature largely run on the particle-in-cell codes above (WarpX, Gkeyll), and the Open FUSION Toolkit descends from spheromak research — the entries here are concept-specific tools.*

### Heating, current drive & fast particles

- 🟢 [ASCOT5](https://github.com/ascot4fusion/ascot5) — High-performance Monte Carlo orbit-following code for fast ions, neutral-beam injection, and wall-load studies in tokamaks and stellarators. `C/Python · source`
- 🟢 [CQL3D](https://github.com/compxco/cql3d) — CompX's 3D Fokker–Planck collisional/quasilinear code for RF and neutral-beam heating, now openly published; the CQL3D-m variant serves mirror machines. `Fortran · source`
- 🟢 [GENRAY](https://github.com/compxco/genray) — All-frequencies ray-tracing code for RF wave propagation in plasmas, the standard companion to CQL3D. `Fortran · source`
- 🟢 [Petra-M](https://github.com/piScope/PetraM_Base) — Finite-element RF wave simulation framework (built on MFEM) used for ICRF antenna-to-core modeling. `Python · source`
- 🟢 [Scotty](https://github.com/beam-tracing/Scotty) — Beam-tracing code for Doppler backscattering and microwave beam propagation in fusion plasmas. `Python · pip`

### Neutronics, activation & shielding

- 🟢 [ALARA](https://github.com/svalinn/ALARA) — Activation, decay-heat, and dose analysis code designed for fusion energy systems. `C++ · source`
- 🟢 [DAGMC](https://github.com/svalinn/DAGMC) — Direct Accelerated Geometry Monte Carlo — run neutronics directly on CAD geometry with OpenMC, MCNP, and more. `C++ · conda`
- 🟢 [Geant4](https://geant4.web.cern.ch) — CERN's general-purpose particle transport toolkit, used for shielding and detector studies. `C++ · source`
- 🟢 [HYPERION activation study](https://github.com/KronosFE/hyperion-activation) — Worked open OpenMC R2S example — activation, waste classification, and shutdown dose for a breeder blanket. `Python · source`
- 🟢 [OpenMC](https://github.com/openmc-dev/openmc) — Community Monte Carlo neutron and photon transport code — the open standard for fusion neutronics. `C++/Python · conda`
- 🟢 [Paramak](https://github.com/fusion-energy/paramak) — Parametric CAD models of fusion reactors, ready for neutronics workflows. `Python · pip`
- 🟢 [PyNE](https://github.com/pyne/pyne) — Nuclear engineering toolkit — nuclear data, cross sections, transmutation, and mesh utilities. `Python/C++ · conda`
- 🟡 [FISPACT-II](https://fispact.ukaea.uk) — UKAEA inventory code for activation, transmutation, and waste — the fusion-standard companion to TENDL data. `Fortran`
- 🟡 [Serpent](https://serpent.vtt.fi) — Continuous-energy Monte Carlo transport and burnup code from VTT with strong fusion adoption. `C`
- 🔴 [MCNP](https://rsicc.ornl.gov) — The reference general Monte Carlo N-Particle transport code; export-controlled, distributed through RSICC. `Fortran`

### Materials & fuel cycle

- 🟢 [FESTIM](https://github.com/festim-dev/FESTIM) — Finite-element hydrogen/tritium transport in materials — trapping, permeation, and thermal fields. `Python · pip`
- 🟢 [LAMMPS](https://github.com/lammps/lammps) — Molecular dynamics workhorse for radiation damage and plasma-facing materials studies. `C++ · conda`
- 🟢 [MOOSE](https://github.com/idaholab/moose) — Idaho National Laboratory's multiphysics finite-element framework underlying many fusion materials and blanket tools. `C++ · conda`
- 🟢 [TMAP8](https://github.com/idaholab/TMAP8) — Tritium Migration Analysis Program, rebuilt on MOOSE — the standard for fuel-cycle tritium safety analysis. `C++ · source`
- 🟡 [SRIM](http://www.srim.org) — Stopping and Range of Ions in Matter — the classic ion-implantation and sputtering tables; free binaries, closed source. `binary`

### Plant engineering & plasma-facing components

- 🟢 [cfsem](https://github.com/cfs-energy/cfsem-py) — Commonwealth Fusion Systems' quasi-steady electromagnetics library — Biot–Savart, filamentized coils, and Grad–Shafranov utilities for tokamak design. `Rust/Python · pip`
- 🟢 [CoolProp](https://www.coolprop.org) — Open thermophysical property library covering cryogenic fluids such as helium and hydrogen; used in Bluemira's cryogenics and coolant calculations. `C++ · pip`
- 🟢 [GeN-Foam](https://gitlab.com/foam-for-nuclear/GeN-Foam) — OpenFOAM-based multiphysics solver for thermal-hydraulics, thermal-mechanics, and neutronics, relevant to balance-of-plant and liquid-metal blanket analysis. `C++ · source · GitLab`
- 🟢 [HEAT](https://github.com/plasmapotential/HEAT) — Heat flux Engineering Analysis Toolkit mapping 3D plasma heat and particle loads onto real CAD of plasma-facing components. `Python · source`
- 🟢 [Robinson HTS Wire Database](https://htsdb.wimbush.eu) — Open database of measured critical-current characteristics of commercial REBCO/HTS wires — a standard data source for fusion magnet conductor design.
- 🟢 [SMARDDA (smalib)](https://github.com/smardda/smalib) — UKAEA library for magnetic field-line following and power-deposition mapping onto CAD plasma-facing surfaces, the approach underlying ITER's SMITER framework. `Fortran · source`
- 🟢 [Stellarmesh](https://github.com/stellarmesh/stellarmesh) — CAD-to-DAGMC meshing library for neutronics workflows, originally from Thea Energy and now community-maintained. `Python · pip`
- 🟢 [Stellarvista](https://github.com/Thea-Energy/stellarvista) — Thea Energy's tool for in-notebook 3D visualization of DAGMC geometry and OpenMC tallies in stellarator neutronics workflows. `Python · pip`

### Plasma control, machine learning & quantum

- 🟢 [disruption-py](https://github.com/MIT-PSFC/disruption-py) — Open workflow from MIT PSFC for building disruption-prediction databases from tokamak shots. `Python · pip`
- 🟢 [DisruptionBench](https://github.com/MIT-PSFC/DisruptionBench) — Machine-agnostic benchmarking framework for ML disruption predictors across Alcator C-Mod, DIII-D, and EAST — the companion to disruption-py. `Python · source`
- 🟢 [FRNN](https://github.com/PPPLDeepLearning/plasma-python) — Fusion Recurrent Neural Network — deep learning for disruption prediction from PPPL. `Python · source`
- 🟢 [fusion_surrogates](https://github.com/google-deepmind/fusion_surrogates) — Google DeepMind's library of JAX surrogate transport models, including the QuaLiKiz-trained QLKNN networks used by TORAX. `Python · pip`
- 🟢 [fusion_tcv](https://github.com/google-deepmind/deepmind-research/tree/master/fusion_tcv) — Reference environment and agent-interface code from DeepMind's Nature 2022 deep-reinforcement-learning magnetic control of TCV plasmas. `Python · source`
- 🟢 [KODEX](https://github.com/KronosFE/kronos-ml) — The Kronos family of codes — a fleet of benchmarked AI/ML fusion surrogates and quantum tools spanning transport, magnet quench warning, disruption prediction, breeding, and control, each release archived with citable DOIs ([PyPI](https://pypi.org/project/kronos-fusion-ml/)). `Python · pip`
- 🟢 [kronos-quantum](https://github.com/KronosFE/kronos-quantum) — Runnable quantum-computing-for-fusion codes with a white paper — honest simulators today, pluggable into real quantum hardware as the field matures. `Python · source`
- 🟢 [mycela](https://github.com/firstlightfusion/mycela) — Distributed control-system framework and UI toolkit published by First Light Fusion from its experimental-controls stack. `Rust · source`
- 🟢 [TearingAvoidance](https://github.com/PlasmaControl/TearingAvoidance) — Training code for the Nature 2024 deep-RL tearing-instability avoidance controller demonstrated on DIII-D. `Python · source`
- 🟢 [TORAX](https://github.com/google-deepmind/torax) — Also listed under integrated modeling — its differentiability makes it a natural base for control and ML research. `Python · pip`

### Diagnostics & synthetic diagnostics

- 🟢 [Cherab](https://github.com/cherab/core) — Spectroscopic modeling framework for synthetic diagnostics, built on the Raysect ray-tracer. `Python · pip`
- 🟢 [FIDASIM](https://github.com/D3DEnergetic/FIDASIM) — Synthetic fast-ion D-alpha and neutral-beam diagnostic modeling. `Fortran · source`
- 🟢 [Raysect](https://github.com/raysect/source) — Scientific ray-tracing engine powering Cherab's synthetic camera and spectrometer views. `Python · pip`
- 🟢 [ToFu](https://github.com/ToFuProject/tofu) — Open library for tomography and synthetic diagnostics in fusion devices, used for bolometry and soft-X-ray inversion workflows. `Python · pip`

### Inertial confinement & high-energy-density

- 🟢 [Flash-X](https://flash-x.org) — Multiphysics adaptive-mesh radiation-hydrodynamics code with a long heritage in HED and laboratory astrophysics. `Fortran · source`
- 🟡 [FLASH](https://flash.rochester.edu) — Multiphysics radiation-MHD code from the Flash Center — a workhorse for magneto-inertial and magnetized HED fusion simulation. `Fortran`

*The production ICF radiation-hydrodynamics codes (HYDRA, xRAGE, and kin) are export-controlled and not publicly distributed; EPOCH, Smilei, and WarpX above cover much of the open kinetic side of HED science.*

### General plasma frameworks & utilities

- 🟢 [fusion-energy org](https://github.com/fusion-energy) — GitHub organization of open fusion neutronics tools and workflows surrounding OpenMC, DAGMC, and Paramak.
- 🟢 [MDSplus](https://github.com/MDSplus/mdsplus) — The data acquisition and storage system used by most magnetic fusion experiments worldwide. `C/Python · binary`
- 🟢 [MFEM](https://github.com/mfem/mfem) — Lightweight scalable finite-element library from LLNL, the numerical engine under several fusion codes. `C++ · conda`
- 🟢 [OMAS](https://github.com/gafusion/omas) — Ordered Multidimensional Array Structure — Python data-schema layer implementing the ITER IMAS ontology. `Python · pip`
- 🟢 [PlasmaPy](https://github.com/PlasmaPy/PlasmaPy) — The community Python package for plasma physics — formulary, particles, diagnostics, and simulation primitives. `Python · pip`
- 🟢 [Struphy](https://gitlab.mpcdf.mpg.de/struphy/struphy) — Structure-preserving hybrid kinetic-fluid plasma simulation package from Max Planck IPP. `Python · pip · GitLab`

## Data

### Open experimental & simulation datasets

- 🟢 [FAIR MAST](https://mastapp.site) — UKAEA's open data service for the MAST spherical tokamak — thousands of shots, browsable and downloadable ([API & code](https://github.com/ukaea/fair-mast)).
- 🟢 [IAEA Nuclear Data Services](https://www-nds.iaea.org) — The IAEA's portal of evaluated nuclear data libraries and related services.
- 🟢 [ITER Organization on GitHub](https://github.com/iterorganization) — ITER's open-source releases, including the IMAS data infrastructure and physics codes.
- 🟢 [OpenSTEP](https://github.com/ukaea/OpenSTEP) — Public data release of the STEP prototype fusion power plant tokamak design from UKAEA.
- 🟢 [SPARCPublic](https://github.com/cfs-energy/SPARCPublic) — Commonwealth Fusion Systems' public SPARC design data — equilibria, profiles, and reference scenarios.
- 🟢 [Zenodo — fusion energy records](https://zenodo.org/search?q=%22fusion%20energy%22) — CERN-hosted open repository where fusion datasets, code archives, and supplementary material receive citable DOIs; Kronos Fusion Energy's open research archive is published here.

### Machine learning datasets & models

- 🟢 [ConStellaration](https://huggingface.co/datasets/proxima-fusion/constellaration) — Proxima Fusion's open dataset of quasi-isodynamic stellarator boundaries with equilibria and performance metrics, the basis of an open optimization benchmark ([CoilStellaration companion](https://huggingface.co/datasets/proxima-fusion/coilstellaration)). `Hugging Face`
- 🟢 [Fusion Equilibrium Challenge](https://huggingface.co/datasets/Sophelio/fusion-equilibrium-challenge) — Challenge dataset for predicting plasma magnetic equilibrium from control inputs and non-magnetic diagnostics on DIII-D and MAST data. `Hugging Face`
- 🟢 [GyroSwin](https://huggingface.co/ml-jku/gyroswin_large) — Pretrained 5D neural surrogate for nonlinear gyrokinetic plasma turbulence, roughly a thousand times faster than the code it emulates. `Hugging Face`
- 🟢 [KBENCH](https://doi.org/10.5281/zenodo.22713389) — Open fusion-ML benchmark suite from the KODEX family — citable tasks on gyrokinetic turbulence, MAST disruption prediction, and flux reduced-order modeling, with fixed splits, metrics, and baselines to beat.
- 🟢 [NearAxisStellarators](https://huggingface.co/datasets/pedrocurvo/near-axis-stellarators) — Large dataset of stellarator configurations generated with the pyQSC near-axis expansion, pairing design parameters with derived properties for surrogate training. `Hugging Face`
- 🟢 [Pedestal Predictor](https://huggingface.co/SCS-Lab/pedestal-predictor-onnx) — DIII-D-trained ensemble predicting pedestal temperature, density, and rotation values, packaged as self-contained ONNX bundles for real-time inference. `Hugging Face`
- 🟢 [TokaMark](https://huggingface.co/datasets/UKAEA-IBM-STFC/tokamark-v1) — Benchmark packaging harmonized diagnostic signals from over ten thousand real MAST tokamak shots into task-ready evaluations for AI models. `Hugging Face`
- 🟢 [TokaMind](https://huggingface.co/UKAEA-IBM-STFC/tokamind-base-v2) — Multi-modal Transformer foundation model for tokamak plasma dynamics, pretrained on MAST data via TokaMark. `Hugging Face`

### Atomic, molecular & nuclear data

- 🟢 [ENDF/B (NNDC)](https://www.nndc.bnl.gov/endf/) — The US evaluated nuclear data file, from Brookhaven's National Nuclear Data Center.
- 🟢 [FENDL](https://www-nds.iaea.org/fendl/) — Fusion Evaluated Nuclear Data Library — the IAEA-curated nuclear data library for fusion neutronics.
- 🟢 [IAEA AMDIS](https://amdis.iaea.org) — Atomic and molecular data for fusion, including the ALADDIN database and CollisionDB.
- 🟢 [JEFF (OECD NEA)](https://www.oecd-nea.org/dbdata/jeff/) — The Joint Evaluated Fission and Fusion nuclear data library from the OECD Nuclear Energy Agency.
- 🟢 [NIST Atomic Spectra Database](https://physics.nist.gov/asd) — Reference wavelengths, energy levels, and transition probabilities.
- 🟢 [OPEN-ADAS](https://open.adas.ac.uk) — Freely downloadable subset of the Atomic Data and Analysis Structure — ionization, recombination, and radiation rates for fusion plasmas.
- 🟢 [TENDL](https://tendl.web.psi.ch/home.html) — TALYS-based evaluated nuclear data library, the standard companion to FISPACT-II activation calculations ([NEA Data Bank mirror](https://databank.io.oecd-nea.org/data/tendl/)).

### Standards & interoperability

- 🟢 [FreeQDSK](https://github.com/freegs-plasma/FreeQDSK) — The de-facto G-EQDSK equilibrium exchange format, implemented cleanly (also listed under equilibrium). `Python · pip`
- 🟢 [IMAS Data Dictionary](https://github.com/iterorganization/IMAS-Data-Dictionary) — The ITER-standard ontology for describing fusion experiments and simulations.
- 🟢 [IMAS-Python](https://github.com/iterorganization/IMAS-Python) — Pure-Python library for reading and writing IMAS data structures. `Python · pip`
- 🟢 [OMAS](https://github.com/gafusion/omas) — Practical Python implementation of the IMAS schema over NetCDF/HDF5/JSON (also listed under frameworks). `Python · pip`

## Learning

### Textbooks & foundational papers

- [Chen, "Introduction to Plasma Physics and Controlled Fusion"](https://link.springer.com/book/10.1007/978-3-319-22309-4) — The classic gentle introduction to plasma physics.
- [Dolan, "Magnetic Fusion Technology"](https://doi.org/10.1007/978-1-4471-5556-0) — Comprehensive reference on the engineering systems of magnetic fusion devices.
- [Freidberg, "Plasma Physics and Fusion Energy"](https://doi.org/10.1017/CBO9780511755705) — The standard first textbook for fusion-oriented plasma physics.
- [Miyamoto, "Plasma Physics and Controlled Nuclear Fusion"](https://doi.org/10.1007/3-540-28097-9) — Graduate text on plasma physics fundamentals for fusion.
- [Progress in the ITER Physics Basis](https://iopscience.iop.org/article/10.1088/0029-5515/47/6/S01) — The community-consensus physics basis for burning-plasma tokamaks, open access in Nuclear Fusion.
- [Stacey, "Fusion"](https://doi.org/10.1002/9783527629312) — Standard graduate textbook spanning the physics and technology of magnetic confinement fusion.
- [Wesson & Campbell, "Tokamaks"](https://global.oup.com/academic/product/tokamaks-9780198509226) — The encyclopedic reference on tokamak physics and engineering.

### Courses, schools & lectures

- [Culham Plasma Physics Summer School](https://culhamsummerschool.org.uk/) — UKAEA's two-week summer school in plasma physics and fusion, running since 1965.
- [DOE Fusion Energy Sciences](https://www.energy.gov/science/fes/fusion-energy-sciences) — Program overviews and primers from the US fusion science office.
- [EPFL Plasma Physics MOOC](https://www.edx.org/learn/physics/ecole-polytechnique-federale-de-lausanne-plasma-physics-introduction) — Introduction to plasma physics and fusion applications from EPFL's Swiss Plasma Center; free to audit on edX.
- [FuseNet](https://fusenet.eu/) — The European Fusion Education Network — master's programs, PhD events, internships, and teaching material.
- [ITER International School](https://www.iter.org/public/education/iter-international-school) — Annual themed school for young fusion scientists and engineers, organized by ITER and Aix-Marseille University.
- [MIT OCW 22.012 — Seminar. Fusion and Plasma Physics](https://ocw.mit.edu/courses/22-012-seminar-fusion-and-plasma-physics-spring-2006/) — Approachable seminar-style introduction to fusion from MIT.
- [MIT OCW 22.611J — Introduction to Plasma Physics I](https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/) — Full graduate course materials, free.
- [PPPL Graduate Summer School](https://gss.pppl.gov) — Annual one-week plasma physics school with archived lectures.

### Hands-on workshops

- 🟢 [Fusion Neutronics Workshop](https://github.com/fusion-energy/neutronics-workshop) — Self-paced Jupyter workshop covering OpenMC, DAGMC, and Paramak for fusion neutronics.
- 🟢 [PlasmaPy example gallery](https://docs.plasmapy.org/en/stable/examples.html) — Notebook examples for computational plasma physics in Python.

## Community

### Regulation & policy

- [CATF — Fusion Energy Regulation in the United States](https://www.catf.us/resource/fusion-energy-regulation-united-states-frameworks-licensing-deployment/) — Plain-language overview of US fusion licensing frameworks and deployment pathways from Clean Air Task Force.
- [NRC Regulatory Framework for Fusion Machines](https://www.federalregister.gov/documents/2026/02/26/2026-03865/regulatory-framework-for-fusion-machines) — The official US proposed rule regulating commercial fusion under the byproduct-material framework (10 CFR Part 30) rather than as fission reactors.
- [Towards Fusion Energy (UK government response)](https://assets.publishing.service.gov.uk/media/62b1f78a8fa8f53571e130c7/towards-fusion-energy-uk-government-response.pdf) — The UK's regulatory decision — the first country to legislate fusion-specific regulation, under the Environment Agency and HSE rather than nuclear site licensing.

### Organizations, news & sibling lists

- [ANS Fusion Energy Division](https://fed.ans.org/) — The American Nuclear Society's Fusion Energy Division, host of the biennial TOFE conference.
- [APS Division of Plasma Physics](https://engage.aps.org/dpp/home) — The main US plasma physics society and annual meeting.
- [EUROfusion](https://euro-fusion.org) — The European fusion research consortium.
- [Fusion Energy Base](https://www.fusionenergybase.com) — Tracking of fusion companies, projects, and technologies.
- [Fusion Industry Association](https://www.fusionindustryassociation.org) — The trade association of private fusion companies; publishes the annual industry report.
- [IAEA Fusion Portal](https://nucleus.iaea.org/sites/fusionportal/Pages/default.aspx) — The IAEA's fusion hub, including the Fusion Device Information System and Fusion Energy Conference materials.
- [ITER Newsline](https://www.iter.org/news) — News from the world's largest fusion project.
- [r/fusion](https://www.reddit.com/r/fusion/) — The main Reddit community for fusion energy discussion.
- [U.S. Fusion Energy](https://usfusionenergy.org/) — US fusion outreach and education hub with explainers, K-12 materials, news, and a careers portal.

*Live feeds of open fusion repositories: GitHub topics [nuclear-fusion](https://github.com/topics/nuclear-fusion) and [plasma-physics](https://github.com/topics/plasma-physics).*

*Sibling lists: [awesome-nuclear](https://github.com/paulromano/awesome-nuclear) · [awesome-ML-in-plasma-physics](https://github.com/kharitonov-ivan/awesome-ML-in-plasma-physics) · [List of plasma physics software (Wikipedia)](https://en.wikipedia.org/wiki/List_of_plasma_physics_software).*

## Getting access to licensed codes

Many of the field's most important codes are free for research but require a signed agreement. This is normal, and turnaround is usually days to weeks. The front doors:

| Code | How to get it |
|------|---------------|
| 🟡 [DEGAS 2](https://w3.pppl.gov/degas2/) | Complete the licensing form at w3.pppl.gov/degas2 |
| 🟡 [EFIT](https://omfit.io/modules/mod_EFIT.html) | Via General Atomics; commonly run through OMFIT |
| 🟡 [EIRENE](https://www.eirene.de) | Request from the EIRENE team at eirene.de |
| 🟡 [FISPACT-II](https://fispact.ukaea.uk) | UKAEA license, free for academic use |
| 🟡 [FLASH](https://flash.rochester.edu) | Register with the Flash Center at flash.rochester.edu |
| 🟡 [GBS](https://gbs.epfl.ch) | Request from EPFL's Swiss Plasma Center via gbs.epfl.ch |
| 🟡 [GENE](https://genecode.org) | Sign the user agreement at genecode.org |
| 🟡 [GS2](https://bitbucket.org/gyrokinetics/gs2) | Request access at bitbucket.org/gyrokinetics (also hosts GX) |
| 🟡 [JOREK](https://www.jorek.eu) | Via consortium membership at jorek.eu |
| 🟡 [M3D-C1](https://m3dc1.pppl.gov) | Request access from PPPL |
| 🟡 [NIMROD](https://nimrodteam.org) | Contact the NIMROD team |
| 🟡 [OMFIT](https://omfit.io) | Free registration form at omfit.io |
| 🟡 [Serpent](https://serpent.vtt.fi) | VTT license via national distribution centers |
| 🟡 [SOLEDGE3X](https://soledge3x.com) | On request via the contact address at soledge3x.com |
| 🟡 [SOLPS-ITER](https://www.iter.org/) | Distributed under ITER Organization user agreement |
| 🟡 [SRIM](http://www.srim.org) | Free binaries from srim.org (closed source) |
| 🟡 [TRANSP](https://transp.pppl.gov) | Run as a service; request a PPPL account |
| 🟡 [XGC](https://xgc.pppl.gov) | Request access from PPPL |
| 🔴 [MCNP](https://rsicc.ornl.gov) | Export-controlled; RSICC handles eligibility |
| 🔴 [ORB5](https://orb5.epfl.ch) | Via collaboration agreement with EPFL's Swiss Plasma Center |

## Roadmap

The Fusion Commons is built in phases, each useful on its own:

1. **The index** (this repository) — the definitive curated map of fusion software, data, and learning.
2. **The website** — a searchable, filterable edition of the index with live project-health information.
3. **The data registry** — a DOI-indexed registry of open fusion datasets with machine-readable metadata.
4. **The fusion stack** — a one-command environment (Docker image + conda specification) installing the open-source fusion toolchain.
5. **The runner** — a unified interface for chaining indexed codes into working pipelines: one input format in, one results format out.

## Contributing

Additions and corrections are very welcome — this map gets better with every pair of eyes.

- **Easiest:** [open an issue](https://github.com/fusion-commons/index/issues/new/choose) with the *Add a resource* template — maintainers do the rest.
- **Direct:** edit [`data/entries.yml`](data/entries.yml) and open a pull request; the README regenerates from it.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format and quality bar. Every pull request is reviewed by a maintainer before merge.

## Support

The Fusion Commons is free, forever. If it saves you time and you'd like to give something back, consider a gift to [The Elephant Sanctuary in Tennessee](https://www.elephants.com/donate) — this project's chosen cause. The ❤️ Sponsor button at the top of this page goes to the same place.

## License

The contents of this index are licensed under [CC BY 4.0](LICENSE). The build scripts in this repository are licensed under Apache-2.0. The codes and datasets linked above carry their own licenses — always check before you build on them.
