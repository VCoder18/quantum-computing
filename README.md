# quantum-computing

Python environment and starter programs for learning and experimenting with quantum
computing. Written against **Qiskit 2.x** and run on a local statevector simulator —
no IBM Quantum account, no API token, no queue. Every script is self-contained and
prints its results to stdout.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install "qiskit>=2.0" numpy matplotlib
```

Or just install into your current interpreter:

```bash
pip install "qiskit>=2.0" numpy matplotlib
```

Verified against Python 3.14.3 with qiskit 2.5.2, numpy 2.4.3, matplotlib 3.11.2.

> **Note on the parent folder.** This repo lives inside a directory tree that also
> contains an unrelated, unused Python virtualenv. That virtualenv is *not* this
> project's environment — ignore it entirely and create your own as shown above.

## Programs

| File | Demonstrates | Expected output |
| --- | --- | --- |
| `day1_bell.py` | H + CX to build a Bell pair, then measure | Counts containing only `00` and `11`, roughly 50/50 |
| `day2_gates.py` | Single-qubit gates: X, H, and the HZH / HSH / HTH phase kicks, plus Rx/Ry/Rz rotations | Counts per circuit showing how each gate moves the amplitudes |
| `day2_twoqubit.py` | Two- and three-qubit gates: CX, CZ (conjugated by H), SWAP, CCX, CSWAP | Counts confirming each classical truth table |
| `day3_grover.py` | Grover's search — oracle + diffusion operator, `round(π/4 · √2ⁿ)` iterations on 3 qubits | The target bitstring `101` dominates the counts |
| `day4_cost_layer.py` | The QAOA cost layer: CX-RZ-CX phase encoding over a graph's edges | Amplitude (phase) printed for each 4-qubit basis state |
| `day4_max_cut` | QAOA for Max-Cut at p=1 — brute-force grid search over γ and β | Best cut value found and the parameter pair that found it |
| `day4_max_cut_solver.py` | QAOA for Max-Cut at p=2 — random parameter search over four different graphs | Best cut per graph (square+diagonal, triangle, pentagon, K4) |
| `day4_simple_qaoa.py` | Parameterized QAOA circuit skeleton with symbolic γ/β parameters | The drawn circuit with parameterized rotation gates |

## Running

Run any script from the repository root:

```bash
python day1_bell.py
python day3_grover.py
```

Two notes:

- Several scripts call `plt.show()` at the end. On a headless machine set
  `MPLBACKEND=Agg` first, or add `import matplotlib; matplotlib.use("Agg")` before
  running.
- `day4_simple_qaoa.py` draws a circuit containing the Greek parameter names
  `γ` and `β`. On Windows the console defaults to a legacy code page that cannot
  encode them, and the draw step raises `UnicodeEncodeError`. Run it with
  `PYTHONUTF8=1` (or `chcp 65001`) to avoid that.

## Notes on the code

- `day4_max_cut` intentionally has no `.py` extension; it runs the same way
  (`python day4_max_cut`).
- Both Max-Cut scripts evaluate the cut by reading the measured bitstring in
  little-endian order, matching Qiskit's convention where qubit 0 is the
  rightmost character.
- The parameter search in `day4_max_cut` and `day4_max_cut_solver.py` is a plain
  random/grid search over the cost landscape, not a real classical optimizer. It
  is good enough to find a decent cut on small graphs but is not competitive with
  COBYLA or a gradient-based optimizer on larger ones.
