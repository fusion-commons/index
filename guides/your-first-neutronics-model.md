# Your first neutronics model

**Goal:** build a tiny [OpenMC](https://github.com/openmc-dev/openmc) model — a sphere of lithium bombarded by 14 MeV fusion neutrons — and compute a tritium production rate, the quantity at the heart of every breeder blanket design.

**Time:** about 45 minutes, most of it the one-time nuclear data download. **Requirements:** conda or mamba ([miniforge](https://github.com/conda-forge/miniforge) is the easiest way to get one).

## 1. Set up

OpenMC installs from conda-forge (there are no pip wheels for every platform):

```bash
conda create -n neutronics -c conda-forge openmc
conda activate neutronics
```

Download a nuclear data library (one-time, a few GB). The official data page at [openmc.org](https://openmc.org) lists the options — ENDF/B-VIII.0 is the standard general-purpose choice, and [FENDL](https://www-nds.iaea.org/fendl/) is the fusion-specific library. After downloading, point OpenMC at it:

```bash
export OPENMC_CROSS_SECTIONS=/path/to/cross_sections.xml
```

## 2. Build and run

Save this as `first_neutronics.py`:

```python
import openmc

# Material: natural lithium, the classic breeder
lithium = openmc.Material(name="lithium")
lithium.add_element("Li", 1.0)
lithium.set_density("g/cm3", 0.534)

# Geometry: a 50 cm sphere of it
sphere = openmc.Sphere(r=50.0, boundary_type="vacuum")
cell = openmc.Cell(fill=lithium, region=-sphere)
model = openmc.Model()
model.geometry = openmc.Geometry([cell])
model.materials = [lithium]

# Source: 14.1 MeV point source — a D-T fusion neutron
source = openmc.IndependentSource()
source.energy = openmc.stats.Discrete([14.1e6], [1.0])
model.settings.source = source
model.settings.batches = 10
model.settings.particles = 10000
model.settings.run_mode = "fixed source"

# Tally: tritium production (the (n,Xt) reaction)
tally = openmc.Tally(name="tritium production")
tally.scores = ["(n,Xt)"]
model.tallies = [tally]

model.run()
```

Run it, then read the result:

```bash
python first_neutronics.py
openmc-statepoint-summary statepoint.10.h5 2>/dev/null || python -c "
import openmc
sp = openmc.StatePoint('statepoint.10.h5')
t = sp.get_tally(name='tritium production')
print(f'Tritium atoms produced per source neutron: {t.mean.item():.3f}')"
```

A value near or above 1.0 tritons per neutron is why lithium blankets can breed their own fuel — and why real designs add neutron multipliers to push it higher.

## Where to go next

- The [Fusion Neutronics Workshop](https://github.com/fusion-energy/neutronics-workshop) is the definitive self-paced course — tokamak geometries, breeding blankets, dose maps, all in notebooks.
- [Paramak](https://github.com/fusion-energy/paramak) generates parametric reactor CAD, and [DAGMC](https://github.com/svalinn/DAGMC) lets OpenMC run directly on it.
- For activation and shutdown dose after irradiation, see [ALARA](https://github.com/svalinn/ALARA) and the worked [HYPERION activation study](https://github.com/KronosFE/hyperion-activation).

---
*This guide follows the official OpenMC install and quickstart documentation (conda-forge route); the model script uses the standard OpenMC Python API. Unlike the other two guides, it was not executed on the maintainers' machine — no conda toolchain there — so treat the expected number as indicative and the [official docs](https://docs.openmc.org) as authoritative.*
