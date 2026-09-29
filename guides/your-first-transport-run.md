# Your first transport run

**Goal:** simulate five seconds of tokamak core plasma — temperature and density profiles evolving under heating and transport — with [TORAX](https://github.com/google-deepmind/torax), in about two seconds of wall-clock time.

**Time:** about 15 minutes. **Requirements:** Python 3.10–3.12 (TORAX's JAX dependency does not yet support the very newest Python).

## 1. Set up

```bash
python3.12 -m venv torax-env
source torax-env/bin/activate
pip install torax
```

## 2. Run

TORAX ships example configurations inside the package. Find the basic one and run it:

```bash
CFG=$(python -c "import torax, pathlib; print(pathlib.Path(torax.__file__).parent/'examples'/'basic_config.py')")
run_torax --config="$CFG" --quit
```

Expected output (timing varies by machine):

```
Simulating (t=5.00000): 100%|██████████| 100/100
Simulated 5.00s of physics in 1.82s of wall clock time.
Finished running simulation.
Wrote simulation output to /tmp/torax_results/state_history_<timestamp>.nc
```

That NetCDF file holds the full time history: temperatures, densities, current profile, and more.

## 3. Look at it

```bash
plot_torax --outfile /tmp/torax_results/state_history_<timestamp>.nc
```

(Use the actual filename from your run.)

## Where to go next

- Copy `basic_config.py` somewhere, edit the heating power or plasma current, and rerun — the config file is plain Python.
- The [TORAX documentation](https://torax.readthedocs.io) covers coupled transport equations, ML surrogates like QLKNN, and time-dependent scenarios.
- For whole-discharge analysis against real experimental data, the reference tool is [TRANSP](../README.md#integrated-modeling--systems-codes); for whole-plant design, try [FUSE](https://github.com/ProjectTorreyPines/FUSE.jl) or [Bluemira](https://github.com/Fusion-Power-Plant-Framework/bluemira).

---
*Every command and the expected output in this guide were run and verified on 2026-09-29 (macOS, Python 3.12, TORAX from PyPI).*
