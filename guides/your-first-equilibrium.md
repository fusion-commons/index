# Your first equilibrium

**Goal:** solve a free-boundary tokamak equilibrium — the magnetic configuration that holds a plasma in place — on your laptop with [FreeGS](https://github.com/freegs-plasma/freegs).

**Time:** about 15 minutes. **Requirements:** Python 3.10–3.12 (the released FreeGS needs NumPy 1.x, which is why we pin it below).

## 1. Set up

```bash
python3.12 -m venv fusion-env
source fusion-env/bin/activate
pip install freegs "numpy<2" matplotlib
```

## 2. Solve

Save this as `first_equilibrium.py`:

```python
import freegs

# A test tokamak with poloidal field coils
tokamak = freegs.machine.TestTokamak()

# The computational domain
eq = freegs.Equilibrium(tokamak=tokamak,
                        Rmin=0.1, Rmax=2.0,
                        Zmin=-1.0, Zmax=1.0,
                        nx=65, ny=65)

# Plasma profiles: pressure on axis 1 kPa, plasma current 200 kA
profiles = freegs.jtor.ConstrainPaxisIp(eq, 1e3, 2e5, 2.0)

# Shape constraints: an upper and lower X-point
constrain = freegs.control.constrain(xpoints=[(1.1, -0.6), (1.1, 0.6)],
                                     isoflux=[(1.1, -0.6, 1.1, 0.6)])

# Solve the free-boundary Grad-Shafranov equation
freegs.solve(eq, profiles, constrain)

print(f"Plasma current: {eq.plasmaCurrent() / 1e3:.1f} kA")
print(f"Poloidal beta:  {eq.poloidalBeta():.3f}")
```

Run it:

```bash
python first_equilibrium.py
```

Expected output (an initial "No O points found" warning before the solve is normal):

```
Plasma current: 200.0 kA
Poloidal beta:  0.027
```

You just solved the Grad–Shafranov equation — the same calculation, at heart, that every tokamak control room does between shots.

## 3. Look at it

Add these lines to plot the flux surfaces, coils, and separatrix:

```python
from freegs.plotting import plotEquilibrium
plotEquilibrium(eq)
```

## Where to go next

- Change the X-point positions and target current and watch the shape respond.
- FreeGS's [documentation](https://freegs.readthedocs.io) covers real machine geometries.
- Ready for experiment-grade reconstruction? That's [EFIT's](../README.md#plasma-equilibrium--mhd) job; for stellarators, start with [DESC](https://github.com/PlasmaControl/DESC).

---
*Every command and the expected output in this guide were run and verified on 2026-09-29 (macOS, Python 3.12, FreeGS from PyPI).*
