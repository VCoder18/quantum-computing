from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4

p = 1
gammas = [Parameter(f"γ{i}") for i in range(p)]
betas = [Parameter(f"β{i}") for i in range(p)]

qc = QuantumCircuit(n)

qc.h(range(n))

for layer in range(p):
    for i, j in edges:
        qc.cx(i, j)
        qc.rz(2 * gammas[layer], j)
        qc.cx(i, j)
    for i in range(n):
        qc.rx(2 * betas[layer], i)

qc.measure_all()
print(qc.draw("text"))