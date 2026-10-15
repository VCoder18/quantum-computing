from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def run(qc, shots=1024, label=""):
    qc.measure_all()
    sampler = StatevectorSampler()
    counts = sampler.run([qc], shots=shots).result()[0].data.meas.get_counts()
    print(f"{label}: {counts}")
    return counts

qc = QuantumCircuit(2)
qc.x(0)
qc.cx(0, 1)
run(qc, label="X then CX")


qc = QuantumCircuit(2)
qc.x(0)
qc.h(1)
qc.cz(0, 1)
qc.h(1)
run(qc, label="X, H, CZ, H")


qc = QuantumCircuit(2)
qc.x(0)
qc.swap(0, 1)
run(qc, label="X then SWAP")


qc = QuantumCircuit(3)
qc.x(0)
qc.x(1)
qc.ccx(0, 1, 2)
run(qc, label="XX then CCX")


qc = QuantumCircuit(3)
qc.x(0)
qc.x(1)
qc.cswap(0, 1, 2)
run(qc, label="XX then CSWAP")