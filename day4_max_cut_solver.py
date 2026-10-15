from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

def build_qaoa(edges, n, p, gammas, betas):
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
    return qc

def evaluate_cut(bitstring, edges):
    cut = 0
    for i, j in edges:
        bit_i = int(bitstring[-(i+1)])
        bit_j = int(bitstring[-(j+1)])
        if bit_i != bit_j:
            cut += 1
    return cut

def solve_maxcut(edges, n, p=2, num_samples=30):
    sampler = StatevectorSampler()
    best_cut = -1
    best_bitstring = None
    best_counts = None
    
    # Random parameter search
    for _ in range(num_samples):
        gammas = np.random.uniform(0, 2*np.pi, p)
        betas = np.random.uniform(0, 2*np.pi, p)
        
        qc = build_qaoa(edges, n, p, gammas, betas)
        counts = sampler.run([qc], shots=2048).result()[0].data.meas.get_counts()
        
        # Evaluate the most likely bitstring
        top_bitstring = max(counts, key=counts.get)
        cut = evaluate_cut(top_bitstring, edges)
        
        if cut > best_cut:
            best_cut = cut
            best_bitstring = top_bitstring
            best_counts = counts
    
    return best_cut, best_bitstring, best_counts

# --- Try it on a few graphs ---
graphs = {
    "Square + diagonal": ([(0,1),(1,2),(2,3),(3,0),(0,2)], 4),
    "Triangle": ([(0,1),(1,2),(0,2)], 3),
    "Pentagon": ([(0,1),(1,2),(2,3),(3,4),(4,0)], 5),
    "Complete graph K4": ([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], 4),
}

for name, (edges, n) in graphs.items():
    best_cut, best_bitstring, counts = solve_maxcut(edges, n, p=2)
    print(f"\n{name}:")
    print(f"  Best cut: {best_cut} / {len(edges)}")
    print(f"  Best bitstring: {best_bitstring}")
    print(f"  Top counts: {dict(sorted(counts.items(), key=lambda x: -x[1])[:5])}")