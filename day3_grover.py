from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

def grover_oracle(n, target):
    qc = QuantumCircuit(n)

    for i in range(n):
        if not (target >> i) & 1:
            qc.x(i)

    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    
    for i in range(n):
        if not (target >> i) & 1:
            qc.x(i)
    
    return qc

def diffusion_operator(n):
    
    qc = QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))
    
    return qc

def grover(n, target, iterations=None):
    if iterations is None:
        iterations = int(np.round(np.pi / 4 * np.sqrt(2**n)))
    
    qc = QuantumCircuit(n)
    qc.h(range(n))
    for _ in range(iterations):
        qc.compose(grover_oracle(n, target), inplace=True)
        qc.compose(diffusion_operator(n), inplace=True)
    qc.measure_all()
    return qc

n = 3
target = 5
qc = grover(n, target)
print(qc.draw("text"))

sampler = StatevectorSampler()
counts = sampler.run([qc], shots=1024).result()[0].data.meas.get_counts()
print(f"\nCounts: {counts}")

plot_histogram(counts)
plt.show()
        